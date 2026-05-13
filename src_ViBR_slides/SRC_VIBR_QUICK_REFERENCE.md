# src_ViBR Quick Reference Guide

## One-Sentence Summary
**A robot that watches bug videos and replays them on test devices automatically.**

---

## The 5 Stages (Visual)

```
┌────────────────────────────────────────────────────────────────────┐
│ 1️⃣  ACTION SEGMENTATION                                            │
│ ════════════════════════════════════════════════════════════════   │
│ Input:  Long video with many frames                               │
│ Tool:   CLIP (smart) or SSIM (fast)                               │
│ Do:     Find where each user action begins/ends                   │
│ Output: Chunks like "user tapped Settings" from frames 50-51      │
└────────────────────────────────────────────────────────────────────┘
                              ↓
┌────────────────────────────────────────────────────────────────────┐
│ 2️⃣  INTERACTIVE REGION DETECTION                                   │
│ ════════════════════════════════════════════════════════════════   │
│ Input:  Screenshot from video                                     │
│ Tool:   GroundingDINO (object detector)                           │
│ Do:     Find all clickable buttons, menus, text fields            │
│ Output: List of regions with bounding boxes and indices           │
└────────────────────────────────────────────────────────────────────┘
                              ↓
┌────────────────────────────────────────────────────────────────────┐
│ 3️⃣  STATE CONSISTENCY CHECK                                        │
│ ════════════════════════════════════════════════════════════════   │
│ Input:  Video frame + Current device screenshot                   │
│ Tool:   GPT-4o Vision (understanding)                             │
│ Do:     Are these screens "the same" functionally?                │
│ Output: YES (proceed) or NO (navigate first)                      │
└────────────────────────────────────────────────────────────────────┘
                              ↓
┌────────────────────────────────────────────────────────────────────┐
│ 4️⃣  ACTION INFERENCE                                               │
│ ════════════════════════════════════════════════════════════════   │
│ Input:  Before frame + After frame + Current device              │
│ Tool:   GPT-4o Vision (reasoning)                                 │
│ Do:     What action changed the screen? Where to tap?             │
│ Output: {"action": "tap", "region": 2} or similar                 │
└────────────────────────────────────────────────────────────────────┘
                              ↓
┌────────────────────────────────────────────────────────────────────┐
│ 5️⃣  DEVICE EXECUTION                                               │
│ ════════════════════════════════════════════════════════════════   │
│ Input:  Inferred action                                           │
│ Tool:   ADB (Android Debug Bridge)                                │
│ Do:     Execute the action (tap, swipe, type, etc.)               │
│ Output: ✓ Bug reproduced!                                         │
└────────────────────────────────────────────────────────────────────┘
```

---

## The Three Key Technologies

### 🎬 CLIP vs SSIM (Segmentation)

| SSIM | CLIP |
|------|------|
| Compares pixels | Compares meaning |
| Fast ⚡ | Slower 🐢 |
| Breaks with theme changes | Handles theme changes |
| Best: Static GUIs | Best: Dynamic GUIs |

**When to use?**
- CLIP: Default, better accuracy
- SSIM: If CLIP is slow and GUI is stable

---

### 🔍 GroundingDINO (Region Detection)

**What it finds:**
- Buttons
- Text inputs
- Checkboxes
- Toggles
- Icons
- Menus
- Cards
- Tabs
- Headers
- Navigation bars

**Why it matters:**
Instead of guessing "click at pixel (340, 500)", it says:
"Region 2 is a button, centered at (340, 500)"

This works across devices because it understands the *meaning*, not exact pixels.

---

### 🤖 GPT-4o (Smart Decisions)

**Three main uses:**

1. **Consistency:** "Are these screens the same (functionally)?"
   - Ignores: color changes, layout shifts, language
   - Checks: same buttons? same menus? same actions possible?

2. **Regions:** "Which regions changed between screens?"
   - Uses GroundingDINO output
   - Identifies what user likely interacted with

3. **Action:** "What did the user do and how to replay?"
   - Sees: start frame, end frame, current device state
   - Decides: which region to tap? swipe where? type what?

---

## File Structure

```
src_ViBR/
├── main.py                      # Entry point (loads config, runs segment_replay)
├── config.py                    # Config parsing (YAML support)
├── io_utils.py                  # File I/O helpers
├── approach/
│   ├── segment_replay.py        # Main orchestration loop
│   ├── clip_seg.py              # CLIP-based segmentation
│   ├── yyh_utils.py             # SSIM-based segmentation
│   ├── dino_detection.py        # GroundingDINO wrapper
│   ├── openai_api.py            # GPT-4o API calls
│   ├── gemini_api.py            # Gemini API support
│   ├── adb_device_controller.py # Device interaction
│   ├── execute_action.py        # Convert actions to ADB commands
│   └── input_formatter.py       # Android UI parsing
├── GroundingDINO/               # Submodule (object detection)
├── input/
│   └── config.yml               # Configuration file
└── apps/
    └── <app_name>/llm/ViBR/     # Outputs by app
        ├── handheld/
        │   └── run-001/
        │       ├── artifacts/   # Frames, segmentation data
        │       ├── logs/        # Execution logs
        │       └── metadata.json # Run metadata
        └── screenrec/
            └── run-001/
```

---

## Configuration Example

```yaml
config:
  algorithm: "clip"              # or "ssim"
  llm: "openai"                  # or "gemini"
  llm_model: "gpt-4o"            # or "gemini-1.5-flash"
  
  output:
    overwrite: true              # Overwrite previous runs
  
  logging:
    level: "INFO"                # DEBUG, INFO, WARNING, ERROR, CRITICAL
  
  runs:
    - app_name: "adaway"
      video_path: "hhv"          # shorthand for handheld video
      algorithm: "clip"
      llm: "openai"
      llm_model: "gpt-4o"
    
    - app_name: "adaway"
      video_path: "srv"          # shorthand for screen recording
      algorithm: "ssim"
      llm: "gemini"
```

---

## Performance by the Numbers

### Segmentation (Dividing Video into Actions)
```
Metric          ViBR        GIFdroid    Baseline
────────────────────────────────────────────────
Precision       89.3%       82.1%       70-80%
Recall          92.8%       91.7%       70-80%
F1-Score        90.9%       86.5%       70-80%
```
**Winner:** ViBR is 7.4% better!

### GUI State Comparison (Same Screen? Different Device?)
```
Method                              F1-Score
─────────────────────────────────────────────
ViBR (Full)                         0.86
ViBR (No GroundingDINO)             0.72
SSIM (Pixel comparison)             0.62
```
**Winner:** GroundingDINO helps by +15%!

### Bug Reproduction Success Rate
```
Method              Success Rate    Time/Bug    Cost/Bug
─────────────────────────────────────────────────────────
ViBR                72%             302.6 sec   $0.02
GIFdroid            58%             400+ sec    N/A
Manual               ~50%            ??? min    Many hours
```

---

## Common Action Types

| Action | JSON | Use Case |
|--------|------|----------|
| Tap | `{"action": "tap", "region": 2}` | Click a button |
| Swipe | `{"action": "swipe", "from": [x1,y1], "to": [x2,y2], "duration": 500}` | Scroll list |
| Type | `{"action": "input_text", "text": "hello"}` | Enter search |
| Back | `{"action": "back"}` | Go back screen |
| Home | `{"action": "home"}` | Home screen |
| Wait | `{"action": "wait", "duration": 1500}` | Wait for animation |
| None | `{"action": "no action"}` | Screen auto-updated |

---

## Guided Exploration (When States Don't Match)

**Scenario:** Device screen doesn't match video reference

**Solution:**
```
GPS-4o: "Current device shows a popup.
         Reference showed a list.
         
         Suggestion: Press BACK to close popup"
         
ViBR: Execute back button
      Take new screenshot
      Compare again
      
If match: Proceed with action ✓
If no: Ask for more guidance (loop)
```

---

## Key Advantages Over Other Methods

| Feature | ViBR | Image Matching | Manual |
|---------|------|----------------|--------|
| Works across devices | ✓ | ✗ | N/A |
| Handles theme changes | ✓ | ✗ | N/A |
| Handles layout changes | ✓ | ✗ | N/A |
| No app instrumentation | ✓ | ✓ | N/A |
| Understands intent | ✓ | ✗ | ✓ |
| Fast | ✓ | ✓ | ✗ |
| Cheap | ✓ | ✓ | ✗ |

---

## Cost Breakdown (per Bug)

### API Calls per Action Scene (e.g., one tap)
```
1. Region detection (GroundingDINO): 4.17 sec, FREE
2. State consistency (GPT-4o): 4.15 sec, ~$0.005
3. Action inference (GPT-4o): 5.93 sec, ~$0.01
4. Plus other analysis: ~$0.005
─────────────────────────────────────
Total per action: ~14 seconds, ~$0.02
```

### For a Typical Bug (10 actions)
```
10 actions × $0.02 = $0.20 per bug
```

**Comparison:** Much cheaper than developer time!

---

## Troubleshooting Quick Guide

| Problem | Cause | Solution |
|---------|-------|----------|
| Poor segmentation | SSIM threshold too high | Use CLIP instead |
| Regions not detected | GroundingDINO confidence low | Lower BOX_THRESHOLD |
| State check fails repeatedly | Device state too different | Improve guided exploration |
| Action not found | Region indices wrong | Check GroundingDINO output |
| Device doesn't execute | ADB connection issue | Run `adb devices` |

---

## Workflow Summary

```
1. User films bug on their phone
   ↓
2. ViBR analyzes video
   ├─ Segments it (CLIP/SSIM)
   ├─ Detects regions (GroundingDINO)
   └─ Understands state (GPT-4o)
   ↓
3. ViBR infers actions
   ├─ What button was tapped?
   ├─ Where is it on test device?
   └─ How to adapt to different UI?
   ↓
4. ViBR executes on device
   ├─ Sends ADB commands
   ├─ Verifies results
   └─ Handles failures gracefully
   ↓
5. Bug reproduced automatically!
   ✓ No manual replay needed
   ✓ Works across devices
   ✓ Fast & cheap
```

---

## Key Insights

1. **Vision-LLMs are smart:** They understand UI *meaning*, not just pixels
2. **Signal processing works:** Detecting action boundaries is more than pixel matching
3. **Grounding is crucial:** Knowing what's clickable helps across devices
4. **Guided recovery:** When alignment fails, explore first, then act
5. **Cross-device works:** One video → multiple device configurations

---

## Learn More

- **Full technical details:** See SRC_VIBR_OVERVIEW.md
- **Diagrams:** Check FigJam board (system architecture & flow)
- **Research paper:** docs/research_papers/2025 - ViBR.pdf
- **Code:** src_ViBR directory

---

**Remember:** src_ViBR turns **manual bug reproduction** into **automatic intelligence**! 🤖
