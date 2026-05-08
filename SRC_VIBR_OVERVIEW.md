# src_ViBR: Automated Bug Replay from Video-Based Reports
## Complete Overview with Simple Explanations

---

## What is src_ViBR?

**src_ViBR** is a tool that **automatically reproduces bugs** from video recordings. Instead of developers manually watching videos and clicking buttons, src_ViBR watches the video, understands what the user did, and **replays those exact actions on a test device**.

Think of it like a **robot watching a tutorial video** and then doing the exact same steps on its own Android phone.

---

## The Big Picture Problem

### Why is this hard?

Imagine you film a bug on your phone (resolution: 1440×2560, dark mode, English). But the developer tests it on a different phone (resolution: 1920×1080, light mode, French).

**Same app, same bug... but the screen looks COMPLETELY different!**

```
User's Phone              Developer's Phone
─────────────             ─────────────────
Dark theme           ≠     Light theme
1440×2560 resolution ≠     1920×1080 resolution
English labels       ≠     French labels
Different layout     ≠     Different layout
```

**The challenge:** How do you map "tap the red button here" on one phone to "tap the equivalent button there" on a different phone?

**Traditional approaches fail because:**
- Image processing (pixel matching) breaks with different layouts
- UI element detection needs the exact app structure
- Manual replay is slow and error-prone

---

## src_ViBR's Solution: Vision-Language Models + Signal Processing

src_ViBR uses **three key technologies**:

1. **CLIP/SSIM** - Find action boundaries in the video
2. **GroundingDINO** - Detect UI elements and interactive regions
3. **GPT-4o** - Understand GUI state and infer actions

---

## The 5-Step Process

### **Stage 1: Action Segmentation**
**Goal:** Break the video into "chunks" where each chunk is one user action

#### What Happens?
- Video contains 100s of frames
- We need to find where one action ends and the next begins
- Example: User taps a button → screen updates → action complete

#### Two Algorithms:

**SSIM (Structural Similarity Index)**
```
Frame 1 ──→ Compare pixels ──→ 98% similar
Frame 2 ──→ Compare pixels ──→ 97% similar
Frame 3 ──→ Compare pixels ──→ 15% similar ✓ ACTION BOUNDARY!
```
- Fast but struggles with semantic changes (color changes, layout shifts)
- Good for stable GUIs

**CLIP (Contrastive Learning Image Pre-training)**
```
Frame 1 ──→ Extract "meaning" (embedding) ──→ "showing button list"
Frame 2 ──→ Extract "meaning" (embedding) ──→ "showing button list"
Frame 3 ──→ Extract "meaning" (embedding) ──→ "showing confirmation dialog" ✓ BOUNDARY!
```
- Slower but understands semantic changes
- Better for dynamic GUIs with theme/layout variations

**Output:** Segments like:
```
Segment 1: [Frame 0-42]   "User taps Settings button"
Segment 2: [Frame 43-67]  "User scrolls down"
Segment 3: [Frame 68-90]  "User taps a checkbox"
```

---

### **Stage 2: Interactive Region Detection**
**Goal:** Find all clickable UI elements on each screen

#### What Happens?
- GroundingDINO scans the screenshot
- It identifies: buttons, text fields, icons, menus, toggles, checkboxes
- Each region gets a **bounding box** and an **index number**

#### Example:
```
Screenshots:
[Before action]                [After action]
┌──────────────────┐          ┌──────────────────┐
│  0: Settings btn │          │  0: Settings btn │
│     (tapped!)    │          │                  │
│                  │          │  Settings Menu:  │
│                  │          │  1: Language     │
│  1: Language     │  ──→     │  2: Theme        │
│  2: Theme        │          │  3: Account      │
│  3: Account      │          │  4: About        │
└──────────────────┘          └──────────────────┘
```

**Key insights:**
- GroundingDINO focuses on "interactive" regions (GUI elements)
- Each region has a center point: useful for "tap here"
- Bounding boxes handle size/position variations across devices

---

### **Stage 3: State Consistency Check**
**Goal:** Verify the device's current screen matches the video's reference screen (functionally)

#### Why This Matters?
Devices are different. We need to confirm:
- Same buttons are present?
- Same menus available?
- Can the user perform the same action?

#### The Smart Comparison:
```
                              Device Screenshot
Reference Screenshot          ──────────────────
    ↓                         "What is the device showing NOW?"
┌─────────────┐              
│ Pre-action  │              
│  frame      │      ────→ GPT-4o Vision
│ (focus on   │             "Are these functionally
│  ROI)       │              equivalent?"
└─────────────┘
                              
                              YES ✓  → Proceed with action
                              NO  ✗  → Guided exploration
```

#### What "Functionally Equivalent" Means?
- ✓ Same buttons/menus present
- ✓ Same text/icons visible
- ✓ Same actions can be performed
- ✗ Icon color slightly different (doesn't matter)
- ✗ Text font changed (doesn't matter)
- ✗ Layout order is different (matters if affects action)

**Real Example:**
```
Device: Light theme, English, 1920×1080
Video:  Dark theme, French, 1440×2560

GPT-4o: "Settings button position is different,
         but I can see it, and the user can tap it.
         States are equivalent! ✓"
```

---

### **Stage 4: Action Inference**
**Goal:** Figure out what action the user performed and where/how to replay it

#### What Are the Possible Actions?

| Action | Example | Output |
|--------|---------|--------|
| **Tap** | Click button | `{"action": "tap", "region": 2}` |
| **Swipe** | Scroll list up | `{"action": "swipe", "from": [x, y], "to": [x, y], "duration": 500}` |
| **Type Text** | Enter search query | `{"action": "input_text", "text": "hello"}` |
| **Back** | Go back | `{"action": "back"}` |
| **Home** | Home screen | `{"action": "home"}` |
| **Wait** | Let animation finish | `{"action": "wait", "duration": 1000}` |
| **No Action** | Screen auto-refreshed | `{"action": "no action"}` |

#### How GPT-4o Infers Actions:

```
GPT-4o gets THREE screenshots:

1. Before-Action Frame (from video)
   "I see a list of items, Settings button highlighted"

2. After-Action Frame (from video)
   "Settings menu opened! Items are gone."

3. Current Device Frame
   "Device shows a list of items (looks like #1)"

GPT-4o decides:
"User tapped the Settings button (index 2).
Device also has Settings button in same position.
Action: tap region 2"
```

---

### **Stage 5: Device Execution**
**Goal:** Execute the inferred action on the real device

#### The Execution Flow:

```
                   ┌─────────────────────────────────┐
                   │  Inferred Action                │
                   │  {"action": "tap", "region": 2} │
                   └──────────────┬──────────────────┘
                                  │
                   ┌──────────────▼──────────────┐
                   │ Convert region index to    │
                   │ device coordinates         │
                   │ Region 2 = (340, 512)      │
                   └──────────────┬──────────────┘
                                  │
                   ┌──────────────▼──────────────┐
                   │  ADB Command                │
                   │  adb shell input tap 340   │
                   │  512                       │
                   └──────────────┬──────────────┘
                                  │
                   ┌──────────────▼──────────────┐
                   │  Device executes tap       │
                   │  Screen updates            │
                   └──────────────┬──────────────┘
                                  │
                   ┌──────────────▼──────────────┐
                   │  Screenshot taken          │
                   │  Compare with expected     │
                   │  If match: continue ✓      │
                   │  If no match: explore 🗺️   │
                   └─────────────────────────────┘
```

#### What Happens if Device Screen Doesn't Match?

**Scenario:** Device is in wrong state (showed popup, different menu)

**Solution: Guided Exploration**
- GPT-4o receives: current device state + target state
- GPT-4o suggests: "Press back first" or "Close this popup"
- ViBR executes the guidance commands
- Once aligned: replay the actual action

---

## Architecture Overview

### Component Roles:

```
┌─────────────────────────────────────────────────────────┐
│  main.py (Orchestrator)                                 │
│  ✓ Loads YAML config                                   │
│  ✓ Validates paths & dependencies                      │
│  ✓ Spawns segment_replay.py as subprocess              │
└─────────────────────────────────────────────────────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ clip_seg.py  │  │ segment_     │  │ yyh_utils.py │
│              │  │ replay.py    │  │              │
│ CLIP-based   │  │              │  │ SSIM-based   │
│ segmentation │  │ Main flow:   │  │ segmentation │
│              │  │ 1. Segment   │  │              │
│              │  │ 2. Detect    │  │ Pixel-level  │
│              │  │ 3. Compare   │  │ comparison   │
│              │  │ 4. Infer     │  │              │
│              │  │ 5. Execute   │  │              │
└──────────────┘  └──────────────┘  └──────────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│dino_         │  │openai_api.py │  │adb_device_   │
│detection.py  │  │              │  │controller.py │
│              │  │ GPT-4o calls:│  │              │
│GroundingDINO│  │ • Consistency│  │ ADB commands │
│ detection    │  │ • Region     │  │ for device   │
│              │  │ • Action     │  │ execution    │
│ Finds UI     │  │ • Inference  │  │              │
│ elements     │  │              │  │              │
└──────────────┘  └──────────────┘  └──────────────┘
```

---

## Key Technologies Explained Simply

### 1. CLIP (Contrastive Learning Image Pre-Training)
**What it does:** Extracts the "meaning" of an image as a number vector

**Simple analogy:**
- SSIM: "Pixel 1 is blue, pixel 2 is blue... screens 98% identical"
- CLIP: "This screen shows 'a list of settings'. That screen shows 'an open menu'. They're different!"

**Why it matters:** Understands semantic meaning, not just pixel similarity

---

### 2. GroundingDINO (Grounded Detection In the wild with ON-vocabulary detection)
**What it does:** Identifies "things you can click" in a screenshot

**Simple analogy:**
- You look at a screenshot and instantly find: buttons, text fields, menus
- GroundingDINO does the same thing!

**Text Prompt Used:**
```
"header bar. navigation bar. toolbar. button. icon. 
checkbox. toggle. text input. search bar. text field. 
image. card. list item. bottom navigation. tab bar"
```

**Output Example:**
```
Region 0: "button" at (340, 512) with 0.89 confidence
Region 1: "text input" at (200, 620) with 0.92 confidence
Region 2: "checkbox" at (100, 450) with 0.85 confidence
```

---

### 3. GPT-4o (Vision-Language Model)
**What it does:** Understands images and answers questions about them

**Uses in ViBR:**

a) **Consistency Checking**
```
Q: "Are these two Android screens functionally equivalent
   for performing this action: tap Settings button?"
A: "Yes, both screens show Settings button in accessible position"
```

b) **Relevant Region Selection**
```
Q: "Which UI regions changed between these two frames?"
A: "[0, 2, 5] - Regions 0, 2, and 5 changed"
```

c) **Action Inference**
```
Q: "What action caused this transition from Frame A to Frame B?
   What's the equivalent action on the current device?"
A: {"action": "tap", "region": 2, "description": "Tap Settings"}
```

---

## Performance Insights

### Action Segmentation Accuracy:
- **ViBR:** 89.3% precision, 92.8% recall, 90.9% F1-score
- **GIFdroid:** 82.1% precision, 91.7% recall, 86.5% F1-score
- **Traditional methods:** 70-80% (way worse)

### GUI State Comparison:
- **ViBR with GroundingDINO:** 0.86 F1-score
- **ViBR without GroundingDINO:** 0.72 F1-score
- **SSIM (pixel-based):** 0.62 F1-score

**Key insight:** Region-aware (GroundingDINO) comparison is 15% better!

### Bug Reproduction Success:
- **72% of bugs successfully reproduced**
- Average time: **302.6 seconds** per bug
- Cost per bug: **$0.02** (using GPT-4o)

---

## Simple Walkthrough: Real Example

Let's say user reports: *"Settings button doesn't highlight when I click it"*

### Step 1: Action Segmentation
```
Video Analysis:
Frame 0-50:   Stable (user looking at screen)
Frame 51-70:  User's finger moving → BOUNDARY!
Frame 71-100: Settings menu opened
RESULT: Action identified at frame 50-51
```

### Step 2: Region Detection
```
Frame 50 (before):
[0] Settings button at (340, 500)
[1] Search at (200, 200)
[2] About at (340, 600)

Frame 100 (after):
[0] Settings menu opened
[1] Language option
[2] Theme option
```

### Step 3: State Check
```
Current Device Screenshot:
Shows same app, same Settings button position

GPT-4o: "Both screens show accessible Settings button.
         Equivalent! ✓"
```

### Step 4: Action Inference
```
GPT-4o receives:
- Frame 50: "Settings button visible"
- Frame 100: "Settings menu opened"
- Current: "Settings button visible (same position)"

GPT-4o: "Action = tap region [0]"
```

### Step 5: Execution
```
ADB Command: input tap 340 500
Device: Tap executed
Result: Settings opens
Screenshot shows: Settings menu (matches expected!)
✓ BUG REPRODUCED!
```

---

## Summary: Why ViBR is Smart

| Problem | ViBR's Solution |
|---------|-----------------|
| **Device variations** | Vision-LLM (GPT-4o) understands semantic meaning, not pixels |
| **Complex GUIs** | GroundingDINO finds interactive elements automatically |
| **Subtle transitions** | CLIP embeddings catch semantic changes SSIM misses |
| **Guided recovery** | If device state doesn't match, explore first before action |
| **Low cost** | ~$0.02 per bug using GPT-4o API |
| **No instrumentation** | Works with any app (no special setup needed) |

---

## Diagram Legend

```
📹 = Video/Input
🎬 = Processing stage
📊 = Data/Frames
🔍 = Detection/Analysis
🤖 = AI/Machine Learning
✔️ = Verification
🎯 = Target/Goal
🗺️ = Navigation/Exploration
📱 = Device action
✅ = Success
```

---

## Key Takeaway

src_ViBR is like a **robot that watches videos and learns**:
1. It identifies when actions occur (segmentation)
2. It finds what to click on (region detection)
3. It checks if the current state is ready (consistency)
4. It figures out what action to do (inference)
5. It executes the action on a real device (execution)

All **automatically** and **intelligently**, across different devices with different layouts, themes, and languages!
