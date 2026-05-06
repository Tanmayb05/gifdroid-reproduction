"""End-to-end orchestration of Stage 1 (video_to_memory) → Stage 2 (memory_to_device).

This module runs both stages in sequence using a unified config file.

Usage:
    # Run both stages in sequence
    python -m src_llm.end_to_end --config src_llm/input/config.yml --env-file .env.local

    # Run only Stage 1
    python -m src_llm.end_to_end --config src_llm/input/config.yml --env-file .env.local --stage 1

    # Run only Stage 2
    python -m src_llm.end_to_end --config src_llm/input/config.yml --env-file .env.local --stage 2

    # Dry-run both stages
    python -m src_llm.end_to_end --config src_llm/input/config.yml --env-file .env.local --dry-run
"""
from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="python -m src_llm.end_to_end",
        description="End-to-end workflow: analyze video → automate on device",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("src_llm/input/config.yml"),
        help="Path to config.yml (used by both stages)",
    )
    parser.add_argument(
        "--env-file",
        type=Path,
        default=Path(".env.local"),
        help="Path to .env file with provider credentials",
    )
    parser.add_argument(
        "--stage",
        choices=["1", "2", "all"],
        default="all",
        help="Which stage(s) to run: 1=video_to_memory, 2=memory_to_device, all=both (default: all)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate config without executing",
    )
    return parser.parse_args(argv)


def _run_stage_1(config_path: Path, env_file: Path, dry_run: bool) -> int:
    """Run Stage 1: video_to_memory."""
    from src_llm import video_to_memory

    argv = [
        "--config",
        str(config_path),
        "--env-file",
        str(env_file),
    ]
    if dry_run:
        argv.append("--dry-run")

    return video_to_memory.main(argv)


def _run_stage_2(config_path: Path, env_file: Path, dry_run: bool) -> int:
    """Run Stage 2: memory_to_device."""
    from src_llm import memory_to_device

    argv = [
        "--config",
        str(config_path),
        "--env-file",
        str(env_file),
    ]
    if dry_run:
        argv.append("--dry-run")

    return memory_to_device.main(argv)


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)

    log_level = logging.INFO
    logging.basicConfig(
        level=log_level,
        format="[%(levelname)s] %(asctime)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        stream=sys.stderr,
    )
    logger = logging.getLogger("src_llm.end_to_end")

    logger.info("=== End-to-End Workflow Orchestrator ===")
    logger.info("Config: %s", args.config)
    logger.info("Stages: %s", args.stage)

    # Validate config file exists
    if not args.config.exists():
        logger.error("Config file not found: %s", args.config)
        return 1

    exit_code = 0

    # Stage 1: video_to_memory
    if args.stage in ("1", "all"):
        logger.info("\n=== STAGE 1: video_to_memory ===")
        logger.info("Analyzing video and generating memory.md")
        code = _run_stage_1(args.config, args.env_file, args.dry_run)
        if code != 0:
            logger.error("Stage 1 failed with exit code %d", code)
            exit_code = code
            if args.stage == "1":
                return exit_code
        else:
            logger.info("✓ Stage 1 complete")

    # Stage 2: memory_to_device
    if args.stage in ("2", "all"):
        logger.info("\n=== STAGE 2: memory_to_device ===")
        logger.info("Automating on device using memory from Stage 1")
        code = _run_stage_2(args.config, args.env_file, args.dry_run)
        if code != 0:
            logger.error("Stage 2 failed with exit code %d", code)
            exit_code = code
        else:
            logger.info("✓ Stage 2 complete")

    if exit_code == 0:
        logger.info("\n=== End-to-End Workflow Complete ===")
    else:
        logger.error("\n=== End-to-End Workflow Failed ===")

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
