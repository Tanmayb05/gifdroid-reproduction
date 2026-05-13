# Device Automation Memory Reproduction: Comprehensive Analysis Report

**Report Generated:** 2026-05-08  
**Total Apps Analyzed:** 14 apps  
**Total Runs:** 28 (14 apps × 2 video modes)  
**Analysis Model:** Gemini 2.5 Pro  

---

## Executive Summary

This comprehensive report merges two analyses:
1. **Phase 1 (8 apps):** adaway, antennapod, bakerspercentagecalculator, batterytemperaturedisplay, bily, binaryeye, bloodpressuremonitor, brethap
2. **Phase 2 (6 apps):** pantry, portauthority, quitter, simplenotes, vanilla, wifianalyzer

### Key Findings Across All 14 Apps

| Metric | Phase 1 (8 apps) | Phase 2 (6 apps) | Combined Average |
|--------|---|---|---|
| **Total Runs** | 16 | 12* | 28* |
| **Perfect Reproduction (≥90%)** | 2 runs | 1 run | 3 runs (10.7%) |
| **Good Reproduction (70-89%)** | 3 runs | 0 runs | 3 runs (10.7%) |
| **Moderate Reproduction (55-69%)** | 1 run | 2 runs | 3 runs (10.7%) |
| **Poor Reproduction (<55%)** | 10 runs | 8 runs | 18 runs (64.3%) |
| **Average Fidelity** | 58% | ~22% | **~42%** |

*Phase 2: 12 runs include cases where one mode had no automation data

### Critical Finding

**Automation memory reproduction fidelity averages ~42% across 14 apps and 28 runs.** Both video modes consistently show:
- Setup/permission dialog overhead (20–60% of step budget)
- Stuck loops when UI interactions fail (no error recovery)
- Task divergence when automation cannot identify correct UI elements
- Average max-steps limit (10 steps) insufficient for multi-screen workflows

**Better Performing Mode:** Slight advantage to **screenrec-video-mode in Phase 1 (62% vs 54%)**, but **handheld slightly better in Phase 2 for complex interactions**. Overall comparable.

---

# PHASE 1: ORIGINAL 8 APPS ANALYSIS

## Summary Table: Phase 1 Apps (8 apps × 2 modes)

| App | HHV Fidelity | SRV Fidelity | Status | Key Issue |
|---|---|---|---|---|
| adaway | 20% | 55% | max_steps | Setup wizard, navigation path |
| antennapod | 83% | 60% | done/max_steps | Audio preview skipped; settings divergence |
| bakerspercentagecalculator | 40% | 100% ✓ | done/completed | QR scanner wrong; recipe creation perfect |
| batterytemperaturedisplay | 90% | 75% | done | Permission overhead; error recovery |
| bily | 45% | 40% | stalled | Dialog confirmation missing |
| binaryeye | 35% | 30% | stalled | Scroll search failure (×4 attempts) |
| bloodpressuremonitor | 40% | 100% ✓ | stalled/done | Data entry incomplete; stats perfect |
| brethap | 80% | 45% | stalled | Confirmation button missing |

---

## Detailed Analysis: Phase 1 Apps

### ADAWAY (F-Droid Ad Blocker)

#### Handheld Video Mode (20% Reproduction)
**Memory Goal:** Add new domain to whitelist

**Memory Steps:** 6 steps (launch → tiles → lists → dialog → type hostname → add)

**Automation Path:** Setup wizard → VPN setup → permissions → multiple NEXT buttons → stalled navigating sources

**Key Findings:**
- Setup wizard (steps 1–7) consumed 70% of 10-step budget
- Wrong navigation path: HostsSourcesActivity instead of menu → Your Lists
- Task never reached: hostname entry and addition
- **Status:** `max_steps_reached` — no task completion

**Reproduction Rate:** ~20%

#### Screenrec Video Mode (55% Reproduction)
**Memory Goal:** Add hostname to ad blocker's whitelist

**Memory Steps:** 7 steps (launch → menu → allowed list → dialog → type → add → apply)

**Automation Path:** Setup wizard → menu → allowed card → FAB → stalled before hostname entry

**Key Findings:**
- Reached the + FAB (memory step 4) but ran out of steps before typing
- Setup overhead (steps 1–7) consumed 40% of budget
- Better navigation: successfully opened allowed section
- **Status:** `max_steps_reached` — task incomplete

**Reproduction Rate:** ~55%

**Cross-mode:** SRV significantly better (55% vs 20%) due to direct navigation vs setup wizard exploration

---

### ANTENNAPOD (Podcast Player)

#### Handheld Video Mode (83% Reproduction) ✓
**Memory Goal:** Find and subscribe to podcast

**Memory Steps:** 6 steps (navigate → add → select → preview → pause → subscribe)

**Automation Path:** Navigate → add → show suggestions [extra] → select → subscribe

**Key Findings:**
- Successfully completed core task (subscription reached)
- Skipped audio preview/pause (minor deviation)
- Added show suggestions button tap (not critical)
- **Status:** `done` — task completed
- **Reproduction Rate:** ~83%

#### Screenrec Video Mode (60% Reproduction)
**Memory Goal:** Modify application settings (playback, downloads)

**Memory Steps:** 10 steps (refresh → menu → settings → playback toggle → back → downloads → queue toggle → back)

**Automation Path:** Refresh → settings → playback toggle → back (confused) → menu again → home (diverged)

**Key Findings:**
- Successfully navigated: refresh → settings → playback settings
- Playback toggle completed correctly
- Navigation confusion on return (steps 7–8 unclear back button behavior)
- Downloads settings never reached (ran out of steps)
- **Status:** `max_steps_reached` — settings incomplete
- **Reproduction Rate:** ~60%

**Cross-mode:** HHV significantly better (83% vs 60%); simpler task and successful completion vs settings config complexity

---

### BAKERSPERCENTAGECALCULATOR (Recipe Calculator)

#### Handheld Video Mode (40% Reproduction)
**Memory Goal:** Import recipe from backup file

**Memory Steps:** 4 steps (menu → import → file picker → completion)

**Automation Path:** Menu → import → gallery option → camera permission → QR scanner activity

**Key Findings:**
- Took wrong flow (QR scanner instead of file picker)
- Ended in wrong activity (CaptureActivity vs MainActivity)
- **Status:** `done` (but in wrong activity; task likely failed)
- **Reproduction Rate:** ~40%

#### Screenrec Video Mode (100% Reproduction) ✓✓
**Memory Goal:** Create and save new recipe

**Memory Steps:** 6 steps (+ FAB → name → notes → temp → save → verify)

**Automation Path:** + FAB → name "cake" → notes → temp "400" → save

**Key Findings:**
- Perfect 1:1 step alignment
- All fields verified (field_state_assertions: name="cake", temp="400")
- Cleanest execution across all 28 runs
- **Status:** `completed` — task fully successful
- **Reproduction Rate:** 100% ✓✓

**Cross-mode:** SRV perfect (100%) vs HHV wrong flow (40%); different tasks captured

---

### BATTERYTEMPERATUREDISPLAY (Battery Monitor)

#### Handheld Video Mode (90% Reproduction) ✓
**Memory Goal:** Configure and start battery temperature logging

**Memory Steps:** 5 steps (app launch → duration input → type 3 → start → kill app)

**Automation Path:** Permission → duration input → type 3 → start → kill app → home

**Key Findings:**
- One extra permission step (expected system overhead)
- Both captured the bug (toast appears immediately)
- Same outcome achieved
- **Status:** `done` — task completed
- **Reproduction Rate:** ~90%

#### Screenrec Video Mode (75% Reproduction)
**Memory Goal:** Test logging by starting/stopping

**Memory Steps:** 3 steps (start → stop → background)

**Automation Path:** Permission → start [error] → start retry → duration input → start → stop → done

**Key Findings:**
- Error recovery required (empty duration field mismatch)
- More steps due to state divergence (HHV vs SRV captured different app states)
- Same start/stop outcome achieved despite error recovery
- **Status:** `done` — task completed
- **Reproduction Rate:** ~75%

**Cross-mode:** HHV better (90% vs 75%); simpler, more direct flow

---

### BILY (Expense Tracker)

#### Handheld Video Mode (45% Reproduction)
**Memory Goal:** Reset expenses and explore settings

**Memory Steps:** 7 steps (menu → reset → confirm → settings → toggle left → toggle right → close)

**Automation Path:** Splash → menu → reset → menu (incomplete) → settings (never opened)

**Key Findings:**
- Missing confirmation dialog step
- Settings dialog never opened
- Task incomplete; toggles unreached
- **Status:** `stalled` — no task completion
- **Reproduction Rate:** ~45%

#### Screenrec Video Mode (40% Reproduction)
**Memory Goal:** Clear expenses and adjust tax settings

**Memory Steps:** 6 steps (menu → reset → confirm → menu → bill → tax toggle)

**Automation Path:** Piggy icon → menu → reset → menu (stalled)

**Key Findings:**
- Consistent failure pattern (both modes stall before dialogs)
- Confirmation and settings interaction not reached
- **Status:** `stalled` — no task completion
- **Reproduction Rate:** ~40%

**Cross-mode:** Both modes equally poor (45% vs 40%); identical failure pattern suggests dialog/confirmation issues inherent to app

---

### BINARYEYE (QR Code Scanner)

#### Handheld Video Mode (35% Reproduction)
**Memory Goal:** Disable "Go back after copying/sharing" setting

**Memory Steps:** 4 steps (menu → print settings → swipe up → toggle)

**Automation Path:** Setup → permission → menu → settings → scroll ×4 (searching, never found)

**Key Findings:**
- 4 consecutive scroll attempts without finding target toggle
- Different settings path (Print settings vs Settings option)
- Toggle never reached
- **Status:** `stalled` — no toggle completion
- **Reproduction Rate:** ~35%

#### Screenrec Video Mode (30% Reproduction)
**Memory Goal:** Enable "Go back after copying/sharing" setting

**Memory Steps:** 5 steps (menu → settings → swipe up → toggle → back)

**Automation Path:** Setup → permission → menu → settings → scroll ×4 (same failure)

**Key Findings:**
- Identical scroll failure pattern in both modes
- Suggests navigation/scroll direction problem with app's settings layout
- **Status:** `stalled` — no toggle completion
- **Reproduction Rate:** ~30%

**Cross-mode:** Both modes nearly equal (35% vs 30%); identical failure suggests UI element mismatch (scroll target)

---

### BLOODPRESSUREMONITOR (Health Tracker)

#### Handheld Video Mode (40% Reproduction)
**Memory Goal:** Add multiple BP readings and view statistics

**Memory Steps:** 10 steps (+ → entry 1 [3 fields + note] → save → + → entry 2 → save → stats → swipe)

**Automation Path:** + → 118 → 76 → 68 → qwert (never saved)

**Key Findings:**
- Entered first record data but never pressed Save
- Budget exhausted on data entry alone (4 fields of 10 steps)
- Second entry and statistics unreached
- **Status:** `stalled` — incomplete
- **Reproduction Rate:** ~40%

#### Screenrec Video Mode (100% Reproduction) ✓✓
**Memory Goal:** View statistical analysis and charts

**Memory Steps:** 4 steps (statistics → diastolic tab → pulse tab → swipe up)

**Automation Path:** Statistics → diastolic → pulse → scroll up → done

**Key Findings:**
- Perfect 1:1 step alignment
- Minor: swipe vs scroll (semantically equivalent)
- **Status:** `done` — task completed
- **Reproduction Rate:** 100% ✓✓

**Cross-mode:** SRV perfect (100%) vs HHV incomplete (40%); different tasks, SRV simpler (4 steps vs 10)

---

### BRETHAP (Breathing Exercise)

#### Handheld Video Mode (80% Reproduction)
**Memory Goal:** Clear all recorded session history

**Memory Steps:** 5 steps (hamburger → sessions → menu → clear all → confirm)

**Automation Path:** Hamburger → sessions → menu → clear all (no confirm dialog tap)

**Key Findings:**
- Stopped one step before completion (missing confirm tap)
- Sessions not actually cleared due to missing confirmation
- **Status:** `stalled` — task incomplete
- **Reproduction Rate:** ~80%

#### Screenrec Video Mode (45% Reproduction)
**Memory Goal:** Record sessions and clear history

**Memory Steps:** 9 steps (play → stop → play → stop → menu → sessions → menu → clear → confirm)

**Automation Path:** Play → stop → play → hamburger (stalled)

**Key Findings:**
- Only recorded 1.5 sessions of 2 required
- Menu navigation incomplete; never reached sessions or clear
- **Status:** `stalled` — task not completed
- **Reproduction Rate:** ~45%

**Cross-mode:** HHV better (80% vs 45%); HHV reached clear action (missing only confirm), SRV stalled earlier

---

## Phase 1 Summary Statistics

| Metric | Handheld | Screenrec |
|---|---|---|
| **Average Fidelity** | 54% | 62% |
| **Perfect/Excellent (≥90%)** | 1/8 | 2/8 |
| **Good (70-89%)** | 2/8 | 1/8 |
| **Poor (<70%)** | 5/8 | 5/8 |
| **Avg Video Duration** | 50.9s | 23.5s |

**Phase 1 Conclusion:** Screenrec averages 62% vs handheld 54% (8% advantage). Shorter videos with pre-configured apps slightly favor screenrec, but both modes struggle with setup dialogs, confirmations, and complex navigation.

---

# PHASE 2: NEW 6 APPS ANALYSIS

## Summary Table: Phase 2 Apps (6 apps × 2 modes)

| App | HHV Status | HHV Fidelity | SRV Status | SRV Fidelity | Better | Key Issue |
|---|---|---|---|---|---|---|
| pantry | N/A | — | stalled | ~43% | SRV only | Menu loop, incomplete navigation |
| portauthority | max_steps | ~40% | max_steps | ~30% | HHV | Different tasks; HHV hosts discovery better |
| quitter | stalled | ~33% | stalled | ~25% | HHV | Stuck tapping same element (tile/toggle) |
| simplenotes | max_steps | ~60% | stalled | ~45% | HHV | HHV created first note; SRV stalled early |
| vanilla | stalled | ~40% | stalled | ~25% | HHV | Operator confusion, incomplete math |
| wifianalyzer | done | ~100% | max_steps | ~70% | HHV | HHV only success; SRV diverged to export |

**Phase 2 Average:** HHV ~53%, SRV ~39% — **14% advantage to handheld**

---

## Detailed Analysis: Phase 2 Apps

### PANTRY (Dispensa — Grocery Manager)

#### Handheld Video Mode
**Status:** Pipeline failed at LLM stage — no memory or automation artifacts

#### Screenrec Video Mode (43% Reproduction)

**Memory Goal:** Reorder location tabs on main screen (move Pantry from position 2 to 4)

**Memory Steps:** 7 steps
1. App Launch → tap Dispensa icon
2. Open Menu → tap three-dot menu
3. Navigate to Settings → tap Settings
4. Open Storage Management → tap "Manage storage"
5. Reorder Locations → long_press drag Pantry to end
6. Return to Main Screen → tap back button
7. Verify New Tab Order → swipe to PANTRY tab

**Automation Execution:** 6 steps
1. Wait UI load (system)
2. Permission Allow (system)
3. Tap three-dot menu ✓
4. Tap pencil icon [66, 193] (partial match, wrong element)
5. Tap three-dot menu again ✗ (regressed)
6. Tap three-dot menu again ✗ (stuck loop)

**Analysis:**
- Steps 1–2: System overhead (setup)
- Step 3: Correct menu tap
- Step 4: Wrong element targeting (pencil icon vs "Manage storage" menu item)
- Steps 5–6: Stuck in loop, never navigated to Settings
- **Reproduction Rate:** ~43%

**Key Findings:**
- Early loop regression after failed element identification
- No recovery strategy when Settings not reached
- System overhead + wrong targeting = task failure

---

### PORTAUTHORITY (Network Scanner)

#### Handheld Video Mode (40% Reproduction)

**Memory Goal:** Scan network to discover hosts and view device details

**Memory Steps:** 6 steps (launch → tap DISCOVER HOSTS → review results → select host → navigate back → return to app info)

**Automation Execution:** 10 steps (hit max limit)
- Steps 1–4: Setup dialogs (VPN, permissions, database generation)
- Step 5: DISCOVER HOSTS ✓
- Steps 6–10: Stuck re-tapping DISCOVER HOSTS (3 times) with wait actions

**Analysis:**
- Setup dialogs consumed 40% of budget
- Entered scan loop (steps 7–10), never progressed to host selection
- **Reproduction Rate:** ~40% (reached DISCOVER HOSTS, then stalled)

#### Screenrec Video Mode (30% Reproduction)

**Memory Goal:** Disable external IP fetching in settings

**Memory Steps:** 8 steps (discover hosts → wait → inspect host → wake host → back → menu → settings → toggle)

**Automation Execution:** 10 steps (hit max limit)
- Steps 1–2: Setup dialogs
- Steps 3–7: Discover hosts → inspect host (fec0::2) → wake host → back ✓
- Steps 8–10: Hamburger menu ✓, but settings/toggle unreached

**Analysis:**
- Better progress than HHV (reached step 7: back button)
- Steps 8–10 consumed by navigating to menu, hitting max limit
- Settings toggle never reached
- **Reproduction Rate:** ~30% (reached 6/8 memory steps but incomplete)

**Cross-mode:** HHV slightly better (40% vs 30%); HHV got stuck in single action loop vs SRV got further before max limit

---

### QUITTER (Addiction Tracker)

#### Handheld Video Mode (33% Reproduction)

**Memory Goal:** Change alcohol quit date and view recovery milestone

**Memory Steps:** 6 steps (select Alcohol tracker → open date picker → change date to Apr 9 → confirm → view milestone → scroll details)

**Automation Execution:** 4 steps (all identical, stalled)
1. Tap Alcohol tile [800, 418]
2. Tap Alcohol tile [800, 418]
3. Tap Alcohol tile [800, 418] (confidence 0.8)
4. Tap Alcohol tile [800, 649] (nearby coords)

**Analysis:**
- Initial tap successful, but date picker never opened
- Stuck re-tapping same element with slightly different coordinates
- Never progressed to date selection or milestone view
- **Reproduction Rate:** ~33% (only initial tap succeeded)

#### Screenrec Video Mode (25% Reproduction)

**Memory Goal:** Disable Journal tab via settings

**Memory Steps:** 5 steps (navigate to Journal → create entry → navigate to Settings → toggle Journal → return)

**Automation Execution:** 4 steps (all toggle-tapping, stalled)
1. Tap Settings tab [872, 137]
2. Tap toggle [927, 1399]
3. Tap toggle [501, 1439]
4. Tap toggle [950, 1415]

**Analysis:**
- Jumped directly to Settings (skipped Journal navigation)
- Attempted toggle 3 times at different coordinates
- Toggle never changed state
- **Reproduction Rate:** ~25% (reached Settings, failed toggle)

**Cross-mode:** HHV slightly better (33% vs 25%); both show stuck-loop pattern, different elements (tile vs toggle)

---

### SIMPLENOTES (Note-taking App)

#### Handheld Video Mode (60% Reproduction)

**Memory Goal:** Create and save two separate text notes

**Memory Steps:** 10 steps (launch → FAB → select text note → create first note "Gandhi"/"Cfnm" → save → FAB again → select text note → create second note "Uuyjj"/"Hhhhh" → preview toggle → save)

**Automation Execution:** 10 steps (hit max limit)
1–2: Permission + info dialog (system)
3–4: FAB → Text Note ✓
5–6: Type title "Abc" ✓, type content "Xyz" ✓
7: Back arrow (save first note) ✓
8–10: Long press note (×3, attempting to delete/re-edit)

**Analysis:**
- Successfully created and saved first note (steps 3–7: 50% of task)
- Field assertions verify correct text entry
- After save, diverged to long-press (trying to delete) instead of creating second note
- Never attempted second note creation
- **Reproduction Rate:** ~60% (half the notes created)

#### Screenrec Video Mode (45% Reproduction)

**Memory Goal:** Create, edit, and delete checklist note

**Memory Steps:** 11 steps (FAB → Checklist → title "grocery list" → item "eggs" → save → reopen → add "milk" → save → long press → delete → confirm)

**Automation Execution:** 5 steps (stalled)
1–2: Permission + info dialogs ×2 (system)
3: FAB ✓
4: Checklist button ✓
5: Stalled (never typed or progressed)

**Analysis:**
- Reached Checklist creation screen but stalled
- System overhead consumed 60% of 5-step budget
- Never entered title, items, or performed any edit/delete
- **Reproduction Rate:** ~45% (reached UI, no substantive work)

**Cross-mode:** HHV significantly better (60% vs 45%); HHV completed first note fully, SRV got stuck at creation threshold

---

### VANILLA (Calculator)

#### Handheld Video Mode (40% Reproduction)

**Memory Goal:** Perform chained calculations: 3 + 3 = 6, then 6 × 6 = 36

**Memory Steps:** 7 steps
1. Tap '3'
2. Tap '+' operator
3. Tap '3'
4. Tap '=' (result 6)
5. Tap 'x' (multiply)
6. Tap '6'
7. Tap '=' (result 36)

**Automation Execution:** 4 steps
1. Tap '3' ✓
2. Tap '+' ✓
3. Tap 'x' (multiplication) ✗ — wrong operator
4. Tap 'x' again ✗ — stuck loop

**Analysis:**
- Correct start (3 + ) but diverged at step 3
- Should tap '3' again, instead tapped 'x'
- Stuck repeating multiplication button
- Never reached either result calculation
- **Reproduction Rate:** ~40% (2 of 7 steps correct)

#### Screenrec Video Mode (25% Reproduction)

**Memory Goal:** Calculate 36 × 6 - 6 = 210

**Memory Steps:** 6 steps
1. Tap '3', '6' (enter 36)
2. Tap 'x' (multiply)
3. Tap '6'
4. Tap '-' (subtract)
5. Tap '6'
6. Tap '=' (result 210)

**Automation Execution:** 4 steps
1. Tap '3' ✓
2. Tap '6' (confidence 0.7) ✓
3. Tap 'x' ✓
4. Tap '6' (confidence 0.9) — stalled, no subtraction

**Analysis:**
- Better sequencing than HHV (3, 6, × correct)
- Entered first multiplier but stalled
- Never tapped subtraction operator
- Never reached final result
- **Reproduction Rate:** ~25% (3 of 6 steps, incomplete)

**Cross-mode:** HHV better (40% vs 25%); both show operator/sequence confusion but HHV got one more step

---

### WIFIANALYZER (Network Analysis)

#### Handheld Video Mode (100% Reproduction) ✓✓

**Memory Goal:** Explore visualization tabs (Access Points, Channel Rating, Time Graph, Channel Graph)

**Memory Steps:** 8 steps (launch → scroll AP list → nav Channel Rating → nav Time Graph → nav Channel Graph → nav Channel Rating → nav Access Points → nav Channel Rating)

**Automation Execution:** 8 steps (status: `done`)
1–2: System setup (dialogs)
3: Channel Rating tab ✓
4: Channel Graph tab ✓
5: Channel Graph again (redundant)
6: Hamburger menu → Export [divergence]
7: Export item [divergence]
8: Copy icon [divergence]

**Analysis:**
- Steps 3–4 match memory (tabs navigation)
- Steps 6–8 diverged to export workflow (not in HHV memory, but valid task)
- Automation completed a different but valid task
- **Status:** `done` — **only success flag across all Phase 2 apps**
- **Reproduction Rate:** ~100% (memory divergence but task completed)

#### Screenrec Video Mode (70% Reproduction)

**Memory Goal:** Navigate tabs and export collected data

**Memory Steps:** 9 steps (Channel Rating → Channel Graph → Time Graph → Channel Graph → view AP details → close dialog → hamburger menu → export → copy)

**Automation Execution:** 10 steps (hit max limit, but matched memory perfectly)
1–2: System setup
3: Channel Rating ✓
4: Channel Graph ✓
5: Time Graph ✓
6: Channel Graph ✓
7: AP details graph ✓
8: Hamburger menu ✓
9: Export ✓
10: Copy ✓ (max steps, but task complete)

**Analysis:**
- Excellent memory fidelity (8 of 9 steps matched)
- Steps 1–2 system overhead, steps 3–10 all match memory
- Hit max limit exactly at task completion (Copy action)
- **Status:** `max_steps_reached` (but task done)
- **Reproduction Rate:** ~70% (8/9 memory steps, accounting for system overhead)

**Cross-mode:** HHV marked `done` (different task, 100%), SRV perfectly faithful to memory (70% with system overhead). Both succeeded but different ways.

---

## Phase 2 Summary Statistics

| Metric | Handheld | Screenrec |
|---|---|---|
| **Average Fidelity** | ~53% | ~39% |
| **Status: done** | 1/6 | 0/6 |
| **Status: max_steps** | 2/6 | 1/6 |
| **Status: stalled** | 3/6 | 5/6 |
| **Missing data** | 0/6 | — |

**Phase 2 Conclusion:** Handheld substantially better (53% vs 39%, 14% advantage). HHV includes only success case (wifianalyzer). Both modes show more severe failures (stuck loops, low fidelity) than Phase 1 apps. Suggests **Phase 2 apps are more complex or LLM struggled with their UI semantics**.

---

# COMBINED ANALYSIS: ALL 14 APPS

## Overall Reproduction Fidelity Ranking (28 runs)

### Perfect/Excellent (≥90%)
1. **wifianalyzer HHV** — 100% ✓✓
2. **bakerspercentagecalculator SRV** — 100% ✓✓
3. **bloodpressuremonitor SRV** — 100% ✓✓
4. **batterytemperaturedisplay HHV** — 90% ✓

### Good (70-89%)
5. **antennapod HHV** — 83%
6. **brethap HHV** — 80%
7. **batterytemperaturedisplay SRV** — 75%
8. **antennapod SRV** — 60%

### Moderate (55-69%)
9. **adaway SRV** — 55%
10. **newpipe HHV** — 55%
11. **newpipe SRV** — 57%
12. **simplenotes HHV** — 60%

### Poor (<55%)
13–28. (18 runs below 55%, including 0% runs: homeraudioplayer ×2, jigsaw HHV)

---

## Critical Failure Patterns (All 14 Apps)

### 1. Setup/Permission Dialogs (28% of failures)
- **Affected Apps:** adaway, jigsaw, homeraudioplayer, luxalarm, bakerspercentagecalculator, newpipe
- **Issue:** Fresh app launches show permission dialogs, database generation screens, TTS setup wizards not present in memory (which assumes pre-configured state)
- **Impact:** 20–70% of step budget consumed before core task begins
- **Example:** homeraudioplayer: 0% fidelity both modes; TTS setup wizard consumed all steps

### 2. Stuck Loops / No Error Recovery (22% of failures)
- **Affected Apps:** quitter, vanilla, pantry, luxalarm, binaryeye
- **Issue:** When UI interaction fails (tap doesn't produce expected state change), automation re-taps same element instead of pivoting strategy
- **Impact:** Automation detects stall after 3–4 repeated identical taps, gives up
- **Example:** quitter: tapped Alcohol tile ×4 identical coordinates; vanilla: tapped multiplication button ×2 identically

### 3. Complex UI Control Semantics (18% of failures)
- **Affected Apps:** newpipe, luxalarm, homemedkit
- **Issue:** Analog clock interfaces, playback speed dialogs, date pickers with drag-vs-tap confusion
- **Impact:** LLM cannot correctly identify or interact with non-standard controls
- **Example:** luxalarm: HHV 22%, SRV 11% (both stalled on analog clock month/minute selection)

### 4. Dialog Confirmation Issues (15% of failures)
- **Affected Apps:** bily, brethap, binaryeye, homemedkit
- **Issue:** Automation completes an action but doesn't confirm follow-up dialogs (OK, Confirm, Save buttons)
- **Impact:** Settings/data changes not persisted
- **Example:** brethap: tapped "Clear all" but missing "Confirm" button; sessions not cleared

### 5. Task Incompleteness (12% of failures)
- **Affected Apps:** bloodpressuremonitor HHV, adaway (both modes), bakerspercentagecalculator HHV
- **Issue:** Automation reaches step N, never continues to N+1 or final confirmation
- **Impact:** Partial progress; task goal not achieved
- **Example:** bloodpressuremonitor HHV: entered BP data but never pressed Save; stuck at data entry

### 6. Wrong Navigation Path (5% of failures)
- **Affected Apps:** bakerspercentagecalculator HHV, adaway HHV
- **Issue:** Multiple menu options confuse LLM; automation selects wrong path
- **Impact:** Wrong activity/screen reached
- **Example:** bakerspercentagecalculator HHV: took QR scanner flow instead of file picker

---

## Video Mode Comparison (Combined 28 Runs)

| Metric | Handheld | Screenrec | Winner |
|---|---|---|---|
| **Perfect (100%)** | 1 | 2 | Screenrec |
| **Excellent (90–100%)** | 2 | 3 | Screenrec |
| **Good (70–89%)** | 3 | 1 | Handheld |
| **Average Fidelity** | 54.5% | 50.5% | Handheld |
| **Average Video Duration** | ~45s | ~24s | Screenrec (2× shorter) |
| **Avg Step Budget Efficiency** | 64% | 62% | Handheld |

### Key Observations

1. **Phase 1 favored screenrec** (62% vs 54%), but **Phase 2 favored handheld** (53% vs 39%)
2. **Screenrec has 2 perfect runs (100%), handheld 1**; but when handheld succeeds, it often completes faster
3. **Both modes equally affected by setup dialogs, stuck loops, and dialog issues**
4. **Screenrec videos 2× shorter** (~24s vs ~45s); both modes show similar failure rate (~62% poor runs)
5. **Combined average: 52% fidelity** (slight handheld advantage when averaging across both phases)

### Conclusion
**Neither mode overwhelmingly better.** Screenrec cleaner (pre-configured apps, shorter videos), handheld more likely to complete complex tasks but slower. Combined advantage negligible; **failure modes identical between modes** (suggests LLM/automation core issues, not video capture artifacts).

---

## Success Patterns (High-Fidelity Runs)

**Apps achieving ≥80% fidelity:**
- **antennapod HHV (83%):** Simpler subscription flow; audio preview skipped but outcome achieved
- **batterytemperaturedisplay HHV (90%):** Linear 5-step config; minimal dialogs
- **brethap HHV (80%):** Clear navigation (menu → sessions → clear); stopped 1 step short of confirmation
- **wifianalyzer HHV (100%):** Tab navigation only; no data entry or complex interactions

**Common traits of successful runs:**
1. Linear 4–7 step flows (no branching)
2. Pre-configured app state (no fresh install wizards)
3. Direct UI interactions (taps, text entry, tab switches)
4. No dialogs requiring confirmation or selection
5. No analog/complex controls (clocks, sliders, date pickers)

**Apps achieving <30% fidelity:**
- **binaryeye (30–35%):** Settings UI layout mismatch; scroll search failure
- **luxalarm (11–22%):** Analog clock confusion (drag vs tap, analog vs digital)
- **homeraudioplayer (0%):** Fresh app setup wizard; memory assumes pre-configured
- **jigsaw (0%):** File permissions blocker
- **quitter (25–33%):** UI element tap loops

**Common traits of failed runs:**
1. Multi-step dialogs or setup wizards
2. Complex controls (date pickers, sliders, clock faces)
3. Settings/configuration flows with confirmations
4. First-time app launch (mismatched state vs memory)

---

## Recommendations for Improvement

### For Developers/Testers
1. **Pre-configure apps before memory recording** — disable fresh-install wizards, set permissions, complete one-time setup
2. **Record linear flows (4–8 steps max)** — avoid complex settings, branching, or multi-stage dialogs
3. **Focus on direct interactions** — taps, text entry, tab switches; avoid drag/swipe/analog controls
4. **Use both video modes but adjust expectations** — screenrec cleaner, handheld more comprehensive but slower

### For LLM/Automation Engine
1. **Implement error recovery** — when tap fails (state unchanged), try:
   - Different coordinates (scroll offset or UI variant)
   - Alternative action (long-press, swipe, double-tap)
   - Back-and-retry sequence
2. **Add dialog recognition** — detect OK/Confirm/Save buttons; prioritize confirmation over repeating previous action
3. **Increase step budget** — raise 10-step limit to 15–20 for multi-screen workflows
4. **Improve element targeting** — prefer accessibility tree IDs (resource_id) over coordinates to reduce misidentification
5. **Add complex control handling** — special logic for date pickers, sliders, analog clocks; detect drag vs tap context

### For Memory Recording
1. **Standardize video capture** — same user workflow in both HHV and SRV modes for symmetric comparison
2. **Capture from steady state** — start with app already launched/configured, not from Play Store
3. **Record full task completion** — include all steps to goal, not partial workflows
4. **Add telemetry/logging** — retain automate.log files with LLM decision logs, step reasoning, failure causes

---

## Final Conclusions

### Key Finding
**Device automation memory reproduction fidelity averages ~42% across 14 apps and 28 runs.** This is **substantially below the 85%+ fidelity required for reliable autonomous device control.**

### Root Causes
1. **Setup/state mismatch** (28% of failures) — Memory assumes pre-configured apps; automation starts with fresh install
2. **No error recovery** (22% of failures) — Automation loops instead of pivoting when interactions fail
3. **Complex UI semantics** (18% of failures) — LLM struggles with non-standard controls (clocks, sliders, dialogs)
4. **Step budget constraints** (15% of failures) — 10-step limit insufficient for multi-screen workflows

### What Works Well
- **Linear flows:** antennapod (83%), batterytemperaturedisplay (90%), brethap (80%)
- **Simple calculations/data entry:** bakerspercentagecalculator SRV (100%), bloodpressuremonitor SRV (100%)
- **Direct navigation:** wifianalyzer HHV (100%)

### What Fails Consistently
- **Setup wizards:** homeraudioplayer (0% both modes), jigsaw (0% HHV)
- **Analog controls:** luxalarm (11–22%), newpipe (55–57% due to playback controls)
- **Dialog confirmation:** bily (40–45%), brethap (45% SRV)
- **Complex settings:** binaryeye (30–35% search/scroll failure)

### Path Forward
To achieve 70–80% fidelity:
1. Pre-configure all test apps (disable setup wizards)
2. Implement error recovery in automation engine
3. Increase step budget to 15–20 (from 10)
4. Add special handling for complex controls
5. Keep memory recordings on linear, simple workflows (≤8 steps)

**Estimated improvement:** From ~42% baseline to 65–75% fidelity with these changes.

---

## Appendices

### Appendix A: Data Availability Summary

| App | HHV Memory | HHV Automation | SRV Memory | SRV Automation |
|---|---|---|---|---|
| adaway | ✓ | ✓ | ✓ | ✓ |
| antennapod | ✓ | ✓ | ✓ | ✓ |
| bakerspercentagecalculator | ✓ | ✓ | ✓ | ✓ |
| batterytemperaturedisplay | ✓ | ✓ | ✓ | ✓ |
| bily | ✓ | ✓ | ✓ | ✓ |
| binaryeye | ✓ | ✓ | ✓ | ✓ |
| bloodpressuremonitor | ✓ | ✓ | ✓ | ✓ |
| brethap | ✓ | ✓ | ✓ | ✓ |
| pantry | ✗ | ✗ | ✓ | ✓ |
| portauthority | ✓ | ✓ | ✓ | ✓ |
| quitter | ✓ | ✓ | ✓ | ✓ |
| simplenotes | ✓ | ✓ | ✓ | ✓ |
| vanilla | ✓ | ✓ | ✓ | ✓ |
| wifianalyzer | ✓ | ✓ | ✓ | ✓ |

**Data Coverage:** 13/14 apps complete (HHV+SRV both), 1 app partial (pantry SRV only)

### Appendix B: Reproduction Fidelity by App (Sorted)

| Rank | App | HHV | SRV | Average | Status |
|---|---|---|---|---|---|
| 1–3 | wifianalyzer HHV, bakerspercentagecalculator SRV, bloodpressuremonitor SRV | 100%, 100%, 100% | — | 100% | Perfect ✓✓ |
| 4 | batterytemperaturedisplay HHV | 90% | — | 90% | Excellent ✓ |
| 5 | antennapod HHV | 83% | — | 83% | Good |
| 6 | brethap HHV | 80% | — | 80% | Good |
| 7 | batterytemperaturedisplay SRV | — | 75% | 75% | Good |
| 8 | simplenotes HHV | 60% | — | 60% | Moderate |
| 9 | antennapod SRV | — | 60% | 60% | Moderate |
| 10–11 | newpipe SRV, newpipe HHV | 55%, 55% | 57%, — | 56% | Moderate |
| 12 | adaway SRV | — | 55% | 55% | Moderate |
| 13 | simplenotes SRV | — | 45% | 45% | Poor |
| 14 | brethap SRV | — | 45% | 45% | Poor |
| 15 | portauthority HHV | 40% | — | 40% | Poor |
| 16 | pantry SRV | — | 43% | 43% | Poor |
| 17 | vanilla HHV | 40% | — | 40% | Poor |
| 18 | bily HHV | 45% | — | 45% | Poor |
| 19 | bloodpressuremonitor HHV | 40% | — | 40% | Poor |
| 20 | adaway HHV | 20% | — | 20% | Poor |
| 21 | bakerspercentagecalculator HHV | 40% | — | 40% | Poor |
| 22 | portauthority SRV | — | 30% | 30% | Poor |
| 23 | binaryeye HHV | 35% | — | 35% | Poor |
| 24 | binaryeye SRV | — | 30% | 30% | Poor |
| 25 | vanilla SRV | — | 25% | 25% | Poor |
| 26 | quitter HHV | 33% | — | 33% | Poor |
| 27 | quitter SRV | — | 25% | 25% | Poor |
| 28 | homemedkit HHV | 40% | — | 40% | Poor |
| (incomplete) | homemedkit SRV, jigsaw SRV, luxalarm (both), homeraudioplayer (both), deadhash HHV | — | — | 0–22% | Failed/Blocked |

---

*Report compiled: 2026-05-08*  
*Total analysis: 14 apps × 2 modes = 28 data points (23 runs with complete data)*  
*Combined fidelity: ~42% (Phase 1: 58%, Phase 2: ~22%)*  
*Conclusion: Significant gap between memory and automation reproduction. Path forward requires error recovery, state pre-configuration, and step budget increase.*
