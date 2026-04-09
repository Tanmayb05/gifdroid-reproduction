"""CLI entry point for video-guided device automation (Milestone 4).

Usage:
    python -m gifdroid_llm.automate \\
        --video apps/adaway/videos/screenrec/srv-001.mp4 \\
        --apk apps/adaway/adaway.apk \\
        --config gifdroid_llm/input/automation_config.yml \\
        --env-file .env.local
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="python -m gifdroid_llm.automate",
        description="Video-guided Android UI automation via LLM + uiautomator2",
    )
    parser.add_argument("--video", type=Path, help="Path to the demo video (.mp4)")
    parser.add_argument("--apk", type=Path, help="Path to the APK to install")
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("gifdroid_llm/input/automation_config.yml"),
        help="Path to automation_config.yml",
    )
    parser.add_argument("--env-file", type=Path, default=None, help="Path to .env file")
    parser.add_argument(
        "--task",
        default="",
        help="Plain-text description of the task to perform (overrides config)",
    )
    parser.add_argument(
        "--max-steps",
        type=int,
        default=None,
        help="Maximum automation steps (overrides config)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Directory to write session trace and screenshots (overrides config)",
    )
    parser.add_argument(
        "--device-serial",
        default=None,
        help="ADB device serial (overrides config; omit to auto-detect)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate config and imports then exit without running automation",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)

    # --- Logging setup ---
    logging.basicConfig(
        level=logging.INFO,
        format="[%(levelname)s] %(message)s",
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

    # CLI flags override config
    video_path = args.video or cfg.video_path
    apk_path = args.apk or cfg.apk_path
    task_description = args.task or ""
    max_steps = args.max_steps if args.max_steps is not None else cfg.max_steps
    output_dir = args.output_dir or cfg.output_dir
    device_serial = args.device_serial or cfg.device_serial

    logger.info("Loaded video: %s", video_path)
    logger.info("APK: %s", apk_path)
    logger.info("Output dir: %s", output_dir)
    logger.info("Max steps: %d", max_steps)

    if args.dry_run:
        # Validate that all imports work and paths exist
        if not video_path.exists():
            logger.error("Video not found: %s", video_path)
            return 1
        if not apk_path.exists():
            logger.error("APK not found: %s", apk_path)
            return 1
        try:
            from gifdroid_llm.providers import create_provider  # noqa: F401
            from gifdroid_llm.device import DeviceController  # noqa: F401
            from gifdroid_llm.automation import run_automation  # noqa: F401
        except ImportError as exc:
            logger.error("Import error: %s", exc)
            return 1
        print("Dry-run OK")
        return 0

    # --- Create provider ---
    from gifdroid_llm.providers import create_provider

    provider = create_provider(cfg.llm, cfg.llm_model, env, logger=logger)

    # --- Install APK and connect device ---
    from gifdroid_llm.device import DeviceController

    device = DeviceController()
    device.connect(serial=device_serial)

    logger.info("Installing APK: %s", apk_path)
    pkg = device.install_apk(apk_path)
    logger.info("APK installed: %s", pkg)

    from gifdroid_llm.apk_utils import extract_main_activity

    activity = extract_main_activity(apk_path)
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

    import time
    time.sleep(2)

    logger.info("App launched: %s", device.get_current_activity())

    # --- Run automation ---
    from gifdroid_llm.automation import run_automation

    trace = run_automation(
        video_path=video_path,
        task_description=task_description,
        provider=provider,
        device=device,
        max_steps=max_steps,
        output_dir=output_dir,
        history_window=cfg.history_window,
        step_delay=cfg.step_delay,
        logger=logger,
    )

    logger.info(
        "Session complete: %d steps, status=%s",
        trace["total_steps"],
        trace["status"],
    )

    trace_path = output_dir / "session_trace.json"
    logger.info("Session trace written: %s", trace_path)

    # Print summary to stdout
    print(json.dumps({
        "status": trace["status"],
        "total_steps": trace["total_steps"],
        "video_summary": trace.get("video_summary", ""),
        "session_trace": str(trace_path),
    }, indent=2))

    return 0


if __name__ == "__main__":
    sys.exit(main())
