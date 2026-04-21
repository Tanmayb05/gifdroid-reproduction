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


def detect_video_source(video_path: Path) -> str:
    normalized = video_path.as_posix().lower()
    if "/handheld/" in normalized or "hhv_" in normalized or "hhv-" in normalized:
        return "handheld"
    if "/screenrec/" in normalized or "srv_" in normalized or "srv-" in normalized:
        return "screenrec"
    raise PathError(
        "Could not detect video source from path. Expect handheld/hhv or screenrec/srv in video path."
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


def create_output_layout(project_root: Path, app_name: str, llm: str, source: str, run_dt: datetime) -> OutputLayout:
    variant_dir = f"ViBR_{llm.lower()}"
    base_dir = project_root / "apps" / app_name.lower() / "llm" / variant_dir / source
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
