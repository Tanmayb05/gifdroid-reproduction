"""CLI entry point for memory-guided device automation (Stage 2).

Uses pre-generated memory from Stage 1 (video_to_memory) to automate on device.

Usage:
    python -m src_llm.memory_to_device \\
        --config src_llm/input/config.yml \\
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
        prog="python -m src_llm.memory_to_device",
        description="Memory-guided Android UI automation via LLM + uiautomator2",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("src_llm/input/config.yml"),
        help="Path to config.yml (default: src_llm/input/config.yml)",
    )
    parser.add_argument("--env-file", type=Path, default=None, help="Path to .env file")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate config and imports then exit without running automation",
    )
    parser.add_argument(
        "--skip-apk-install",
        action="store_true",
        help="Skip APK install and app launch; start automation from the current device screen",
    )
    return parser.parse_args(argv)


def _normalize_model_slug(model_str: str) -> str:
    """Normalize model name to lowercase with hyphens and dots.
    e.g., 'Gemini-2.5-Pro' -> 'gemini-2.5-pro'
    """
    normalized = re.sub(r"[^a-z0-9.-]+", "-", model_str.lower()).strip("-")
    return normalized if normalized else "model"


def _run_number(run_dir: Path) -> int:
    match = re.match(r"^run-(\d+)$", run_dir.name)
    return int(match.group(1)) if match else -1


def _runs_with_metadata(run_parent: Path) -> list[Path]:
    return [
        p for p in sorted(run_parent.glob("run-*"), key=_run_number)
        if (p / "metadata.json").exists()
    ]


def _locate_latest_run(app_name: str, llm_model: str, video_path: Path) -> Path:
    """Locate the latest Stage 1 run for this exact app+model+video.

    Searches: apps/<app>/llm/<video-stem>-<model>-vm/run-*/
    Only returns runs with metadata.json (Stage 1 outputs), skipping Stage 2 device-automation dirs.
    Returns: Path to run directory (e.g., apps/bakerspercentagecalculator/llm/srv-002-gemini-2.5-pro-vm/run-001)
    Raises: FileNotFoundError if no run found
    """
    model_slug = _normalize_model_slug(llm_model)
    video_stem = video_path.stem
    video_name = video_path.name
    llm_base = Path("apps") / app_name / "llm"

    if not llm_base.exists():
        raise FileNotFoundError(
            f"No Stage 1 runs found for {app_name} | {model_slug} | {video_name}\n"
            f"Expected path: {llm_base}\n"
            f"Make sure to run Stage 1 (src_llm.main) first with video_mode=true"
        )

    exact_parent = llm_base / f"{video_stem}-{model_slug}-vm"
    exact_runs = _runs_with_metadata(exact_parent) if exact_parent.exists() else []
    if exact_runs:
        return sorted(exact_runs, key=lambda p: (_run_number(p), p.stat().st_mtime))[-1]

    # Fallback for older/renamed layouts: scan same-model dirs, but only accept metadata
    # for the exact configured video filename.
    matching_runs = []
    for run_parent in llm_base.glob(f"*-{model_slug}-vm"):
        for run_dir in _runs_with_metadata(run_parent):
            try:
                metadata = _load_run_metadata(run_dir)
            except (OSError, json.JSONDecodeError):
                continue
            if metadata.get("video") == video_name:
                matching_runs.append(run_dir)

    if not matching_runs:
        raise FileNotFoundError(
            f"No Stage 1 runs with metadata.json found for {app_name} | {model_slug} | {video_name}\n"
            f"Expected path: {exact_parent}/run-*/metadata.json\n"
            f"Make sure to run Stage 1 for this exact video first with video_mode=true"
        )

    return sorted(matching_runs, key=lambda p: (_run_number(p), p.stat().st_mtime))[-1]


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


def _resolve_output_dir(run, llm: str, llm_model: str, prior_stage1_run: Path | None = None) -> Path:
    """Return the output dir for a run, auto-deriving if not set in config.

    For Stage 2 (device automation), uses the prior Stage 1 run directory to co-locate outputs.
    This prevents Stage 2 from creating new run-NNN directories that would interfere with
    subsequent Stage 1 → Stage 2 workflows.

    Auto-derived path (Stage 2):
        apps/<app>/llm/<model>/<video_type>-video-mode/run-<NNN>/device-automation/

    model slug includes provider info (e.g., 'gemini-2.5-pro')
    """
    if run.output_dir is not None:
        return run.output_dir

    # If prior Stage 1 run provided, use it as base (Stage 2 case)
    if prior_stage1_run is not None:
        return prior_stage1_run / "device-automation"

    # Otherwise, create new run-NNN directory (Stage 1 case, not used in Stage 2)
    model_slug = _normalize_model_slug(llm_model)
    source = "handheld" if run.video_type == "handheld" else "screenrec"
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


def _run_single(
    run,
    env: dict,
    logger: logging.Logger,
    dry_run: bool,
    skip_apk_install: bool = False,
) -> dict | None:
    """Execute one automation run. Returns the trace dict or None on dry-run."""
    skip_apk_install = skip_apk_install or run.skip_apk_install
    # --- Locate prior Stage 1 run FIRST (before creating output dir) ---
    prior_stage1_run = None
    memory_md_content = None
    task_description = ""

    if not dry_run:
        try:
            prior_stage1_run = _locate_latest_run(run.app_name, run.llm_model, run.video_path)
            logger.info("Located prior Stage 1 run: %s", prior_stage1_run)

            prior_metadata = _load_run_metadata(prior_stage1_run)
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

    # Now resolve output directory (uses prior_stage1_run if provided)
    output_dir = _resolve_output_dir(run, run.llm, run.llm_model, prior_stage1_run)

    # Attach a per-run file handler to the whole src_llm logger tree so
    # device/provider/automation logs are saved alongside run outputs.
    file_handler: logging.FileHandler | None = None
    file_logger: logging.Logger | None = None
    file_logger_level: int | None = None
    if not dry_run:
        log_dir = output_dir / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_dir / "automate.log", encoding="utf-8")
        file_handler.setFormatter(logging.Formatter(
            "[%(levelname)s] %(asctime)s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        ))
        file_logger = logging.getLogger("src_llm")
        file_logger_level = file_logger.level
        file_logger.setLevel(min(logger.getEffectiveLevel(), logging.INFO))
        file_logger.addHandler(file_handler)

    logger.info(
        "--- Run: app=%s video_type=%s video=%s ---",
        run.app_name, run.video_type, run.video_path,
    )
    logger.info("Output dir: %s", output_dir)

    if dry_run:
        # Note: Stage 2 doesn't need the video file; memory is already generated in Stage 1
        if not skip_apk_install and not run.apk_path.exists():
            logger.error("APK not found: %s", run.apk_path)
            return None
        return {}

    # --- Pre-flight: verify required files exist before touching the device ---
    # Note: Stage 2 doesn't need the video file; memory is already generated in Stage 1
    missing = []
    if not skip_apk_install and not run.apk_path.exists():
        missing.append(f"APK not found: {run.apk_path}")
    if missing:
        for msg in missing:
            logger.warning("SKIP run — %s", msg)
        logger.warning("Skipping run: app=%s video_type=%s", run.app_name, run.video_type)
        if file_handler is not None:
            if file_logger is not None:
                file_logger.removeHandler(file_handler)
                if file_logger_level is not None:
                    file_logger.setLevel(file_logger_level)
            file_handler.close()
        return None

    run_start = time.perf_counter()

    # --- Create provider ---
    from src_llm.providers import create_provider

    provider = create_provider(run.llm, run.llm_model, env, logger=logger, video_mode=True)

    # --- Connect device + optionally install/launch APK ---
    from src_llm.device import DeviceController

    device = DeviceController()
    device.connect(serial=run.device_serial)

    pkg = None
    activity = None

    if skip_apk_install:
        logger.info(
            "Skipping APK install and launch; starting automation from current device screen"
        )
        if run.apk_path.exists():
            try:
                from src_llm.apk_utils import extract_main_activity, extract_package_name

                pkg = extract_package_name(run.apk_path)
                activity = extract_main_activity(run.apk_path)
                logger.info("Resolved package from APK metadata for replay: %s", pkg)
            except Exception as exc:
                logger.warning("Could not resolve package metadata from APK: %s", exc)
        try:
            current_activity = device.get_current_activity()
            logger.info("Current device activity: %s", current_activity or "unknown")
        except Exception as exc:
            logger.warning("Could not read current device activity: %s", exc)
    else:
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

    if run.reset_between_runs and skip_apk_install:
        logger.info("Skipping app reset because skip_apk_install uses a manually prepared screen")
    elif run.reset_between_runs and pkg:
        logger.info("Resetting app state: force-stop + clear data | pkg=%s", pkg)
        device.reset_app(pkg)
        logger.info("App reset complete: %s", pkg)
    elif run.reset_between_runs:
        logger.info("Skipping app reset because no package name is available")

    if pkg:
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
    else:
        logger.info("Skipping replay script because no package name is available")

    _log_run_stats(logger, run, trace, output_dir, provider, time.perf_counter() - run_start)

    if file_handler is not None:
        if file_logger is not None:
            file_logger.removeHandler(file_handler)
            if file_logger_level is not None:
                file_logger.setLevel(file_logger_level)
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
            result = _run_single(
                run,
                env,
                logger,
                dry_run=True,
                skip_apk_install=args.skip_apk_install,
            )
            if result is None:
                ok = False
        if ok:
            print("Dry-run OK")
        return 0 if ok else 1

    # --- Execute all runs ---
    summaries = []
    for run in cfg.runs:
        trace = _run_single(
            run,
            env,
            logger,
            dry_run=False,
            skip_apk_install=args.skip_apk_install,
        )
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
