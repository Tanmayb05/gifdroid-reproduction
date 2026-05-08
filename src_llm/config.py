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


VIDEO_MODE_SUPPORTED_PROVIDERS = {"gemini"}


@dataclass(frozen=True)
class AutomationRunConfig:
    """A single resolved automation run: one app + one video type."""
    app_name: str
    video_path: Path       # e.g. apps/adaway/videos/srv-001.mp4
    apk_path: Path         # e.g. apps/adaway/apk/adaway.apk
    video_type: str        # "screenrec" | "handheld"
    llm: str
    llm_model: str
    device_serial: str | None
    max_steps: int
    history_window: int
    step_delay: float
    stall_repeat_threshold: int  # stop if same action repeats this many times
    reset_between_runs: bool     # force-stop + clear app data after each run
    output_dir: Path | None  # None = auto-derive in automate.py


@dataclass(frozen=True)
class AutomationConfig:
    """Top-level automation config holding shared settings and one or more runs."""
    llm: str
    llm_model: str
    device_serial: str | None
    max_steps: int
    history_window: int
    step_delay: float
    stall_repeat_threshold: int
    reset_between_runs: bool
    output_dir: Path | None
    runs: List["AutomationRunConfig"]


_VIDEO_TYPE_MAP: Dict[str, str] = {
    "srv": "screenrec",
    "hhv": "handheld",
}


def _resolve_video_type(filename: str) -> str:
    """Infer video type from filename prefix (srv/hhv)."""
    for prefix, vtype in _VIDEO_TYPE_MAP.items():
        if filename.lower().startswith(prefix):
            return vtype
    raise ConfigError(
        f"Unknown video file '{filename}'. "
        f"Must start with 'srv' or 'hhv' prefix."
    )


def _build_run_configs(
    root: Dict[str, Any],
    llm: str,
    llm_model: str,
    device_serial: str | None,
    max_steps: int,
    history_window: int,
    step_delay: float,
    stall_repeat_threshold: int,
    reset_between_runs: bool,
    output_dir: "Path | None",
) -> "List[AutomationRunConfig]":
    """Parse the runs list and expand each entry into one AutomationRunConfig per video type."""
    runs_raw = root.get("runs")
    if not isinstance(runs_raw, list) or len(runs_raw) == 0:
        raise ConfigError("'runs' must be a non-empty list")

    result: List[AutomationRunConfig] = []
    for i, entry in enumerate(runs_raw):
        if not isinstance(entry, dict):
            raise ConfigError(f"runs[{i}] must be a mapping")

        app_name = _require_str(entry, "app_name")

        # apk_path: explicit or auto-derived as apps/<app>/apk/<app>.apk
        apk_raw = _optional_str(entry, "apk_path")
        apk_path = Path(apk_raw) if apk_raw else Path(f"apps/{app_name}/apk/{app_name}.apk")

        # video_path: list of shorthands (srv, hhv) or explicit paths
        vp_raw = entry.get("video_path")
        if vp_raw is None:
            raise ConfigError(f"runs[{i}].video_path is required")
        if isinstance(vp_raw, str):
            vp_raw = [vp_raw]
        if not isinstance(vp_raw, list) or len(vp_raw) == 0:
            raise ConfigError(f"runs[{i}].video_path must be a non-empty string or list")

        for vp_entry in vp_raw:
            if not isinstance(vp_entry, str) or not vp_entry.strip():
                raise ConfigError(f"runs[{i}].video_path entries must be non-empty strings")
            vp_entry = vp_entry.strip()

            # If it looks like a full path (contains '/'), use it directly
            if "/" in vp_entry:
                video_path = Path(vp_entry)
                video_type = _resolve_video_type(video_path.name)
            else:
                # Shorthand or filename: resolve to flat videos directory
                # Support: "srv", "hhv", "srv-001.mp4", "hhv-002.mp4", etc.
                video_type = _resolve_video_type(vp_entry)
                filename = vp_entry if vp_entry.endswith(".mp4") else f"{vp_entry}.mp4"
                video_path = Path(f"apps/{app_name}/videos/{filename}")

            # Per-run overrides
            run_max_steps = entry.get("max_steps", max_steps)
            run_output_dir_raw = _optional_str(entry, "output_dir")
            run_output_dir = Path(run_output_dir_raw) if run_output_dir_raw else output_dir

            result.append(AutomationRunConfig(
                app_name=app_name,
                video_path=video_path,
                apk_path=apk_path,
                video_type=video_type,
                llm=llm,
                llm_model=llm_model,
                device_serial=device_serial,
                max_steps=run_max_steps,
                history_window=history_window,
                step_delay=step_delay,
                stall_repeat_threshold=stall_repeat_threshold,
                reset_between_runs=reset_between_runs,
                output_dir=run_output_dir,
            ))

    return result


def load_automation_config(config_path: Path) -> "AutomationConfig":
    """Load and validate automation config from YAML.

    Supports a multi-run format with a top-level ``runs`` list. Each run entry
    specifies ``app_name`` and ``video_path`` (list of shorthands or explicit paths).
    Shared settings (llm, max_steps, etc.) are defined at the top level and can be
    overridden per run.
    """
    if not config_path.exists():
        raise ConfigError(f"Automation config file not found: {config_path}")

    with config_path.open("r", encoding="utf-8") as f:
        raw = yaml.safe_load(f)

    root: Dict[str, Any] = _require_mapping(raw, "config")

    # --- Shared settings ---
    llm = _require_str(root, "llm").lower()
    llm_model = _normalize_model_slug(_optional_str(root, "llm_model") or "gemini-2.5-pro")
    device_serial = _optional_str(root, "device_serial")

    max_steps_raw = root.get("max_steps", 10)
    if not isinstance(max_steps_raw, int) or max_steps_raw <= 0:
        raise ConfigError("max_steps must be a positive integer")
    max_steps = max_steps_raw

    history_window_raw = root.get("history_window", 3)
    if not isinstance(history_window_raw, int) or history_window_raw <= 0:
        raise ConfigError("history_window must be a positive integer")
    history_window = history_window_raw

    step_delay_raw = root.get("step_delay", 1.5)
    if not isinstance(step_delay_raw, (int, float)) or step_delay_raw < 0:
        raise ConfigError("step_delay must be a non-negative number")
    step_delay = float(step_delay_raw)

    stall_repeat_threshold_raw = root.get("stall_repeat_threshold", 4)
    if not isinstance(stall_repeat_threshold_raw, int) or stall_repeat_threshold_raw < 2:
        raise ConfigError("stall_repeat_threshold must be an integer >= 2")
    stall_repeat_threshold = stall_repeat_threshold_raw

    reset_between_runs_raw = root.get("reset_between_runs", True)
    if not isinstance(reset_between_runs_raw, bool):
        raise ConfigError("reset_between_runs must be a boolean")
    reset_between_runs = reset_between_runs_raw

    output_dir_raw = _optional_str(root, "output_dir")
    output_dir = Path(output_dir_raw) if output_dir_raw else None

    # --- Runs ---
    runs = _build_run_configs(
        root, llm, llm_model, device_serial,
        max_steps, history_window, step_delay, stall_repeat_threshold,
        reset_between_runs, output_dir,
    )

    return AutomationConfig(
        llm=llm,
        llm_model=llm_model,
        device_serial=device_serial,
        max_steps=max_steps,
        history_window=history_window,
        step_delay=step_delay,
        stall_repeat_threshold=stall_repeat_threshold,
        reset_between_runs=reset_between_runs,
        output_dir=output_dir,
        runs=runs,
    )


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
    video_mode: bool = True


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


def _normalize_model_slug(model_str: str) -> str:
    """Normalize model name to lowercase with hyphens and dots.

    Examples: "Gemini-2.5-Pro" -> "gemini-2.5-pro"
    """
    import re
    normalized = re.sub(r"[^a-z0-9.-]+", "-", model_str.lower()).strip("-")
    return normalized


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
            "gemini": "gemini-2.5-pro",
            "llama": "llama3.2-vision:latest",
            "llava": "llava:13b",
            "minicpm": "minicpm-v:latest",
            "gemma": "gemma3:4b",
            "qwen": "qwen2.5vl:7b",
        }
        llm_model = default_models.get(llm, llm)

    llm_model = _normalize_model_slug(llm_model)

    video_mode = bool(root.get("video_mode", True))
    if video_mode and llm not in VIDEO_MODE_SUPPORTED_PROVIDERS:
        supported = ", ".join(sorted(VIDEO_MODE_SUPPORTED_PROVIDERS))
        raise ConfigError(
            f"video_mode: true requires a supported provider. "
            f"Got llm='{llm}', supported: {supported}"
        )

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
        video_mode,
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
        video_mode,
    ) = shared
    app_name = _require_str(entry, "app_name")
    vp_raw = entry.get("video_path")
    if vp_raw is None:
        raise ConfigError(f"runs[{idx}].video_path is required")
    if isinstance(vp_raw, str):
        vp_raw = [vp_raw]
    if not isinstance(vp_raw, list) or len(vp_raw) == 0:
        raise ConfigError(f"runs[{idx}].video_path must be a non-empty string or list")

    result: List[AppConfig] = []
    for vp_entry in vp_raw:
        if not isinstance(vp_entry, str) or not vp_entry.strip():
            raise ConfigError(f"runs[{idx}].video_path entries must be non-empty strings")
        vp_entry = vp_entry.strip()

        # If it looks like a full path (contains '/'), use it directly
        if "/" in vp_entry:
            video_path = Path(vp_entry)
        else:
            # Shorthand or filename: resolve to flat videos directory
            # Support: "srv", "hhv", "srv-001.mp4", "hhv-002.mp4", etc.
            filename = vp_entry if vp_entry.endswith(".mp4") else f"{vp_entry}.mp4"
            video_path = Path(f"apps/{app_name}/videos/{filename}")

        result.append(AppConfig(
            app_name=app_name,
            video_path=video_path,
            llm=llm,
            llm_model=llm_model,
            llm_prompt_file=llm_prompt_file,
            frame_sampling=frame_sampling,
            keyframe_selection=keyframe_selection,
            output=output_cfg,
            logging=logging_cfg,
            video_mode=video_mode,
        ))
    return result


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
            video_mode,
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
            video_mode=video_mode,
        )]

    return PipelineConfig(runs=runs)
