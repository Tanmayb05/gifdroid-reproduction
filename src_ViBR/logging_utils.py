from __future__ import annotations

import json
import logging
import re
import sys
from pathlib import Path


_PROJECT_ROOT: Path | None = None


def set_project_root(root: Path) -> None:
    """Set the project root for relative path display."""
    global _PROJECT_ROOT
    _PROJECT_ROOT = root


def _shorten_path(path_str: str) -> str:
    """Convert absolute paths to relative paths from project root."""
    if not path_str or not isinstance(path_str, str):
        return str(path_str)

    if _PROJECT_ROOT:
        try:
            p = Path(path_str)
            relative = p.relative_to(_PROJECT_ROOT)
            return str(relative)
        except (ValueError, TypeError):
            pass
    return path_str


def _format_json_summary(text: str) -> str:
    """Format multi-line JSON as single-line summary with key info."""
    try:
        data = json.loads(text)
        if isinstance(data, dict):
            # For state consistency responses, extract key info
            if "same_state" in data:
                desc = data.get("description", "")
                desc_short = (desc[:50] + "...") if len(desc) > 50 else desc
                return f'{{same_state: {data["same_state"]}, desc: "{desc_short}"}}'
            # For action responses, show action only
            if "action" in data:
                return f'{{action: {data["action"]}}}'
            # For region responses, show count of regions
            if "target_regions" in data:
                regions = data.get("target_regions", [])
                action = data.get("predicted_action", "unknown")
                return f'{{regions: {len(regions)}, action: {action}}}'
        return text
    except (json.JSONDecodeError, TypeError):
        return text


class _CompactFormatter(logging.Formatter):
    """Custom formatter that shortens paths and formats JSON responses."""

    def format(self, record: logging.LogRecord) -> str:
        # Shorten file paths in message
        if record.pathname:
            record.pathname = _shorten_path(record.pathname)

        # Format JSON responses compactly
        if record.msg and isinstance(record.msg, str):
            # Check if this is a Gemini response message
            if "Consistency Response" in record.msg or "Action Response" in record.msg or "Region Response" in record.msg:
                # Try to extract and format JSON from message
                json_match = re.search(r'\{.*\}', record.msg, re.DOTALL)
                if json_match:
                    json_str = json_match.group(0)
                    formatted = _format_json_summary(json_str)
                    prefix = record.msg[:json_match.start()].rstrip()
                    record.msg = f"{prefix} {formatted}"

        return super().format(record)


def _filter_library_warnings(record: logging.LogRecord) -> bool:
    """Filter out noisy warnings from dependencies that can't be easily fixed."""
    message = record.getMessage()

    # Suppress gradient-related warnings (common in inference, harmless)
    if "requires_grad=True" in message and "Gradients will be None" in message:
        return False

    return True


def setup_logger(log_path: Path, level: str) -> logging.Logger:
    log_path.parent.mkdir(parents=True, exist_ok=True)

    logger_name = f"src_vibr.{log_path.stem}"
    logger = logging.getLogger(logger_name)
    logger.setLevel(getattr(logging, level.upper(), logging.INFO))
    logger.propagate = False

    for handler in list(logger.handlers):
        logger.removeHandler(handler)

    formatter = _CompactFormatter(
        fmt="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler = logging.FileHandler(log_path, mode="a", encoding="utf-8")
    file_handler.setFormatter(formatter)
    file_handler.addFilter(_filter_library_warnings)
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(_filter_library_warnings)
    logger.addHandler(stream_handler)

    logger.info("=== %s ===", logger_name)
    return logger


def finalize_log_file(log_path: Path, final_status: str) -> Path:
    new_name = log_path.name.replace("__started", f"__{final_status}")
    new_path = log_path.parent / new_name
    if log_path.exists() and not new_path.exists():
        log_path.rename(new_path)
    return new_path
