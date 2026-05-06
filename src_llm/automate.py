"""CLI entry point for video-guided device automation.

Usage:
    python -m src_llm.automate \\
        --config src_llm/input/automation_config.yml \\
        --env-file .env.local
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import re
import sys
import time
from pathlib import Path


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="python -m src_llm.automate",
        description="Video-guided Android UI automation via LLM + uiautomator2",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("src_llm/input/automation_config.yml"),
        help="Path to automation_config.yml (default: src_llm/input/automation_config.yml)",
    )
    parser.add_argument("--env-file", type=Path, default=None, help="Path to .env file")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate config and imports then exit without running automation",
    )
    return parser.parse_args(argv)


def _normalize_model_slug(model_str: str) -> str:
    """Normalize model name to lowercase with hyphens and dots.
    e.g., 'Gemini-2.5-Pro' -> 'gemini-2.5-pro'
    """
    normalized = re.sub(r"[^a-z0-9.-]+", "-", model_str.lower()).strip("-")
    return normalized if normalized else "model"


def _locate_latest_run(app_name: str, llm_model: str, video_type: str) -> Path:
    """Locate the latest Stage 1 run for an app+model+video_type combination.

    Searches: apps/<app>/llm/<model>/<video_type>-video-mode/run-*/
    Returns: Path to run directory (e.g., apps/adaway/llm/gemini-2.5-pro/screenrec-video-mode/run-001)
    Raises: FileNotFoundError if no run found
    """
    model_slug = _normalize_model_slug(llm_model)
    source = "handheld" if video_type == "hhv" else "screenrec"
    source_dir = f"{source}-video-mode"

    base = Path("apps") / app_name / "llm" / model_slug / source_dir
    if not base.exists():
        raise FileNotFoundError(
            f"No Stage 1 runs found for {app_name} | {model_slug} | {source_dir}\n"
            f"Expected path: {base}\n"
            f"Make sure to run Stage 1 (src_llm.main) first with video_mode=true"
        )

    existing = sorted(base.glob("run-*"), key=lambda p: int(p.name[4:]))
    if not existing:
        raise FileNotFoundError(f"No numbered runs in {base}")

    return existing[-1]


def _load_run_metadata(run_dir: Path) -> dict:
    """Load metadata.json from a completed Stage 1 run.

    Returns: dict with keys like video_mode_metadata, task_description, etc.
    """
    metadata_path = run_dir / "metadata.json"
    if not metadata_path.exists():
        raise FileNotFoundError(
            f"metadata.json not found in {run_dir}\n"
            f"Expected path: {metadata_path}"
        )

    with metadata_path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _resolve_output_dir(run, llm: str, llm_model: str) -> Path:
    """Return the output dir for a run, auto-deriving if not set in config.

    Auto-derived path (flat structure):
        apps/<app>/llm/<model>/<video_type>-video-mode/run-<NNN>

    model slug includes provider info (e.g., 'gemini-2.5-pro')
    """
    if run.output_dir is not None:
        return run.output_dir

    model_slug = _normalize_model_slug(llm_model)
    source = "handheld" if run.video_type == "hhv" else "screenrec"
    source_dir = f"{source}-video-mode"

    base = Path("apps") / run.app_name / "llm" / model_slug / source_dir
    existing = sorted(base.glob("run-*"), key=lambda p: int(p.name[4:])) if base.exists() else []
    next_idx = len(existing) + 1
    return base / f"run-{next_idx:03d}"


def _log_run_stats(logger: logging.Logger, run, trace: dict, output_dir: Path, provider, wall_sec: float) -> None:
    """Emit a structured stats block at the end of each run."""
    from collections import Counter

    steps = trace.get("steps") or []
    action_counts = Counter(s.get("action", {}).get("type", "unknown") for s in steps)
    actions_str = "  ".join(f"{k}={v}" for k, v in sorted(action_counts.items())) or "none"

    llm_calls = getattr(provider, "llm_calls", [])
    if llm_calls:
        latencies = [c["elapsed_sec"] for c in llm_calls]
        total_prompt = sum(c["prompt_tokens"] for c in llm_calls)
        total_output = sum(c["output_tokens"] for c in llm_calls)
        from collections import Counter as _C
        calls_by_kind = _C(c["kind"] for c in llm_calls)
        calls_str = "  ".join(f"{k}={v}" for k, v in sorted(calls_by_kind.items()))
        lat_str = (
            f"min={min(latencies):.1f}s  max={max(latencies):.1f}s  "
            f"avg={sum(latencies)/len(latencies):.1f}s  total={sum(latencies):.1f}s"
        )
        tokens_str = (
            f"prompt={total_prompt:,}  output={total_output:,}  "
            f"total={total_prompt + total_output:,}"
        )
    else:
        calls_str = lat_str = tokens_str = "n/a"

    sep = "=" * 72
    logger.info(sep)
    logger.info("RUN SUMMARY")
    logger.info("  App         : %s", run.app_name)
    logger.info("  Video type  : %s", run.video_type)
    logger.info("  Status      : %s", trace.get("status", "unknown"))
    logger.info("  Steps       : %d", trace.get("total_steps", 0))
    logger.info("  Actions     : %s", actions_str)
    logger.info("  LLM calls   : %s", calls_str)
    logger.info("  LLM latency : %s", lat_str)
    logger.info("  Tokens used : %s", tokens_str)
    logger.info("  Wall time   : %dm %ds", int(wall_sec) // 60, int(wall_sec) % 60)
    logger.info("  Output      : %s", output_dir)
    logger.info(sep)


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

    # --- Pre-flight: verify required files exist before touching the device ---
    missing = []
    if not run.apk_path.exists():
        missing.append(f"APK not found: {run.apk_path}")
    if not run.video_path.exists():
        missing.append(f"Video not found: {run.video_path}")
    if missing:
        for msg in missing:
            logger.warning("SKIP run — %s", msg)
        logger.warning("Skipping run: app=%s video_type=%s", run.app_name, run.video_type)
        if file_handler is not None:
            logger.removeHandler(file_handler)
            file_handler.close()
        return None

    run_start = time.perf_counter()

    # --- Create provider ---
    from src_llm.providers import create_provider

    provider = create_provider(run.llm, run.llm_model, env, logger=logger, video_mode=True)

    # --- Connect device + install APK ---
    from src_llm.device import DeviceController

    device = DeviceController()
    device.connect(serial=run.device_serial)

    logger.info("Installing APK: %s", run.apk_path)
    pkg = device.install_apk(run.apk_path)
    logger.info("APK installed: %s", pkg)

    from src_llm.apk_utils import extract_main_activity

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

    # --- Locate and load prior Stage 1 run memory ---
    memory_md_content = None
    task_description = ""
    try:
        prior_run_dir = _locate_latest_run(run.app_name, run.llm_model, run.video_type)
        logger.info("Located prior Stage 1 run: %s", prior_run_dir)

        prior_metadata = _load_run_metadata(prior_run_dir)
        video_mode_metadata = prior_metadata.get("video_mode_metadata", {})
        memory_md_content = video_mode_metadata.get("memory_md_content")
        task_description = video_mode_metadata.get("task_description", "")

        if not memory_md_content:
            logger.error("No memory.md content found in prior run metadata")
            return None

        logger.info("Loaded memory.md from prior Stage 1 run | task_desc_len=%d", len(task_description))
    except FileNotFoundError as exc:
        logger.error("Failed to locate prior Stage 1 run: %s", exc)
        return None

    # --- Run automation with memory context ---
    from src_llm.automation import run_automation

    trace = run_automation(
        task_description=task_description,
        provider=provider,
        device=device,
        max_steps=run.max_steps,
        output_dir=output_dir,
        history_window=run.history_window,
        step_delay=run.step_delay,
        stall_repeat_threshold=run.stall_repeat_threshold,
        logger=logger,
        memory_content=memory_md_content,
    )

    logger.info(
        "Run complete: app=%s video_type=%s steps=%d status=%s",
        run.app_name, run.video_type, trace["total_steps"], trace["status"],
    )
    logger.info("Session trace: %s", output_dir / "session_trace.json")

    if run.reset_between_runs:
        logger.info("Resetting app state: force-stop + clear data | pkg=%s", pkg)
        device.reset_app(pkg)
        logger.info("App reset complete: %s", pkg)

    from src_llm.replay_writer import write_replay_script

    replay_path = write_replay_script(
        output_dir=output_dir,
        trace=trace,
        apk_path=run.apk_path,
        package=pkg,
        activity=activity,
        device_serial=run.device_serial,
    )
    logger.info("Replay script: %s", replay_path)

    _log_run_stats(logger, run, trace, output_dir, provider, time.perf_counter() - run_start)

    if file_handler is not None:
        logger.removeHandler(file_handler)
        file_handler.close()

    return trace


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)

    log_level = os.environ.get("DEBUG") and logging.DEBUG or logging.INFO
    logging.basicConfig(
        level=log_level,
        format="[%(levelname)s] %(asctime)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        stream=sys.stderr,
    )
    logger = logging.getLogger("src_llm.automate")
    if log_level == logging.DEBUG:
        logger.info("DEBUG mode enabled")

    # --- Load config ---
    from src_llm.config import load_automation_config, ConfigError

    try:
        cfg = load_automation_config(args.config)
    except ConfigError as exc:
        logger.error("Config error: %s", exc)
        return 1

    # --- Load environment ---
    from src_llm.env_loader import load_and_validate_env

    env = load_and_validate_env(args.env_file, cfg.llm) if args.env_file else {}

    logger.info("Loaded %d run(s) from config", len(cfg.runs))

    if args.dry_run:
        try:
            from src_llm.providers import create_provider  # noqa: F401
            from src_llm.device import DeviceController  # noqa: F401
            from src_llm.automation import run_automation  # noqa: F401
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
