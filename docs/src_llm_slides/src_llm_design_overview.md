# src_llm: Two-Stage LLM Workflow for Android App Automation

## Overview: What is src_llm?

`src_llm` is a sophisticated tool that **automates Android app tasks using AI (LLM models)**. Instead of watching a video once and analyzing it multiple times for each automation step, it uses a **two-stage architecture** that reduces token usage by ~90%.

### Key Features

- ✅ **Two-stage workflow**: Separate video analysis from device automation
- ✅ **Token efficiency**: ~90% token savings vs traditional approaches
- ✅ **Flexible models**: Local (Ollama) and cloud (Gemini) providers
- ✅ **Memory-based context**: Reuse analysis across multiple automation steps
- ✅ **Easy configuration**: YAML config + .env file

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        src_llm System                           │
│                                                                  │
│  ┌──────────────────────┐         ┌──────────────────────────┐  │
│  │   STAGE 1            │         │   STAGE 2                │  │
│  │  Video → Memory      │         │  Memory → Device         │  │
│  │                      │         │                          │  │
│  │  Input:              │         │  Input:                  │  │
│  │  • Video file        │         │  • memory.md             │  │
│  │                      │         │  • Android device        │  │
│  │  Process:            │         │                          │  │
│  │  1. Extract frames   │         │  Process:                │  │
│  │  2. Select keyframes │         │  1. Load memory context  │  │
│  │  3. Send to LLM      │         │  2. Capture screen       │  │
│  │  4. Generate memory  │         │  3. LLM decides action   │  │
│  │                      │         │  4. Execute on device    │  │
│  │  Output:             │         │  5. Repeat until done    │  │
│  │  • memory.md         │         │                          │  │
│  │  • metadata.json     │         │  Output:                 │  │
│  │  • keyframes/        │         │  • Automated actions     │  │
│  │  • execution logs    │         │  • Device trace          │  │
│  └──────────────────────┘         └──────────────────────────┘  │
│           ↓                                    ↑                 │
│           └────────────────────────────────────┘                │
│                  Shared via metadata.json                       │
│                                                                  │
│  Config: config.yml (app_name, video_path, llm settings)       │
│  Auth: .env (API keys, URLs)                                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## Data Flow Through the System

```
Video File (.mp4)
       │
       ↓
┌──────────────────────────────────────────────┐
│  Stage 1: Video Analysis                     │
├──────────────────────────────────────────────┤
│  1. VideoFrameExtractor                      │
│     • Opens video file                       │
│     • Extracts frames at fixed intervals     │
│                                              │
│  2. KeyframeSelector                         │
│     • Analyzes frames for changes            │
│     • Uses SSIM (recommended) or heuristic   │
│     • Keeps only unique/important frames     │
│                                              │
│  3. LLM Provider (Gemini/Qwen/Llama)         │
│     • Sends keyframe images to LLM           │
│     • LLM analyzes and generates memory      │
│                                              │
│  4. Memory Generator                         │
│     • Structures output as markdown          │
│     • Extracts task, steps, UI elements      │
└──────────────────────────────────────────────┘
       │
       ↓
    memory.md (structured analysis)
  metadata.json (embeds memory content)
       │
       ↓
┌──────────────────────────────────────────────┐
│  Stage 2: Device Automation                  │
├──────────────────────────────────────────────┤
│  Repeat for each automation step:            │
│                                              │
│  1. Load Memory Context                      │
│     • Read memory.md from metadata.json      │
│     • Understand task and expected steps     │
│                                              │
│  2. Capture Current Screen                   │
│     • Take screenshot of device              │
│     • Extract UI elements                    │
│                                              │
│  3. LLM Decision                             │
│     • Send: memory + current screen          │
│     • LLM decides next action                │
│     • Action: tap, type, scroll, wait, etc   │
│                                              │
│  4. Execute on Device                        │
│     • Apply action via uiautomator2          │
│     • Wait for response                      │
│     • Loop until task complete               │
└──────────────────────────────────────────────┘
       │
       ↓
    Android Device (Automated)
```

---

## Component Architecture

### 1. ConfigLoader (`config.py`)

**Purpose**: Parse and validate configuration

- Reads YAML config file
- Validates app_name, video_path, model settings
- Supports video path shorthands ("hhv" → `apps/{app}/videos/handheld/hhv-001.mp4`)
- Returns structured `PipelineConfig` object

**Key Variables**:
- `app_name`: Which app to automate
- `video_path`: Video file location or shorthand
- `llm`: Provider name (gemini, qwen, llama, etc)
- `llm_model`: Specific model (optional, uses provider default)
- `video_mode`: Enable/disable Stage 1 memory generation

### 2. VideoFrameExtractor (`video.py`)

**Purpose**: Extract frames from video file

- Opens MP4 video using OpenCV
- Samples frames at specified FPS (frames per second)
- Returns frame objects with timestamps
- Config controls sampling strategy (uniform, adaptive)

**Inputs**:
- Video file path
- Frame sampling config (FPS, max frames)

**Outputs**:
- List of sampled frames
- Video metadata (duration, fps, resolution)

### 3. KeyframeSelector (`keyframes.py`)

**Purpose**: Select important frames from sampled set

Three methods:

1. **Heuristic**: Motion-based detection
   - Calculates optical flow (pixel movement)
   - Keeps frames with significant motion
   - Simple and fast

2. **SSIM** (Recommended): Structural similarity
   - Compares frames pixel-by-pixel
   - Detects stable vs changing screens
   - Best quality for UI automation

3. **LLM-Assisted**: Uses LLM to select
   - Currently behaves like heuristic
   - Future: LLM ranks frame importance

**Key Parameter**: `ssim_threshold` (0.95 = very similar, skip)

**Output**: Reduced set of keyframes with confidence scores

### 4. LLM Providers (`providers.py`)

**Purpose**: Abstract interface for all LLM providers

**Base Class**: `BaseLLMProvider`

```python
class BaseLLMProvider(ABC):
    def infer_memory_from_video(video_path) -> str:
        """Analyze video, return markdown memory"""
    
    def infer_actions(keyframes) -> List[ProviderAction]:
        """Analyze keyframes, return action decisions"""
```

**Implementations**:

| Provider | Model | Auth | Method |
|----------|-------|------|--------|
| Gemini | gemini-1.5-flash | API key | HTTP |
| Qwen | qwen2.5vl:7b | Ollama URL | Local |
| Llama | llama3.2-vision:11b | Ollama URL | Local |
| LLaVA | llava:7b | Ollama URL | Local |
| MiniCPM | minicpm-v:latest | Ollama URL | Local |
| Gemma | gemma3:4b | Ollama URL | Local |

**Error Handling**:
- HTTP retries with exponential backoff (429, timeouts)
- Fallback to deterministic heuristic if LLM fails
- Saves raw response for debugging

### 5. Memory Parser (`main.py`)

**Purpose**: Parse memory.md into structured data

**Extracts**:
- Task description
- Steps sequence
- UI elements (buttons, fields, screens)
- Completion criteria

**Format** (YAML header + markdown sections):

```markdown
---
goal: Enable AdAway ad filter
outcome: Filter status shows enabled
---

## Steps
- **Action:** launch → App starting screen
- **Action:** tap → "Enable" button at top-right
- **Screen:** Filter status confirmation

## UI Elements
- Button: "Enable" (coordinates: top-right)
- Text: "Status: Disabled" (center)
```

### 6. MemoryToDevice (`memory_to_device.py`)

**Purpose**: Automate Android device using Stage 1 memory

**Process**:
1. Locate latest Stage 1 run for app+model+video_type
2. Load memory.md from metadata.json
3. For each automation step:
   - Capture device screenshot
   - Send memory + screenshot to LLM
   - LLM decides action
   - Execute action via uiautomator2
4. Log execution trace

**Device Actions Supported**:
- `tap`: Click element at coordinates
- `type`: Type text into field
- `scroll`: Scroll up/down/left/right
- `swipe`: Swipe gesture
- `long_press`: Long touch
- `back`: Press back button
- `wait`: Pause execution
- `done`: Task complete

### 7. TraceBuilder (`trace.py`)

**Purpose**: Build and serialize execution trace

**Output Format** (JSON):

```json
{
  "video": "apps/adaway/videos/handheld/hhv-001.mp4",
  "llm": "qwen2.5vl-7b",
  "video_type": "hhv",
  "app_name": "adaway",
  "generated_at": "2026-05-08T10:30:00+00:00",
  "video_mode": true,
  "replay_trace": [
    {
      "step_index": 1,
      "timestamp_sec": 1.333,
      "frame_file": "kf-0001.png",
      "screen_description": "AdAway home screen with Enable button",
      "action": {
        "action_type": "launch",
        "target": "app_entrypoint",
        "details": "App launched successfully"
      },
      "confidence": 0.95
    }
  ]
}
```

---

## Memory.md Format (Stage 1 Output)

### Structure

```markdown
# Task Memory: AdAway

## Task Summary
Enable the ad filtering feature in AdAway by toggling the main switch in the app's settings.

## Steps
1. Launch app → App opens with initial disabled state
2. Tap "Enable" button → Filter becomes active
3. Confirm in dialog → Filter status updates to enabled

## UI Elements
- Button: "Enable" (top-right corner)
- Toggle: "Status: Disabled" (center of screen)
- Text: "Filter is active" (appears after enabling)
- Dialog: "Enable filter?" (confirmation)

## Completion Criteria
- App shows "Status: Enabled"
- Filter icon changes to active state
- Toast message appears: "Filter activated"
```

### Why This Format?

✅ **Human-readable**: Easy to debug and understand  
✅ **Structured**: Clear sections for parsing  
✅ **Reusable**: Stage 2 can extract and use sections  
✅ **Extensible**: Can add more sections as needed  
✅ **Markdown**: Standard format, version-controllable  

---

## Configuration Files

### config.yml Example

```yaml
llm: "gemini"                                    # Provider
llm_model: "gemini-1.5-flash"                   # Optional: model name
video_mode: true                                # Enable memory generation
llm_prompt_file: "src_llm/input/prompts/llama_action_prompt_gemini_2.txt"

frame_sampling:
  strategy: "uniform"
  fps: 1.5
  max_frames: 100

keyframe_selection:
  method: "ssim"                                # Recommended
  min_gap_seconds: 1.0
  ssim_threshold: 0.95
  stable_threshold: 2

output:
  overwrite: true

runs:
  - app_name: "adaway"
    video_path: ["hhv", "srv"]                 # Shorthands or explicit paths
```

### .env.local Example

```bash
# Local Ollama (Llama, Qwen, LLaVA, Gemma, MiniCPM)
LLAMA_BASE_URL=http://localhost:11434/v1

# Cloud Gemini
GOOGLE_GENERATIVE_AI_API_KEY=your_api_key_here

# Optional: Custom timeouts
LLAMA_TIMEOUT_SEC=120
QWEN_TIMEOUT_SEC=180
```

---

## Workflow & Commands

### Both Stages (Recommended)

```bash
python -m src_llm.end_to_end \
  --config src_llm/input/config.yml \
  --env-file .env.local
```

Runs:
1. Stage 1: Analyzes video → generates memory.md
2. Stage 2: Uses memory → automates on device

### Stage 1 Only

```bash
python -m src_llm.end_to_end \
  --stage 1 \
  --config src_llm/input/config.yml \
  --env-file .env.local
```

Output: `memory.md` + `metadata.json`

### Stage 2 Only

```bash
python -m src_llm.end_to_end \
  --stage 2 \
  --config src_llm/input/config.yml \
  --env-file .env.local
```

Uses existing memory from prior Stage 1 run

### Dry-Run (Validation)

```bash
python -m src_llm.end_to_end \
  --dry-run \
  --config src_llm/input/config.yml \
  --env-file .env.local
```

Validates config and environment without processing

---

## Output Directory Structure

```
apps/{app}/llm/{model}/{video_type}-video-mode/run-NNN/

├── memory.md
│   └── Structured task description (Stage 1)
│
├── metadata.json
│   ├── Config used (llm, model, frame sampling)
│   ├── Timing and duration
│   ├── Status (success/failed/skipped)
│   └── memory_md_content (embedded for Stage 2)
│
├── execution_trace.json
│   └── Action sequence with timestamps and confidence
│
├── llm_raw_response.txt
│   └── Raw LLM output for debugging
│
├── frames_manifest.json
│   └── Metadata about sampled and selected keyframes
│
├── keyframes/
│   ├── kf-0001.png
│   ├── kf-0002.png
│   └── ...
│
└── logs/
    └── run.log (detailed execution log)
```

**Model Name Format**:
- Local: `{provider}{version}-{size}` (e.g., `qwen2.5vl-7b`)
- Cloud: `{provider}-{version}` (e.g., `gemini-1.5-flash`)

---

## Token Savings Analysis

### Traditional Approach (❌ Inefficient)

```
Task: Automate 5-step app workflow

1. Watch video → Analyze → Extract actions (6 LLM tokens)
2. Step 1 on device
   → Watch video AGAIN → Analyze (6 LLM tokens)
3. Step 2 on device
   → Watch video AGAIN → Analyze (6 LLM tokens)
4. Step 3 on device
   → Watch video AGAIN → Analyze (6 LLM tokens)
5. Step 4 on device
   → Watch video AGAIN → Analyze (6 LLM tokens)
6. Step 5 on device
   → Watch video AGAIN → Analyze (6 LLM tokens)

Total: 36 video analyses per task
Cost: Extremely high
```

### Two-Stage Approach (✅ Efficient)

```
Task: Automate 5-step app workflow

Stage 1: Watch video → Analyze ONCE → Generate memory (6 LLM tokens)
         Save to memory.md and metadata.json

Stage 2: Repeat 5 times:
         1. Load memory context (minimal tokens)
         2. Capture device screen (minimal tokens)
         3. Decide action (uses memory context, ~2 LLM tokens)
         4. Execute on device

Total: 1 video analysis + 5 context-light decisions
Cost: ~16 LLM tokens vs 36 (83% savings!)
```

### Real Numbers

| Metric | Traditional | Two-Stage | Savings |
|--------|------------|-----------|---------|
| Full video analyses | 6 | 1 | 83% ↓ |
| Memory context uses | 0 | 5 | - |
| Total LLM calls | 6 | 6 | - |
| Avg tokens per call | ~2000 | ~300 | **85% ↓** |
| **Total tokens** | **~12,000** | **~2,000** | **~83% ↓** |

---

## Supported LLM Models

### Local Models (Ollama)

| Model | Provider | Size | Speed | Best For |
|-------|----------|------|-------|----------|
| Llama 3.2 Vision | ollama | 7.8 GB | 🟢 Good | Baseline vision |
| Qwen 2.5-VL | ollama | 6.0 GB | 🟢 Good | M3 Pro (recommended) |
| LLaVA | ollama | 4.7 GB | 🟢🟢 Fast | Instruction following |
| MiniCPM | ollama | 5.5 GB | 🟢 Good | Dense UI analysis |
| Gemma 3 | ollama | 3.3 GB | 🟢🟢🟢 Very fast | Low latency |

### Cloud Models

| Model | Provider | Auth | Best For |
|-------|----------|------|----------|
| Gemini 1.5 Flash | Google | API key | Recommended (free tier) |
| Claude (stub) | Anthropic | API key | Future integration |

---

## Error Handling & Fallbacks

### What Happens When LLM Fails?

```
LLM Request
    ↓
    ├─ HTTP Error (429, 500, timeout)
    │  └─ Retry with exponential backoff (10s, 20s, 40s, ...)
    │     └─ Max 5 retries
    │
    ├─ Connection timeout
    │  └─ Retry with backoff
    │
    ├─ Unparseable JSON output
    │  └─ Use deterministic heuristic
    │
    └─ Success
       └─ Process response
```

### Deterministic Fallback Heuristic

If LLM provider fails or returns unparseable output:

```python
if frame_index == 0:
    action = "launch"  # First frame always launch
elif motion_score >= 18:
    action = "tap"     # High motion = user tapping
elif motion_score >= 9:
    action = "scroll"  # Medium motion = scrolling
else:
    action = "wait"    # Low motion = waiting for response
```

This ensures the pipeline never completely fails—fallback is deterministic but less intelligent.

---

## Key Design Decisions

### Why Two Separate Stages?

**✅ Flexibility**
- Run Stage 1 offline (on any machine)
- Stage 2 can run on device farm
- Decouple expensive video analysis from execution

**✅ Reusability**
- Analyze video once
- Reuse memory for multiple automation runs
- Memory is much cheaper than re-analyzing video

**✅ Parallelization**
- Multiple Stage 2 runs can use same memory
- Run different models on same video
- Test different automation strategies

### Why Embed Memory in metadata.json?

- Stage 2 doesn't need filesystem traversal
- Memory is preserved with all run metadata
- Easy to export and share run results
- Fast lookup during automation

### Why Flat Model Directory?

Instead of: `apps/{app}/llm/{provider}/{model}/...`  
Use: `apps/{app}/llm/{provider_model}/...`

**Pros**:
- Simpler paths
- Model names include provider
- No naming conflicts (e.g., both Ollama and API have "gemini")
- Easier to locate specific model outputs

---

## Getting Started

### 1. Install Dependencies

```bash
pip install -r src_llm/requirements.txt
```

### 2. Set Up Environment

```bash
# Copy example
cp .env.local.example .env.local

# Edit with your settings
nano .env.local
```

For **Ollama local models**:
```bash
LLAMA_BASE_URL=http://localhost:11434/v1
```

For **Gemini cloud**:
```bash
GOOGLE_GENERATIVE_AI_API_KEY=sk-...
```

### 3. Create Configuration

```bash
# Copy example config
cp src_llm/config.example.yml src_llm/input/config.yml

# Edit with your app details
nano src_llm/input/config.yml
```

### 4. Run Pipeline

```bash
python -m src_llm.end_to_end \
  --config src_llm/input/config.yml \
  --env-file .env.local
```

### 5. Check Output

```bash
# Find generated files
ls apps/your_app/llm/model_name/video_type-video-mode/run-001/

# View memory
cat apps/your_app/llm/model_name/video_type-video-mode/run-001/memory.md

# View logs
tail -f apps/your_app/llm/model_name/video_type-video-mode/run-001/logs/run.log
```

---

## Summary

**src_llm** is a powerful two-stage system that combines AI-driven video analysis with memory-based device automation. By separating these concerns, it achieves massive token savings while maintaining flexibility and modularity.

### Key Takeaways

✅ **Two-Stage Design**: Analyze video once, automate many times  
✅ **90% Token Savings**: Memory reuse is extremely cost-effective  
✅ **Flexible Providers**: Local and cloud models supported  
✅ **Easy Configuration**: Single YAML file for both stages  
✅ **Fallback Logic**: Pipeline continues even if LLM fails  
✅ **Structured Output**: memory.md is human-readable and parseable  

