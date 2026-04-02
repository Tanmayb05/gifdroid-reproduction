from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import List

from gifdroid_llm.config import AppConfig, ConfigError, PipelineConfig, load_config
from gifdroid_llm.env_loader import EnvError, load_and_validate_env
from gifdroid_llm.io_utils import (
    PathError,
    create_output_layout,
    resolve_video_path,
    write_json,
    write_run_metadata,
)
from gifdroid_llm.keyframes import KeyframeSelector
from gifdroid_llm.llama_prereq import LlamaPrereqError, assert_llama_accessible
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


def _env_timeout_sec(env: dict, key: str, default: int) -> int:
    raw = str(env.get(key, "")).strip()
    if not raw:
        return default
    try:
        value = int(raw)
    except ValueError:
        return default
    return value if value > 0 else default


def run_single(args: argparse.Namespace, cfg: AppConfig) -> int:
    project_root = Path.cwd()

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
        try:
            ensure_write_policy(cfg, layout.execution_trace_json_path, layout.keyframes_dir)
        except FileExistsError as exc:
            logger.warning("RUN SKIPPED — execution trace already present: %s", exc)
            pipeline_status = "skipped"
            return 0

        if args.dry_run:
            logger.info("Dry-run completed successfully (provider/API preflight skipped)")
            print("Dry-run OK")
            pipeline_status = "success"
            return 0

        env = load_and_validate_env(args.env_file, cfg.llm)
        logger.info("Environment validated for llm=%s model=%s", cfg.llm, cfg.llm_model)

        if cfg.llm in {"llama", "qwen"}:
            prereq_timeout_key = "LLAMA_PREREQ_TIMEOUT_SEC" if cfg.llm == "llama" else "QWEN_PREREQ_TIMEOUT_SEC"
            base_url_key = "LLAMA_BASE_URL" if cfg.llm == "llama" else "QWEN_BASE_URL"
            api_key_key = "LLAMA_API_KEY" if cfg.llm == "llama" else "QWEN_API_KEY"
            raw_prereq = str(env.get(prereq_timeout_key, "")).strip()
            prereq_timeout_sec: int | None = None
            if raw_prereq:
                try:
                    parsed = int(raw_prereq)
                    prereq_timeout_sec = parsed if parsed > 0 else None
                except ValueError:
                    pass
            logger.info(
                "Running %s prerequisite check before trace generation | timeout=%s",
                cfg.llm,
                prereq_timeout_sec if prereq_timeout_sec is not None else "unlimited",
            )
            assert_llama_accessible(
                base_url=str(env.get(base_url_key, "")),
                model=cfg.llm_model,
                api_key=str(env.get(api_key_key, "")),
                timeout_sec=prereq_timeout_sec,
            )

        provider = create_provider(
            cfg.llm,
            cfg.llm_model,
            env,
            logger,
            llama_action_prompt_file=cfg.llama_action_prompt_file,
        )

        if cfg.llm == "gemini":
            logger.info("Running %s API preflight before trace generation", cfg.llm)
            provider.validate_connection()

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

        if provider.raw_llm_response is not None:
            layout.llm_raw_response_path.parent.mkdir(parents=True, exist_ok=True)
            layout.llm_raw_response_path.write_text(provider.raw_llm_response, encoding="utf-8")
            logger.info("LLM raw response written: %s", layout.llm_raw_response_path)

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

        pipeline_status = "success"
        print(str(layout.execution_trace_json_path))
        return 0
    finally:
        for handler in list(logger.handlers):
            handler.close()
            logger.removeHandler(handler)
        finalize_log_file(layout.log_file_path, pipeline_status)


def run_pipeline(args: argparse.Namespace) -> int:
    pipeline_cfg = load_config(args.config)
    runs = pipeline_cfg.runs
    if len(runs) > 1:
        print(f"[gifdroid_llm] Running {len(runs)} configured runs")
    exit_code = 0
    for i, cfg in enumerate(runs, start=1):
        if len(runs) > 1:
            print(f"[gifdroid_llm] --- Run {i}/{len(runs)}: {cfg.app_name} ({cfg.video_path}) ---")
        try:
            code = run_single(args, cfg)
        except VideoError as exc:
            print(f"[gifdroid_llm] SKIP run {i}/{len(runs)}: {exc}")
            continue
        if code != 0:
            exit_code = code
    return exit_code


def main() -> int:
    args = parse_args()
    try:
        return run_pipeline(args)
    except (ConfigError, EnvError, PathError, VideoError, ProviderError, LlamaPrereqError) as exc:
        print(f"[gifdroid_llm] ERROR: {exc}", file=sys.stderr)
        return 1
    except Exception as exc:  # pragma: no cover
        print(f"[gifdroid_llm] UNEXPECTED ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
