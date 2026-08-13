# Issues: amazefilemanager hhv-002 run-001

## Video vs memory.md gaps

Video (29.03s, frames checked at ~1/4/7/13/21/29s): file browser at `/storage/emulated/0` (23 folders) → drawer opens → "FTP Server" nav item tapped → FTP Server screen, "Not Running" → START tapped → status becomes "Secure Connection", URL shown, system notification appears → home screen with notification visible ("Amaze FTP Server running... STOP") → notification-shade interactions → recents → back to Amaze FTP Server screen, "Secure Connection" still shown near end of clip.

memory.md's 9-step narrative tracks the video's beats reasonably well from spot-checks (drawer open, FTP nav, server start, home-screen notification, FTP screen state at the end). No major fabrication found in Stage 1 for this run — the video itself is a clean, linear flow and the model appears to have stayed grounded to it.

## memory.md vs device-automation gap

Automation stalled at step 4/9 (`Run complete: app=amazefilemanager ... steps=4 status=done`, self-terminated after 3 identical failed taps). automate.log shows the LLM repeatedly tapped coordinates `[84,158]` for the "hamburger menu icon" 3 times, then gave up:

> Step 1 reasoning: "Although this icon is not visible on the current screen, its standard location is in the top-left corner..." (confidence 0.80 — tapping a guessed/assumed location, not one grounded in the actual screenshot)
> Step 4 reasoning: "I have attempted to tap the same coordinates three consecutive times... indicating that I am stuck."

**Root cause, confirmed by inspecting `step_001.png`:** the automation did **not** start from the screen memory.md's Stage 1 narrative describes. Instead of the video's starting point (`/storage/emulated/0` root, 23 folders — see video f_001), `step_001.png` shows an **entirely different, leftover screen**: the empty `Amaze2595` subdirectory ("0 folders and 0 files") — which is actually the ending/working directory from the **hhv-001 run** (create-duplicate-file task) on this same app.

This is a **device-state contamination bug**, not a vision/reasoning failure. The pipeline is invoked with `--skip-apk-install`, which explicitly starts automation "from the current device screen" rather than resetting/relaunching the app (confirmed in automate.log: `Skipping APK install and launch; starting automation from current device screen`). Because the previous hhv-001 automation run left the Amaze app open inside the `Amaze2595` subdirectory, hhv-002's automation inherited that stale state instead of the fresh root-directory view the video and memory.md assume as the starting point. The LLM then correctly could not find a hamburger menu (the `Amaze2595` empty-folder screen may not render one identically, or it's positioned differently than at the root view) and, after guessing coordinates based on memory.md's description rather than the actual screen, correctly detected it was stuck and stopped.

**This is the same class of issue as k9 hhv-002's run** in the sense that the automation never got a fair run against the scenario memory.md describes — but the underlying mechanism here is cross-run device-state leakage via `--skip-apk-install`, not a stall-detector code bug or coordinate-scale mismatch.

**Suggested fix:** when chaining multiple automation runs against the same device with `--skip-apk-install`, either (a) explicitly navigate/reset the target app to a known starting state (e.g. app home / root directory) before each run rather than assuming a fresh launch state, or (b) do not reuse `--skip-apk-install` across different video/task runs unless the prior run's ending state is verified to match the next run's expected starting state.
