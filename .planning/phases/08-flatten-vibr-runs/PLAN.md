---
phase: 8
title: Apply Flattened Run Directory Structure to src_ViBR
goal: Update src_ViBR codebase to use the same flattened directory structure as src_llm (video-name-model-vm format)
created: 2026-05-12
---

# Phase 8: Apply Flattened Run Directory Structure to src_ViBR

## Overview

src_ViBR currently uses the old nested directory structure: `apps/{app}/llm/{variant_dir}/{source}/run-NNN/`

Phase 8 aligns src_ViBR with the flattened structure already implemented in src_llm: `apps/{app}/llm/{video-name}-{model}{-vm}/run-NNN/`

This improves consistency across the codebase and makes run directories immediately identifiable.

---

## Requirements Mapping

- [R8.1] Update src_ViBR/io_utils.py with new flat naming convention
- [R8.2] Extract video name from config and construct paths like `{video-name}-{model}-{vm?}/run-NNN/`
- [R8.3] Update src_ViBR/config.py to support video_file field
- [R8.4] Add helper functions: _extract_video_name(), path normalization
- [R8.5] Update create_output_layout() to match src_llm pattern
- [R8.6] Unit tests for path construction logic
- [R8.7] Integration test with actual run to verify new structure

---

## Wave 1: Code Refactoring (Parallel)

### Task 1.1: Add Helper Functions to io_utils.py

**File:** `src_ViBR/io_utils.py`

**Changes:**
1. Add `_extract_video_name(video_path: Path | str) -> str` — extract stem from video path
2. Add `_normalize_model_slug(model_str: str) -> str` — normalize model name (lowercase, hyphens)
3. Update `detect_video_source()` to work with the new flat structure (already identifies hhv/srv prefix)

**Reference from src_llm:**
```python
def _normalize_model_slug(model_str: str) -> str:
    """Normalize model name to lowercase with hyphens and dots.
    e.g., 'Gemini-2.5-Pro' -> 'gemini-2.5-pro'
    """
    normalized = re.sub(r"[^a-z0-9.-]+", "-", model_str.lower()).strip("-")
    return normalized if normalized else "model"

def _extract_video_name(video_path: Path | str) -> str:
    """Extract video name without extension (e.g., 'hhv-002.mp4' -> 'hhv-002')."""
    return Path(video_path).stem
```

**Dependencies:** None
**Complexity:** Low — direct port from src_llm

---

### Task 1.2: Update create_output_layout() in io_utils.py

**File:** `src_ViBR/io_utils.py`

**Changes:**
1. Refactor `create_output_layout()` signature and implementation
2. Extract video name from `video_path` using `_extract_video_name()`
3. Normalize model name using `_normalize_model_slug()`
4. Build flat directory name: `{video-name}-{model}` (no -vm suffix for ViBR since it's not video_mode)
5. Update path construction to: `apps/{app}/llm/{flat_dir}/run-NNN/`
6. Keep `detect_video_source()` for internal use (returns "handheld" or "screenrec")
7. Update docstring to reflect new structure

**Current signature:**
```python
def create_output_layout(project_root: Path, app_name: str, llm: str, source: str, run_dt: datetime) -> OutputLayout:
```

**New signature:**
```python
def create_output_layout(project_root: Path, app_name: str, video_path: Path, llm_model: str, run_dt: datetime) -> OutputLayout:
```

**Example transformation:**
- Old: `apps/binaryeye/llm/ViBR_gemini/handheld/run-001/`
- New: `apps/binaryeye/llm/hhv-001-gemini-2-5-pro/run-001/`

**Dependencies:** Task 1.1 (needs helper functions)
**Complexity:** Medium — signature change requires updating all callers

---

### Task 1.3: Update src_ViBR/config.py

**File:** `src_ViBR/config.py`

**Changes:**
1. Add `llm_model: str` field to `ViBRRunConfig` dataclass (normalize model name including version)
2. Update config parsing to extract and validate `llm_model` from YAML
3. Ensure `video_path` remains accessible (already in dataclass)
4. Update docstring/comments to reflect the new flat structure

**Current ViBRRunConfig:**
```python
@dataclass(frozen=True)
class ViBRRunConfig:
    app_name: str
    video_path: Path
    algorithm: str
    llm: str
    llm_model: str  # ← already exists
```

**Note:** `llm_model` already exists in config, so primary change is updating create_output_layout() callers to pass it.

**Dependencies:** None (config already has needed fields)
**Complexity:** Low — minimal changes

---

## Wave 2: Update Call Sites

### Task 2.1: Update src_ViBR/main.py Calls to create_output_layout()

**File:** `src_ViBR/main.py`

**Changes:**
1. Find all calls to `create_output_layout()` (likely in main function)
2. Replace old signature:
   ```python
   source = detect_video_source(run.video_path)
   layout = create_output_layout(project_root, run.app_name, run.llm, source, run_dt)
   ```
3. With new signature:
   ```python
   layout = create_output_layout(project_root, run.app_name, run.video_path, run.llm_model, run_dt)
   ```

**Dependencies:** Task 1.2 (needs updated create_output_layout)
**Complexity:** Medium — find and update all call sites

---

### Task 2.2: Update Other References to Old Path Structure

**Files:** src_ViBR/main.py, src_ViBR/approach/*.py (if any direct path construction)

**Changes:**
1. Search for any hardcoded path patterns or assumptions about the old `ViBR_*` variant directory
2. Remove or update any path normalization logic specific to old structure
3. Verify logging/output doesn't reference hardcoded path components

**Dependencies:** Task 1.2
**Complexity:** Low-Medium — depends on how many files reference paths

---

## Wave 3: Testing

### Task 3.1: Unit Tests for Path Construction

**File:** Create `tests/test_vibr_io_utils.py` (or add to existing test file)

**Test cases:**
1. `test_extract_video_name()` — verify extraction of video name:
   - Input: "hhv-002.mp4" → Output: "hhv-002"
   - Input: "srv-001.mp4" → Output: "srv-001"
   - Input: Path("hhv-003.mp4") → Output: "hhv-003"

2. `test_normalize_model_slug()` — verify model normalization:
   - Input: "gemini-2.5-pro" → Output: "gemini-2-5-pro"
   - Input: "GPT-4o" → Output: "gpt-4o"
   - Input: "Gemini 2.5 Pro" → Output: "gemini-2-5-pro"

3. `test_create_output_layout_flat_path()` — verify full path construction:
   - Verify path format: `apps/{app}/llm/{video-name}-{model}/run-001/`
   - Verify run ID increments correctly
   - Verify logs subdirectory is created correctly
   - Verify metadata_path is under run_dir

4. `test_create_output_layout_run_id_increment()` — verify run ID counter:
   - Create run-001, verify next is run-002
   - Handle existing run directories correctly

**Dependencies:** Task 1.1, 1.2
**Complexity:** Medium — integration with Path/filesystem

---

### Task 3.2: Integration Test

**File:** Create `tests/test_vibr_integration.py` or add to existing integration tests

**Test:**
1. Create a minimal test config with a video file
2. Call create_output_layout() with test app name, video path, model
3. Verify:
   - Directory structure matches flat naming convention
   - All required subdirectories created (logs, artifacts if applicable)
   - metadata.json path is correct
   - Run ID is run-001 (fresh directory)

**Dependencies:** Task 1.2, 3.1
**Complexity:** Medium — requires test fixtures/mocking

---

## Wave 4: Documentation & Validation

### Task 4.1: Update src_ViBR/README.md

**File:** `src_ViBR/README.md` (if exists)

**Changes:**
1. Update "Directory Structure" section with new flat format
2. Update examples showing old vs new paths
3. Add note about migration date (2026-05-12)
4. Update any command-line examples that reference paths

**Example:**
```
## Output Directory Structure

All ViBR runs follow the flat naming convention:

apps/{app_name}/llm/{video-name}-{model}/run-NNN/
├── metadata.json
├── artifacts/
└── logs/
```

**Dependencies:** None (documentation only)
**Complexity:** Low

---

### Task 4.2: Create Migration Notes (if applicable)

**File:** Create `docs/VIBR_MIGRATION.md`

**Content:**
1. Explain the change from old to new structure
2. Note the date of migration (Phase 8, 2026-05-12)
3. Clarify that this applies to **future runs only** (existing runs not migrated in Phase 8)
4. Mention that config.py llm_model field now required in YAML

**Dependencies:** None
**Complexity:** Low

---

## Wave 5: Final Verification

### Task 5.1: Run Full Test Suite

**Command:** `pytest tests/ -v --tb=short`

**Checks:**
1. All src_ViBR tests pass
2. No regression in existing functionality
3. New path construction tests pass
4. Integration test completes successfully

**Dependencies:** Tasks 3.1, 3.2
**Complexity:** Low — automated verification

---

### Task 5.2: Verify Config Parsing

**Check:** 
1. Ensure existing ViBR YAML configs still parse correctly
2. Verify that llm_model is properly extracted and normalized
3. Test with both short names ("gemini", "openai") and full names ("gemini-2.5-pro")

**Dependencies:** Task 1.3
**Complexity:** Low

---

## Summary

| Wave | Tasks | Goal |
|------|-------|------|
| 1 | 1.1, 1.2, 1.3 | Helper functions and refactored path logic |
| 2 | 2.1, 2.2 | Update all call sites and references |
| 3 | 3.1, 3.2 | Comprehensive unit and integration testing |
| 4 | 4.1, 4.2 | Documentation updates |
| 5 | 5.1, 5.2 | Final validation and test suite pass |

**Estimated effort:** 6-8 hours
**Risk level:** Medium (affects path structure, but well-tested)
**Rollback:** Git revert if issues discovered

---

## Success Criteria

- [x] All helper functions added and tested
- [x] create_output_layout() refactored to flat structure
- [x] All call sites updated with new signature
- [x] Unit tests pass (path extraction, normalization, construction)
- [x] Integration test passes
- [x] Documentation updated
- [x] Full test suite passes (no regressions)
- [x] New runs create flat directory structure

---

## Notes

- Phase 8 **does NOT migrate existing runs** — only affects future runs
- Migration of existing ViBR runs can be a separate Phase 8.1 if needed
- The flat structure makes ViBR consistent with src_llm
- Video name + model + optional mode suffix in directory name improves discoverability
