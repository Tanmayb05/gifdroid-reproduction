# Flattening Run Directory Structure for src_llm

## Current Status (as of May 12, 2026)

- **Total runs across all apps:** 51 gemini-2.5-pro runs (handheld-video-mode and screenrec-video-mode)
- **Current structure:** `apps/<app>/llm/<model>/<video-type><-video-mode>/run-NNN/`
- **Problem:** Deep nesting, difficult to identify which video is associated with a run without checking metadata

## Desired Target Structure

New flat structure: `apps/<app>/llm/<video-name>-<model>-<video-mode-suffix>/run-NNN/`

### Examples

| Current Path | Target Path |
|--------------|-------------|
| `apps/bakerspercentagecalculator/llm/gemini-2.5-pro/handheld-video-mode/run-001/` | `apps/bakerspercentagecalculator/llm/hhv-002-gemini-2.5-pro-vm/run-001/` |
| `apps/antennapod/llm/gemini-2.5-pro/screenrec-video-mode/run-001/` | `apps/antennapod/llm/srv-001-gemini-2.5-pro-vm/run-001/` |

### Naming Convention

- `<video-name>`: Extract from `metadata.json::video` field (e.g., `hhv-002.mp4` → `hhv-002`)
- `<model>`: Extract from `metadata.json::variant` field and normalize (e.g., `gemini-2.5-pro`)
- `<video-mode-suffix>`: 
  - `vm` if `metadata.json::video_mode_metadata` exists (video mode)
  - omitted if not present (standard mode)

## Phase 1: Migration of Existing Runs (Dry-Run + Execution)

### Step 1.1: Generate Migration Script

**Script purpose:** Python script to scan all existing gemini-2.5-pro runs, extract video info from metadata.json, and perform safe migration.

**Script: `scripts/migrate_runs_flatten.py`**

Key features:
1. **Discovery phase:** Find all `apps/*/llm/gemini-2.5-pro/*/run-NNN/` directories
2. **Validation phase:** For each run, read `metadata.json` and extract:
   - `app` name
   - `variant` (model)
   - `video` filename
   - Check presence of `video_mode_metadata` field
3. **Path construction phase:** Build new target path using naming convention
4. **Dry-run output:** Print table showing:
   - Current path
   - Target path
   - Video name extracted
   - Model variant
   - Video mode (true/false)
5. **Safety checks:**
   - Verify source directory exists
   - Warn if target directory already exists
   - Check for metadata.json consistency across runs
6. **Execution phase (post-approval):**
   - Copy entire run directory tree to new location
   - Update any internal path references (if needed)
   - Delete source directory
   - Cleanup empty parent directories

### Step 1.2: Execute Dry-Run

```bash
cd /Users/tanmaybhuskute/Documents/gifdroid-reproduction
python scripts/migrate_runs_flatten.py --dry-run
```

Expected output:
- Table of ~51 migrations showing current → target paths
- Count of runs by app
- Summary of video modes detected
- Any warnings or conflicts

### Step 1.3: User Approval

Present dry-run results to user for approval before making changes.

### Step 1.4: Execute Migration

```bash
python scripts/migrate_runs_flatten.py --execute
```

The script will:
1. Create new directory structure
2. Move all files and directories
3. Report completion status
4. Clean up empty directories
5. Verify checksums (optional, for data integrity)

### Step 1.5: Cleanup

After successful migration:
1. Delete `scripts/migrate_runs_flatten.py`
2. Delete any `.pyc` files or `__pycache__` directories created
3. Commit the restructured runs

---

## Phase 2: Code Changes for Future Runs

### Target Files to Modify

**File: `src_llm/io_utils.py` — `create_output_layout()` function**

Current implementation (lines 118-164):
```python
def create_output_layout(
    project_root: Path,
    cfg: AppConfig,
    video_type: VideoType,
    run_dt: datetime,
    is_dry_run: bool = False,
) -> OutputLayout:
    """Build output paths under apps/{app}/llm/{model}/{source}{-video-mode}/run-NNN/"""
    model_slug = _normalize_model_slug(cfg.llm_model)
    source = "handheld" if video_type == "hhv" else "screenrec"
    source_dir = f"{source}-video-mode" if cfg.video_mode else source

    run_parent = (
        project_root
        / "apps"
        / cfg.app_name.lower()
        / "llm"
        / model_slug
        / source_dir
    )
    # ... rest of function
```

**Changes needed:**
1. Update `create_output_layout()` to use the new flat naming convention
2. Extract video name (without `.mp4` extension) from the AppConfig
3. Add logic to append `-vm` suffix for video_mode runs
4. Build the new path: `apps/{app}/llm/{video-name}-{model}-{vm?}/run-NNN/`

### Updated Implementation Pattern

```python
def create_output_layout(
    project_root: Path,
    cfg: AppConfig,
    video_type: VideoType,
    run_dt: datetime,
    is_dry_run: bool = False,
) -> OutputLayout:
    """Build output paths under apps/{app}/llm/{video-name}-{model}{-vm}/run-NNN/"""
    model_slug = _normalize_model_slug(cfg.llm_model)
    
    # Extract video name from config (e.g., "hhv-002.mp4" → "hhv-002")
    video_name = _extract_video_name(cfg.video_file)  # new helper function
    
    # Build flat directory name
    dir_parts = [video_name, model_slug]
    if cfg.video_mode:
        dir_parts.append("vm")
    flat_dir = "-".join(dir_parts)
    
    run_parent = (
        project_root
        / "apps"
        / cfg.app_name.lower()
        / "llm"
        / flat_dir
    )
    # ... rest of function unchanged
```

### Helper Function

**Add to `src_llm/io_utils.py`:**

```python
def _extract_video_name(video_file: str) -> str:
    """Extract video name without extension (e.g., 'hhv-002.mp4' → 'hhv-002')."""
    return Path(video_file).stem
```

### Configuration Updates

**Check `src_llm/config.py`:**
- Verify that `AppConfig` contains `video_file` or equivalent field
- If not present, add parsing from YAML config to capture the video filename
- Ensure `video_mode` boolean is accessible in AppConfig

### Testing

1. **Unit test:** Create test case in test suite to verify:
   - Video name extraction
   - Correct path construction for video_mode=true
   - Correct path construction for video_mode=false
   - Run ID incrementing logic still works

2. **Integration test:**
   - Run a video through entire pipeline
   - Verify output lands in correct new structure
   - Verify all artifacts (metadata.json, memory.md, etc.) are in correct location

3. **Backward compatibility check:**
   - Ensure config parsing doesn't break existing YAML files
   - Document any required config changes in MIGRATION.md

### Documentation Updates

1. **Update `src_llm/README.md`:**
   - Document new directory structure
   - Explain video name extraction
   - Update examples with new paths

2. **Create `docs/MIGRATION.md`:**
   - Document the migration from old to new structure
   - Provide commands to update any external references
   - Note date of migration (2026-05-12)

3. **Update docstring in `create_output_layout()`:**
   - Change from: `"""Build output paths under apps/{app}/llm/{model}/{source}{-video-mode}/run-NNN/"""`
   - Change to: `"""Build output paths under apps/{app}/llm/{video-name}-{model}{-vm}/run-NNN/"""`

---

## Migration Checklist

### Phase 1: Existing Runs
- [ ] Create `scripts/migrate_runs_flatten.py`
- [ ] Run dry-run and present results
- [ ] Get user approval
- [ ] Execute migration
- [ ] Verify all runs migrated successfully
- [ ] Delete migration script and cache
- [ ] Commit restructured runs

### Phase 2: Code Changes
- [ ] Add `_extract_video_name()` helper to `src_llm/io_utils.py`
- [ ] Update `create_output_layout()` to use new flat naming
- [ ] Update `src_llm/config.py` if needed (ensure video_file is accessible)
- [ ] Add unit tests for path construction
- [ ] Run integration test with actual video
- [ ] Update `src_llm/README.md` documentation
- [ ] Create `docs/MIGRATION.md`
- [ ] Commit code changes

### Post-Migration
- [ ] Run a few new jobs to confirm new structure works
- [ ] Verify metadata.json contains all expected fields
- [ ] Update any automation scripts that reference run paths
- [ ] Archive old directory structure documentation

---

## Expected Benefits

1. **Easier identification:** Run purpose immediately visible from directory name
2. **Flatter hierarchy:** Fewer directory levels to navigate
3. **Better organization:** Video name + model + mode clearly separated
4. **Scalability:** Works for future models without deep nesting
5. **Automation friendly:** Predictable naming pattern for scripting

---

## Rollback Plan (if needed)

If migration encounters issues:
1. Keep backup of original `apps/` directory structure
2. Reverse migration script can rebuild old structure from new one
3. Git allows reverting commits if needed
4. Dry-run phase catches issues before execution

