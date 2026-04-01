# Issue: llama3.2-vision ignores JSON-only instruction and hallucinates app content

## Summary
llama3.2-vision responds in markdown prose instead of the required JSON array, and consistently
hallucinates "AdAway" as the app name regardless of which app video was actually provided.

## Context
LLM keyframe analysis pipeline — `gifdroid_llm` module, Llama provider (`providers.py`).
The prompt (`gifdroid_llm/input/prompts/llama_action_prompt_baseline.txt`) explicitly instructs
the model: *"Return ONLY a valid JSON array, no markdown fences, no extra text."*
Affects all `run-002` runs across all apps using `llm: "llama"` + `llm_model: "llama3.2-vision"`.

## Expected behavior
The model returns a valid JSON array with one object per keyframe, exactly as shown in the prompt
example:
```json
[
  {"screen_description": "...", "action_type": "launch", "target": "...", "details": "...", "confidence": 0.95}
]
```

## Actual behavior
The model:
1. **Ignores the JSON-only instruction** — responds in markdown bullet/prose format (`**Keyframe 1:**`, `* Screen description: ...`)
2. **Hallucinates the app name** — describes "AdAway home screen" for all apps (simplenotes, wifianalyzer, portauthority, etc.) regardless of what is actually in the video
3. **Still falls into repetition loops** — some files end with thousands of repeated `"  "` characters inside a JSON string value, even after `repeat_penalty: 1.3` was added
4. **Ignores the actual screenshots** — screen descriptions are generic/wrong and do not reflect the real UI visible in the keyframe images

Example from `apps/simplenotes/.../handheld/.../run-002/llm_raw_response.txt`:
```
**Keyframe 1:**
* Screen description: AdAway home screen with a disabled status.
* Action: launch
...
**Keyframe 4:**
* Screen description: Ad-A-Wa- status screen.   ← hallucinated + garbled
* Action: tap
* Target: Ad-A-Wa- status
```

## Steps to reproduce
1. Configure `config.yml` with `llm: "llama"`, `llm_model: "llama3.2-vision"`
2. Run the pipeline on any app video (handheld or screenrec) — confirmed on simplenotes, wifianalyzer, portauthority, adaway (screenrec), all run-002
3. Inspect `apps/<app>/llm/llama/llama3-2-vision/<source>/fps1-5__max100__ssim__gap1__ssim0-95__stable2/run-002/llm_raw_response.txt`

## Inputs / environment
- Branch: `refactor`
- Commit: `aeaa45af3ef0335ff9132bec8bc1e8660554ad0b`
- Environment: local
- OS: macOS 26.3.1
- Python: 3.13.7 (`.venv`)
- Ollama server: 0.19.0
- Model: `llama3.2-vision` (11B)
- Frame sampling: `fps: 1.5`, `max_frames: 100`, keyframe method: `ssim`
- Prompt: `gifdroid_llm/input/prompts/llama_action_prompt_baseline.txt`
- `repeat_penalty: 1.3` was already applied before these run-002s were generated

## Evidence
Files affected (all run-002):
- `apps/simplenotes/llm/llama/llama3-2-vision/handheld/.../run-002/llm_raw_response.txt`
- `apps/simplenotes/llm/llama/llama3-2-vision/screenrec/.../run-002/llm_raw_response.txt`
- `apps/wifianalyzer/llm/llama/llama3-2-vision/handheld/.../run-002/llm_raw_response.txt`
- `apps/wifianalyzer/llm/llama/llama3-2-vision/screenrec/.../run-002/llm_raw_response.txt`
- `apps/portauthority/llm/llama/llama3-2-vision/handheld/.../run-002/llm_raw_response.txt`
- `apps/portauthority/llm/llama/llama3-2-vision/screenrec/.../run-002/llm_raw_response.txt`
- `apps/adaway/llm/llama/llama3-2-vision/screenrec/.../run-002/llm_raw_response.txt`

Run timestamps: `2026-04-01T21:57` – `2026-04-01T22:11` (after `repeat_penalty` fix was applied)

Repetition loop still present in simplenotes handheld run-002 (ends with thousands of `"  "`):
```
"details": "The user has tapped on the Ad-A-Wa- status.", "  "  "  "  "  "  "  " ...
```

## Suspected cause
llama3.2-vision (11B) has weak instruction-following for structured output formats:

1. **Markdown prose instead of JSON**: The model's RLHF training strongly biases it toward
   formatted markdown responses. The text-only "Return ONLY a JSON array" instruction is
   insufficient to override this bias when processing multimodal (image) input.

2. **AdAway hallucination**: The prompt example uses AdAway as the sample app. The model is
   pattern-matching to the example rather than attending to the actual images. This suggests
   the model is not properly processing the attached image data URLs, or is ignoring them in
   favour of the text context.

3. **Repetition loop persists despite `repeat_penalty: 1.3`**: The penalty may be too low, or
   the Ollama `/v1/chat/completions` endpoint may not honour `repeat_penalty` at the top level
   (it may need to be nested under an `options` key for the native Ollama API).

## Fix implemented
None yet. The `repeat_penalty: 1.3` added in the previous issue
([llama-repetition-loop-raw-response.md](llama-repetition-loop-raw-response.md)) did not resolve
these problems.

## Files changed
- None (open issue)

## Risk / side effects
- All llama3.2-vision runs produce unusable output — downstream JSON parsing will fail on markdown
  prose responses
- The AdAway hallucination means even partial JSON extracted from these responses is wrong data

## Validation
Potential fixes to try (not yet validated):
- Move `repeat_penalty` under an `options` key: `"options": {"repeat_penalty": 1.5}`
- Add `"format": "json"` to the Ollama payload to force JSON mode
- Prefix the prompt with a stronger constraint: `RESPOND WITH JSON ONLY. NO PROSE. NO MARKDOWN.`
- Replace the AdAway example in the prompt with a neutral placeholder to prevent anchoring
- Test with a different model (e.g. `llava`, `gemini-2.5-flash`) as a baseline

## Status
Open
