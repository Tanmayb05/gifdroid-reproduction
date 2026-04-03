from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List

import yaml


class ConfigError(ValueError):
    """Raised when config values are missing or invalid."""


@dataclass(frozen=True)
class FrameSamplingConfig:
    strategy: str
    fps: float
    max_frames: int


@dataclass(frozen=True)
class KeyframeSelectionConfig:
    method: str
    min_gap_seconds: float
    stable_threshold: int
    ssim_threshold: float


@dataclass(frozen=True)
class OutputConfig:
    overwrite: bool


@dataclass(frozen=True)
class LoggingConfig:
    level: str


@dataclass(frozen=True)
class AppConfig:
    app_name: str
    video_path: Path
    llm: str
    llm_model: str
    llm_prompt_file: Path | None
    frame_sampling: FrameSamplingConfig
    keyframe_selection: KeyframeSelectionConfig
    output: OutputConfig
    logging: LoggingConfig


@dataclass(frozen=True)
class PipelineConfig:
    """Top-level config holding shared settings and one or more runs."""
    runs: List[AppConfig]


def _require_mapping(data: Any, section: str) -> Dict[str, Any]:
    if not isinstance(data, dict):
        raise ConfigError(f"Section '{section}' must be a mapping")
    return data


def _require_str(data: Dict[str, Any], key: str) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ConfigError(f"Field '{key}' must be a non-empty string")
    return value.strip()


def _optional_str(data: Dict[str, Any], key: str) -> str | None:
    value = data.get(key)
    if value is None:
        return None
    if not isinstance(value, str) or not value.strip():
        raise ConfigError(f"Field '{key}' must be a non-empty string when provided")
    return value.strip()


def _require_bool(data: Dict[str, Any], key: str) -> bool:
    value = data.get(key)
    if not isinstance(value, bool):
        raise ConfigError(f"Field '{key}' must be a boolean")
    return value


def _require_number(data: Dict[str, Any], key: str) -> float:
    value = data.get(key)
    if not isinstance(value, (int, float)):
        raise ConfigError(f"Field '{key}' must be a number")
    return float(value)


def _require_int(data: Dict[str, Any], key: str) -> int:
    value = data.get(key)
    if not isinstance(value, int):
        raise ConfigError(f"Field '{key}' must be an integer")
    return value



def _validate_frame_sampling(raw: Dict[str, Any]) -> FrameSamplingConfig:
    strategy = _require_str(raw, "strategy").lower()
    if strategy not in {"uniform", "adaptive"}:
        raise ConfigError("frame_sampling.strategy must be 'uniform' or 'adaptive'")

    fps = _require_number(raw, "fps")
    if fps <= 0:
        raise ConfigError("frame_sampling.fps must be > 0")

    max_frames = _require_int(raw, "max_frames")
    if max_frames <= 0:
        raise ConfigError("frame_sampling.max_frames must be > 0")

    return FrameSamplingConfig(strategy=strategy, fps=fps, max_frames=max_frames)


def _validate_keyframe_selection(raw: Dict[str, Any]) -> KeyframeSelectionConfig:
    method = _require_str(raw, "method").lower()
    if method not in {"heuristic", "llm_assisted", "ssim"}:
        raise ConfigError(
            "keyframe_selection.method must be 'heuristic', 'llm_assisted', or 'ssim'"
        )

    min_gap = _require_number(raw, "min_gap_seconds")
    if min_gap < 0:
        raise ConfigError("keyframe_selection.min_gap_seconds must be >= 0")

    stable_threshold_raw = raw.get("stable_threshold", 2)
    if not isinstance(stable_threshold_raw, int):
        raise ConfigError("keyframe_selection.stable_threshold must be an integer when provided")
    if stable_threshold_raw < 0:
        raise ConfigError("keyframe_selection.stable_threshold must be >= 0")

    ssim_threshold_raw = raw.get("ssim_threshold", 0.95)
    if not isinstance(ssim_threshold_raw, (int, float)):
        raise ConfigError("keyframe_selection.ssim_threshold must be a number when provided")
    ssim_threshold = float(ssim_threshold_raw)
    if ssim_threshold <= 0 or ssim_threshold > 1:
        raise ConfigError("keyframe_selection.ssim_threshold must be in (0, 1]")

    return KeyframeSelectionConfig(
        method=method,
        min_gap_seconds=min_gap,
        stable_threshold=stable_threshold_raw,
        ssim_threshold=ssim_threshold,
    )


def _validate_logging(raw: Dict[str, Any]) -> LoggingConfig:
    level = _require_str(raw, "level").upper()
    allowed = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}
    if level not in allowed:
        raise ConfigError(f"logging.level must be one of {sorted(allowed)}")
    return LoggingConfig(level=level)


def _parse_shared(root: Dict[str, Any]) -> tuple:
    """Parse shared settings (llm, frame_sampling, etc.) from root mapping."""
    llm = _require_str(root, "llm").lower()
    llm_model = _optional_str(root, "llm_model")
    llm_prompt_file_raw = _optional_str(root, "llm_prompt_file")
    llm_prompt_file = (
        Path(llm_prompt_file_raw) if llm_prompt_file_raw else None
    )
    if llm_model is None:
        default_models = {
            "gemini": "gemini-1.5-flash",
            "llama": "llama3.2-vision:latest",
            "llava": "llava:13b",
            "minicpm": "minicpm-v:latest",
            "gemma": "gemma3:4b",
            "qwen": "qwen2.5vl:7b",
        }
        llm_model = default_models.get(llm, llm)

    frame_sampling = _validate_frame_sampling(
        _require_mapping(root.get("frame_sampling"), "frame_sampling")
    )
    keyframe_selection = _validate_keyframe_selection(
        _require_mapping(root.get("keyframe_selection"), "keyframe_selection")
    )
    output_cfg = OutputConfig(
        overwrite=_require_bool(_require_mapping(root.get("output"), "output"), "overwrite")
    )
    logging_cfg = _validate_logging(_require_mapping(root.get("logging"), "logging"))
    return (
        llm,
        llm_model,
        llm_prompt_file,
        frame_sampling,
        keyframe_selection,
        output_cfg,
        logging_cfg,
    )


def _parse_video_paths(value: Any) -> List[Path]:
    """Parse video_path as scalar or list and return Path values."""
    if isinstance(value, list):
        if len(value) == 0:
            raise ConfigError("Field 'video_path' list must be non-empty")
        paths: List[Path] = []
        for i, item in enumerate(value):
            if not isinstance(item, str) or not item.strip():
                raise ConfigError(
                    f"Field 'video_path[{i}]' must be a non-empty string"
                )
            paths.append(Path(item.strip()))
        return paths
    if not isinstance(value, str) or not value.strip():
        raise ConfigError("Field 'video_path' must be a non-empty string or a non-empty list")
    return [Path(value.strip())]


def _parse_run_entry(entry: Any, idx: int, shared: tuple) -> List[AppConfig]:
    """Parse one run entry and expand video_path list into one AppConfig per video."""
    if not isinstance(entry, dict):
        raise ConfigError(f"runs[{idx}] must be a mapping")
    (
        llm,
        llm_model,
        llm_prompt_file,
        frame_sampling,
        keyframe_selection,
        output_cfg,
        logging_cfg,
    ) = shared
    app_name = _require_str(entry, "app_name")
    video_paths = _parse_video_paths(entry.get("video_path"))
    return [
        AppConfig(
            app_name=app_name,
            video_path=video_path,
            llm=llm,
            llm_model=llm_model,
            llm_prompt_file=llm_prompt_file,
            frame_sampling=frame_sampling,
            keyframe_selection=keyframe_selection,
            output=output_cfg,
            logging=logging_cfg,
        )
        for video_path in video_paths
    ]


def load_config(config_path: Path) -> PipelineConfig:
    """Load and validate pipeline config from YAML.

    Supports two formats:
    - Single-run: top-level app_name / utg_number / video_path fields (legacy).
    - Multi-run: top-level ``runs`` list, each entry with app_name / utg_number / video_path.
      ``utg_number`` and ``video_path`` can each be scalar or list values in runs entries.
    """
    if not config_path.exists():
        raise ConfigError(f"Config file not found: {config_path}")

    with config_path.open("r", encoding="utf-8") as f:
        raw = yaml.safe_load(f)

    root_obj = _require_mapping(raw, "config")
    # Support optional nested "config" wrapper.
    if "config" in root_obj and isinstance(root_obj["config"], dict):
        root = root_obj["config"]
    else:
        root = root_obj

    shared = _parse_shared(root)

    if "runs" in root:
        runs_raw = root["runs"]
        if not isinstance(runs_raw, list) or len(runs_raw) == 0:
            raise ConfigError("'runs' must be a non-empty list")
        runs: List[AppConfig] = []
        for i, entry in enumerate(runs_raw):
            runs.extend(_parse_run_entry(entry, i, shared))
    else:
        # Legacy single-run format
        app_name = _require_str(root, "app_name")
        video_path = Path(_require_str(root, "video_path"))
        (
            llm,
            llm_model,
            llm_prompt_file,
            frame_sampling,
            keyframe_selection,
            output_cfg,
            logging_cfg,
        ) = shared
        runs = [AppConfig(
            app_name=app_name,
            video_path=video_path,
            llm=llm,
            llm_model=llm_model,
            llm_prompt_file=llm_prompt_file,
            frame_sampling=frame_sampling,
            keyframe_selection=keyframe_selection,
            output=output_cfg,
            logging=logging_cfg,
        )]

    return PipelineConfig(runs=runs)
