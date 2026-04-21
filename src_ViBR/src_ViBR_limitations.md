# src_ViBR Limitations

## Scope of this note
This list is grounded in:
- Source code under `src_ViBR/`
- Existing run artifacts under `apps/<app_name>/llm/ViBR/`

Quick dataset snapshot from current artifacts:
- Total runs in metadata: `49`
- Success: `27`
- Failed: `22`
- Handheld: `36` runs (`22` failed, `14` succeeded)
- Screenrec: `13` runs (`13` succeeded)

## 1) OpenAI model selection is effectively fixed to GPT-4o
Even when a run is configured with `llm_model: gpt-4o-mini`, OpenAI requests are hardcoded to `gpt-4o`.

Evidence:
- `src_ViBR/approach/openai_api.py` uses `model="gpt-4o"` in all three calls.
- `src_ViBR/approach/segment_replay.py` accepts `--llm-model`, but only Gemini has `set_model(...)` wiring.
- Example run log still says `Consistency Response from GPT-4o` while run metadata/log header may show `gpt-4o-mini`.

Impact:
- Cost/latency control from config is unreliable for OpenAI.
- Experiment reproducibility by model is reduced.

## 2) Pipeline is highly state-sensitive and drifts on handheld runs
The replay loop expects the live device to match recorded start states segment-by-segment.

Evidence:
- `max_attempts = 3` recovery loop in `segment_replay.py`.
- Frequent `same_state: "no"` and `Skipping action` in failed handheld logs (e.g., AntennaPod/LuxAlarm/HomeMedkit).
- Artifact-level pattern: all observed failures are in `handheld` runs; `screenrec` runs are all successful in current metadata.

Impact:
- Practical reliability depends heavily on tightly controlled initial app state.
- Replaying long recordings on natural device states is brittle.

## 3) ADB/UI dump fragility can abort runs early
UI XML extraction is a hard dependency and still fails in real runs.

Evidence:
- `adb_device_controller.py` raises after retries if `uiautomator dump`/pull fails.
- Multiple failed logs end with `RuntimeError: Failed to dump or pull UI XML`.

Impact:
- Device lock screen, foreground focus, transient ADB instability, or OEM behavior can terminate runs.

## 4) LLM output formatting can crash execution
The code expects strict JSON and does limited recovery parsing.

Evidence:
- `extract_json(...)` in `segment_replay.py` raises on parse failure.
- Observed failure: Gemini returned explanatory prose + fenced JSON; pipeline still crashed with `JSONDecodeError` in HomeMedkit failed run.

Impact:
- A single malformed/verbose LLM response can fail the entire run.

## 5) Provider/model availability errors are not gracefully degraded
Gemini provider errors (model access/version mismatch) bubble up as fatal runtime errors.

Evidence:
- `gemini_api.py` raises `RuntimeError` on non-retriable HTTP errors.
- Observed failure: `Gemini HTTP error 404` (model not found/access issue) in AntennaPod run.

Impact:
- Runs are sensitive to external model availability/configuration drift.
- No automatic fallback provider/model when the selected one fails.

## 6) Output schema and run metadata consistency is mixed
Run metadata is not fully uniform across historical outputs.

Evidence:
- Current `main.py` writes `llm`/`llm_model`, but many older metadata files omit these fields.
- Some runs marked `success` show `duration_sec: 0.0`, limiting interpretability.

Impact:
- Cross-run analytics and fair comparisons require schema-normalization logic.

## 7) `output.overwrite` is validated but not used
Config supports `output.overwrite`, but runtime pathing always increments run ID.

Evidence:
- `config.py` validates `output.overwrite`.
- No usage elsewhere (search in `src_ViBR/*.py` shows no runtime read of this flag).
- `io_utils.py` always uses `_next_run_id(...)`.

Impact:
- Config suggests behavior that does not exist.
- Users may assume overwrite semantics that never happen.

## 8) Source detection relies on path naming heuristics
Video source classification depends on filename/path tokens like `hhv`, `srv`, `handheld`, `screenrec`.

Evidence:
- `io_utils.detect_video_source(...)` checks path substrings only.

Impact:
- Non-standard filenames can fail source detection even when video is valid.

## 9) Action execution lacks post-action verification at actuator level
Executor sends ADB events directly with minimal guardrails.

Evidence:
- `execute_action.py` executes commands directly from action dict.
- Unknown action types are logged and ignored rather than triggering controlled recovery.

Impact:
- Silent skips can hide policy/model errors.
- Mislocalized taps/swipes are hard to diagnose without deeper telemetry.

## 10) Runtime/performance variability is large
Observed run durations vary from seconds to ~20+ minutes.

Evidence:
- Metadata examples include durations from `0.0` to `1244.2` seconds.
- Logs show expensive per-frame processing and heavy model calls (CLIP + DINO + LLM loop).

Impact:
- Hard to budget CI/runtime.
- Throughput depends strongly on hardware, video length, and provider latency.

## 11) Current artifact coverage is algorithm-skewed
All observed metadata runs use `algorithm: clip`.

Evidence:
- Artifact scan shows clip-only runs (`49/49`).
- `ssim` path exists in code but has little/no evidence in current app outputs.

Impact:
- Real-world quality/robustness conclusions for SSIM remain under-validated in this workspace.

## 12) Segment index edge case can crash late
There is at least one observed `IndexError: list index out of range` in segment iteration.

Evidence:
- Failed LuxAlarm run ends at `start_img = frames[start]` with `IndexError`.

Impact:
- Late-stage crashes waste full-run time and require reruns.

---

## Suggested prioritization (highest ROI first)
1. Fix OpenAI model plumbing so configured `llm_model` is actually used.
2. Harden JSON extraction/validation and add retry/re-ask on malformed outputs.
3. Add robust state sync hooks (explicit reset/checkpoints) before each segment.
4. Make ADB/UI dump recovery more defensive (health checks, app refocus, retry tiers).
5. Implement or remove `output.overwrite` to match config expectations.
6. Add deterministic run telemetry (per-step success/failure counters + schema version).
