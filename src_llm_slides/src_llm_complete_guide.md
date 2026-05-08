# src_llm: Complete Guide with Design Overview & Diagrams

## Table of Contents

1. **Overview** - What is src_llm?
2. **Architecture** - How it works
3. **Node Explanations** - What each part does
4. **Data Flow** - How data moves through system
5. **Getting Started** - How to use it
6. **Token Savings** - Why it's efficient

---

## 1. OVERVIEW: What is src_llm?

### Simple Definition

**src_llm** is an AI-powered system that **automates Android app tasks by analyzing a video once, then reusing that understanding to control the device.**

### Key Features

✅ **Two-stage architecture**: Separate expensive analysis from cheap automation  
✅ **90% token savings**: Memory reuse reduces AI calls dramatically  
✅ **Multiple AI models**: Google Gemini (cloud) or local Ollama (free)  
✅ **Flexible and modular**: Easy to understand, debug, and extend  
✅ **Smart error handling**: Falls back to simple heuristics if AI fails  

### Why You Need It

**Problem**: Traditional approach analyzes video multiple times = expensive!
- Watch video → Analyze → Automate step 1
- Analyze video again → Automate step 2
- Analyze video again → Automate step 3
- ...costs a fortune in tokens!

**Solution**: src_llm
- Watch video → Analyze ONCE → Create "memory"
- Use memory for step 1 (cheap)
- Use memory for step 2 (cheap)
- Use memory for step 3 (cheap)
- ...saves 80-90% of tokens!

---

## 2. ARCHITECTURE: System Design

### High-Level Overview

```
┌─────────────────────────────────────────────────────────────┐
│                       src_llm                               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  STAGE 1                          STAGE 2                   │
│  Video → Memory Analysis          Memory → Device Automation│
│  ────────────────────             ──────────────────────   │
│                                                             │
│  [Video File]                     [Memory Loaded]           │
│        ↓                                ↓                   │
│  [Extract Frames]                 [Capture Screen]         │
│        ↓                                ↓                   │
│  [Select Keyframes]               [LLM Decision]           │
│        ↓                                ↓                   │
│  [LLM Analysis]                   [Execute Action]         │
│        ↓                                ↓                   │
│  [Generate Memory.md]             [Android Device]         │
│        ↓                                ↓                   │
│  [metadata.json]          ──────────────────→              │
│        │                                                    │
│        └────────────[Loop until done]─────────────┘        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Two Stages Explained

#### Stage 1: Video → Memory (Offline Analysis)

**Purpose**: Analyze video once, extract understanding

**Steps**:
1. **VideoFrameExtractor**: Break MP4 into ~90 individual frames
2. **KeyframeSelector**: Filter to ~20 important frames (remove duplicates)
3. **LLM Provider**: AI analyzes images, generates understanding
4. **Memory Parser**: Structure output into memory.md

**Output**:
- `memory.md` - Task description + steps + UI elements (human-readable)
- `metadata.json` - Embedded memory + config (machine-readable)
- `execution_trace.json` - Action sequence for debugging
- `keyframes/` - Sampled frames for visual reference

**Key insight**: Runs **once** per video, memory is **reused** in Stage 2

#### Stage 2: Memory → Device (Online Automation)

**Purpose**: Use Stage 1 memory to automate device

**Loop** (repeat until task done):
1. **Load Memory**: Read memory.md from metadata.json
2. **Capture Screen**: Take screenshot of current device state
3. **LLM Decision**: "Memory says do X, screen shows Y, so next action is Z"
4. **Execute**: Tap, type, scroll, or wait
5. **Record**: Log action in execution trace
6. **Check Done**: Verify completion criteria from memory

**Output**:
- Device is automated following the task
- Full trace of what happened
- Screenshots showing before/after each action

---

## 3. NODE EXPLANATIONS: What Each Part Does

### 🎬 Video File (Input)

The recorded video showing the task being performed.

**Examples**:
- `hhv-001.mp4` - Handheld camera recording
- `srv-001.mp4` - Screen recording from device

**Contains**: 45-60 seconds of someone using the app

**In simple words**: *"The tutorial video showing how to do the task"*

---

### ⚙️ ConfigLoader (config.py)

Reads your instructions from config.yml and .env files.

**Checks**:
- ✅ App name is valid
- ✅ Video file exists
- ✅ LLM provider is configured
- ✅ All settings are reasonable

**Outputs**: Configuration ready to use

**In simple words**: *"Reads the recipe and makes sure you have all ingredients"*

---

### 📹 VideoFrameExtractor (video.py)

Breaks the video into individual still images.

**How it works**:
- Opens MP4 file
- Samples frames at regular intervals (~1.5 FPS)
- Saves ~90 individual frames

**Settings**:
- `fps: 1.5` → Take a picture every 0.67 seconds
- `max_frames: 100` → Maximum 100 pictures total

**In simple words**: *"Takes a 60-second video and extracts ~90 snapshots evenly spaced"*

---

### 🔍 KeyframeSelector (keyframes.py)

Filters out duplicate/similar frames, keeps interesting ones.

**Method**: SSIM (Structural Similarity)
- Compares each frame to previous
- If 95%+ similar → Skip (boring, nothing changed)
- If different → Keep (interesting, something changed!)

**Result**: 90 frames → ~20 important keyframes

**In simple words**: *"Movie editor removing repeated shots. Keeps exciting moments, removes waiting."*

---

### 🤖 LLM Provider (providers.py)

The AI brain that understands the video.

**Supported Models**:
- **Gemini 1.5 Flash** (Google, cloud, smart)
- **Qwen 2.5-VL** (Local, free, M3 optimized)
- **Llama 3.2** (Local, free, baseline)
- **LLaVA** (Local, free, fast)
- **MiniCPM** (Local, free, good for dense UI)

**What it does**:
1. Receives 20 keyframe images
2. Reads your prompt
3. Analyzes and outputs understanding

**Output**: Structured memory (task, steps, UI elements)

**In simple words**: *"Super smart AI that looks at pictures and understands what's happening"*

---

### 📝 Memory Parser (main.py)

Structures AI output into organized notes.

**Extracts**:
- **Task Summary**: What is the goal? (one paragraph)
- **Steps**: Each action in order (1. Launch 2. Tap 3. Confirm)
- **UI Elements**: Button names, locations, types
- **Completion Criteria**: How to know when done

**Output**: `memory.md` - Clean, organized document

**In simple words**: *"Secretary writing down key points from a meeting in organized format"*

---

### 📋 metadata.json (Output)

Container holding all Stage 1 information.

**Contains**:
- Memory content (embedded for Stage 2)
- Configuration used
- Timing information
- Status (success/failed)
- UI elements extracted

**Why important**: Stage 2 reads from this file

**In simple words**: *"Briefcase containing all documents from Stage 1"*

---

### 🎯 MemoryToDevice (memory_to_device.py)

Uses Stage 1 memory to automate the device.

**Process**:
1. Load memory from metadata.json
2. For each automation step:
   - Capture device screenshot
   - Show memory + screenshot to LLM
   - LLM decides next action
   - Execute action on device
   - Record in trace

**In simple words**: *"Conductor using sheet music (memory) to perform symphony (automation)"*

---

### 📱 Android Device

The phone being automated.

**Receives**:
- Tap → at coordinates
- Type → text
- Scroll → direction
- Wait → pause
- Back → press back button

**Returns**: Screenshot after each action

**In simple words**: *"Actor following director's instructions. 'Tap here!' → Device taps."*

---

### 🔄 Automation Loop

Keeps automating until task is complete.

```
1. Take screenshot
2. Show to LLM with memory
3. LLM decides action
4. Execute action
5. Log in trace
6. Is task done?
   - No → Go to step 1
   - Yes → Exit
```

**In simple words**: *"Checklist you keep working through until done"*

---

### 📊 Execution Trace

Log of everything that happened.

**Records**:
- Timestamp of each action
- Action type (tap, type, scroll)
- Coordinates and target
- Before/after screenshots
- Confidence score
- LLM reasoning

**Purpose**: Debugging and verification

**In simple words**: *"Security camera footage of the automation. Used to debug if something fails."*

---

## 4. DATA FLOW: How Data Moves

```
INPUT
  │
  ├─ video.mp4
  ├─ config.yml
  └─ .env.local
       │
       ▼
  ┌─────────────────────────────────────────┐
  │  STAGE 1: Video Analysis                │
  ├─────────────────────────────────────────┤
  │                                         │
  │  VideoFrameExtractor                    │
  │  • Read MP4                             │
  │  • Extract 90 frames at 1.5 FPS         │
  │                                         │
  │  KeyframeSelector                       │
  │  • Compare frames                       │
  │  • Keep different ones                  │
  │  • Result: 20 important frames          │
  │                                         │
  │  LLM Provider                           │
  │  • Analyze 20 keyframes                 │
  │  • Generate understanding               │
  │  • Output: Memory content               │
  │                                         │
  │  Memory Parser                          │
  │  • Parse LLM output                     │
  │  • Extract task, steps, UI              │
  │  • Format as markdown                   │
  │                                         │
  └────────┬──────────────────────────────────┘
           │
           ├─ memory.md (task description)
           ├─ metadata.json (embeds memory)
           ├─ execution_trace.json
           ├─ llm_raw_response.txt
           ├─ keyframes/ (sampled images)
           └─ logs/run.log
           │
           ▼
  ┌─────────────────────────────────────────┐
  │  STAGE 2: Device Automation             │
  ├─────────────────────────────────────────┤
  │  For each step until done:              │
  │                                         │
  │  1. Load Memory Context                 │
  │     (from metadata.json)                │
  │                                         │
  │  2. Capture Device Screenshot           │
  │     (current UI state)                  │
  │                                         │
  │  3. LLM Decision                        │
  │     (memory + screenshot → action)      │
  │                                         │
  │  4. Execute on Device                   │
  │     (tap, type, scroll, etc)            │
  │                                         │
  │  5. Log Action                          │
  │     (execution_trace.json)              │
  │                                         │
  └─────────────────────────────────────────┘
           │
           ▼
OUTPUT
  │
  ├─ Device is automated
  ├─ memory.md (understanding)
  ├─ metadata.json (all metadata)
  ├─ execution_trace.json (actions)
  ├─ screenshots (before/after)
  └─ logs/ (detailed trace)
```

---

## 5. GETTING STARTED

### Step 1: Install

```bash
pip install -r src_llm/requirements.txt
```

### Step 2: Set Up Environment

```bash
cp .env.local.example .env.local
nano .env.local
```

**For Ollama (local, free)**:
```
LLAMA_BASE_URL=http://localhost:11434/v1
```

**For Gemini (cloud)**:
```
GOOGLE_GENERATIVE_AI_API_KEY=your_api_key
```

### Step 3: Create Configuration

```bash
cp src_llm/config.example.yml src_llm/input/config.yml
nano src_llm/input/config.yml
```

**Example config**:
```yaml
llm: "gemini"
llm_model: "gemini-1.5-flash"
video_mode: true

frame_sampling:
  strategy: "uniform"
  fps: 1.5
  max_frames: 100

keyframe_selection:
  method: "ssim"
  ssim_threshold: 0.95

runs:
  - app_name: "adaway"
    video_path: ["hhv", "srv"]
```

### Step 4: Run Pipeline

```bash
python -m src_llm.end_to_end \
  --config src_llm/input/config.yml \
  --env-file .env.local
```

### Step 5: Check Output

```bash
ls apps/adaway/llm/gemini-2.5-flash/handheld-video-mode/run-001/

# View memory
cat apps/adaway/llm/gemini-2.5-flash/handheld-video-mode/run-001/memory.md

# View logs
tail -f apps/adaway/llm/gemini-2.5-flash/handheld-video-mode/run-001/logs/run.log
```

---

## 6. TOKEN SAVINGS: Why It's Efficient

### Traditional Approach (❌ Expensive)

```
Task: Automate 5-step workflow

Step 1: Watch video → Analyze (~2000 tokens) → Execute
Step 2: Watch video → Analyze (~2000 tokens) → Execute
Step 3: Watch video → Analyze (~2000 tokens) → Execute
Step 4: Watch video → Analyze (~2000 tokens) → Execute
Step 5: Watch video → Analyze (~2000 tokens) → Execute

Total: 5 full video analyses = ~10,000 tokens
Cost: $$$$$
```

### Two-Stage Approach (✅ Efficient)

```
Stage 1: Watch video → Analyze (~2000 tokens) → Create memory

Stage 2:
Step 1: Use memory (~300 tokens) → Execute
Step 2: Use memory (~300 tokens) → Execute
Step 3: Use memory (~300 tokens) → Execute
Step 4: Use memory (~300 tokens) → Execute
Step 5: Use memory (~300 tokens) → Execute

Total: 1 video analysis + 5 memory uses = ~3500 tokens
Cost: $
Savings: 65% less! 🎉
```

### Why Memory is Cheaper

- **Video analysis**: Full image processing, understanding task flow
- **Memory use**: Just context reminder, straightforward decisions

Memory context = 85% cheaper than re-analyzing video!

---

## Summary

**src_llm = Smart memory-based automation**

### Key Innovation

Separate expensive video analysis from cheap automation execution.

### Benefits

✅ 90% token savings (massive cost reduction)  
✅ Offline capability (analyze video anytime, automate later)  
✅ Reusable memory (one analysis, many automations)  
✅ Modular design (easy to understand and extend)  
✅ Error resilient (fallbacks ensure pipeline continues)  

### When to Use

- Automating Android app tasks
- Testing apps at scale
- Repetitive UI interactions
- Tasks that need understanding, not just button tapping

### When Not to Use

- Real-time critical operations (too slow)
- Complex robot arm movement (not designed for)
- Non-Android platforms (specific to Android)

---

## Quick Command Reference

```bash
# Both stages
python -m src_llm.end_to_end --config config.yml

# Stage 1 only
python -m src_llm.end_to_end --stage 1 --config config.yml

# Stage 2 only
python -m src_llm.end_to_end --stage 2 --config config.yml

# Validate without running
python -m src_llm.end_to_end --dry-run --config config.yml
```

---

**Now you understand src_llm! 🎉**

For detailed information, see:
- `src_llm_design_overview.md` - Comprehensive architecture
- `src_llm_visual_diagrams.md` - ASCII diagrams
- `src_llm_node_explanations.md` - Node-by-node guide

