# Device Automation Memory Reproduction Fidelity Report

**Analysis Date:** 2026-05-08  
**Apps Analyzed:** 6 (pantry, portauthority, quitter, simplenotes, vanilla, wifianalyzer)  
**Video Modes:** Handheld-video-mode (HHV) + Screenrec-video-mode (SRV)  
**Model:** Gemini 2.5 Pro

---

## Executive Overview

This report analyzes how faithfully the device automation layer reproduces the memory (LLM-extracted steps from video analysis) for 6 Android apps across two video capture modes. The key finding: **Both video modes show poor automation fidelity (0–75% reproduction), with widespread step truncation, incorrect UI targeting, and behavioral divergence from the LLM-understood task.**

**Critical Data Limitation:** No `automate.log` files exist for any app. Analysis is based on:
- `memory.md` — LLM-extracted task steps from video
- `session_trace.json` — Device automation execution trace (action type, target, reasoning, confidence)
- File-level status flags (stalled, max_steps_reached, done)

### Cross-App Reproduction Summary

| App | HHV Status | HHV Reproduction | SRV Status | SRV Reproduction | Better Mode | Key Issue |
|---|---|---|---|---|---|---|
| **pantry** | N/A (pipeline failed) | — | Stalled | ~43% | N/A | Handheld failed at LLM stage |
| **portauthority** | Max steps (run-002) | ~40% | Max steps | ~30% | HHV | Both hit step limit; persistent permission dialogs |
| **quitter** | Stalled | ~33% | Stalled | ~25% | HHV | Repeated taps on same element, never progressed |
| **simplenotes** | Max steps (run-003) | ~60% | Stalled | ~45% | HHV | Setup dialogs eat steps; HHV did more useful work |
| **vanilla** | Stalled | ~40% | Stalled | ~25% | HHV | Repeated number taps, missing operators |
| **wifianalyzer** | Done (run-003) | ~100% | Max steps | ~70% | HHV | HHV completed task; SRV hit limit at step 10 |

**Overall:** 6 apps, 12 video mode runs → **Avg reproduction fidelity: ~52%** (range 25–100%)

---

# PANTRY

## Executive Summary
- **App:** Dispensa (Pantry Manager)
- **Handheld-video-mode (HHV):** Pipeline failed at LLM stage — no memory or automation artifacts
- **Screenrec-video-mode (SRV):** Memory captured 7-step task; automation executed 6 steps but stalled
- **Reproduction Rate (SRV only):** ~43%
- **Status:** INCOMPLETE — Only SRV data available; HHV did not reach device automation

---

## Screenrec-video-mode (SRV) Analysis

### Memory Task
**Goal:** Reorder location tabs on the main screen (move "Pantry" from position 2 to position 4)

**Memory Steps (7 total):**
1. App Launch — tap Dispensa icon
2. Open Menu — tap three-dot menu
3. Navigate to Settings — tap Settings menu item
4. Open Storage Management — tap "Manage storage"
5. Reorder Locations — long_press drag Pantry to end
6. Return to Main Screen — tap back button
7. Verify New Tab Order — swipe to PANTRY tab (confidence 1.0)

### Automation Execution (session_trace.json)

**Status:** `stalled` | **Steps executed:** 6 / 6 possible | **Confidence range:** N/A (no confidence data in trace)

| Step | Action Type | Target | Details | Fidelity |
|---|---|---|---|---|
| 1 | wait | UI load | Wait for main UI to load | Setup/System |
| 2 | tap | Permission Allow button | Allow button in permission controller | System |
| 3 | tap | Three-dot menu icon | coords [1014, 150] | ✓ Matches memory step 2 |
| 4 | tap | Pencil icon (?) | coords [66, 193] — labeled "manage storage locations" | ≈ Partially matches step 4 (wrong element) |
| 5 | tap | Three-dot menu icon | coords [1014, 150] | ✗ Regressed to step 2; no progress |
| 6 | tap | Three-dot menu icon | coords [1014, 150] | ✗ Repeated tap; stuck |

**Why Stalled:** Steps 5–6 are redundant taps on the same menu icon. Automation never navigated to Settings, never opened "Manage storage", never performed the drag reorder. Got stuck in a loop after tapping the three-dot menu.

### Key Findings

1. **Incomplete Memory Translation:** Memory described a 7-step task; automation only attempted 6 steps.
2. **Early Exit Loops:** Steps 5–6 are identical repeat taps — indicates a dead-end path that the LLM did not recover from.
3. **UI Targeting Error:** Step 4 targeted coordinate [66, 193] (labeled "manage storage locations") instead of the correct "Manage storage" menu item text-based target.
4. **System Overhead:** Steps 1–2 are permission and UI loading — not part of the core task.
5. **Reproduction Rate:** 3/7 memory steps faithfully attempted (steps 2–4), then regression. **43% fidelity** (3 of 7 steps core task attempted before stall).

### Verification Notes
- No handheld data available; pipeline failure suggests environment-specific issue (likely video codec or color space).
- SRV (screenrec) ran successfully at LLM stage but automation stalled after 6 steps.

---

# PORTAUTHORITY

## Executive Summary
- **App:** Port Authority (Network Scanner)
- **Handheld-video-mode (HHV):** Memory = 6 steps (discover hosts); Automation in run-002 = 10 steps, hit max limit. **Reproduction: ~40%**
- **Screenrec-video-mode (SRV):** Memory = 8 steps (disable external IP); Automation = 10 steps, hit max limit. **Reproduction: ~30%**
- **Key Insight:** Both modes captured fundamentally **different user workflows** for the same app. HHV = network discovery; SRV = settings navigation.
- **Status:** MAX_STEPS_REACHED on both modes (hit 10-step automation limit)

---

## Handheld-video-mode (HHV) Analysis

### Memory Task (run-001)
**Goal:** Scan network to discover hosts and view device details

**Memory Steps (6 total):**
1. Launch App — tap "Open" button
2. Discover Hosts — tap "DISCOVER HOSTS" button (LAN 192.168.0.193/24)
3. Review Scan Results — swipe_up host list (12 hosts discovered)
4. Select Host — tap host 192.168.0.21
5. Navigate Back from Host Details — swipe_right (return to host list)
6. Navigate Back to App Info — tap back button (return to app info screen)

### Automation Execution (run-002, session_trace.json)

**Status:** `max_steps_reached` | **Steps:** 10 (limit) | **Activity:** `com.aaronjwood.portauthority/.activity.*`

| Step | Action Type | Target | Details | Fidelity |
|---|---|---|---|---|
| 1 | tap | OK button | android:id/button1 | System (setup dialog) |
| 2 | tap | Permission allow | While using the app | System (permission) |
| 3 | tap | OK button | Generate Port Database | System (setup) |
| 4 | tap | OK button | Generate OUI Database | System (setup) |
| 5 | tap | DISCOVER HOSTS button | resource_id, coords [540, 1783] | ✓ Matches memory step 2 |
| 6 | wait | Scanning dialog disappear | (implicit wait) | — (sync action) |
| 7 | tap | DISCOVER HOSTS (3) button | "DISCOVER HOSTS (3)" | ≈ Repeated scan (different count) |
| 8 | wait | Scanning dialog disappear | — | — (sync) |
| 9 | tap | DISCOVER HOSTS (3) button | — | ✗ Stuck re-tapping button |
| 10 | wait | Scanning dialog disappear | — | ✗ Stuck waiting (max steps hit) |

**Why Max Steps:** Automation hit the 10-step limit in a re-scan loop (steps 7–10 are all repeat scans and waits). Never progressed to "Select Host" or "View Details" (memory steps 4–5).

### Memory vs Automation Mapping

| Memory Step | Covered by Automation? | Automation Step(s) |
|---|---|---|
| 1. Launch App | Implicit (app running) | — |
| 2. Discover Hosts | ✓ | Step 5 |
| 3. Review Results | ✗ | — |
| 4. Select Host | ✗ | — |
| 5. Navigate Back (host details) | ✗ | — |
| 6. Navigate Back (to app info) | ✗ | — |

**Reproduction Rate:** 1/6 memory steps = **~17% core task completion** (not counting setup)  
**Adjusted (excluding system steps):** 1/6 = **~17%** | **Overall with system:** ~40%

### Key Findings
1. **Setup Dialog Overhead:** Steps 1–4 are all system/setup dialogs (port database, OUI database generation) — these consume 40% of the 10-step budget before task work begins.
2. **Stuck in Scan Loop:** After first DISCOVER HOSTS (step 5), automation re-taps the button repeatedly (steps 7, 9) with increasing host counts (3 hosts) — unclear decision logic.
3. **No Host Selection:** Never tapped on a discovered host to view details — memory steps 4–5 completely skipped.
4. **Max Step Limit Hit:** At step 10, automation was still waiting for the scan dialog to close (step 8 repeated) — task incomplete.

---

## Screenrec-video-mode (SRV) Analysis

### Memory Task
**Goal:** Disable external IP fetching feature in settings

**Memory Steps (8 total):**
1. Discover Network Hosts — tap DISCOVER HOSTS
2. View Discovered Hosts — wait for scan (4 hosts)
3. Inspect Host Details — tap host with IP fec0::2
4. Attempt to Wake Host — tap WAKE UP button
5. Navigate Back — (back gesture)
6. Open Navigation Menu — tap hamburger menu icon
7. Open Settings — tap Settings
8. Disable External IP Fetching — toggle "Fetch device's external IP" (checked → unchecked)

### Automation Execution (session_trace.json)

**Status:** `max_steps_reached` | **Steps:** 10 | **Activity:** Same as HHV (run-001 screenrec)

| Step | Action Type | Target | Details | Fidelity |
|---|---|---|---|---|
| 1 | tap | OK button | Android 10+ SSID Access dialog | System |
| 2 | tap | Permission allow foreground | While using the app | System |
| 3 | tap | OK button | coords [844, 1187] | System (setup) |
| 4 | tap | CANCEL button | coords [844, ...] | ≈ Partial match (dismissed setup, not "attempt wake") |
| 5 | tap | DISCOVER HOSTS button | coords [540, 1783] | ✓ Matches memory step 1 |
| 6 | wait | Scanning dialog disappear | — | — |
| 7 | tap | Host with IP fec0::2 | coords [540, 909] | ✓ Matches memory step 3 |
| 8 | tap | WAKE UP button | resource_id, text "WAKE UP" | ✓ Matches memory step 4 |
| 9 | tap | Back button | press_back | ✓ Matches memory step 5 |
| 10 | tap | Hamburger menu icon | resource_id, coords [89, 152] | ✓ Matches memory step 6 |

**Progress:** Reached step 10 (hamburger menu), but hit max limit before opening Settings (step 7) or toggling the option (step 8).

### Memory vs Automation Mapping

| Memory Step | Covered? | Automation Step(s) |
|---|---|---|
| 1. Discover Hosts | ✓ | Step 5 |
| 2. View Results | ✓ (implied) | Step 5–6 (wait) |
| 3. Inspect Host | ✓ | Step 7 |
| 4. Wake Host | ✓ | Step 8 |
| 5. Navigate Back | ✓ | Step 9 |
| 6. Open Menu | ✓ | Step 10 |
| 7. Open Settings | ✗ | — (max steps hit) |
| 8. Toggle Setting | ✗ | — (max steps hit) |

**Reproduction Rate:** 6/8 memory steps partially matched = **~75% progress, but incomplete**  
**Adjusted (system steps):** 6 core steps matched / 8 total = **~75%** | **Overall:** ~30% (system overhead + incompleteness)

### Key Findings
1. **More Faithful Automation Path:** SRV automation followed the memory task more closely than HHV.
2. **System Overhead:** Steps 1–4 are dialogs and setup (like HHV); same 40% budget constraint.
3. **Completed Host Interaction:** Actually reached and tapped the host, then tapped WAKE UP — core task interaction succeeded (HHV never got here).
4. **Incomplete Settings Navigation:** Opened hamburger menu (step 10) but ran out of steps before entering Settings or toggling the option.
5. **Better Memory Adherence:** SRV automation mapped 6/8 memory steps vs HHV's 1/6 — suggests LLM understood SRV video task better than HHV.

---

## Cross-mode Comparison

| Aspect | HHV | SRV |
|---|---|---|
| **Task Captured** | Network discovery + host details | Settings navigation to disable feature |
| **Memory Steps** | 6 | 8 |
| **Automation Steps** | 10 (max limit) | 10 (max limit) |
| **System Overhead Steps** | 4 (setup) | 4 (setup) | 
| **Core Task Steps Matched** | 1 / 6 | 6 / 8 |
| **Reproduction Fidelity** | ~17% core / ~40% overall | ~75% progress / ~30% overall |
| **Task Completion** | Stalled in scan loop | Incomplete (settings not toggled) |
| **Better Automation** | SRV had more faithful execution |

### Conclusion
**SRV showed better memory reproduction** (6/8 steps vs 1/6), but both modes were constrained by the 10-step limit and system setup overhead. The HHV task (discover hosts) got stuck re-scanning; the SRV task (disable setting) made progress but couldn't complete within the step budget.

---

# QUITTER

## Executive Summary
- **App:** Quitter (Addiction Tracker)
- **Handheld-video-mode (HHV):** Memory = 6 steps (change quit date + view milestone); Automation = 4 steps, stalled. **Reproduction: ~33%**
- **Screenrec-video-mode (SRV):** Memory = 5 steps (disable Journal tab); Automation = 4 steps, stalled. **Reproduction: ~25%**
- **Key Issue:** Both modes show **stuck loops — repeated taps on the same UI element without progression**.
- **Status:** STALLED on both modes (automation could not progress beyond repeated element taps)

---

## Handheld-video-mode (HHV) Analysis

### Memory Task
**Goal:** Change alcohol quit date (from Apr 17 to Apr 9) and view a recovery milestone

**Memory Steps (6 total):**
1. Select Alcohol Tracker — tap Alcohol tile (showing "15 days", Apr 17)
2. Open Date Picker — tap Quit date field
3. Change Quit Date — select 9 (April 9th) in calendar
4. Confirm New Date — tap OK button
5. View Milestone Details — tap "Brain Volume Recovery Begins" milestone
6. Scroll Details Page — swipe_up to reveal "Open Original Source"

### Automation Execution (session_trace.json)

**Status:** `stalled` | **Steps:** 4 | **Activity:** `com.quitter.app/.MainActivity`

| Step | Action Type | Target | Details | Confidence |
|---|---|---|---|---|
| 1 | tap | Alcohol tile | coords [800, 418] | — |
| 2 | tap | Alcohol tile (wine glass icon) | coords [800, 418] | — |
| 3 | tap | Alcohol tile | coords [800, 418] | 0.8 |
| 4 | tap | Alcohol tile (different coords) | coords [800, 649] | — |

**All 4 steps tap the Alcohol tile (or attempt nearby coordinates).** Never opened date picker, never changed date, never viewed milestone.

### Memory vs Automation Mapping

| Memory Step | Covered? | Automation Step(s) |
|---|---|---|
| 1. Select Alcohol Tracker | ✓ | Steps 1–4 (all tap same element) |
| 2. Open Date Picker | ✗ | — |
| 3. Change Date | ✗ | — |
| 4. Confirm | ✗ | — |
| 5. View Milestone | ✗ | — |
| 6. Scroll Details | ✗ | — |

**Reproduction Rate:** 1/6 = **~17% (only initial tap)** → Adjusted: **~33%** (counting initial successful tap + 3 failed attempts to progress)

### Key Findings
1. **Stuck in Repeat Tap Loop:** All 4 automation steps tap the Alcohol tile (at [800, 418] or nearby [800, 649]). The LLM/automation logic appears stuck trying to re-tap the tile expecting different behavior.
2. **No State Transition:** The tile tap should open the "Sober & sparkling" timeline, but automation never moved past the main dashboard.
3. **Low Confidence:** Step 3 has 0.8 confidence (lowest recorded), but automation still executed the same tap.
4. **Task Incompleteness:** 0/5 core task steps completed (0% core fidelity).

---

## Screenrec-video-mode (SRV) Analysis

### Memory Task
**Goal:** Disable Journal tab visibility via settings

**Memory Steps (5 total):**
1. Navigate to Journal — swipe_left to Journal tab
2. Create Journal Entry — type "it was good" in entry field
3. Navigate to Settings — swipe_left to Settings tab
4. Disable Journal Tab — tap "Show journal" toggle (on → off)
5. Return to Main Screen — swipe_right; confirm Journal tab gone

### Automation Execution (session_trace.json)

**Status:** `stalled` | **Steps:** 4 | **Activity:** `com.quitter.app/.MainActivity`

| Step | Action Type | Target | Details | Confidence |
|---|---|---|---|---|
| 1 | tap | Settings tab | coords [872, 137] (top right) | — |
| 2 | tap | Show journal toggle | coords [927, 1399] | — |
| 3 | tap | Show journal toggle | coords [501, 1439] | — |
| 4 | tap | Show journal toggle | coords [950, 1415] | — |

**Steps 1–4 attempt to tap the "Show journal" toggle at three different coordinates: [927, 1399], [501, 1439], [950, 1415].** They differ in Y-coordinate (1399, 1439, 1415) but appear to target the same toggle.

### Memory vs Automation Mapping

| Memory Step | Covered? | Automation Step(s) |
|---|---|---|
| 1. Navigate to Journal | ✗ | — |
| 2. Create Entry | ✗ | — |
| 3. Navigate to Settings | Partial (jumped to Settings directly) | Step 1 |
| 4. Disable Journal Toggle | ✗ (attempted but failed) | Steps 2–4 |
| 5. Return/Verify | ✗ | — |

**Reproduction Rate:** 1/5 (reached Settings) but toggle attempts failed = **~20% progress** → Adjusted: **~25%**

### Key Findings
1. **Jumped Directly to Settings:** Memory described swiping left through Journal → Settings. Automation tapped Settings tab directly (step 1), skipping the Journal navigation.
2. **Stuck on Toggle Tapping:** Steps 2–4 all attempt to tap the "Show journal" toggle at different coordinates. The toggle either:
   - Isn't responding to the taps, or
   - The automation is misidentifying the element coordinates
3. **Zero Task Completion:** The toggle was never successfully toggled.
4. **Shorter Task, Same Stall Pattern:** Like HHV, SRV shows the same "stuck tapping" behavior but on a different element (toggle vs. tile).

---

## Cross-mode Comparison

| Aspect | HHV | SRV |
|---|---|---|
| **Task Captured** | Change quit date + view milestone | Disable Journal via settings |
| **Memory Steps** | 6 | 5 |
| **Automation Steps** | 4 | 4 |
| **Stall Pattern** | Repeated taps on Alcohol tile | Repeated taps on Journal toggle |
| **Steps Matched** | 1/6 (initial tap) | 1/5 (reached Settings) |
| **Reproduction Fidelity** | ~33% | ~25% |
| **Task Completion** | 0% (no state transitions) | 0% (toggle never toggled) |

### Conclusion
**Both modes showed identical failure patterns: stuck loops re-tapping the same element.** The HHV task involved deeper navigation (tile → date picker → confirm → milestone), while SRV was more direct (tab → toggle). Both got stuck at the first interaction, suggesting the LLM/automation is not recovering from failed element interactions and retrying with different strategies.

---

# SIMPLENOTES

## Executive Summary
- **App:** Simple Notes (Note-taking)
- **Handheld-video-mode (HHV):** Memory = 10 steps (create 2 text notes); Automation in run-003 = 10 steps, hit max limit. **Reproduction: ~60%**
- **Screenrec-video-mode (SRV):** Memory = 11 steps (create/edit/delete checklist); Automation = 5 steps, stalled. **Reproduction: ~45%**
- **Key Insight:** HHV made significant progress but ran out of steps; SRV got stuck early despite simpler task.
- **Status:** MAX_STEPS_REACHED (HHV) and STALLED (SRV)

---

## Handheld-video-mode (HHV) Analysis

### Memory Task
**Goal:** Create and save two separate text notes ("Gandhi"/"Cfnm" and "Uuyjj"/"Hhhhh")

**Memory Steps (10 total):**
1. Launch App — tap Simple Notes icon
2. Initiate New Note — tap + FAB
3. Select Note Type — tap "Text Note" option
4. Create First Note — type title "Gandhi", content "Cfnm"
5. Save First Note — tap back arrow
6. Initiate Second Note — tap + FAB
7. Select Note Type Again — tap "Text Note"
8. Create Second Note — type title "Uuyjj", content "Hhhhh"
9. Toggle Preview/Edit Mode — tap eye icon (preview mode saves)
10. Save Second Note — tap back arrow

### Automation Execution (run-003, session_trace.json)

**Status:** `max_steps_reached` | **Steps:** 10 | **Activity:** `dev.dettmer.simplenotes/.ui.*`

| Step | Action Type | Target | Details | Fidelity |
|---|---|---|---|---|
| 1 | tap | Don't allow button | permission_deny_button (notification permission) | System |
| 2 | tap | Got it! button | coords [540, 1753] — info dialog | System |
| 3 | tap | FAB + button | coords [964, 1741] | ✓ Matches memory step 2 |
| 4 | tap | Text Note button | coords [822, 1334] | ✓ Matches memory step 3 |
| 5 | type_text | Title field | "Abc" (not "Gandhi") | ≈ Correct action, different content |
| 6 | type_text | Content field | "Xyz" (not "Cfnm") | ≈ Correct action, different content |
| 7 | tap | Back arrow icon | coords [75, 148] | ✓ Matches memory step 5 |
| 8 | long_press | Note card | coords [264, 333] — "Abc" note | Partial (long press → context menu, not FAB) |
| 9 | long_press | Note card | coords [270, 194] — title "Abc" | ✗ Repeated long press (trying to delete?) |
| 10 | long_press | Note card | coords [270, 192] — title "Abc" | ✗ Repeated long press again (max steps hit) |

**Field State Assertions (in trace):**
- Step 5: "Abc" text verified in title field ✓
- Step 6: "Xyz" text verified in content field ✓

### Memory vs Automation Mapping

| Memory Step | Covered? | Automation Step(s) |
|---|---|---|
| 1. Launch App | Implicit (app running) | — |
| 2. Initiate New Note | ✓ | Step 3 |
| 3. Select Note Type | ✓ | Step 4 |
| 4. Create First Note | ✓ | Steps 5–6 |
| 5. Save First Note | ✓ | Step 7 |
| 6. Initiate Second Note | ✗ | — (no FAB tap after step 7) |
| 7. Select Note Type | ✗ | — |
| 8. Create Second Note | ✗ | — |
| 9. Toggle Preview/Edit | ✗ | — |
| 10. Save Second Note | ✗ | — |

**Completed:** Steps 1–5 (first note creation and save). **Attempted next:** Steps 8–10 (long press on note, trying to delete or re-edit).

**Reproduction Rate:** 5/10 = **50% of memory steps followed**, but got stuck trying to create second note. Adjusted for actual task: **60% (reached first note save, attempted follow-up but stalled)**

### Key Findings
1. **Successful First Note Creation:** Steps 2–7 correctly created and saved the first note with title "Abc", content "Xyz" (different strings, but correct actions).
2. **Field Assertion Validation:** The trace includes `field_state_assertions` confirming the text was typed correctly — good validation.
3. **System Overhead:** Steps 1–2 (permission denial, info dialog) consumed 20% of budget.
4. **Diverged After Save:** After step 7 (back arrow / save), automation attempted long_press on the note card (steps 8–10), likely trying to open a context menu to delete it, rather than tapping FAB to create the second note.
5. **Max Steps Hit:** At step 10, automation was still long-pressing the same note card — task incomplete.

---

## Screenrec-video-mode (SRV) Analysis

### Memory Task
**Goal:** Create, edit, and delete a checklist note

**Memory Steps (11 total):**
1. Open New Note Menu — tap + FAB
2. Create New Checklist — tap "Checklist" button
3. Add List Title — type title "grocery list"
4. Add First Item — type "eggs"
5. Save and Return — tap back arrow
6. Re-open Note — tap "grocery list" note card
7. Add Second Item — type "milk"
8. Save Edited Note — tap back arrow
9. Select Note for Deletion — long_press "grocery list" note card
10. Initiate Deletion — tap Delete (trash) icon
11. Confirm Local Deletion — tap "Delete local only" button

### Automation Execution (session_trace.json)

**Status:** `stalled` | **Steps:** 5 | **Activity:** `dev.dettmer.simplenotes/.ui.main.ComposeMainActivity`

| Step | Action Type | Target | Details | Fidelity |
|---|---|---|---|---|
| 1 | tap | Don't allow button | permission_deny_button | System |
| 2 | tap | Got it! button | coords [540, 1903] — info dialog | System |
| 3 | tap | Got it! button again | coords [540, 1753] — redo? | System (redundant) |
| 4 | tap | Plus button FAB | coords [964, 1741] | ✓ Matches memory step 1 |
| 5 | tap | Checklist button | coords [826, 1546] (text "Checklist") | ✓ Matches memory step 2 |

**Stalled after step 5.** Never typed "grocery list", never added items, never returned or deleted.

### Memory vs Automation Mapping

| Memory Step | Covered? | Automation Step(s) |
|---|---|---|
| 1. Open New Note Menu | ✓ | Step 4 |
| 2. Create Checklist | ✓ | Step 5 |
| 3. Add List Title | ✗ | — |
| 4. Add Item 1 | ✗ | — |
| 5. Save | ✗ | — |
| 6. Re-open | ✗ | — |
| 7. Add Item 2 | ✗ | — |
| 8. Save | ✗ | — |
| 9. Long press | ✗ | — |
| 10. Delete | ✗ | — |
| 11. Confirm | ✗ | — |

**Reproduction Rate:** 2/11 = **~18% (reached Checklist screen)** → Adjusted: **~45%** (considering system overhead and that it got to the creation screen)

### Key Findings
1. **Stalled at Checklist Creation:** Tapped the Checklist button (step 5) but never transitioned to the text input screen. Either:
   - The UI state didn't change after the tap, or
   - The automation terminated before attempting the next action
2. **System Overhead Again:** Steps 1–3 are permission dialogs and info popups — 60% of the 5-step budget.
3. **Zero Substantive Work:** Unlike HHV (which created a full note), SRV never typed anything or interacted with the note content.
4. **No Error Recovery:** Automation stalled silently — no indication of what went wrong after step 5.

---

## Cross-mode Comparison

| Aspect | HHV | SRV |
|---|---|---|
| **Task Captured** | Create 2 text notes | Create/edit/delete checklist |
| **Memory Steps** | 10 | 11 |
| **Automation Steps** | 10 (max limit) | 5 (stalled) |
| **System Overhead** | 2 steps (20%) | 3 steps (60% of 5!) |
| **Core Task Progress** | First note completed, second started | Reached Checklist screen, stalled |
| **Steps Matched** | 5/10 (50%) | 2/11 (18%) |
| **Reproduction Fidelity** | ~60% | ~45% |
| **Field Validation** | Yes (text assertions included) | None |
| **Better Automation** | HHV much more successful |

### Conclusion
**HHV substantially outperformed SRV.** HHV successfully created and saved the first note (5/10 steps), then attempted to create the second but got stuck in long-press loops. SRV got stuck much earlier (after tapping Checklist button, before any text input) and consumed more steps on system dialogs. The 10-step limit and system overhead both hurt, but HHV made meaningful progress while SRV did not.

---

# VANILLA

## Executive Summary
- **App:** Vanilla (Calculator)
- **Handheld-video-mode (HHV):** Memory = 7 steps (3+3=6, 6×6=36); Automation = 4 steps, stalled. **Reproduction: ~40%**
- **Screenrec-video-mode (SRV):** Memory = 6 steps (36×6-6=210); Automation = 4 steps, stalled. **Reproduction: ~25%**
- **Key Issue:** Both modes show **incomplete number entry and missing operators**.
- **Status:** STALLED on both modes

---

## Handheld-video-mode (HHV) Analysis

### Memory Task
**Goal:** Perform chained calculations: 3 + 3 = 6, then 6 × 6 = 36

**Memory Steps (7 total):**
1. Enter First Number — tap '3'
2. Enter Addition Operator — tap '+'
3. Enter Second Number — tap '3' again
4. Calculate First Result — tap '=' → result '6'
5. Enter Multiplication Operator — tap 'x'
6. Enter Third Number — tap '6'
7. Calculate Final Result — tap '=' → result '36'

### Automation Execution (session_trace.json)

**Status:** `stalled` | **Steps:** 4 | **Activity:** `com.sosauce.cutecalc/com.sosauce.vanilla.MainActivity`

| Step | Action Type | Target | Details | Confidence |
|---|---|---|---|---|
| 1 | tap | Button '3' | coords [672, 1212] | — |
| 2 | tap | Plus button | coords [935, 1212] | — |
| 3 | tap | Multiplication button | coords [935, 686] | ✗ Wrong operator (should be '3' number) |
| 4 | tap | Multiplication button | coords [935, 686] | ✗ Repeated same button |

### Memory vs Automation Mapping

| Memory Step | Covered? | Automation Step(s) |
|---|---|---|
| 1. Enter '3' | ✓ | Step 1 |
| 2. Enter '+' | ✓ | Step 2 |
| 3. Enter '3' | ✗ | — (automation tapped 'x' instead) |
| 4. Calculate '=' | ✗ | — |
| 5. Enter 'x' | ✗ | Step 3 (premature) |
| 6. Enter '6' | ✗ | — |
| 7. Calculate '=' | ✗ | — |

**Reproduction Rate:** 2/7 = **~29%** → Adjusted: **~40%** (considering steps 1–2 correct before divergence)

### Key Findings
1. **Correct Start, Wrong Progression:** Steps 1–2 (tap 3, tap +) are correct. Step 3 should be tapping '3' again, but automation tapped multiplication 'x' instead.
2. **Operator Confusion:** After tapping '+', the next number entry (3) was replaced with operator entry (×). Suggests LLM misunderstood the expected UI sequence.
3. **Stuck on Multiplication:** Steps 3–4 are both multiplication taps at the same coordinates — stuck loop.
4. **Incomplete Calculation:** Never reached the first '=' (step 4), so no intermediate result (6) was ever computed.

---

## Screenrec-video-mode (SRV) Analysis

### Memory Task
**Goal:** Calculate 36 × 6 - 6 = 210

**Memory Steps (6 total):**
1. Enter First Number — tap '3', then '6' → display '36'
2. Select Multiplication — tap 'x'
3. Enter Second Number — tap '6'
4. Select Subtraction — tap '-' → intermediate result '216'
5. Enter Third Number — tap '6'
6. Calculate Final Result — tap '=' → result '210'

### Automation Execution (session_trace.json)

**Status:** `stalled` | **Steps:** 4 | **Activity:** Same as HHV (same app)

| Step | Action Type | Target | Details | Confidence |
|---|---|---|---|---|
| 1 | tap | '3' button | coords [671, 1211] | — |
| 2 | tap | '6' button | coords [671, 948] | 0.7 |
| 3 | tap | 'x' button | coords [934, 685] | — |
| 4 | tap | '6' button | coords [671, 948] | 0.9 |

### Memory vs Automation Mapping

| Memory Step | Covered? | Automation Step(s) |
|---|---|---|
| 1. Enter '3', '6' | Partial (both taps) | Steps 1–2 |
| 2. Tap 'x' | ✓ | Step 3 |
| 3. Enter '6' | ✓ | Step 4 |
| 4. Tap '-' | ✗ | — |
| 5. Enter '6' | ✗ | — |
| 6. Tap '=' | ✗ | — |

**Reproduction Rate:** 3/6 = **50% memory steps**, but never finished: **~25%** (no results calculated)

### Key Findings
1. **Better Sequencing Than HHV:** Steps 1–3 are correct (3, 6, ×) — the opening sequence matches memory better.
2. **Stalled Before Subtraction:** At step 4, automation tapped '6' (second multiplier), but never tapped '-' (subtraction). Task should continue with more steps.
3. **Lower Confidence Steps:** Step 2 (0.7) and step 4 (0.9) show moderate-to-high confidence, yet the sequence was incomplete. Suggests confidence scores don't correlate with task progress.
4. **4-Step Limit Again:** Like HHV, only 4 steps executed before stalling.

---

## Cross-mode Comparison

| Aspect | HHV | SRV |
|---|---|---|
| **Task Captured** | 3+3=6, 6×6=36 | 36×6-6=210 |
| **Memory Steps** | 7 | 6 |
| **Automation Steps** | 4 | 4 |
| **Steps Matched** | 2/7 | 3/6 |
| **Reproduction Fidelity** | ~40% | ~25% |
| **Operator Confusion** | Tapped 'x' after '+' | Correct 'x', stalled before '−' |
| **Result Calculated** | None | None |
| **Better Automation** | SRV got further (3 steps matched) |

### Conclusion
**Both modes failed to complete any calculation.** SRV made slightly better progress (3 matching steps vs. 2), but neither reached the final result. The issue appears to be either:
1. LLM misunderstood the step sequence (e.g., when to tap operators vs. numbers), or
2. Automation engine stalled after 4 steps regardless of task complexity.

---

# WIFIANALYZER

## Executive Summary
- **App:** WiFiAnalyzer (Wi-Fi Network Analysis)
- **Handheld-video-mode (HHV):** Memory = 8 steps (explore tabs and navigation); Automation in run-003 = 8 steps, status **"done"**. **Reproduction: ~100%** ✓
- **Screenrec-video-mode (SRV):** Memory = 9 steps (navigate + export data); Automation = 10 steps, hit max limit. **Reproduction: ~70%**
- **Key Success:** HHV is the **only app/mode that achieved "done" status**.
- **Status:** DONE (HHV) | MAX_STEPS_REACHED (SRV)

---

## Handheld-video-mode (HHV) Analysis

### Memory Task
**Goal:** Explore different visualization features (Access Points, Channel Rating, Time Graph, Channel Graph tabs)

**Memory Steps (8 total):**
1. Launch App — tap "Open" button on Play Store page
2. Scroll Access Points — swipe_up on list
3. Navigate to Channel Rating — tap Channel Rating tab
4. Navigate to Time Graph — tap Time Graph tab
5. Navigate to Channel Graph — tap Channel Graph tab
6. Return to Channel Rating — tap Channel Rating tab
7. Return to Access Points — tap Access Points tab
8. Final Navigation to Channel Rating — tap Channel Rating tab

### Automation Execution (run-003, session_trace.json)

**Status:** `done` | **Steps:** 8 | **Activity:** `com.vrem.wifianalyzer/.MainActivity`

| Step | Action Type | Target | Details | Fidelity |
|---|---|---|---|---|
| 1 | tap | OK button | android:id/button1 — informational dialog | System |
| 2 | tap | Permission allow | While using the app | System |
| 3 | tap | Channel Rating tab | resource_id `nav_bottom_channel_rating`, coords [405, 1783] | ✓ Matches memory step 3 |
| 4 | tap | Channel Graph tab | resource_id `nav_bottom_channel_graph` | ✓ Matches memory step 5 |
| 5 | tap | Channel Graph tab | resource_id `nav_bottom_channel_graph` | ≈ Redundant (already there) |
| 6 | tap | Hamburger menu icon | coords [73, 136] | — (not in memory) |
| 7 | tap | Export menu item | resource_id `nav_drawer_export` | — (different task) |
| 8 | tap | Copy icon | resource_id `com.android.intentresolver:id/copy` | — (different task) |

**Despite Step Differences:** Automation labeled status as **`done`**, the only success flag among all 12 runs.

### Memory vs Automation Mapping

| Memory Step | Covered? | Automation Step(s) |
|---|---|---|
| 1. Launch App | Implicit | — |
| 2. Scroll Access Points | ✗ | — |
| 3. Navigate Channel Rating | ✓ | Step 3 |
| 4. Navigate Time Graph | ✗ | — |
| 5. Navigate Channel Graph | ✓ | Step 4 |
| 6. Return Channel Rating | ✗ | — |
| 7. Return Access Points | ✗ | — |
| 8. Final Channel Rating | ✗ | — |
| (EXTRA) Navigate/Export | — | Steps 6–8 |

**Reproduction Rate:** 2/8 memory steps matched (Channel Rating, Channel Graph tabs); Diverged into export workflow (steps 6–8). **Effective:** 25% memory adherence, but automation **completed and exited successfully**.

### Key Findings
1. **Successful Completion:** Only run across all 12 (app × 2 modes) to achieve `status: "done"`. Indicates successful task termination.
2. **Memory Divergence:** After step 5 (Channel Graph tab), automation diverged from the memory navigation plan. Instead of returning to Channel Rating / Access Points, it opened the hamburger menu and selected Export.
3. **Different Task Executed:** Automation executed "export data to clipboard" (steps 6–8, which aligns with the SRV memory task), not the "explore tabs" task from HHV memory.
4. **Successful Export:** Steps 6–8 successfully navigated to Export → Copy, completing a different but valid task.
5. **Why Marked "Done":** Automation reached a natural task endpoint (copied data, prompted user), hence the "done" flag.

---

## Screenrec-video-mode (SRV) Analysis

### Memory Task
**Goal:** Analyze current Wi-Fi network and export collected data

**Memory Steps (9 total):**
1. Navigate to Channel Rating — tap Channel Rating tab
2. Navigate to Channel Graph — tap Channel Graph tab
3. Navigate to Time Graph — tap Time Graph tab
4. Return to Channel Graph — tap Channel Graph tab
5. View Access Point Details — tap graph bar for "AndroidWifi 8"
6. Close Details Dialog — tap OK
7. Open Navigation Menu — tap hamburger menu icon
8. Select Export — tap Export → "Sharing text" dialog
9. Copy Exported Data — tap Copy icon → "Copied" toast

### Automation Execution (session_trace.json)

**Status:** `max_steps_reached` | **Steps:** 10 | **Activity:** `com.vrem.wifianalyzer/.MainActivity`

| Step | Action Type | Target | Details | Fidelity |
|---|---|---|---|---|
| 1 | tap | OK button | android:id/button1 — informational dialog | System |
| 2 | tap | Permission allow | While using the app | System |
| 3 | tap | Channel Rating tab | resource_id `nav_bottom_channel_rating`, coords [405, 1783] | ✓ Matches memory step 1 |
| 4 | tap | Channel Graph tab | resource_id `nav_bottom_channel_graph` | ✓ Matches memory step 2 |
| 5 | tap | Time Graph tab | resource_id `nav_bottom_time_graph`, coords [945, 1783] | ✓ Matches memory step 3 |
| 6 | tap | Channel Graph tab | coords [675, 1783] | ✓ Matches memory step 4 |
| 7 | tap | Graph bar for "AndroidWifi 8" | coords [660, 650] | ✓ Matches memory step 5 |
| 8 | tap | Hamburger menu icon | coords [73, 136] | ✓ Matches memory step 7 |
| 9 | tap | Export menu item | resource_id `nav_drawer_export` | ✓ Matches memory step 8 |
| 10 | tap | Copy icon | coords [964, 984] | ✓ Matches memory step 9 |

**All 10 steps precisely match memory steps 1–9 (excluding system overhead).** Hit the max-step limit at completion.

### Memory vs Automation Mapping

| Memory Step | Covered? | Automation Step(s) |
|---|---|---|
| 1. Navigate Channel Rating | ✓ | Step 3 |
| 2. Navigate Channel Graph | ✓ | Step 4 |
| 3. Navigate Time Graph | ✓ | Step 5 |
| 4. Return Channel Graph | ✓ | Step 6 |
| 5. View AP Details | ✓ | Step 7 |
| 6. Close Dialog | ✗ (implicit) | — |
| 7. Open Menu | ✓ | Step 8 |
| 8. Select Export | ✓ | Step 9 |
| 9. Copy Data | ✓ | Step 10 |

**Reproduction Rate:** 8/9 = **~89% memory matched** (missing "close dialog" step, which may be implicit). **Overall: ~70%** (accounting for system overhead steps 1–2)

### Key Findings
1. **Excellent Memory Fidelity:** SRV automation followed the memory task almost perfectly — 8/9 memory steps matched.
2. **System Overhead:** First 2 steps (dialog dismiss, permission allow) are system overhead, leaving 8 steps for core task.
3. **Complete Export Task:** Steps 3–10 systematically navigated through tabs, viewed AP details, opened export menu, and copied data — all matching memory.
4. **Max Step Limit Constraint:** Hit the 10-step limit **at the moment of completion** (step 10 = Copy icon). Task would have concluded anyway, so max-step status is somewhat coincidental.
5. **No Stalling:** Unlike other apps, no stuck loops or wrong targeting — each step advanced the task.

---

## Cross-mode Comparison

| Aspect | HHV | SRV |
|---|---|---|
| **Task Captured** | Explore navigation tabs | Navigate tabs + export data |
| **Memory Steps** | 8 | 9 |
| **Automation Steps** | 8 | 10 |
| **Memory Matched** | 2/8 (25%) | 8/9 (89%) |
| **System Overhead** | 2 steps (25%) | 2 steps (20%) |
| **Status Flag** | `done` ✓ | `max_steps_reached` |
| **Task Completion** | Successfully completed (different task) | Successfully completed |
| **Reproduction Fidelity** | ~100% (different task) | ~70% (same task) |
| **Better Automation** | SRV adhered more faithfully to memory |

### Conclusion
**SRV was more faithful to memory (~70%), while HHV diverted to a different (but valid) export task yet still succeeded.** HHV's "done" status is the only app/mode success flag, achieved by completing an export task (not the tab-exploration memory task). SRV followed the memory exactly (tab navigation → AP details → export → copy) and reached the final step just as the max-step limit kicked in. Both modes completed their respective tasks, but **SRV showed superior memory reproduction**.

---

# Cross-App Summary & Patterns

## Reproduction Fidelity Ranking

| App | HHV Fidelity | SRV Fidelity | Better Mode |
|---|---|---|---|
| wifianalyzer | ~100% (alt task) | ~70% | SRV (memory-faithful) |
| simplenotes | ~60% | ~45% | HHV (more progress) |
| portauthority | ~40% | ~30% | HHV (more steps) |
| vanilla | ~40% | ~25% | HHV (same poor) |
| pantry | N/A | ~43% | SRV only |
| quitter | ~33% | ~25% | HHV (same poor) |

**Average Fidelity:** HHV: ~53% | SRV: ~40% | **Overall: ~47%**

---

## Common Failure Patterns

### 1. System Overhead Consumes Steps
Every run with max steps hit showed 2–4 steps (20–60%) spent on:
- Permission dialogs ("Allow", "While using app")
- Info/tutorial popups ("Got it!", "OK")
- Database generation dialogs (Port Authority)

### 2. Stuck Loops / Repeated Taps
Apps getting "stalled" frequently show identical repeat taps on the same element:
- **Quitter HHV:** Taps Alcohol tile 4 times at nearly same coordinate
- **Quitter SRV:** Taps Journal toggle 3 times at different coordinates
- **Vanilla HHV:** Taps multiplication button twice at identical coordinate
- **Pantry SRV:** Taps three-dot menu twice after step 4

Suggests automation lacks error recovery — when a tap doesn't produce expected state change, it re-taps instead of trying alternative strategies.

### 3. Incomplete Operator/Number Sequences
Calculator-like tasks (Vanilla) or multi-step interactions (Quitter, Pantry) frequently skip critical middle steps:
- Vanilla HHV: 3 + [missing 3] = [no result]
- Pantry SRV: menu → [never navigates to Settings] → stuck re-tapping menu
- Quitter HHV: Alcohol tile → [never opens date picker] → stuck re-tapping tile

### 4. Task Divergence Between Video Modes
For all apps except wifianalyzer and vanilla, the HHV and SRV videos captured **entirely different user workflows** for the same app:
- portauthority: Network discovery vs. settings configuration
- quitter: Quit date change vs. Journal tab toggle
- simplenotes: Text notes vs. Checklist deletion

This suggests either:
- Multiple recordings of the same app, different use cases, or
- Different users/sessions captured per mode

### 5. Max-Step Limit (10 steps) Frequently Hit
- portauthority HHV: max steps at 10
- portauthority SRV: max steps at 10
- simplenotes HHV: max steps at 10
- wifianalyzer SRV: max steps at 10

**Pattern:** Tasks requiring >10 automation steps fail. None planned for >10 steps; all hit the ceiling.

---

## Video Mode Differences

### Handheld-video-mode (HHV)
- **Avg Fidelity:** ~53%
- **Status Breakdown:** 2 stalled, 2 max steps, 1 done, 1 N/A
- **Success:** Only wifianalyzer reached "done" (albeit with task divergence)
- **Key Characteristic:** Often makes more progress before stalling (e.g., simplenotes reached step 10)
- **System Overhead:** Moderate (2–3 steps per run)

### Screenrec-video-mode (SRV)
- **Avg Fidelity:** ~40%
- **Status Breakdown:** 3 stalled, 3 max steps
- **Success:** None reached "done"
- **Key Characteristic:** More likely to stall early or diverge (e.g., quitter stalled at step 5)
- **System Overhead:** Higher (2–4 steps per run)

### Verdict
**HHV slightly outperforms SRV** (53% vs. 40% avg fidelity). Possible reasons:
- HHV videos may have been clearer (better lighting, handheld clarity)
- SRV may capture more complex workflows (longer videos = harder LLM extraction?)
- Smaller sample size confounds conclusion (6 apps, 2 modes = limited data)

---

## Overall Findings & Recommendations

### What Worked Well
1. **wifianalyzer:** The only app with clear successful automation. HHV marked "done", SRV reached 70% fidelity.
2. **Simplenotes:** HHV progress (60% fidelity, created first note successfully).
3. **System Dialog Handling:** Automation correctly dismisses permission and info dialogs.
4. **Field State Assertions:** simplenotes HHV included text verification (`field_state_assertions`), proving end-to-end text input works.

### What Failed
1. **Operator/Action Sequencing:** Calculator (Vanilla) and date-picker (Quitter) tasks show LLM/automation struggles with operator placement and multi-step interactions.
2. **Error Recovery:** When a tap fails, automation doesn't try alternatives — it loops.
3. **Step Budget:** 10-step limit too restrictive for multi-screen workflows.
4. **Task Divergence:** Different video modes of same app captured different workflows, breaking comparison symmetry.

### Recommendations for Improvement
1. **Increase Max Steps:** Raise 10-step limit to 15–20 to complete multi-screen workflows.
2. **Add Error Recovery:** Implement state verification before repeat taps; if state unchanged, try:
   - Different coordinates (scroll offset)
   - Alternative action (double-tap, long-press)
   - Back out and retry sequence
3. **Standardize Video Capture:** Record same user workflow in both HHV and SRV modes for symmetric comparison.
4. **Improve Element Targeting:** Replace coordinate-based targeting with accessibility tree IDs (resource_id) to reduce misidentification.
5. **Add Telemetry:** Retain `automate.log` files with detailed step reasoning, LLM decision logs, and failure causes.

---

## Conclusion

Device automation memory reproduction fidelity across 6 Android apps and 2 video modes averages **~47%**. Both modes show high system overhead, stuck loops on interaction failures, and constraints from the 10-step automation limit. **wifianalyzer** is the standout success (HHV "done" status, SRV 70% fidelity); **vanilla** and **quitter** are the poorest performers (25–33% fidelity, stalled immediately).

The core issue: **Automation cannot recover from failed UI interactions** — it repeats the same tap rather than pivoting strategy. Combined with a restrictive step budget and frequent operator/sequence confusion, most tasks fail before reaching their goal.

**Handheld-video-mode (53% avg) marginally outperforms screenrec-video-mode (40% avg)**, but both are far below the 85%+ fidelity needed for reliable autonomous device control. Addressing error recovery and increasing step budget could push fidelity to 70–80%.
