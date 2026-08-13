import json
from pathlib import Path

import pytest

from src_llm.memory_to_device import _locate_latest_run


def _write_metadata(run_dir: Path, video_name: str) -> None:
    run_dir.mkdir(parents=True)
    (run_dir / "metadata.json").write_text(
        json.dumps({
            "app": "amazefilemanager",
            "variant": "gemini-2.5-pro",
            "video": video_name,
            "video_mode_metadata": {
                "memory_md_content": "memory",
                "task_description": "task",
            },
        }),
        encoding="utf-8",
    )


def test_locate_latest_run_uses_exact_video_stem(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    base = tmp_path / "apps" / "amazefilemanager" / "llm"
    _write_metadata(base / "hhv-001-gemini-2.5-pro-vm" / "run-001", "hhv-001.mp4")
    _write_metadata(base / "srv-001-gemini-2.5-pro-vm" / "run-009", "srv-001.mp4")

    found = _locate_latest_run(
        "amazefilemanager",
        "gemini-2.5-pro",
        Path("apps/amazefilemanager/videos/hhv-001.mp4"),
    )

    assert found == Path("apps/amazefilemanager/llm/hhv-001-gemini-2.5-pro-vm/run-001")


def test_locate_latest_run_rejects_other_video_prefixes(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    base = tmp_path / "apps" / "amazefilemanager" / "llm"
    _write_metadata(base / "srv-001-gemini-2.5-pro-vm" / "run-009", "srv-001.mp4")

    with pytest.raises(FileNotFoundError, match="hhv-001.mp4"):
        _locate_latest_run(
            "amazefilemanager",
            "gemini-2.5-pro",
            Path("apps/amazefilemanager/videos/hhv-001.mp4"),
        )
