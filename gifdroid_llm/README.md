# gifdroid_llm

`gifdroid_llm` generates an LLM-based execution trace (keyframes + action sequence) directly from a video recording of an Android app.

## Output Structure

Runs are stored under the app, independent of any UTG:

```text
apps/{app}/
  llm/
    {provider}/
      {model}/
        handheld/
          run-001/
            execution_trace.json
            frames_manifest.json
            metadata.json
            keyframes/
            logs/
        screenrec/
          run-001/
            ...
  utgs/          ← UTG input data only, not touched by gifdroid_llm
  videos/
  apk/
```

## Install

```bash
pip install -r gifdroid_llm/requirements.txt
```

## Configure

1. Copy `.env.local.example` to `.env.local` and fill credentials.
   - Gemini: set `GOOGLE_GENERATIVE_AI_API_KEY` or use Application Default Credentials.
   - Llama (Ollama): set `LLAMA_BASE_URL` (e.g. `http://localhost:11434/v1`).
2. Edit `gifdroid_llm/input/config.yml`: set `llm`, `llm_model`, and the `runs` list.
   - `video_path` accepts `"hhv"`, `"srv"`, an explicit path, or a list of paths.
   - `keyframe_selection.method` supports:
     - `heuristic` (motion-threshold based)
     - `llm_assisted` (currently same behavior as `heuristic`)
     - `ssim` (GIFdroid-style stable-screen SSIM detection; configurable with `ssim_threshold` and `stable_threshold`)

## Run

```bash
python -m gifdroid_llm.main \
  --config gifdroid_llm/input/config.yml \
  --env-file .env.local
```

Optional dry-run (validates config/env, skips inference):

```bash
python -m gifdroid_llm.main --dry-run
```

Llama prerequisite check (standalone):

```bash
python -m gifdroid_llm.llama_prereq --env-file .env.local --model llama3.2-vision:latest
```

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

## Notes

- Gemini: performs API preflight at startup; supports API key or ADC/Vertex auth.
- Llama: runs a prerequisite accessibility check before inference; sends keyframe images for vision-capable models (e.g. `llama3.2-vision`). Set `LLAMA_TIMEOUT_SEC` in `.env.local` to tune the inference timeout (default 180s).
- Sonnet/Qwen: adapter stubs (not yet integrated).
- Video type is auto-detected from path (`handheld`/`hhv` → `hhv`, `screenrec`/`srv` → `srv`).
