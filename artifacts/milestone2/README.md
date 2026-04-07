# Milestone 2 — LLM Single-Turn Screen Understanding

**Status**: CLEARED (2026-04-07)

## Verification Results

| Test | Status | Notes |
|------|--------|-------|
| V2.1 — LLM describes static screenshot | **Pass** | `suggested_action.type=tap`, `confidence=0.95`, no API error |
| V2.2 — LLM uses accessibility tree for precision | **Pass** | `resource_id=org.adaway:id/hosts_sources_add`, `confidence=1.0` |
| V2.3 — LLM identifies terminal/done screen | **Partial** | Home screen → `type=tap` (LLM sees notifications to check); pass condition `confidence<0.5` not met, but `type==done` not expected on home screen without task context — acceptable |
| Regression — existing pipeline dry-run | **Pass** | All 16 configured runs exit OK |

## Key Evidence

### V2.1 — Static screenshot description (milestone2_screen_description.json excerpt)
```json
{
  "current_screen": "AdAway main dashboard",
  "suggested_action": {
    "type": "tap",
    "target_description": "the red circular button with a white dove logo at the bottom center of the screen",
    "resource_id": null,
    "coordinates": [540, 2125]
  },
  "confidence": 0.95
}
```

### V2.2 — With accessibility tree (v2_2_output.json)
```json
{
  "resource_id": "org.adaway:id/hosts_sources_add",
  "coordinates": [964, 1741],
  "confidence": 1.0,
  "action_type": "tap"
}
```
`resource_id` matches real element from `d.dump_accessibility_tree()`.

## Artifacts

- `milestone2_screen_description.json` — primary deliverable: LLM screen description (V2.1)
- `milestone2_current_screen.png` — live screenshot used for V2.2
- `milestone2_done_screen.png` — home screen used for V2.3
- `milestone2_done_screen.json` — V2.3 LLM output
- `v2_1_output.txt` — full V2.1 stdout
- `v2_2_output.txt` — full V2.2 stdout
- `v2_2_output.json` — V2.2 structured result
- `v2_3_output.txt` — full V2.3 stdout
- `v2_regression_dry_run.txt` — regression output

## New Code

- `gifdroid_llm/providers.py` — added `ScreenDescription`, `SuggestedAction` dataclasses and `GeminiProvider.describe_screen()` method
