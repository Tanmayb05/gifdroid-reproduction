---
phase: 8
plan: 1
subsystem: src_ViBR
tags: [io_utils, config, refactor, flat-paths]
dependency_graph:
  requires: []
  provides: [flat-vibr-run-dirs]
  affects: [src_ViBR/io_utils.py, src_ViBR/config.py, src_ViBR/main.py]
tech_stack:
  added: []
  patterns: [flat-directory-naming, video-name-model-slug]
key_files:
  modified:
    - src_ViBR/io_utils.py
    - src_ViBR/config.py
    - src_ViBR/main.py
decisions:
  - "Dots in model version numbers are preserved in slug (e.g., gemini-2.5-pro stays as-is)"
  - "main.py call site updated as deviation Rule 3 (blocking fix)"
metrics:
  duration: ~10 min
  completed: 2026-05-12
  tasks: 3
  files: 3
---

# Phase 8 Plan 1: Apply Flattened Run Directory Structure to src_ViBR (Wave 1) Summary

**One-liner:** Helper functions _extract_video_name/_normalize_model_slug ported from src_llm; create_output_layout() refactored to flat `{video-name}-{model}/run-NNN/` convention.

## Tasks Completed

| Task | Name | Commit | Files |
|------|------|--------|-------|
| 1.1 | Add helper functions to io_utils.py | 85731d1 | src_ViBR/io_utils.py |
| 1.2 | Refactor create_output_layout() | 16a9822 | src_ViBR/io_utils.py, src_ViBR/main.py |
| 1.3 | Verify and document config.py llm_model | 56aca54 | src_ViBR/config.py |

## Changes Made

### Task 1.1 — Helper Functions

Added to `src_ViBR/io_utils.py`:
- `_extract_video_name(video_path)` — returns `Path(video_path).stem`
- `_normalize_model_slug(model_str)` — lowercase + hyphenate; preserves dots and hyphens in version strings

### Task 1.2 — create_output_layout() Refactored

**Old signature:** `create_output_layout(project_root, app_name, llm, source, run_dt)`
**New signature:** `create_output_layout(project_root, app_name, video_path, llm_model, run_dt)`

Old path: `apps/{app}/llm/ViBR_{llm}/{source}/run-NNN/`
New path: `apps/{app}/llm/{video-name}-{model}/run-NNN/`

Example: `apps/binaryeye/llm/hhv-001-gemini-2.5-pro/run-001/`

### Task 1.3 — config.py

`llm_model` field was already present in `ViBRRunConfig`. Added docstring documenting the flat naming convention and a clarifying inline comment.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 3 - Blocking] Updated main.py call site to use new create_output_layout() signature**
- **Found during:** Task 1.2
- **Issue:** main.py called `create_output_layout(project_root, run_cfg.app_name, run_cfg.llm, source, run_dt)` which would break at runtime with the new signature
- **Fix:** Updated to `create_output_layout(project_root, run_cfg.app_name, resolved_video, run_cfg.llm_model, run_dt)`
- **Files modified:** src_ViBR/main.py
- **Commit:** 16a9822

## Self-Check: PASSED

- src_ViBR/io_utils.py: FOUND
- src_ViBR/config.py: FOUND
- src_ViBR/main.py: FOUND
- commit 85731d1: FOUND
- commit 16a9822: FOUND
- commit 56aca54: FOUND
