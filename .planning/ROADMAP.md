# Two-Stage LLM Workflow Roadmap

## Overview
Refactor video analysis and device automation into a two-stage pipeline:
- **Stage 1**: Analyze video once → generate memory.md + metadata
- **Stage 2**: Reuse memory.md for device automation (no video re-analysis)

Eliminates redundant video processing and reduces LLM token usage by 10x.

---

## Phase 1: Foundation & Configuration
**Goal:** Establish flat directory structure and extend config to support video_mode flag

**Requirements:**
- [R1.1] Flat directory structure (no provider subdirectory)
- [R1.2] Model names include provider (e.g., "gemini-2.5-pro")
- [R1.3] video_mode flag in AppConfig (defaults to true)
- [R1.4] Dry-run outputs to single overwritable dry-run/ directory

**Deliverables:**
- Updated AppConfig dataclass with video_mode field
- Directory path logic: `apps/<app>/llm/<model>/<source>-video-mode/run-NNN/`
- Normalize model slugs (hyphens, lowercase)

---

## Phase 2: I/O & Output Layout Refactoring
**Goal:** Update file handling to support both video_mode and keyframe_mode paths

**Requirements:**
- [R2.1] OutputLayout includes is_dry_run and run_id fields
- [R2.2] create_output_layout() handles video_mode and keyframe_mode branches
- [R2.3] Flat run directories with /logs subdirectory
- [R2.4] Metadata.json stores memory content for Stage 2

**Deliverables:**
- Refactored OutputLayout dataclass
- Updated create_output_layout() function
- Enhanced write_run_metadata() with video_mode fields
- Parsing helpers for memory.md extraction

---

## Phase 3: Provider Enhancement for Memory Generation
**Goal:** Add memory.md generation capability to LLM providers

**Requirements:**
- [R3.1] BaseLLMProvider.infer_memory_from_video() abstract method
- [R3.2] GeminiProvider implements memory inference
- [R3.3] Structured markdown output (Task Summary, Steps, UI Elements, Completion Criteria)
- [R3.4] Memory parsing extracts task, UI elements, completion criteria

**Deliverables:**
- Provider interface for memory generation
- Gemini implementation with video frame extraction
- Memory.md format and parsing logic
- Helpers to extract structured data from markdown

---

## Phase 4: Stage 1 Implementation (Video → Memory)
**Goal:** Implement src_llm.main with video_mode support for memory generation

**Requirements:**
- [R4.1] main.py accepts --dry-run flag
- [R4.2] video_mode=true path generates memory.md via provider
- [R4.3] Writes memory.md, metadata.json with video_mode_metadata
- [R4.4] Dry-run validates config without API calls

**Deliverables:**
- Updated main.py with video_mode branching
- Memory generation and persistence logic
- Metadata writing with embedded memory content
- Dry-run flow that skips provider calls

---

## Phase 5: Stage 2 Implementation (Memory → Device Automation)
**Goal:** Implement src_llm.automate with memory-aware automation

**Requirements:**
- [R5.1] Locate latest Stage 1 run for app+model+video_type
- [R5.2] Load metadata.json and extract memory.md content
- [R5.3] Pass memory context to LLM during automation steps
- [R5.4] Device automation uses memory instead of re-analyzing video

**Deliverables:**
- Run locator: _locate_latest_run()
- Metadata loader: _load_run_metadata()
- Output dir resolver with auto-derivation
- Integration with automation loop

---

## Phase 6: Automation Memory Context Integration
**Goal:** Update automation loop to use memory context in LLM decisions

**Requirements:**
- [R6.1] run_automation() accepts memory_content parameter
- [R6.2] decide_next_action() receives memory context
- [R6.3] Memory injected into LLM prompt for each step
- [R6.4] Session trace logs memory usage

**Deliverables:**
- Updated run_automation() signature
- Provider.decide_next_action() with memory context
- Prompt construction with memory injection
- Session trace with memory metadata

---

## Phase 7: End-to-End Orchestration & Testing
**Goal:** Create orchestrator and validate two-stage pipeline integration

**Requirements:**
- [R7.1] Single config.yml serves both Stage 1 and Stage 2
- [R7.2] End-to-end entry point (pipeline module)
- [R7.3] Sequential execution: Stage 1 → Stage 2
- [R7.4] Integration tests validate Stage 1 → Stage 2 handoff
- [R7.5] Dry-run validates full pipeline without processing

**Deliverables:**
- src_llm/pipeline.py (orchestrator)
- Unified config.yml example
- Integration tests
- Documented workflow examples

---

## Summary

| Phase | Title | Status |
|-------|-------|--------|
| 1 | Foundation & Configuration | ○ |
| 2 | I/O & Output Layout Refactoring | ○ |
| 3 | Provider Enhancement for Memory Generation | ○ |
| 4 | Stage 1 Implementation (Video → Memory) | ○ |
| 5 | Stage 2 Implementation (Memory → Device) | ○ |
| 6 | Automation Memory Context Integration | ○ |
| 7 | End-to-End Orchestration & Testing | ○ |

**Total effort:** ~7 phases, estimated 40-60 hours of implementation
**Token savings:** ~90% reduction in video re-analysis (10x improvement)
