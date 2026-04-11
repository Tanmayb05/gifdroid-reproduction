# GIFdroid Reproduction — System Documentation

> Last updated: 2026-04-06

## Overview

This project is a dual-pipeline system for automatically generating **execution traces** from Android app video recordings. Given a video of someone using an Android app, the system figures out what UI actions were taken and outputs a structured JSON trace that can be replayed or evaluated.

Two pipelines exist side by side:

| Pipeline | Approach | Input |
|----------|----------|-------|
| **GIFdroid** (original) | Classical CV: SSIM + ORB + LCS | Video + UTG + artifact screenshots |
| **GIFdroid-LLM** (extension) | AI-augmented: frame sampling + LLM inference | Video + config YAML |

---

## Repository Layout

```
gifdroid-reproduction/
├── src_gifdroid/              # Original CV-based pipeline
├── src_llm/          # LLM-enhanced pipeline
├── apps/                  # Test dataset — 10 Android apps, 2 video types each
├── data/                  # Experimental results & traces
├── analysis/              # Post-run analysis & reporting scripts
├── docs/                  # Implementation guides, issue tracking, this file
├── scripts/               # Utility scripts for data processing
└── logs/                  # Pipeline execution logs
```

---

## Pipeline 1: GIFdroid (Original)

### Entry Point

```
python -m src_gifdroid.main \
  --video <video.mp4> \
  --utg <utg.json> \
  --artifact <artifact_dir/> \
  --out <output.json> \
  [--keyframe-method baseline|stabilize|hysteresis|homography|clip]
```

### 4-Phase Architecture

```
Video
  │
  ▼ Phase 1: Keyframe Location   (location.py, hhv_keyframe.py)
  │    Extract stable GUI states via consecutive-frame SSIM
  │
  ▼ Phase 2: GUI Mapping         (mapping.py)
  │    Match keyframes → artifact screenshots (SSIM + ORB)
  │
  ▼ Phase 3: Trace Generation    (trace.py)
  │    Find shortest UTG path via LCS against observed screen sequence
  │
  ▼ Phase 4: Output Storage      (main.py)
       Write execution_trace.json
```

### Phase 1 — Keyframe Location

**File**: [src_gifdroid/location.py](../../src_gifdroid/location.py), [src_gifdroid/hhv_keyframe.py](../../src_gifdroid/hhv_keyframe.py)

Five detection methods available (selected via `--keyframe-method`):

| Method | Description |
|--------|-------------|
| `baseline` | Luma-channel SSIM on consecutive frames; stable if SSIM > 0.95 for 2+ frames |
| `stabilize` | Two-pass FFmpeg stabilization (vidstabdetect → vidstabtransform), then baseline |
| `hysteresis` | Require k=3 consecutive stable frames before marking keyframe |
| `homography` | SIFT keypoint matching + homography warp to compensate camera motion, then SSIM |
| `clip` | Baseline + CLIP-encode + agglomerative clustering to remove near-duplicates |

Entry: `hhv_keyframe.get_keyframe_fn(method)` returns the appropriate callable.

### Phase 2 — GUI Mapping

**File**: [src_gifdroid/mapping.py](../../src_gifdroid/mapping.py)

- Loads all artifact PNGs; extracts ORB descriptors (nfeatures=1500) and grayscale
- For each keyframe: computes `combined_score = 0.5 × SSIM + 0.5 × ORB_ratio_test`
- Returns the screen ID of the best-scoring artifact

### Phase 3 — Trace Generation

**File**: [src_gifdroid/trace.py](../../src_gifdroid/trace.py)

- Parses UTG JSON → directed graph
- Enumerates all simple paths from screen 0 → last observed screen (DFS via `Graph` class)
- Scores paths using LCS against the observed screen sequence
- Returns shortest paths among those with the highest LCS score

### Supporting Files

| File | Purpose |
|------|---------|
| [src_gifdroid/main.py](../../src_gifdroid/main.py) | CLI + orchestration |
| [src_gifdroid/prerequisites.py](../../src_gifdroid/prerequisites.py) | Dependency checks, MOV→mp4 conversion, command batch generation |

---

## Pipeline 2: GIFdroid-LLM (AI-Enhanced)

### Entry Point

```
python -m src_llm.main \
  --config src_llm/input/config.yml \
  --env-file .env.local
```

### 4-Phase Architecture (Keyframe Mode)

```
Video
  │
  ▼ Phase 1: Frame Sampling      (video.py)
  │    Uniform or adaptive sampling at target FPS
  │
  ▼ Phase 2: Keyframe Selection  (keyframes.py)
  │    SSIM-based or heuristic method to pick representative frames
  │
  ▼ Phase 3: LLM Inference       (providers.py)
  │    Encode keyframes → send to LLM → parse action responses
  │
  ▼ Phase 4: Trace Building      (trace.py)
       Assemble execution_trace.json
```

### Video Mode (Gemini Only)

Bypasses phases 1–2 entirely:
1. Upload raw `.mp4` to Vertex AI File API
2. Poll until `ACTIVE` (up to 300s)
3. Send video + prompt to Gemini 2.5 Pro
4. Parse sparse action list
5. Delete uploaded file

### Phase 1 — Frame Sampling

**File**: [src_llm/video.py](../../src_llm/video.py)

| Strategy | Behavior |
|----------|----------|
| `uniform` | Extract at fixed FPS (default: 1.5) |
| `adaptive` | Uniform extraction, then filter by motion threshold (65th percentile) |

Output: `List[SampledFrame]` — frame number, timestamp, image_bgr, motion_from_prev

### Phase 2 — Keyframe Selection

**File**: [src_llm/keyframes.py](../../src_llm/keyframes.py)

| Method | Behavior |
|--------|----------|
| `ssim` | Consecutive-frame SSIM on luma channel; stable regions → keyframe indices (mirrors GIFdroid logic) |
| `heuristic` | Motion threshold = median + 0.4×σ; enforce min_gap_seconds between selections |

Output: `List[Keyframe]` — sequence_index, timestamp, motion_score, image_bgr, filename

### Phase 3 — LLM Inference

**File**: [src_llm/providers.py](../../src_llm/providers.py)

Abstract base: `BaseLLMProvider`

```python
class BaseLLMProvider(ABC):
    def infer_actions(keyframes: List[Keyframe]) -> List[ProviderAction]
    def infer_actions_from_video(video_path: Path) -> List[ProviderAction]  # optional
    def validate_connection() -> None  # optional preflight
```

#### Supported Providers

| Provider | Type | Auth | Default Model | VRAM |
|----------|------|------|---------------|------|
| `gemini` | Cloud | API key or ADC | gemini-1.5-flash | — |
| `llama` | Local (Ollama) | None | llama3.2-vision:latest | 7.8 GB |
| `llava` | Local (Ollama) | None | llava:7b | 4.7 GB |
| `minicpm` | Local (Ollama) | None | minicpm-v:latest | 5.5 GB |
| `gemma` | Local (Ollama) | None | gemma3:4b | 3.3 GB |
| `qwen` | Local (Ollama) | None | qwen2.5vl:7b | 6.0 GB |

**Recommended for M-series Macs**: `qwen`

#### Fallback Behavior (all local providers)

When JSON parsing fails:
- First keyframe → `"launch"`
- motion_score ≥ 18 → `"tap"`
- motion_score ≥ 9 → `"scroll"`
- motion_score < 9 → `"wait"`

### Core Data Models

```python
@dataclass
class SampledFrame:
    frame_number: int
    timestamp_sec: float
    image_bgr: np.ndarray
    motion_from_prev: float

@dataclass
class Keyframe:
    sequence_index: int
    frame_number: int
    timestamp_sec: float
    motion_score: float
    image_bgr: np.ndarray
    file_name: str

@dataclass
class ProviderAction:
    screen_description: str
    action_type: str       # "tap", "scroll", "launch", "wait", etc.
    target: str
    details: str
    confidence: float      # 0.0–1.0

@dataclass
class TraceStep:
    step_index: int
    timestamp_sec: float
    frame_file: str
    screen_description: str
    action: TraceAction
    confidence: float
```

### Supporting Files

| File | Purpose |
|------|---------|
| [src_llm/main.py](../../src_llm/main.py) | CLI + batch orchestration |
| [src_llm/config.py](../../src_llm/config.py) | YAML config parsing + validation |
| [src_llm/io_utils.py](../../src_llm/io_utils.py) | Output layout, path resolution (shorthand hhv/srv → full paths), metadata |
| [src_llm/env_loader.py](../../src_llm/env_loader.py) | .env loading + provider-specific validation |
| [src_llm/logging_utils.py](../../src_llm/logging_utils.py) | Logging setup |
| [src_llm/llama_prereq.py](../../src_llm/llama_prereq.py) | Ollama preflight (Metal detection, model availability) |
| [src_llm/reset_runs.py](../../src_llm/reset_runs.py) | Batch cleanup of run directories |

---

## Configuration

### config.yml (src_llm/input/config.yml)

```yaml
llm: "gemini"                       # gemini | llama | llava | minicpm | gemma | qwen
llm_model: "gemini-1.5-flash"      # Optional; provider defaults apply if omitted
llm_prompt_file: "..."             # Optional; path to prompt template

frame_sampling:
  strategy: "uniform"              # "uniform" or "adaptive"
  fps: 1.5
  max_frames: 100

keyframe_selection:
  method: "ssim"                   # "ssim" | "heuristic"
  min_gap_seconds: 1.0
  ssim_threshold: 0.95
  stable_threshold: 2

output:
  overwrite: false                 # Skip run if execution_trace.json exists

logging:
  level: "INFO"

runs:
  - app_name: "adaway"
    video_path:
      - "hhv"                      # Shorthand: apps/adaway/videos/handheld/hhv-001.mp4
      - "srv"                      # Shorthand: apps/adaway/videos/screenrec/srv-001.mp4
```

### .env.local (credentials)

```bash
GOOGLE_GENERATIVE_AI_API_KEY=...
GEMINI_VERTEX_PROJECT_ID=...
GEMINI_VERTEX_LOCATION=us-central1

ANTHROPIC_API_KEY=...   # Reserved; not yet integrated

LLAMA_BASE_URL=http://localhost:11434/v1
LLAMA_TIMEOUT_SEC=180
QWEN_BASE_URL=http://localhost:11434/v1
QWEN_TIMEOUT_SEC=300
```

### Prompt Templates (src_llm/input/prompts/)

| File | Notes |
|------|-------|
| `llama_action_prompt_gemini_2.txt` | **Recommended** — schema-first, works across providers |
| `llama_action_prompt_baseline.txt` | Compact fallback if model struggles with schema |
| `llama_action_prompt_gemini_1.txt` | Verbose schema-first with role definition |
| `llama_action_prompt_claude.txt` | Anthropic-style variant |
| `gemini_video_prompt.txt` | For video mode (sparse action detection) |

Contains `{KEYFRAMES}` placeholder for per-keyframe metadata injection.

---

## Dataset Structure

### Test Corpus — 10 Android Apps

```
apps/
├── adaway/
├── antennapod/
├── deadhash/
├── homemedkit/
├── jigsaw/
├── luxalarm/
├── pomodorot/
├── portauthority/
├── simplenotes/
└── wifianalyzer/
```

Each app:
```
apps/<app>/
├── videos/
│   ├── handheld/hhv-001.mp4       # Real handheld camera recording
│   └── screenrec/srv-001.mp4      # ADB screen recording
├── utgs/utg-01/
│   └── input/
│       ├── utg.json               # GUI Transition Graph (screen graph + actions)
│       └── artifacts/             # Screenshots of each UI state
└── llm/<provider>/<model>/<type>/run-<n>/
    ├── execution_trace.json
    ├── frames_manifest.json
    ├── metadata.json
    ├── keyframes/
    └── logs/
```

### UTG JSON Schema

```json
{
  "events": [
    {
      "sourceScreenId": "0",
      "destinationScreenId": "1",
      "launch": {"action": "android.intent.action.MAIN"}
    },
    {
      "sourceScreenId": "1",
      "destinationScreenId": "2",
      "target": {
        "type": "TAP",
        "targetDetails": {
          "className": "android.widget.Button",
          "resourceName": "com.example:id/my_button"
        }
      }
    }
  ]
}
```

### Output — execution_trace.json

```json
{
  "video": "apps/adaway/videos/handheld/hhv-001.mp4",
  "llm": "qwen",
  "replay_trace": [
    {
      "step_index": 0,
      "timestamp_sec": 0.0,
      "frame_file": "keyframes/frame_0000.png",
      "screen_description": "App launch screen",
      "action": {"type": "launch", "target": "", "details": ""},
      "confidence": 0.9
    }
  ]
}
```

---

## External Dependencies

### Python Packages

**src_gifdroid/** (original, pinned for CV compatibility):
```
opencv-contrib-python==3.4.2.16
opencv-python==4.5.1.48
scikit-image==0.17.2
scikit-learn==0.24.2
numpy==1.19.2
matplotlib==3.3.4
transformers, torch    # For CLIP keyframe method
```

**src_llm/**:
```
PyYAML>=6.0
python-dotenv>=1.0.0
opencv-python>=4.8.0
numpy>=1.24.0
scikit-image>=0.22.0
google-auth>=2.30.0
requests>=2.31.0
```

### External Tools

| Tool | Purpose |
|------|---------|
| **ffmpeg** | Video stabilization (vidstabdetect + vidstabtransform) |
| **Ollama** | Local LLM inference server |
| **Google Cloud SDK** | Vertex AI ADC auth for Gemini |

---

## Extensibility

### Adding a New LLM Provider

1. Subclass `BaseLLMProvider` in [src_llm/providers.py](../../src_llm/providers.py)
2. Implement `infer_actions(keyframes: List[Keyframe]) -> List[ProviderAction]`
3. Register in `create_provider()` factory function
4. Add to config validation if needed

### Adding a New Keyframe Method (GIFdroid original)

1. Create function with signature: `(video, stable_threshold=2, **kwargs) -> (keyframes, indices)`
2. Register in `hhv_keyframe.get_keyframe_fn(method)` dispatch dict

### Adding Video Mode to a Provider

1. Override `infer_actions_from_video(video_path: Path)` in provider subclass
2. Add provider name to `VIDEO_MODE_SUPPORTED_PROVIDERS` in [src_llm/config.py](../../src_llm/config.py)

---

## Known Issues

| Issue | Impact | Reference |
|-------|--------|-----------|
| Qwen HTTP 500 on Apple Silicon with multiple images (OOM) | Inference failure | [docs/issues/](../issues/) |
| Llama repetition loop in raw response | JSON parse failure → fallback | [docs/issues/](../issues/) |
| Llama ignores JSON instruction, hallucinates | Wrong action types | Use `llama_action_prompt_gemini_2.txt` |
| bt2020 color space in handheld videos | Video decode issues | See [project_handheld_issues](../../../.claude/projects/-Users-tanmaybhuskute-Documents-gifdroid-reproduction/memory/project_handheld_issues.md) |
