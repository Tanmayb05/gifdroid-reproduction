# src_ViBR Visual & ASCII Guide
## Easy-to-Understand Diagrams with Explanations

---

## 1. The Complete Pipeline

```
                    ┌─────────────────────────────────┐
                    │   BUG REPORT VIDEO              │
                    │   User films bug on phone       │
                    └────────────┬────────────────────┘
                                 │
                    ┌────────────▼─────────────────┐
                    │  1️⃣  SEGMENTATION           │
                    │  Split into action chunks   │
                    │  CLIP or SSIM algorithm     │
                    └────────────┬─────────────────┘
                                 │
                ┌────────────────┴────────────────┐
                │                                 │
        ┌──────▼────────┐             ┌───────────▼──────┐
        │ Pre-Action    │             │  Post-Action     │
        │ Frame 50      │             │  Frame 51        │
        │ (Before tap)  │             │  (After tap)     │
        └──────┬────────┘             └────────┬──────────┘
               │                               │
        ┌──────▼───────────────────────────────▼──────────┐
        │  2️⃣  REGION DETECTION (GroundingDINO)          │
        │  Find all clickable UI elements                │
        │  Assign index: 0, 1, 2, 3...                   │
        └──────┬───────────────────────────────┬──────────┘
               │                               │
        ┌──────▼────────────┐         ┌────────▼──────────┐
        │ Frame 50 Regions: │         │ Frame 51 Regions: │
        │ [0] Settings      │         │ [0] Settings menu │
        │ [1] Help          │         │ [1] Language      │
        │ [2] About         │         │ [2] Theme         │
        └──────────────────┘         └───────────────────┘
                │                               │
                └───────────────┬───────────────┘
                                │
        ┌───────────────────────▼───────────────────────┐
        │  3️⃣  DEVICE STATE CONSISTENCY CHECK           │
        │  Does current device match reference frame?   │
        │  Using: GPT-4o Vision                         │
        └──────────────┬──────────────────┬─────────────┘
                       │                  │
                  ┌────▼──────┐      ┌────▼──────┐
                  │ YES ✓      │      │ NO ✗      │
                  │ Proceed    │      │ Explore   │
                  │            │      │ First     │
                  └────┬──────┘      └────┬──────┘
                       │                  │
                       │            ┌─────▼──────────┐
                       │            │ Guided Explore │
                       │            │ "Close popup"  │
                       │            │ "Go back"      │
                       │            │ "Scroll up"    │
                       │            └─────┬──────────┘
                       │                  │
                       └──────────┬───────┘
                                  │
        ┌─────────────────────────▼──────────────────┐
        │  4️⃣  ACTION INFERENCE                      │
        │  What did user do? How to replay?          │
        │  Using: GPT-4o Vision + Region indices     │
        └────────────┬─────────────────────┬─────────┘
                     │                     │
            ┌────────▼─────────┐   ┌───────▼────────┐
            │ Decision Made:    │   │ Region Mapping:│
            │ Action = "tap"    │   │ Region 0 →     │
            │                   │   │ Coords (340,   │
            │                   │   │ 500)           │
            └────────┬─────────┘   └────────────────┘
                     │
        ┌────────────▼──────────────────────────────┐
        │  5️⃣  DEVICE EXECUTION                     │
        │  Execute via ADB (Android Debug Bridge)   │
        │  Command: adb shell input tap 340 500     │
        └────────────┬───────────────────────────────┘
                     │
        ┌────────────▼──────────────────────────────┐
        │  Device Screen Updates                    │
        │  Settings Menu Opened!                    │
        └────────────┬───────────────────────────────┘
                     │
        ┌────────────▼──────────────────────────────┐
        │  Verify Result                            │
        │  Does screenshot match expected state?    │
        └────────────┬───────────────────────────────┘
                     │
    ┌────────────────┴──────────────────┐
    │                                   │
┌───▼──────┐                       ┌────▼──────┐
│Match ✓    │                       │Fail ✗     │
│Next action│                       │Retry or   │
│or Done!   │                       │Explore    │
└───────────┘                       └───────────┘
```

---

## 2. Algorithm Comparison: CLIP vs SSIM

### SSIM: Pixel-Level Similarity

```
Frame sequence:
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│ Frame 50        │  │ Frame 51        │  │ Frame 52        │
│ [List of items] │  │ [List of items] │  │ [Settings menu] │
│ Blue BG         │  │ Blue BG         │  │ White BG        │
└─────────────────┘  └─────────────────┘  └─────────────────┘
        │                    │                    │
        └────┬───────────────┴─────────┬──────────┘
             │                        │
     Compare pixels           Compare pixels
     99% Similar             20% Similar ← ACTION BOUNDARY!
```

**How SSIM works:**
1. Convert images to grayscale
2. Calculate structural similarity
3. Threshold at 0.95
4. Below threshold = new action

**Good for:** Stable screens, no theme changes
**Bad for:** Dynamic content, theme changes

---

### CLIP: Semantic Embedding

```
Frame sequence:
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│ Frame 50        │  │ Frame 51        │  │ Frame 52        │
│ [List of items] │  │ [List of items] │  │ [Settings menu] │
│ Dark theme      │  │ Dark theme      │  │ Light theme     │
└─────────────────┘  └─────────────────┘  └─────────────────┘
        │                    │                    │
        └────┬───────────────┴─────────┬──────────┘
             │                        │
     Extract meaning          Extract meaning
     "showing list"           "showing menu"
     (embedding vector)       (different vector)
             │                        │
     0.99 similarity          0.15 similarity ← BOUNDARY!
```

**How CLIP works:**
1. Use pre-trained vision model
2. Extract semantic embeddings (vectors)
3. Compare embeddings (cosine similarity)
4. Threshold at appropriate level
5. Below threshold = new action

**Good for:** Dynamic screens, theme changes, layout shifts
**Bad for:** Slow (but accurate)

---

## 3. GroundingDINO: Finding Interactive Regions

### Visual Example

```
Original Screenshot                Detected Regions
─────────────────────             ──────────────────

┌─────────────────┐               ┌─────────────────┐
│ ┌─────────────┐ │               │ ┌─────────────┐ │
│ │ SETTINGS    │ │  ◄─┐          │ │[0]SETTINGS  │ │
│ └─────────────┘ │    └──→ Region│ └─────────────┘ │
│                 │     Detected  │                 │
│ ┌─────────────┐ │  ◄─┐          │ ┌─────────────┐ │
│ │ HELP        │ │    └──→ Region│ │[1]HELP      │ │
│ └─────────────┘ │     Detected  │ └─────────────┘ │
│                 │               │                 │
│ ┌─────────────┐ │  ◄─┐          │ ┌─────────────┐ │
│ │ ABOUT       │ │    └──→ Region│ │[2]ABOUT     │ │
│ └─────────────┘ │     Detected  │ └─────────────┘ │
│                 │               │                 │
└─────────────────┘               └─────────────────┘

Detected Regions (output):
┌────────────────────────────────────────┐
│ Region 0: "button"                     │
│   Center: (200, 150)                   │
│   BBox: [(100, 80), (300, 220)]        │
│   Confidence: 0.92                     │
│                                        │
│ Region 1: "button"                     │
│   Center: (200, 350)                   │
│   BBox: [(100, 280), (300, 420)]       │
│   Confidence: 0.89                     │
│                                        │
│ Region 2: "button"                     │
│   Center: (200, 550)                   │
│   BBox: [(100, 480), (300, 620)]       │
│   Confidence: 0.91                     │
└────────────────────────────────────────┘
```

**Key advantage:** Works across devices!
- Device A: Region 0 at (340, 500)
- Device B: Region 0 at (200, 300)
- Both can be identified as "Region 0"

---

## 4. State Consistency Checking Flow

### Decision Tree

```
┌──────────────────────────────────────────┐
│ Reference Frame              Device Frame │
│ (From video)                 (Live)       │
└──────────────────┬───────────┬────────────┘
                   │           │
                   └──────┬────┘
                          │
        ┌─────────────────▼──────────────────┐
        │ GPT-4o: Are these equivalent?      │
        │ Focus on Region of Interest (ROI)  │
        └──────────┬──────────────────┬──────┘
                   │                  │
            ┌──────▼────────┐   ┌─────▼──────────┐
            │ Check:        │   │ Check:         │
            │ • Same ROI?   │   │ • Popup?       │
            │ • Same buttons│   │ • Overlay?     │
            │ • Same menus? │   │ • Different    │
            │ • Same text?  │   │   language?    │
            └──────┬────────┘   └────┬───────────┘
                   │                 │
            ┌──────▼────────┐   ┌────▼───────────┐
            │ YES ✓         │   │ NO ✗           │
            │ Consistent    │   │ Inconsistent   │
            │ State         │   │ State          │
            └──────┬────────┘   └────┬───────────┘
                   │                 │
        ┌──────────▼──┐    ┌────────▼──────────┐
        │ Execute     │    │ Guided Exploration│
        │ Action      │    │ Ask GPT:          │
        │             │    │ "What to do?"     │
        │ ✓ Proceed   │    │ • Close popup     │
        │             │    │ • Go back         │
        └─────────────┘    │ • Scroll         │
                           │ • Change setting  │
                           │ • Wait            │
                           └────────┬──────────┘
                                    │
                           ┌────────▼──────────┐
                           │ Re-check state    │
                           │ If match: proceed │
                           │ If no: explore    │
                           └───────────────────┘
```

---

## 5. Action Inference: The Smart Reasoning

### Inputs and Outputs

```
INPUTS (GPT-4o receives):
─────────────────────────

[Frame 50: Before]              [Frame 51: After]
┌──────────────────────┐       ┌──────────────────────┐
│ [0] Settings button  │       │ Settings menu opened │
│     (highlighted)    │       │ [0] Language         │
│ [1] Help             │       │ [1] Theme            │
│ [2] About            │       │ [2] Backup           │
└──────────────────────┘       └──────────────────────┘
   "What changed?"                "New elements"

[Device: Current State]
┌──────────────────────┐
│ [0] Settings button  │
│     (visible)        │
│ [1] Help             │
│ [2] About            │
└──────────────────────┘
"Where are we now?"


PROCESSING:
───────────
GPT-4o thinks:
"
Frame 50 shows: Settings button highlighted
Frame 51 shows: Settings menu opened, new options visible

What changed? Settings menu opened!
What caused it? User tapped Settings button!

Current device shows: Same layout, same Settings button
Region 0 is: Settings button
Region 0 position on device: (340, 500)

Action to perform on device:
→ Tap region 0 at coordinates (340, 500)
"


OUTPUT (to device):
──────────────────
┌──────────────────────────────┐
│ Action Decision:             │
│ {                            │
│   "action": "tap",           │
│   "region": 0,               │
│   "coordinates": [340, 500], │
│   "description": "Settings"  │
│ }                            │
└──────────────────────────────┘
```

---

## 6. Cross-Device Adaptation

### The Challenge

```
DEVICE A (User's Phone)         DEVICE B (Test Device)
────────────────────────        ─────────────────────
Resolution: 1440×2560           Resolution: 1920×1080
Theme: Dark mode                Theme: Light mode
Language: English               Language: French
Layout: Bottom nav              Layout: Top nav

┌────────────────────┐          ┌────────────────────┐
│ [🏠][🔍][⭐]        │          │ [☰] [🔍]          │
│                    │          │                    │
│ SETTINGS ← tap     │          │ Settings           │
│                    │    ??    │                    │
│ HELP               │  How to  │ Aide               │
│ ABOUT              │ translate│ À propos            │
│                    │  this?   │                    │
│ (480,1440)         │          │ (960,400)          │
└────────────────────┘          └────────────────────┘

Traditional approach FAILS:
❌ Pixel coordinates different
❌ Layout different
❌ Language different
❌ Theme different
```

### ViBR's Solution

```
Step 1: Region Detection (UNIVERSAL)
─────────────────────────────────────
Device A Region 0 (SETTINGS):
┌────────────────┐
│ [0] SETTINGS   │
│ Center: (480,  │
│ 1440)          │
└────────────────┘

Device B Region 0 (Settings):
┌────────────────┐
│ [0] Settings   │
│ Center: (960,  │
│ 400)           │
└────────────────┘

Both detected as "Region 0" (same UI element!)

Step 2: Action Inference
────────────────────────
"User tapped Region 0 in Device A"
↓
"Region 0 on Device B is at (960, 400)"
↓
"Tap Region 0 on Device B at (960, 400)"

Step 3: Universal Execution
──────────────────────────
ADB Command A: input tap 480 1440
ADB Command B: input tap 960 400

Same ACTION, DIFFERENT COORDINATES!
✓ Cross-device reproduction works!
```

---

## 7. The Complete Processing Loop

```
                    START
                     │
          ┌──────────▼──────────┐
          │ Load video & config │
          └──────────┬──────────┘
                     │
     ┌───────────────▼───────────────┐
     │ For each action in video:     │
     │ (loop through all scenes)     │
     └──────────┬────────────────────┘
                │
    ┌───────────▼────────────────────┐
    │ 1. Segment action              │
    │    Extract start & stop frames │
    └──────────┬─────────────────────┘
               │
    ┌──────────▼──────────────────────┐
    │ 2. Detect regions (DINO)        │
    │    Find UI elements             │
    └──────────┬──────────────────────┘
               │
    ┌──────────▼──────────────────────┐
    │ 3. Check device state (GPT)     │
    │    Current screen match video?  │
    └──────────┬──────────────────────┘
               │
          ┌────┴─────────────────┐
          │                      │
      ┌───▼──────┐         ┌────▼──────────┐
      │ MATCH ✓  │         │ MISMATCH ✗    │
      │          │         │               │
      │ Skip     │    ┌────▼───────────┐  │
      │ exploration   │ 3b. Guided     │  │
      └────┬─────┘    │ Exploration    │  │
           │          │ Navigate state │  │
           │          └────┬───────────┘  │
           │               │              │
           │          ┌────▼──────────┐  │
           │          │ Loop until    │  │
           │          │ match or max  │  │
           │          │ attempts      │  │
           │          └────┬──────────┘  │
           │               │             │
           └───────┬───────┘             │
                   │                     │
    ┌──────────────▼────────────────────┐
    │ 4. Infer action (GPT)             │
    │    What to do? Where to tap?      │
    └──────────┬─────────────────────────┘
               │
    ┌──────────▼────────────────────────┐
    │ 5. Execute on device (ADB)        │
    │    adb shell input tap X Y        │
    └──────────┬─────────────────────────┘
               │
    ┌──────────▼────────────────────────┐
    │ Verify result                     │
    │ Take screenshot & compare         │
    └──────────┬──────────┬─────────────┘
               │          │
           ┌───▼──┐   ┌───▼──┐
           │Match?│   │Match?│
           └──┬───┘   └──┬───┘
              │          │
         ┌────▼─┐    ┌───▼──┐
         │YES ✓ │    │NO ✗  │
         │      │    │      │
         │Next  │    │Retry/│
         │action│    │Fail  │
         └──────┘    └──┬───┘
                        │
                   ┌────▼────┐
                   │Max tries?│
                   └────┬─────┘
                        │
                   ┌────┴────┐
                   │          │
                ┌──▼──┐   ┌──▼──┐
                │YES  │   │NO   │
                │FAIL │   │RETRY│
                └─────┘   └──┬──┘
                             │
                        ┌────▼────┐
                        │More      │
                        │actions?  │
                        └────┬─────┘
                             │
                        ┌────┴────┐
                        │          │
                     ┌──▼──┐   ┌──▼──┐
                     │YES  │   │NO   │
                     │LOOP │   │END  │
                     └──┬──┘   └──┬──┘
                        │        │
                  ┌─────┴────────┘
                  │
                  │ (success count)
                  │ (failed count)
                  │
              ┌───▼──────┐
              │ REPORT   │
              │ Results  │
              └──────────┘
```

---

## 8. Cost Analysis Visualization

```
Per Action (one tap/swipe):
──────────────────────────

Time Breakdown:
┌──────────────────────────────────────┐
│ GroundingDINO Region Detection   4s  │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
│ GPT-4o Region Selection         4s   │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
│ GPT-4o State Comparison         4s   │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
│ GPT-4o Action Inference         6s   │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
│ ─────────────────────────────────────│
│ TOTAL:                         18 sec│
└──────────────────────────────────────┘

Cost Breakdown:
┌──────────────────────────────────────┐
│ GroundingDINO:         FREE (local)  │
│ GPT-4o Region:         ~$0.005       │
│ GPT-4o State:          ~$0.005       │
│ GPT-4o Action:         ~$0.010       │
│ ─────────────────────────────────────│
│ TOTAL PER ACTION:      ~$0.020       │
└──────────────────────────────────────┘

Example Bug Reproduction (10 actions):
─────────────────────────────────────

Time:  18 sec × 10 = 180 sec = 3 minutes
Cost:  $0.02 × 10 = $0.20 per bug

Compared to:
Developer manually replaying: 10-30 minutes!
Cost to company:              $5-50 (dev time)

SAVINGS: 90% time, 99% cost!
```

---

## 9. Performance Metrics Visualization

```
Action Segmentation Accuracy:
─────────────────────────────
                    Precision  Recall  F1-Score
ViBR            ┌───────────────────────────────┐
┃┃┃┃┃┃┃┃┃┃  89% │                               │
├─┤           ├─► 93% │                          │
┃┃┃┃┃┃┃┃┃┃      │ 91% │                         │
GIFdroid     ┌───────────────────────────────┐
┃┃┃┃┃┃┃┃    82% │                               │
├─┤         ├─► 92% │                            │
┃┃┃┃┃┃┃    86% │                                │
Baseline    ┌───────────────────────────────┐
┃┃┃┃┃┃   70% │                               │
├─┤        ├─► 75% │                            │
┃┃┃┃   72% │                                   │
            └───────────────────────────────┘

State Comparison Accuracy:
──────────────────────────
ViBR Full          ████████████████████████ 0.86
ViBR No DINO       ██████████████████  0.72
SSIM               ███████████████  0.62

Bug Reproduction Rate:
──────────────────────
ViBR           █████████████████ 72%
GIFdroid       ███████████ 58%
Manual Replay  ████████ 50%
```

---

## 10. Complete System Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                          USER INPUT                              │
│                    (Bug Report Video + ADB)                      │
└──────────────────┬──────────────────────────────────────────────┘
                   │
        ┌──────────▼─────────────┐
        │    main.py             │
        │  • Load YAML config    │
        │  • Validate setup      │
        │  • Spawn segment_      │
        │    replay.py           │
        └──────────┬─────────────┘
                   │
        ┌──────────▼──────────────────────────────────────────┐
        │  segment_replay.py (Main Orchestrator)              │
        │  • Coordinate 5-stage pipeline                      │
        │  • Manage LLM calls                                 │
        │  • Handle ADB communication                         │
        └──────┬─────────────────────────────────┬────────────┘
               │                                 │
    ┌──────────▼──────────┐        ┌────────────▼──────────┐
    │  Segmentation       │        │  GroundingDINO        │
    │  ┌──────────────┐   │        │  ┌──────────────────┐ │
    │  │ clip_seg.py  │   │        │  │dino_detection.py│ │
    │  │ (CLIP embeds)│   │        │  │ • Load model    │ │
    │  └──────────────┘   │        │  │ • Detect regions│ │
    │  ┌──────────────┐   │        │  │ • Generate      │ │
    │  │yyh_utils.py │   │        │  │   annotations   │ │
    │  │ (SSIM)       │   │        │  └──────────────────┘ │
    │  └──────────────┘   │        └────────────────────────┘
    └────────┬────────────┘
             │
    ┌────────▼─────────────────────────────────────────┐
    │  Vision-Language Models                         │
    │  ┌─────────────────────────────────────────────┐│
    │  │ openai_api.py (GPT-4o)                      ││
    │  │ • ask_gpt_state_consistency()                ││
    │  │ • ask_gpt_for_relevant_regions()             ││
    │  │ • ask_gpt_for_action_region()                ││
    │  └─────────────────────────────────────────────┘│
    │  ┌─────────────────────────────────────────────┐│
    │  │ gemini_api.py (Gemini)                       ││
    │  │ • Alternative LLM support                    ││
    │  └─────────────────────────────────────────────┘│
    └────────┬─────────────────────────────────────────┘
             │
    ┌────────▼────────────────────────────────────────┐
    │  Device Control                                │
    │  ┌────────────────────────────────────────────┐│
    │  │ adb_device_controller.py                    ││
    │  │ • Manage ADB connection                     ││
    │  │ • Take screenshots                          ││
    │  │ • Get device state                          ││
    │  └────────────────────────────────────────────┘│
    │  ┌────────────────────────────────────────────┐│
    │  │ execute_action.py                           ││
    │  │ • Convert actions to ADB commands           ││
    │  │ • Tap, swipe, type, etc.                    ││
    │  └────────────────────────────────────────────┘│
    └────────┬────────────────────────────────────────┘
             │
┌────────────▼─────────────────────────────────────────┐
│              OUTPUT                                  │
│  • artifacts/  (frames, detections, etc.)            │
│  • logs/       (execution logs)                      │
│  • metadata.json (run info)                          │
│  ✓ Bug Reproduced or                                │
│  ✗ Reproduction Failed                              │
└────────────────────────────────────────────────────────┘
```

---

## Summary

ViBR is a **5-stage automated bug reproduction system** that:

1. **Segments** videos into actions (CLIP/SSIM)
2. **Detects** UI regions (GroundingDINO)
3. **Checks** screen consistency (GPT-4o)
4. **Infers** actions (GPT-4o)
5. **Executes** on devices (ADB)

All **automatically**, **cross-device**, and **intelligently**!

🤖 → 📹 → 🎬 → 🔍 → 📱 → ✅
