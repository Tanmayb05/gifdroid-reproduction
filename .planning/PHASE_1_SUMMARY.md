# Phase 1: Foundation & Configuration - Completed ✅

## Overview
Established flat directory structure and extended AppConfig to support video_mode flag, enabling the two-stage pipeline architecture.

## Requirements Delivered

### R1.1: Flat Directory Structure ✅
- **Before**: `apps/<app>/llm/<provider>/<model>/<source>/<cfg_slug>/run-NNN/`
- **After**: `apps/<app>/llm/<model>/<source>{-video-mode}/run-NNN/`
- Provider directory removed (info embedded in model name)
- Significantly flattens output hierarchy

### R1.2: Model Names Include Provider ✅
- **Implementation**: Model slugs now include provider information
- **Example**: `gemini-2.5-pro` (was `gemini` + `2.5-pro` split)
- **Normalization**: `_normalize_model_slug()` converts any format to lowercase with dots/hyphens
  - `Gemini-2.5-Pro` → `gemini-2.5-pro`
  - `GEMINI_2_5_PRO` → `gemini-2-5-pro`
  - `gemini-2.5-pro` → `gemini-2.5-pro`

### R1.3: video_mode Flag in AppConfig ✅
- **Default**: `video_mode=True` (Stage 1 optimized)
- **Location**: `src_llm/config.py::AppConfig.video_mode`
- **YAML Override**: `video_mode: false` enables keyframe mode
- **Validation**: Only gemini provider supports video_mode=true

### R1.4: Dry-run Directory Handling ✅
- **Single Directory**: `apps/<app>/llm/<model>/<source>{-video-mode}/dry-run/`
- **Behavior**: Overwritten on each dry-run (no versioning)
- **Separation**: Dry-run isolated from numbered runs (run-001, run-002, etc.)
- **is_dry_run Field**: Added to OutputLayout to track dry-run status

## Files Modified

### src_llm/config.py
- Changed `AppConfig.video_mode` default from `False` to `True`
- Updated `load_config()` default for video_mode from `False` to `True`

### src_llm/io_utils.py
- **Added**: `_normalize_model_slug()` utility function
- **Enhanced**: `OutputLayout` with `is_dry_run: bool = False` field
- **Refactored**: `create_output_layout()` function:
  - Added `is_dry_run: bool = False` parameter
  - Flat directory structure logic (no provider directory)
  - Support for `-video-mode` suffix in source_dir
  - Dry-run special handling (single directory, not numbered)
- **Enhanced**: `write_run_metadata()` function:
  - Optional `frame_sampling_cfg` and `keyframe_selection_cfg` (None for video_mode)
  - New parameters: `memory_md_content`, `task_description`, `ui_elements`, `completion_criteria`
  - Conditional metadata: video_mode metadata only when provided

### src_llm/main.py
- **Import**: Added `_normalize_model_slug` from io_utils
- **Updated**: `run_single()` to pass `is_dry_run=args.dry_run` to create_output_layout
- **Updated**: write_run_metadata call to:
  - Use `_normalize_model_slug()` instead of inline regex
  - Pass `None` for frame_sampling_cfg and keyframe_selection_cfg in video_mode
  - (Stub for future: memory metadata fields)

## Directory Structure Examples

### Video Mode (video_mode=true)
```
apps/adaway/llm/gemini-2.5-pro/screenrec-video-mode/
├── run-001/          (Stage 1 output)
│   ├── memory.md
│   ├── metadata.json (with video_mode_metadata)
│   ├── llm_raw_response.txt
│   └── logs/
│
├── run-002/          (Stage 2 output, auto-created)
│   ├── session_trace.json
│   ├── step_*.png
│   └── logs/
│
└── dry-run/          (Single dry-run directory, overwritten)
    ├── metadata.json
    └── logs/
```

### Keyframe Mode (video_mode=false)
```
apps/adaway/llm/gemini-2.5-pro/screenrec/
├── run-001/          (Contains sampling/selection config)
│   ├── execution_trace.json
│   ├── frames_manifest.json
│   ├── keyframes/
│   ├── metadata.json
│   └── logs/
│
└── dry-run/
    ├── metadata.json
    └── logs/
```

## Testing

### Unit Tests Passed
```
✓ Model slug normalization: Gemini-2.5-Pro → gemini-2.5-pro
✓ Flat structure (video_mode=true): apps/adaway/llm/gemini-2.5-pro/screenrec-video-mode/run-001
✓ Dry-run structure: apps/adaway/llm/gemini-2.5-pro/screenrec-video-mode/dry-run
✓ Keyframe mode structure: apps/adaway/llm/gemini-2.5-pro/screenrec/run-001
✓ Handheld video type: handheld-video-mode suffix applied correctly
```

### Integration
- All imports successful
- No breaking changes to existing API (backward compatible with keyframe mode)
- AppConfig properly defaults video_mode=true

## Next Phase (Phase 2)

Phase 2 will build on this foundation:
- **I/O & Output Layout Refactoring**
- Implement memory.md generation from video analysis
- Extend metadata.json to embed memory content
- Prepare for Stage 2 memory consumption

## Key Design Decisions

1. **Video mode as default** (video_mode=True): Aligns with two-stage optimization goals
2. **Flat directory structure**: Simplifies path logic and reduces nesting depth
3. **Single dry-run directory**: Avoids accumulation of test runs
4. **Provider in model name**: Eliminates redundant directory level
5. **Backward compatible**: Keyframe mode still works with video_mode=false

## Technical Notes

- Model slug normalization preserves dots (e.g., 2.5) which are common in version numbers
- `is_dry_run` field allows downstream code to distinguish dry-run vs actual runs
- Metadata structure designed to be consumed by Stage 2 (automate.py) without file lookups
- Config loading validates video_mode only with supported providers (gemini)
