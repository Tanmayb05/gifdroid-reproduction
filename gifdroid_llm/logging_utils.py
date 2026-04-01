from __future__ import annotations

import logging
from pathlib import Path


def setup_logger(log_path: Path, level: str) -> logging.Logger:
    """Create a structured file logger and return it."""
    log_path.parent.mkdir(parents=True, exist_ok=True)

    logger_name = f"gifdroid_llm.{log_path.stem}"
    logger = logging.getLogger(logger_name)
    logger.setLevel(getattr(logging, level.upper(), logging.INFO))
    logger.propagate = False

    for handler in list(logger.handlers):
        logger.removeHandler(handler)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler = logging.FileHandler(log_path, mode="a", encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    logger.info("=== %s ===", logger_name)

    return logger


def finalize_log_file(log_path: Path, final_status: str) -> Path:
    """Rename the log file from __started to the final status."""
    new_name = log_path.name.replace("__started", f"__{final_status}")
    new_path = log_path.parent / new_name
    if log_path.exists() and not new_path.exists():
        log_path.rename(new_path)
    return new_path
