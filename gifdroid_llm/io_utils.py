from __future__ import annotations

import dataclasses
import json
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Literal, Tuple

from gifdroid_llm.config import AppConfig, FrameSamplingConfig, KeyframeSelectionConfig

VideoType = Literal["hhv", "srv"]


class PathError(ValueError):
    """Raised when input video path or output layout is invalid."""


@dataclass(frozen=True)
class OutputLayout:
    run_dir: Path
    keyframes_dir: Path
    execution_trace_json_path: Path
    frames_manifest_path: Path
    metadata_path: Path
    log_file_path: Path
    run_id: str
    llm_raw_response_path: Path


def detect_video_type(video_path: Path) -> VideoType:
    """Infer HHV/SRV video type from the file path."""
    normalized = video_path.as_posix().lower()
    if "/handheld/" in normalized or "hhv_" in normalized or "hhv-" in normalized:
        return "hhv"
    if "/screenrec/" in normalized or "srv_" in normalized or "srv-" in normalized:
        return "srv"
    raise PathError(
        "Could not detect video type from path. Expect handheld/hhv or screenrec/srv in video path."
    )


def resolve_video_path(project_root: Path, cfg: AppConfig) -> Tuple[Path, VideoType]:
    """Resolve video input from shorthand token ('hhv'/'srv') or explicit path."""
    raw_value = cfg.video_path.as_posix().strip().lower()
    if raw_value in {"hhv", "srv"}:
        video_type: VideoType = "hhv" if raw_value == "hhv" else "srv"
        input_subdir = "handheld" if video_type == "hhv" else "screenrec"
        video_file = f"{video_type}-001.mp4"
        resolved = (
            project_root
            / "apps"
            / cfg.app_name.lower()
            / "videos"
            / input_subdir
            / video_file
        )
        return resolved, video_type

    explicit = cfg.video_path if cfg.video_path.is_absolute() else (project_root / cfg.video_path)
    video_type = detect_video_type(explicit)
    return explicit, video_type


def _next_run_id(run_parent_dir: Path) -> str:
    """Auto-increment run ID by scanning existing run-NNN directories."""
    import os
    max_num = 0
    if run_parent_dir.exists():
        for entry in os.scandir(run_parent_dir):
            if entry.is_dir():
                m = re.match(r"^run-(\d+)$", entry.name)
                if m:
                    max_num = max(max_num, int(m.group(1)))
    return f"run-{max_num + 1:03d}"


def _build_cfg_slug(fs: FrameSamplingConfig, ks: KeyframeSelectionConfig) -> str:
    """Build a human-readable slug encoding all four sampling config fields.

    Example: fps1-5__max100__llm-assisted__gap1-0
    """
    fps_str = f"fps{fs.fps:.10g}".replace(".", "-")
    max_str = f"max{fs.max_frames}"
    method_str = re.sub(r"[^a-z0-9-]+", "-", ks.method.lower()).strip("-")
    gap_str = f"gap{ks.min_gap_seconds:.10g}".replace(".", "-")
    return f"{fps_str}__{max_str}__{method_str}__{gap_str}"


def create_output_layout(
    project_root: Path,
    cfg: AppConfig,
    video_type: VideoType,
    run_dt: datetime,
) -> OutputLayout:
    """Build all output paths under apps/{app}/llm/{provider}/{model}/{source}/{cfg_slug}/run-NNN/."""
    provider = cfg.llm.lower()
    model_slug = re.sub(r"[^a-z0-9-]+", "-", cfg.llm_model.lower()).strip("-")
    if not model_slug:
        model_slug = "model"
    source = "handheld" if video_type == "hhv" else "screenrec"
    cfg_slug = _build_cfg_slug(cfg.frame_sampling, cfg.keyframe_selection)

    run_parent = (
        project_root
        / "apps"
        / cfg.app_name.lower()
        / "llm"
        / provider
        / model_slug
        / source
        / cfg_slug
    )
    run_id = _next_run_id(run_parent)
    run_dir = run_parent / run_id

    ts_file = run_dt.strftime("%Y-%m-%dT%H-%M-%S")
    run_num = run_id[len("run-"):]
    log_file = run_dir / "logs" / f"{ts_file}__run-{run_num}__pipeline__started.log"

    return OutputLayout(
        run_dir=run_dir,
        keyframes_dir=run_dir / "keyframes",
        execution_trace_json_path=run_dir / "execution_trace.json",
        frames_manifest_path=run_dir / "frames_manifest.json",
        metadata_path=run_dir / "metadata.json",
        log_file_path=log_file,
        run_id=run_id,
        llm_raw_response_path=run_dir / "llm_raw_response.txt",
    )


def write_json(path: Path, payload: Dict[str, Any]) -> None:
    """Write deterministic, pretty JSON output."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=True, indent=2, sort_keys=False)


def write_run_metadata(
    path: Path,
    app_name: str,
    method: str,
    variant: str,
    source: str,
    video_file: str,
    frame_sampling_cfg: FrameSamplingConfig,
    keyframe_selection_cfg: KeyframeSelectionConfig,
    run_dt: datetime,
    duration_sec: float,
    status: str,
) -> None:
    """Write metadata.json for a completed run."""
    payload = {
        "app": app_name.lower(),
        "method": method,
        "variant": variant,
        "source": source,
        "video": video_file,
        "config": {
            "frame_sampling": dataclasses.asdict(frame_sampling_cfg),
            "keyframe_selection": dataclasses.asdict(keyframe_selection_cfg),
        },
        "timestamp": run_dt.strftime("%Y-%m-%dT%H:%M:%S"),
        "duration_sec": round(duration_sec, 1),
        "status": status,
    }
    write_json(path, payload)
