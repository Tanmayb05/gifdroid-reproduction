# src_ViBR vs src_llm: A Detailed Comparison

Both approaches use LLMs to generate action sequences from video recordings, but they have fundamentally different architectures and philosophies.

---

## At a Glance

| Aspect | **src_ViBR** | **src_llm** |
|--------|-------------|-----------|
| **Input** | Video (frames) | Video (keyframes sampled) |
| **Output** | Live action replay on device | Trace/sequence (no device needed) |
| **Vision** | GroundingDINO + CLIP + VLM | LLM's multimodal capabilities |
| **Device Required** | ✅ **Yes** (live Android device/emulator) | ❌ **No** (offline analysis) |
| **Replays Bug** | ✅ **Yes** (executes on actual device) | ❌ **No** (generates action sequence only) |
| **Segmentation** | CLIP/SSIM-based scene detection | SSIM keyframe selection |
| **State Consistency** | Checks before each action | Generates trace blindly |
| **Best For** | Bug reproduction, functional testing | Understanding bug narratives, trace generation |
| **Feedback Loop** | Live (take screenshot → compare → act) | Batch (process once, output trace) |

---

## Detailed Comparison

### 1. **Input Representation**

#### src_ViBR
- **Takes the entire video** (all frames)
- **Segments into scenes** using CLIP embeddings or SSIM (Luminance channel)
- **Detects scene boundaries** by finding sharp drops in frame-to-frame similarity
- Each scene = a user action (tap, scroll, input)

```
Video: frame_0 → frame_1 → frame_2 → ... → frame_N
                    ↓
         Segmentation (CLIP or SSIM)
                    ↓
Scene 1: [f0-f5]   Scene 2: [f5-f12]   Scene 3: [f12-f20]
```

#### src_llm
- **Samples keyframes** from the video (e.g., 1.5 FPS → 100 frames max)
- **Selects "stable" keyframes** using SSIM (same as GIFdroid)
  - Only keeps frames that differ significantly from neighbors
  - Filters out in-between frames (motion blur, animations)
- **Passes keyframes + metadata** to LLM for analysis

```
Video: frame_0 → frame_1 → frame_2 → ... → frame_N
                    ↓
         Keyframe Selection (SSIM)
                    ↓
        KF_0, KF_5, KF_12, KF_20  (sparse set)
                    ↓
           LLM processes these 4 keyframes
```

**Key Difference:** ViBR uses all frames and groups them; src_llm cherry-picks representative frames upfront.

---

### 2. **Vision Understanding**

#### src_ViBR
- **Multi-stage vision pipeline:**
  1. **CLIP** (Contrastive Language-Image Pretraining)
     - Encodes frames into embeddings
     - Used to detect scene boundaries (cosine similarity)
     - Also extracts Y-luminance for noise reduction

  2. **GroundingDINO** (Open-vocabulary object detection)
     - Detects interactive regions on the recorded start frame
     - Generic GUI prompts: "button", "text field", "search bar", etc.
     - Produces candidate bounding boxes with confidence scores
     - Handles vision-only UI understanding (no app instrumentation needed)

  3. **GPT-4o VLM** (Vision-Language Model)
     - Selects which GroundingDINO region matters
     - Compares GUI state between recording and device
     - Infers actions based on semantic reasoning
     - Handles dark mode, resolution differences, etc.

#### src_llm
- **Single LLM with multimodal capabilities:**
  - Uses the LLM's built-in vision encoder
  - Supports multiple providers: Ollama (llama, qwen, minicpm, llava), Gemini
  - No specialized UI detection (GroundingDINO)
  - No scene segmentation via vision (uses SSIM heuristic)
  - LLM reasons about the entire keyframe directly
  - Falls back to deterministic heuristic if LLM output is unparseable

**Key Difference:** ViBR decomposes the problem (CLIP for segmentation, GroundingDINO for regions, GPT-4o for reasoning). src_llm relies on the LLM to do everything.

---

### 3. **Core Algorithm: The Replay Loop**

#### src_ViBR (Video-Guided Replay)
```
For each scene in video:
  ├─ Take recorded start frame
  ├─ Take recorded end frame
  │
  ├─ (A) Detect interactive regions
  │    └─ Run GroundingDINO on start frame
  │       Output: candidate regions (button, text field, etc.)
  │
  ├─ (B) Identify which region changed
  │    ├─ Show GPT-4o: dual-view image (start + end frames)
  │    ├─ Show detected regions numbered
  │    └─ GPT-4o picks: "Region 2 changed" → ROI identified
  │
  ├─ (C) Check state consistency
  │    ├─ Take live device screenshot
  │    ├─ Show GPT-4o: recorded ROI vs live screen
  │    └─ GPT-4o answers: "Same state? YES/NO"
  │
  ├─ (D) Infer action based on consistency
  │    ├─ If YES (consistent):
  │    │   └─ Show GPT-4o: recorded-start, recorded-end, live-screen
  │    │       GPT-4o predicts: tap/scroll/input action
  │    │
  │    └─ If NO (inconsistent):
  │        └─ Show GPT-4o: recorded-start (target), live-screen (current)
  │            GPT-4o generates recovery action to reach target state
  │
  └─ (E) Execute action on device via ADB
     ├─ If action succeeds: take new screenshot, continue
     └─ If recovery fails 3×: skip scene, continue
```

**Characteristics:**
- ✅ **Reactive**: sees live device state, adapts in real-time
- ✅ **State-aware**: checks consistency before acting
- ✅ **Recoverable**: tries exploratory actions if stuck
- ❌ **Slow**: VLM queries per scene + ADB delays
- ❌ **Requires device**: can't run offline

#### src_llm (Trace Generation)
```
Sample keyframes from video:
  ├─ KF_0, KF_5, KF_12, KF_20
  
For each keyframe:
  ├─ Encode keyframe as base64 image
  ├─ Send to LLM with action-prediction prompt:
  │   "Given this keyframe, what action likely happened?
  │    action_type: tap | scroll | type_text | press_back | wait | done"
  │
  ├─ Parse LLM output (JSON or fallback to heuristic)
  │   Example: {"action_type": "tap", "target": "button", "confidence": 0.92}
  │
  └─ Store in execution_trace.json (no execution)

Output: execution_trace.json
  [
    {"step": 1, "frame": "kf-0001.png", "action_type": "launch", ...},
    {"step": 2, "frame": "kf-0005.png", "action_type": "tap", ...},
    {"step": 3, "frame": "kf-0012.png", "action_type": "scroll", ...},
  ]
```

**Characteristics:**
- ✅ **Fast**: batch process, no live device
- ✅ **Offline**: analyze anywhere, anytime
- ✅ **Parallelizable**: process multiple keyframes concurrently
- ❌ **Blind**: no device feedback, can't recover from mistakes
- ❌ **No execution**: just generates a trace
- ❌ **Stateless**: each keyframe analyzed independently

---

### 4. **Performance Results (from apps/description.txt)**

#### Example 1: **wifi-analyser**
| Config | ViBR (GPT-4o mini) | Gemini 2.5-pro | Best |
|--------|-------------------|----------------|------|
| handheld | 3/4 ❌ | 4/4 ✅ | Gemini |
| screenrec | 3/8 ❌ | 6/8 ✅ | Gemini |

#### Example 2: **portauthority**
| Config | ViBR (GPT-4o mini) | Gemini 2.5-pro | Best |
|--------|-------------------|----------------|------|
| handheld | 3/2 (overexecute) | 2/2 ✅ | Gemini |
| screenrec | 6/6 ✅ | 6/6 ✅ | Tie |

#### Example 3: **luxalarm**
| Config | ViBR (GPT-4o mini) | Gemini 2.5-pro | Best |
|--------|-------------------|----------------|------|
| handheld | 0/8 (stuck) ❌ | 2/8 (partial) | Gemini |
| screenrec | 0/9 (stuck) ❌ | 6/9 (partial) | Gemini |

#### Example 4: **jigsaw**
| Config | ViBR (GPT-4o mini) | Gemini 2.5-pro | Best |
|--------|-------------------|----------------|------|
| handheld | 0/5 (stuck) ❌ | 0/5 (stuck) ❌ | Both fail |
| screenrec | 0/4 (stuck) ❌ | 2/4 (partial) | Gemini |

#### Example 5: **homemedkit**
| Config | ViBR (GPT-4o) | Gemini 2.5-pro | Best |
|--------|--------------|----------------|------|
| handheld | 0/10 (stuck) ❌ | 7/10 (early exit) | Gemini |
| screenrec | 0/1 ❌ | 6/10 (early exit) | Gemini |

**Summary:**
- **Gemini 2.5-pro is winning** across most apps
- **ViBR gets stuck** on apps with modal dialogs or complex state transitions
- **Early exit** in Gemini means it completed some steps correctly but bailed out early (conservative)
- **Complete failures** in ViBR suggest issues with GroundingDINO detection or LLM confusion on layout changes

---

### 5. **Why Gemini (src_llm via Gemini provider) Outperforms ViBR**

Based on the results, here are the likely reasons:

#### A. **Gemini Has Better Vision Understanding**
- Gemini 2.5-pro is trained on diverse UI screenshots
- Better at detecting interactive elements without needing GroundingDINO
- Handles resolution/layout variations better out-of-the-box

#### B. **Simpler Pipeline = Fewer Failure Points**
ViBR's multi-stage approach has many places to fail:
1. Scene segmentation mistake → wrong action boundaries
2. GroundingDINO misses a region → wrong ROI selection
3. State consistency check fails → wrong recovery action
4. Each stage compounds errors

src_llm (Gemini):
1. LLM sees keyframe → predicts action
   - Single pass, fewer dependencies

#### C. **Gemini Knows App Conventions**
Gemini has seen thousands of Android apps during pretraining:
- Recognizes Material Design patterns
- Understands common app flows (onboarding, forms, dialogs)
- Better at inferring user intent from UI alone

#### D. **ViBR's Device Requirements Are a Bottleneck**
- ViBR must run on a live device
- ADB communication delays accumulate
- Screen state might change between LLM query and execution
- GroundingDINO detection is for the **recorded** frame, not the live device (context mismatch)

#### E. **Early Exit Strategy Works Better**
Gemini's "early exit" (stops after completing what it can) is actually smarter than ViBR's "stuck indefinitely":
- 7/10 is better than 0/10
- Graceful degradation beats spinning on incompatible state

---

### 6. **When to Use Each**

#### Use **src_ViBR** if:
- ✅ You have a **live Android device** available
- ✅ You want to **actually replay the bug** (not just trace it)
- ✅ You need **interactive state management** (can recover from stuck states)
- ✅ You're doing **functional testing** where the actual execution matters
- ✅ You want fine-grained control over each action

#### Use **src_llm** (with Gemini) if:
- ✅ You want **fast offline analysis** (no device needed)
- ✅ You want to **understand the bug narrative** (what actions caused it)
- ✅ You're **analyzing recorded bugs** for documentation
- ✅ You want **parallelizable processing** (batch many videos)
- ✅ You have **limited device resources** (no real device needed)
- ✅ You want **better overall accuracy** (Gemini outperforms ViBR)

---

### 7. **Key Architectural Differences Summary**

| Dimension | src_ViBR | src_llm |
|-----------|----------|---------|
| **Philosophy** | "See device → reason → act → see result" | "Analyze frames → infer actions → output trace" |
| **Vision Model** | CLIP (segmentation) + GroundingDINO (regions) + GPT-4o (reasoning) | Single multimodal LLM (Gemini, Ollama, etc.) |
| **State Loop** | Closed-loop (live feedback) | Open-loop (batch prediction) |
| **Execution** | On-device ADB commands | None (trace generation) |
| **Keyframes** | All frames grouped by scene | Cherry-picked stable frames |
| **Error Recovery** | Yes (up to 3 retries) | No (one-shot prediction) |
| **Speed** | Slow (~289s per run typical) | Fast (seconds, offline) |
| **Accuracy** | Lower (0-3/X) | Higher (2-7/X) |
| **Complexity** | High (4 components) | Low (1 LLM) |

---

## Conclusion

**src_llm with Gemini is the better approach overall** based on the test results. It offers:
1. **Better accuracy** (Gemini 2.5-pro > GPT-4o mini)
2. **Faster execution** (no device communication)
3. **Simpler pipeline** (fewer failure points)
4. **Offline processing** (scale easily)

**ViBR remains valuable** for:
1. **Live bug reproduction** (actually executing on device)
2. **Interactive recovery** (exploring to fix stuck states)
3. **Functional validation** (proof that bugs are fixed)

The trade-off: ViBR trades accuracy for *actual* execution; src_llm trades execution for better *understanding*.
