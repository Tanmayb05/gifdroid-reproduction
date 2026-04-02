# gifdroid_llm

`gifdroid_llm` generates an LLM-based execution trace (keyframes + action sequence) directly from a video recording of an Android app.

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
python -m gifdroid_llm.llama_prereq \
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

```text
apps/{app}/
  llm/
    {provider}/
      {model}/
        handheld/
          run-001/
            execution_trace.json   <- main output: action sequence
            frames_manifest.json   <- all sampled + selected keyframe metadata
            metadata.json          <- run config, timing, status
            llm_raw_response.txt   <- raw model output for debugging
            keyframes/             <- kf-0001.png, kf-0002.png, ...
            logs/
              run.log
        screenrec/
          run-001/
            ...
  utgs/          <- UTG input data only, not touched by gifdroid_llm
  videos/
  apk/
```

### execution_trace.json schema

```json
{
  "video": "apps/adaway/videos/handheld/hhv-001.mp4",
  "llm": "qwen",
  "video_type": "hhv",
  "app_name": "adaway",
  "generated_at": "2026-04-02T00:00:00+00:00",
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

## Install

```bash
pip install -r gifdroid_llm/requirements.txt
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

Edit `gifdroid_llm/input/config.yml` (see `config.example.yml` for full documentation):

```yaml
llm: "qwen"                  # provider key
llm_model: "qwen2.5vl:7b"   # optional — uses provider default if omitted
llama_action_prompt_file: "gifdroid_llm/input/prompts/llama_action_prompt_gemini_2.txt"

frame_sampling:
  strategy: "uniform"
  fps: 1.5
  max_frames: 100

keyframe_selection:
  method: "ssim"             # recommended
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

`keyframe_selection.method` options:

- `heuristic` — motion-threshold based
- `llm_assisted` — currently same behavior as `heuristic`
- `ssim` — GIFdroid-style stable-screen SSIM detection (recommended)

## Run

```bash
python -m gifdroid_llm.main \
  --config gifdroid_llm/input/config.yml \
  --env-file .env.local
```

Dry-run (validates config/env, skips inference):

```bash
python -m gifdroid_llm.main --dry-run
```

## Prompt Templates

All local Ollama providers use a shared prompt template file specified by `llama_action_prompt_file` in config. The template must contain a `{KEYFRAMES}` placeholder where per-keyframe metadata is injected at runtime.

Available templates in `gifdroid_llm/input/prompts/`:

| File | Description |
| --- | --- |
| `llama_action_prompt_gemini_2.txt` | **Recommended.** Schema-first prompt with example output. Instructs the model to act as a JSON API. Works well across all local providers. |
| `llama_action_prompt_baseline.txt` | Compact prompt with explicit rules and inline example. Good fallback if the model struggles with the schema-first format. |
| `llama_action_prompt_gemini_1.txt` | Verbose schema-first prompt with role definition. More context but longer token count. |
| `llama_action_prompt_claude.txt` | Anthropic-style variant. |

To use a different template:

```yaml
llama_action_prompt_file: "gifdroid_llm/input/prompts/llama_action_prompt_baseline.txt"
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

### Local Ollama providers (`llama`, `llava`, `minicpm`, `gemma`, `qwen`)

- Run a prerequisite accessibility check before inference.
- Send keyframe images as base64-encoded JPEG in the request (multimodal).
- Fall back to a deterministic heuristic if the model returns unparseable output.
- Image resolution per provider: `llama` → 768px, `qwen`/`gemma` → 512px, `minicpm` → 448px (matches its native tile size).
- Set `LLAMA_TIMEOUT_SEC` (or `QWEN_TIMEOUT_SEC`) in `.env.local` to tune the inference timeout.
- Check Metal (Apple Silicon GPU) acceleration: `python -m gifdroid_llm.llama_prereq --check-metal`

### Gemini

- Performs API preflight at startup.
- Supports API key (`GOOGLE_GENERATIVE_AI_API_KEY`) or Application Default Credentials (ADC/Vertex).
- Set `GEMINI_VERTEX_PROJECT_ID` and `GEMINI_VERTEX_LOCATION` in `.env.local` when using Vertex AI.

## Known Issues

See `docs/issues/` for documented issues and fixes:

| Issue | File |
| --- | --- |
| Qwen2.5-VL crashes (HTTP 500) with multiple images on Apple Silicon | `docs/issues/2026-04-02-qwen-model-runner-crash-oom.md` |
| Llama repetition loop in raw response | `docs/issues/2026-04-01-llama-repetition-loop-raw-response.md` |
| Llama ignores JSON instruction and hallucinates | `docs/issues/2026-04-01-llama-ignores-json-instruction-hallucinates.md` |
| Llama wrong prompt schema (Gemini template mismatch) | `docs/issues/2026-04-01-llama-wrong-prompt-schema-gemini-template.md` |

## Reset Runs

Wipes `apps/{app}/llm/` run directories for selected apps.

Preview first:

```bash
python -m gifdroid_llm.reset_runs \
  --config gifdroid_llm/input/reset_runs.example.yml \
  --dry-run
```

Apply:

```bash
python -m gifdroid_llm.reset_runs \
  --config gifdroid_llm/input/reset_runs.example.yml \
  --apply
```
