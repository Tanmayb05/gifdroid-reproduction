# Milestone 6 — Replay Script Generation

**Date**: 2026-04-10
**Status**: CLEARED

## V6.1 — `replay.py` written to run output dir

**Test**: Generated `replay.py` from `apps/adaway/llm/gemini/gemini-2.5-pro/screenrec/run-001/session_trace.json`.

**Result**: Pass

```
Written: apps/adaway/llm/gemini/gemini-2.5-pro/screenrec/run-001/replay.py
Syntax OK  (py_compile passed)
```

The file exists, passes syntax check, and contains:
- Header docstring with package, video path, task summary, timestamp
- `APK_PATH`, `PACKAGE`, `ACTIVITY` constants
- `ACTIONS` list (10 steps, Python dict literals with `None` for nulls)
- `_execute(d, action)` dispatcher for tap/scroll/type_text/press_back/press_home
- `main()` with `--serial`, `--delay`, `--skip-install` args

## V6.2 — Replay executes on connected device

**Test**: `python replay.py --skip-install --delay 1.2` against `emulator-5554`.

**Result**: Pass (with expected caveat)

```
Connected to device: sdk_gphone64_arm64
Running 10 action(s)...
  Step 1: tap → the menu icon in the bottom-left corner
  Step 2: tap → the 'Allowed' card with the number 2
  Step 3: tap → the red plus button
  Step 4: type_text → the text input field with the current text 'The hosts source URL'
  Step 5: tap → the ADD button
  Step 6: type_text → [element not found — dialog was already closed by step 5]
```

Steps 1–5 executed successfully (the actual task — navigate to allowed list, add dialog, type hostname, confirm). Steps 6–10 are redundant loop steps from the LLM getting stuck in the original run; step 6 correctly errors because the dialog element is no longer present. This is expected: the replay faithfully re-executes the recorded trace, including the LLM's repetition loop.

The replay mechanism itself works correctly. The device connection, action dispatch, and error reporting all function as designed.

## New Files

| File | Description |
|------|-------------|
| `gifdroid_llm/replay_writer.py` | `write_replay_script()` — renders `replay.py` from a session trace |
| `gifdroid_llm/automate.py` | Edited — calls `write_replay_script()` after each run |
| `apps/adaway/llm/gemini/gemini-2.5-pro/screenrec/run-001/replay.py` | Generated replay script (adaway example) |
