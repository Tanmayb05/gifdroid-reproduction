from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import List

from gifdroid_llm_trace.config import AppConfig, ConfigError, load_config
from gifdroid_llm_trace.env_loader import EnvError, load_and_validate_env
from gifdroid_llm_trace.io_utils import (
    PathError,
    create_output_layout,
    resolve_video_path,
    write_json,
)
from gifdroid_llm_trace.keyframes import KeyframeSelector
from gifdroid_llm_trace.logging_utils import setup_logger
from gifdroid_llm_trace.providers import ProviderError, create_provider
from gifdroid_llm_trace.trace import TraceAction, TraceBuilder, TraceStep
from gifdroid_llm_trace.video import VideoError, VideoFrameExtractor


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate an LLM-based execution trace from a bug video."
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("gifdroid_llm_trace/input/config.yml"),
        help="Path to YAML config file.",
    )
    parser.add_argument(
        "--env-file",
        type=Path,
        default=Path(".env.local"),
        help="Path to .env file with provider credentials.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate config/env and output paths without processing video.",
    )
    return parser.parse_args()


def ensure_write_policy(cfg: AppConfig, execution_json_path: Path, keyframes_dir: Path) -> None:
    if cfg.output.overwrite:
        return
    if execution_json_path.exists():
        raise FileExistsError(
            f"Output exists and overwrite=false: {execution_json_path}"
        )
    if keyframes_dir.exists() and any(keyframes_dir.iterdir()):
        raise FileExistsError(
            f"Keyframes directory is not empty and overwrite=false: {keyframes_dir}"
        )


def run_pipeline(args: argparse.Namespace) -> int:
    project_root = Path.cwd()

    cfg = load_config(args.config)
    resolved_video_path, video_type = resolve_video_path(project_root, cfg)
    if not resolved_video_path.exists():
        raise VideoError(
            f"Video file not found: {resolved_video_path}. "
            "If using shorthand video_path, expected hhv/srv file under app_<name>/utg<id>/input/."
        )
    run_dt = datetime.now(timezone.utc)
    layout = create_output_layout(project_root, cfg, video_type, run_dt)

    layout.app_utg_dir.mkdir(parents=True, exist_ok=True)
    layout.llm_output_dir.mkdir(parents=True, exist_ok=True)

    logger = setup_logger(layout.log_file_path, cfg.logging.level)
    logger.info("Starting gifdroid_llm_trace pipeline")
    logger.info("Resolved video path: %s", resolved_video_path)

    try:
        env = load_and_validate_env(args.env_file, cfg.llm)
        logger.info("Environment validated for llm=%s model=%s", cfg.llm, cfg.llm_model)
        provider = create_provider(cfg.llm, cfg.llm_model, env, logger)

        if cfg.llm == "gemini":
            logger.info("Running Gemini API preflight before trace generation")
            provider.validate_connection()

        ensure_write_policy(cfg, layout.execution_trace_json_path, layout.keyframes_dir)

        if args.dry_run:
            logger.info("Dry-run completed successfully")
            print("Dry-run OK")
            return 0

        extractor = VideoFrameExtractor()
        sampled_frames, metadata = extractor.extract(resolved_video_path, cfg.frame_sampling, logger)

        selector = KeyframeSelector()
        keyframes = selector.select(sampled_frames, cfg.keyframe_selection, logger)
        selector.save_keyframes(keyframes, layout.keyframes_dir, video_type)

        provider_actions = provider.infer_actions(keyframes)

        steps: List[TraceStep] = []
        for idx, (keyframe, action) in enumerate(zip(keyframes, provider_actions), start=1):
            steps.append(
                TraceStep(
                    step_index=idx,
                    timestamp_sec=keyframe.timestamp_sec,
                    frame_file=keyframe.file_name,
                    screen_description=action.screen_description,
                    action=TraceAction(
                        action_type=action.action_type,
                        target=action.target,
                        details=action.details,
                    ),
                    confidence=action.confidence,
                )
            )

        trace_builder = TraceBuilder()
        trace_payload = trace_builder.build(
            video_path=resolved_video_path,
            llm_name=cfg.llm,
            video_type=video_type,
            app_name=cfg.app_name,
            utg_number=cfg.utg_number,
            generated_at=run_dt,
            steps=steps,
        )

        manifest_payload = selector.build_frames_manifest(
            sampled_frames=sampled_frames,
            keyframes=keyframes,
            video_path=resolved_video_path,
            llm=cfg.llm,
        )
        manifest_payload["video_metadata"] = metadata

        write_json(layout.execution_trace_json_path, trace_payload)
        write_json(layout.frames_manifest_path, manifest_payload)

        logger.info("Execution trace written: %s", layout.execution_trace_json_path)
        logger.info("Frames manifest written: %s", layout.frames_manifest_path)
        logger.info("Saved keyframes: %s", layout.keyframes_dir)

        print(str(layout.execution_trace_json_path))
        return 0
    finally:
        for handler in list(logger.handlers):
            handler.close()
            logger.removeHandler(handler)


def main() -> int:
    args = parse_args()
    try:
        return run_pipeline(args)
    except (ConfigError, EnvError, PathError, VideoError, FileExistsError, ProviderError) as exc:
        print(f"[gifdroid_llm_trace] ERROR: {exc}", file=sys.stderr)
        return 1
    except Exception as exc:  # pragma: no cover
        print(f"[gifdroid_llm_trace] UNEXPECTED ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
