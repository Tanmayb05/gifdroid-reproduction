# Qwen2.5-VL: Model Runner Crash (HTTP 500) on Multi-Image Inference

## Symptom

When running `qwen2.5vl:7b` via Ollama with 8 keyframe images, the inference request
fails with HTTP 500:

```
{"error":{"message":"model runner has unexpectedly stopped, this may be due to resource
limitations or an internal error, check ollama server logs for details","type":"api_error"}}
```

The pipeline falls back to the deterministic heuristic instead of using LLM inference.

## Environment

- Hardware: Apple Silicon M3 Pro (18 GB unified memory)
- Model: `qwen2.5vl:7b` (6.0 GB)
- Ollama version: local
- Images sent per request: 8 keyframes at 768px max dimension

## Root Cause

Two compounding VRAM allocation issues:

1. **Default context window too large** — Qwen2.5-VL has a 32K token context window.
   Ollama pre-allocates KV cache proportional to `num_ctx`. Without an explicit cap,
   this consumes several GB of unified memory before image processing even starts.

2. **Image token budget** — At 768px, each image generates ~500–800 visual tokens.
   With 8 images, that's up to 6400 visual tokens on top of the KV cache allocation,
   causing the model runner to exceed available memory and crash.

## Fix

Two changes in `gifdroid_llm/providers.py` (`QwenProvider`):

### 1. Cap `num_ctx` to 4096

```python
payload: Dict[str, Any] = {
    "model": self.llm_model,
    "temperature": 0.1,
    "repeat_penalty": 1.3,
    "stream": True,
    "num_ctx": 4096,   # ← added
}
```

4096 tokens is ample for the GIFdroid prompt + image tokens + JSON response.
This prevents Ollama from pre-allocating a 32K KV cache.

### 2. Reduce image max dimension from 768px → 512px

```python
# In QwenProvider._encode_keyframe_data_url()
max_dim = 512   # was 768
```

Qwen2.5-VL performs well at 512px for Android UI analysis. The reduction cuts
visual token count per image by ~55%, making 8-image batches feasible.

## Result

With both fixes applied, `qwen2.5vl:7b` completes multimodal inference on 8 keyframes
without crashing on an M3 Pro 18 GB.

## Notes

- `LlamaProvider` keeps 768px — `llama3.2-vision` uses a smaller vision encoder and
  does not exhibit this issue.
- If inference still crashes on very long videos (>10 keyframes), reduce `num_ctx`
  further to `2048` or lower `ssim_threshold` in config to produce fewer keyframes.
