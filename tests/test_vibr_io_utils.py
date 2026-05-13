"""Unit tests for src_ViBR/io_utils.py path construction helpers."""

import tempfile
import unittest
from datetime import datetime
from pathlib import Path

from src_ViBR.io_utils import (
    _extract_video_name,
    _normalize_model_slug,
    create_output_layout,
)


class TestExtractVideoName(unittest.TestCase):
    def test_mp4_string(self):
        self.assertEqual(_extract_video_name("hhv-002.mp4"), "hhv-002")

    def test_srv_string(self):
        self.assertEqual(_extract_video_name("srv-001.mp4"), "srv-001")

    def test_path_object(self):
        self.assertEqual(_extract_video_name(Path("hhv-003.mp4")), "hhv-003")

    def test_absolute_path(self):
        self.assertEqual(_extract_video_name(Path("/some/dir/hhv-010.mp4")), "hhv-010")

    def test_no_extension(self):
        self.assertEqual(_extract_video_name("myvideo"), "myvideo")

    def test_multiple_dots_in_name(self):
        # Only the last extension is stripped by Path.stem
        self.assertEqual(_extract_video_name("video.2024.mp4"), "video.2024")


class TestNormalizeModelSlug(unittest.TestCase):
    def test_already_lowercase(self):
        self.assertEqual(_normalize_model_slug("gemini-2.5-pro"), "gemini-2.5-pro")

    def test_mixed_case(self):
        self.assertEqual(_normalize_model_slug("GPT-4o"), "gpt-4o")

    def test_spaces_become_hyphens(self):
        self.assertEqual(_normalize_model_slug("Gemini 2.5 Pro"), "gemini-2.5-pro")

    def test_underscore_becomes_hyphen(self):
        self.assertEqual(_normalize_model_slug("gpt_4_turbo"), "gpt-4-turbo")

    def test_dots_preserved(self):
        # Dots in version numbers should be preserved
        self.assertEqual(_normalize_model_slug("gemini-2.0-flash"), "gemini-2.0-flash")

    def test_empty_string_returns_model(self):
        self.assertEqual(_normalize_model_slug(""), "model")

    def test_only_hyphens_returns_model(self):
        self.assertEqual(_normalize_model_slug("---"), "model")

    def test_uppercase_with_version(self):
        self.assertEqual(_normalize_model_slug("Claude-3.5-Sonnet"), "claude-3.5-sonnet")


class TestCreateOutputLayout(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.project_root = Path(self.tmp.name)
        self.run_dt = datetime(2026, 5, 12, 10, 30, 0)

    def tearDown(self):
        self.tmp.cleanup()

    def test_flat_path_format(self):
        layout = create_output_layout(
            self.project_root,
            "binaryeye",
            Path("hhv-001.mp4"),
            "gemini-2.5-pro",
            self.run_dt,
        )
        expected_base = self.project_root / "apps" / "binaryeye" / "llm" / "hhv-001-gemini-2.5-pro"
        self.assertEqual(layout.base_dir, expected_base)

    def test_run_dir_under_base(self):
        layout = create_output_layout(
            self.project_root,
            "myapp",
            Path("srv-002.mp4"),
            "gpt-4o",
            self.run_dt,
        )
        self.assertEqual(layout.run_dir, layout.base_dir / "run-001")

    def test_run_id_is_run_001_fresh(self):
        layout = create_output_layout(
            self.project_root,
            "myapp",
            Path("hhv-003.mp4"),
            "claude-3.5-sonnet",
            self.run_dt,
        )
        self.assertEqual(layout.run_id, "run-001")

    def test_metadata_path_under_run_dir(self):
        layout = create_output_layout(
            self.project_root,
            "myapp",
            Path("hhv-001.mp4"),
            "gemini",
            self.run_dt,
        )
        self.assertEqual(layout.metadata_path, layout.run_dir / "metadata.json")

    def test_artifacts_dir_under_run_dir(self):
        layout = create_output_layout(
            self.project_root,
            "myapp",
            Path("hhv-001.mp4"),
            "gemini",
            self.run_dt,
        )
        self.assertEqual(layout.artifacts_dir, layout.run_dir / "artifacts")

    def test_log_file_under_logs_subdir(self):
        layout = create_output_layout(
            self.project_root,
            "myapp",
            Path("hhv-001.mp4"),
            "gemini",
            self.run_dt,
        )
        self.assertIn("logs", str(layout.log_file_path))
        self.assertTrue(str(layout.log_file_path).startswith(str(layout.run_dir)))

    def test_app_name_lowercased(self):
        layout = create_output_layout(
            self.project_root,
            "BinaryEye",
            Path("hhv-001.mp4"),
            "gemini",
            self.run_dt,
        )
        self.assertIn("binaryeye", str(layout.base_dir))

    def test_model_name_normalized_in_path(self):
        layout = create_output_layout(
            self.project_root,
            "myapp",
            Path("hhv-001.mp4"),
            "Gemini 2.5 Pro",
            self.run_dt,
        )
        self.assertIn("gemini-2.5-pro", str(layout.base_dir))


class TestCreateOutputLayoutRunIdIncrement(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.project_root = Path(self.tmp.name)
        self.run_dt = datetime(2026, 5, 12, 10, 30, 0)

    def tearDown(self):
        self.tmp.cleanup()

    def _layout(self, video="hhv-001.mp4", model="gemini"):
        return create_output_layout(
            self.project_root, "myapp", Path(video), model, self.run_dt
        )

    def test_increments_after_existing_run(self):
        first = self._layout()
        # Create the first run directory on disk so the counter advances
        first.run_dir.mkdir(parents=True, exist_ok=True)
        second = self._layout()
        self.assertEqual(first.run_id, "run-001")
        self.assertEqual(second.run_id, "run-002")

    def test_skips_non_run_directories(self):
        # Create a non-matching directory — should not affect counter
        base = self.project_root / "apps" / "myapp" / "llm" / "hhv-001-gemini"
        base.mkdir(parents=True)
        (base / "logs").mkdir()
        layout = self._layout()
        self.assertEqual(layout.run_id, "run-001")

    def test_handles_gap_in_run_numbers(self):
        base = self.project_root / "apps" / "myapp" / "llm" / "hhv-001-gemini"
        base.mkdir(parents=True)
        (base / "run-001").mkdir()
        (base / "run-003").mkdir()  # gap: run-002 is missing
        layout = self._layout()
        self.assertEqual(layout.run_id, "run-004")


if __name__ == "__main__":
    unittest.main()
