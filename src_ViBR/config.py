from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


SUPPORTED_ALGORITHMS = {"clip", "ssim"}
SUPPORTED_LLMS = {"openai", "gemini"}
DEFAULT_MODELS = {
    "openai": "gpt-4o",
    "gemini": "gemini-1.5-flash",
}
VIDEO_TYPE_ALIASES = {
    "screenrec": "screenrec",
    "srv": "screenrec",
    "handheld": "handheld",
    "hhv": "handheld",
}
VIDEO_PREFIX = {
    "screenrec": "srv",
    "handheld": "hhv",
}


class ConfigError(ValueError):
    """Raised when config values are missing or invalid."""


@dataclass(frozen=True)
class OutputConfig:
    overwrite: bool


@dataclass(frozen=True)
class LoggingConfig:
    level: str


@dataclass(frozen=True)
class ViBRRunConfig:
    app_name: str
    video_path: Path
    algorithm: str
    llm: str
    llm_model: str


@dataclass(frozen=True)
class ViBRPipelineConfig:
    output: OutputConfig
    logging: LoggingConfig
    runs: list[ViBRRunConfig]


def _require_mapping(data: Any, section: str) -> dict[str, Any]:
    if not isinstance(data, dict):
        raise ConfigError(f"Section '{section}' must be a mapping")
    return data


def _require_non_empty_str(data: dict[str, Any], key: str) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ConfigError(f"Field '{key}' must be a non-empty string")
    return value.strip()


def _resolve_llm(run: dict[str, Any], default_llm: str, default_llm_model: str) -> tuple[str, str]:
    raw_llm = run.get("llm", default_llm)
    if not isinstance(raw_llm, str) or not raw_llm.strip():
        raise ConfigError("Run field 'llm' must be a non-empty string when provided")
    llm = raw_llm.strip().lower()
    if llm not in SUPPORTED_LLMS:
        raise ConfigError(f"llm must be one of {sorted(SUPPORTED_LLMS)}")

    raw_model = run.get("llm_model", None)
    if raw_model is not None:
        if not isinstance(raw_model, str) or not raw_model.strip():
            raise ConfigError("Run field 'llm_model' must be a non-empty string when provided")
        llm_model = raw_model.strip()
    elif llm == default_llm:
        llm_model = default_llm_model
    else:
        llm_model = DEFAULT_MODELS[llm]
    return llm, llm_model


def _resolve_algorithm(run: dict[str, Any], default_algorithm: str) -> str:
    raw = run.get("algorithm", default_algorithm)
    if not isinstance(raw, str) or not raw.strip():
        raise ConfigError("Run field 'algorithm' must be a non-empty string when provided")
    algo = raw.strip().lower()
    if algo not in SUPPORTED_ALGORITHMS:
        raise ConfigError(f"algorithm must be one of {sorted(SUPPORTED_ALGORITHMS)}")
    return algo


def _parse_video_path_list(value: Any) -> list[Path]:
    if isinstance(value, list):
        if not value:
            raise ConfigError("Field 'video_path' list must be non-empty")
        paths: list[Path] = []
        for i, item in enumerate(value):
            if not isinstance(item, str) or not item.strip():
                raise ConfigError(f"Field 'video_path[{i}]' must be a non-empty string")
            paths.append(Path(item.strip()))
        return paths
    if isinstance(value, str) and value.strip():
        return [Path(value.strip())]
    raise ConfigError("Field 'video_path' must be a non-empty string or a non-empty list")


def _expand_video_path(app_name: str, video_path: Path) -> Path:
    raw = video_path.as_posix().strip().lower()
    if raw in VIDEO_TYPE_ALIASES:
        video_type = VIDEO_TYPE_ALIASES[raw]
        prefix = VIDEO_PREFIX[video_type]
        return Path(f"apps/{app_name}/videos/{video_type}/{prefix}-001.mp4")
    return video_path


def _validate_output(root: dict[str, Any]) -> OutputConfig:
    section = _require_mapping(root.get("output"), "output")
    overwrite = section.get("overwrite")
    if not isinstance(overwrite, bool):
        raise ConfigError("output.overwrite must be a boolean")
    return OutputConfig(overwrite=overwrite)


def _validate_logging(root: dict[str, Any]) -> LoggingConfig:
    section = _require_mapping(root.get("logging"), "logging")
    level = section.get("level")
    if not isinstance(level, str) or not level.strip():
        raise ConfigError("logging.level must be a non-empty string")
    normalized = level.strip().upper()
    allowed = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}
    if normalized not in allowed:
        raise ConfigError(f"logging.level must be one of {sorted(allowed)}")
    return LoggingConfig(level=normalized)


def _parse_runs(
    root: dict[str, Any],
    default_algorithm: str,
    default_llm: str,
    default_llm_model: str,
) -> list[ViBRRunConfig]:
    runs_raw = root.get("runs")
    if not isinstance(runs_raw, list) or not runs_raw:
        raise ConfigError("'runs' must be a non-empty list")

    runs: list[ViBRRunConfig] = []
    for idx, run in enumerate(runs_raw):
        run_map = _require_mapping(run, f"runs[{idx}]")
        app_name = _require_non_empty_str(run_map, "app_name")
        video_values = _parse_video_path_list(run_map.get("video_path"))
        algorithm = _resolve_algorithm(run_map, default_algorithm)
        llm, llm_model = _resolve_llm(run_map, default_llm, default_llm_model)
        for video_value in video_values:
            resolved_video = _expand_video_path(app_name, video_value)
            runs.append(ViBRRunConfig(
                app_name=app_name,
                video_path=resolved_video,
                algorithm=algorithm,
                llm=llm,
                llm_model=llm_model,
            ))
    return runs


def load_config(config_path: Path) -> ViBRPipelineConfig:
    if not config_path.exists():
        raise ConfigError(f"Config file not found: {config_path}")

    with config_path.open("r", encoding="utf-8") as f:
        loaded = yaml.safe_load(f)

    root_obj = _require_mapping(loaded, "config")
    root = root_obj["config"] if isinstance(root_obj.get("config"), dict) else root_obj

    algorithm_raw = root.get("algorithm", "clip")
    if not isinstance(algorithm_raw, str) or not algorithm_raw.strip():
        raise ConfigError("Top-level 'algorithm' must be a non-empty string when provided")
    default_algorithm = algorithm_raw.strip().lower()
    if default_algorithm not in SUPPORTED_ALGORITHMS:
        raise ConfigError(f"algorithm must be one of {sorted(SUPPORTED_ALGORITHMS)}")

    llm_raw = root.get("llm", "openai")
    if not isinstance(llm_raw, str) or not llm_raw.strip():
        raise ConfigError("Top-level 'llm' must be a non-empty string when provided")
    default_llm = llm_raw.strip().lower()
    if default_llm not in SUPPORTED_LLMS:
        raise ConfigError(f"llm must be one of {sorted(SUPPORTED_LLMS)}")

    llm_model_raw = root.get("llm_model", None)
    if llm_model_raw is not None:
        if not isinstance(llm_model_raw, str) or not llm_model_raw.strip():
            raise ConfigError("Top-level 'llm_model' must be a non-empty string when provided")
        default_llm_model = llm_model_raw.strip()
    else:
        default_llm_model = DEFAULT_MODELS[default_llm]

    output_cfg = _validate_output(root)
    logging_cfg = _validate_logging(root)
    runs = _parse_runs(root, default_algorithm, default_llm, default_llm_model)
    return ViBRPipelineConfig(output=output_cfg, logging=logging_cfg, runs=runs)
