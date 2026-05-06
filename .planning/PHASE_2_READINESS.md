# Phase 2 Readiness: I/O & Output Layout Refactoring

## Status: Foundation Ready ✅

Phase 1 has successfully established the foundation. Phase 2 can now build on:

### Available Infrastructure

1. **Flat Directory Structure**
   - Model-based paths: `apps/<app>/llm/<model>/<source>{-video-mode}/`
   - Dry-run directories ready for testing
   - Both video_mode and keyframe_mode paths supported

2. **AppConfig with video_mode**
   - video_mode defaults to True (Stage 1 oriented)
   - Can be overridden per-app in YAML config
   - Validation ensures only supported providers enabled

3. **OutputLayout Enhanced**
   - is_dry_run field to distinguish run types
   - All path fields ready for Stage 2 consumption
   - Memory.md path included in layout

4. **Metadata Framework**
   - write_run_metadata() accepts video_mode fields
   - Structure ready to embed memory content
   - Fields for task_description, ui_elements, completion_criteria

### What Phase 2 Needs to Implement

#### R2.1: OutputLayout video_mode fields
- Already partially done: memory_md_path exists
- Just needs population during Stage 1 analysis

#### R2.2: Memory.md generation pathway
- Create `_parse_memory_md()` function to extract structured data
- Provider interface for memory generation (not yet done)
- GeminiProvider implementation of memory inference (not yet done)

#### R2.3: Flat run directories with /logs
- Already ready: layout.log_file_path points to run_dir/logs/
- Directory creation in main.py ready

#### R2.4: Metadata.json with memory content
- write_run_metadata() already accepts memory_md_content parameter
- Just needs to be called from main.py with actual memory content

### Easy Wins for Phase 2

1. **Memory parsing function**: Implement `_parse_memory_md()` in main.py
   - Extract task summary from "# Task Summary" section
   - Extract UI elements from "## UI Elements" section
   - Extract completion criteria from "## Completion Criteria" section

2. **Provider interface**: Add abstract method to BaseLLMProvider
   ```python
   def infer_memory_from_video(self, video_path: Path) -> str:
       """Return structured markdown memory from video."""
       raise NotImplementedError(...)
   ```

3. **Main.py integration**: Call memory generation and metadata writing
   - Check if cfg.video_mode is True
   - Call provider.infer_memory_from_video()
   - Parse result with _parse_memory_md()
   - Pass to write_run_metadata() with all fields populated

### Critical Path for Phase 2

```
Phase 1 (✓ Done)
    ↓
[Phase 2] Provider Enhancement + Memory Generation
    ├─ Add BaseLLMProvider.infer_memory_from_video()
    ├─ Implement GeminiProvider version
    ├─ Create _parse_memory_md() helper
    └─ Integrate into main.py flow
    ↓
[Phase 3] Stage 1 Output + Metadata
    ├─ Complete main.py video_mode path
    ├─ Write memory.md to disk
    └─ Populate metadata.json with memory
    ↓
[Phase 4+] Stage 2 Implementation
```

### Dependencies Ready

✅ All Phase 2 dependencies met:
- config.py: supports video_mode flag
- io_utils.py: supports dry-run, provides output layout
- main.py: scaffolding ready for memory generation
- main.py: metadata writing function ready for video_mode fields

### Configuration Ready

Default config.yml already has `video_mode: true`, so Phase 2 testing can start immediately:
```yaml
llm: "gemini"
llm_model: "gemini-2.5-pro"
video_mode: true              # ✓ Ready for Phase 2
```

## Recommendation

Phase 2 is a clean, well-scoped phase that can proceed immediately. No blockers or dependencies from Phase 1. Focus on:

1. Provider interface definition (quick)
2. Memory inference implementation (main effort)
3. Main.py integration (straightforward)
4. Testing with actual Gemini API (timeline dependent)

Expected Phase 2 duration: ~8-12 hours (depends on Gemini API latency)
