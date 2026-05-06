# Two-Stage LLM Workflow Implementation — Complete ✓

**Date:** May 6, 2026  
**Status:** All core components implemented and verified

## Summary

The two-stage LLM workflow is fully implemented:
- **Stage 1 (video_to_memory)**: Analyzes video once → generates structured memory.md + metadata with memory content
- **Stage 2 (memory_to_device)**: Reads pre-generated memory from Stage 1 → automates on device without re-analyzing video
- **Orchestrator (end_to_end)**: Runs both stages in sequence with unified configuration

No redundant video analysis. Memory reusable across multiple automation runs.

---

## Implementation Summary

### Stage 1: Video → Memory (src_llm/video_to_memory.py)

**Flow:**
1. Load config from `src_llm/input/config.yml`
2. Resolve video path (handheld or screenrec)
3. Create provider with `video_mode=True` → returns `GeminiVideoProvider`
4. Call `provider.infer_memory_from_video(video_path)`
5. Parse memory.md for task description, UI elements, completion criteria
6. Write memory.md to flat output structure: `apps/<app>/llm/<model>/<source>-video-mode/run-NNN/memory.md`
7. Write metadata.json with `video_mode_metadata` containing:
   - `memory_md_content`: Full memory.md text
   - `task_description`: Extracted task summary
   - `ui_elements`: Dict of UI elements mentioned in memory
   - `completion_criteria`: List of completion criteria

**Key Implementation:**
- `_parse_memory_md()` function extracts structured data from both YAML header and markdown sections
- `video_mode=True` in config skips keyframe extraction, jumps straight to memory generation
- Metadata storage enables Stage 2 to use memory without file lookups

### Stage 2: Memory → Device (src_llm/memory_to_device.py)

**Flow:**
1. Load config from unified `src_llm/input/config.yml`
2. For each run:
   - Call `_locate_latest_run()` to find latest Stage 1 run: `apps/<app>/llm/<model>/<source>-video-mode/run-*/`
   - Load `metadata.json` from that run
   - Extract `memory_md_content` and `task_description` from metadata
   - Create provider (standard GeminiProvider, not video mode)
   - Call `run_automation(..., memory_content=memory_md_content)`
   - LLM uses memory as context in every step via `decide_next_action_with_video_context()`

**Key Implementation:**
- `_locate_latest_run()` automatically finds prior Stage 1 output
- `_load_run_metadata()` extracts memory from metadata.json (no file I/O needed)
- Memory passed directly to automation loop as `video_summary` context

### Orchestrator: End-to-End (src_llm/end_to_end.py)

**Flow:**
1. Parse `--stage` parameter (1, 2, or all)
2. If stage 1 or all:
   - Import `src_llm.video_to_memory`
   - Call `video_to_memory.main()`
3. If stage 2 or all:
   - Import `src_llm.memory_to_device`
   - Call `memory_to_device.main(argv)`
4. Log progress and exit codes
5. Returns 0 on success, non-zero on failure

**Usage:**
```bash
# Both stages
python -m src_llm.end_to_end --config src_llm/input/config.yml --env-file .env.local

# Stage 1 only
python -m src_llm.end_to_end --stage 1 --config src_llm/input/config.yml --env-file .env.local

# Stage 2 only
python -m src_llm.end_to_end --stage 2 --config src_llm/input/config.yml --env-file .env.local

# Dry-run both (validate config, skip API calls)
python -m src_llm.end_to_end --dry-run --config src_llm/input/config.yml --env-file .env.local
```

---

## Provider Support

### GeminiVideoProvider (providers.py, lines 1100-1270)

**infer_memory_from_video(video_path: Path) -> str:**
- Reads memory prompt from `src_llm/input/prompts/llama_action_prompt_memory.txt`
- Encodes video as base64
- Sends to Vertex AI generateContent API with inline video + memory prompt
- Extracts and returns raw markdown memory text
- Memory format: YAML header (app, goal, outcome) + Session Summary + Steps + Key Observations

**create_provider() routing (providers.py, lines 2716-2717):**
```python
if provider_key == "gemini":
    if video_mode:
        return GeminiVideoProvider(provider_key, llm_model, env, logger, llm_prompt_file)
    return GeminiProvider(provider_key, llm_model, env, logger)
```

---

## Configuration

### Unified Config Format (src_llm/input/config.yml)

Both stages read the same config file. Irrelevant fields ignored:
- **Stage 1 uses:** `llm`, `llm_model`, `video_mode`, `frame_sampling`, `keyframe_selection`, `runs[].app_name`, `runs[].video_path`, `runs[].output.overwrite`
- **Stage 2 uses:** `llm`, `llm_model`, `runs[].app_name`, `runs[].device_serial`, `runs[].max_steps`, `runs[].history_window`, `runs[].step_delay`, `runs[].stall_repeat_threshold`, `runs[].reset_between_runs`

**Key Settings:**
- `video_mode: true` (Stage 1 uses memory mode)
- `llm_model: "gemini-2.5-pro"` (normalized to hyphens, lowercase)
- Default directory structure: flat (no provider directory level)
- Single `dry-run/` that overwrites each test run

---

## Directory Structure

### Flat Structure (no provider directory)

```
apps/
├── adaway/
│   └── llm/
│       ├── gemini-2.5-pro/
│       │   ├── handheld-video-mode/
│       │   │   ├── run-001/
│       │   │   │   ├── memory.md (Stage 1 output)
│       │   │   │   ├── metadata.json (with video_mode_metadata)
│       │   │   │   ├── logs/
│       │   │   │   └── steps/ (Stage 2 automation steps)
│       │   │   ├── run-002/
│       │   │   └── dry-run/ (overwrites each dry-run)
│       │   └── screenrec-video-mode/
│       │       └── run-001/
│       └── gemini-2-flash/
│           └── screenrec-video-mode/
│               └── run-001/
```

**Model slug normalization:**
- Input: "Gemini-2.5-Pro", "GEMINI_2_FLASH", "gemini 2.5 pro"
- Output: "gemini-2.5-pro", "gemini-2-flash" (hyphens, lowercase)
- Applied in: `config.py`, `io_utils.py`, `video_to_memory.py`, `memory_to_device.py`

---

## Metadata Structure

### metadata.json format (Stage 1 output)

```json
{
  "app_name": "adaway",
  "method": "llm",
  "variant": "gemini-2.5-pro",
  "source": "handheld",
  "video_file": "hhv_12345.mp4",
  "video_mode_metadata": {
    "memory_md_content": "---\napp: AdAway\ngoal: ...\noutcome: ...\n---\n\n## Session Summary\n...",
    "task_description": "User opens AdAway, grants permissions, enables blocking",
    "ui_elements": {
      "Allow button": "tap",
      "screen: Main": "navigation_target",
      "input: Toggle Host Blocking": "user_input"
    },
    "completion_criteria": [
      "Host blocking enabled",
      "All permissions granted"
    ]
  },
  "run_dt": "2026-05-06T12:34:56Z",
  "duration_sec": 45.3,
  "status": "success"
}
```

Stage 2 reads `video_mode_metadata` from metadata.json and passes to `run_automation()`.

---

## Automation Memory Context

### automation.py integration (src_llm/automation.py, lines 162-295)

**run_automation() signature:**
```python
def run_automation(
    task_description: str,
    provider: Any,
    device: DeviceController,
    max_steps: int,
    output_dir: Path | None = None,
    history_window: int = 3,
    step_delay: float = 1.5,
    stall_repeat_threshold: int = 4,
    logger: logging.Logger | None = None,
    memory_content: str | None = None,  # NEW: Stage 1 memory
    video_path: Path | None = None,
) -> dict:
```

**Memory usage:**
- Line 198: `video_summary: str | None = memory_content`
- Line 263: If memory provided, skip video analysis
- Line 289: Pass video_summary to LLM in each step via `decide_next_action_with_video_context()`

**Fallback behavior:**
- If memory_content provided: use it directly (Stage 2 path)
- If memory_content is None: attempt direct-video summarization (Milestone 4)
- If no video analysis method: raise error

---

## Verification Checklist

✓ **Stage 1 (video_to_memory.py)**
- [x] Imports `infer_memory_from_video` from providers
- [x] Creates provider with `video_mode=True`
- [x] Calls `provider.infer_memory_from_video(video_path)`
- [x] Parses memory.md with `_parse_memory_md()`
- [x] Writes memory.md to output
- [x] Calls `write_run_metadata()` with memory fields
- [x] Handles dry-run mode

✓ **Stage 2 (memory_to_device.py)**
- [x] Implements `_locate_latest_run()` to find Stage 1 output
- [x] Implements `_load_run_metadata()` to extract memory
- [x] Passes memory_content to `run_automation()`
- [x] Uses unified config.yml

✓ **Orchestrator (end_to_end.py)**
- [x] Parses --stage argument (1, 2, all)
- [x] Imports and runs video_to_memory
- [x] Imports and runs memory_to_device
- [x] Handles --dry-run flag
- [x] Returns proper exit codes

✓ **Provider Support (providers.py)**
- [x] `GeminiVideoProvider.infer_memory_from_video()` implemented
- [x] `_send_video_request()` encodes and sends video
- [x] Memory prompt file exists: `llama_action_prompt_memory.txt`
- [x] `create_provider()` returns GeminiVideoProvider when video_mode=True

✓ **Configuration**
- [x] Model slug normalization applied
- [x] `video_mode: true` default
- [x] Unified config.yml for both stages
- [x] Flat directory structure implemented

✓ **Automation Integration**
- [x] `run_automation()` accepts `memory_content` parameter
- [x] Memory passed to LLM as `video_summary` context
- [x] Falls back to video analysis if memory unavailable
- [x] `decide_next_action_with_video_context()` uses memory

---

## Next Steps (Optional Enhancement)

1. **Test with real video:**
   - Stage 1: Generate memory from sample app video
   - Verify memory.md format and parsing
   - Check metadata.json contains memory content

2. **Test end-to-end flow:**
   - Stage 1 generates memory
   - Stage 2 locates memory, loads it, runs automation
   - Verify LLM uses memory context in decisions

3. **Performance validation:**
   - Measure Stage 1 time (video analysis)
   - Measure Stage 2 time (automation with memory)
   - Verify Stage 2 is faster than full re-analysis

4. **Error handling:**
   - Test missing Stage 1 output (Stage 2 error message)
   - Test corrupted metadata.json (graceful fallback)
   - Test Stage 1 failure (stop orchestrator early)

---

## Rollout & Documentation

- `.claude/IMPLEMENTATION_PROGRESS.md` — detailed progress tracking
- `src_llm/end_to_end.py` — usage examples in docstring
- Config files — unified `src_llm/input/config.yml`
- Memory prompt — `src_llm/input/prompts/llama_action_prompt_memory.txt`

All components integrated and ready for testing.
