Here’s a **clean, condensed Markdown file** you can directly drop into your repo (e.g., `PROJECT_STRUCTURE.md`). It aligns with your pipeline, is reproducible, and consistent with GIFdroid’s modular phases (keyframe → mapping → trace) .

---

```md
# 📁 Project Structure & Naming Conventions

## 1. Overview

This project extends GIFdroid to support both:
- Screen recordings (SRV)
- Handheld recordings (HHV)

Core pipeline:
1. Keyframe Extraction  
2. GUI Mapping (UTG)  
3. Execution Trace Generation  

Each experiment is treated as a **run** to ensure reproducibility.

---

## 2. Directory Structure

```

apps/
<app_name>/
videos/
handheld/
hhv-001.mp4
screenrec/
srv-001.mp4

```
utgs/
  utg-01/
    input/
      utg.json
      artifacts/
        artifact-001.png

    runs/
      baseline/
        handheld/run-001/
      keyframe-fixes/
        clip/handheld/run-001/
        homography/handheld/run-001/
        hysteresis/handheld/run-001/
        stabilize/handheld/run-001/
        vlm/handheld/run-001/
      llm/
        gemini/gemini-1-5-pro/handheld/run-001/

    manifest.json
```

```

---

## 3. Naming Conventions

### General Rules
- Lowercase only
- Use `kebab-case` for folders, `snake_case` for files
- Zero-padded IDs: `utg-01`, `run-001`, `kf-0001`
- Avoid redundant metadata in filenames (store in path or metadata.json)

---

### Files

| Type | Naming |
|------|------|
| UTG | `utg.json` |
| Artifacts | `artifact-001.png` |
| Keyframes | `kf-0001.png` |
| Execution Trace | `execution_trace.json` |
| Frames Manifest | `frames_manifest.json` |
| Run Metadata | `metadata.json` |

---

### Videos

```

handheld/
hhv-001.mp4

screenrec/
srv-001.mp4

```

---

### Runs

Each run = one execution with fixed config.

```

run-001/
run-002/
run-003/

```

---

## 4. Run Folder Structure

```

run-001/
keyframes/
kf-0001.png
execution_trace.json
frames_manifest.json
metadata.json
logs/

```

---

## 5. Metadata (MANDATORY)

Each run must include:

```

metadata.json

````

### Required Fields

```json
{
  "app": "antennapod",
  "utg": "utg-01",
  "method": "llm",
  "variant": "gemini-1-5-pro",
  "source": "handheld",
  "video": "hhv-001.mp4",
  "config": {
    "frame_sampling": {},
    "keyframe_selection": {}
  },
  "timestamp": "2026-03-31T18:42:10",
  "duration_sec": 120,
  "status": "success"
}
````

---

## 6. UTG-Level Manifest (CRITICAL)

Each UTG must maintain:

```
utg-01/manifest.json
```

### Purpose

* Track all runs
* Enable evaluation scripts
* Avoid scanning directories

### Example

```json
{
  "app": "antennapod",
  "utg": "utg-01",

  "videos": {
    "handheld": ["hhv-001.mp4"],
    "screenrec": ["srv-001.mp4"]
  },

  "runs": [
    {
      "id": "run-001",
      "method": "baseline",
      "source": "handheld",
      "status": "success",
      "path": "runs/baseline/handheld/run-001/"
    },
    {
      "id": "run-002",
      "method": "llm",
      "variant": "gemini-1-5-pro",
      "source": "handheld",
      "status": "success",
      "path": "runs/llm/gemini/gemini-1-5-pro/handheld/run-002/"
    }
  ],

  "latest": {
    "baseline": "run-001",
    "llm_gemini_1_5_pro": "run-002"
  }
}
```

---

## 7. Logs Strategy

### Principle

Logs must be:

* tied to a run
* timestamped
* stage-aware

### Location

```
run-001/logs/
```

### Naming Format

```
<timestamp>__run-<id>__<stage>__<status>.log
```

### Example

```
2026-03-31T18-42-10__run-001__pipeline__success.log
2026-03-31T18-42-10__run-001__llm-inference__failed.log
```

---

### Standard Stages

* `pipeline`
* `frame-sampling`
* `keyframe-selection`
* `stabilization`
* `gui-mapping`
* `trace-generation`
* `llm-inference`

---

### Status Values

* `started`
* `success`
* `failed`
* `partial`

---

## 8. Method Organization

### Baseline

```
runs/baseline/
```

### Keyframe Fixes

```
runs/keyframe-fixes/
  clip/
  homography/
  hysteresis/
  stabilize/
  vlm/
```

### LLM

```
runs/llm/<provider>/<model>/
```

Example:

```
llm/gemini/gemini-1-5-pro/
```

---

## 9. Design Principles

### 1. Path Encodes Context

Avoid long filenames — use folder hierarchy.

### 2. Reproducibility First

Every run must be reproducible using:

* metadata.json
* input video
* config

### 3. Immutable Runs

Never overwrite runs → create new run IDs.

### 4. Evaluation-Friendly

Structure supports:

* baseline vs LLM comparison
* ablation studies
* RQ-based evaluation

### 5. Modular Pipeline

Aligns with GIFdroid phases:

* Keyframe Location
* GUI Mapping
* Trace Generation 

---

## 10. Anti-Patterns (Avoid)

❌ `kf_clip_hhv_appname_1.png`
❌ `llm_gemini_pro_final_v2.json`
❌ mixing runs in same folder
❌ no metadata per run

---

## 11. Minimal Checklist

Before committing a run:

* [ ] metadata.json exists
* [ ] execution_trace.json exists
* [ ] keyframes saved
* [ ] logs recorded
* [ ] manifest.json updated

---

## 12. Future Extensions

* Add preprocessing stage (stabilization, homography)
* Add evaluation outputs per run
* Add failure categorization logs
* Add cross-run comparison scripts

---

```

---

If you want next step, I can:
- generate a **Python utility to auto-create this structure**
- or design a **run manager CLI (very useful for experiments + paper evaluation)**
```
