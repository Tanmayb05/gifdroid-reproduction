# src_llm Video Mode: End-to-End Architecture & Data Flow

Complete visual guide to the `src_llm` two-stage pipeline: **Stage 1** converts a video recording to structured memory, then **Stage 2** uses that memory to automate the same task on a live Android device.

---

## System Overview: Single Video Run

High-level flow from start to finish.

```mermaid
flowchart TD
    A["📹 Input: Video<br/>apps/app/videos/hhv-NNN.mp4"] --> B["🔧 Load Config<br/>src_llm/input/config.yml"]
    C["🔑 Load APK<br/>apps/app/apk/app.apk"] --> D["🤖 Stage 2: Memory → Device"]
    B --> E["▶️ Stage 1: Video → Memory<br/>pipeline.py → main.py"]
    E --> F["📝 Generate memory.md<br/>GeminiVideoProvider<br/>infer_memory_from_video"]
    F --> G["💾 Output: Metadata & Memory<br/>run-NNN/memory.md<br/>run-NNN/metadata.json"]
    G --> D
    D --> H["▶️ Automation Loop<br/>automate.py → automation.py<br/>LLM guides each step"]
    H --> I["📱 Device Execution<br/>DeviceController<br/>uiautomator2/ADB"]
    I --> J["📸 Capture Screenshots<br/>Extract UI XML<br/>Parse Accessibility Tree"]
    J --> H
    H --> K["✅ Final Output<br/>run-NNN/session_trace.json<br/>run-NNN/steps/step_*.png<br/>run-NNN/replay_script.sh"]
    
    style A fill:#e1f5ff
    style C fill:#e1f5ff
    style E fill:#fff3e0
    style D fill:#f3e5f5
    style K fill:#e8f5e9
```

---

## Stage 1: Video → Memory (Structured Extraction)

Converts full video recording to structured markdown memory document using vision LLM.

```mermaid
flowchart TD
    A["config.yml<br/>video_path: ...hhv-NNN.mp4<br/>video_mode: true<br/>llm: gemini"]
    A --> B["pipeline.py<br/>run all stages"]
    B --> C["main.py::main"]
    C --> D["Load Config<br/>config.py::load_config"]
    D --> E["Create OutputLayout<br/>io_utils.py<br/>run-NNN dir"]
    E --> F["Load LLM Prompt<br/>prompts/llama_action_prompt_memory.txt"]
    F --> G["Initialize Provider<br/>providers.py<br/>GeminiVideoProvider"]
    G --> H["Encode Video to Base64<br/>Full MP4 → bytes → base64"]
    H --> I["Send to Gemini API<br/>generateContent with video + prompt<br/>temperature=0.1"]
    I --> J["Parse LLM Response<br/>main.py::_parse_memory_md"]
    J --> K["Extract Sections<br/>• app, goal, outcome<br/>• Steps array<br/>• Key Observations"]
    K --> L["Write memory.md<br/>run-NNN/memory.md"]
    L --> M["Write metadata.json<br/>video_mode_metadata:<br/>  memory_md_content<br/>  task_description<br/>  ui_elements<br/>  completion_criteria"]
    M --> N["Write llm_raw_response.txt<br/>Raw Gemini response"]
    N --> O["✅ Stage 1 Complete<br/>Ready for Stage 2"]
    
    style A fill:#e3f2fd
    style I fill:#ffccbc
    style L fill:#c8e6c9
    style O fill:#c8e6c9
```

### Stage 1 Key Artifacts

| File | Creator | Content |
|---|---|---|
| `memory.md` | `main.py` | Structured markdown memory trace: app, goal, steps, observations |
| `metadata.json` | `io_utils.py::write_run_metadata()` | Run metadata + `video_mode_metadata` (memory content, task desc, UI elements) |
| `llm_raw_response.txt` | `main.py` | Raw API response from Gemini |
| `logs/run-NNN__*.log` | `logging_utils.py` | Execution log |

---

## Stage 2: Memory → Device (Live Automation)

Uses extracted memory to guide automated execution of the same task on live Android device.

```mermaid
flowchart TD
    A["automation_config.yml<br/>app_name: X<br/>apk_path: apps/X/apk/X.apk<br/>llm: gemini"]
    B["Latest Stage 1 Output<br/>run-NNN/metadata.json<br/>Contains: memory.md content"]
    A --> C["automate.py::main"]
    B --> C
    C --> D["Load Automation Config<br/>config.py::load_automation_config"]
    D --> E["Locate Latest Run<br/>io_utils.py::_locate_latest_run<br/>Find newest run-* metadata.json"]
    E --> F["Extract Memory + Task<br/>Load memory_md_content<br/>Extract task_description"]
    F --> G["Initialize DeviceController<br/>device.py<br/>uiautomator2 connection"]
    G --> H["Install APK<br/>adb uninstall + install -r<br/>apps/X/apk/X.apk"]
    H --> I["Launch App<br/>adb shell am start"]
    I --> J["Initialize Automation Session<br/>session.py::AutomationSession<br/>history_window = 3 steps"]
    
    J --> K["🔄 AUTOMATION LOOP<br/>max_steps or until done"]
    K --> L["Capture Screenshot<br/>device.py::capture_screenshot<br/>PIL.Image"]
    K --> M["Dump Accessibility Tree<br/>device.py::dump_accessibility_tree<br/>XML string"]
    K --> N["Extract Top 20 Elements<br/>Parse clickable regions<br/>resource_id, coordinates, text"]
    L --> O["LLM Decision<br/>providers.py<br/>decide_next_action_with_video_context"]
    M --> O
    N --> O
    F --> O
    J --> O
    
    O --> P["LLM Prompt Sent:<br/>• Current screenshot base64<br/>• Video summary memory.md<br/>• Task description<br/>• Accessibility tree elements<br/>• Last 3 steps history"]
    P --> Q["LLM Response:<br/>action: tap/scroll/type<br/>target: resource_id or coords<br/>reasoning: why<br/>confidence: 0-100"]
    
    Q --> R["Parse ActionDecision<br/>automation.py::ActionDecision"]
    R --> S["Execute on Device<br/>device.py<br/>tap/scroll/type/back/home/wait"]
    S --> T["Record Step<br/>session.py::add_turn<br/>Log action taken"]
    T --> U["Check Stall Detection<br/>Same action repeat > threshold?<br/>→ Stop if repeated"]
    U --> V{"Stall Detected?"}
    V -->|No| W["Continue Loop"]
    V -->|Yes| X["🛑 Stop Automation"]
    
    W --> K
    X --> Y["Write session_trace.json<br/>automation.py<br/>Task, steps[], status, assertions"]
    Y --> Z["Write replay_script.sh<br/>replay_writer.py<br/>Executable replay"]
    Z --> AA["Save step screenshots<br/>steps/step_NNN.png"]
    AA --> AB["✅ Stage 2 Complete"]
    
    style A fill:#f3e5f5
    style B fill:#ffe0b2
    style O fill:#ffccbc
    style P fill:#ffccbc
    style Y fill:#c8e6c9
    style AB fill:#c8e6c9
```

### Stage 2 Key Artifacts

| File | Creator | Content |
|---|---|---|
| `session_trace.json` | `automation.py` | Full automation trace: task, steps array, status, field assertions |
| `steps/step_NNN.png` | `automation.py` | Screenshots captured per automation step |
| `video_summary.txt` | `automate.py` | Copy of memory.md content used as context |
| `replay_script.sh` | `replay_writer.py` | Executable bash script to replay automation |
| `automate.log` | `logging_utils.py` | Per-run automation log |

---

## Complete Data Flow: Sequence Diagram

Shows all components and data movement over time.

```mermaid
sequenceDiagram
    participant User
    participant Config as Config Files
    participant P as pipeline.py
    participant M as main.py
    participant Prov as GeminiVideoProvider
    participant API as Gemini API
    participant IO as io_utils.py
    participant A as automate.py
    participant Auto as automation.py
    participant Dev as DeviceController
    participant Device as Android Device
    
    User->>Config: Provides config.yml<br/>automation_config.yml
    User->>Config: Provides video MP4<br/>Provides APK
    
    Config->>P: Load config
    P->>M: Call main() Stage 1
    M->>IO: Create output layout<br/>run-NNN/
    M->>Prov: Load GeminiVideoProvider
    
    Note over Prov,API: Stage 1: Video → Memory
    Prov->>Prov: Read MP4 video<br/>Encode to base64
    Prov->>API: POST generateContent<br/>Video + memory prompt
    API-->>Prov: Return memory.md<br/>structured markdown
    Prov->>M: Return parsed memory
    M->>IO: Write memory.md
    M->>IO: Write metadata.json<br/>with memory content
    P->>A: Call automate() Stage 2
    
    Note over A,Device: Stage 2: Memory → Device Automation
    A->>IO: Locate latest run<br/>Load metadata.json
    A->>Auto: Pass memory_md_content<br/>task_description
    A->>Dev: Connect uiautomator2
    Dev->>Device: ADB connect
    Dev->>Device: Install APK
    Dev->>Device: Launch app
    
    A->>A: Init AutomationSession<br/>history_window=3
    
    loop Up to max_steps
        Auto->>Dev: Capture screenshot
        Dev->>Device: screencap → PIL.Image
        Auto->>Dev: Dump accessibility tree
        Dev->>Device: uiautomator2 dump
        Dev-->>Auto: XML + coordinates
        Auto->>Auto: Parse top 20 elements
        
        Note over Auto,API: LLM Decision
        Auto->>Prov: decide_next_action<br/>with_video_context()
        Prov->>API: POST generateContent<br/>Screenshot base64<br/>Memory summary<br/>Task description<br/>Accessibility tree<br/>History (last 3 steps)
        API-->>Prov: ActionDecision JSON<br/>action, target, reasoning
        Prov-->>Auto: Parsed ActionDecision
        
        Auto->>Dev: Execute action<br/>tap/scroll/type
        Dev->>Device: ADB/uiautomator2<br/>Execute
        Auto->>A: Record step<br/>add_turn()
        
        Auto->>Auto: Check stall?<br/>If repeated N times → stop
    end
    
    Auto->>IO: Write session_trace.json
    Auto->>IO: Write step_*.png screenshots
    A->>IO: Write replay_script.sh
    
    A-->>User: ✅ Automation complete
```

---

## LLM Calls Detail

### Stage 1: `GeminiVideoProvider.infer_memory_from_video()`

**When:** Called once per video in Stage 1.

**Input:**
- Full video file encoded as base64
- System/user prompt from `prompts/llama_action_prompt_memory.txt`
- Model: `gemini-2.0-flash-exp` (or configured model)
- Temperature: 0.1
- API: Google Vertex AI `generateContent`

**Processing:**
Video is streamed as inline base64. Gemini processes the entire video sequence and extracts structured actions.

**Output:**
Structured markdown string with:
```
---
app: AppName
goal: What the user is trying to do
outcome: Final result
---

## Session Summary
...

## Steps
### Step 1
- Screen: Description of what's visible
- Action: What was done (tap, swipe, type, etc.)
- Details: Coordinates or element details
- Result: Outcome of the action
- Confidence: 0.0-1.0

...

## Key Observations
- Notable patterns or issues
```

**Parsed by:** `main.py::_parse_memory_md()` → extract `task_description`, `ui_elements` dict, `completion_criteria` list.

**Stored in:**
- `memory.md` (raw)
- `metadata.json["video_mode_metadata"]["memory_md_content"]` (for Stage 2)

---

### Stage 2: `GeminiProvider.decide_next_action_with_video_context()`

**When:** Called once per automation step (up to `max_steps` times).

**Input:**
```
{
  screenshot: base64-encoded PNG (current device screen),
  accessibility_tree: XML string (top 20 clickable elements),
  task_description: str (from Stage 1 memory),
  video_summary: str (full memory.md content from Stage 1),
  history: List[ConversationTurn] (last N steps taken, default N=3),
  max_steps_remaining: int
}
```

**Processing:**
- Screenshot + video summary + task context sent to Gemini
- LLM decides next action to progress toward task goal
- Considers stall detection: if same action repeated, suggest alternative

**Output:**
```json
{
  "continue": true/false,
  "action": {
    "type": "tap|scroll|type|back|home|wait",
    "resource_id": "android.widget.Button:id/submit",
    "coordinates": [100, 200],
    "text": "text to type",
    "direction": "up|down|left|right",
    "target_description": "what we're interacting with"
  },
  "reasoning": "why this action moves us toward the goal",
  "confidence": 0.85
}
```

**Parsed by:** `automation.py::ActionDecision` → `ExecutableAction` → `device.execute_action()`.

**Loop Control:**
- If `continue=false` → break loop, task complete
- If action repeated N times (stall) → break loop, task failed

---

## Input & Output: Single Video Run

### Inputs Required

| Input | Path | Format | Used By |
|---|---|---|---|
| **Stage 1 Config** | `src_llm/input/config.yml` | YAML | `main.py`, `pipeline.py` |
| **Stage 2 Config** | `src_llm/input/automation_config.yml` | YAML | `automate.py`, `pipeline.py` |
| **Video** | `apps/<app>/videos/hhv-NNN.mp4` | MP4 (h264/h265) | Stage 1 (GeminiVideoProvider) |
| **APK** | `apps/<app>/apk/<app>.apk` | Android APK | Stage 2 (DeviceController::install_apk) |
| **Memory Prompt** | `src_llm/input/prompts/llama_action_prompt_memory.txt` | Plain text | GeminiVideoProvider (prepended to request) |
| **Credentials** | `.env.local` | .env format | Both (provider auth) |

### Outputs Generated

```
apps/<app>/llm/<model>-vm/run-NNN/
├── memory.md                    # Stage 1: structured memory trace
├── metadata.json                # Stage 1: run metadata + memory_md_content
├── llm_raw_response.txt         # Stage 1: raw Gemini response
├── logs/
│   └── <timestamp>__run-NNN__pipeline__<status>.log
├── steps/
│   ├── step_001.png             # Stage 2: screenshots per step
│   ├── step_002.png
│   └── ...
├── session_trace.json           # Stage 2: full automation trace
├── video_summary.txt            # Stage 2: copy of memory.md used as context
├── replay_script.sh             # Stage 2: executable replay script
└── automate.log                 # Stage 2: automation execution log
```

---

## Module Responsibility Matrix

| Module | File | Responsibility |
|---|---|---|
| **Pipeline Orchestrator** | `pipeline.py` | Decide stage order, invoke main.py then automate.py |
| **Stage 1 Runner** | `main.py` | Load config, coordinate Stage 1 flow, write outputs |
| **LLM Provider** | `providers.py` | Encode/send API requests (Gemini, Llama, etc.) |
| **Config Parser** | `config.py` | Parse YAML config files → dataclasses |
| **Output Layout** | `io_utils.py` | Create run dirs, resolve paths, write metadata |
| **Stage 2 Runner** | `automate.py` | Load Stage 1 results, invoke automation loop |
| **Automation Loop** | `automation.py` | Per-step: screenshot → LLM → execute → stall check |
| **Device Control** | `device.py` | ADB/uiautomator2 wrapper (install, launch, tap, scroll, etc.) |
| **Session Memory** | `session.py` | Ring buffer of last N conversation turns |
| **APK Utils** | `apk_utils.py` | Extract package name & main activity from APK |
| **Replay Writer** | `replay_writer.py` | Generate bash script from session trace |
| **Logging** | `logging_utils.py` | Setup logger, rename log with status at end |
| **Env Loader** | `env_loader.py` | Load & validate `.env.local` per provider |

---

## Config Examples

### Stage 1: config.yml (Video Mode)

```yaml
llm: gemini
llm_model: gemini-2.0-flash-exp
video_mode: true
frame_sampling: 10
keyframe_selection:
  strategy: adaptive
  max_frames: 50

runs:
  - app_name: myapp
    video_path: apps/myapp/videos/hhv-001.mp4
    
output:
  overwrite: true

logging:
  level: INFO
```

### Stage 2: automation_config.yml

```yaml
llm: gemini
llm_model: gemini-2.0-flash-exp

automation:
  app_name: myapp
  apk_path: apps/myapp/apk/myapp.apk
  max_steps: 50
  history_window: 3
  stall_repeat_threshold: 3

logging:
  level: INFO
```

---

## Verification Checklist

- [ ] `src_llm/input/config.yml` and `automation_config.yml` exist with required fields
- [ ] `apps/<app>/videos/*.mp4` and `apps/<app>/apk/*.apk` available
- [ ] `.env.local` contains LLM credentials (GOOGLE_API_KEY or Vertex auth)
- [ ] `src_llm/input/prompts/llama_action_prompt_memory.txt` exists
- [ ] Run `python -m src_llm.pipeline --config src_llm/input/config.yml` (full 2-stage)
- [ ] Or run `python -m src_llm.main --config src_llm/input/config.yml` (Stage 1 only)
- [ ] Or run `python -m src_llm.automate --config src_llm/input/automation_config.yml` (Stage 2 only with prior Stage 1 metadata)
- [ ] Verify output in `apps/<app>/llm/<model>-vm/run-NNN/`
- [ ] Check `memory.md` for structured content, `session_trace.json` for automation log

---

## Key Distinctions from src_ViBR

| Aspect | src_llm | src_ViBR |
|---|---|---|
| **Stage 1** | Gemini video LLM → structured memory.md | Frame-by-frame CLIP/SSIM segmentation + GPT-4o inference per segment |
| **Output format** | Markdown memory + JSON metadata | Markdown memory.md only |
| **Speed** | Fast (one LLM call for whole video) | Slower (multiple segment-level calls) |
| **Accuracy** | Vision LLM on full video context | Ground truth device matching per segment |
| **Use case** | Mass-running, prioritize throughput | Validation, prioritize correctness |
| **Memory passing** | Entire memory.md → Stage 2 | Entire memory.md → Stage 2 |