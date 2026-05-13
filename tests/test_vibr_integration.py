"""Integration test: verify create_output_layout() creates flat directory structure on disk.

Exercises the full path-construction path for a simulated ViBR run, including
verifying that the correct directories and metadata path are produced and that
run IDs increment correctly across consecutive runs.
"""

import json
import tempfile
import unittest
from datetime import datetime
from pathlib import Path

from src_ViBR.io_utils import OutputLayout, create_output_layout


class TestCreateOutputLayoutIntegration(unittest.TestCase):
    """Integration tests that touch the real filesystem via tempdir."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.project_root = Path(self.tmp.name)
        self.run_dt = datetime(2026, 5, 12, 10, 30, 0)

    def tearDown(self):
        self.tmp.cleanup()

    # ------------------------------------------------------------------
    # Helper
    # ------------------------------------------------------------------
    def _run(self, app="binaryeye", video="hhv-001.mp4", model="gemini-2.5-pro") -> OutputLayout:
        return create_output_layout(
            self.project_root, app, Path(video), model, self.run_dt
        )

    def _materialise(self, layout: OutputLayout) -> None:
        """Simulate a real run by creating the run_dir (and a metadata.json) on disk."""
        layout.run_dir.mkdir(parents=True, exist_ok=True)
        layout.metadata_path.parent.mkdir(parents=True, exist_ok=True)
        layout.metadata_path.write_text(json.dumps({"run_id": layout.run_id}))

    # ------------------------------------------------------------------
    # Structural assertions
    # ------------------------------------------------------------------
    def test_base_dir_path_matches_flat_convention(self):
        layout = self._run()
        expected_suffix = Path("apps") / "binaryeye" / "llm" / "hhv-001-gemini-2.5-pro-vibr"
        self.assertTrue(
            str(layout.base_dir).endswith(str(expected_suffix)),
            msg=f"base_dir '{layout.base_dir}' does not end with '{expected_suffix}'",
        )

    def test_run_dir_is_run_001_for_fresh_base(self):
        layout = self._run()
        self.assertEqual(layout.run_dir.name, "run-001")

    def test_metadata_path_inside_run_dir(self):
        layout = self._run()
        self.assertEqual(layout.metadata_path.parent, layout.run_dir)
        self.assertEqual(layout.metadata_path.name, "metadata.json")

    def test_artifacts_dir_inside_run_dir(self):
        layout = self._run()
        self.assertEqual(layout.artifacts_dir.parent, layout.run_dir)
        self.assertEqual(layout.artifacts_dir.name, "artifacts")

    def test_log_file_inside_logs_subdir(self):
        layout = self._run()
        self.assertEqual(layout.log_file_path.parent.name, "logs")
        self.assertEqual(layout.log_file_path.parent.parent, layout.run_dir)

    def test_log_file_name_contains_timestamp(self):
        layout = self._run()
        # Timestamp from run_dt = 2026-05-12T10:30:00
        self.assertIn("2026-05-12", layout.log_file_path.name)

    # ------------------------------------------------------------------
    # Run ID increment across consecutive calls
    # ------------------------------------------------------------------
    def test_run_id_increments_after_first_run_materialised(self):
        first = self._run()
        self._materialise(first)

        second = self._run()
        self.assertEqual(first.run_id, "run-001")
        self.assertEqual(second.run_id, "run-002")
        self.assertEqual(second.run_dir.parent, first.run_dir.parent)  # same base_dir

    def test_three_consecutive_runs_increment(self):
        for expected_id in ("run-001", "run-002", "run-003"):
            layout = self._run()
            self.assertEqual(layout.run_id, expected_id)
            self._materialise(layout)

    # ------------------------------------------------------------------
    # Different apps / models stay isolated
    # ------------------------------------------------------------------
    def test_different_app_names_produce_different_base_dirs(self):
        layout_a = self._run(app="appA")
        layout_b = self._run(app="appB")
        self.assertNotEqual(layout_a.base_dir, layout_b.base_dir)

    def test_different_models_produce_different_base_dirs(self):
        layout_a = self._run(model="gemini-2.5-pro")
        layout_b = self._run(model="gpt-4o")
        self.assertNotEqual(layout_a.base_dir, layout_b.base_dir)

    def test_different_videos_produce_different_base_dirs(self):
        layout_a = self._run(video="hhv-001.mp4")
        layout_b = self._run(video="hhv-002.mp4")
        self.assertNotEqual(layout_a.base_dir, layout_b.base_dir)

    # ------------------------------------------------------------------
    # Verify directories can actually be created (no permission issues)
    # ------------------------------------------------------------------
    def test_run_dir_can_be_created_on_disk(self):
        layout = self._run()
        layout.run_dir.mkdir(parents=True)
        self.assertTrue(layout.run_dir.is_dir())

    def test_metadata_json_written_to_expected_path(self):
        layout = self._run()
        layout.metadata_path.parent.mkdir(parents=True, exist_ok=True)
        data = {"run_id": layout.run_id, "model": "gemini-2.5-pro"}
        layout.metadata_path.write_text(json.dumps(data))

        self.assertTrue(layout.metadata_path.exists())
        loaded = json.loads(layout.metadata_path.read_text())
        self.assertEqual(loaded["run_id"], "run-001")


if __name__ == "__main__":
    unittest.main()
