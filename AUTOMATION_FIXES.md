# Device Automation Fixes — May 6, 2026

## Summary
Fixed three critical issues in the automation loop that were causing the recipe creation task to loop 10 times, fail, and require manual recovery. All fixes applied to `src_llm/automation.py` and `src_llm/device.py`.

**Result: Task now completes in 5 steps (52s) vs. 10 steps (2m 24s), with full state verification and success detection.**

---

## Issues Identified

### 1. **Text Input Not Persisting**
**Problem:** After `type_text` action executed, the field remained empty. The accessibility tree showed no text despite the action completing.

**Root Cause:** `type_text` called `send_keys(text)` without first **focusing/tapping the input field**. Without focus, the text was sent but not captured by the field.

**Fix (device.py:143-158):** 
- Before typing, tap the field to ensure focus using either `resource_id` or `coordinates`
- Added logging to confirm field focus before text entry

**Verification:** Post-action screenshot captured and a11y tree checked for text presence. Field assertions now tracked in trace.

---

### 2. **No State Verification After Actions**
**Problem:** History context only tracked decisions, not what actually happened on the device. LLM couldn't see if text persisted.

**Fix (automation.py:265-398):**
- After each `type_text` action, capture a post-action screenshot and a11y tree
- Check if the intended text appears in the accessibility tree
- Log success/failure with details: `field_verified: bool`, `problem: string` (if failed)
- Store field state assertions in trace for debugging

**Example Log Output:**
```
[INFO] Step 2: Field state verified — text 'cake' found in a11y tree
[WARNING] Step X: Field state FAILED — text 'xyz' NOT found in a11y tree
```

---

### 3. **No Save Success Detection**
**Problem:** After tapping "Save Recipe", automation continued looping. It didn't detect successful save vs. validation error.

**Fix (automation.py:365-398):**
- After "Save" tap, wait briefly and capture post-action screenshot/a11y tree
- Check if main screen appeared (recipe list visible) and no error message visible
- If save successful: set `status = "completed"` and break loop immediately
- If validation error visible: log problem with `save_successful: false`

**Example Log Output:**
```
[INFO] Step 5: Save appears successful — recipe list visible on main screen
[WARNING] Step X: Save FAILED — validation error still visible
```

---

### 4. **Prior Run Lookup Including In-Progress Runs**
**Problem:** `_locate_latest_run()` returned newly created run directories (e.g., run-003) before they had metadata.json, causing FileNotFoundError.

**Fix (automate.py:48-72):**
- Filter glob results to only include runs with completed `metadata.json`
- This ensures only finished Stage 1 runs are considered "latest"

**Before:** `existing = sorted(base.glob("run-*"), ...)`  
**After:** `existing = [p for p in base.glob("run-*") if (p / "metadata.json").exists()]`

---

## Code Changes

### src_llm/device.py (execute_action method)
```python
elif action_type == "type_text":
    if action.text:
        # Ensure the field is focused by tapping it first
        if action.resource_id:
            el = self._device(resourceId=action.resource_id)
            if el.exists:
                logger.info("Tapping field before typing (focus): resource_id=%s", action.resource_id)
                el.click()
        elif action.coordinates:
            logger.info("Tapping field before typing (focus): coordinates=%s", action.coordinates)
            self.tap(action.coordinates[0], action.coordinates[1])

        logger.info("Typing text: %s", action.text[:50])
        self.type_text(action.text)
```

### src_llm/automation.py (post-action verification)
- Added `field_state_assertions: list[dict]` to track all text input verifications
- Post-action check: capture screenshot + a11y tree, verify text in tree
- Success check: after "Save" tap, look for main screen + absence of error
- Updated trace to include `field_state_assertions` for audit trail

### src_llm/automate.py (prior run lookup)
- Filter for completed runs: `if (p / "metadata.json").exists()`
- Prevents finding in-progress or empty run directories

---

## Results

| Metric | Before | After |
|--------|--------|-------|
| **Total Steps** | 10 (max_steps limit hit) | 5 (completed early) |
| **Wall Time** | 2m 24s | 52s |
| **LLM Calls** | 10 | 5 |
| **LLM Tokens** | 33,571 | 16,466 |
| **Status** | max_steps_reached | completed |
| **Field Verification** | None | 3/3 text inputs verified ✓ |
| **Save Detection** | None | Detected success on step 5 ✓ |

---

## Testing

Ran full automation on `bakerspercentagecalculator` app with screenrec video:
- ✓ Stage 1 (memory generation) completed successfully
- ✓ Stage 2 (device automation) completed in 5 steps
- ✓ All field inputs verified present in accessibility tree
- ✓ Recipe successfully created and persisted on main screen
- ✓ No looping or validation errors

**Test Output:**
```
[INFO] Run complete: app=bakerspercentagecalculator video_type=screenrec steps=5 status=completed
[INFO] Wall time: 0m 52s
```

---

## Next Steps

1. Test on other apps to ensure fixes generalize
2. Consider: should field verification fail cause a retry with different approach?
3. Monitor token usage — field verification adds post-action captures but saves tokens by completing early
