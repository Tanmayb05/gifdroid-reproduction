# Qwen Vision Integration Plan

## Goal

Replace (or complement) Llama 3.2 Vision with Qwen2.5-VL as the primary vision-language model
for GIFdroid action inference. Qwen2.5-VL is a stronger multimodal model that handles Android
UI screenshots more accurately than Llama 3.2 Vision.

## Model Selection

| Model | Size | RAM Required | Vision | Why |
|-------|------|-------------|--------|-----|
| `llama3.2-vision:latest` | 7.8 GB | ~10 GB | Yes | Baseline; already working |
| `qwen2.5vl:7b` | ~5.5 GB | ~8 GB | Yes | **Recommended** — stronger multimodal, fits M3 Pro |
| `qwen2.5vl:32b` | ~20 GB | ~26 GB | Yes | Overkill for M3 Pro 18 GB |

**Chosen model: `qwen2.5vl:7b`** — best quality/performance trade-off for Apple Silicon M3 Pro.

## Pull Command

```bash
ollama pull qwen2.5vl:7b
```

## Changes Made

### 1. `gifdroid_llm/providers.py`

`QwenProvider` was a stub. It is now a full implementation:

- Reads `QWEN_BASE_URL` from env (Ollama local endpoint).
- Reads optional `QWEN_API_KEY` (not needed for local Ollama).
- Reads optional `QWEN_TIMEOUT_SEC` for per-inference timeout.
- Uses the same OpenAI-compatible `/v1/chat/completions` API as `LlamaProvider`.
- `_supports_vision()` detects `vl` in model name → sends multimodal payloads.
- Images are resized to max 768px and base64-encoded as JPEG (same as Llama).
- Streaming response with SSE parsing and heartbeat logging.
- `_parse_actions()` uses identical JSON schema validation as `LlamaProvider`.
- Fallback to deterministic heuristic on parse failure or provider error.

`create_provider()` updated to pass the prompt template path to `QwenProvider`
(defaults to `gifdroid_llm/input/prompts/llama_action_prompt_gemini_2.txt`).

### 2. `gifdroid_llm/env_loader.py`

- `REQUIRED_ENV_BY_LLM["qwen"]` reduced to `["QWEN_BASE_URL"]` only.
- `QWEN_API_KEY` is optional (local Ollama needs no auth).
- `QWEN_MODEL` removed — model is set via `llm_model` in `config.yml`.

### 3. `gifdroid_llm/main.py`

- Prereq check (`assert_llama_accessible`) now runs for both `llama` and `qwen`.
- Dynamically picks env var keys (`QWEN_BASE_URL`, `QWEN_API_KEY`, `QWEN_PREREQ_TIMEOUT_SEC`)
  based on the selected provider.

### 4. `.env.local.example`

- Qwen section updated for local Ollama usage.
- `QWEN_BASE_URL=http://localhost:11434/v1` (Ollama default).
- Optional timeout vars documented.

## Configuration

### To run with Qwen

Edit `gifdroid_llm/input/config.yml`:

```yaml
llm: "qwen"
llm_model: "qwen2.5vl:7b"
llama_action_prompt_file: "gifdroid_llm/input/prompts/llama_action_prompt_gemini_2.txt"
```

Add to `.env.local`:

```
QWEN_BASE_URL=http://localhost:11434/v1
```

### To run with Llama (unchanged)

```yaml
llm: "llama"
llm_model: "llama3.2-vision"
llama_action_prompt_file: "gifdroid_llm/input/prompts/llama_action_prompt_gemini_2.txt"
```

## Why Qwen2.5-VL is Better

1. **Stronger instruction following** — more reliably outputs valid JSON arrays.
2. **Better UI understanding** — trained on more diverse visual data including mobile UIs.
3. **Smaller footprint** — `qwen2.5vl:7b` is ~5.5 GB vs Llama's 7.8 GB.
4. **Context length** — 32K token context vs Llama's 128K (sufficient for GIFdroid workloads).

## Known Considerations

- Qwen2.5-VL uses `vl` in the model name slug which `_supports_vision()` already detects.
- The same prompt template (`llama_action_prompt_gemini_2.txt`) works for both models.
- If Qwen outputs `<think>...</think>` reasoning tokens (Qwen3 style), the JSON parser
  will still find the `[...]` array via the `bracket_idx` fallback in `_parse_actions`.
- `repeat_penalty: 1.3` is passed in the payload; Ollama applies it if the model supports it.

## CLI Usage

```bash
# Run with Qwen
.venv/bin/python -m gifdroid_llm.main \
  --config gifdroid_llm/input/config.yml \
  --env-file .env.local

# Verify Qwen endpoint is accessible
.venv/bin/python -m gifdroid_llm.llama_prereq \
  --base-url http://localhost:11434/v1 \
  --model qwen2.5vl:7b \
  --check-metal
```
