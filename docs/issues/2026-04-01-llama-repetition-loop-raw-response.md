# Issue: llama3.2-vision repetition loop produces garbage llm_raw_response.txt

## Summary
When using llama3.2-vision as the LLM provider, the model enters a token repetition loop
mid-generation, filling the output with thousands of `\xa0…` characters instead of valid JSON.

## Context
LLM keyframe analysis pipeline — `gifdroid_llm` module, Llama provider (`providers.py`).
Affects any run using `llm: "llama"` + `llm_model: "llama3.2-vision"` with SSIM or LLM-assisted
keyframe selection. Output is written to `llm_raw_response.txt` per run directory.

## Expected behavior
The model returns a valid JSON array of keyframe action objects, e.g.:
```json
[
  {"screen_description": "...", "action_type": "launch", "target": "...", "details": "...", "confidence": 0.9}
]
```

## Actual behavior
`llm_raw_response.txt` is a single 100KB+ line. The content is a JSON array where the first
`screen_description` value is cut off and padded with thousands of `\xa0…` (non-breaking space +
ellipsis) repetitions until the token limit is hit. The file appears to contain `—` and `…`
characters when viewed in an IDE (IDE rendering of the unicode), leading to the appearance of
`----` output.

Example of actual content (truncated):
```
[
  {"screen_description": "AdAway home screen with Ad\xa0—\xa0…\xa0—\xa0…\xa0—\xa0… [x10000]
```

## Steps to reproduce
1. Configure `config.yml` with `llm: "llama"`, `llm_model: "llama3.2-vision"`
2. Run the pipeline on any app video (handheld or screenrec)
3. Inspect `apps/<app>/llm/llama/llama3-2-vision/<source>/<variant>/run-<N>/llm_raw_response.txt`

## Prompt
Prompt template used by `gifdroid_llm/providers.py` for Llama action inference:

```text
You are a mobile QA engineer analysing screenshots from an Android app recording.
Each screenshot image is a keyframe extracted from the video at the listed timestamp.
Your task: describe what is visible on each screen and what user action caused the transition.

Rules:
- Look at the actual screenshot image to write screen_description. Describe the visible UI: screen title, main content area, buttons, dialogs, lists — be specific.
- action_type must be one of: launch, tap, type, swipe, scroll, wait, long_press, back, open_menu, select.
- target must name the concrete UI element the user interacted with (e.g. 'Enable AdAway button', 'Hosts sources list', 'OK dialog button'). Never use None, N/A, unknown, or null.
- details must explain in one sentence why that action was taken or what changed.
- confidence is a float 0-1 reflecting how certain you are from the visual evidence.
- motion_score hints at transition magnitude (0=static, high=large visual change); use it as a secondary signal only — the screenshot is primary.
- Return ONLY a valid JSON array, no markdown fences, no extra text.
- The array must have EXACTLY one object per keyframe, in order.

Example output format (2 keyframes):
[
  {"screen_description": "AdAway home screen showing Enable button and status disabled", "action_type": "launch", "target": "app_entrypoint", "details": "App launched and showing initial disabled state.", "confidence": 0.92},
  {"screen_description": "Hosts sources list with three entries and a refresh icon in toolbar", "action_type": "tap", "target": "Hosts sources menu item", "details": "User opened hosts sources to review blocklist entries.", "confidence": 0.85}
]

Keyframes to analyse:
- idx=1, timestamp_sec=<...>, motion_score=<...>
- idx=2, timestamp_sec=<...>, motion_score=<...>
- ...
```

For vision models (like `llama3.2-vision`), each keyframe image is attached in the same request as
multimodal content (`image_url` data URLs), so the model receives both this text prompt and the
actual screenshots.

## Inputs / environment
- Branch: `refactor`
- Commit: `aeaa45af3ef0335ff9132bec8bc1e8660554ad0b`
- Environment: local
- OS: macOS 26.3.1
- Python: 3.13.7 (`.venv`)
- Ollama server: 0.19.0
- Model: `llama3.2-vision` (11B)
- Frame sampling: `fps: 1.5`, `max_frames: 100`, keyframe method: `ssim`
- Observed on: simplenotes (screenrec), and likely all other apps

## Evidence
- File: `apps/simplenotes/llm/llama/llama3-2-vision/screenrec/fps1-5__max100__ssim__gap1__ssim0-95__stable2/run-001/llm_raw_response.txt`
- File size: 102,421 bytes, 1 line
- Content inspection:
  ```
  Total length: 41001 chars
  First 500: '[\n  {"screen_description": "AdAway home screen with Ad\xa0—\xa0…\xa0—\xa0…\xa0—\xa0…
  ```
- Run metadata shows `keyframe_count: 8` — frame count is not the cause

## Suspected cause
llama3.2-vision (11B) is prone to token repetition loops when generating structured (JSON) output.
Once the model begins repeating a token pattern, it continues until the context/token limit is
reached. No `repeat_penalty` was set in the Ollama API request, allowing the loop to run
unchecked.

## Fix implemented
Added `repeat_penalty: 1.3` to the Ollama `/v1/chat/completions` request payload in the Llama
provider. This penalizes the model for reusing recently generated tokens, breaking the loop.

```python
payload: Dict[str, Any] = {
    "model": self.llm_model,
    "temperature": 0.1,
    "repeat_penalty": 1.3,   # added
    "stream": True,
}
```

## Files changed
- `gifdroid_llm/providers.py` (line 510)

## Risk / side effects
- `repeat_penalty` is an Ollama-specific parameter; it is silently ignored by other providers
  (Gemini), so no cross-provider impact.
- Very high values (>1.5) can cause the model to avoid reasonable repetitions (e.g. repeated
  action types like `"tap"`) and degrade output quality. 1.3 is a conservative starting point.

## Validation
- [ ] Re-run simplenotes screenrec with the fix and confirm `llm_raw_response.txt` contains valid
      JSON without `\xa0…` padding
- [ ] Spot-check 2–3 other apps (handheld + screenrec) to confirm no regression
- [ ] If loop still occurs at 1.3, increase to 1.5 and re-test

## Status
Fixed (unvalidated — fix applied, re-runs pending)
