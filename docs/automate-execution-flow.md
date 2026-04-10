# `gifdroid_llm.automate` Execution Flow

Command entrypoint:

```bash
python -m gifdroid_llm.automate \
  --config gifdroid_llm/input/automation_config.yml \
  --env-file .env.local
```

Optional flags:

- `--dry-run` — validate paths and imports then exit without running

All run parameters (apps, videos, LLM, steps, output) are defined in the config file.
See `gifdroid_llm/input/automation_config.example.yml` for all options with comments.

## High-Level Sequence

1. Parse CLI arguments in `gifdroid_llm/automate.py`.
2. Load automation config from YAML (`gifdroid_llm/input/automation_config.yml`).
3. Load/validate environment variables from `.env` (if `--env-file` is provided).
4. If `--dry-run` is set, validate paths/imports across all runs and exit.
5. For each run defined in `runs:`:
   1. Resolve output dir (auto-derived or explicit).
   2. Create LLM provider.
   3. Connect to Android device.
   4. Install and launch APK.
   5. Run video-guided automation loop.
   6. Save `session_trace.json` and `video_summary.txt`.
6. Print final JSON summary array and exit.

## Config Format

Top-level shared settings apply to all runs. Each entry in `runs:` specifies an app
and one or more video types. Paths are auto-derived from `app_name`:

- Video: `apps/<app>/videos/<video_type>/<prefix>-001.mp4`
- APK:   `apps/<app>/apk/<app>.apk`
- Output: `apps/<app>/llm/<provider>/<model>/<video_type>/run-<NNN>`

`video_path` shorthands per run entry:

| Shorthand            | Folder              | File prefix  |
|----------------------|---------------------|--------------|
| `screenrec` or `srv` | `videos/screenrec/` | `srv-001.mp4`|
| `handheld` or `hhv`  | `videos/handheld/`  | `hhv-001.mp4`|

Per-run optional overrides: `apk_path`, `max_steps`, `output_dir`.

## Detailed Call Flow

### 1) CLI Parse and Setup

- `gifdroid_llm/automate.py::_parse_args()` parses:
  - `--config`, `--env-file`, `--dry-run`
- `gifdroid_llm/automate.py::main()` sets logging.

### 2) Config + Env Load

- `gifdroid_llm.config.load_automation_config(config_path)`
  - Parses shared settings and expands `runs` list into `AutomationRunConfig` objects.
  - Returns `AutomationConfig`.
- `gifdroid_llm.env_loader.load_and_validate_env(env_file, llm)`
  - Loads `.env` and validates provider-specific requirements.

### 3) Dry-Run Path (Optional)

If `--dry-run`:

- For each run: checks `video_path.exists()` and `apk_path.exists()`.
- Imports:
  - `gifdroid_llm.providers.create_provider`
  - `gifdroid_llm.device.DeviceController`
  - `gifdroid_llm.automation.run_automation`
- Prints `Dry-run OK` and exits `0`.

### 4) Per-Run: Provider + Device Bootstrapping

For each run in `cfg.runs`:

- Output dir resolved: explicit `output_dir` or auto-derived
  `apps/<app>/llm/<provider>/<model>/<video_type>/run-<NNN>`
- Provider factory:
  - `gifdroid_llm.providers.create_provider(llm, llm_model, env, logger, video_mode=True)`
- Device setup:
  - `DeviceController.connect(serial)`
- APK install:
  - `DeviceController.install_apk(apk_path)`
  - internally calls `apk_utils.extract_package_name(apk_path)`
- App launch:
  - `apk_utils.extract_main_activity(apk_path)`
  - if activity found: `DeviceController.launch_app(package, activity)`
  - else fallback: `adb shell monkey -p <pkg> -c android.intent.category.LAUNCHER 1`

### 5) Video-Guided Automation (`run_automation`)

`gifdroid_llm.automation.run_automation(...)` does:

1. Summarize video intent — two paths tried in order:
   - **Direct-video path** (preferred): if `hasattr(provider, "summarize_video_task_from_video")`,
     call `provider.summarize_video_task_from_video(video_path)` to send the raw video
     directly to the model (e.g. Gemini inline video). Logs `"direct-video summary obtained"`.
   - **Keyframe fallback**: used when the provider lacks direct-video support *or* when the
     direct-video call raises an exception. Steps:
     1. `VideoFrameExtractor.extract(video_path, FrameSamplingConfig(...))`
     2. `KeyframeSelector.select(frames, KeyframeSelectionConfig(...))`
     3. `provider.summarize_video_task(keyframes)` — logs `"keyframe-based task summary"`.
2. Execute multi-step feedback loop (`for step in max_steps`)
   - Capture live state:
     - `device.capture_screenshot()`
     - `device.dump_accessibility_tree()`
     - `device.get_current_activity()`
   - Save screenshot to `output_dir/steps/step_XXX.png`
   - Ask LLM for next action:
     - `provider.decide_next_action_with_video_context(...)`
   - Append step entry to trace log
   - Update rolling conversation history:
     - `AutomationSession.add_turn(...)`
   - Stop if:
     - `continue_automation == False`, or
     - action is `None`, or
     - action type is `done`
   - Otherwise execute action:
     - `device.execute_action(action)`
   - Sleep `step_delay`
3. Build final trace object and write:
   - `output_dir/session_trace.json`
   - `output_dir/video_summary.txt`

### 6) Process Output

Back in `automate.main()`:

- Logs final status and trace path per run.
- Prints JSON array to stdout, one entry per completed run:
  - `app`
  - `video_type`
  - `status`
  - `total_steps`
  - `video_summary`

## Key Files Involved

- `gifdroid_llm/automate.py` (CLI orchestrator)
- `gifdroid_llm/input/automation_config.yml` (active config)
- `gifdroid_llm/input/automation_config.example.yml` (all options with comments)
- `gifdroid_llm/config.py` (automation config loading)
- `gifdroid_llm/env_loader.py` (env loading/validation)
- `gifdroid_llm/providers.py` (LLM provider, action decisions)
- `gifdroid_llm/device.py` (device actions via uiautomator2/adb)
- `gifdroid_llm/apk_utils.py` (APK package/activity extraction)
- `gifdroid_llm/automation.py` (video-guided loop)
- `gifdroid_llm/session.py` (history window state)
- `gifdroid_llm/video.py` (frame extraction)
- `gifdroid_llm/keyframes.py` (keyframe selection)
