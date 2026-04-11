# Issue: llama_action_prompt_gemini_1.txt uses wrong schema — parse fails, repetition loop in output

## Summary
The prompt file configured for the Llama provider (`llama_action_prompt_gemini_1.txt`) was written
for a Gemini-style workflow and instructs the model to return a nested JSON **object** with a
`replay_trace` array. The Llama parser (`_parse_actions` in `providers.py`) expects a flat JSON
**array** with `action_type`, `screen_description`, `target`, `details`, `confidence` keys. The
schema mismatch causes every run to fall through to the deterministic fallback, and the model also
enters a repetition loop filling `screen_description` values with thousands of `"  "` characters.

## Context
LLM keyframe analysis pipeline — `src_llm` module, Llama provider (`providers.py`).
Introduced when `llama_action_prompt_file: "src_llm/input/prompts/llama_action_prompt_gemini_1.txt"`
was set in `config.yml`. The prompt was generated as a Gemini schema-first prompt and was never
adapted for the Llama provider.
Affects all runs using `llm: "llama"` + `llm_model: "llama3.2-vision"` with this prompt file.

## Expected behavior
The model returns a flat JSON array with one object per keyframe:
```json
[
  {"screen_description": "...", "action_type": "launch", "target": "...", "details": "...", "confidence": 0.9}
]
```
`_parse_actions` finds a `[` at the start of the response, parses the array, and returns
`List[ProviderAction]`.

## Actual behavior
Two compounding problems:

1. **Wrong schema**: The model follows the prompt and responds with a nested JSON object:
   ```json
   {
     "video": "...",
     "replay_trace": [
       {"step_index": 1, "action": {"type": "tap", "target": "...", "details": "..."}, ...}
     ]
   }
   ```
   `_parse_actions` looks for a leading `[` (or `\n[`) and finds none → returns `None` →
   pipeline falls back to deterministic heuristic for every run.

2. **Repetition loop inside wrong schema**: Llama also enters a token repetition loop inside the
   `screen_description` values, filling them with thousands of `"  "` characters:
   ```
   "screen_description": "Adaway home screen with  "  "  "  "  "  "  "  "  "  ...
   ```
   This produces a 60KB+ raw response file even though the JSON is structurally unusable.

3. **Conversational preamble**: Before the JSON, the model outputs prose explaining its reasoning
   steps ("To generate a structured replay_trace, I will follow these steps: 1. Analyse..."),
   which also breaks the `[`-prefix check.

Example from `apps/adaway/llm/llama/llama3-2-vision/handheld/.../run-002/llm_raw_response.txt`:
```
To generate a structured `replay_trace` in the exact JSON format specified, I will follow
these steps:
1. **Analyze the provided screen recording**...
...
```json
{
  "video": "...adaway/videos/screenrec/srv-001.mp4",
  "replay_trace": [
    {
      "step_index": 2,
      "screen_description": "Adaway home screen with  "  "  "  "  "  ...
```

## Steps to reproduce
1. Set `llama_action_prompt_file: "src_llm/input/prompts/llama_action_prompt_gemini_1.txt"` in `config.yml`
2. Configure `llm: "llama"`, `llm_model: "llama3.2-vision"`
3. Run the pipeline on any app video
4. Inspect `apps/<app>/llm/llama/llama3-2-vision/<source>/<variant>/run-<N>/llm_raw_response.txt`

## Inputs / environment
- Branch: `refactor`
- Commit: `aeaa45af3ef0335ff9132bec8bc1e8660554ad0b`
- Environment: local
- OS: macOS 26.3.1
- Python: 3.13.7 (`.venv`)
- Ollama server: 0.19.0
- Model: `llama3.2-vision` (11B)
- Frame sampling: `fps: 1.5`, `max_frames: 100`, keyframe method: `ssim`
- Prompt: `src_llm/input/prompts/llama_action_prompt_gemini_1.txt`
- Observed on: adaway handheld run-002 (`2026-04-01T22:19:15`, duration 2115.6s)

## Evidence
- File: `apps/adaway/llm/llama/llama3-2-vision/handheld/fps1-5__max100__ssim__gap1__ssim0-95__stable2/run-002/llm_raw_response.txt`
- File size: ~67KB
- Response begins with prose preamble, then a markdown-fenced JSON object (not array)
- `screen_description` for step 2 ends with thousands of `"  "` repetitions
- `metadata.json` reports `"status": "success"` — the pipeline did not error, it silently fell
  back to deterministic heuristic

## Root cause
`llama_action_prompt_gemini_1.txt` was written as a Gemini schema-first prompt. It:
- Instructs the model to return a JSON **object** with keys `video`, `llm`, `video_type`,
  `app_name`, `generated_at`, `replay_trace`
- Uses a nested `action` sub-object with `type`/`target`/`details` (not the flat `action_type`)
- Does not use the `{KEYFRAMES}` placeholder that `_build_action_prompt` injects
- Does not say "no markdown fences, no prose" — so the model adds both

`LlamaProvider._parse_actions` (`providers.py:608`) is written for the flat-array schema and
rejects any response that does not start with `[`. The object schema response is always rejected.

## Fix (Option A — correct prompt)
Write a new prompt file (`src_llm/input/prompts/llama_action_prompt.txt`) that:
- Uses `{KEYFRAMES}` so `_build_action_prompt` can inject the keyframe list
- Instructs the model to return ONLY a flat JSON array, no markdown fences, no prose
- Uses the flat schema with `action_type` (not `type`) and the exact keys `_parse_actions` reads:
  `screen_description`, `action_type`, `target`, `details`, `confidence`
- Uses `action_type` values from the allowed set: `launch`, `tap`, `type`, `swipe`, `scroll`,
  `wait`, `long_press`, `back`, `open_menu`, `select`
- Uses a neutral (non-AdAway) example to avoid model anchoring (see
  [llama-ignores-json-instruction-hallucinates.md](llama-ignores-json-instruction-hallucinates.md))

Update `config.yml`:
```yaml
llama_action_prompt_file: "src_llm/input/prompts/llama_action_prompt.txt"
```

## Files to change
- `src_llm/input/prompts/llama_action_prompt.txt` (create)
- `src_llm/input/config.yml` (update `llama_action_prompt_file`)

## Validation
- [ ] Run adaway handheld — confirm `llm_raw_response.txt` starts with `[` and contains no prose preamble
- [ ] Confirm `_parse_actions` returns a non-None result (no fallback warning in logs)
- [ ] Spot-check `execution_trace.json` — steps should reflect actual keyframe content, not deterministic heuristic targets (`ui_element_step_N`)
- [ ] Run at least one screenrec variant to confirm both video types are fixed

## Status
Open
