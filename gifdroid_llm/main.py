from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import List

from gifdroid_llm.config import AppConfig, ConfigError, load_config
from gifdroid_llm.env_loader import EnvError, load_and_validate_env
from gifdroid_llm.io_utils import (
    PathError,
    create_output_layout,
    resolve_video_path,
    update_utg_manifest,
    write_json,
    write_run_metadata,
)
from gifdroid_llm.keyframes import KeyframeSelector
from gifdroid_llm.logging_utils import finalize_log_file, setup_logger
from gifdroid_llm.providers import ProviderError, create_provider
from gifdroid_llm.trace import TraceAction, TraceBuilder, TraceStep
from gifdroid_llm.video import VideoError, VideoFrameExtractor


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate an LLM-based execution trace from a bug video."
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("gifdroid_llm/input/config.yml"),
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
            "If using shorthand video_path, expected hhv/srv file under apps/<name>/videos/."
        )
    run_dt = datetime.now(timezone.utc)
    layout = create_output_layout(project_root, cfg, video_type, run_dt)

    layout.run_dir.mkdir(parents=True, exist_ok=True)
    (layout.run_dir / "logs").mkdir(parents=True, exist_ok=True)

    logger = setup_logger(layout.log_file_path, cfg.logging.level)
    logger.info("Starting gifdroid_llm pipeline")
    logger.info("Resolved video path: %s", resolved_video_path)

    pipeline_status = "failed"
    pipeline_start = datetime.now(timezone.utc)
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
            pipeline_status = "success"
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
            utg_number=cfg.utg_id,
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

        # Write run metadata
        duration_sec = (datetime.now(timezone.utc) - pipeline_start).total_seconds()
        video_file = resolved_video_path.name
        source = "handheld" if video_type == "hhv" else "screenrec"
        import re as _re
        model_slug = _re.sub(r"[^a-z0-9-]+", "-", cfg.llm_model.lower()).strip("-")

        write_run_metadata(
            path=layout.metadata_path,
            app_name=cfg.app_name,
            utg_id=cfg.utg_id,
            method="llm",
            variant=model_slug,
            source=source,
            video_file=video_file,
            frame_sampling_cfg=cfg.frame_sampling,
            keyframe_selection_cfg=cfg.keyframe_selection,
            run_dt=run_dt,
            duration_sec=duration_sec,
            status="success",
        )

        # Compute relative path from utg root to run dir
        utg_root = layout.utg_manifest_path.parent
        run_relative_path = str(layout.run_dir.relative_to(utg_root)) + "/"

        update_utg_manifest(
            manifest_path=layout.utg_manifest_path,
            app_name=cfg.app_name,
            utg_id=cfg.utg_id,
            run_id=layout.run_id,
            method="llm",
            variant=model_slug,
            source=source,
            status="success",
            run_relative_path=run_relative_path,
            video_file=video_file,
            video_type=video_type,
        )

        pipeline_status = "success"
        print(str(layout.execution_trace_json_path))
        return 0
    finally:
        for handler in list(logger.handlers):
            handler.close()
            logger.removeHandler(handler)
        finalize_log_file(layout.log_file_path, pipeline_status)


def main() -> int:
    args = parse_args()
    try:
        return run_pipeline(args)
    except (ConfigError, EnvError, PathError, VideoError, FileExistsError, ProviderError) as exc:
        print(f"[gifdroid_llm] ERROR: {exc}", file=sys.stderr)
        return 1
    except Exception as exc:  # pragma: no cover
        print(f"[gifdroid_llm] UNEXPECTED ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
