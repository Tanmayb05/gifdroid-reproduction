# gifdroid_llm

`gifdroid_llm` generates an LLM-based bug reproducibility execution trace directly from a video path and model selection, including explicit model IDs like `gemini-1.5-flash`.

## What It Produces
- Execution trace JSON:
  - `app_<app_name>/utg<utg_number>/output/llm_<llm_name>/execution_trace_llm_hhv_app_<app_name>_<model>_<datetime>.json`
  - `app_<app_name>/utg<utg_number>/output/llm_<llm_name>/execution_trace_llm_srv_app_<app_name>_<model>_<datetime>.json`
- Keyframes directory:
  - `app_<app_name>/utg<utg_number>/output/llm_<llm_name>/execution_trace_llm_hhv_keyframes/`
  - `app_<app_name>/utg<utg_number>/output/llm_<llm_name>/execution_trace_llm_srv_keyframes/`
- Log file:
  - `app_<app_name>/utg<utg_number>/gifdroid_llm_<datetime>_hhv.log`
  - `app_<app_name>/utg<utg_number>/gifdroid_llm_<datetime>_srv.log`
- Intermediate manifest JSON:
  - `app_<app_name>/utg<utg_number>/output/llm_<llm_name>/frames_manifest_<video_type>.json`

## Install
```bash
pip install -r gifdroid_llm/requirements.txt
```

## Configure
1. Copy `.env.local.example` to `.env.local` and fill credentials (for Gemini, use one of: `GOOGLE_GENERATIVE_AI_API_KEY` or Application Default Credentials via `google.auth.default()`. For ADC/Vertex routing, set `GEMINI_VERTEX_PROJECT_ID` (preferred) and optionally `GEMINI_VERTEX_LOCATION`).
2. Edit `gifdroid_llm/input/config.yml` and set both `llm` and `llm_model`.
   - For local Ollama/OpenAI-compatible Llama endpoints, set `LLAMA_BASE_URL` (for example `http://localhost:11434/v1`) and set the model in config via `llm_model` (for example `llama3.2-vision:latest`).
   - `utg_number` supports a single value or a list.
   - `video_path` supports a single value (`"hhv"`, `"srv"`, or explicit path) or a list.
   - When both are lists in a run entry, they are paired by index (same length required). If one side is a single value, it is reused for all values on the other side.

## Run
```bash
python -m gifdroid_llm.main \
  --config gifdroid_llm/input/config.yml \
  --env-file .env.local
```

Optional dry-run:
```bash
python -m gifdroid_llm.main --dry-run
```

Llama prerequisite check (standalone):
```bash
python -m gifdroid_llm.llama_prereq --env-file .env.local --model llama3.2-vision:latest
```

## Reset Existing Runs
Use this to wipe run directories for selected app/UTG targets and reset each target's `manifest.json` (`runs` and `latest` are cleared; `videos` remain unchanged).

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
- Provider adapters are implemented with a common interface.
- Gemini now performs a real API preflight check at startup and logs request/wait/response timings (supports API key or ADC/default creds), and logs the selected auth route (`api_key` or `adc_default`) and both ADC project vs runtime Vertex project.
- Llama now runs a prerequisite accessibility check before every llama run (same endpoint/model validation as standalone `llama_prereq`) and performs real inference via an OpenAI-compatible chat completions endpoint using `LLAMA_BASE_URL`.
- For vision-capable llama models (for example `llama3.2-vision`), keyframe images are sent as multimodal inputs; placeholder outputs (`None`, `N/A`, `unknown`) are rejected and fallback behavior is used instead.
- Sonnet/Qwen remain adapter stubs.
- Video type is auto-detected from the path (`handheld`/`hhv_` => `hhv`, `screenrec`/`srv_` => `srv`).
