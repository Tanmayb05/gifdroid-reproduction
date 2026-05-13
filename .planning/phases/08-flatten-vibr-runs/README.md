# Phase 8 Planning Summary

## Phase: Apply Flattened Run Directory Structure to src_ViBR

**Status:** Planned ✓  
**Created:** 2026-05-12  
**Complexity:** Medium  

---

## Quick Overview

src_ViBR currently uses nested directories like `apps/{app}/llm/ViBR_gemini/handheld/run-001/`.

Phase 8 applies the same flat structure implemented in src_llm: `apps/{app}/llm/{video-name}-{model}/run-001/`

This improves consistency and makes run directories immediately identifiable.

---

## What Gets Changed

| Component | Current | Target |
|-----------|---------|--------|
| Directory structure | Deep nesting with variant dirs | Flat: `{video-name}-{model}` |
| Path logic | `ViBR_llm` + source detection | Direct model name + video name |
| Helpers | Minimal path utilities | _extract_video_name(), _normalize_model_slug() |
| create_output_layout() | Takes `llm`, `source` params | Takes `video_path`, `llm_model` params |

---

## Execution Plan

**5 waves of work:**

1. **Helper Functions (1.1-1.3)** → Add path utilities, refactor create_output_layout()
2. **Call Site Updates (2.1-2.2)** → Update main.py and approach modules
3. **Testing (3.1-3.2)** → Unit tests for path logic + integration test
4. **Documentation (4.1-4.2)** → Update README and create migration notes
5. **Validation (5.1-5.2)** → Run test suite, verify config parsing

**Estimated effort:** 6-8 hours  
**Risk level:** Medium (path structure changes, but well-tested)

---

## Key Design Decisions

1. **No migration of existing runs** — Phase 8 only affects future runs
2. **Consistent with src_llm** — Reuse same helper function patterns
3. **Video name extracted from config** — Uses Path.stem() on video_path
4. **Model normalization** — Standardizes names with lowercase + hyphens
5. **No -vm suffix for ViBR** — ViBR doesn't have video_mode concept (unlike src_llm)

---

## Files Modified

```
src_ViBR/io_utils.py          ← Refactored (helper functions + create_output_layout)
src_ViBR/main.py              ← Updated call sites
src_ViBR/config.py            ← Minimal changes (config already has llm_model)
tests/test_vibr_io_utils.py   ← New tests
tests/test_vibr_integration.py ← New tests
src_ViBR/README.md            ← Documentation update
docs/VIBR_MIGRATION.md        ← New migration guide
```

---

## Next Steps

Review the full plan: `cat .planning/phases/08-flatten-vibr-runs/PLAN.md`

When ready to execute:

```bash
/gsd:execute-phase 8
```

---

## Questions?

- Review specific tasks in PLAN.md for implementation details
- Reference src_llm/io_utils.py for pattern examples
- Check existing ViBR tests for mocking patterns
