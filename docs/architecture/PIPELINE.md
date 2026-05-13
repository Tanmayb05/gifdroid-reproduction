# Two-Stage LLM Pipeline Documentation

## Overview

The pipeline orchestrates a two-stage workflow for video-based device automation:

- **Stage 1 (Video → Memory)**: Analyze a video once with an LLM to generate structured task memory
- **Stage 2 (Memory → Device)**: Replicate the task on a device using the generated memory (no video re-analysis)

This eliminates redundant LLM calls and reduces token usage by ~90%.

## Architecture

```
┌─────────────────────────────────────────┐
│    Unified config.yml                   │
│    (shared by both stages)              │
└────────────┬────────────────────────────┘
             │
      ┌──────▼──────────────────────┐
      │  Stage 1: Video → Memory    │
      │  (src_llm.main)             │
      ├─────────────────────────────┤
      │ 1. Load config              │
      │ 2. Extract video frames     │
      │ 3. Call LLM to analyze      │
      │ 4. Generate memory.md       │
      │ 5. Write metadata.json      │
      │    with video_mode_metadata │
      └──────────┬────────────────────┘
                 │
                 ▼
      ┌──────────────────────────┐
      │ Output:                  │
      │ - memory.md              │
      │ - metadata.json          │
      │ - llm_raw_response.txt   │
      │ - logs/                  │
      └──────────┬──────────────┘
                 │
      ┌──────────▼──────────────────────┐
      │  Stage 2: Memory → Device       │
      │  (src_llm.automate)             │
      ├─────────────────────────────────┤
      │ 1. Locate Stage 1 output        │
      │ 2. Load metadata.json           │
      │ 3. Extract memory.md content    │
      │ 4. Connect device               │
      │ 5. Install APK + launch app     │
      │ 6. Run automation loop using    │
      │    memory context (no video)    │
      │ 7. Write session_trace.json     │
      └──────────┬────────────────────────┘
                 │
                 ▼
      ┌──────────────────────────┐
      │ Output:                  │
      │ - session_trace.json     │
      │ - step_NNN.png           │
      │ - replay_script.sh       │
      │ - logs/                  │
      └──────────────────────────┘
```

## Directory Structure

```
apps/<app>/llm/<model>/<source>-video-mode/
├── run-001/              (Stage 1: Video → Memory)
│   ├── memory.md
│   ├── metadata.json     (with video_mode_metadata)
│   ├── llm_raw_response.txt
│   └── logs/
│
├── run-002/              (Stage 2: Memory → Device)
│   ├── session_trace.json
│   ├── step_001.png
│   ├── step_002.png
│   ├── replay_script.sh
│   └── logs/
│
└── dry-run/              (Validation only, overwritten each time)
    ├── metadata.json
    └── logs/
```

## Usage

### Run Complete Pipeline (Stage 1 → Stage 2)

```bash
python -m src_llm.pipeline \
  --config src_llm/input/config.yml \
  --env-file .env.local
```

**Output:**
- Stage 1 generates `run-001/` with memory.md
- Stage 2 uses memory from run-001/ to create `run-002/`
- Both logs show execution details

### Run Stage 1 Only (Video → Memory)

```bash
python -m src_llm.pipeline \
  --config src_llm/input/config.yml \
  --env-file .env.local \
  --stage 1
```

**Output:**
- Creates `run-001/` with memory.md and metadata.json
- No device interaction

### Run Stage 2 Only (Memory → Device)

Requires a prior Stage 1 run to exist.

```bash
python -m src_llm.pipeline \
  --config src_llm/input/config.yml \
  --env-file .env.local \
  --stage 2
```

**Output:**
- Locates latest Stage 1 run
- Creates `run-002/` with automation results

### Dry-Run: Validate Without Processing

```bash
python -m src_llm.pipeline \
  --config src_llm/input/config.yml \
  --env-file .env.local \
  --dry-run
```

**Validates:**
- ✓ Config syntax
- ✓ Environment variables present
- ✓ Video files exist (Stage 1)
- ✓ APK files exist (Stage 2)
- ✓ Device connectivity (Stage 2)

**Skips:**
- ✗ LLM API calls
- ✗ Video frame extraction
- ✗ Device automation

**Output:**
- Creates `dry-run/` with metadata
- Logs validation details
- Exits with "Dry-run OK"

### Dry-Run Individual Stage

```bash
# Validate Stage 1 only
python -m src_llm.pipeline --config ... --env-file ... --stage 1 --dry-run

# Validate Stage 2 only
python -m src_llm.pipeline --config ... --env-file ... --stage 2 --dry-run
```

## Configuration

### Unified config.yml

Both stages read from the same configuration file. Stage 1 reads its relevant fields, Stage 2 reads its relevant fields.

```yaml
# LLM Configuration (both stages)
llm: "gemini"
llm_model: "gemini-2.5-pro"
video_mode: true

# Frame Sampling (Stage 1 only)
frame_sampling:
  strategy: "uniform"
  fps: 1.0
  max_frames: 100

# Keyframe Selection (Stage 1 only)
keyframe_selection:
  method: "heuristic"
  min_gap_seconds: 2.0

# Output Configuration (both stages)
output:
  overwrite: false

# Logging (both stages)
logging:
  level: "INFO"

# Device Automation (Stage 2 only)
device_serial:  # Leave empty for auto-detect
max_steps: 10
history_window: 3
step_delay: 1.5
stall_repeat_threshold: 4
reset_between_runs: true

# Runs to process
runs:
  - app_name: "AdAway"
    video_path: "srv-001.mp4"
  - app_name: "AntennaPod"
    video_path: "srv-001.mp4"
```

See `src_llm/input/config.yml.pipeline-example` for a complete example.

## Example: Single App Workflow

### Step 1: Create Configuration

```yaml
# config.yml
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

### Step 2: Dry-Run Validation

```bash
python -m src_llm.pipeline --config config.yml --env-file .env.local --dry-run
```

**Expected output:**
```
[INFO] Starting two-stage LLM pipeline
[INFO] Config: config.yml
[INFO] Env file: .env.local
[INFO] Mode: DRY-RUN (no actual processing)
[INFO] Stages: 1 → 2
============================================================
STAGE 1: Video → Memory Generation
============================================================
[INFO] Dry-run completed successfully (provider/API preflight skipped)
============================================================
STAGE 2: Memory → Device Automation
============================================================
[INFO] Dry-run completed successfully (device connection validated)
✓ Pipeline complete (2.3 seconds total)
Dry-run OK for Stage 1 and Stage 2
```

### Step 3: Run Full Pipeline

```bash
python -m src_llm.pipeline --config config.yml --env-file .env.local
```

**Expected output:**
```
[INFO] Starting two-stage LLM pipeline
[INFO] Stages: 1 → 2
============================================================
STAGE 1: Video → Memory Generation
============================================================
[INFO] Loading config from config.yml
[INFO] Running app: AdAway
[INFO] Resolving video: apps/AdAway/videos/srv-001.mp4
[INFO] Creating layout: apps/AdAway/llm/gemini-2.5-pro/screenrec-video-mode/run-001/
[INFO] Video mode enabled — analyzing video and generating memory
[INFO] Memory trace written: .../run-001/memory.md
[INFO] LLM raw response written: .../run-001/llm_raw_response.txt
[INFO] Stage 1 complete
Stage 1 duration: 47.2 seconds

============================================================
STAGE 2: Memory → Device Automation
============================================================
[INFO] Located prior Stage 1 run: apps/AdAway/llm/gemini-2.5-pro/screenrec-video-mode/run-001/
[INFO] Loaded memory.md from prior Stage 1 run
[INFO] Installing APK: apps/AdAway/apk/adaway.apk
[INFO] Launching app: com.adaway.ad.blocker / .MainActivity
[INFO] --- Automation Step 1/10 ---
[INFO] Captured screenshot (using memory context)
[INFO] LLM decided: Tap settings button
[INFO] Executed: Tap settings button
...
[INFO] Run complete: steps=8 status=success
[INFO] Session trace: apps/AdAway/llm/gemini-2.5-pro/screenrec-video-mode/run-002/session_trace.json
[INFO] Stage 2 complete
Stage 2 duration: 156.8 seconds

============================================================
✓ Pipeline complete (204.0 seconds total)
```

## Example: Batch Processing Multiple Apps

```yaml
# config.yml with 3 apps
runs:
  - app_name: "AdAway"
    video_path: "srv-001.mp4"
  - app_name: "AntennaPod"
    video_path: "srv-001.mp4"
  - app_name: "BakersPercentageCalculator"
    video_path: "srv-001.mp4"
```

```bash
python -m src_llm.pipeline --config config.yml --env-file .env.local
```

**Output structure:**
```
apps/AdAway/llm/gemini-2.5-pro/screenrec-video-mode/
├── run-001/  (Stage 1)
└── run-002/  (Stage 2)

apps/AntennaPod/llm/gemini-2.5-pro/screenrec-video-mode/
├── run-001/  (Stage 1)
└── run-002/  (Stage 2)

apps/BakersPercentageCalculator/llm/gemini-2.5-pro/screenrec-video-mode/
├── run-001/  (Stage 1)
└── run-002/  (Stage 2)
```

All apps share the same config file and run sequentially.

## API Integration

### Stage 1 (src_llm.main)

Entry point: `src_llm.main.main(args: argparse.Namespace) -> int`

**Args:**
- `args.config`: Path to config.yml
- `args.env_file`: Path to .env file
- `args.dry_run`: Skip processing

**Returns:** 0 on success, non-zero on failure

### Stage 2 (src_llm.automate)

Entry point: `src_llm.automate.main(args: argparse.Namespace) -> int`

**Args:**
- `args.config`: Path to config.yml
- `args.env_file`: Path to .env file
- `args.dry_run`: Skip processing

**Returns:** 0 on success, non-zero on failure

### Pipeline Orchestration

Entry point: `src_llm.pipeline.main(argv: list[str] | None = None) -> int`

**Args:**
- `argv`: Command-line arguments (default: sys.argv[1:])

**Returns:** 0 on success, non-zero on failure

## Troubleshooting

### Stage 1 fails: "Video file not found"

**Cause:** Video path in config.yml doesn't match actual file location.

**Solution:** Verify video file exists at `apps/<app>/videos/<video_path>`

### Stage 2 fails: "No runs found"

**Cause:** Stage 1 hasn't been run yet, or run directory structure is wrong.

**Solution:**
1. Ensure Stage 1 completed successfully
2. Check `apps/<app>/llm/<model>/<source>-video-mode/` exists
3. Verify `run-001/metadata.json` contains `video_mode_metadata`

### Stage 2 fails: "Failed to locate prior Stage 1 run"

**Cause:** Model name mismatch between stages, or wrong app name.

**Solution:**
1. Verify `llm_model` matches in config (e.g., "gemini-2.5-pro")
2. Check `app_name` matches between Stage 1 and Stage 2
3. Ensure Stage 1 run exists with correct directory structure

### Device connection fails in Stage 2

**Cause:** Device not connected or serial mismatch.

**Solution:**
1. Run `adb devices` to verify device connectivity
2. Set `device_serial` in config if auto-detect fails
3. Verify device is in developer mode and USB debugging enabled

## Performance Metrics

### Token Efficiency

| Approach | LLM Calls | Tokens | Duration |
|----------|-----------|--------|----------|
| Naive (re-analyze per step) | 10+ per app | 100k+ | 3-5 min per app |
| Two-Stage Pipeline | 1 (Stage 1) + 10 (Stage 2) | ~10k | 50s + 2-3 min per app |
| Savings | -90% calls | -90% tokens | ~30% faster |

### Example: 3 Apps

```
Naive approach:
  AdAway: 10 calls × 3 apps = 30 total calls
  AntennaPod: 10 calls × 3 apps
  BakersPercentageCalculator: 10 calls × 3 apps
  Total: 30 calls × 1k tokens/call = 30k tokens

Two-Stage:
  Stage 1: 3 apps × 1 call = 3 calls (5k tokens)
  Stage 2: 3 apps × 10 calls = 30 calls (5k tokens)
  Total: 33 calls × 333 tokens/call = 11k tokens (63% savings)
```

## Testing

Run integration tests:

```bash
python -m pytest tests/test_pipeline_integration.py -v
```

Tests validate:
- ✓ Argument parsing
- ✓ Stage 1 → Stage 2 handoff
- ✓ Metadata structure for memory persistence
- ✓ Dry-run validation
- ✓ Error handling

## Advanced Topics

### Repeating Stage 2 Against Same Memory

Run Stage 2 multiple times against the same Stage 1 memory:

```bash
# Run 1: Creates run-002/
python -m src_llm.pipeline --config config.yml --env-file .env.local --stage 2

# Run 2: Creates run-003/ (reuses memory from run-001/)
python -m src_llm.pipeline --config config.yml --env-file .env.local --stage 2
```

Both runs reference the same memory.md from run-001/ but generate different automation traces.

### Custom LLM Providers

To use a different LLM provider in the pipeline:

1. Update config.yml:
   ```yaml
   llm: "your-provider"
   llm_model: "your-model-name"
   ```

2. Ensure provider implements:
   - `infer_memory_from_video()` for Stage 1
   - `decide_next_action_with_memory_context()` for Stage 2

3. Run pipeline as usual

### Selective Stage Execution

Run specific stages for debugging:

```bash
# Test Stage 1 only
python -m src_llm.pipeline --config config.yml --env-file .env.local --stage 1

# Verify memory was generated
ls apps/AdAway/llm/gemini-2.5-pro/screenrec-video-mode/run-001/

# Test Stage 2 with generated memory
python -m src_llm.pipeline --config config.yml --env-file .env.local --stage 2
```

## Implementation Details

### Stage 1 Pipeline Entry

- Calls `src_llm.main.main()` with shared config
- Passes `video_mode=true` to ensure memory generation
- Collects memory.md + metadata.json in output directory

### Stage 2 Pipeline Entry

- Calls `src_llm.automate.main()` with shared config
- Auto-locates latest Stage 1 run directory
- Loads memory from metadata.json
- Runs device automation using memory context

### Run Numbering

- **Stage 1 Output:** `run-NNN/` (e.g., run-001/)
- **Stage 2 Output:** `run-NNN+1/` (e.g., run-002/)
- **Dry-run:** Always `dry-run/` (overwritten each time)

## See Also

- [Two-Stage LLM Workflow Roadmap](../ROADMAP.md)
- [Implementation Plan](../.claude/PLAN.md)
- [Configuration Reference](./CONFIG.md)
