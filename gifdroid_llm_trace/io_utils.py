from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Literal, Tuple

from gifdroid_llm_trace.config import AppConfig

VideoType = Literal["hhv", "srv"]


class PathError(ValueError):
    """Raised when input video path or output layout is invalid."""


@dataclass(frozen=True)
class OutputLayout:
    app_utg_dir: Path
    llm_output_dir: Path
    execution_trace_json_path: Path
    keyframes_dir: Path
    log_file_path: Path
    frames_manifest_path: Path


def detect_video_type(video_path: Path) -> VideoType:
    """Infer HHV/SRV video type from the file path."""
    normalized = video_path.as_posix().lower()
    if "/handheld/" in normalized or "hhv_" in normalized:
        return "hhv"
    if "/screenrec/" in normalized or "srv_" in normalized:
        return "srv"
    raise PathError(
        "Could not detect video type from path. Expect handheld/hhv_ or screenrec/srv_ in video path."
    )


def resolve_video_path(project_root: Path, cfg: AppConfig) -> Tuple[Path, VideoType]:
    """Resolve video input from shorthand token ('hhv'/'srv') or explicit path."""
    raw_value = cfg.video_path.as_posix().strip().lower()
    if raw_value in {"hhv", "srv"}:
        video_type: VideoType = "hhv" if raw_value == "hhv" else "srv"
        input_subdir = "handheld" if video_type == "hhv" else "screenrec"
        resolved = (
            project_root
            / f"app_{cfg.app_name}"
            / f"utg{cfg.utg_number}"
            / "input"
            / input_subdir
            / f"{video_type}_app_{cfg.app_name}.mp4"
        )
        return resolved, video_type

    explicit = cfg.video_path if cfg.video_path.is_absolute() else (project_root / cfg.video_path)
    video_type = detect_video_type(explicit)
    return explicit, video_type


def create_output_layout(
    project_root: Path,
    cfg: AppConfig,
    video_type: VideoType,
    run_dt: datetime,
) -> OutputLayout:
    """Build all output paths using the required naming conventions."""
    app_utg_dir = project_root / f"app_{cfg.app_name}" / f"utg{cfg.utg_number}"
    llm_output_dir = app_utg_dir / "output" / f"llm_{cfg.llm.lower()}"
    dt_token = run_dt.strftime("%Y%m%d_%H%M%S")
    model_token = re.sub(r"[^a-zA-Z0-9._-]+", "_", cfg.llm_model).strip("._-")
    if not model_token:
        model_token = "model"

    execution_file = (
        llm_output_dir
        / f"execution_trace_llm_{video_type}_app_{cfg.app_name}_{model_token}_{dt_token}.json"
    )
    keyframes_dir = llm_output_dir / f"execution_trace_llm_{video_type}_keyframes"
    log_name = f"gifdroid_llm_{run_dt.strftime('%Y%m%d_%H%M%S')}_{video_type}.log"
    log_file = app_utg_dir / log_name
    manifest_file = llm_output_dir / f"frames_manifest_{video_type}.json"

    return OutputLayout(
        app_utg_dir=app_utg_dir,
        llm_output_dir=llm_output_dir,
        execution_trace_json_path=execution_file,
        keyframes_dir=keyframes_dir,
        log_file_path=log_file,
        frames_manifest_path=manifest_file,
    )


def write_json(path: Path, payload: Dict[str, Any]) -> None:
    """Write deterministic, pretty JSON output."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=True, indent=2, sort_keys=False)
