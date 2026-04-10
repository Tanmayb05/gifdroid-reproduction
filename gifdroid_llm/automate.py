"""CLI entry point for video-guided device automation.

Usage:
    python -m gifdroid_llm.automate \\
        --config gifdroid_llm/input/automation_config.yml \\
        --env-file .env.local
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
import time
from pathlib import Path


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="python -m gifdroid_llm.automate",
        description="Video-guided Android UI automation via LLM + uiautomator2",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("gifdroid_llm/input/automation_config.yml"),
        help="Path to automation_config.yml (default: gifdroid_llm/input/automation_config.yml)",
    )
    parser.add_argument("--env-file", type=Path, default=None, help="Path to .env file")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate config and imports then exit without running automation",
    )
    return parser.parse_args(argv)


def _resolve_output_dir(run, llm: str, llm_model: str) -> Path:
    """Return the output dir for a run, auto-deriving if not set in config.

    Auto-derived path:
        apps/<app>/llm/<provider>/<model>/<video_type>/run-<NNN>
    """
    if run.output_dir is not None:
        return run.output_dir

    base = Path("apps") / run.app_name / "llm" / llm / llm_model / run.video_type
    existing = sorted(base.glob("run-*")) if base.exists() else []
    next_idx = len(existing) + 1
    return base / f"run-{next_idx:03d}"


def _run_single(run, env: dict, logger: logging.Logger, dry_run: bool) -> dict | None:
    """Execute one automation run. Returns the trace dict or None on dry-run."""
    output_dir = _resolve_output_dir(run, run.llm, run.llm_model)

    # Attach a per-run file handler so logs are saved alongside run outputs.
    file_handler: logging.FileHandler | None = None
    if not dry_run:
        log_dir = output_dir / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_dir / "automate.log", encoding="utf-8")
        file_handler.setFormatter(logging.Formatter(
            "[%(levelname)s] %(asctime)s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        ))
        logger.addHandler(file_handler)

    logger.info(
        "--- Run: app=%s video_type=%s video=%s ---",
        run.app_name, run.video_type, run.video_path,
    )
    logger.info("Output dir: %s", output_dir)

    if dry_run:
        if not run.video_path.exists():
            logger.error("Video not found: %s", run.video_path)
            return None
        if not run.apk_path.exists():
            logger.error("APK not found: %s", run.apk_path)
            return None
        return {}

    # --- Create provider ---
    from gifdroid_llm.providers import create_provider

    provider = create_provider(run.llm, run.llm_model, env, logger=logger, video_mode=True)

    # --- Connect device + install APK ---
    from gifdroid_llm.device import DeviceController

    device = DeviceController()
    device.connect(serial=run.device_serial)

    logger.info("Installing APK: %s", run.apk_path)
    pkg = device.install_apk(run.apk_path)
    logger.info("APK installed: %s", pkg)

    from gifdroid_llm.apk_utils import extract_main_activity

    activity = extract_main_activity(run.apk_path)
    if activity:
        logger.info("Launching app: %s / %s", pkg, activity)
        device.launch_app(pkg, activity)
    else:
        logger.info("Launching app: %s (no main activity found, using monkey)", pkg)
        import subprocess
        subprocess.run(
            ["adb", "shell", "monkey", "-p", pkg, "-c", "android.intent.category.LAUNCHER", "1"],
            check=True,
        )

    time.sleep(2)
    logger.info("App launched: %s", device.get_current_activity())

    # --- Run automation ---
    from gifdroid_llm.automation import run_automation

    trace = run_automation(
        video_path=run.video_path,
        task_description="",
        provider=provider,
        device=device,
        max_steps=run.max_steps,
        output_dir=output_dir,
        history_window=run.history_window,
        step_delay=run.step_delay,
        logger=logger,
    )

    logger.info(
        "Run complete: app=%s video_type=%s steps=%d status=%s",
        run.app_name, run.video_type, trace["total_steps"], trace["status"],
    )
    logger.info("Session trace: %s", output_dir / "session_trace.json")

    from gifdroid_llm.replay_writer import write_replay_script

    replay_path = write_replay_script(
        output_dir=output_dir,
        trace=trace,
        apk_path=run.apk_path,
        package=pkg,
        activity=activity,
        device_serial=run.device_serial,
    )
    logger.info("Replay script: %s", replay_path)
    logger.info("=" * 72)

    if file_handler is not None:
        logger.removeHandler(file_handler)
        file_handler.close()

    return trace


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)

    logging.basicConfig(
        level=logging.INFO,
        format="[%(levelname)s] %(asctime)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        stream=sys.stderr,
    )
    logger = logging.getLogger("gifdroid_llm.automate")

    # --- Load config ---
    from gifdroid_llm.config import load_automation_config, ConfigError

    try:
        cfg = load_automation_config(args.config)
    except ConfigError as exc:
        logger.error("Config error: %s", exc)
        return 1

    # --- Load environment ---
    from gifdroid_llm.env_loader import load_and_validate_env

    env = load_and_validate_env(args.env_file, cfg.llm) if args.env_file else {}

    logger.info("Loaded %d run(s) from config", len(cfg.runs))

    if args.dry_run:
        try:
            from gifdroid_llm.providers import create_provider  # noqa: F401
            from gifdroid_llm.device import DeviceController  # noqa: F401
            from gifdroid_llm.automation import run_automation  # noqa: F401
        except ImportError as exc:
            logger.error("Import error: %s", exc)
            return 1
        ok = True
        for run in cfg.runs:
            result = _run_single(run, env, logger, dry_run=True)
            if result is None:
                ok = False
        if ok:
            print("Dry-run OK")
        return 0 if ok else 1

    # --- Execute all runs ---
    summaries = []
    for run in cfg.runs:
        trace = _run_single(run, env, logger, dry_run=False)
        if trace is not None:
            summaries.append({
                "app": run.app_name,
                "video_type": run.video_type,
                "status": trace["status"],
                "total_steps": trace["total_steps"],
                "video_summary": trace.get("video_summary", ""),
            })

    print(json.dumps(summaries, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
