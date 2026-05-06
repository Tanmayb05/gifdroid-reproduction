# Two-Stage LLM Workflow Implementation Plan

## Overview
Implement a two-stage pipeline to eliminate redundant video analysis in device automation:
- **Stage 1 (src_llm.main)**: Analyze video once → generate memory.md + metadata.json
- **Stage 2 (src_llm.automate)**: Use pre-generated memory.md → automate without re-analyzing video

## Directory Structure Changes

### Current Structure
```
apps/<app>/llm/<provider>/<model>/<source>/<cfg_slug>/run-NNN/
  ├── memory.md
  ├── execution_trace.json
  ├── keyframes/
  └── metadata.json
```

### New Flat Structure
```
apps/<app>/llm/<model>/<source>-video-mode/run-NNN/     (video mode)
  ├── memory.md
  ├── metadata.json
  ├── session_trace.json
  └── logs/

apps/<app>/llm/<model>/<source>/run-NNN/                 (keyframe mode)
  ├── execution_trace.json
  ├── frames_manifest.json
  ├── keyframes/
  ├── metadata.json
  └── logs/

apps/<app>/llm/<model>/<source>-video-mode/dry-run/      (single dry-run, always overwritten)
  ├── memory.md
  ├── metadata.json
  └── logs/
```

**Key Changes:**
- Remove provider directory level (model name contains provider info: "gemini-2.5-pro")
- Add `-video-mode` suffix to source for video-mode runs (e.g., "screenrec-video-mode")
- No nested `video-mode/` directory
- Single `dry-run/` directory per model+source that gets overwritten on each dry-run
- Separate `dry-run/` from numbered runs

## Module Changes

### 1. src_llm/config.py

#### Changes to AppConfig
```python
@dataclass(frozen=True)
class AppConfig:
    app_name: str
    video_path: Path
    llm: str
    llm_model: str  # e.g., "gemini-2.5-pro" (includes provider)
    llm_prompt_file: Path | None
    frame_sampling: FrameSamplingConfig
    keyframe_selection: KeyframeSelectionConfig
    output: OutputConfig
    logging: LoggingConfig
    video_mode: bool = False  # defaults to False, set to True in YAML
```

#### Changes to load_config()
- Default `video_mode: true` in YAML config (users can override with `video_mode: false`)
- Validate llm_model format matches provider expectations
- Normalize all gemini models to use hyphen: `gemini-2.5-pro`, `gemini-2-flash`, etc.

#### New metadata structure helper
```python
@dataclass(frozen=True)
class MetadataConfig:
    """Stores minimal config needed to reconstruct automate context."""
    app_name: str
    llm: str
    llm_model: str
    source: str  # "handheld" or "screenrec"
    video_type: str  # "hhv" or "srv"
    video_file: str
    timestamp: str
    status: str
    memory_md_content: str | None  # Only for video_mode=true
    task_description: str  # From memory.md, structured
    ui_elements: dict  # From memory.md, structured
    completion_criteria: list[str]  # From memory.md, structured
```

### 2. src_llm/io_utils.py

#### Update OutputLayout
```python
@dataclass(frozen=True)
class OutputLayout:
    run_dir: Path
    keyframes_dir: Path
    execution_trace_json_path: Path
    memory_md_path: Path
    frames_manifest_path: Path
    metadata_path: Path
    log_file_path: Path
    run_id: str  # "run-NNN" or "dry-run"
    llm_raw_response_path: Path
    is_dry_run: bool  # New field to track if this is dry-run
```

#### Update create_output_layout()
```python
def create_output_layout(
    project_root: Path,
    cfg: AppConfig,
    video_type: VideoType,
    run_dt: datetime,
    is_dry_run: bool = False,
) -> OutputLayout:
    """Build output paths under apps/{app}/llm/{model}/{source}{-video-mode}/run-NNN/ or dry-run/"""
    
    # Normalize model name (ensure hyphens, lowercase)
    model_slug = _normalize_model_slug(cfg.llm_model)
    
    # Build source suffix
    source = "handheld" if video_type == "hhv" else "screenrec"
    source_dir = f"{source}-video-mode" if cfg.video_mode else source
    
    # Build cfg_slug only for non-video-mode
    cfg_slug = "video-mode" if cfg.video_mode else _build_cfg_slug(cfg.frame_sampling, cfg.keyframe_selection)
    
    run_parent = (
        project_root
        / "apps"
        / cfg.app_name.lower()
        / "llm"
        / model_slug
        / source_dir
    )
    
    if is_dry_run:
        run_id = "dry-run"
        run_dir = run_parent / run_id
    else:
        run_id = _next_run_id(run_parent)
        run_dir = run_parent / run_id
    
    # Rest of layout construction...
    return OutputLayout(
        run_dir=run_dir,
        # ... other fields ...
        run_id=run_id,
        is_dry_run=is_dry_run,
    )

def _normalize_model_slug(model_str: str) -> str:
    """Normalize model name to lowercase with hyphens.
    e.g., 'Gemini-2.5-Pro' -> 'gemini-2.5-pro'
    """
    return re.sub(r"[^a-z0-9-]+", "-", model_str.lower()).strip("-")
```

#### Update write_run_metadata()
```python
def write_run_metadata(
    path: Path,
    app_name: str,
    method: str,
    variant: str,
    source: str,
    video_file: str,
    llm_prompt_file: str | None,
    frame_sampling_cfg: FrameSamplingConfig | None,  # None for video_mode
    keyframe_selection_cfg: KeyframeSelectionConfig | None,  # None for video_mode
    run_dt: datetime,
    duration_sec: float,
    status: str,
    memory_md_content: str | None = None,  # New: memory.md content if video_mode
    task_description: str | None = None,  # New: parsed from memory.md
    ui_elements: dict | None = None,  # New: parsed from memory.md
    completion_criteria: list[str] | None = None,  # New: parsed from memory.md
) -> None:
    """Write metadata.json with optional video_mode metadata."""
    payload = {
        "app": app_name.lower(),
        "method": method,
        "variant": variant,
        "source": source,
        "video": video_file,
        "timestamp": run_dt.strftime("%Y-%m-%dT%H:%M:%S"),
        "duration_sec": round(duration_sec, 1),
        "status": status,
    }
    
    # Add config only for non-video-mode
    if frame_sampling_cfg and keyframe_selection_cfg:
        payload["config"] = {
            "llm_prompt_file": llm_prompt_file,
            "frame_sampling": dataclasses.asdict(frame_sampling_cfg),
            "keyframe_selection": dataclasses.asdict(keyframe_selection_cfg),
        }
    
    # Add video_mode metadata for Stage 2 consumption
    if memory_md_content:
        payload["video_mode_metadata"] = {
            "memory_md_content": memory_md_content,
            "task_description": task_description,
            "ui_elements": ui_elements or {},
            "completion_criteria": completion_criteria or [],
        }
    
    write_json(path, payload)
```

### 3. src_llm/providers.py

#### Add new methods to BaseLLMProvider
```python
class BaseLLMProvider(ABC):
    # ... existing methods ...
    
    def infer_memory_from_video(self, video_path: Path) -> str:
        """Analyze video and return structured markdown memory.
        
        Markdown format (for video_mode):
        # Task Summary
        [description of task]
        
        ## Steps
        1. Step 1 description
        2. Step 2 description
        ...
        
        ## UI Elements
        - Element 1: description
        - Element 2: description
        ...
        
        ## Completion Criteria
        - Criterion 1
        - Criterion 2
        ...
        """
        raise NotImplementedError(
            f"Provider '{self.llm_name}' does not support infer_memory_from_video(). "
            "Only 'gemini' is currently supported."
        )
```

#### Implement in GeminiProvider
```python
class GeminiProvider(BaseLLMProvider):
    def infer_memory_from_video(self, video_path: Path) -> str:
        """Analyze video and generate structured memory.md markdown."""
        self.logger.info(
            "Generating memory from video | model=%s | video=%s",
            self.llm_model, video_path.name,
        )
        
        # Extract key frames from video for analysis
        from src_llm.video import VideoFrameExtractor
        extractor = VideoFrameExtractor()
        frames, metadata = extractor.extract(video_path, sampling_config={...}, logger=self.logger)
        
        # Build prompt for memory generation
        prompt = self._build_memory_prompt(frames)
        
        try:
            raw_text = self._call_gemini(
                prompt=prompt,
                timeout_sec=120,  # Longer timeout for full video analysis
                request_kind="memory_inference",
            )
            memory_md = self._format_as_memory_md(raw_text)
            self.logger.info("Memory generated successfully")
            return memory_md
        except ProviderError as exc:
            self.logger.error("Failed to generate memory: %s", exc)
            raise
    
    def _build_memory_prompt(self, frames: List) -> str:
        """Build prompt to analyze video frames and extract memory."""
        # Encode frames as base64
        # Build detailed prompt asking for:
        # - Task summary
        # - Step-by-step breakdown
        # - UI elements involved
        # - Completion criteria
        pass
    
    def _format_as_memory_md(self, raw_response: str) -> str:
        """Convert LLM response into structured markdown."""
        # Parse JSON response and format as markdown with sections:
        # # Task Summary
        # ## Steps
        # ## UI Elements
        # ## Completion Criteria
        pass
```

### 4. src_llm/main.py

#### Update parse_args()
```python
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate an LLM-based execution trace from a bug video."
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("src_llm/input/config.yml"),
        help="Path to YAML config file.",
    )
    parser.add_argument(
        "--env-file",
        type=Path,
        default=Path(".env.local"),
        help="Path to .env file with provider credentials.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate config/env and output paths without processing video.",
    )
    return parser.parse_args()
```

#### Update run_single()
```python
def run_single(args: argparse.Namespace, cfg: AppConfig) -> int:
    project_root = Path.cwd()
    
    resolved_video_path, video_type = resolve_video_path(project_root, cfg)
    if not resolved_video_path.exists():
        raise VideoError(f"Video file not found: {resolved_video_path}")
    
    run_dt = datetime.now(timezone.utc)
    is_dry_run = args.dry_run
    layout = create_output_layout(project_root, cfg, video_type, run_dt, is_dry_run=is_dry_run)
    
    layout.run_dir.mkdir(parents=True, exist_ok=True)
    (layout.run_dir / "logs").mkdir(parents=True, exist_ok=True)
    
    logger = setup_logger(layout.log_file_path, cfg.logging.level)
    logger.info("Starting src_llm pipeline | dry_run=%s", is_dry_run)
    logger.info("Resolved video path: %s", resolved_video_path)
    
    pipeline_status = "failed"
    pipeline_start = datetime.now(timezone.utc)
    
    try:
        try:
            # For dry-run, we overwrite without checking
            if not is_dry_run:
                ensure_write_policy(cfg, layout.execution_trace_json_path, layout.memory_md_path, layout.keyframes_dir)
        except FileExistsError as exc:
            logger.warning("RUN SKIPPED — output already present: %s", exc)
            return 0
        
        if is_dry_run:
            logger.info("Dry-run completed successfully (provider/API preflight skipped)")
            print("Dry-run OK")
            pipeline_status = "success"
            return 0
        
        env = load_and_validate_env(args.env_file, cfg.llm)
        logger.info("Environment validated for llm=%s model=%s", cfg.llm, cfg.llm_model)
        
        # Provider setup...
        provider = create_provider(
            cfg.llm,
            cfg.llm_model,
            env,
            logger,
            llm_prompt_file=cfg.llm_prompt_file,
            video_mode=cfg.video_mode,
        )
        
        if cfg.llm == "gemini":
            logger.info("Running %s API preflight before trace generation", cfg.llm)
            provider.validate_connection()
        
        # STAGE 1: VIDEO MODE - Generate memory.md
        if cfg.video_mode:
            logger.info("Video mode enabled — analyzing video and generating memory")
            memory_text = provider.infer_memory_from_video(resolved_video_path)
            layout.memory_md_path.parent.mkdir(parents=True, exist_ok=True)
            layout.memory_md_path.write_text(memory_text, encoding="utf-8")
            logger.info("Memory trace written: %s", layout.memory_md_path)
            
            # Parse memory.md for metadata
            task_desc, ui_elements, completion_criteria = _parse_memory_md(memory_text)
        
        # STAGE 2: KEYFRAME MODE - Generate execution trace
        else:
            logger.info("Keyframe mode enabled — extracting frames and selecting keyframes")
            extractor = VideoFrameExtractor()
            sampled_frames, metadata = extractor.extract(resolved_video_path, cfg.frame_sampling, logger)
            
            selector = KeyframeSelector()
            keyframes = selector.select(sampled_frames, cfg.keyframe_selection, logger)
            selector.save_keyframes(keyframes, layout.keyframes_dir, video_type)
            
            provider_actions = provider.infer_actions(keyframes)
            
            # Build trace...
            steps = []
            for idx, (keyframe, action) in enumerate(zip(keyframes, provider_actions), start=1):
                steps.append(TraceStep(...))
            
            trace_builder = TraceBuilder()
            trace_payload = trace_builder.build(...)
            
            manifest_payload = selector.build_frames_manifest(...)
            manifest_payload["video_metadata"] = metadata
            
            write_json(layout.execution_trace_json_path, trace_payload)
            write_json(layout.frames_manifest_path, manifest_payload)
            
            task_desc, ui_elements, completion_criteria = None, None, None
        
        # Save raw LLM response if available
        if provider.raw_llm_response is not None:
            layout.llm_raw_response_path.parent.mkdir(parents=True, exist_ok=True)
            layout.llm_raw_response_path.write_text(provider.raw_llm_response, encoding="utf-8")
            logger.info("LLM raw response written: %s", layout.llm_raw_response_path)
        
        # Write run metadata
        duration_sec = (datetime.now(timezone.utc) - pipeline_start).total_seconds()
        video_file = resolved_video_path.name
        source = "handheld" if video_type == "hhv" else "screenrec"
        model_slug = _normalize_model_slug(cfg.llm_model)
        
        write_run_metadata(
            path=layout.metadata_path,
            app_name=cfg.app_name,
            method="llm",
            variant=model_slug,
            source=source,
            video_file=video_file,
            llm_prompt_file=str(cfg.llm_prompt_file) if cfg.llm_prompt_file is not None else None,
            frame_sampling_cfg=cfg.frame_sampling if not cfg.video_mode else None,
            keyframe_selection_cfg=cfg.keyframe_selection if not cfg.video_mode else None,
            run_dt=run_dt,
            duration_sec=duration_sec,
            status="success",
            memory_md_content=memory_text if cfg.video_mode else None,
            task_description=task_desc,
            ui_elements=ui_elements,
            completion_criteria=completion_criteria,
        )
        
        pipeline_status = "success"
        output_path = layout.memory_md_path if cfg.video_mode else layout.execution_trace_json_path
        print(str(output_path))
        return 0
    
    finally:
        for handler in list(logger.handlers):
            handler.close()
            logger.removeHandler(handler)
        finalize_log_file(layout.log_file_path, pipeline_status)

def _parse_memory_md(memory_text: str) -> tuple:
    """Extract structured data from memory.md markdown.
    
    Returns: (task_description, ui_elements_dict, completion_criteria_list)
    """
    import re
    
    task_desc = ""
    ui_elements = {}
    completion_criteria = []
    
    # Parse "# Task Summary" section
    task_match = re.search(r'# Task Summary\n(.*?)(?=\n## |\Z)', memory_text, re.DOTALL)
    if task_match:
        task_desc = task_match.group(1).strip()
    
    # Parse "## UI Elements" section
    ui_match = re.search(r'## UI Elements\n(.*?)(?=\n## |\Z)', memory_text, re.DOTALL)
    if ui_match:
        for line in ui_match.group(1).split('\n'):
            if line.startswith('- '):
                parts = line[2:].split(':', 1)
                if len(parts) == 2:
                    ui_elements[parts[0].strip()] = parts[1].strip()
    
    # Parse "## Completion Criteria" section
    criteria_match = re.search(r'## Completion Criteria\n(.*?)(?=\n## |\Z)', memory_text, re.DOTALL)
    if criteria_match:
        for line in criteria_match.group(1).split('\n'):
            if line.startswith('- '):
                completion_criteria.append(line[2:].strip())
    
    return task_desc, ui_elements, completion_criteria

def _normalize_model_slug(model_str: str) -> str:
    """Normalize model name to lowercase with hyphens."""
    return re.sub(r"[^a-z0-9-]+", "-", model_str.lower()).strip("-")
```

### 5. src_llm/automate.py

#### Update parse_args()
```python
def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="python -m src_llm.automate",
        description="Device automation using pre-generated memory from Stage 1.",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("src_llm/input/automation_config.yml"),
        help="Path to automation_config.yml (default: src_llm/input/automation_config.yml)",
    )
    parser.add_argument("--env-file", type=Path, default=None, help="Path to .env file")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate config and imports then exit without running automation",
    )
    return parser.parse_args(argv)
```

#### Update _resolve_output_dir()
```python
def _resolve_output_dir(run, llm: str, llm_model: str) -> Path:
    """Return the output dir for a run, auto-deriving if not set in config.
    
    Auto-derived path (video mode only):
        apps/<app>/llm/<model>/<video_type>-video-mode/run-NNN
    """
    if run.output_dir is not None:
        return run.output_dir
    
    model_slug = _normalize_model_slug(llm_model)
    source_suffix = f"{run.video_type}-video-mode"
    
    base = Path("apps") / run.app_name / "llm" / model_slug / source_suffix
    existing = sorted(base.glob("run-*")) if base.exists() else []
    next_idx = len(existing) + 1
    return base / f"run-{next_idx:03d}"

def _normalize_model_slug(model_str: str) -> str:
    """Normalize model name to lowercase with hyphens."""
    import re
    return re.sub(r"[^a-z0-9-]+", "-", model_str.lower()).strip("-")
```

#### New helper: Load metadata from run
```python
def _load_run_metadata(run_dir: Path) -> dict:
    """Load metadata.json from a completed run.
    
    Returns: dict with keys like video_mode_metadata, task_description, etc.
    """
    metadata_path = run_dir / "metadata.json"
    if not metadata_path.exists():
        raise FileNotFoundError(f"metadata.json not found in {run_dir}")
    
    with metadata_path.open("r", encoding="utf-8") as f:
        return json.load(f)
```

#### New helper: Locate latest run for app
```python
def _locate_latest_run(app_name: str, llm_model: str, video_type: str) -> Path:
    """Locate the latest run for an app+model+video_type combination.
    
    Searches: apps/<app>/llm/<model>/<video_type>-video-mode/run-*/metadata.json
    Returns: Path to run directory (e.g., apps/adaway/llm/gemini-2.5-pro/screenrec-video-mode/run-001)
    Raises: FileNotFoundError if no run found
    """
    model_slug = _normalize_model_slug(llm_model)
    source_dir = f"{video_type}-video-mode"
    
    base = Path("apps") / app_name / "llm" / model_slug / source_dir
    if not base.exists():
        raise FileNotFoundError(f"No runs found for {app_name} | {model_slug} | {source_dir}")
    
    existing = sorted(base.glob("run-*"), key=lambda p: int(p.name[4:]))
    if not existing:
        raise FileNotFoundError(f"No numbered runs in {base}")
    
    return existing[-1]  # Return latest run
```

#### Update _run_single()
```python
def _run_single(run, env: dict, logger: logging.Logger, dry_run: bool) -> dict | None:
    """Execute one automation run using pre-generated memory.md.
    
    Flow:
    1. Locate latest run for app+model+video_type
    2. Load metadata.json from that run
    3. Extract memory.md content + task description
    4. Run automation using memory (not video)
    """
    output_dir = _resolve_output_dir(run, run.llm, run.llm_model)
    
    # Attach per-run file handler
    file_handler: logging.FileHandler | None = None
    if not dry_run:
        log_dir = output_dir / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_dir / "automate.log", encoding="utf-8")
        file_handler.setFormatter(logging.Formatter(
            "[%(levelname)s] %(asctime)s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        ))
        logger.addHandler(file_handler)
    
    logger.info(
        "--- Run: app=%s video_type=%s ---",
        run.app_name, run.video_type,
    )
    logger.info("Output dir: %s", output_dir)
    
    if dry_run:
        if not run.apk_path.exists():
            logger.error("APK not found: %s", run.apk_path)
            return None
        return {}
    
    # --- Locate and load prior Stage 1 run metadata ---
    try:
        prior_run_dir = _locate_latest_run(run.app_name, run.llm_model, run.video_type)
        logger.info("Located prior Stage 1 run: %s", prior_run_dir)
        
        prior_metadata = _load_run_metadata(prior_run_dir)
        memory_md_content = prior_metadata.get("video_mode_metadata", {}).get("memory_md_content")
        task_description = prior_metadata.get("video_mode_metadata", {}).get("task_description", "")
        
        if not memory_md_content:
            logger.error("No memory.md content found in prior run metadata")
            return None
        
        logger.info("Loaded memory.md from prior Stage 1 run")
    except FileNotFoundError as exc:
        logger.error("Failed to locate prior Stage 1 run: %s", exc)
        return None
    
    # --- Pre-flight: verify required files ---
    missing = []
    if not run.apk_path.exists():
        missing.append(f"APK not found: {run.apk_path}")
    if missing:
        for msg in missing:
            logger.warning("SKIP run — %s", msg)
        if file_handler is not None:
            logger.removeHandler(file_handler)
            file_handler.close()
        return None
    
    run_start = time.perf_counter()
    
    # --- Create provider (memory-aware) ---
    from src_llm.providers import create_provider
    provider = create_provider(run.llm, run.llm_model, env, logger=logger, video_mode=True)
    
    # --- Connect device + install APK ---
    from src_llm.device import DeviceController
    device = DeviceController()
    device.connect(serial=run.device_serial)
    
    logger.info("Installing APK: %s", run.apk_path)
    pkg = device.install_apk(run.apk_path)
    logger.info("APK installed: %s", pkg)
    
    from src_llm.apk_utils import extract_main_activity
    activity = extract_main_activity(run.apk_path)
    if activity:
        logger.info("Launching app: %s / %s", pkg, activity)
        device.launch_app(pkg, activity)
    else:
        logger.info("Launching app: %s (no main activity found, using monkey)", pkg)
        import subprocess
        subprocess.run(
            ["adb", "shell", "monkey", "-p", pkg, "-c", "android.intent.category.LAUNCHER", "1"],
            check=True,
        )
    
    time.sleep(2)
    logger.info("App launched: %s", device.get_current_activity())
    
    # --- Run automation with memory context ---
    from src_llm.automation import run_automation
    trace = run_automation(
        task_description=task_description,  # From memory, not from video
        provider=provider,
        device=device,
        max_steps=run.max_steps,
        output_dir=output_dir,
        history_window=run.history_window,
        step_delay=run.step_delay,
        stall_repeat_threshold=run.stall_repeat_threshold,
        logger=logger,
        memory_content=memory_md_content,  # Pass memory for reference during steps
    )
    
    logger.info(
        "Run complete: app=%s video_type=%s steps=%d status=%s",
        run.app_name, run.video_type, trace["total_steps"], trace["status"],
    )
    logger.info("Session trace: %s", output_dir / "session_trace.json")
    
    if run.reset_between_runs:
        logger.info("Resetting app state: force-stop + clear data | pkg=%s", pkg)
        device.reset_app(pkg)
        logger.info("App reset complete: %s", pkg)
    
    from src_llm.replay_writer import write_replay_script
    replay_path = write_replay_script(
        output_dir=output_dir,
        trace=trace,
        apk_path=run.apk_path,
        package=pkg,
        activity=activity,
        device_serial=run.device_serial,
    )
    logger.info("Replay script: %s", replay_path)
    
    _log_run_stats(logger, run, trace, output_dir, provider, time.perf_counter() - run_start)
    
    if file_handler is not None:
        logger.removeHandler(file_handler)
        file_handler.close()
    
    return trace
```

### 6. src_llm/automation.py

#### Update run_automation() signature
```python
def run_automation(
    task_description: str,
    provider: Any,
    device: DeviceController,
    max_steps: int,
    output_dir: Path | None = None,
    history_window: int = 3,
    step_delay: float = 1.5,
    stall_repeat_threshold: int = 4,
    logger: logging.Logger | None = None,
    memory_content: str | None = None,  # New: memory.md from Stage 1
) -> dict:
    """Run automation loop using pre-generated memory.
    
    At each step:
    1. Capture device screenshot
    2. Ask LLM: given memory context, what's the next action?
    3. Execute action
    4. Repeat
    
    memory_content: The full memory.md markdown from Stage 1 (for context)
    """
    # Pass memory to provider.decide_next_action() so LLM can reference it
    # Memory is injected into the system prompt or context window
    pass
```

#### Update provider.decide_next_action()
```python
def decide_next_action(
    self,
    history: list,
    screenshot: Any,
    accessibility_tree: str,
    task_description: str,
    memory_context: str | None = None,  # New: memory.md content
) -> ActionDecision:
    """Decide next action given current state + memory context.
    
    The memory_context (memory.md) is injected into the system prompt
    to guide the LLM's decision-making at each step.
    """
    # Build prompt with memory context included
    prompt = f"""
    You are an Android automation assistant.
    
    TASK CONTEXT (from Stage 1 analysis):
    {memory_context}
    
    CURRENT STATE:
    Screenshot: [provided]
    Accessibility tree: [provided]
    
    Based on the task context and current state, decide the next action.
    ...
    """
    pass
```

## Execution Flow

### Stage 1: src_llm.main (Video Analysis & Memory Generation)
```
config.yml (video_mode: true)
    ↓
Parse video path + create output layout
    ↓
Load environment & create provider
    ↓
Call provider.infer_memory_from_video(video_path)
    ↓
Provider analyzes entire video once → generates memory.md
    ↓
Parse memory.md → extract task_desc, ui_elements, completion_criteria
    ↓
Write outputs:
    - memory.md
    - metadata.json (includes memory_content + parsed fields)
    - llm_raw_response.txt
    ↓
Done
```

### Stage 2: src_llm.automate (Device Automation using Memory)
```
automation_config.yml (app_name, llm, llm_model, video_type)
    ↓
Locate latest Stage 1 run for app+model+video_type
    ↓
Load metadata.json from that run
    ↓
Extract memory.md content + task_description
    ↓
Install APK + launch app
    ↓
Loop (max_steps):
    1. Capture device screenshot
    2. Call provider.decide_next_action(screenshot, memory_context=memory.md)
    3. Execute action
    4. Continue until done or max_steps
    ↓
Write session_trace.json
    ↓
Done
```

## Configuration Examples

### main config (Stage 1)
```yaml
llm: "gemini"
llm_model: "gemini-2.5-pro"
video_mode: true  # NEW: default to true

frame_sampling:
  strategy: "uniform"
  fps: 1.0
  max_frames: 100

keyframe_selection:
  method: "heuristic"
  min_gap_seconds: 2.0

output:
  overwrite: false

logging:
  level: "INFO"

runs:
  - app_name: "AdAway"
    video_path: "srv-001.mp4"
```

### automate config (Stage 2)
```yaml
llm: "gemini"
llm_model: "gemini-2.5-pro"  # Will auto-locate Stage 1 run with this model

device_serial:
max_steps: 10
history_window: 3
step_delay: 1.5
stall_repeat_threshold: 4
reset_between_runs: true

runs:
  - app_name: "AdAway"
    video_path: "srv-001.mp4"  # Only needed to determine video_type
```

## Sequential Execution Flow

This section describes how to run Stage 1 and Stage 2 in sequence using a **unified configuration**.

### Unified Configuration

Both `src_llm.main` (Stage 1) and `src_llm.automate` (Stage 2) read from the **same config file**:

```yaml
# src_llm/input/config.yml (used by both main.py and automate.py)
llm: "gemini"
llm_model: "gemini-2.5-pro"
video_mode: true

frame_sampling:
  strategy: "uniform"
  fps: 1.0
  max_frames: 100

keyframe_selection:
  method: "heuristic"
  min_gap_seconds: 2.0

output:
  overwrite: false

logging:
  level: "INFO"

# Automation-specific settings (used only by automate.py, ignored by main.py)
device_serial:                    # auto-detect first device
max_steps: 10
history_window: 3
step_delay: 1.5
stall_repeat_threshold: 4
reset_between_runs: true

runs:
  - app_name: "AdAway"
    video_path: "srv-001.mp4"
  - app_name: "AntennaPod"
    video_path: "srv-001.mp4"
  - app_name: "BakersPercentageCalculator"
    video_path: "srv-001.mp4"
```

**Key principle:** 
- `main.py` reads: `llm`, `llm_model`, `video_mode`, `frame_sampling`, `keyframe_selection`, `output`, `logging`, `runs` (video_path)
- `automate.py` reads: `llm`, `llm_model`, `device_serial`, `max_steps`, `history_window`, `step_delay`, `stall_repeat_threshold`, `reset_between_runs`, `runs` (app_name, video_path)
- Single config file serves both stages ✓

### Single Command: Sequential video_to_memory → memory_to_device

New entry point: `src_llm/end_to_end.py` (orchestrates both stages)

```bash
# Run both Stage 1 and Stage 2 in sequence with ONE command
python -m src_llm.end_to_end --config src_llm/input/config.yml --env-file .env.local [--stage 1|2|all]
```

#### Usage Examples

```bash
# Run Stage 1 only (convert video to memory)
python -m src_llm.video_to_memory --config src_llm/input/config.yml --env-file .env.local

# Run Stage 2 only (replicate from memory on device)
python -m src_llm.memory_to_device --config src_llm/input/config.yml --env-file .env.local

# Run both Stage 1 → Stage 2 in sequence (default)
python -m src_llm.end_to_end --config src_llm/input/config.yml --env-file .env.local

# Or explicit:
python -m src_llm.end_to_end --config src_llm/input/config.yml --env-file .env.local --stage all

# Dry-run for Stage 1
python -m src_llm.video_to_memory --config src_llm/input/config.yml --env-file .env.local --dry-run

# Dry-run for Stage 2
python -m src_llm.memory_to_device --config src_llm/input/config.yml --env-file .env.local --dry-run

# Dry-run for both
python -m src_llm.end_to_end --config src_llm/input/config.yml --env-file .env.local --dry-run
```

### Single App Example: Complete Workflow

#### Step 1: Create unified config
```yaml
# src_llm/input/config.yml
llm: "gemini"
llm_model: "gemini-2.5-pro"
video_mode: true

frame_sampling:
  strategy: "uniform"
  fps: 1.0
  max_frames: 100

keyframe_selection:
  method: "heuristic"
  min_gap_seconds: 2.0

output:
  overwrite: false

logging:
  level: "INFO"

device_serial:
max_steps: 10
history_window: 3
step_delay: 1.5
stall_repeat_threshold: 4
reset_between_runs: true

runs:
  - app_name: "AdAway"
    video_path: "srv-001.mp4"
```

#### Step 2: Run Stage 1 → Stage 2 in sequence
```bash
python -m src_llm.pipeline --config src_llm/input/config.yml --env-file .env.local
```

**Execution flow:**

```
=== STAGE 1: src_llm.main ===
Loading config from src_llm/input/config.yml
Running app: AdAway
  - Resolving video path: apps/AdAway/videos/srv-001.mp4
  - Creating output layout: apps/AdAway/llm/gemini-2.5-pro/screenrec-video-mode/run-001/
  - Analyzing video with Gemini (video_mode=true)
  - Generating memory.md
  - Extracting task_description, ui_elements, completion_criteria
  - Writing metadata.json with video_mode_metadata
Duration: 45.2 seconds

✓ Stage 1 complete: apps/AdAway/llm/gemini-2.5-pro/screenrec-video-mode/run-001/

=== STAGE 2: src_llm.automate ===
Loading same config file
Running app: AdAway
  - Locating latest Stage 1 run: apps/AdAway/llm/gemini-2.5-pro/screenrec-video-mode/run-001/
  - Loading metadata.json and extracting memory_md_content
  - Connecting to device (auto-detect)
  - Installing APK: apps/AdAway/apk/adaway.apk
  - Launching app: com.example.adaway / .MainActivity
  
  - Automation step 1/10: Tap settings button (using memory context)
  - Automation step 2/10: Toggle notifications (using memory context)
  - Automation step 3/10: ... (continuing until done or max_steps)
  
  - Automation complete
  - Writing session_trace.json
Duration: 120.5 seconds

✓ Stage 2 complete: apps/AdAway/llm/gemini-2.5-pro/screenrec-video-mode/run-002/
```

**Output structure after sequential execution:**

```
apps/AdAway/llm/gemini-2.5-pro/screenrec-video-mode/
├── run-001/                      (Stage 1 output)
│   ├── memory.md                 # Generated by Gemini LLM
│   ├── metadata.json             # Contains video_mode_metadata + memory content
│   ├── llm_raw_response.txt
│   └── logs/
│       └── 2025-05-05T...run-001__pipeline__started.log
│
├── run-002/                      (Stage 2 output)
│   ├── session_trace.json        # Automation execution trace
│   ├── step_001.png              # Device screenshots per step
│   ├── step_002.png
│   ├── step_003.png
│   ├── replay_script.sh
│   └── logs/
│       └── automate.log
│
└── dry-run/                      (Only if --dry-run used)
    ├── metadata.json
    └── logs/
```

### Multiple Apps Example: Batch Workflow

#### Config with 3 apps
```yaml
# src_llm/input/config.yml
llm: "gemini"
llm_model: "gemini-2.5-pro"
video_mode: true

frame_sampling:
  strategy: "uniform"
  fps: 1.0
  max_frames: 100

keyframe_selection:
  method: "heuristic"
  min_gap_seconds: 2.0

output:
  overwrite: false

logging:
  level: "INFO"

device_serial:
max_steps: 10
history_window: 3
step_delay: 1.5
stall_repeat_threshold: 4
reset_between_runs: true

runs:
  - app_name: "AdAway"
    video_path: "srv-001.mp4"
  - app_name: "AntennaPod"
    video_path: "srv-001.mp4"
  - app_name: "BakersPercentageCalculator"
    video_path: "srv-001.mp4"
```

#### Run both stages for all apps
```bash
python -m src_llm.pipeline --config src_llm/input/config.yml --env-file .env.local
```

**Output:**

```
=== STAGE 1: Generating memory for all apps ===
[1/3] AdAway: generating memory... ✓
[2/3] AntennaPod: generating memory... ✓
[3/3] BakersPercentageCalculator: generating memory... ✓

apps/AdAway/llm/gemini-2.5-pro/screenrec-video-mode/run-001/
  ├── memory.md
  ├── metadata.json
  └── logs/

apps/AntennaPod/llm/gemini-2.5-pro/screenrec-video-mode/run-001/
  ├── memory.md
  ├── metadata.json
  └── logs/

apps/BakersPercentageCalculator/llm/gemini-2.5-pro/screenrec-video-mode/run-001/
  ├── memory.md
  ├── metadata.json
  └── logs/

=== STAGE 2: Automating all apps using memory ===
[1/3] AdAway: automating on device... ✓
[2/3] AntennaPod: automating on device... ✓
[3/3] BakersPercentageCalculator: automating on device... ✓

apps/AdAway/llm/gemini-2.5-pro/screenrec-video-mode/run-002/
  ├── session_trace.json
  ├── step_*.png
  └── logs/

apps/AntennaPod/llm/gemini-2.5-pro/screenrec-video-mode/run-002/
  ├── session_trace.json
  ├── step_*.png
  └── logs/

apps/BakersPercentageCalculator/llm/gemini-2.5-pro/screenrec-video-mode/run-002/
  ├── session_trace.json
  ├── step_*.png
  └── logs/
```

### Dry-Run Examples

#### Dry-run both stages
```bash
python -m src_llm.pipeline --config src_llm/input/config.yml --env-file .env.local --dry-run
```

**Output:**
- Validates config syntax ✓
- Validates environment variables ✓
- Validates video files exist ✓
- Validates APK files exist ✓
- Validates device connectivity (tries to connect, then disconnects) ✓
- Does NOT analyze videos (no Gemini calls)
- Does NOT run automation on device
- Exits cleanly with "Dry-run OK for Stage 1 and Stage 2"

#### Dry-run Stage 1 only
```bash
python -m src_llm.pipeline --config src_llm/input/config.yml --env-file .env.local --stage 1 --dry-run
```

#### Dry-run Stage 2 only
```bash
python -m src_llm.pipeline --config src_llm/input/config.yml --env-file .env.local --stage 2 --dry-run
```

### Key Properties of Sequential Execution

1. **Single config file**: Both stages read from same `config.yml`
2. **One command**: `src_llm.pipeline` orchestrates both stages
3. **Stage 1 → Stage 2**: Runs in sequence, memory from Stage 1 used in Stage 2
4. **Auto-location**: Stage 2 automatically finds latest Stage 1 run without explicit paths
5. **Repeatable**: Can run Stage 2 multiple times against same Stage 1 memory (run-003, run-004, etc.)
6. **Token efficiency**:
   - Stage 1: ~1 LLM call (full video analysis)
   - Stage 2: ~10 LLM calls (one per automation step, screenshot + memory only)
   - Total per batch: ~11 calls vs. ~100+ in naive approach (video re-analyzed per step per app)
7. **Run numbering**:
   - Stage 1 creates: `run-001/`
   - Stage 2 auto-locates `run-001/`, creates: `run-002/`
   - Re-run Stage 2: Creates `run-003/`, `run-004/`, etc.
   - Dry-run: Always `dry-run/` (overwritten each time)
8. **Selective execution**: Use `--stage 1|2|all` to run only what you need

## Implementation Order

1. **config.py**: Update directory structure logic, add metadata helpers
2. **io_utils.py**: Update OutputLayout, create_output_layout(), write_run_metadata()
3. **providers.py**: Add infer_memory_from_video() abstract + GeminiProvider implementation
4. **main.py**: Implement memory.md generation, parsing, and metadata writing
5. **automate.py**: Add run locating, metadata loading, memory-aware execution
6. **automation.py**: Update decide_next_action() to use memory context
7. **Test**: Verify Stage 1 generates memory.md, Stage 2 locates and uses it

## Key Design Decisions

1. **Single dry-run directory**: Overwritten each time, not numbered
2. **Flat structure**: Model contains provider info, no separate provider dir
3. **Memory in metadata.json**: For Stage 2 to easily access without separate file lookup
4. **Memory format**: Structured markdown parsed into task_desc, ui_elements, completion_criteria
5. **Video mode default**: True in YAML, users can opt into keyframe mode with `video_mode: false`
6. **No video re-analysis**: Stage 2 never touches the video, only uses memory
7. **Normalized model names**: All models use hyphens, lowercase (gemini-2.5-pro)
