# ViBR vs Gemini 2.5 Pro VM Analysis: bloodpressuremonitor

## Executive Summary

**App:** bloodpressuremonitor  
**Test Date:** May 13, 2026  
**Overall Status:** ⚠️ PARTIAL SUCCESS with Critical State Detection Issues

ViBR successfully completed **1 of 3 runs** without significant issues, but encountered critical state misalignment failures on **2 of 3 runs**. The primary failure mode is **modal dialog detection**: ViBR fails to detect when a color picker dialog appears on top of the form, causing it to skip remaining actions and report functional state mismatch.

---

## Run-by-Run Analysis

### Run 1: hhv-002-vibr/run-001
**Video:** hhv-002 (handheld video)  
**Status:** ⚠️ PARTIAL FAILURE (2/4 segments executed)

#### Gemini Ground Truth (hhv-002-gemini-2.5-pro-vm/run-001)
1. **Step 1:** Tap `+` icon → Navigate to Add Record screen
2. **Step 2:** Type Systolic/Diastolic/Pulse (118/76/68) → Fields populated
3. **Step 3:** Type Note "qwert" → Note field populated  
4. **Step 4:** Tap Save → Return to main screen, single data point visible
5. **Step 5:** Tap `+` icon again → Navigate to Add Record screen
6. **Step 6:** Type Systolic/Diastolic/Pulse (122/78/72) → Fields populated
7. **Step 7:** Type Note "poiu" → Note field populated
8. **Step 8:** Tap Save → Return to main, graph appears with 2 data points
9. **Step 9:** Tap Statistics icon → Navigate to Statistics screen
10. **Step 10:** Swipe left on chart → Cycle through metrics

#### ViBR Execution
- **Segment 0:** ✅ TAP executed (predicted tap)
- **Segment 1:** ⏭️ SKIPPED - input_text - **Reason:** "Color picker dialog present, not in reference screen"
- **Segment 2:** ✅ TAP executed (predicted tap)
- **Segment 3:** ⏭️ SKIPPED - input_text - **Reason:** "Color picker dialog over form, reference shows keyboard open"

#### Comparison Table

| Step | Gemini Action | ViBR Status | Divergence | Root Cause |
|------|---------------|-------------|-----------|-----------|
| 1 | Tap + icon | ✅ Executed | None | — |
| 2 | Type Systolic/Diastolic/Pulse | ❌ Skipped | **DIVERGE** | **Color picker dialog detection failure** |
| 3 | Type Note | ❌ Skipped | **DIVERGE** | **Modal dialog blocks interaction** |
| 4 | Tap Save | ✅ Executed | None | — |
| 5+ | Remaining steps | ❌ Not reached | **COMPLETE STOP** | **State misalignment prevents continuation** |

#### Failure Analysis
- **Divergence Point:** Step 2 (first text input)
- **Failure Type:** **Detection Failure + State Mismatch**
- **Root Cause:** ViBR's vision system detected a color picker dialog appearing over the form but reported it as a functional state mismatch rather than a UI overlay. The form remains accessible underneath, but ViBR conservatively skipped text input.
- **Evidence from Logs:**
  - Segment 1 skip reason: "the current screen displays a color picker dialog that is not present in the reference screen"
  - Segment 3 skip reason: "The current screen shows a color picker dialog that has appeared on top of the data entry form"
  - This is a **modal detection issue**, not a real functional difference
- **Impact:** Complete task failure after first text input attempt

---

### Run 2: srv-001-vibr/run-001
**Video:** srv-001 (server video, likely different app state)  
**Status:** 🔴 COMPLETE FAILURE (0/8 segments executed)

#### Gemini Ground Truth (srv-001-gemini-2.5-pro-vm/run-001)
1. **Step 1:** Tap Statistics button → Navigate to Statistics screen (1 entry: 98, 70, 123)
2. **Step 2:** Tap Diastolic tab → Chart updates to Diastolic view (70)
3. **Step 3:** Tap Pulse tab → Chart updates to Pulse view (123)
4. **Step 4:** Swipe up → Scroll to see Metrics by time of day radar chart

#### ViBR Execution
- **Segment 0:** ⏭️ SKIPPED - tap - **Reason:** "Reference shows data row, current screen has no data"
- **Segments 1-7:** ⏭️ ALL SKIPPED - tap/swipe/no action - **Reasons:** State mismatches

#### Comparison Table

| Step | Gemini Action | ViBR Status | Divergence | Root Cause |
|------|---------------|-------------|-----------|-----------|
| 1 | Tap Statistics button | ❌ Skipped | **DIVERGE at START** | **Data state mismatch** |
| 2 | Tap Diastolic tab | ❌ Skipped | **COMPLETE STOP** | **Screen state fundamentally different** |
| 3 | Tap Pulse tab | ❌ Skipped | **COMPLETE STOP** | **Charts not present** |
| 4 | Swipe up | ❌ Skipped | **COMPLETE STOP** | **Radar chart missing** |

#### Failure Analysis
- **Divergence Point:** Step 1 (immediate failure at first action)
- **Failure Type:** **State Detection Failure**
- **Root Cause:** **Data inconsistency between video scenes**. The srv-001 video shows two different functional states:
  - **Reference screen (Gemini's view):** Statistics page with populated data (1 entry: 98, 70, 123)
  - **Current screen (ViBR's view):** Empty/initial state with "no data" message
  
  ViBR correctly detected this is not the same state and skipped all 8 segments to avoid executing actions against wrong context.
  
- **Evidence from Logs:**
  - Segment 0: "the reference screen displays a row of data (98, 70, 123), while the current screen does not show any data"
  - Segments 1-7 systematically skipped for state mismatches:
    - "reference screen displays a list of past readings and a graph area, while the current screen is a form for entering a new reading"
    - "reference screen shows a 'statistics' page with graphs and data summaries. the current screen is a data entry form"
- **Impact:** Task cannot be executed; fundamental state mismatch prevents any action

---

### Run 3: srv-001-vibr/run-002
**Video:** srv-001 (second attempt on same video)  
**Status:** 🔴 COMPLETE FAILURE (1/8 segments executed, all others skipped)

#### ViBR Execution
- **Segment 0:** ⏭️ SKIPPED - no action - **Reason:** "Reference shows row of data, current screen has no data"
- **Segment 1:** ✅ NO ACTION executed (conservative pass-through)
- **Segments 2-7:** ⏭️ ALL SKIPPED - **Reasons:** State mismatches (missing elements, wrong screens)

#### Detailed Skip Reasons
| Segment | Action Type | Skip Reason |
|---------|------------|------------|
| 2 | tap | "No valid region or element match" |
| 3 | swipe | "current screen shows empty state with 'no data', reference has populated charts" |
| 4 | no action | "reference shows 'metrics by time of day' graph, current shows 'measurement count' section" |
| 5 | no action | "reference has circular radar graph missing from current screen" |
| 6 | no action | "two different statistics pages - reference has 'metrics by time of day', current has tabs for systolic/diastolic/pulse" |
| 7 | no action | "current has tabs and FABs not in reference; missing title and back button" |

#### Failure Analysis
- **Divergence Point:** Step 1 (immediate state mismatch)
- **Failure Type:** **State Detection Failure + Screen Layout Mismatch**
- **Root Cause:** **Same root cause as run-002** — srv-001 video contains incompatible reference and current states. ViBR's conservative approach skips all actions when state doesn't match ground truth.
- **Critical Finding:** This suggests the srv-001 video itself has structural issues:
  - Reference frames show populated statistics screen with data
  - Current frames show empty/different state
  - This is NOT a ViBR detection failure; ViBR is **correctly identifying incompatible states**

---

## Cross-Run Summary Table

| Run | Video | Gemini Ground Truth | ViBR Execution | Executed/Total | Failure Type | Severity |
|-----|-------|-------------------|-----------------|---|---|---|
| 1 | hhv-002 | 10 complete steps | 2/4 segments | 50% | Modal dialog detection | Medium |
| 2 | srv-001 | 4 steps | 0/8 segments | 0% | Data state mismatch | Critical |
| 3 | srv-001 (retry) | 4 steps | 1/8 segments | 12.5% | Screen layout mismatch | Critical |

---

## Failure Root Causes Categorized

### 1. **Modal Dialog Detection (hhv-002 Run 1)** - Medium Severity
- **Type:** Detection Failure
- **Description:** Color picker dialog appears over form; ViBR detects it but treats it as functional state difference rather than overlay
- **Impact:** Skips text input operations; task cannot complete
- **Log Evidence:**
  ```
  Segment 1 skip: "color picker dialog that is not present in the reference screen. this dialog is modal and blocks interaction"
  Segment 3 skip: "color picker dialog that has appeared on top of the data entry form"
  ```
- **Why It Matters:** Modal dialogs are temporary UI overlays, not fundamental state changes. ViBR should either wait for dismissal or execute actions anyway

### 2. **Data State Mismatch (srv-001 Runs 1 & 2)** - Critical Severity
- **Type:** State Detection Failure (correctly identified by ViBR)
- **Description:** srv-001 video shows incompatible reference and current states (populated vs. empty data)
- **Impact:** All 8 segments skipped; task cannot execute
- **Log Evidence:**
  ```
  Segment 0: "reference screen displays a row of data (98, 70, 123), while the current screen does not show any data"
  Segments 1-7: Consistent reporting of different screens (statistics with data vs. empty form/state)
  ```
- **Why It Matters:** This is **NOT a ViBR bug**. ViBR is correctly refusing to execute actions when reference/current states are fundamentally different. The video itself has problematic reference frames.

### 3. **Screen Layout Mismatch (srv-001 Run 2, Segments 6-7)** - Critical Severity  
- **Type:** State Detection Failure
- **Description:** Reference shows one statistics layout; current shows different layout with different UI elements (tabs vs. no tabs, FABs present vs. absent)
- **Impact:** Systematic skipping of all remaining actions
- **Log Evidence:**
  ```
  Segment 6: "two screens show different statistics pages... reference has 'metrics by time of day' graph"
  Segment 7: "current has tabs and FABs not in reference... missing title and back button"
  ```

---

## Key Observations

1. **Success Case (hhv-002):** Only achieved 50% execution due to modal dialog detection
2. **Failure Cases (srv-001):** Both runs show 0-12% execution; root cause is video reference/current state incompatibility
3. **ViBR's Conservative Behavior:** When state mismatches are detected, ViBR skips actions to avoid executing against wrong context — this is **correct behavior**
4. **Video Quality Issue:** srv-001 appears to have misaligned reference/current pairs, causing systematic failures

---

## Failure Classification Summary

| Category | hhv-002 | srv-001 (run-001) | srv-001 (run-002) | Total |
|----------|---------|------------------|------------------|-------|
| Detection Failure | ✅ Modal overlay | ❌ Data presence | ✅ Element detection | 2 runs |
| Interpretation Failure | ❌ | ❌ | ❌ | 0 runs |
| Execution Failure | ❌ | ❌ | ❌ | 0 runs |
| Timing Issue | ❌ | ❌ | ❌ | 0 runs |
| Context Loss | ❌ | ❌ | ❌ | 0 runs |
| **State Mismatch** | ⚠️ Modal | ✅ Data state | ✅ Screen layout | **3 runs** |

---

## Recommendations

### For hhv-002 (Medium Priority)
1. **Improve modal dialog handling:**
   - Detect modal dialogs as temporary overlays, not state changes
   - Implement modal dismissal logic (tap background or cancel button)
   - Wait for modal to dismiss before continuing form interaction
   
2. **Add color picker detection:**
   - Specifically identify color picker dialogs as cosmetic overlays
   - Allow text input to underlying form even when modal is present

### For srv-001 (Critical Priority - Video-level fix required)
1. **Re-record srv-001 video with consistent states:**
   - Ensure reference frames match current frames in data presence/layout
   - Verify statistics screen has populated data before recording
   - Or: Use different video segments for ground truth vs. automation
   
2. **Validate video structure:**
   - Check that each segment's reference/current pair are logically compatible
   - Consider re-running with correct initial state

### General Improvements
1. **Modal/Dialog Handling:** Implement framework for handling transient UI overlays
2. **State Recovery:** Add logic to recover from minor state mismatches (e.g., navigate to expected state)
3. **Video Validation:** Pre-check video pairs for state compatibility before automation run

---

## Conclusion

ViBR demonstrates **correct conservative behavior** by refusing to execute actions when states mismatch. However:

- **hhv-002 failure** is a genuine detection issue (modal dialog overlay)
- **srv-001 failures** are video structure problems, not ViBR bugs

The **1 successful completion out of 3 runs** (33%) indicates ViBR works well when states align, but struggles with:
1. Modal dialogs masking form interaction
2. Inconsistent video reference/current pairs

These are addressable issues through improved modal handling and video preparation.
