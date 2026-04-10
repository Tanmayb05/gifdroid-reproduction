# Gemini Video Mode — Implementation Plan

Upload the raw `.mp4` directly to Vertex AI and let Gemini analyze the full video timeline, bypassing the frame-extraction + keyframe-selection pipeline entirely.

Activated by setting `video_mode: true` in `config.yml`. This is a generic pipeline-level flag — it is not tied to Gemini specifically and is designed to be implementable by any provider. When set, the keyframe pipeline is skipped even if `frame_sampling` and `keyframe_selection` are present in config.

---

## Decisions Log

| Question | Decision |
|----------|----------|
| Auth path | Vertex AI (ADC) only |
| Upload failure | Hard-fail the run, then skip it (same as `VideoError` skip behavior) |
| File cleanup | Delete immediately after inference (recommended — avoids storage quota buildup across many runs) |
| `frame_file` field | Set to `"video:MM:SS"` — no schema change needed, `TraceStep.frame_file` is a plain `str` |
| Provider interface | New abstract method `infer_actions_from_video(video_path)` on `BaseLLMProvider`; only `GeminiVideoProvider` implements it now |
| Prompt granularity | One action per meaningful user interaction (variable-length, sparse output) |

---

## Current Pipeline vs Video Mode

| Stage | Current (keyframe mode) | Video mode |
|-------|------------------------|------------|
| Frame extraction | `VideoFrameExtractor` at 1.5 FPS | **skipped** |
| Keyframe selection | Motion/SSIM heuristic | **skipped** |
| LLM input | ~10–15 keyframe PNGs + timestamps as text | Raw `.mp4` via Vertex AI File API |
| LLM output | One `ProviderAction` per keyframe | One `ProviderAction` per meaningful interaction |
| `frame_file` in trace | `kf-0001.png` etc. | `"video:00:10"` etc. |
| File cleanup | N/A | Delete uploaded file from Vertex AI after run |

---

## Video Corpus

| App | Type | Size | Duration |
|-----|------|------|----------|
| adaway | handheld | 13.9 MB | 44.4s |
| adaway | screenrec | 3.0 MB | 29.8s |
| antennapod | handheld | 12.8 MB | 34.2s |
| antennapod | screenrec | 5.1 MB | 36.9s |
| homemedkit | handheld | 14.7 MB | 41.7s |
| homemedkit | screenrec | 7.1 MB | 27.4s |
| jigsaw | handheld | 5.6 MB | 15.3s |
| jigsaw | screenrec | 2.3 MB | 21.3s |
| luxalarm | handheld | 7.5 MB | 24.7s |
| luxalarm | screenrec | 6.4 MB | 30.0s |
| portauthority | handheld | 11.5 MB | 29.4s |
| portauthority | screenrec | 9.8 MB | 114.9s |
| simplenotes | handheld | 12.4 MB | 39.1s |
| simplenotes | screenrec | 4.1 MB | 19.5s |
| wifianalyzer | handheld | 8.7 MB | 20.9s |
| wifianalyzer | screenrec | 8.9 MB | 27.5s |

**Total: 16 videos, 133.7 MB.** All well under the 2 GB per-file limit.

Estimated token cost: ~300 tokens/sec × ~590s total video = **~177,000 tokens** across all 16 runs.

---

## API Mechanics (Vertex AI)

### Auth

Reuse the existing `_build_default_adc_token()` method already in `GeminiProvider`. No new env vars needed.

Token scope required: `https://www.googleapis.com/auth/cloud-platform`

### File upload endpoint (Vertex AI)

Vertex AI uses the **Google AI unified SDK** resumable upload protocol via the regional endpoint:

```
POST https://{LOCATION}-aiplatform.googleapis.com/upload/v1beta1/projects/{PROJECT}/locations/{LOCATION}/files
Headers:
  Authorization: Bearer {adc_token}
  X-Goog-Upload-Protocol: resumable
  X-Goog-Upload-Command: start
  X-Goog-Upload-Header-Content-Length: {file_size}
  X-Goog-Upload-Header-Content-Type: video/mp4
Body: {"file": {"display_name": "{app_name}_{video_type}"}}

→ Response header: X-Goog-Upload-URL (session URI)

PUT {session_uri}
Headers:
  Authorization: Bearer {adc_token}
  X-Goog-Upload-Offset: 0
  X-Goog-Upload-Command: upload, finalize
  Content-Length: {file_size}
Body: <raw mp4 bytes>

→ Response: {"name": "projects/.../files/xxx", "uri": "...", "state": "PROCESSING"}
```

### Polling

```
GET https://{LOCATION}-aiplatform.googleapis.com/v1beta1/{file.name}
Headers:
  Authorization: Bearer {adc_token}

→ Repeat every 5s until {"state": "ACTIVE"}
→ Timeout after 300s → raise ProviderError
```

### generateContent payload

```json
{
  "contents": [{
    "role": "user",
    "parts": [
      {
        "fileData": {
          "mimeType": "video/mp4",
          "fileUri": "<file.uri>"
        }
      },
      {"text": "<video_prompt>"}
    ]
  }],
  "generationConfig": {"temperature": 0.1}
}
```

The existing `_call_gemini` / `_extract_text` methods handle the rest of the generateContent call — they only need to receive the updated payload parts.

### Delete after inference

```
DELETE https://{LOCATION}-aiplatform.googleapis.com/v1beta1/{file.name}
Headers:
  Authorization: Bearer {adc_token}
```

Called in a `finally` block so it runs even on parse failures.

---

## Files to Change

### 1. `gifdroid_llm/providers.py`

**`BaseLLMProvider`** — add a new abstract-optional method with a default `NotImplementedError` raise:

```python
def infer_actions_from_video(self, video_path: Path) -> List[ProviderAction]:
    raise NotImplementedError(
        f"Provider '{self.llm_name}' does not support video_mode. "
        "Only 'gemini' is currently supported."
    )
```

This means any provider can be extended to support video mode in future without touching the pipeline. The base class raises clearly if a provider hasn't implemented it yet.

**`GeminiVideoProvider(GeminiProvider)`** — new subclass with:

- `_upload_video(video_path: Path) -> tuple[str, str]`  
  Returns `(file_uri, file_name)`. Two-step resumable upload to Vertex AI. Raises `ProviderError` on failure.

- `_poll_until_active(file_name: str, timeout_sec: int = 300) -> None`  
  Polls `GET .../v1beta1/{file_name}` every 5s. Raises `ProviderError` on timeout or `FAILED` state.

- `_delete_file(file_name: str) -> None`  
  Best-effort DELETE in `finally` block. Logs warning if it fails, does not raise.

- `infer_actions_from_video(video_path: Path) -> List[ProviderAction]`  
  Override: upload → poll → generateContent → parse → delete. Raises `ProviderError` on any failure (no deterministic fallback).

- Inherits `_build_default_adc_token`, `_call_gemini`, `_extract_text`, `_parse_actions` from `GeminiProvider` unchanged.

Update `create_provider()` factory: when `llm == "gemini"` and `video_mode=True`, return `GeminiVideoProvider` instead of `GeminiProvider`.

### 2. `gifdroid_llm/config.py`

Add `video_mode: bool` to `AppConfig` (default `False`).

In `_parse_shared()`, read:
```python
video_mode = bool(root.get("video_mode", False))
```

Validation: if `video_mode: true` and `llm` is not in the set of providers that implement `infer_actions_from_video` (currently only `"gemini"`), raise `ConfigError` with a clear message listing which providers support it.

`frame_sampling` and `keyframe_selection` remain in config and are parsed normally — they are just not used when `video_mode` is `True`. This avoids breaking existing configs that have those fields.

### 3. `gifdroid_llm/main.py`

In `run_single()`, branch after provider creation:

```python
if cfg.video_mode:
    # Video mode: skip frame extraction and keyframe selection entirely
    provider_actions = provider.infer_actions_from_video(resolved_video_path)
    # Build TraceSteps from returned actions (timestamp from action, frame_file = "video:MM:SS")
else:
    # Existing keyframe path
    sampled_frames, metadata = extractor.extract(...)
    keyframes = selector.select(...)
    selector.save_keyframes(...)
    provider_actions = provider.infer_actions(keyframes)
```

In video mode:
- `keyframes_dir` is never created
- `frames_manifest.json` is not written
- `ensure_write_policy` only checks `execution_trace_json_path`
- `TraceStep.frame_file` is set to `"video:{MM:SS}"` derived from `timestamp_sec`

### 4. `gifdroid_llm/io_utils.py`

The `config_slug` function currently encodes fps/max_frames/method. Add a branch:

```python
if cfg.video_mode:
    return "video-mode"
```

So output lands at:
```
apps/<app>/llm/gemini/<model>/<source>/video-mode/run-001/
```

This slug is provider-agnostic — if Qwen or Llama ever implement video mode, their output will use the same `video-mode/` directory pattern.

### 5. `gifdroid_llm/input/prompts/gemini_video_prompt.txt` _(new file)_

Prompt design (sparse, interaction-only):

```
You are analyzing a mobile app screen recording to extract a bug reproduction trace.

Watch the full video. Identify only the meaningful user interactions (taps, swipes, long-presses, text input, back navigation). Ignore idle frames, loading spinners, and system UI transitions that the user did not initiate.

For each user interaction, output one JSON object. Return a JSON array only — no markdown, no prose.

Each object must have exactly these keys:
- "timestamp_sec": number — seconds from start when the action occurs (e.g. 10.5)
- "screen_description": string — brief description of the UI state at that moment
- "action_type": one of: "tap", "long_press", "swipe_up", "swipe_down", "swipe_left", "swipe_right", "type", "back", "launch"
- "target": string — the UI element or region interacted with
- "details": string — any relevant detail (text typed, direction, etc.)
- "confidence": number between 0 and 1

Return only the JSON array.
```

### 6. `gifdroid_llm/input/config.yml`

Add the new flag at the top level:

```yaml
video_mode: true   # when true, skips keyframe pipeline and sends video directly to the provider
                   # currently only supported by llm: "gemini" via Vertex AI File API

llm: "gemini"
llm_model: "gemini-2.5-pro"

# frame_sampling and keyframe_selection are still required by config parser
# but are ignored when video_mode is true
frame_sampling:
  ...
keyframe_selection:
  ...
```

---

## Output Layout

```
apps/<app>/llm/gemini/gemini-2-5-pro/handheld/
  video-mode/
    run-001/
      execution_trace.json   ← frame_file values are "video:00:10" etc.
      metadata.json
      logs/
      llm_raw_response.txt
      # no keyframes/ directory
      # no frames_manifest.json
```

---

## Error Handling

| Failure point | Behavior |
|---------------|----------|
| `video_mode: true` with unsupported provider | `ConfigError` at startup — lists supported providers |
| ADC token fetch fails | `ProviderError` → caught in `run_single` → run skipped with warning |
| Upload HTTP error | `ProviderError` → same |
| Poll timeout (>300s) | `ProviderError` → same |
| generateContent HTTP error | `ProviderError` → same |
| Response parse failure | `ProviderError` (no deterministic fallback in video mode) → run skipped |
| Delete fails | Log warning only, do not raise |

The existing `run_pipeline` loop in `main.py` already catches exceptions and skips failed runs — video mode plugs into that same mechanism.

---

## Constraints & Token Cost

| Parameter | Value |
|-----------|-------|
| Max file size | 2 GB |
| Token cost | ~300 tokens/sec (standard resolution) |
| File TTL | 48h (but deleted immediately after run) |
| Gemini frame sampling | 1 FPS (fixed by the API) |
| Vertex AI location | `GEMINI_VERTEX_LOCATION` env var (default `us-central1`) |
| Project ID | `GEMINI_VERTEX_PROJECT_ID` env var (already used in `_call_gemini`) |

---

## Extending to Other Providers (Future)

To add video mode support to any other provider (e.g. Qwen via Ollama, or a future Claude provider):
1. Override `infer_actions_from_video(video_path)` in that provider class
2. Add the provider name to the `VIDEO_MODE_SUPPORTED_PROVIDERS` set in `config.py`

No changes to `main.py`, `io_utils.py`, or `trace.py` needed.

---

## Implementation Phases

### Phase 1 — Config flag
- Add `video_mode: bool` to `AppConfig` and `_parse_shared()`
- Add `VIDEO_MODE_SUPPORTED_PROVIDERS = {"gemini"}` set to `config.py` for validation
- Add `"video-mode"` config slug to `io_utils.py`

### Phase 2 — Base class method
- Add default `infer_actions_from_video` to `BaseLLMProvider` that raises `NotImplementedError`

### Phase 3 — Upload + poll + delete (Gemini)
- Implement `_upload_video`, `_poll_until_active`, `_delete_file` in `GeminiVideoProvider`
- Manually test upload with one video, verify `ACTIVE` state, verify delete

### Phase 4 — Inference
- Write `gifdroid_llm/input/prompts/gemini_video_prompt.txt`
- Implement `infer_actions_from_video` in `GeminiVideoProvider`
- Reuse `_parse_actions` from `GeminiProvider`; adapt timestamp extraction from response

### Phase 5 — Pipeline integration
- Branch in `main.py` `run_single()` on `cfg.video_mode`
- Build `TraceStep` list from `ProviderAction` list in video mode (no keyframes)
- Skip `frames_manifest.json` write in video mode
- Update `ensure_write_policy` to not check `keyframes_dir` in video mode

### Phase 6 — Validation
- Run against all 16 videos
- Compare traces to keyframe-mode baseline
- Spot-check `frame_file` values and timestamp accuracy
