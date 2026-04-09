# Milestone 4 — Video Context Integration

**Date**: 2026-04-09
**Gate status**: CLEARED

## Verification Results

### V4.1 — Keyframes extracted and sent to LLM for task understanding

**Pass**

- `VideoFrameExtractor` extracted 46 sampled frames from `apps/adaway/videos/screenrec/srv-001.mp4`
- `KeyframeSelector` (SSIM method) selected 8 keyframes
- `GeminiProvider.summarize_video_task(keyframes)` returned a non-empty task summary:

> "The user opens the AdAway application and navigates to the 'Allowed' list for managing whitelisted hosts. After a new host, 'utl.web,' is added to the list, the user immediately unchecks it, disabling it from the whitelist. Finally, the user briefly taps on the 'Redirected' tab before returning to the 'Allowed' list."

- Elapsed time: 21.71s
- No API error

---

### V4.2 — Full end-to-end automation run: video → device → session trace

**Pass**

Command:
```
.venv/bin/python -m gifdroid_llm.automate \
  --video apps/adaway/videos/screenrec/srv-001.mp4 \
  --apk apps/adaway/apk/adaway.apk \
  --config gifdroid_llm/input/automation_config.yml \
  --env-file .env.local \
  --task "Open AdAway, navigate to the custom lists (Allowed tab), add and then cancel an entry, toggle the utl.web entry, and briefly view the Redirected tab." \
  --output-dir artifacts/milestone4/run-001
```

Output:
```
[INFO] APK installed: org.adaway
[INFO] App launched: org.adaway/.ui.home.HomeActivity
[INFO] Keyframes selected: 8
[INFO] Task summary: The user opens the AdAway application and navigates to the "Allowed" list...
[INFO] Step 1/10: tap coordinates=[73, 1783]
[INFO] Step 2/10: tap org.adaway:id/allowedHostCardView
[INFO] Step 3/10: tap org.adaway:id/lists_add
[INFO] Step 4/10: tap android:id/button2 (CANCEL)
[INFO] Step 5/10: tap org.adaway:id/checkbox_list_checkbox
[INFO] Step 6/10: tap org.adaway:id/lists_navigation_redirected
[INFO] Step 7/10: tap org.adaway:id/lists_navigation_allowed
[INFO] Step 8/10: continue=False — done
[INFO] Automation loop complete at step 8
[INFO] Session complete: 8 steps, status=done
```

Artifacts:
- `run-001/session_trace.json` — full machine-readable session trace
- `run-001/steps/step_001.png` … `step_008.png` — screenshots at each step

Session trace: `status=done`, 8 steps, keyframes_used=8.

---

### V4.3 — Existing passive trace pipeline is unaffected

**Pass**

```
.venv/bin/python -m gifdroid_llm.main --config gifdroid_llm/input/config.yml --env-file .env.local --dry-run
```

Exits 0 across all 20 configured runs. Dry-run OK.

Also:
```
.venv/bin/python -m gifdroid_llm.automate --config gifdroid_llm/input/automation_config.yml --env-file .env.local --dry-run
```
Exits 0: Dry-run OK.

---

## New Files

- `gifdroid_llm/automate.py` — CLI entry point (`python -m gifdroid_llm.automate`)
- `gifdroid_llm/automation.py` — extended with `run_automation(video_path, ...)` for video-guided loop
- `gifdroid_llm/providers.py` — added `GeminiProvider.summarize_video_task()` and `decide_next_action_with_video_context()`
- `gifdroid_llm/config.py` — added `AutomationConfig` dataclass and `load_automation_config()`
- `gifdroid_llm/input/automation_config.yml` — automation config template

## Artifacts

- `artifacts/milestone4/run-001/session_trace.json`
- `artifacts/milestone4/run-001/steps/step_001.png` … `step_008.png`
