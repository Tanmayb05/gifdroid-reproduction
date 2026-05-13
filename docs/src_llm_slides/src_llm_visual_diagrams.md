# src_llm Visual Diagrams & Architecture

## 1. Complete System Architecture

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                            src_llm System                                    ║
╚══════════════════════════════════════════════════════════════════════════════╝

                         ┌─────────────────────┐
                         │   Input Files       │
                         ├─────────────────────┤
                         │ • config.yml        │
                         │ • .env.local        │
                         │ • video.mp4         │
                         └────────┬────────────┘
                                  │
                    ╔═════════════╩═════════════╗
                    │                           │
        ╔═══════════▼════════════╗   ╔═════════▼══════════════╗
        │   STAGE 1              │   │   STAGE 2              │
        │ Video → Memory         │   │ Memory → Device        │
        ├───────────────────────┤   ├──────────────────────┤
        │                       │   │                      │
        │ 1️⃣  VideoExtractor   │   │ 1️⃣  Load Memory     │
        │    Extract frames     │   │    From metadata.json  │
        │                       │   │                      │
        │ 2️⃣  KeyframeSelector │   │ 2️⃣  Capture Screen  │
        │    Select important   │   │    Current device UI   │
        │                       │   │                      │
        │ 3️⃣  LLM Provider     │   │ 3️⃣  LLM Decision    │
        │    Analyze frames     │   │    Based on memory     │
        │    Generate memory    │   │                      │
        │                       │   │ 4️⃣  Execute Action  │
        │ 4️⃣  Write Output     │   │    tap/type/scroll     │
        │    memory.md          │   │                      │
        │    metadata.json      │   │ 5️⃣  Loop Until Done │
        │                       │   │                      │
        └───────────┬───────────┘   └──────────┬──────────┘
                    │                           │
                    │   Shared Data             │
                    └───────────┬───────────────┘
                                │
                    ┌───────────▼────────────┐
                    │  Output Directory      │
                    ├────────────────────────┤
                    │ run-NNN/               │
                    │ ├─ memory.md           │
                    │ ├─ metadata.json       │
                    │ ├─ keyframes/          │
                    │ ├─ execution_trace.json│
                    │ └─ logs/               │
                    └────────────────────────┘
```

---

## 2. Data Flow Diagram

```
                            VIDEO FILE
                                │
                    ┌───────────▼───────────┐
                    │ VideoFrameExtractor   │
                    │ • Read MP4            │
                    │ • Sample @ 1.5 FPS    │
                    │ • Extract ~150 frames │
                    └───────────┬───────────┘
                                │
                    ┌───────────▼──────────────┐
                    │ KeyframeSelector       │
                    │ Method: SSIM           │
                    │ • Compare frame pairs  │
                    │ • Threshold: 0.95      │
                    │ • Output: ~20 keyframes│
                    └───────────┬──────────────┘
                                │
                    ┌───────────▼──────────────┐
                    │ LLM Provider           │
                    │ Gemini/Qwen/Llama      │
                    │ • Send keyframes       │
                    │ • Analyze structure    │
                    │ • Extract task info    │
                    └───────────┬──────────────┘
                                │
                    ┌───────────▼──────────────┐
                    │ Memory Parser          │
                    │ • Extract sections     │
                    │ • Parse steps          │
                    │ • Extract UI elements  │
                    └───────────┬──────────────┘
                                │
                    ┌───────────▼──────────────┐
                    │ MEMORY.MD OUTPUT       │
                    │ ────────────────────   │
                    │ # Task Summary         │
                    │ - One paragraph goal   │
                    │                        │
                    │ ## Steps               │
                    │ 1. Launch → Start      │
                    │ 2. Tap → Enable btn    │
                    │                        │
                    │ ## UI Elements         │
                    │ - Button: Enable       │
                    │ - Text: Status         │
                    │                        │
                    │ ## Completion          │
                    │ - Status shows enabled │
                    └────────────┬───────────┘
                                 │
                                 │ STAGE 2 BEGINS
                                 │
                    ┌────────────▼────────────┐
                    │ Load Memory Context     │
                    │ • Read metadata.json    │
                    │ • Extract memory_md     │
                    │ • Understand task      │
                    └────────────┬────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │ Capture Device Screen   │
                    │ • Screenshot current UI │
                    │ • Extract elements     │
                    │ • Analyze layout       │
                    └────────────┬────────────┘
                                 │
                    ┌────────────▼─────────────┐
                    │ LLM Decision Making      │
                    │ Inputs:                  │
                    │ • Memory (task, steps)   │
                    │ • Current screen         │
                    │ • Previous actions       │
                    │ Output:                  │
                    │ • Next action type       │
                    │ • Target coordinates     │
                    │ • Text to type (if any)  │
                    └────────────┬─────────────┘
                                 │
                    ┌────────────▼─────────────┐
                    │ Execute on Device        │
                    │ • Tap at coordinates     │
                    │ • Type text              │
                    │ • Scroll direction       │
                    │ • Wait for response      │
                    │ • Capture new screen     │
                    └────────────┬─────────────┘
                                 │
                          [Is task done?]
                           /           \
                        No/              \Yes
                        /                  \
                    [Loop]          [AUTOMATION COMPLETE]
                    Return to        Output: execution_trace.json
                   Capture Screen
```

---

## 3. Component Interaction Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                     Configuration System                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  config.yml                        .env.local                   │
│  ┌───────────────────────┐  ┌──────────────────────┐           │
│  │ app_name: adaway      │  │ GOOGLE_API_KEY=...   │           │
│  │ llm: gemini           │  │ LLAMA_BASE_URL=...   │           │
│  │ video_path: hhv       │  │ QWEN_TIMEOUT_SEC=120 │           │
│  │ llm_model: gem 2.5-f  │  │ LLAMA_PREREQ_CHECK=1 │           │
│  │ video_mode: true      │  └──────────────────────┘           │
│  │ frame_sampling:       │                                      │
│  │   fps: 1.5            │                                      │
│  │   strategy: uniform   │                                      │
│  │ keyframe_selection:   │                                      │
│  │   method: ssim        │                                      │
│  │   threshold: 0.95     │                                      │
│  └───────────────────────┘                                      │
│           │                    │                                │
└───────────┼────────────────────┼────────────────────────────────┘
            │                    │
            ▼                    ▼
┌──────────────────────────────────────────────────────────────────┐
│                   ConfigLoader                                   │
│  Parse YAML → Validate settings → Return PipelineConfig         │
└──────────────┬───────────────────────────────────────────────────┘
               │
        ┌──────┴──────────────────────┐
        │                             │
        ▼ (STAGE 1)                   ▼ (STAGE 2)
┌──────────────────────┐      ┌──────────────────────┐
│  VideoFrameExtractor │      │  MemoryToDevice      │
│  ────────────────    │      │  ────────────────    │
│  • Read video.mp4    │      │  • Locate Stage 1    │
│  • Extract frames    │      │  • Load metadata.json│
│  • Output: Frames[]  │      │  • Parse memory.md   │
└──────┬───────────────┘      │  • Capture screen    │
       │                      │  • Call LLM provider │
       ▼                      │  • Execute actions   │
┌──────────────────────┐      └──────────┬───────────┘
│  KeyframeSelector    │                 │
│  ────────────────    │          [Loop until done]
│  • Compare frames    │                 │
│  • Filter stable     │                 ▼
│  • Output: Keyframes │      ┌──────────────────────┐
└──────┬───────────────┘      │  Automation Device   │
       │                      │  ────────────────    │
       ▼                      │  • uiautomator2      │
┌──────────────────────┐      │  • Execute taps      │
│  LLM Provider        │      │  • Type text         │
│  ────────────────    │      │  • Scroll            │
│  • Gemini (API)      │      │  • Capture screen    │
│  • Qwen (Ollama)     │      └──────────────────────┘
│  • Llama (Ollama)    │
│  • LLaVA (Ollama)    │
│  • MiniCPM (Ollama)  │
│  • Gemma (Ollama)    │
│  • HTTP/Ollama calls │
│  • Error recovery    │
└──────┬───────────────┘
       │
       ▼
┌──────────────────────┐
│  Memory Parser       │
│  ────────────────    │
│  • Extract sections  │
│  • Parse markdown    │
│  • Build dict        │
└──────┬───────────────┘
       │
       ▼
┌──────────────────────┐
│  TraceBuilder        │
│  ────────────────    │
│  • Serialize steps   │
│  • Build JSON        │
│  • Metadata embed    │
└──────┬───────────────┘
       │
       ▼
┌──────────────────────────────────────────────────────────────────┐
│                   Output Files                                   │
├──────────────────────────────────────────────────────────────────┤
│ • memory.md ..................... Task description              │
│ • metadata.json ................. Run config + memory content   │
│ • execution_trace.json .......... Action sequence              │
│ • llm_raw_response.txt .......... Debug info                   │
│ • keyframes/ .................... Frame samples                │
│ • logs/run.log .................. Execution log                │
└──────────────────────────────────────────────────────────────────┘
```

---

## 4. Stage 1: Video Analysis Pipeline

```
╔════════════════════════════════════════════════════════════════╗
║           STAGE 1: Video → Memory Analysis                    ║
╚════════════════════════════════════════════════════════════════╝

Input: video.mp4 (handheld or screenrec)
       ↓
       ├─ Duration: 45 seconds
       ├─ FPS: 30
       ├─ Resolution: 1920x1080
       └─ Total frames: 1350

Step 1️⃣ : Frame Extraction
       ├─ Strategy: uniform (fixed intervals)
       ├─ Target FPS: 1.5
       ├─ Max frames: 100
       └─ Output: 68 sampled frames at regular intervals

Step 2️⃣ : Keyframe Selection
       ├─ Method: SSIM (Structural Similarity)
       ├─ Threshold: 0.95 (very similar = skip)
       ├─ Min gap: 1.0 second
       ├─ Stable threshold: 2
       │
       └─ Process:
          Frame 0  (t=0s) ──► [KEYFRAME 1] - app starts
          Frame 2  (t=1.3s)  [compare] similar, skip
          Frame 4  (t=2.6s)  [KEYFRAME 2] - screen changed
          Frame 6  (t=3.9s)  [compare] similar, skip
          ...
          Frame 52 (t=34.6s) [KEYFRAME 18] - final state
       │
       └─ Output: 18 keyframes (98% reduction!)

Step 3️⃣ : LLM Analysis
       ├─ Provider: Gemini (cloud) or Qwen (local)
       ├─ Model: gemini-1.5-flash (cloud)
       ├─ Encoding: Base64 JPEG
       ├─ Temperature: 0.1 (deterministic)
       │
       └─ Prompt sends:
          [TASK DESCRIPTION]
          [18 keyframes as images]
          [Instructions: Analyze and output memory.md]

Step 4️⃣ : Memory Generation
       ├─ LLM outputs structured response:
       │
       │  # Task Memory: AdAway
       │  
       │  ## Task Summary
       │  Enable the ad filtering feature by toggling main switch.
       │  
       │  ## Steps
       │  1. Launch app → App appears with initial screen
       │  2. Tap Enable button → Filter status changes
       │  3. Confirm dialog → Feature is now active
       │  
       │  ## UI Elements
       │  - Button: "Enable" at top-right
       │  - Toggle: "Status: Disabled" in center
       │  - Text: "Filter active" appears after enable
       │  
       │  ## Completion Criteria
       │  - Status shows "Enabled"
       │  - UI updates to show active state
       │
       └─ Output files:
          memory.md ..................... Markdown (human-readable)
          metadata.json ................. JSON (machine-readable)
          llm_raw_response.txt .......... Raw LLM output
          execution_trace.json .......... Action sequence
          keyframes/ .................... Frame images
          logs/run.log .................. Detailed logs

═════════════════════════════════════════════════════════════════

Stage 1 Output Summary:
  ✅ memory.md created (task description + steps + UI)
  ✅ memory embedded in metadata.json for Stage 2
  ✅ Keyframes saved for debugging
  ✅ Full trace of what LLM analyzed
  ✅ Ready for Stage 2!
```

---

## 5. Stage 2: Device Automation Pipeline

```
╔════════════════════════════════════════════════════════════════╗
║         STAGE 2: Memory → Device Automation                   ║
╚════════════════════════════════════════════════════════════════╝

Input: metadata.json from Stage 1 + Android device
       ↓
       ├─ memory.md content (embedded in metadata)
       ├─ Android device (connected via USB)
       └─ Ready to automate!

Step 0️⃣ : Load Memory Context
       ├─ Locate Stage 1 output:
       │  apps/adaway/llm/gemini-2.5-pro/handheld-video-mode/run-001/
       │
       ├─ Load metadata.json
       │  {
       │    "memory_md_content": "# Task Memory: AdAway\n...",
       │    "task_description": "Enable ad filtering",
       │    "ui_elements": {"Enable": "tap", "Status": "text"},
       │    ...
       │  }
       │
       └─ Memory loaded! Context ready for automation.

Loop: For each automation step...
════════════════════════════════════════════════════════════════

Step 1️⃣ : Capture Current Screen
       ├─ Take screenshot of device
       ├─ Size: 1080x1920 pixels
       ├─ Format: PNG
       └─ Extract visible UI elements

Step 2️⃣ : Prepare LLM Input
       ├─ Memory context:
       │  Task: Enable ad filtering
       │  Steps: Launch → Tap Enable → Confirm
       │  UI Elements: Button "Enable" at top-right
       │
       ├─ Current screen:
       │  [Screenshot PNG]
       │  Visible elements: 5 buttons, 3 text fields, 1 toggle
       │
       └─ LLM request:
          "Based on this task and memory, what should we do next?"

Step 3️⃣ : LLM Decision
       ├─ LLM analyzes:
       │  1. Memory says: "Tap Enable button"
       │  2. Screen shows: Enable button visible at top-right
       │  3. Decision: Tap the button
       │
       └─ Output:
          {
            "action": "tap",
            "target": "Enable button",
            "coordinates": [1000, 120],
            "reasoning": "Memory indicates enable button tap",
            "confidence": 0.95
          }

Step 4️⃣ : Execute Action on Device
       ├─ Action type: "tap"
       ├─ Coordinates: [1000, 120]
       ├─ Device: Send uiautomator2 command
       ├─ Execution: uiautomator2.device.click(1000, 120)
       │
       └─ Device responds:
          ✓ Button tapped
          ✓ Screen transitions
          ✓ New UI appears

Step 5️⃣ : Record in Trace
       ├─ Step index: 2
       ├─ Timestamp: 5.234 seconds
       ├─ Action: tap at [1000, 120]
       ├─ Confidence: 0.95
       └─ Log entry added to execution_trace.json

Step 6️⃣ : Check Completion
       ├─ Is task done?
       │  ├─ Check completion criteria from memory
       │  ├─ "Status shows Enabled"? → Yes! ✓
       │  └─ Task complete!
       │
       └─ Exit loop

═════════════════════════════════════════════════════════════════

Stage 2 Output:
  ✅ Device automated successfully
  ✅ execution_trace.json logged all actions
  ✅ Screenshots saved for each step
  ✅ Confidence scores recorded
  ✅ Full audit trail created
```

---

## 6. Memory.md Format & Structure

```
┌───────────────────────────────────────────────────────────────┐
│                    memory.md Example                         │
├───────────────────────────────────────────────────────────────┤
│                                                               │
│ # Task Memory: AdAway                                         │
│                                                               │
│ ## Task Summary                                               │
│ Enable the ad filtering feature in AdAway by toggling the     │
│ main switch located in the app's main screen. This blocks     │
│ advertisements from appearing in other apps.                  │
│                                                               │
│ ## Steps                                                      │
│ 1. **Action:** launch → App launches showing the initial      │
│    disabled state with a large red "Enable" button            │
│                                                               │
│ 2. **Action:** tap → Tap the "Enable" button located at       │
│    the top-right corner. A dialog appears.                    │
│                                                               │
│ 3. **Action:** tap → Confirm in dialog by tapping "Yes"       │
│                                                               │
│ 4. **Action:** wait → Filter activates, UI updates            │
│                                                               │
│ ## UI Elements                                                │
│ - Button "Enable": Located at top-right, red color            │
│ - Toggle: Shows "Status: Disabled" initially                  │
│ - Text: "Filter is now active" appears after enabling         │
│ - Dialog: Confirmation dialog with Yes/No buttons             │
│ - Icon: Filter icon changes to enabled state                  │
│                                                               │
│ ## Completion Criteria                                        │
│ - App shows "Status: Enabled" text                            │
│ - Filter icon displays as active (green)                      │
│ - No "Enable" button visible (hidden when active)             │
│ - Toast notification: "Filter activated"                      │
│                                                               │
└───────────────────────────────────────────────────────────────┘

Format Notes:
  ✓ Markdown format (readable, versionable)
  ✓ Clear sections (parsed by Stage 2)
  ✓ Action descriptions (tap, scroll, type, wait)
  ✓ UI locations (top-right, center, etc)
  ✓ Completion criteria (clear success condition)
```

---

## 7. Token Savings Visualization

```
Traditional Workflow (❌ Inefficient)
═══════════════════════════════════════

Video Frame 1 ──▶ [LLM] ──▶ Action 1  ~2000 tokens
Video Frame 2 ──▶ [LLM] ──▶ Action 2  ~2000 tokens
Video Frame 3 ──▶ [LLM] ──▶ Action 3  ~2000 tokens
Video Frame 4 ──▶ [LLM] ──▶ Action 4  ~2000 tokens
Video Frame 5 ──▶ [LLM] ──▶ Action 5  ~2000 tokens
Video Frame 6 ──▶ [LLM] ──▶ Action 6  ~2000 tokens

Total: 6 full video analyses
Total tokens: ~12,000
Cost: $$$$$ (Very expensive!)


Two-Stage Workflow (✅ Efficient)
═════════════════════════════════

Stage 1:
Video + Frames ──▶ [LLM] ──▶ memory.md  ~2000 tokens
                              + metadata.json
                              + keyframes

Stage 2 (Repeat 5 times):
memory.md + Screen 1 ──▶ [LLM] ──▶ Action 1  ~300 tokens
memory.md + Screen 2 ──▶ [LLM] ──▶ Action 2  ~300 tokens
memory.md + Screen 3 ──▶ [LLM] ──▶ Action 3  ~300 tokens
memory.md + Screen 4 ──▶ [LLM] ──▶ Action 4  ~300 tokens
memory.md + Screen 5 ──▶ [LLM] ──▶ Action 5  ~300 tokens

Total: 1 full video analysis + 5 memory uses
Total tokens: ~1000 + 1500 = ~2500
Cost: $ (Much cheaper!)


SAVINGS SUMMARY
═══════════════════════════════════════

                Traditional    Two-Stage    Reduction
  ─────────────────────────────────────────────────
  Video analyses        6            1         83% ↓
  Memory uses           0            5           -
  Tokens per call   ~2000         ~300        85% ↓
  TOTAL TOKENS     ~12,000      ~2,500       80% ↓
  COST              VERY $         $        80% ↓↓↓
```

---

## 8. Error Handling & Recovery

```
┌──────────────────────────────────────────────────────┐
│              Error Handling Flow                     │
└──────────────────────────────────────────────────────┘

When LLM request is made:
       │
       ▼
   ┌─────────────────┐
   │ Send to LLM     │
   └────────┬────────┘
            │
      ┌─────┴──────────────┐
      │                    │
      ▼                    ▼
 ┌─────────────┐    ┌──────────────┐
 │ Success ✓   │    │ Error ✗      │
 │ Parse JSON  │    │ (429, 500,   │
 │ Continue    │    │  timeout)    │
 └─────────────┘    └──────┬───────┘
                           │
                    ┌──────▼──────┐
                    │ Retry Logic │
                    ├─────────────┤
                    │ Max: 5      │
                    │ Delay: 10s  │
                    │   → 20s     │
                    │   → 40s     │
                    │   → 80s     │
                    │   → 160s    │
                    └──────┬──────┘
                           │
                      ┌────┴────┐
                      │          │
                      ▼          ▼
                  Success    Max retries
                    │        reached
                    │        │
                    ▼        ▼
                Continue  ┌──────────────────┐
                          │ Fallback Heuristic
                          ├──────────────────┤
                          │ if frame == 0:   │
                          │   action="launch"│
                          │ elif motion>=18: │
                          │   action="tap"   │
                          │ elif motion>=9:  │
                          │   action="scroll"│
                          │ else:            │
                          │   action="wait"  │
                          └──────────────────┘

Fallback ensures pipeline never completely fails!
```

---

## 9. Configuration & Setup Flow

```
┌─────────────────────────────────────────────────────────┐
│                 Getting Started                         │
└─────────────────────────────────────────────────────────┘

Step 1: Install
   pip install -r src_llm/requirements.txt
         │
         ▼ (installs: opencv, requests, pyyaml, etc)

Step 2: Create .env.local
   cp .env.local.example .env.local
   nano .env.local
         │
         ├─ For Ollama:
         │  LLAMA_BASE_URL=http://localhost:11434/v1
         │
         └─ For Gemini:
            GOOGLE_GENERATIVE_AI_API_KEY=sk-...

Step 3: Create config.yml
   cp src_llm/config.example.yml src_llm/input/config.yml
   nano src_llm/input/config.yml
         │
         ├─ app_name: "adaway"
         ├─ llm: "gemini"
         ├─ video_path: ["hhv", "srv"]
         ├─ video_mode: true
         └─ keyframe_selection.method: "ssim"

Step 4: Run Pipeline
   python -m src_llm.end_to_end \
     --config src_llm/input/config.yml \
     --env-file .env.local
         │
         ├─ Stage 1: Analyze video (5-10 mins)
         │           Generate memory.md
         │
         └─ Stage 2: Automate device (varies)
                     Use memory to drive actions

Step 5: Check Output
   ls apps/adaway/llm/gemini-2.5-flash/handheld-video-mode/run-001/
         │
         ├─ memory.md ................. ✓ Check this!
         ├─ metadata.json ............. ✓ Verify memory embedded
         ├─ execution_trace.json ...... ✓ Actions logged
         ├─ llm_raw_response.txt ...... ✓ Debug info
         ├─ keyframes/ ................ ✓ Sampled frames
         └─ logs/run.log .............. ✓ Full trace
```

---

## 10. Comparison Table: Traditional vs Two-Stage

```
┌──────────────────────────────────────────────────────────────┐
│              Traditional vs Two-Stage Architecture           │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│ Feature              Traditional      Two-Stage             │
│ ─────────────────────────────────────────────────────────  │
│ Video analysis       For each step    Once at start          │
│ Token usage/step     ~2000            ~300                   │
│ Total tokens         ~12000           ~2500 (83% less!)      │
│ Cost                 $$$$             $                      │
│ Reusability          No (new video)   Yes (memory reuse)     │
│ Offline capability   No               Yes (Stage 1)          │
│ Parallelization      Limited          Yes (Stage 2 parallel) │
│ Debugging            Difficult        Easier (trace logged)  │
│ Model flexibility    Hard to switch   Easy (Stage 2 reuse)   │
│ Latency per step     ~5-10 min        ~30 sec               │
│ Memory usage         High             Low                    │
│ Maintainability      Complex          Modular                │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

## Summary: Why src_llm is Efficient

```
The Key Innovation: MEMORY REUSE
═════════════════════════════════════════════════════════════

Traditional:
  Video → Expensive analysis (2000 tokens)
       → Action
       → Expensive analysis (2000 tokens)
       → Action
       → Expensive analysis (2000 tokens)
       ...repeat for each step

Two-Stage:
  Video → Expensive analysis (2000 tokens)
       → Generate MEMORY (reusable!)
       → Action using memory (300 tokens) ← Cheap!
       → Action using memory (300 tokens) ← Cheap!
       → Action using memory (300 tokens) ← Cheap!
       ...

Memory is 85% cheaper than re-analyzing the video!
═════════════════════════════════════════════════════════════
```

