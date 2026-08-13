"""End-to-end orchestration for two-stage LLM pipeline.

Coordinates Stage 1 (video → memory) and Stage 2 (memory → device automation)
in a single unified workflow using a shared config.yml file.

Usage:
  python -m src_llm.pipeline --config src_llm/input/config.yml --env-file .env.local
  python -m src_llm.pipeline --config src_llm/input/config.yml --env-file .env.local --stage 1
  python -m src_llm.pipeline --config src_llm/input/config.yml --env-file .env.local --dry-run
"""

import argparse
import logging
import sys
import time
from pathlib import Path
from typing import Literal

from src_llm import main as stage1_main
from src_llm import automate as stage2_automate


def _parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        prog="python -m src_llm.pipeline",
        description="Run complete two-stage LLM pipeline: Stage 1 (video→memory) + Stage 2 (memory→device)",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("src_llm/input/config.yml"),
        help="Path to unified config.yml (used by both stages, default: src_llm/input/config.yml)",
    )
    parser.add_argument(
        "--env-file",
        type=Path,
        default=Path(".env.local"),
        help="Path to .env file with provider credentials",
    )
    parser.add_argument(
        "--stage",
        type=int,
        choices=[1, 2],
        default=None,
        help="Run only stage 1 or 2 (default: both in sequence)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate config/env without processing (skips video analysis and device automation)",
    )
    parser.add_argument(
        "--skip-apk-install",
        action="store_true",
        help="Stage 2 only: skip APK install and launch; automate from the current device screen",
    )
    return parser.parse_args()


def _setup_logger() -> logging.Logger:
    """Set up pipeline-level logger."""
    logger = logging.getLogger("src_llm.pipeline")
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "[%(levelname)s] %(asctime)s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger


def run_stage1(config_path: Path, env_file: Path, dry_run: bool, logger: logging.Logger) -> int:
    """Run Stage 1: Video → Memory generation.

    Args:
        config_path: Path to config.yml
        env_file: Path to .env file
        dry_run: Skip actual processing
        logger: Logger instance

    Returns:
        0 on success, non-zero on failure
    """
    logger.info("=" * 60)
    logger.info("STAGE 1: Video → Memory Generation")
    logger.info("=" * 60)

    stage1_args = argparse.Namespace(
        config=config_path,
        env_file=env_file,
        dry_run=dry_run,
    )

    try:
        result = stage1_main.main(stage1_args)
        if result == 0:
            logger.info("✓ Stage 1 complete")
        else:
            logger.error("✗ Stage 1 failed with code %d", result)
        return result
    except Exception as exc:
        logger.error("Stage 1 failed with exception: %s", exc, exc_info=True)
        return 1


def run_stage2(
    config_path: Path,
    env_file: Path,
    dry_run: bool,
    logger: logging.Logger,
    skip_apk_install: bool = False,
) -> int:
    """Run Stage 2: Memory → Device Automation.

    Args:
        config_path: Path to config.yml
        env_file: Path to .env file
        dry_run: Skip actual processing
        logger: Logger instance

    Returns:
        0 on success, non-zero on failure
    """
    logger.info("=" * 60)
    logger.info("STAGE 2: Memory → Device Automation")
    logger.info("=" * 60)

    stage2_args = [
        "--config",
        str(config_path),
        "--env-file",
        str(env_file),
    ]
    if dry_run:
        stage2_args.append("--dry-run")
    if skip_apk_install:
        stage2_args.append("--skip-apk-install")

    try:
        result = stage2_automate.main(stage2_args)
        if result == 0:
            logger.info("✓ Stage 2 complete")
        else:
            logger.error("✗ Stage 2 failed with code %d", result)
        return result
    except Exception as exc:
        logger.error("Stage 2 failed with exception: %s", exc, exc_info=True)
        return 1


def main(argv: list[str] | None = None) -> int:
    """Run complete pipeline: Stage 1 → Stage 2 (or individual stages).

    Args:
        argv: Command-line arguments (default: sys.argv[1:])

    Returns:
        0 on success, non-zero on failure
    """
    args = _parse_args() if argv is None else argparse.ArgumentParser().parse_args(argv)
    logger = _setup_logger()

    logger.info("Starting two-stage LLM pipeline")
    logger.info("Config: %s", args.config)
    logger.info("Env file: %s", args.env_file)
    if args.dry_run:
        logger.info("Mode: DRY-RUN (no actual processing)")
    if args.skip_apk_install:
        logger.info("Stage 2 mode: skip APK install and launch")
    logger.info("Stages: %s", f"Stage {args.stage}" if args.stage else "1 → 2")

    if not args.config.exists():
        logger.error("Config file not found: %s", args.config)
        return 1

    if not args.env_file.exists():
        logger.error("Env file not found: %s", args.env_file)
        return 1

    pipeline_start = time.perf_counter()
    overall_status = 0

    try:
        # Stage 1: Video → Memory
        if args.stage is None or args.stage == 1:
            stage1_start = time.perf_counter()
            result = run_stage1(args.config, args.env_file, args.dry_run, logger)
            stage1_duration = time.perf_counter() - stage1_start
            logger.info("Stage 1 duration: %.1f seconds", stage1_duration)

            if result != 0:
                logger.error("Pipeline aborted: Stage 1 failed")
                return result

            # Only proceed to Stage 2 if Stage 1 succeeded and we're not running stage-only
            if args.stage is not None:
                return 0

        # Stage 2: Memory → Device Automation
        if args.stage is None or args.stage == 2:
            stage2_start = time.perf_counter()
            result = run_stage2(
                args.config,
                args.env_file,
                args.dry_run,
                logger,
                skip_apk_install=args.skip_apk_install,
            )
            stage2_duration = time.perf_counter() - stage2_start
            logger.info("Stage 2 duration: %.1f seconds", stage2_duration)

            if result != 0:
                logger.error("Pipeline aborted: Stage 2 failed")
                overall_status = result

        pipeline_duration = time.perf_counter() - pipeline_start
        logger.info("=" * 60)
        if overall_status == 0:
            logger.info("✓ Pipeline complete (%.1f seconds total)", pipeline_duration)
            if args.dry_run:
                logger.info("Dry-run OK for Stage 1 and Stage 2")
        else:
            logger.error("✗ Pipeline failed")

        return overall_status

    except KeyboardInterrupt:
        logger.warning("Pipeline interrupted by user")
        return 1
    except Exception as exc:
        logger.error("Pipeline failed with exception: %s", exc, exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
