# src_llm Architecture: Node-by-Node Explanations

## Simple, Easy-to-Understand Guide

---

## 🎯 Main Nodes Explained

### 1. **Video File** (Input)

**What it is**: The MP4 video file you want to automate

**Where it comes from**: 
- `apps/{app}/videos/handheld/hhv-001.mp4` (handheld camera recording)
- `apps/{app}/videos/screenrec/srv-001.mp4` (screen recording)

**What it contains**:
- 45-60 seconds of app interaction
- User performs the task you want to automate
- Examples: Enable feature, login, fill form

**In simple words**: 
> "This is the recorded video showing someone doing the task. Like a tutorial video of 'how to enable the filter'."

---

### 2. **ConfigLoader** (config.py)

**What it does**: Reads your setup instructions

**Reads from**:
- `config.yml` - Your task instructions
- `.env.local` - Your API keys

**Checks**:
- ✅ Is the app name valid?
- ✅ Does the video file exist?
- ✅ Is the LLM provider available?
- ✅ Are all settings correct?

**Output**: A configuration object ready to use

**In simple words**:
> "Like reading a recipe before cooking. It makes sure you have all ingredients and the instructions make sense."

---

### 3. **VideoFrameExtractor** (video.py)

**What it does**: Breaks the video into individual pictures

**Process**:
1. Opens the MP4 file
2. Reads every frame (like flipping through comic book panels)
3. Takes pictures at regular intervals (every ~0.7 seconds)
4. Stores them temporarily for analysis

**Settings**:
- `fps: 1.5` → Take 1-2 pictures per second
- `max_frames: 100` → Maximum 100 pictures total

**Output**: List of 50-100 individual image frames

**In simple words**:
> "Takes a 60-second video and extracts about 90 still pictures evenly spaced throughout. Like taking snapshots of a movie every second."

---

### 4. **KeyframeSelector** (keyframes.py)

**What it does**: Filters out duplicate/boring pictures, keeps important ones

**How it works**:
- Compares each picture to the previous one
- Uses SSIM (Structural Similarity) - fancy way of comparing images
- If pictures look 95% the same → Skip it (probably just waiting)
- If pictures look different → Keep it (something changed!)

**Example**:
```
Picture 1 (app launches)         ✅ KEEP (different from previous)
Picture 2 (loading screen)       ❌ SKIP (similar to pic 1)
Picture 3 (still loading)        ❌ SKIP (similar to pic 1-2)
Picture 4 (screen changed!)      ✅ KEEP (different!)
Picture 5 (transition effect)    ❌ SKIP (similar to pic 4)
Picture 6 (final screen)         ✅ KEEP (different!)
```

**Output**: 15-25 important keyframes (vs original 90)

**In simple words**:
> "Like a movie editor removing repeated shots. Keeps interesting moments, removes boring repetition. Result: 90 pictures → 20 important ones."

---

### 5. **LLM Provider** (providers.py)

**What it does**: The AI/smart part. Analyzes pictures and understands the task

**Types of providers**:
- **Gemini** (Google Cloud) - Very smart, needs API key
- **Qwen, Llama, LLaVA** (Local via Ollama) - Free, runs on your machine
- **MiniCPM, Gemma** (Local) - Fast, good for phones

**What it receives**:
- 20 keyframe images
- Your prompt: "Analyze these screenshots and describe what's happening"

**What it outputs**:
- Structured memory (task, steps, UI elements)
- Action sequence (what the user did)
- Confidence scores (how sure it is)

**In simple words**:
> "The AI brain that looks at the 20 pictures and understands: 'The user opened the app, then tapped the Enable button.' Very intelligent understanding!"

---

### 6. **Memory Parser** (main.py)

**What it does**: Takes AI output and structures it into organized notes

**Extracts from LLM output**:
- **Task Summary**: What is being done? (one paragraph)
- **Steps**: Each action in order (1. Launch, 2. Tap, 3. Confirm)
- **UI Elements**: Button names and locations
- **Completion Criteria**: How to know when done

**Creates**: `memory.md` - A nicely formatted document

**Output example**:
```markdown
# Task Memory: Enable AdAway

## Task Summary
Enable the ad filtering feature in AdAway.

## Steps
1. Launch app → Shows initial screen
2. Tap "Enable" button → Filter activates
3. Confirm → Done!

## UI Elements
- Button: "Enable" (top-right)
- Text: "Status" (center)

## Completion Criteria
- Shows "Enabled"
```

**In simple words**:
> "Takes messy AI output and turns it into clean, organized notes. Like a secretary writing down the key points from a meeting."

---

### 7. **metadata.json** (Output)

**What it is**: A container holding all run information

**Contains**:
- The memory.md content (embedded)
- Configuration used
- Timing information
- Status (success/failed)
- UI elements extracted
- Task description

**Why it's important**: 
- Stage 2 reads from this file
- All info is in one place
- Easy to export and share

**In simple words**:
> "Like a briefcase containing all important documents from Stage 1. Stage 2 opens this briefcase and uses the memory inside."

---

### 8. **MemoryToDevice** (memory_to_device.py)

**What it does**: Takes Stage 1 memory and uses it to automate the device

**Process**:
1. Opens the metadata.json from Stage 1
2. Extracts the memory content
3. Connects to Android device
4. Reads the memory context
5. For each step:
   - Take a screenshot
   - Show memory + screenshot to LLM
   - LLM decides next action
   - Execute action on device

**In simple words**:
> "The conductor using the sheet music (memory) to perform the symphony (automation). Looks at memory, looks at current state, decides next move."

---

### 9. **Android Device** (Physical/Emulator)

**What it is**: The phone being automated

**What happens**:
1. Receives tap coordinates → Taps screen
2. Receives text → Types it
3. Receives scroll → Scrolls screen
4. Receives wait → Pauses
5. Returns screenshot after each action

**In simple words**:
> "The actor following the director's (LLM's) instructions. 'Tap here!' → Device taps. 'Type this!' → Device types. 'Show me current state' → Device takes screenshot."

---

### 10. **Automation Loop** (Repeat until done)

**What it does**: Keeps automating until task is complete

**Each iteration**:

```
┌─────────────────────────────────────┐
│ 1. Take device screenshot            │
│ 2. Show to LLM with memory context   │
│ 3. LLM decides next action           │
│ 4. Execute action on device          │
│ 5. Record in trace                   │
│ 6. Check: Is task complete?          │
│    ├─ NO → Go to step 1 again       │
│    └─ YES → Exit loop               │
└─────────────────────────────────────┘
```

**In simple words**:
> "Like a checklist you keep working through. After each action, check: 'Are we done yet?' If no, do the next action. If yes, stop."

---

### 11. **Execution Trace** (execution_trace.json)

**What it records**:
- Timestamp of each action
- Action type (tap, type, scroll)
- Target and coordinates
- Screenshot before and after
- Confidence score
- Reasoning from LLM

**Purpose**: 
- Debugging (what went wrong?)
- Verification (what happened?)
- Playback (replay the automation)

**In simple words**:
> "A complete log/recording of everything that happened. Like a security camera footage of the automation. Used for debugging if something fails."

---

## 🔄 The Complete Flow (Simplified)

```
START
  │
  ▼
User provides: video.mp4 + config.yml + .env.local
  │
  ▼
STAGE 1: Video → Memory
  1. Extract frames from video (90 pictures)
  2. Filter to important ones (20 pictures)
  3. Show to AI for analysis
  4. AI creates memory.md (task + steps + UI)
  5. Save to memory.md + metadata.json
  │
  ▼
STAGE 2: Memory → Device
  1. Load memory from metadata.json
  2. Connect to Android device
  3. Loop until task done:
     a. Take screenshot
     b. Show memory + screenshot to AI
     c. AI decides action
     d. Execute on device
     e. Log in trace
  │
  ▼
END
  Output: Automated device + memory.md + trace.json
```

---

## 💡 Key Insights (Why This Design?)

### Why Two Stages?

**Traditional (bad)**:
- Analyze video → Do step 1 → Analyze video again → Do step 2 → Analyze video again...
- Video analyzed 6+ times per task
- Very expensive!

**Two-Stage (good)**:
- Analyze video ONCE → Generate memory
- Use memory for all automation steps
- Memory is 85% cheaper than re-analyzing video
- Do more with less!

**In simple words**:
> "Don't repeat yourself. Analyze the video once, then reuse that understanding many times. Like reading a recipe once, then following it step-by-step without re-reading."

---

### Why Separate Memory?

**Good reasons**:
1. **Reusable**: Use same memory for multiple automation runs
2. **Debuggable**: Can read human-friendly memory.md
3. **Shareable**: Export memory and share with others
4. **Offline**: Stage 1 can run offline, Stage 2 later
5. **Modular**: Each stage can be improved independently

**In simple words**:
> "Like writing a lesson plan once, then using it to teach many classes. Don't re-plan for every class!"

---

### Why Different LLM Providers?

**Choice flexibility**:
- **Gemini (Cloud)**: Very smart, needs internet, costs money
- **Llama (Local)**: Free, runs on your machine, no internet needed
- **Qwen (Local)**: Good balance, works great on M3 Macs
- **MiniCPM (Local)**: Excellent for dense UI analysis

**In simple words**:
> "Different tools for different jobs. Use cloud AI for complex tasks, use local AI for privacy/cost."

---

### Why Error Handling?

**Real world problems**:
- Internet can be slow (timeout)
- API can be overloaded (HTTP 429)
- LLM can hallucinate (bad output)

**Solution**:
- Retry failed requests with delays
- Fallback to simple heuristic if AI fails
- Never completely fail

**In simple words**:
> "Like a backup plan. If the fancy plan fails, have a simpler plan ready. Always keep going!"

---

## 📊 Complexity Breakdown

### Easy Parts
- ✅ Extract video frames (standard video library)
- ✅ Compare images (standard image comparison)
- ✅ Tap on device (standard Android library)
- ✅ Log actions (standard file I/O)

### Smart Parts
- 🧠 LLM analysis (requires cloud/local AI)
- 🧠 Memory context (requires prompt engineering)
- 🧠 Decision making (requires understanding)

### Hard Parts
- 🚀 Handling errors gracefully
- 🚀 Supporting multiple providers
- 🚀 Optimal keyframe selection
- 🚀 Accurate action coordination

---

## 🎓 Learning Path

If you're new to src_llm, understand in this order:

1. **Memory concept** (Stage 1 output)
   - Read a sample `memory.md` file
   - Understand: task + steps + UI elements

2. **Configuration** (How to set it up)
   - Understand `config.yml` structure
   - Understand `.env.local` purpose

3. **Two-Stage flow** (Overall architecture)
   - Stage 1: Video → Memory
   - Stage 2: Memory → Device

4. **Components** (Individual pieces)
   - VideoFrameExtractor
   - KeyframeSelector
   - LLM Provider
   - MemoryToDevice

5. **Token savings** (Why it's efficient)
   - Understand memory reuse
   - Compare traditional vs two-stage

6. **Error handling** (Edge cases)
   - Retry logic
   - Fallback heuristics

---

## 🎯 Quick Reference

| Node | Purpose | Input | Output |
|------|---------|-------|--------|
| VideoFrameExtractor | Break video into frames | MP4 file | 90 frames |
| KeyframeSelector | Filter to important frames | 90 frames | 20 keyframes |
| LLM Provider | Analyze frames, create memory | 20 keyframes | memory content |
| Memory Parser | Structure output | LLM text | memory.md |
| metadata.json | Container for Stage 1 output | memory + config | JSON file |
| MemoryToDevice | Use memory to automate | metadata.json | device actions |
| Execution Trace | Log all actions | actions | JSON trace |

---

## Final Thought

**src_llm = Smart memory-based automation**

```
Old way: Watch, analyze, act, watch again, analyze again, act again...
         Boring and expensive!

New way: Watch once, remember, act, act, act, act...
         Smart and cheap!
```

The core innovation: **Separate expensive analysis from cheap execution.**

