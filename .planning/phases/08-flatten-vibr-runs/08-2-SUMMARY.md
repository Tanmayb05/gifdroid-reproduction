---
phase: 08-flatten-vibr-runs
plan: 2
subsystem: src_ViBR
tags: [io_utils, main, refactor, flat-paths, call-sites]
dependency_graph:
  requires:
    - phase: 08-flatten-vibr-runs
      provides: [flat-vibr-run-dirs, helper-functions, updated-create_output_layout]
  provides:
    - verified-all-call-sites-updated
    - no-old-ViBR_-path-patterns-in-python-code
  affects: [src_ViBR/main.py]
tech_stack:
  added: []
  patterns: [flat-directory-naming]
key_files:
  created: []
  modified:
    - src_ViBR/main.py
key-decisions:
  - "detect_video_source() retained — still used for metadata.source field (not path construction)"
  - "Task 2.1 was already completed in Wave 1 as deviation Rule 3; Wave 2 confirmed no further changes needed"
patterns-established:
  - "source variable passed only to metadata dict, never to path construction"
requirements-completed: []
duration: ~5 min
completed: 2026-05-12
---

# Phase 8 Plan 2: Update Call Sites (Wave 2) Summary

**All src_ViBR call sites verified fully updated; no ViBR_* path patterns remain in any Python source file.**

## Performance

- **Duration:** ~5 min
- **Started:** 2026-05-12
- **Completed:** 2026-05-12
- **Tasks:** 2
- **Files modified:** 0 (verification only — Wave 1 had already completed all changes)

## Accomplishments

- Confirmed main.py uses new `create_output_layout(project_root, app_name, video_path, llm_model, run_dt)` signature (line 89)
- Confirmed no Python file under src_ViBR/ contains `ViBR_` path patterns
- Confirmed approach/*.py has zero path construction or `create_output_layout` calls — no updates needed there
- `detect_video_source()` confirmed as still valid: used only for metadata.source field, not path construction

## Task Commits

Tasks 2.1 and 2.2 required no code changes — all work was completed in Wave 1 (commit 16a9822).

No additional per-task commits issued (verified-only tasks).

**Plan metadata:** (see final docs commit)

## Files Created/Modified

None — verification pass only.

## Decisions Made

- `detect_video_source()` is still imported and called in main.py. This is intentional: it populates the `"source"` key in `metadata.json` for observability/analysis purposes. It is NOT used in path construction anymore — that changed in Wave 1.

## Deviations from Plan

None — plan executed exactly as written. Wave 1 had proactively completed the call-site update (main.py) as deviation Rule 3. Wave 2 confirmed completeness.

## Issues Encountered

None.

## User Setup Required

None — no external service configuration required.

## Next Phase Readiness

- All src_ViBR Python code now uses flat `{video-name}-{model}/run-NNN/` path structure
- Wave 3 (testing) can proceed: unit tests for `_extract_video_name`, `_normalize_model_slug`, and `create_output_layout`
- No blockers

## Self-Check: PASSED

- src_ViBR/main.py: call site on line 89 confirmed correct
- No ViBR_ pattern in any .py file: confirmed by grep returning empty
- approach/*.py: confirmed no path construction calls

---
*Phase: 08-flatten-vibr-runs*
*Completed: 2026-05-12*
