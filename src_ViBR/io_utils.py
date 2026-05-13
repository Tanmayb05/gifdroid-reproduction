from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


class PathError(ValueError):
    """Raised when video path or derived output paths are invalid."""


@dataclass(frozen=True)
class OutputLayout:
    base_dir: Path
    run_dir: Path
    artifacts_dir: Path
    metadata_path: Path
    log_file_path: Path
    run_id: str


def _extract_video_name(video_path: Path | str) -> str:
    """Extract video name without extension (e.g., 'hhv-002.mp4' -> 'hhv-002')."""
    return Path(video_path).stem


def _normalize_model_slug(model_str: str) -> str:
    """Normalize model name to lowercase with hyphens and dots.

    e.g., 'Gemini-2.5-Pro' -> 'gemini-2.5-pro', 'GPT-4o' -> 'gpt-4o'
    Dots in version numbers are preserved; other non-alphanumeric chars become hyphens.
    """
    normalized = re.sub(r"[^a-z0-9.-]+", "-", model_str.lower()).strip("-")
    return normalized if normalized else "model"


def detect_video_source(video_path: Path) -> str:
    filename = video_path.name.lower()
    if filename.startswith("hhv"):
        return "handheld"
    if filename.startswith("srv"):
        return "screenrec"
    raise PathError(
        f"Could not detect video source from filename '{video_path.name}'. "
        "Expect filename to start with 'hhv' or 'srv'."
    )


def _next_run_id(base_dir: Path) -> str:
    max_num = 0
    if base_dir.exists():
        for entry in base_dir.iterdir():
            if not entry.is_dir():
                continue
            match = re.match(r"^run-(\d+)$", entry.name)
            if match:
                max_num = max(max_num, int(match.group(1)))
    return f"run-{max_num + 1:03d}"


def create_output_layout(project_root: Path, app_name: str, video_path: Path, llm_model: str, run_dt: datetime) -> OutputLayout:
    """Create the output directory layout for a ViBR run.

    Uses flat naming convention: apps/{app}/llm/{video-name}-{model}/run-NNN/

    Args:
        project_root: Repository root directory.
        app_name: Application name (lowercased for path).
        video_path: Path to the input video (stem used for directory name).
        llm_model: Full LLM model name (normalized to slug for directory name).
        run_dt: Run start datetime (used for log file naming).

    Returns:
        OutputLayout with all paths resolved.
    """
    video_name = _extract_video_name(video_path)
    model_slug = _normalize_model_slug(llm_model)
    flat_dir = f"{video_name}-{model_slug}"
    base_dir = project_root / "apps" / app_name.lower() / "llm" / flat_dir
    run_id = _next_run_id(base_dir)
    run_dir = base_dir / run_id
    run_num = run_id.split("-")[1]
    ts_file = run_dt.strftime("%Y-%m-%dT%H-%M-%S")
    log_file = run_dir / "logs" / f"{ts_file}__run-{run_num}__pipeline__started.log"
    return OutputLayout(
        base_dir=base_dir,
        run_dir=run_dir,
        artifacts_dir=run_dir / "artifacts",
        metadata_path=run_dir / "metadata.json",
        log_file_path=log_file,
        run_id=run_id,
    )


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=True, indent=2)
