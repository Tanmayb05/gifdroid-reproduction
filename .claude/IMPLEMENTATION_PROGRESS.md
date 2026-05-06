# Two-Stage LLM Workflow Implementation Progress

## Summary
Started implementation of two-stage LLM workflow: video analysis → device automation without redundant video re-analysis.

## Completed (✓)

### 1. **config.py** — Standardized model naming & directory structure
- ✓ Added `_normalize_model_slug()` function to normalize model names (e.g., "gemini-2.5-pro")
- ✓ Updated default `llm_model` for gemini to "gemini-2.5-pro" (was "gemini-1.5-flash")
- ✓ Changed default `video_mode` to `True` (was `False`)
- ✓ Applied model normalization in both `_parse_shared()` and `load_automation_config()`
- ✓ All gemini models now use hyphen notation for consistency

### 2. **io_utils.py** — Flat directory structure & enhanced metadata
- ✓ `_normalize_model_slug()` function for model slug normalization
- ✓ `OutputLayout` dataclass already includes `is_dry_run` field
- ✓ `create_output_layout()` updated to:
  - Accept `is_dry_run` parameter
  - Create flat structure: `apps/<app>/llm/<model>/<source>-video-mode/run-NNN/`
  - Single `dry-run/` directory that overwrites on each dry-run
  - No provider directory level (model name contains provider)
- ✓ `write_run_metadata()` enhanced to support:
  - `memory_md_content`: Full memory markdown from Stage 1
  - `task_description`: Parsed from memory.md
  - `ui_elements`: Parsed from memory.md
  - `completion_criteria`: Parsed from memory.md
  - Optional `frame_sampling_cfg` and `keyframe_selection_cfg` (None for video_mode)

### 3. **video_to_memory.py** (Stage 1) — Created from main.py
- ✓ Copied and renamed `src_llm/main.py` → `src_llm/video_to_memory.py`
- ✓ Updated docstrings and module names (src_llm → video_to_memory)
- ✓ Imported `_normalize_model_slug` from io_utils
- ✓ `_parse_memory_md()` function handles both memory formats:
  1. YAML header format (current Gemini format with goal/outcome)
  2. Markdown header format (# Task Summary, ## UI Elements, etc.)
- ✓ Integrated with `create_output_layout(..., is_dry_run=args.dry_run)`
- ✓ Updated `write_run_metadata()` call to include video_mode_metadata fields
- ✓ Syntax validated ✓

### 4. **memory_to_device.py** (Stage 2) — Created from automate.py
- ✓ Copied and renamed `src_llm/automate.py` → `src_llm/memory_to_device.py`
- ✓ Updated docstrings: "memory-guided" instead of "video-guided"
- ✓ Added helper functions:
  - `_normalize_model_slug()`: Normalize model names
  - `_locate_latest_run()`: Find latest Stage 1 run for app+model+video_type
  - `_load_run_metadata()`: Load metadata.json from Stage 1 run
- ✓ `_resolve_output_dir()` updated for flat structure
- ✓ Config file changed from `automation_config.yml` → `config.yml` (unified config)
- ✓ Syntax validated ✓

### 5. **end_to_end.py** — Created orchestrator for both stages
- ✓ New module `src_llm/end_to_end.py`
- ✓ Orchestrates Stage 1 (video_to_memory) → Stage 2 (memory_to_device)
- ✓ Command-line interface:
  - `--stage 1|2|all` to run specific stages
  - `--config` for unified config file
  - `--env-file` for credentials
  - `--dry-run` for validation
- ✓ Logging output shows stage progress
- ✓ Returns appropriate exit codes
- ✓ Syntax validated ✓

### 6. **Module Structure Verified**
- ✓ All three new modules syntax check passed
- ✓ No import errors (yaml not installed in test env, but syntax OK)
- ✓ File layout correct:
  ```
  src_llm/
  ├── main.py (original, still present)
  ├── automate.py (original, still present)
  ├── video_to_memory.py (NEW: Stage 1)
  ├── memory_to_device.py (NEW: Stage 2)
  ├── end_to_end.py (NEW: Orchestrator)
  ├── config.py (UPDATED: model normalization)
  ├── io_utils.py (UPDATED: flat structure)
  └── ...
  ```

## Pending (⏳)

### 1. **providers.py** — Add memory inference
- [ ] Add abstract `infer_memory_from_video(video_path: Path) -> str` to `BaseLLMProvider`
- [ ] Implement in `GeminiProvider`:
  - Extract keyframes from video
  - Build analysis prompt asking for task summary, steps, UI elements, completion criteria
  - Format response as structured markdown
  - Return memory.md content

### 2. **automation.py** — Add memory context support
- [ ] Update `run_automation()` signature to accept `memory_content: str | None`
- [ ] Pass memory to provider's `decide_next_action()` method
- [ ] Inject memory as system prompt context in LLM calls
- [ ] Ensures at each step, LLM has access to task context from Stage 1

### 3. **Integration & Testing**
- [ ] Test video_to_memory.py: generate memory.md from sample video
- [ ] Test memory_to_device.py: locate and use memory from prior run
- [ ] Test end_to_end.py: run both stages in sequence
- [ ] Verify flat directory structure creation
- [ ] Verify metadata.json includes video_mode_metadata
- [ ] Verify dry-run creates/overwrites single dry-run/ directory

## Key Design Decisions Made

1. **Unified Config**: Both stages read from single `src_llm/input/config.yml`
   - main.py reads: llm, llm_model, video_mode, frame_sampling, keyframe_selection, runs
   - automate.py reads: llm, llm_model, device_serial, max_steps, etc., runs
   - Single config file minimizes duplication

2. **Model Slug Normalization**: 
   - All provider models normalized to hyphens, lowercase
   - "gemini-2.5-pro", "gemini-2-flash", etc.
   - Consistent across config parsing and directory structures

3. **Flat Directory Structure**:
   - No provider directory level (model name includes provider)
   - Example: `apps/adaway/llm/gemini-2.5-pro/screenrec-video-mode/run-001/`
   - Simpler paths, easier to navigate

4. **Single Dry-Run Directory**:
   - Always `dry-run/`, overwrites each time (not `dry-run-001`, `dry-run-002`, etc.)
   - Keeps directory structure clean, test runs don't clutter

5. **Memory in metadata.json**:
   - Full memory.md content stored in metadata.json under `video_mode_metadata`
   - Stage 2 doesn't need separate file lookup, just reads metadata
   - All context for automation in one place

6. **Semantic Module Names**:
   - `video_to_memory`: Stage 1, clear intent
   - `memory_to_device`: Stage 2, clear intent
   - `end_to_end`: Orchestrator, clear purpose

## Files Modified/Created

```
Modified:
- src_llm/config.py
- src_llm/io_utils.py

Created:
- src_llm/video_to_memory.py (from main.py)
- src_llm/memory_to_device.py (from automate.py)
- src_llm/end_to_end.py (new orchestrator)

Original files still present:
- src_llm/main.py
- src_llm/automate.py
```

## Next Steps

1. Implement `infer_memory_from_video()` in GeminiProvider
2. Update `automation.py` to pass memory context to LLM
3. Test end-to-end workflow with sample app
4. Verify directory structure and file outputs
5. Run integration tests to confirm Stage 1 → Stage 2 flow works

## Commands for Testing (when dependencies available)

```bash
# Stage 1 only
python -m src_llm.video_to_memory --config src_llm/input/config.yml --env-file .env.local

# Stage 2 only
python -m src_llm.memory_to_device --config src_llm/input/config.yml --env-file .env.local

# Both stages in sequence
python -m src_llm.end_to_end --config src_llm/input/config.yml --env-file .env.local

# Dry-run both
python -m src_llm.end_to_end --config src_llm/input/config.yml --env-file .env.local --dry-run
```