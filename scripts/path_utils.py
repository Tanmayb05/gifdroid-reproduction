"""
path_utils.py — Shared path-building utilities for GIFdroid new directory structure.

New layout:
  apps/<app>/videos/handheld/hhv-001.mp4
  apps/<app>/videos/screenrec/srv-001.mp4
  apps/<app>/utgs/<utg-id>/input/utg.json
  apps/<app>/utgs/<utg-id>/input/artifacts/artifact-001.png
  apps/<app>/utgs/<utg-id>/runs/<method-path>/<source>/run-NNN/
  apps/<app>/utgs/<utg-id>/manifest.json
"""

from __future__ import annotations

import os
import re
from pathlib import Path


def normalize_utg_id(value) -> str:
    """Normalize any utg identifier to 'utg-NN' form.

    Accepts: "01", "1", 1, "utg01", "utg-01"
    Returns: "utg-01"
    """
    if isinstance(value, int):
        return f"utg-{value:02d}"
    s = str(value).strip().lower()
    m = re.match(r"^(?:utg-?)?(\d+)$", s)
    if not m:
        raise ValueError(f"Cannot parse utg identifier: {value!r}")
    return f"utg-{int(m.group(1)):02d}"


def normalize_app_name(name: str) -> str:
    """Normalize app name to lowercase slug."""
    return name.lower()


def normalize_model_slug(model_name: str) -> str:
    """Normalize model name to kebab-case slug for directory names."""
    return re.sub(r"[^a-z0-9-]+", "-", model_name.lower()).strip("-")


def app_root(project_root: Path, app_name: str) -> Path:
    return project_root / "apps" / normalize_app_name(app_name)


def utg_root(project_root: Path, app_name: str, utg_id: str) -> Path:
    return app_root(project_root, app_name) / "utgs" / utg_id


def video_path(project_root: Path, app_name: str, source: str, video_file: str) -> Path:
    """source: 'handheld' or 'screenrec'"""
    return app_root(project_root, app_name) / "videos" / source / video_file


def input_root(project_root: Path, app_name: str, utg_id: str) -> Path:
    return utg_root(project_root, app_name, utg_id) / "input"


def artifacts_dir(project_root: Path, app_name: str, utg_id: str) -> Path:
    return input_root(project_root, app_name, utg_id) / "artifacts"


def run_dir_gifdroid(
    project_root: Path,
    app_name: str,
    utg_id: str,
    method: str,
    source: str,
    run_id: str,
) -> Path:
    """Build run directory path for gifdroid (baseline or keyframe-fixes)."""
    if method == "baseline":
        method_path = "baseline"
    else:
        method_path = f"keyframe-fixes/{method}"
    return utg_root(project_root, app_name, utg_id) / "runs" / method_path / source / run_id


def run_dir_llm(
    project_root: Path,
    app_name: str,
    utg_id: str,
    provider: str,
    model: str,
    source: str,
    run_id: str,
) -> Path:
    """Build run directory path for gifdroid_llm."""
    model_slug = normalize_model_slug(model)
    return (
        utg_root(project_root, app_name, utg_id)
        / "runs" / "llm" / provider.lower() / model_slug / source / run_id
    )


def next_run_id(run_parent_dir: Path) -> str:
    """Auto-increment run ID by scanning existing run-NNN directories."""
    max_num = 0
    if run_parent_dir.exists():
        for entry in os.scandir(run_parent_dir):
            if entry.is_dir():
                m = re.match(r"^run-(\d+)$", entry.name)
                if m:
                    max_num = max(max_num, int(m.group(1)))
    return f"run-{max_num + 1:03d}"


def keyframe_file_path(run_dir: Path, index: int) -> Path:
    """Path for kf-0001.png style keyframe files."""
    return run_dir / "keyframes" / f"kf-{index:04d}.png"


def execution_trace_path(run_dir: Path) -> Path:
    return run_dir / "execution_trace.json"


def frames_manifest_path(run_dir: Path) -> Path:
    return run_dir / "frames_manifest.json"


def metadata_path(run_dir: Path) -> Path:
    return run_dir / "metadata.json"


def log_path(run_dir: Path, run_id: str, stage: str, status: str, timestamp: str) -> Path:
    """timestamp format: '2026-03-31T18-42-10' (colons replaced with dashes)"""
    run_num = run_id[len("run-"):]
    return run_dir / "logs" / f"{timestamp}__run-{run_num}__{stage}__{status}.log"


def manifest_path(project_root: Path, app_name: str, utg_id: str) -> Path:
    return utg_root(project_root, app_name, utg_id) / "manifest.json"