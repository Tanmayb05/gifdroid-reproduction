# src_llm

`src_llm` implements a **two-stage LLM workflow** for Android app automation:

- **Stage 1**: Analyze video once → generate `memory.md` + metadata (reduces redundant processing)
- **Stage 2**: Reuse `memory.md` for device automation (no video re-analysis)

This architecture reduces LLM token usage by ~90% compared to traditional re-analysis workflows.

## Supported LLM Providers

### Local (Ollama — Apple Silicon recommended)

All local providers run via [Ollama](https://ollama.com) on your machine. No API key required.
They share `LLAMA_BASE_URL` in `.env.local` (except Qwen which uses `QWEN_BASE_URL`).

| `llm:` value | Default model | Size | Notes |
| --- | --- | --- | --- |
| `llama` | `llama3.2-vision:latest` | 7.8 GB | Baseline vision model |
| `llama` | `llama3.2-vision:11b` | 7.8 GB | Set `llm_model` explicitly; stronger reasoning |
| `llava` | `llava:7b` | 4.7 GB | Fast, good instruction following |
| `minicpm` | `minicpm-v:latest` | 5.5 GB | Excellent for dense UI screenshots, low hallucination |
| `gemma` | `gemma3:4b` | 3.3 GB | Google's latest multimodal, small footprint |
| `qwen` | `qwen2.5vl:7b` | 6.0 GB | Strong multimodal, recommended for M3 Pro |

Pull any model before use:

```bash
ollama pull qwen2.5vl:7b
ollama pull llava:7b
ollama pull minicpm-v
ollama pull gemma3:4b
ollama pull llama3.2-vision:11b
```

Verify a model endpoint is accessible:

```bash
python -m src_llm.llama_prereq \
  --base-url http://localhost:11434/v1 \
  --model qwen2.5vl:7b \
  --check-metal
```

### Cloud (API key required)

| `llm:` value | Model | Auth |
| --- | --- | --- |
| `gemini` | `gemini-1.5-flash` (default) | `GOOGLE_GENERATIVE_AI_API_KEY` or ADC/Vertex |
| `sonnet` / `claude` | — | `ANTHROPIC_API_KEY` (stub, not yet integrated) |

## Output Structure

**Flat directory structure** combining video name + model + mode:

```text
apps/{app}/
  llm/
    {video-name}-{model}{-vm}/  <- video name + model + optional -vm for video_mode
                                   e.g., "hhv-001-gemini-2.5-pro-vm", "srv-002-vibr"
      run-001/
        memory.md             <- Stage 1 output: task summary, steps, UI elements
        metadata.json         <- run config, timing, memory_content (for Stage 2)
        execution_trace.json  <- action sequence (legacy or Stage 2 output)
        frames_manifest.json  <- sampled + selected keyframe metadata
        llm_raw_response.txt  <- raw model output for debugging
        keyframes/
          kf-0001.png
          kf-0002.png
          ...
        logs/
          run.log
  utgs/                       <- UTG input data only, not touched by src_llm
  videos/
  apk/
```

**Directory naming convention:**

- `{video-name}`: Extracted from video filename without extension (e.g., `hhv-001`, `srv-002`)
- `{model}`: Normalized model name in lowercase with hyphens (e.g., `gemini-2.5-pro`, `vibr`)
- `-vm` suffix: Added only when `video_mode=true` to distinguish video-mode runs from standard runs

**Examples:**

- `hhv-001-gemini-2.5-pro-vm/` — handheld video HHV-001, Gemini 2.5 Pro, video mode enabled
- `srv-002-vibr/` — screenrec video SRV-002, ViBR model, standard mode

**video_mode flag** (defaults to `true`):

- `true`: Stage 1 generates `memory.md` from video, Stage 2 uses memory for automation, directory has `-vm` suffix
- `false`: Skip video analysis, use keyframes only (legacy mode), directory has no `-vm` suffix

### memory.md schema (Stage 1 output)

Markdown document containing structured task analysis from video:

```markdown
# Task Memory: [App Name]

## Task Summary
One-paragraph description of the overall task or workflow demonstrated in the video.

## Steps
1. Step 1: [action] — [description]
2. Step 2: [action] — [description]
...

## UI Elements
- Button: "Enable" (top-right)
- Text: "Status: Disabled" (center)
- Checkbox: "Auto-refresh" (bottom-left)
...

## Completion Criteria
- App reaches final state: [description]
- User action: [description]
```

This memory is automatically extracted and embedded in `metadata.json` for Stage 2 automation.

### execution_trace.json schema

```json
{
  "video": "apps/adaway/videos/handheld/hhv-001.mp4",
  "llm": "qwen2.5vl-7b",
  "video_type": "hhv",
  "app_name": "adaway",
  "generated_at": "2026-04-02T00:00:00+00:00",
  "video_mode": true,
  "replay_trace": [
    {
      "step_index": 1,
      "timestamp_sec": 1.333,
      "frame_file": "kf-0001.png",
      "screen_description": "AdAway home screen showing Enable button",
      "action": {
        "action_type": "launch",
        "target": "app_entrypoint",
        "details": "App launched showing initial disabled state."
      },
      "confidence": 0.95
    }
  ]
}
```

Valid `action_type` values: `launch`, `tap`, `type`, `swipe`, `scroll`, `wait`, `long_press`, `back`, `open_menu`, `select`.

## Two-Stage Workflow

### Stage 1: Video → Memory (Offline Analysis)

Analyzes a recorded video and generates task memory (`memory.md`) describing the app's behavior, UI elements, and task steps. Runs once per video, model, and video type.

```bash
python -m src_llm.video_to_memory \
  --config src_llm/input/config.yml \
  --env-file .env.local
```

**Output:**

- `memory.md` — structured task description
- `metadata.json` — embeds memory_content for Stage 2
- `execution_trace.json` — action sequence (optional)
- `keyframes/` — extracted frames for debugging

### Stage 2: Memory → Device Automation (Online Execution)

Reuses the memory from Stage 1 to drive device automation without re-analyzing the video. Reduces LLM calls by ~90%.

```bash
python -m src_llm.memory_to_device \
  --config src_llm/input/config.yml \
  --env-file .env.local
```

**Input:**

- Locates latest Stage 1 run for app+model+video_type
- Loads `memory.md` from metadata.json
- Uses memory context in each automation step

**Output:**

- Device automation trace with memory-guided decisions

### End-to-End Orchestrator (Both Stages)

Run both stages in sequence with a single command:

```bash
python -m src_llm.end_to_end \
  --config src_llm/input/config.yml \
  --env-file .env.local
```

**Options:**

- `--stage 1` — Run only Stage 1 (video → memory)
- `--stage 2` — Run only Stage 2 (memory → device)
- `--stage all` — Run both stages (default)
- `--dry-run` — Validate config without executing

**Example:**

```bash
# Both stages
python -m src_llm.end_to_end --config src_llm/input/config.yml --env-file .env.local

# Stage 1 only
python -m src_llm.end_to_end --stage 1 --config src_llm/input/config.yml --env-file .env.local

# Stage 2 only
python -m src_llm.end_to_end --stage 2 --config src_llm/input/config.yml --env-file .env.local

# Dry-run both
python -m src_llm.end_to_end --dry-run --config src_llm/input/config.yml --env-file .env.local
```

## Install

```bash
pip install -r src_llm/requirements.txt
```

## Configure

### 1. Environment file

Copy `.env.local.example` to `.env.local` and fill in the relevant section.

**Local Ollama providers** (`llama`, `llava`, `minicpm`, `gemma`):

```bash
LLAMA_BASE_URL=http://localhost:11434/v1
```

**Qwen via Ollama:**

```bash
QWEN_BASE_URL=http://localhost:11434/v1
```

**Gemini:**

```bash
GOOGLE_GENERATIVE_AI_API_KEY=your_key_here
```

### 2. Config file

Edit `src_llm/input/config.yml` (see `config.example.yml` for full documentation):

```yaml
llm: "gemini"                                 # provider: gemini, qwen, llama, etc.
llm_model: "gemini-1.5-flash"                # optional — uses provider default if omitted
video_mode: true                             # Stage 1: generate memory.md (default: true)
llm_prompt_file: "src_llm/input/prompts/llama_action_prompt_gemini_2.txt"

frame_sampling:
  strategy: "uniform"
  fps: 1.5
  max_frames: 100

keyframe_selection:
  method: "ssim"                             # recommended
  min_gap_seconds: 1.0
  ssim_threshold: 0.95
  stable_threshold: 2

output:
  overwrite: true

runs:
  - app_name: "adaway"
    video_path:
      - "hhv"
      - "srv"
```

`video_path` accepts:

- `"hhv"` — shorthand for `apps/{app}/videos/handheld/hhv-001.mp4`
- `"srv"` — shorthand for `apps/{app}/videos/screenrec/srv-001.mp4`
- An explicit path or a list of paths/shorthands

`video_mode` options:

- `true` — Stage 1: analyze video and generate `memory.md` (recommended, default)
- `false` — Legacy mode: generate execution_trace directly from keyframes

`keyframe_selection.method` options:

- `heuristic` — motion-threshold based
- `llm_assisted` — currently same behavior as `heuristic`
- `ssim` — GIFdroid-style stable-screen SSIM detection (recommended)

## Run

### Stage 1: Video Analysis (Memory Generation)

```bash
python -m src_llm.video_to_memory \
  --config src_llm/input/config.yml \
  --env-file .env.local
```

Generates `memory.md` and `metadata.json` for all runs in config.

### Stage 2: Device Automation (Memory-Driven)

```bash
python -m src_llm.memory_to_device \
  --config src_llm/input/config.yml \
  --env-file .env.local
```

Uses memory from Stage 1 run to guide device automation.

### Both Stages (Recommended)

```bash
python -m src_llm.end_to_end \
  --config src_llm/input/config.yml \
  --env-file .env.local
```

Runs Stage 1 followed by Stage 2 in sequence.

Dry-run (validates config/env, skips inference):

```bash
python -m src_llm.end_to_end --dry-run --config src_llm/input/config.yml --env-file .env.local
```

Or for individual stages:

```bash
python -m src_llm.video_to_memory --dry-run --config src_llm/input/config.yml --env-file .env.local
python -m src_llm.memory_to_device --dry-run --config src_llm/input/config.yml --env-file .env.local
```

## Prompt Templates

All local Ollama providers use a shared prompt template file specified by `llm_prompt_file` in config. The template must contain a `{KEYFRAMES}` placeholder where per-keyframe metadata is injected at runtime.

Available templates in `src_llm/input/prompts/`:

| File | Description |
| --- | --- |
| `llama_action_prompt_gemini_2.txt` | **Recommended.** Schema-first prompt with example output. Instructs the model to act as a JSON API. Works well across all local providers. |
| `llama_action_prompt_baseline.txt` | Compact prompt with explicit rules and inline example. Good fallback if the model struggles with the schema-first format. |
| `llama_action_prompt_gemini_1.txt` | Verbose schema-first prompt with role definition. More context but longer token count. |
| `llama_action_prompt_claude.txt` | Anthropic-style variant. |

To use a different template:

```yaml
llm_prompt_file: "src_llm/input/prompts/llama_action_prompt_baseline.txt"
```

## Fallback Behavior

If a provider fails (HTTP error, timeout, or unparseable JSON output), the pipeline falls back to a **deterministic heuristic** based on `motion_score` rather than failing the run:

| Condition | Assigned action |
| --- | --- |
| First keyframe | `launch` |
| `motion_score >= 18` | `tap` |
| `motion_score >= 9` | `scroll` |
| `motion_score < 9` | `wait` |

The fallback result is still written to `execution_trace.json`. Check `llm_raw_response.txt` and `logs/run.log` to diagnose why the model output was rejected.

## Provider Notes

### Memory Generation (Stage 1)

Providers that support `video_mode: true` for memory.md generation:

- **Gemini** — Recommended for dense UI and task understanding
- **Qwen** — Strong multimodal, M3 Pro optimized
- **Llama, LLaVA, MiniCPM, Gemma** — Local alternatives, lower latency

### Local Ollama providers (`llama`, `llava`, `minicpm`, `gemma`, `qwen`)

- Run a prerequisite accessibility check before inference.
- Send keyframe images as base64-encoded JPEG in the request (multimodal).
- Fall back to a deterministic heuristic if memory generation fails (returns unparseable output).
- Image resolution per provider: `llama` → 768px, `qwen`/`gemma` → 512px, `minicpm` → 448px (matches native tile size).
- Set `LLAMA_TIMEOUT_SEC` (or `QWEN_TIMEOUT_SEC`) in `.env.local` to tune inference timeout.
- Check Metal (Apple Silicon GPU) acceleration: `python -m src_llm.llama_prereq --check-metal`

### Gemini

- Performs API preflight at startup.
- Supports API key (`GOOGLE_GENERATIVE_AI_API_KEY`) or Application Default Credentials (ADC/Vertex).
- Set `GEMINI_VERTEX_PROJECT_ID` and `GEMINI_VERTEX_LOCATION` in `.env.local` when using Vertex AI.
- Recommended for Stage 1 memory generation (excellent task summarization).

## Known Issues

See `docs/issues/` for documented issues and fixes:

| Issue | File |
| --- | --- |
| Qwen2.5-VL crashes (HTTP 500) with multiple images on Apple Silicon | `docs/issues/2026-04-02-qwen-model-runner-crash-oom.md` |
| Llama repetition loop in raw response | `docs/issues/2026-04-01-llama-repetition-loop-raw-response.md` |
| Llama ignores JSON instruction and hallucinates | `docs/issues/2026-04-01-llama-ignores-json-instruction-hallucinates.md` |
| Llama wrong prompt schema (Gemini template mismatch) | `docs/issues/2026-04-01-llama-wrong-prompt-schema-gemini-template.md` |

## Reset Runs

Wipes `apps/{app}/llm/` run directories (Stage 1 and Stage 2) for selected apps.

Preview first:

```bash
python -m src_llm.reset_runs \
  --config src_llm/input/reset_runs.example.yml \
  --dry-run
```

Apply:

```bash
python -m src_llm.reset_runs \
  --config src_llm/input/reset_runs.example.yml \
  --apply
```

## FAQ: How does video_mode work?

**Q: What happens when `video_mode: true`?**

A: Video mode skips keyframe extraction and sends the entire video directly to the LLM provider (Gemini) for analysis. The LLM returns a structured markdown summary (memory.md) instead of an execution trace.

**Q: What's the execution flow in video mode?**

A:

1. **Entry point** ([main.py:261–275](src_llm/main.py#L261-L275)):
   - Check `cfg.video_mode` flag
   - Call `provider.infer_memory_from_video(video_path)` → returns markdown directly
   - Parse markdown for task description, UI elements, and completion criteria
   - Skip frame extraction + keyframe selection (entire normal pipeline bypassed)

2. **Provider layer** ([providers.py:1182–1199](src_llm/providers.py#L1182-L1199)):
   - Base class defines `infer_memory_from_video()` interface (line 129)
   - Only Gemini implements it; other providers raise `NotImplementedError`
   - Reads memory prompt from `src_llm/input/prompts/llama_action_prompt_memory.txt`
   - Calls `_send_video_request(video_path, prompt)` → sends to Gemini API
   - Extracts + returns raw markdown text

3. **Video encoding** ([providers.py](src_llm/providers.py)):
   - `_send_video_request()` encodes video as base64
   - Sends inline to Gemini generateContent API
   - Parses JSON response, extracts text content

**Q: When should I use video_mode?**

A: Use `video_mode: true` (default) for Stage 1 memory generation. It reduces API calls and token usage by generating the task summary once. Disable it (`video_mode: false`) only if you need keyframe-level precision or don't have API access.

**Q: Why is video_mode Gemini-only?**

A: Gemini's API natively supports inline video uploads in requests. Local Ollama providers don't support video input directly; they require pre-extracted keyframes. To use video_mode with local models, keyframes must be extracted first (use `video_mode: false`).

**Q: What's the difference: video_mode vs. legacy keyframe mode?**

A:

| Aspect | video_mode=true | video_mode=false |
| --- | --- | --- |
| Input | Full video file | Extracted keyframes |
| Output | memory.md + metadata | execution_trace.json |
| Keyframe extraction | Skipped | Required (1–2 min) |
| LLM calls | 1× (video → memory) | N× (1 per keyframe) |
| Use case | Stage 1 analysis | Detailed action traces |
| Provider support | Gemini only | All providers |

## Architecture & Design Decisions

| Decision | Rationale |
| --- | --- |
| Flat model directory (no provider subdir) | Simplifies run location, supports model portability |
| Model names include provider | Avoids naming conflicts (e.g., both Ollama and API use "gemini") |
| Embed memory in metadata.json | Stage 2 can load memory without filesystem traversal |
| video_mode flag | Allows legacy keyframe-only workflows alongside new memory pipeline |
| Separate Stage 1 & Stage 2 commands | Supports offline analysis + async device execution |

## Token Savings

Typical workflow comparison:

| Task | Traditional | Two-Stage | Savings |
| --- | --- | --- | --- |
| Analyze video + extract actions | 1× video analysis | 1× video → memory | 0% |
| Device automation (5 steps) | 5× full video re-analysis | 5× memory context | **90%** |
| Total (1 video + 5 device steps) | 6 full analyses | 1 analysis + 5 memory uses | **~83%** |
