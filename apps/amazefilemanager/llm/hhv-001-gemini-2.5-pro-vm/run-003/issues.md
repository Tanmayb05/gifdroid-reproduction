# Issues: amazefilemanager hhv-001 run-003

## Video vs memory.md gaps

Video (35.57s, frames checked at memory.md's claimed timestamps 1/2/9/17/19/32/33s): empty `Amaze2595` directory → FAB tap → "New File" dialog (pre-filled ".txt") → text entry "demo.txt" → CREATE → file appears in list → FAB tap again → "New File" dialog again → text entry "demo.txt" again → CREATE again → **second file named "demo.txt" visibly appears in the file list** (f_036, ~36s: list shows two distinct "demo.txt" rows with different timestamps, header reads "0 folders and 2 files").

memory.md's 9-step narrative is **accurate and video-grounded** — the claimed bug (app silently allows creating two files with the identical name) is directly confirmed on screen, not a hallucination. No gaps found between video and memory.md for this run.

## memory.md vs device-automation gap

Automation completed all 9 steps (`Run complete: app=amazefilemanager ... steps=9 status=done`), but **the on-device outcome at step 9 diverges from what the video showed**.

`step_009.png` shows: a "New File" dialog with the **name field reset to bare ".txt"** (not "demo.txt" as step 8 was supposed to have entered), a warning "The created file will be hidden in the file list," and — critically — a toast at the bottom reading **"File with same name already exists."**

This is a real behavioral divergence, not a misread by the LLM:
- The video (Stage 1 source) shows the app **silently permitting** a duplicate filename with no warning.
- The live device automation (Stage 2) shows the app **correctly rejecting** the duplicate with an explicit "File with same name already exists" toast, and the input field did not retain "demo.txt" as typed — it reverted to ".txt" before the CREATE tap fired.

Two plausible root causes, not distinguishable from the artifacts alone:
1. **Non-deterministic bug**: the duplicate-name bug is a race condition or state-dependent quirk in the app (e.g. depends on whether the file list had already refreshed/indexed the first `demo.txt` by the time CREATE is tapped a second time) — the human-recorded video happened to hit the buggy silent-success path, while the slower/differently-timed automation run hit the app's normal validation path instead.
2. **Text-entry timing bug in the automation itself**: step 8's `type_text` action for "demo.txt" may not have fully landed before the automation captured its result screenshot or fired the CREATE tap in step 9, leaving the field at "demo.txt" only partially/differently entered by the time CREATE actually executed — explaining why the field shows ".txt" in step_009.png rather than "demo.txt".

Either way, this means **the on-device reproduction did not confirm the claimed bug** — it actually demonstrated the app's guard rail working as expected, which is the opposite of what the video/memory.md concluded. Any downstream bug report based on this run should note that reproduction on live device is not confirmed and may depend on timing.
