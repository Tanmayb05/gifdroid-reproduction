from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Tuple

from src_llm.config import AppConfig, ConfigError, PipelineConfig, load_config
from src_llm.env_loader import EnvError, load_and_validate_env
from src_llm.io_utils import (
    PathError,
    _normalize_model_slug,
    create_output_layout,
    resolve_video_path,
    write_json,
    write_run_metadata,
)
from src_llm.keyframes import KeyframeSelector
from src_llm.llama_prereq import LlamaPrereqError, assert_llama_accessible
from src_llm.logging_utils import finalize_log_file, setup_logger
from src_llm.providers import ProviderError, create_provider
from src_llm.trace import TraceAction, TraceBuilder, TraceStep
from src_llm.video import VideoError, VideoFrameExtractor


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate an LLM-based execution trace from a bug video."
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("src_llm/input/config.yml"),
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
    return parser.parse_args(argv)


def ensure_write_policy(cfg: AppConfig, execution_json_path: Path, memory_md_path: Path, keyframes_dir: Path) -> None:
    if cfg.output.overwrite:
        return
    if cfg.video_mode:
        if memory_md_path.exists():
            raise FileExistsError(
                f"Output exists and overwrite=false: {memory_md_path}"
            )
    else:
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


def _parse_memory_md(memory_text: str) -> Tuple[str, Dict[str, str], List[str]]:
    """Extract structured data from memory.md markdown.

    Returns: (task_description, ui_elements_dict, completion_criteria_list)

    Handles both formats:
    1. YAML header + Session Summary + Steps (current format from Gemini)
    2. # Task Summary + ## UI Elements + ## Completion Criteria (planned format)
    """
    task_desc = ""
    ui_elements: Dict[str, str] = {}
    completion_criteria: List[str] = []

    # Try Format 1: Check for YAML header with goal/outcome
    yaml_match = re.search(r'^---\n(.*?)\n---', memory_text, re.DOTALL)
    if yaml_match:
        yaml_content = yaml_match.group(1)
        # Extract goal from YAML
        goal_match = re.search(r'goal:\s*(.+?)$', yaml_content, re.MULTILINE)
        if goal_match:
            task_desc = goal_match.group(1).strip()

        # Extract outcome for completion criteria
        outcome_match = re.search(r'outcome:\s*(.+?)$', yaml_content, re.MULTILINE)
        if outcome_match:
            outcome = outcome_match.group(1).strip()
            if outcome:
                completion_criteria.append(f"Task outcome: {outcome}")

        # Extract UI elements from steps
        # Skip blank lines after "## Steps\n" with \n*(.*?)
        steps_match = re.search(r'## Steps\n\n+(.*?)(?=\n##|\Z)', memory_text, re.DOTALL)
        if steps_match:
            steps_text = steps_match.group(1)

            # Parse line by line to extract UI elements
            seen_elements = set()
            seen_screens = set()

            for line in steps_text.split('\n'):
                # Extract action targets from **Action:** lines
                if '**Action:**' in line:
                    # Format: "- **Action:** tap → \"Allowed\" button"
                    if '→' in line:
                        parts = line.split('→', 1)
                        if len(parts) == 2:
                            target = parts[1].strip()
                            # Remove trailing descriptors and quotes
                            target = re.sub(r'\s+(button|field|menu|dialog|list|screen|bar)$', '', target, flags=re.IGNORECASE)
                            target = target.strip('`"() ')
                            action_type = re.search(r'(\w+)\s+→', line)
                            if target and target not in seen_elements:
                                if action_type:
                                    ui_elements[target] = action_type.group(1)
                                seen_elements.add(target)

                # Extract screen names from **Screen:** lines
                if '**Screen:**' in line:
                    match = re.search(r'\*\*Screen:\*\*\s+([^\n]+)', line)
                    if match:
                        screen = match.group(1).strip()
                        if screen and screen not in seen_screens:
                            ui_elements[f"screen: {screen}"] = "navigation_target"
                            seen_screens.add(screen)

                # Extract user input details
                if '**Details:**' in line and 'type' in line.lower():
                    match = re.search(r'\*\*Details:\*\*\s+([^\n]+)', line)
                    if match:
                        detail = match.group(1).strip()
                        if len(detail) > 5:
                            ui_elements[f"input: {detail[:35]}"] = "user_input"
    else:
        # Try Format 2: Check for # Task Summary section
        task_match = re.search(r'# Task Summary\n(.*?)(?=\n## |\Z)', memory_text, re.DOTALL)
        if task_match:
            task_desc = task_match.group(1).strip()

        # Parse "## UI Elements" section
        ui_match = re.search(r'## UI Elements\n(.*?)(?=\n## |\Z)', memory_text, re.DOTALL)
        if ui_match:
            for line in ui_match.group(1).split('\n'):
                if line.startswith('- '):
                    parts = line[2:].split(':', 1)
                    if len(parts) == 2:
                        ui_elements[parts[0].strip()] = parts[1].strip()

        # Parse "## Completion Criteria" section
        criteria_match = re.search(r'## Completion Criteria\n(.*?)(?=\n## |\Z)', memory_text, re.DOTALL)
        if criteria_match:
            for line in criteria_match.group(1).split('\n'):
                if line.startswith('- '):
                    completion_criteria.append(line[2:].strip())

    return task_desc, ui_elements, completion_criteria


def run_single(args: argparse.Namespace, cfg: AppConfig) -> int:
    project_root = Path.cwd()

    resolved_video_path, video_type = resolve_video_path(project_root, cfg)
    if not resolved_video_path.exists():
        raise VideoError(
            f"Video file not found: {resolved_video_path}. "
            "If using shorthand video_path, expected hhv/srv file under apps/<name>/videos/."
        )
    run_dt = datetime.now(timezone.utc)
    layout = create_output_layout(project_root, cfg, video_type, run_dt, is_dry_run=args.dry_run)

    layout.run_dir.mkdir(parents=True, exist_ok=True)
    (layout.run_dir / "logs").mkdir(parents=True, exist_ok=True)

    logger = setup_logger(layout.log_file_path, cfg.logging.level)
    logger.info("Starting src_llm pipeline")
    logger.info("Resolved video path: %s", resolved_video_path)

    pipeline_status = "failed"
    pipeline_start = datetime.now(timezone.utc)
    try:
        try:
            ensure_write_policy(cfg, layout.execution_trace_json_path, layout.memory_md_path, layout.keyframes_dir)
        except FileExistsError as exc:
            logger.warning("RUN SKIPPED — output already present: %s", exc)
            pipeline_status = "skipped"
            return 0

        if args.dry_run:
            logger.info("Dry-run completed successfully (provider/API preflight skipped)")
            print("Dry-run OK")
            pipeline_status = "success"
            return 0

        env = load_and_validate_env(args.env_file, cfg.llm)
        logger.info("Environment validated for llm=%s model=%s", cfg.llm, cfg.llm_model)

        _LLAMA_BASE_PROVIDERS = {"llama", "llava", "minicpm", "gemma"}
        if cfg.llm in _LLAMA_BASE_PROVIDERS or cfg.llm == "qwen":
            if cfg.llm == "qwen":
                base_url_key, api_key_key, prereq_timeout_key = "QWEN_BASE_URL", "QWEN_API_KEY", "QWEN_PREREQ_TIMEOUT_SEC"
            else:
                base_url_key, api_key_key, prereq_timeout_key = "LLAMA_BASE_URL", "LLAMA_API_KEY", "LLAMA_PREREQ_TIMEOUT_SEC"
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
            llm_prompt_file=cfg.llm_prompt_file,
            video_mode=cfg.video_mode,
        )

        if cfg.llm == "gemini":
            logger.info("Running %s API preflight before trace generation", cfg.llm)
            provider.validate_connection()

        memory_text = None
        task_desc = None
        ui_elements = None
        completion_criteria = None

        if cfg.video_mode:
            logger.info("Video mode enabled — skipping frame extraction and keyframe selection")
            memory_text = provider.infer_memory_from_video(resolved_video_path)
            layout.memory_md_path.parent.mkdir(parents=True, exist_ok=True)
            layout.memory_md_path.write_text(memory_text, encoding="utf-8")
            logger.info("Memory trace written: %s", layout.memory_md_path)

            # Parse memory.md for metadata storage
            task_desc, ui_elements, completion_criteria = _parse_memory_md(memory_text)
            logger.info(
                "Parsed memory: task_desc=%s | ui_elements=%d | completion_criteria=%d",
                len(task_desc) if task_desc else 0,
                len(ui_elements) if ui_elements else 0,
                len(completion_criteria) if completion_criteria else 0,
            )
        else:
            extractor = VideoFrameExtractor()
            sampled_frames, metadata = extractor.extract(resolved_video_path, cfg.frame_sampling, logger)

            selector = KeyframeSelector()
            keyframes = selector.select(sampled_frames, cfg.keyframe_selection, logger)
            selector.save_keyframes(keyframes, layout.keyframes_dir, video_type)

            provider_actions = provider.infer_actions(keyframes)

            steps = []
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
                llm_prompt_file=str(cfg.llm_prompt_file) if cfg.llm_prompt_file is not None else None,
            )
            manifest_payload["video_metadata"] = metadata

            write_json(layout.execution_trace_json_path, trace_payload)
            write_json(layout.frames_manifest_path, manifest_payload)

        if provider.raw_llm_response is not None:
            layout.llm_raw_response_path.parent.mkdir(parents=True, exist_ok=True)
            layout.llm_raw_response_path.write_text(provider.raw_llm_response, encoding="utf-8")
            logger.info("LLM raw response written: %s", layout.llm_raw_response_path)

        if not cfg.video_mode:
            logger.info("Execution trace written: %s", layout.execution_trace_json_path)
            logger.info("Frames manifest written: %s", layout.frames_manifest_path)
            logger.info("Saved keyframes: %s", layout.keyframes_dir)

        # Write run metadata
        duration_sec = (datetime.now(timezone.utc) - pipeline_start).total_seconds()
        video_file = resolved_video_path.name
        source = "handheld" if video_type == "hhv" else "screenrec"
        model_slug = _normalize_model_slug(cfg.llm_model)

        write_run_metadata(
            path=layout.metadata_path,
            app_name=cfg.app_name,
            method="llm",
            variant=model_slug,
            source=source,
            video_file=video_file,
            llm_prompt_file=str(cfg.llm_prompt_file) if cfg.llm_prompt_file is not None else None,
            frame_sampling_cfg=cfg.frame_sampling if not cfg.video_mode else None,
            keyframe_selection_cfg=cfg.keyframe_selection if not cfg.video_mode else None,
            run_dt=run_dt,
            duration_sec=duration_sec,
            status="success",
            memory_md_content=memory_text,
            task_description=task_desc,
            ui_elements=ui_elements,
            completion_criteria=completion_criteria,
        )

        pipeline_status = "success"
        output_path = layout.memory_md_path if cfg.video_mode else layout.execution_trace_json_path
        print(str(output_path))
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
        print(f"[video_to_memory] Running {len(runs)} configured runs")
    exit_code = 0
    for i, cfg in enumerate(runs, start=1):
        if len(runs) > 1:
            print(f"[video_to_memory] --- Run {i}/{len(runs)}: {cfg.app_name} ({cfg.video_path}) ---")
        try:
            code = run_single(args, cfg)
        except VideoError as exc:
            print(f"[video_to_memory] SKIP run {i}/{len(runs)}: {exc}")
            continue
        if code != 0:
            exit_code = code
    return exit_code


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv) if argv else parse_args()
    try:
        return run_pipeline(args)
    except (ConfigError, EnvError, PathError, VideoError, ProviderError, LlamaPrereqError) as exc:
        print(f"[video_to_memory] ERROR: {exc}", file=sys.stderr)
        return 1
    except Exception as exc:  # pragma: no cover
        print(f"[video_to_memory] UNEXPECTED ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
