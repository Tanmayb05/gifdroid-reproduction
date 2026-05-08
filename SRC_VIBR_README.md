# src_ViBR: Complete Documentation Index

## Overview

This directory contains comprehensive documentation about **src_ViBR** (Vision Intelligence-driven Bug Reproduction), a tool that automatically reproduces Android app bugs from video recordings.

**One sentence:** A robot that watches bug videos and replays them on test devices automatically.

---

## 📚 Documentation Files

### 1. **SRC_VIBR_SLIDES_SUMMARY.md** ← START HERE!
**Best for:** Quick 15-slide presentation overview
- **What:** High-level slides covering all aspects
- **Format:** Slide-by-slide breakdown
- **Time to read:** 15 minutes
- **Perfect for:** Presentations, quick understanding

### 2. **SRC_VIBR_QUICK_REFERENCE.md**
**Best for:** Quick lookup and cheat sheet
- **What:** Tables, comparisons, performance metrics
- **Format:** Organized by topic with quick facts
- **Time to read:** 10 minutes
- **Perfect for:** Need info on one specific aspect

### 3. **SRC_VIBR_OVERVIEW.md**
**Best for:** Complete technical deep-dive
- **What:** Detailed explanations of each stage
- **Format:** In-depth with real examples
- **Time to read:** 30 minutes
- **Perfect for:** Deep understanding, teaching others

### 4. **SRC_VIBR_VISUAL_GUIDE.md**
**Best for:** Understanding through ASCII diagrams
- **What:** Step-by-step visual flows and diagrams
- **Format:** ASCII art with annotations
- **Time to read:** 20 minutes
- **Perfect for:** Visual learners, seeing the flow

### 5. **SRC_VIBR_README.md** (this file)
**Best for:** Navigation and getting started
- **What:** Index and guide to all documents
- **Format:** Organized reference
- **Time to read:** 5 minutes
- **Perfect for:** Finding what you need

---

## 🎯 How to Use These Docs

### If you have 5 minutes
Read: **Quick Summary** below

### If you have 15 minutes
Read: **SRC_VIBR_SLIDES_SUMMARY.md** (Slides 1-10)

### If you have 30 minutes
Read: **SRC_VIBR_OVERVIEW.md** (Sections 1-5)

### If you need specific info
Use: **SRC_VIBR_QUICK_REFERENCE.md** (find the table)

### If you're a visual learner
Read: **SRC_VIBR_VISUAL_GUIDE.md** (ASCII diagrams)

### If you want to present it
Use: **SRC_VIBR_SLIDES_SUMMARY.md** (all 15 slides)

---

## 🚀 Quick Summary

### The Problem
Developers waste time manually testing bug reports because:
- Different devices look different (different themes, resolutions, layouts)
- Manual replay is slow (20-30 minutes per bug)
- Manual replay is error-prone
- Manual replay is expensive ($5-50 per bug in developer time)

### The Solution: src_ViBR
A 5-stage intelligent system:
1. **Segment** video into actions (CLIP/SSIM)
2. **Detect** clickable UI regions (GroundingDINO)
3. **Check** if device screen matches reference (GPT-4o)
4. **Infer** what action to perform (GPT-4o)
5. **Execute** action on device (ADB)

### The Results
- ✅ **72% success rate** (vs 58% for competitors)
- ✅ **~5 minutes per bug** (vs 20-30 minutes manual)
- ✅ **$0.02 per bug** (vs $5-50 developer cost)
- ✅ **Cross-device** (handles different phones)
- ✅ **Smart** (understands intent, not just pixels)

---

## 🏗️ Architecture

```
Video Input
    ↓
1️⃣  Action Segmentation (CLIP or SSIM)
    ↓
2️⃣  Interactive Region Detection (GroundingDINO)
    ↓
3️⃣  State Consistency Check (GPT-4o Vision)
    ↓
4️⃣  Action Inference (GPT-4o Reasoning)
    ↓
5️⃣  Device Execution (ADB Commands)
    ↓
✅ Bug Reproduced!
```

---

## 🔑 Key Technologies

| Tech | Purpose | Why Smart |
|------|---------|-----------|
| **CLIP** | Video segmentation | Understands *intent*, not pixels |
| **SSIM** | Fast segmentation | Good for stable GUIs |
| **GroundingDINO** | Find UI elements | Works across device variations |
| **GPT-4o** | Make smart decisions | Understands semantics & context |
| **ADB** | Device control | Android standard automation |

---

## 📊 Performance

### Segmentation (Finding action boundaries)
```
ViBR:     89% precision, 93% recall, 91% F1
GIFdroid: 82% precision, 92% recall, 87% F1  
Baseline: 70-75%
```
**ViBR wins by 7.4%!**

### State Comparison (Current screen matches video?)
```
ViBR (with GroundingDINO): 0.86 F1-score
ViBR (without):           0.72 F1-score
SSIM:                     0.62 F1-score
```
**GroundingDINO provides +15% improvement!**

### Bug Reproduction Success
```
ViBR:     72% success
GIFdroid: 58% success
Manual:   ~50% success
```

---

## 📖 Understanding the 5 Stages

### Stage 1: Segmentation
**Goal:** Break long video into chunks, each chunk = one action
**How:** Analyze consecutive frames with CLIP (semantic) or SSIM (pixel-based)
**Output:** Scene boundaries like "frames 50-51 = tap Settings"

### Stage 2: Region Detection
**Goal:** Find all clickable UI elements (buttons, menus, text fields)
**How:** GroundingDINO scans screenshot, detects interactive regions
**Output:** Regions with indices: [0] Settings, [1] Help, [2] About

### Stage 3: State Consistency Check
**Goal:** Verify device's current screen matches video reference (functionally)
**How:** GPT-4o compares pre-action frame with current device state
**Output:** YES (proceed) or NO (explore first with guidance)

### Stage 4: Action Inference
**Goal:** Decide what action caused the transition and how to replay it
**How:** GPT-4o analyzes before/after frames + current device state
**Output:** Action command: {"action": "tap", "region": 0, "coords": [340, 500]}

### Stage 5: Execution
**Goal:** Execute inferred action on real device
**How:** Convert to ADB command, execute, verify results
**Output:** ✓ Success (screenshot matches expected) or ✗ Fail (retry)

---

## 💡 Key Insights

### Why ViBR Works Cross-Device

Instead of pixel-perfect matching:
```
❌ Device A: Button at (100, 200)
   Device B: Button at (340, 500)
   Can't match pixels!
```

ViBR uses semantic understanding:
```
✅ Device A: Region 0 = Settings button
   Device B: Region 0 = Settings button
   Can map regions!
```

### Why CLIP Beats SSIM for Complex UIs

```
SSIM: "Screen changed from 99% blue to 85% blue" → boundary!
CLIP: "Screen changed from 'list view' to 'menu view'" → boundary!
```

CLIP understands semantic changes that SSIM misses.

### Why GroundingDINO Matters

Instead of guessing "click at pixel (340, 500)":
- GroundingDINO identifies: "Region 2 is a button at (340, 500)"
- On different device: Region 2 is still identifiable!
- Just with different coordinates

---

## 🎓 Learning Path

### Beginner: Just want overview?
1. Read: This file (Quick Summary)
2. View: FigJam diagrams (visual overview)
3. Time: 5 minutes

### Intermediate: Want to understand?
1. Read: SRC_VIBR_SLIDES_SUMMARY.md (Slides 1-10)
2. Read: SRC_VIBR_VISUAL_GUIDE.md (Stage diagrams)
3. Time: 25 minutes

### Advanced: Want deep dive?
1. Read: SRC_VIBR_OVERVIEW.md (all sections)
2. Read: SRC_VIBR_QUICK_REFERENCE.md (tables & metrics)
3. Review: Code in src_ViBR/approach/
4. Time: 60 minutes

### Expert: Want to modify/extend?
1. Read: All documentation
2. Study: Code implementation
3. Review: Research paper (docs/research_papers/2025 - ViBR.pdf)
4. Time: 120+ minutes

---

## 🗂️ Project Structure

```
src_ViBR/
├── README.md                    # Original README
├── config.py                    # Configuration parsing
├── main.py                      # Entry point
├── io_utils.py                  # File utilities
├── logging_utils.py             # Logging setup
│
├── approach/
│   ├── segment_replay.py        # Main orchestrator (5-stage pipeline)
│   ├── clip_seg.py              # CLIP-based segmentation
│   ├── yyh_utils.py             # SSIM-based segmentation
│   ├── dino_detection.py        # GroundingDINO wrapper
│   ├── openai_api.py            # GPT-4o API calls
│   ├── gemini_api.py            # Gemini API support
│   ├── adb_device_controller.py # Device interaction
│   ├── execute_action.py        # Action execution
│   ├── input_formatter.py       # Android XML parsing
│   └── yyh_utils.py             # Video processing
│
├── GroundingDINO/               # Object detection submodule
│
├── input/
│   └── config.yml               # Configuration file
│
└── apps/
    └── <app_name>/llm/ViBR/
        ├── handheld/
        │   └── run-001/
        │       ├── artifacts/   # Frames, segmentation
        │       ├── logs/        # Execution logs
        │       └── metadata.json
        └── screenrec/
```

---

## 🔧 Configuration

Basic config structure:
```yaml
config:
  algorithm: "clip"      # or "ssim"
  llm: "openai"         # or "gemini"
  llm_model: "gpt-4o"
  
  runs:
    - app_name: "adaway"
      video_path: "hhv"  # handheld-video shorthand
      algorithm: "clip"
```

---

## 💰 Cost Analysis

### Per Action (e.g., one tap)
- GroundingDINO: Free (local)
- GPT-4o calls: ~$0.02
- **Total: $0.02 per action, ~18 seconds**

### Per Bug (typical: 10 actions)
- Time: 5 minutes
- Cost: $0.20
- **vs Manual: 25 minutes, $5-50**

---

## ✅ Strengths & Limitations

### Strengths
✅ Handles device variations (resolution, theme, language)
✅ No app instrumentation needed
✅ Works on black-box apps
✅ Cross-device compatibility
✅ Cheap & fast
✅ Understands intent (not just pixels)

### Limitations
❌ 72% success (not 100%)
❌ Struggles with complex interactions
❌ Can't handle biometric auth
❌ Timing-dependent bugs difficult
❌ Dynamic/real-time content challenging

---

## 📚 Additional Resources

### Research & Papers
- `docs/research_papers/2025 - ViBR.pdf` - Original research paper

### Comparisons
- `docs/ViBR-vs-src_llm-comparison.md` - vs other approaches

### Code Examples
- `src_ViBR/input/config.yml` - Configuration examples
- `src_ViBR/approach/` - Implementation details

### Evaluation
- `src_ViBR/evaluation/` - Benchmark results

---

## 🎯 Quick Navigation

**Need help with...**

| Question | File | Section |
|----------|------|---------|
| "What is src_ViBR?" | SLIDES_SUMMARY | Slide 1 |
| "How does it work?" | OVERVIEW | "The 5-Step Process" |
| "How is it different?" | SLIDES_SUMMARY | Slide 11 |
| "What are the results?" | QUICK_REFERENCE | Performance section |
| "Can I see diagrams?" | VISUAL_GUIDE | All sections |
| "How much does it cost?" | QUICK_REFERENCE | Cost Breakdown |
| "How accurate is it?" | SLIDES_SUMMARY | Slide 9 |
| "Show me real example" | OVERVIEW | "Real Example Walkthrough" |
| "What's the architecture?" | VISUAL_GUIDE | Diagram 10 |
| "Detailed explanation?" | OVERVIEW | All sections |

---

## 🚀 Getting Started

1. **First time?** Read: SRC_VIBR_SLIDES_SUMMARY.md
2. **Need specifics?** Search: SRC_VIBR_QUICK_REFERENCE.md
3. **Deep dive?** Read: SRC_VIBR_OVERVIEW.md
4. **Visual person?** Read: SRC_VIBR_VISUAL_GUIDE.md
5. **Want code?** Check: src_ViBR/approach/ folder

---

## 📞 Questions?

### Common Questions

**Q: How do you handle device differences?**
A: Using GroundingDINO to detect regions semantically, not by pixel coordinates. Regions map universally across devices.

**Q: Why not just image-match?**
A: Image matching breaks with theme changes, layout differences, and resolution variations. ViBR understands intent instead.

**Q: Can it handle my app?**
A: Most Android apps with standard UI elements. Struggles with games, real-time content, biometric auth.

**Q: How much does it cost?**
A: ~$0.02 per action, ~$0.20 per average bug. Compare to $5-50 developer cost.

**Q: Is it 100% accurate?**
A: No, 72% success rate. But 72% > manual ~50%, and much faster/cheaper.

---

## 📝 Summary

src_ViBR is a **Vision-Language Model-powered** tool that:
- ✅ Watches bug videos
- ✅ Understands user actions
- ✅ Handles device variations intelligently
- ✅ Replays bugs automatically
- ✅ Works across different phones

**Result:** Automated bug reproduction that's fast, cheap, and smart!

---

**Last Updated:** May 8, 2026
**Version:** Complete Documentation Set v1.0
**Related:** FigJam diagrams, GitHub code, research paper
