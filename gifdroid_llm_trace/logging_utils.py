from __future__ import annotations

import logging
from pathlib import Path


def setup_logger(log_path: Path, level: str) -> logging.Logger:
    """Create a structured file logger and return it."""
    log_path.parent.mkdir(parents=True, exist_ok=True)

    logger_name = f"gifdroid_llm_trace.{log_path.stem}"
    logger = logging.getLogger(logger_name)
    logger.setLevel(getattr(logging, level.upper(), logging.INFO))
    logger.propagate = False

    for handler in list(logger.handlers):
        logger.removeHandler(handler)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler = logging.FileHandler(log_path, encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger
