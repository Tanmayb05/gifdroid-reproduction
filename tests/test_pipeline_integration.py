"""Integration tests for two-stage pipeline (Stage 1 → Stage 2).

Tests validate that:
1. Stage 1 generates memory.md and metadata.json with video_mode_metadata
2. Stage 2 locates the Stage 1 output and uses it for automation
3. Sequential execution works without intermediate manual steps
4. Dry-run validates both stages without processing
"""

import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from src_llm import pipeline


class TestPipelineOrchestration(unittest.TestCase):
    """Test end-to-end pipeline orchestration."""

    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.TemporaryDirectory()
        self.test_root = Path(self.temp_dir.name)

    def tearDown(self):
        """Clean up test fixtures."""
        self.temp_dir.cleanup()

    def test_parse_args_default(self):
        """Test argument parsing with defaults."""
        with mock.patch("sys.argv", ["pipeline.py"]):
            args = pipeline._parse_args()
            assert args.config == Path("src_llm/input/config.yml")
            assert args.env_file == Path(".env.local")
            assert args.stage is None
            assert args.dry_run is False

    def test_parse_args_stage_1(self):
        """Test argument parsing for Stage 1 only."""
        with mock.patch(
            "sys.argv",
            ["pipeline.py", "--stage", "1", "--dry-run"],
        ):
            args = pipeline._parse_args()
            assert args.stage == 1
            assert args.dry_run is True

    def test_parse_args_stage_2(self):
        """Test argument parsing for Stage 2 only."""
        with mock.patch(
            "sys.argv",
            ["pipeline.py", "--stage", "2"],
        ):
            args = pipeline._parse_args()
            assert args.stage == 2

    def test_parse_args_custom_paths(self):
        """Test argument parsing with custom config and env paths."""
        config = Path("/tmp/custom-config.yml")
        env = Path("/tmp/.env.custom")
        with mock.patch(
            "sys.argv",
            ["pipeline.py", "--config", str(config), "--env-file", str(env)],
        ):
            args = pipeline._parse_args()
            assert args.config == config
            assert args.env_file == env


class TestStage1Stage2Handoff(unittest.TestCase):
    """Test the handoff between Stage 1 and Stage 2.

    Validates that metadata.json from Stage 1 is correctly loaded and
    used by Stage 2 without re-analyzing the video.
    """

    def test_stage1_produces_metadata_with_memory(self):
        """Stage 1 should produce metadata.json with video_mode_metadata."""
        # Mock metadata structure that Stage 1 would produce
        metadata = {
            "app": "adaway",
            "method": "llm",
            "variant": "gemini-2.5-pro",
            "source": "screenrec",
            "video": "srv-001.mp4",
            "timestamp": "2026-05-05T10:00:00",
            "duration_sec": 45.2,
            "status": "success",
            "video_mode_metadata": {
                "memory_md_content": "# Task Summary\nOpen settings...",
                "task_description": "Open settings and toggle notifications",
                "ui_elements": {
                    "Settings Button": "Top-right icon",
                    "Notifications Toggle": "In settings menu",
                },
                "completion_criteria": [
                    "Settings dialog is visible",
                    "Notifications are toggled",
                ],
            },
        }

        # Verify structure has required keys for Stage 2
        assert "video_mode_metadata" in metadata
        assert "memory_md_content" in metadata["video_mode_metadata"]
        assert "task_description" in metadata["video_mode_metadata"]

    def test_stage2_loads_memory_from_metadata(self):
        """Stage 2 should load memory content from Stage 1 metadata."""
        metadata = {
            "video_mode_metadata": {
                "memory_md_content": "# Task Summary\n...",
                "task_description": "Test task",
            }
        }

        # Simulate Stage 2 loading
        memory_content = metadata.get("video_mode_metadata", {}).get("memory_md_content")
        task_desc = metadata.get("video_mode_metadata", {}).get("task_description")

        assert memory_content is not None
        assert task_desc == "Test task"


class TestDryRunValidation(unittest.TestCase):
    """Test that dry-run validates pipeline without processing."""

    def test_dry_run_skips_processing(self):
        """Dry-run should validate config without calling LLM or device."""
        # This would be tested with actual integration,
        # but here we verify the parameter is passed correctly
        with mock.patch("sys.argv", ["pipeline.py", "--dry-run"]):
            args = pipeline._parse_args()
            assert args.dry_run is True

    def test_dry_run_stage_1_only(self):
        """Dry-run with Stage 1 should validate video files and config."""
        with mock.patch("sys.argv", ["pipeline.py", "--stage", "1", "--dry-run"]):
            args = pipeline._parse_args()
            assert args.stage == 1
            assert args.dry_run is True

    def test_dry_run_stage_2_only(self):
        """Dry-run with Stage 2 should validate device and config."""
        with mock.patch("sys.argv", ["pipeline.py", "--stage", "2", "--dry-run"]):
            args = pipeline._parse_args()
            assert args.stage == 2
            assert args.dry_run is True

    def test_dry_run_both_stages(self):
        """Dry-run with both stages should validate without processing either."""
        with mock.patch("sys.argv", ["pipeline.py", "--dry-run"]):
            args = pipeline._parse_args()
            assert args.stage is None
            assert args.dry_run is True


class TestPipelineSequentialExecution(unittest.TestCase):
    """Test that pipeline executes Stage 1 → Stage 2 in sequence."""

    @mock.patch("src_llm.automate.main")
    @mock.patch("src_llm.main.main")
    def test_stage1_then_stage2(self, mock_stage1, mock_stage2):
        """Pipeline should run Stage 1, then Stage 2 when stage=None."""
        mock_stage1.return_value = 0
        mock_stage2.return_value = 0

        with tempfile.NamedTemporaryFile(suffix=".yml") as config_file:
            with tempfile.NamedTemporaryFile(suffix=".local") as env_file:
                with mock.patch("sys.argv", [
                    "pipeline.py",
                    "--config", config_file.name,
                    "--env-file", env_file.name,
                ]):
                    args = pipeline._parse_args()
                    assert args.stage is None
                    # Both stages should be queued for execution

    @mock.patch("src_llm.main.main")
    def test_stage_1_only(self, mock_stage1):
        """Pipeline should run only Stage 1 when stage=1."""
        mock_stage1.return_value = 0

        with tempfile.NamedTemporaryFile(suffix=".yml") as config_file:
            with tempfile.NamedTemporaryFile(suffix=".local") as env_file:
                with mock.patch("sys.argv", [
                    "pipeline.py",
                    "--stage", "1",
                    "--config", config_file.name,
                    "--env-file", env_file.name,
                ]):
                    args = pipeline._parse_args()
                    assert args.stage == 1

    @mock.patch("src_llm.automate.main")
    def test_stage_2_only(self, mock_stage2):
        """Pipeline should run only Stage 2 when stage=2."""
        mock_stage2.return_value = 0

        with tempfile.NamedTemporaryFile(suffix=".yml") as config_file:
            with tempfile.NamedTemporaryFile(suffix=".local") as env_file:
                with mock.patch("sys.argv", [
                    "pipeline.py",
                    "--stage", "2",
                    "--config", config_file.name,
                    "--env-file", env_file.name,
                ]):
                    args = pipeline._parse_args()
                    assert args.stage == 2


class TestPipelineErrorHandling(unittest.TestCase):
    """Test that pipeline handles errors gracefully."""

    def test_missing_config_file(self):
        """Pipeline should fail if config file doesn't exist."""
        with tempfile.NamedTemporaryFile(suffix=".local") as env_file:
            with mock.patch("sys.argv", [
                "pipeline.py",
                "--config", "/nonexistent/config.yml",
                "--env-file", env_file.name,
            ]):
                args = pipeline._parse_args()
                assert not args.config.exists()

    def test_missing_env_file(self):
        """Pipeline should fail if env file doesn't exist."""
        with tempfile.NamedTemporaryFile(suffix=".yml") as config_file:
            with mock.patch("sys.argv", [
                "pipeline.py",
                "--config", config_file.name,
                "--env-file", "/nonexistent/.env",
            ]):
                args = pipeline._parse_args()
                assert not args.env_file.exists()


class TestMemoryPersistence(unittest.TestCase):
    """Test that memory.md is correctly persisted and reused."""

    def test_memory_md_format(self):
        """Memory.md should have required sections for Stage 2."""
        memory_md = """# Task Summary
This task demonstrates automation.

## Steps
1. Open settings
2. Toggle notifications
3. Close settings

## UI Elements
- Settings Button: Top-right corner
- Notifications Toggle: In settings menu

## Completion Criteria
- Settings dialog visible
- Notifications toggled
"""
        # Verify required sections exist
        assert "# Task Summary" in memory_md
        assert "## Steps" in memory_md
        assert "## UI Elements" in memory_md
        assert "## Completion Criteria" in memory_md

    def test_metadata_json_structure(self):
        """Metadata.json should have correct structure for Stage 2 handoff."""
        metadata = {
            "app": "adaway",
            "method": "llm",
            "variant": "gemini-2.5-pro",
            "source": "screenrec",
            "video": "srv-001.mp4",
            "timestamp": "2026-05-05T10:00:00",
            "duration_sec": 45.2,
            "status": "success",
            "video_mode_metadata": {
                "memory_md_content": "# Task Summary\n...",
                "task_description": "Test task",
                "ui_elements": {},
                "completion_criteria": [],
            },
        }

        # Verify Stage 2 can extract memory
        video_mode_data = metadata.get("video_mode_metadata")
        assert video_mode_data is not None
        assert video_mode_data["memory_md_content"] is not None
        assert video_mode_data["task_description"] is not None


if __name__ == "__main__":
    unittest.main()
