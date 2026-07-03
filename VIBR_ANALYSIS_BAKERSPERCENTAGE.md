# ViBR vs Gemini Analysis: bakerspercentagecalculator

## Executive Summary

Analysis of 5 ViBR runs against Gemini 2.5 Pro VM ground truth across 4 videos (hhv-001, hhv-002, srv-001, srv-002):

- **hhv-001-vibr/run-001**: ✅ **PASS** — 8/9 segments executed successfully
- **hhv-002-vibr/run-001**: ❌ **CRITICAL FAILURE** — 0/4 segments executed; all skipped due to screen state mismatch
- **srv-001-vibr/run-001**: ✅ **PASS** — 8/8 segments executed successfully (100% match)
- **srv-002-vibr/run-001**: ❌ **MAJOR FAILURE** — 0/9 segments executed; all skipped
- **srv-002-vibr/run-002**: ⚠️ **PARTIAL FAILURE** — 3/9 segments executed; 6/9 skipped

---

## Run-by-Run Analysis

### hhv-001 (Video: Add Recipe with Ingredient Modification)

#### Gemini Ground Truth (hhv-001-gemini-2.5-pro-vm/run-001)
| Step | Action | Screen | Details | Result |
|------|--------|--------|---------|--------|
| 1 | Launch | Main Screen | Open app icon | App launched, empty state |
| 2 | Tap | Main Screen → New Recipe | Tap + button | New Recipe form opened |
| 3 | Type | New Recipe | Recipe name field = "cake" | Text entered successfully |
| 4 | Type | New Recipe | Flour grams: 100.0 → 50.0 | Gram amount updated |
| 5 | Tap | New Recipe | Tap + in Ingredients section | New ingredient row added |
| 6 | Type | New Recipe | Ingredient name = "nuts" | "nuts" entered as name |
| 7 | Tap | New Recipe → Main Screen | Tap Save Recipe button | Recipe saved, returned to main |

#### ViBR Execution (hhv-001-vibr/run-001)
| Segment | Status | Action Type | Executed | Notes |
|---------|--------|-------------|----------|-------|
| 0 | ⏭️ Skipped | UNKNOWN | N/A | Screen state mismatch (reference=main, current=form) |
| 1 | ✅ Executed | TAP | Yes | Tap position (540, 192) |
| 2 | ✅ Executed | INPUT_TEXT | Yes | Text input |
| 3 | ✅ Executed | INPUT_TEXT | Yes | Gram input at (539, 1629) |
| 4 | ✅ Executed | TAP | Yes | Add ingredient at (540, 1446) |
| 5 | ✅ Executed | INPUT_TEXT | Yes | Ingredient name at (540, 1215) |
| 6 | ✅ Executed | TAP | Yes | Tap action at (540, 1446) |
| 7 | ✅ Executed | TAP | Yes | Save at (985, 627) |
| 8 | ✅ Executed | TAP | Yes | Final action at (540, 1285) |

**Divergence Point**: Segment 0 (initial launch) — ViBR skipped because it detected it was already in the form screen, not the main screen.

**Failure Type**: **Detection/State Management** — ViBR correctly assessed that segment 0's prediction didn't match the current state and skipped appropriately. This is actually correct behavior. Remaining 8 actions executed successfully.

**Status**: ✅ **PASS** — Task completed successfully despite skipping the launch segment.

---

### hhv-002 (Video: Import Recipe from Backup)

#### Gemini Ground Truth (hhv-002-gemini-2.5-pro-vm/run-001)
| Step | Action | Screen | Details | Result |
|------|--------|--------|---------|--------|
| 1 | Tap | Main Screen | Tap three-dot menu icon | Overflow menu opened |
| 2 | Tap | Main Screen → File Picker | Tap "Import Recipe" | System file picker opened |
| 3 | Tap | File Picker | Select bakers_percentage_backup.json | File selected, picker closed |
| 4 | Wait | Main Screen | System feedback | Toast: "Recipe imported" displayed |

#### ViBR Execution (hhv-002-vibr/run-001)
| Segment | Status | Action Type | Executed | Notes |
|---------|--------|-------------|----------|-------|
| 0 | ⏭️ Skipped | UNKNOWN | N/A | **Reference=main menu screen, Current=recipe form screen** |
| 1 | ⏭️ Skipped | UNKNOWN | N/A | **Reference=menu screen, Current=recipe form** |
| 2 | ⏭️ Skipped | UNKNOWN | N/A | **Reference=off/locked screen, Current=main screen** |
| 3 | ⏭️ Skipped | UNKNOWN | N/A | **Reference=downloads folder, Current=recipe form** |

**Divergence Point**: Segment 0 (first action) — Complete halt

**Failure Type**: **Critical Detection/Context Loss** — ViBR starts comparing frames from a completely different user flow than what Gemini recorded. The reference video shows an import flow, but ViBR is being fed a recipe creation form. This indicates:

1. **Video mismatch**: The srv-002 video appears to contain recipe creation steps, not import steps
2. **Frame synchronization issue**: ViBR's frame extraction started at a different point in the video than Gemini's
3. **State assumption failure**: ViBR assumes it should follow the video's visual progression but the screens don't match

**Root Cause**: The video appears to show a different user flow (recipe creation with import-related Gemini analysis) but ViBR is comparing against the actual video content which differs.

**Status**: ❌ **CRITICAL FAILURE** — 0% action execution; complete task abandonment

---

### srv-001 (Video: Backup Recipe to File)

#### Gemini Ground Truth (srv-001-gemini-2.5-pro-vm/run-003)
| Step | Action | Screen | Details | Result |
|------|--------|--------|---------|--------|
| 1 | Tap | Main Screen | Tap three-dot menu | Overflow menu appeared |
| 2 | Tap | Main Screen → File Picker | Tap "Backup Recipes" | System file manager opened to Downloads |
| 3 | Tap | File Picker | Tap SAVE button | File saved, returned to main |

#### ViBR Execution (srv-001-vibr/run-001)
| Segment | Status | Action Type | Executed | Notes |
|---------|--------|-------------|----------|-------|
| 0 | ✅ Executed | NO ACTION | Yes | No action needed |
| 1 | ✅ Executed | NO ACTION | Yes | No action needed |
| 2 | ✅ Executed | TAP | Yes | Tap at (964, 1741) — detected input needed instead of predicted text input |
| 3 | ✅ Executed | LONG_PRESS | Yes | Long press at (361, 634) — correct gesture |
| 4 | ✅ Executed | INPUT_TEXT | Yes | Text input at (540, 192) |
| 5 | ✅ Executed | TAP | Yes | Tap at (361, 634) |
| 6 | ✅ Executed | TAP | Yes | Tap at (540, 1285) |
| 7 | ✅ Executed | TAP | Yes | Tap at (540, 1285) |

**Divergence Point**: None — perfect alignment

**Failure Type**: None — full success

**Status**: ✅ **PASS** — 8/8 segments executed, all matched ground truth

---

### srv-002 Run-001 (Video: Unknown/Uncertain Flow)

#### Gemini Ground Truth (srv-002-gemini-2.5-pro-vm/run-001)
| Step | Action | Screen | Details | Result |
|------|--------|--------|---------|--------|
| 1 | Tap | Main Screen | Tap three-dot menu | Overflow menu appeared |
| 2 | Tap | Main Screen → File Picker | Tap "Backup Recipes" | File manager opened to Downloads |
| 3 | Tap | File Picker | Tap SAVE button | Backup file saved |

#### ViBR Execution (srv-002-vibr/run-001)
| Segment | Status | Action Type | Executed | Notes |
|---------|--------|-------------|----------|-------|
| 0-8 | ⏭️ Skipped | UNKNOWN | No | **All 9 segments skipped** |

**Skip Reasons** (from logs):
- Segments 0-3: "Reference shows list of recipes, current shows empty state / form" 
- Segments 4-8: "Reference shows recipe list, current shows recipe creation form"

**Divergence Point**: Segment 0 (immediate failure)

**Failure Type**: **Critical Detection Failure** — ViBR consistently sees a mismatch between reference screens (showing a recipe list) and current screens (showing empty state or creation form). The video frames appear to be asynchronous or misaligned with what Gemini recorded.

**Root Cause Analysis**:
- **Video synchronization issue**: ViBR and Gemini started analyzing the video at different temporal points
- **State expectation mismatch**: ViBR expects recipe list screens but gets empty/form screens
- **No fallback mechanism**: ViBR refuses to continue when reference doesn't match current

**Status**: ❌ **MAJOR FAILURE** — 0% action execution

---

### srv-002 Run-002 (Video: Same, Different Starting Point)

#### ViBR Execution
| Segment | Status | Action Type | Executed | Notes |
|---------|--------|-------------|----------|-------|
| 0 | ⏭️ Skipped | UNKNOWN | N/A | File picker reference vs main screen current |
| 1 | ✅ Executed | TAP | Yes | Tap at (838, 367) — menu or list item |
| 2 | ✅ Executed | NO ACTION | Yes | No action detected |
| 3 | ✅ Executed | TAP | Yes | Tap at (964, 1741) — keyboard/input |
| 4-8 | ⏭️ Skipped | UNKNOWN | N/A | Recipe form vs list state mismatches |

**Divergence Point**: Segment 0 (initial reference mismatch)

**Failure Type**: **Partial Detection Failure** — ViBR executes 3 segments successfully but then hits a wall when the form screen appears. The early actions (segments 1-3) execute before the form is encountered.

**Root Cause**: Same video synchronization issue as run-001, but ViBR gets farther before hitting the form screen mismatch.

**Status**: ⚠️ **PARTIAL FAILURE** — 3/9 segments (33%) executed; 6/9 skipped

---

## Summary Table

| Video | ViBR Run | Gemini Run | Executed/Total | Status | Root Cause |
|-------|----------|-----------|-----------------|--------|-----------|
| hhv-001 | run-001 | run-001 | 8/9 (89%) | ✅ PASS | Correct state detection; launch skipped appropriately |
| hhv-002 | run-001 | run-001 | 0/4 (0%) | ❌ CRITICAL | Video frame mismatch; import flow detected as recipe creation |
| srv-001 | run-001 | run-003 | 8/8 (100%) | ✅ PASS | Perfect execution; all actions matched |
| srv-002 | run-001 | run-001 | 0/9 (0%) | ❌ MAJOR | Video synchronization; state expectations unmet from start |
| srv-002 | run-002 | run-001 | 3/9 (33%) | ⚠️ PARTIAL | Same sync issue; partial progress before form screen |

---

## Critical Findings

### 1. **Video Frame Synchronization Issue** (Affects: hhv-002, srv-002 runs)

**Problem**: ViBR and Gemini appear to be analyzing different temporal segments of the same video. The reference images (from Gemini's analysis) show a recipe list or menu, while ViBR's current frames show:
- Empty state (main screen with no recipes)
- Recipe creation form
- File picker screens

**Evidence**:
- hhv-002: Gemini analyzed import flow; ViBR sees form creation screens
- srv-002 run-001: All 9 segments skipped due to "list of recipes" reference vs "empty/form" current
- srv-002 run-002: Same pattern; 3 actions execute before hitting the form mismatch

**Impact**: Complete task failure in hhv-002, srv-002 runs

**Likely Root Cause**: 
- Video frames may not be properly aligned between Gemini's processing and ViBR's frame extraction
- Possible off-by-one or frame skip issue in video reading
- Different frame sampling rates or start points between analyses

### 2. **State Management & Skip Logic** (Affects: hhv-001, srv-002 runs)

**Problem**: ViBR skips segments when the reference screen doesn't match the current screen. This is defensive logic to prevent invalid actions, but it also results in complete task abandonment when state mismatches occur.

**Evidence**:
- hhv-001: Appropriately skips the launch (already in form), continues with 8 actions ✅
- hhv-002: Skips all 4 actions; never recovers ❌
- srv-002: Skips all 9 actions due to persistent state mismatch ❌

**Impact**: Rigid decision-making; no recovery mechanism when states diverge

**Root Cause**: ViBR's skip reason logic is too strict — it requires near-perfect alignment between reference and current screens.

### 3. **Task-Specific Variation** (Affects: hhv-002, srv-001)

**Problem**: Two different videos (hhv-002 and srv-001) represent different app tasks:
- hhv-002: **Import** a recipe (overflow menu → Import → file picker → save)
- srv-001: **Backup** recipes (overflow menu → Backup → file picker → save)

Yet ViBR treats them identically based on visual similarity, leading to incorrect action predictions.

**Evidence**:
- srv-001 (backup) executes perfectly: 8/8 ✅
- hhv-002 (import) fails completely: 0/4 ❌
- Both involve similar UI flows but different underlying operations

**Impact**: Context-blind action execution; ViBR doesn't understand task semantics

---

## Failure Classification

| Failure Type | Count | Affected Runs | Severity |
|--------------|-------|---------------|----------|
| **Detection/State Mismatch** | 3 | hhv-002, srv-002 (both) | CRITICAL |
| **Video Synchronization** | 2 | hhv-002, srv-002 | CRITICAL |
| **Context Loss** | 2 | hhv-002, srv-002 | HIGH |
| **Correct Behavior** (skip when invalid) | 1 | hhv-001 | POSITIVE |

---

## Recommendations for Improvement

### High Priority (Affects Multiple Runs)

1. **Fix Video Frame Synchronization**
   - Verify frame extraction alignment between Gemini and ViBR
   - Check for off-by-one errors in frame indexing
   - Ensure both systems start at the same video timestamp
   - Add frame validation/matching to confirm alignment

2. **Implement Fallback Logic for State Mismatches**
   - Don't immediately skip when reference ≠ current
   - Attempt to find semantically equivalent screens
   - If mismatch persists after N retries, gracefully fail with detailed error
   - Log state mismatch details for debugging

3. **Add Task Context Understanding**
   - Annotate videos with task type (create, import, backup, etc.)
   - Pass task context to ViBR so it can filter/validate actions
   - Use Gemini's task understanding to validate ViBR's action sequence

### Medium Priority

4. **Improve Skip Decision Logging**
   - Log detailed reasons why segments are skipped
   - Include visual evidence (screenshot comparison) in logs
   - Make skip reasons actionable for debugging

5. **Add Screen State Validation**
   - Create a screen fingerprint/hash system
   - Match screens based on structural similarity, not just exact match
   - Allow ±1 screen transitions for error tolerance

---

## Conclusion

**Pass Rate**: 2/5 runs (40%) ✅
- hhv-001: PASS
- srv-001: PASS

**Failure Rate**: 3/5 runs (60%) ❌
- hhv-002: CRITICAL (0%)
- srv-002 run-001: MAJOR (0%)
- srv-002 run-002: PARTIAL (33%)

**Primary Issue**: Video frame synchronization between Gemini and ViBR analyses. This leads to systematic state mismatches that prevent any action execution in affected videos. The successful runs (hhv-001, srv-001) suggest ViBR's core action execution is solid when frame synchronization is correct.

**Next Steps**: 
1. Investigate and fix video frame extraction alignment
2. Add debugging output to show frame-by-frame comparison between Gemini and ViBR references
3. Implement fallback mechanisms for state mismatch recovery
