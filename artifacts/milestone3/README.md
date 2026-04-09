# Milestone 3 — Multi-Turn Decision Loop (No Video)

**Status**: CLEARED (2026-04-08)

## Verification Results

| Test | Status | Notes |
|------|--------|-------|
| V3.1 — Single action round-trip | **Pass** | `continue=True`, action `tap org.adaway:id/snackbar_action`, screenshot saved |
| V3.2 — 3-step blind loop | **Pass** | Loop ran 5 steps, `status=done` after "VPN configuration successfully updated" |
| V3.3 — Sliding window history | **Pass** | 5 turns added, `get_history()` returns 3 (window correct) |
| Regression — existing pipeline dry-run | **Pass** | All 20 configured runs exit OK (4 skipped for missing video files, same as prior milestones) |

## Key Evidence

### V3.1 — Single round-trip
```text
Decision: continue=True
Action: ExecutableAction(type='tap', resource_id='org.adaway:id/snackbar_action', coordinates=[954, 1747], ...)
Reasoning: The screen displays a message at the bottom stating 'Your configuration changed. You need to apply it.'
Action executed. Screenshot saved.
```

### V3.2 — 5-step loop trace summary
```json
{
  "task": "Open AdAway and apply host sources configuration.",
  "total_steps": 5,
  "status": "done",
  "steps": [
    {"step": 1, "action": {"type": "tap", "coordinates": [73, 136], "target_description": "the back arrow"}},
    {"step": 2, "action": {"type": "tap", "resource_id": "org.adaway:id/sourcesCardView"}},
    {"step": 3, "action": {"type": "tap", "coordinates": [73, 136], "target_description": "the back arrow"}},
    {"step": 4, "action": {"type": "tap", "resource_id": "org.adaway:id/updateImageView"}},
    {"step": 5, "action": {"type": "done"}, "continue": false}
  ]
}
```
LLM correctly identified task completion: "VPN configuration successfully updated."

### V3.3 — Sliding window
```text
Total turns added: 5, History window: 3 (expected 3)
Sliding window OK
```

## Artifacts

- `v3_1_output.txt` — V3.1 console output
- `v3_2_session_trace.json` — full session trace from V3.2
- `v3_3_sliding_window.txt` — V3.3 output
- `milestone3_after_step1.png` — screenshot after first LLM-directed action (V3.1)
- `milestone3_run/` — step screenshots and session trace from V3.2 loop
- `v3_regression_dry_run.txt` — regression dry-run output

## New Code

- `gifdroid_llm/session.py` — `AutomationSession`, `ConversationTurn`
- `gifdroid_llm/automation.py` — `run_blind_loop` orchestration function
- `gifdroid_llm/providers.py` — added `ExecutableAction`, `ActionDecision` dataclasses; `GeminiProvider.decide_next_action()` and `_parse_action_decision()` methods
- `gifdroid_llm/device.py` — added `execute_action()` method
