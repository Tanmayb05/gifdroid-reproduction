# Flat Video Structure Migration

## Summary
Updated all code in `src_llm` and `src_ViBR` to use a flat video directory structure instead of nested subdirectories.

### Old Structure
```
apps/<app_name>/videos/
├── handheld/
│   ├── hhv-001.mp4
│   └── hhv-002.mp4
└── screenrec/
    ├── srv-001.mp4
    └── srv-002.mp4
```

### New Structure
```
apps/<app_name>/videos/
├── hhv-001.mp4
├── hhv-002.mp4
├── srv-001.mp4
└── srv-002.mp4
```

## Changes Made

### src_llm/config.py
- Renamed `_VIDEO_TYPE_ALIASES` → `_VIDEO_TYPE_MAP` (simpler mapping without aliases)
- Updated `_resolve_video_type()` to infer type from filename prefix (srv/hhv) instead of directory names
- Modified `_build_run_configs()` to generate flat video paths:
  - Shorthand `"srv"` → `apps/{app_name}/videos/srv-001.mp4`
  - Shorthand `"hhv"` → `apps/{app_name}/videos/hhv-001.mp4`
  - Full paths are resolved directly
- Updated docstrings and comments

### src_llm/io_utils.py
- Updated `detect_video_type()` to detect type from filename prefix instead of directory path
- Updated `resolve_video_path()` to construct flat paths:
  - Shorthand `"hhv"` → `apps/{app_name}/videos/hhv-001.mp4`
  - Shorthand `"srv"` → `apps/{app_name}/videos/srv-001.mp4`
  - Explicit paths are resolved with flat structure in mind

### src_ViBR/config.py
- Removed `VIDEO_TYPE_ALIASES` (no longer needed)
- Updated `_expand_video_path()` to build flat paths:
  - Shorthand `"hhv"` → `apps/{app_name}/videos/hhv-001.mp4`
  - Shorthand `"srv"` → `apps/{app_name}/videos/srv-001.mp4`

### src_ViBR/io_utils.py
- Updated `detect_video_source()` to infer source from filename prefix instead of directory path

## Video Type Detection
The code now determines video type (handheld/screenrec) by examining the **filename prefix**:
- `hhv` prefix → handheld videos
- `srv` prefix → screen recording videos

This works for filenames like:
- `hhv-001.mp4`
- `hhv_001.mp4`
- `srv-002.mp4`
- `srv_001.mp4`
- Any filename starting with `hhv` or `srv`

## Config Examples
The example config files already use the correct format:
- `src_llm/config.example.yml` - uses explicit paths (e.g., `apps/adaway/videos/adaway_utg01.mp4`)
- `src_ViBR/input/config.example.yml` - uses shorthands (e.g., `"hhv"`, `"srv"`)

Both will now work with the flat directory structure.

## Files Modified
1. `src_llm/config.py`
2. `src_llm/io_utils.py`
3. `src_ViBR/config.py`
4. `src_ViBR/io_utils.py`

All files have been syntax-validated and are ready to use.
