from __future__ import annotations

import argparse
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    from src_ViBR.config import ConfigError, ViBRRunConfig, load_config
    from src_ViBR.io_utils import PathError, create_output_layout, detect_video_source, write_json
    from src_ViBR.logging_utils import finalize_log_file, setup_logger
except ModuleNotFoundError:
    from config import ConfigError, ViBRRunConfig, load_config
    from io_utils import PathError, create_output_layout, detect_video_source, write_json
    from logging_utils import finalize_log_file, setup_logger


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run ViBR from a YAML config with multi-run support.")
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("src_ViBR/input/config.yml"),
        help="Path to YAML config file.",
    )
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Pass interactive mode to segment_replay (OpenCV windows + pauses).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate config and path resolution without running replay.",
    )
    return parser.parse_args()


def _resolve_video(project_root: Path, run_cfg: ViBRRunConfig) -> Path:
    return run_cfg.video_path if run_cfg.video_path.is_absolute() else (project_root / run_cfg.video_path)


def _detect_project_root() -> Path:
    # Resolve repository root relative to this file so paths stay correct
    # even when launched from src_ViBR/ instead of repo root.
    return Path(__file__).resolve().parent.parent


def _find_groundingdino_dir(project_root: Path) -> Path | None:
    candidates = [
        project_root / "GroundingDINO",
        project_root / "src_ViBR" / "GroundingDINO",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return None


def _stream_subprocess_to_logger(cmd: list[str], cwd: Path, logger) -> int:
    process = subprocess.Popen(
        cmd,
        cwd=str(cwd),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
        env=os.environ.copy(),
    )
    assert process.stdout is not None
    for line in process.stdout:
        logger.info(line.rstrip("\n"))
    process.wait()
    return process.returncode


def run_single(project_root: Path, run_cfg: ViBRRunConfig, log_level: str, interactive: bool, dry_run: bool) -> int:
    resolved_video = _resolve_video(project_root, run_cfg)
    source = detect_video_source(resolved_video)
    run_dt = datetime.now(timezone.utc)
    layout = create_output_layout(project_root, run_cfg.app_name, source, run_dt)

    layout.run_dir.mkdir(parents=True, exist_ok=True)
    (layout.run_dir / "logs").mkdir(parents=True, exist_ok=True)
    layout.artifacts_dir.mkdir(parents=True, exist_ok=True)

    logger = setup_logger(layout.log_file_path, log_level)
    status = "failed"
    started = datetime.now(timezone.utc)

    try:
        if not resolved_video.exists():
            raise FileNotFoundError(f"Video file not found: {resolved_video}")

        logger.info("Starting ViBR run")
        logger.info("App: %s", run_cfg.app_name)
        logger.info("Video: %s", resolved_video)
        logger.info("Algorithm: %s", run_cfg.algorithm)
        logger.info("Output: %s", layout.run_dir)

        if dry_run:
            logger.info("Dry-run completed successfully")
            status = "success"
            return 0

        dino_root = _find_groundingdino_dir(project_root)
        if dino_root is None:
            raise FileNotFoundError(
                "GroundingDINO not found. Checked:\n"
                f"- {project_root / 'GroundingDINO'}\n"
                f"- {project_root / 'src_ViBR' / 'GroundingDINO'}\n"
                "Clone https://github.com/IDEA-Research/GroundingDINO and install it."
            )

        cmd = [
            sys.executable,
            str(project_root / "src_ViBR" / "approach" / "segment_replay.py"),
            str(resolved_video),
            run_cfg.algorithm,
            "--output-root",
            str(layout.artifacts_dir),
        ]
        if interactive:
            cmd.append("--interactive")

        rc = _stream_subprocess_to_logger(cmd, project_root, logger)
        if rc != 0:
            raise RuntimeError(f"segment_replay failed with exit code {rc}")

        status = "success"
        return 0
    finally:
        duration_sec = (datetime.now(timezone.utc) - started).total_seconds()
        write_json(
            layout.metadata_path,
            {
                "app": run_cfg.app_name.lower(),
                "method": "llm",
                "variant": "ViBR",
                "source": source,
                "video": str(resolved_video),
                "algorithm": run_cfg.algorithm,
                "run_id": layout.run_id,
                "timestamp": run_dt.strftime("%Y-%m-%dT%H:%M:%S"),
                "duration_sec": round(duration_sec, 1),
                "status": status,
            },
        )
        for handler in list(logger.handlers):
            handler.close()
            logger.removeHandler(handler)
        finalize_log_file(layout.log_file_path, status)


def main() -> int:
    args = parse_args()
    cfg = load_config(args.config)
    project_root = _detect_project_root()

    if len(cfg.runs) > 1:
        print(f"[src_ViBR] Running {len(cfg.runs)} configured runs")

    exit_code = 0
    for idx, run_cfg in enumerate(cfg.runs, start=1):
        print(f"[src_ViBR] --- Run {idx}/{len(cfg.runs)}: {run_cfg.app_name} ({run_cfg.video_path}) ---")
        rc = run_single(project_root, run_cfg, cfg.logging.level, args.interactive, args.dry_run)
        if rc != 0:
            exit_code = rc

    return exit_code


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ConfigError, PathError, FileNotFoundError, RuntimeError) as exc:
        print(f"[src_ViBR] ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
