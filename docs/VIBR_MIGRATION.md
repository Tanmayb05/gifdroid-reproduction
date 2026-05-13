# ViBR Run Directory Migration: Flat Structure (Phase 8)

## Summary

Phase 8 (2026-05-12) replaced the old nested run directory structure used by `src_ViBR` with a flat,
self-describing format that matches the convention already used by `src_llm`.

---

## What Changed

### Old structure (retired 2026-05-12)

```
apps/<app_name>/llm/ViBR_<algo>/<source>/run-NNN/
```

Example:

```
apps/binaryeye/llm/ViBR_gemini/handheld/run-001/
apps/binaryeye/llm/ViBR_gemini/screenrec/run-001/
```

Components:
- `ViBR_<algo>` — hard-coded prefix plus algorithm name
- `<source>` — video source inferred at runtime (`handheld` or `screenrec`)

### New structure (active from 2026-05-12)

```
apps/<app_name>/llm/<video-name>-<model>-vibr/run-NNN/
```

Example:

```
apps/binaryeye/llm/hhv-001-gemini-2.5-pro-vibr/run-001/
apps/binaryeye/llm/srv-003-gpt-4o-vibr/run-001/
```

Components:
- `<video-name>` — stem of the `video_path` value in `config.yml` (e.g. `hhv-001`, `srv-003`)
- `<model>` — normalized `llm_model` from `config.yml` (lowercase, special characters replaced by hyphens)
- `-vibr` — suffix indicating this is a ViBR run (vs. `-llm` for src_llm runs)
- `run-NNN` — zero-padded run counter, auto-incremented per variant directory

---

## Scope

**This change applies to future runs only.**

Existing run directories stored in the old format are NOT migrated or renamed by Phase 8.
If migration of historical runs is needed, it can be handled in a separate phase.

---

## Config Requirements

The `llm_model` field in `config.yml` is now used to construct the output directory name.
Ensure every run block in your config includes a fully-qualified model identifier:

```yaml
runs:
  - app_name: binaryeye
    video_path: hhv-001
    algorithm: clip
    llm: gemini
    llm_model: gemini-2.5-pro   # required — used in directory name
```

Short aliases (`gemini`, `openai`) still work for provider selection but result in less descriptive
directory names (e.g. `hhv-001-gemini/run-001/`). Use the full model slug for clarity.

---

## Implementation Notes

Changes made in Phase 8:

| File | Change |
|------|--------|
| `src_ViBR/io_utils.py` | Added `_extract_video_name()`, `_normalize_model_slug()`; refactored `create_output_layout()` signature and path logic |
| `src_ViBR/main.py` | Updated all `create_output_layout()` call sites to pass `video_path` and `llm_model` instead of `source` and `llm` |
| `src_ViBR/config.py` | Confirmed `llm_model` field is present and forwarded to layout creation |
| `src_ViBR/README.md` | Updated output path documentation and examples |
| `tests/test_vibr_io_utils.py` | Unit tests for helper functions and path construction |
| `tests/test_vibr_integration.py` | Integration test verifying end-to-end flat path creation |

---

## Consistency with src_llm

`src_llm` adopted the flat `<video-name>-<model>[-vm]-llm` convention in an earlier phase.
Phase 8 brings `src_ViBR` into alignment using `-vibr` suffix to distinguish from `-llm`:

- **src_llm runs:** `<video-name>-<model>[-vm]-llm/run-NNN/`
- **src_ViBR runs:** `<video-name>-<model>-vibr/run-NNN/`

The `-vibr` suffix makes it immediately clear which subsystem generated each run directory.
