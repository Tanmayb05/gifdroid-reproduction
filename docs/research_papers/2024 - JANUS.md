# 📄 JANUS: Semantic GUI Scene Learning and Video Alignment for Detecting Duplicate Video-based Bug Reports

**Domain:** Android Bug Reporting (Vision / Video Analysis / Duplicate Detection)

---

## 🧾 Paper Info

* **Title:** Semantic GUI Scene Learning and Video Alignment for Detecting Duplicate Video-based Bug Reports
* **Authors:** Yanfu Yan, Nathan Cooper, Oscar Chaparro, Kevin Moran, Denys Poshyvanyk
* **Year / Venue:** 2024 / ICSE '24: Proceedings of the 46th IEEE/ACM International Conference on Software Engineering, April 14–20, 2024, Lisbon, Portugal
* **Link:** https://doi.org/10.1145/3597503.3639163
* **Code Available:** Not explicitly mentioned

---

## 🎯 Problem Statement

* **What problem is this paper solving?**
  * Automatically detecting **duplicate** video-based bug reports — identifying when two different videos depict the same underlying app bug
  * _Reference:_ [Abstract, Page 1]

* **Why is this problem important?**
  * Video-based bug reports are increasingly common (15–35% increase in usage 2018–2020 on GitHub); manual review of duplicates wastes developer time; >13% of reports in issue trackers identified as duplicate
  * _Reference:_ [Section 1, Page 1]

* **What assumptions does the paper make?**
  * Input: two video-based bug reports to compare; both show GUI screen recordings of Android apps; videos depict crashes or functional bugs; sampled at fixed rate (every 6th frame)
  * _Reference:_ [Section 2.2, Page 2]

* **Gap addressed:** Existing duplicate detection relies on textual reports; prior video-based approach (TANGO) uses contrastive learning + CNNs for visual features but misses GUI-specific semantic information; no approach combines visual, textual, and sequential video information
  * _Reference:_ [Section 1, Page 1; Section 6.1, Page 10]

---

## 📥 Input Representation (CRITICAL)

* **What is the input to the system?**
   * [ ] Text bug report
   * [x] GUI screenshots (sampled video frames)
   * [ ] Execution traces
   * [x] Video (screen recordings of Android apps)
   * [ ] Source code
   * [ ] APK file
   * [ ] Crash logs / Stack traces

   _Reference:_ [Section 2.2, Figure 1, Page 2]

* **Input quality:**
   * Real-world screen recordings from multiple users on various devices/OS versions
   * Videos vary in length, display, and reproduction steps
   * No touch indicators — cannot see user taps
   * _Reference:_ [Section 5.2, Page 9; Section 1, Page 1]

* **Limitations of input:**
   * Different reproduction paths for the same bug → videos look visually different
   * Videos recorded at different speeds, with different intermediate screens
   * No textual bug report or step-by-step description required
   * _Reference:_ [Section 1, Page 1; Section 2.1, Page 1]

---

## 🧠 Role of LLM (if applicable)

* **Is LLM used?** → No
  _Reference:_ [Section 2.2, Page 2]

---

## 👁️ Vision Component (if applicable)

* **Is vision/image understanding used?** → Yes
  _Reference:_ [Section 2.3, Page 3]

* **Vision model:**
   * DINO (Vision Transformer, ViT) — self-supervised pre-trained on ImageNet; fine-tuned on Android GUI screenshots (RiCo dataset)
   * EAST (text detector) + TrOCR (OCR model) — for textual representation of frames
   * _Reference:_ [Sections 2.3, 2.4, Pages 3–5]

* **What visual information is extracted?**
   * UI element detection (ViT attention maps for semantic segmentation)
   * Layout/scene understanding (BoVW — Bag of Visual Words from DINO patches)
   * Text recognition from GUI screens (EAST + TrOCR)
   * Widget identification (implicit via ViT attention)
   * _Reference:_ [Sections 2.3, 2.4, Pages 3–5]

* **Integration with other components:**
   * Visual representations (JANUS_vis): frame patches → DINO → BoVW → TF-IDF vector per video → cosine similarity
   * Textual representations (JANUS_txt): frames → EAST (text detection) → TrOCR (text recognition) → BoW → TF-IDF vector → cosine similarity
   * Sequential component (JANUS_seq): LCS-based video alignment weighting later frames more heavily
   * Combined: weighted sum of visual + textual + sequential similarity scores
   * _Reference:_ [Figure 1, Sections 2.3–2.6, Pages 3–6]

---

## 🔁 System Design / Pipeline

**Describe full pipeline (step-by-step):**

1. **Input Processing (Video Sampling):**
   * Sample every 6th frame from both input videos
   * Resize frames to 224×224 pixels
   * _Reference:_ [Section 2.2, Page 2]

2. **Visual Representation (JANUS_vis):**
   * Feed frame patches into fine-tuned DINO ViT encoder
   * Encode each frame as BoVW vector (K=128 cluster Codebook from K-Means on RiCo dataset frames, 15k images)
   * Represent video as TF-IDF weighted BoVW vector
   * _Reference:_ [Section 2.3, Pages 3–4]

3. **Textual Representation (JANUS_txt):**
   * Apply EAST text detector to each frame → bounding boxes of text regions
   * Apply TrOCR to each text region → recognized text
   * Represent video as TF-IDF weighted BoW of text tokens
   * _Reference:_ [Section 2.4, Pages 4–5]

4. **Sequential Similarity (JANUS_seq):**
   * Compute modified LCS (Longest Common Subsequence) on frame-level representations
   * Weight later frames more heavily (buggy behavior appears later)
   * Apply to both visual (JANUS_seq-v) and textual (JANUS_seq-t) representations
   * _Reference:_ [Section 2.5, Page 5]

5. **Similarity Computation:**
   * Compute cosine similarity between video-level TF-IDF vectors (JANUS_vis, JANUS_txt)
   * Compute LCS-based similarity scores (JANUS_seq)
   * Combine linearly with weights: w = [0.8, 0.8, 0.8, 0.6, 1] for best configuration
   * _Reference:_ [Section 2.6, Page 6; Section 3.2, Table 3, Page 8]

6. **Ranking:**
   * Given a query video, rank corpus videos by combined similarity score
   * Higher score → more likely to be duplicate
   * _Reference:_ [Section 2.1, Page 2]

**Architecture diagram:**

```text
┌───────────────────────────────────────────────────────────────────┐
│                          INPUT                                    │
│     Video A (query)  +  Video B (candidate)  — screen recordings  │
└──────────────┬────────────────────────────────┬───────────────────┘
               │                                │
               ▼ (same pipeline for both)       │
┌──────────────────────────────┐                │
│  Frame Sampling              │◄───────────────┘
│  • Every 6th frame sampled   │
│  • Resized to 224×224 px     │
└──────────────┬───────────────┘
               │  Frame sequence
    ┌──────────┴──────────────────┐
    │                             │
    ▼                             ▼
┌───────────────────────┐  ┌───────────────────────────────────────┐
│  VISUAL BRANCH        │  │  TEXTUAL BRANCH                       │
│  (JANUS_vis)          │  │  (JANUS_txt)                          │
│                       │  │                                       │
│ • Fine-tuned DINO ViT │  │ • EAST text detector → bounding boxes │
│   encodes each frame  │  │ • TrOCR recognizes text per region    │
│   as patch embeddings │  │ • BoW (Bag of Words) per frame        │
│ • K-Means codebook    │  │ • TF-IDF weighted BoW per video       │
│   (K=128 clusters)    │  │                                       │
│ • BoVW + TF-IDF       │  └──────────────┬────────────────────────┘
│   vector per video    │                 │
└──────────┬────────────┘                 │
           │                             │
           ▼                             ▼
┌──────────────────────────────────────────────────────────────────┐
│  SEQUENTIAL BRANCH  (JANUS_seq)                                  │
│  • LCS (Longest Common Subsequence) on per-frame representations │
│  • Temporal weighting: later frames weighted higher              │
│    (buggy behavior appears toward end of video)                  │
│  • Applied to both visual (JANUS_seq-v) and textual (JANUS_seq-t)│
└──────────────────────────────┬───────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────────┐
│  SIMILARITY FUSION                                               │
│  • Cosine similarity between Video A and B vectors for each      │
│    branch: sim_vis, sim_txt, sim_seq-v, sim_seq-t                │
│  • Weighted linear combination:                                  │
│    score = 0.8·sim_vis + 0.8·sim_txt + 0.8·sim_seq-v            │
│           + 0.6·sim_seq-t + 1.0·(additional component)          │
└──────────────────────────────┬───────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────────┐
│  OUTPUT: Ranked list of candidate videos by duplicate likelihood │
│  Higher combined score → more likely to be a duplicate report    │
└──────────────────────────────────────────────────────────────────┘
```

_Reference:_ [Figure 1, Page 3]

**Key algorithms/techniques:**
* DINO ViT fine-tuned on RiCo Android GUI dataset
* BoVW + TF-IDF for both visual and textual video representation
* LCS-based sequential alignment with temporal weighting
* _Reference:_ [Sections 2.3–2.5, Pages 3–5]

**Novelty:**
* First approach combining visual (ViT-based), textual (OCR-based), and sequential (LCS-based) representations for video-based duplicate bug report detection
* Fine-tuning DINO on Android GUIs for GUI-specific scene understanding
* Sequential alignment accounting for temporal ordering of reproduction steps
* _Reference:_ [Abstract, Page 1; Section 7, Page 10]

---

## 🎬 Action Space & Execution

* **What actions can the system perform?**
   * N/A — this is a duplicate detection system, not a reproduction system

* **How are actions selected?** N/A

* **How are actions executed?** N/A

* **Handling dynamic/complex UIs:**
   * ViT attention mechanism handles varying layouts; textual component captures text-heavy screens
   * _Reference:_ [Section 4.5.1, Page 9]

---

## 🔍 Oracle / Bug Detection

* **How does the system know a bug is reproduced?**
   * N/A — system ranks videos by duplicate likelihood, not reproduction oracle

* **Duplicate detection metric:**
  * Mean Reciprocal Rank (mRR): rank of first true duplicate in ranked list
  * Mean Average Precision (mAP): precision across all true duplicates
  * _Reference:_ [Section 3.3, Page 7]

---

## 📊 Evaluation

### **Dataset:**

* **Name/Source:**
  * Original dataset: 7,290 duplicate detection tasks from 270 video-based bug reports across 90 Android apps (extended from prior TANGO dataset [Cooper et al.])
  * Extended dataset: 3k additional tasks with real bugs (not injected) on more diverse apps
  * _Reference:_ [Section 3.1, Pages 6–7]

* **Size:** 7,290 tasks (original) + extended set; 270 videos, 90 apps
  * _Reference:_ [Section 3.1, Page 7]

* **Bug types:** Crashes + functional/visual bugs (both injected and real)
  * _Reference:_ [Section 3.1, Page 7]

* **Real-world or synthetic?** Mix — injected bugs (original TANGO dataset) + real bugs (extended)
  * _Reference:_ [Section 3.1, Page 7]

* **Publicly available?** Yes (JANUS Replication Package on GitHub)
  * _Reference:_ [Section 3.1, Page 7]

### **Baselines:**

* **What is this paper compared against?**
  * TANGO (prior state-of-the-art video duplicate detector — contrastive learning + CNN)
  * SimCLR (contrastive learning baseline)
  * Individual JANUS components evaluated separately
  * _Reference:_ [Section 3.2, Page 7; Section 4.1, Table 2, Page 7]

* **Are baselines strong/recent?** Yes — TANGO was the state-of-the-art at time; published at ICSE 2021
  * _Reference:_ [Section 6.1, Page 10]

### **Metrics:**

* [x] **Mean Reciprocal Rank (mRR)**
* [x] **Mean Average Precision (mAP)**
* [ ] Reproduction rate
* [ ] Time metrics

_Reference:_ [Section 3.3, Page 7]

### **Results Summary:**

* **Main quantitative findings:**
  * Best JANUS configuration (Vis + Txt + Seq): 89.8% mRR, 84.7% mAP on original dataset
  * Outperforms prior work by >9% mRR (statistically significant, Wilcoxon p < 0.05)
  * On extended (real bug) dataset: similar improvements maintained
  * _Reference:_ [Abstract; Section 4.1, Tables 2–3, Pages 7–8]

* **Best performing configuration:** JANUS "Vis + Txt + Seq" with weights [0.8, 0.8, 0.8, 0.6, 1]
  * _Reference:_ [Section 3.2, Table 3, Page 8]

* **Ablation studies:**
  * JANUS_vis alone significantly outperforms SimCLR for most apps
  * JANUS_txt alone substantially outperforms JANUS_seq-t for 5/9 apps
  * Sequential component provides improvements for apps with diverse reproduction paths
  * _Reference:_ [Sections 4.2–4.3, Pages 8–9]

* **Statistical significance:** Wilcoxon test, p < 0.05 for all comparisons to prior work
  * _Reference:_ [Section 4.1, Page 7]

### **Qualitative Analysis:**

* **Case studies?** Yes — two detailed case studies (DroidWeight duplicate detection, GNUCash text localization)
  * _Reference:_ [Sections 4.5.1–4.5.2, Figures 2–3, Pages 9–10]

* **Failure analysis?** Implicit — JANUS_vis handles visual patterns; JANUS_txt handles text; neither alone is sufficient
  * _Reference:_ [Section 4.2, Page 8]

* **What types of bugs does it handle well/poorly?**
  * Well: bugs with distinctive visual patterns (different UI layouts, distinctive text)
  * Poorly: bugs where visual content is nearly identical between different bugs (e.g., same screen but different underlying state)
  * _Reference:_ [Section 4.5, Pages 9–10]

---

## 💪 Strengths

* **What does this approach do really well?**
  * Rich multi-modal representation (visual + textual + sequential) captures complementary information
  * ViT-based GUI understanding significantly outperforms CNN-based approaches (ResNet-50)
  * Works on real-world diverse videos recorded by multiple users on different devices
  * _Reference:_ [Section 4, Pages 7–10; Abstract]

* **What's the biggest contribution?**
  * Demonstrates that GUI-specific vision Transformer (DINO fine-tuned on Android GUIs) substantially outperforms general-purpose visual features for video bug report duplicate detection
  * _Reference:_ [Abstract; Section 7, Page 10]

---

## ⚠️ Limitations / Weaknesses

### **Technical:**
* Duplicate detection only — does not reproduce bugs, only identifies duplicates
  * _Reference:_ [Abstract, Page 1]
* Relies on fixed frame sampling rate — may miss brief but important UI states
  * _Reference:_ [Section 2.2, Page 2]
* EAST OCR fails on low-brightness, low-contrast regions
  * _Reference:_ [Section 4.5.2, Figure 3, Page 10]

### **Experimental:**
* Original dataset uses injected bugs — may not fully represent real-world bug diversity
  * _Reference:_ [Section 5.1, Page 9]
* Android-only evaluation — no iOS or other platforms
  * _Reference:_ [Section 5.2, Page 9]

### **Practical:**
* Computationally expensive to run DINO + OCR on every video frame
* Codebook construction requires RiCo dataset (15k images) — not trivial to adapt to new domains
  * _Reference:_ [Section 2.3, Page 4]

### **Threats to Validity:**
* Internal: JANUS implementation choices (Codebook size K=128, threshold 40×40, warm-up teacher epochs 4) — hyperparameter sensitivity
* External: single platform (Android); may not generalize to iOS or other app categories
* _Reference:_ [Section 5, Pages 9–10]

---

## 🔮 Future Work / Open Questions

* **What do the authors suggest as next steps?**
  * Exploring different app languages (non-English apps)
  * Extending to iOS or other mobile platforms
  * Combining JANUS with textual bug report information when available
  * _Reference:_ [Section 5.2, Page 9]

* **What's still unsolved?**
  * Videos with nearly identical visual content but different underlying bugs
  * Handling videos without clear visual bug manifestation
  * _Reference:_ [Section 4.5, Pages 9–10]

---

## 💡 Key Takeaways

* **One-line summary:** JANUS detects duplicate video-based bug reports by combining GUI-specific ViT visual features, OCR-based text features, and LCS-based sequential alignment of video frames.

* **Most interesting insight:**
  * ViT (DINO) dramatically outperforms ResNet-50 for GUI understanding — traditional CV models designed for natural images miss the structured, component-based nature of GUIs
  * _Reference:_ [Section 4.5.1, Figure 2, Page 9]

* **Relevance to my work:** Shows that vision models specifically adapted to GUI screenshots (ViT + RiCo fine-tuning) are critical for understanding Android app behavior from video; directly relevant for video-based bug reproduction pipelines.

* **Ideas to borrow/adapt:**
  * DINO ViT fine-tuned on RiCo for GUI frame understanding
  * TF-IDF weighting for aggregating frame-level features into video-level representation
  * Sequential LCS alignment for handling variable-length reproduction sequences
  * Temporal weighting (later frames = buggy behavior) for video analysis

---

## 📎 Related Work

* **Prior work this builds on:**
  * TANGO [Cooper et al., 2021] — prior video duplicate detector using contrastive learning
  * DINO [Caron et al., 2021] — self-supervised ViT training
  * _Reference:_ [Section 6, Pages 10–11]

* **Key citations to follow up:**
  * [Cooper et al., 2021] TANGO — direct predecessor on duplicate video detection
  * [Yan et al., 2023] — duplicate bug report detection combining visual and textual
  * [RiCo dataset] — Android GUI screenshot corpus used for fine-tuning

---

## 🔬 Reproducibility

* **Enough detail to reimplement?** Partial (architecture described; some hyperparameters given; Codebook training details provided)

* **Hyperparameters provided?**
  * K=128 clusters; frame resize 224×224; EAST threshold 40×40; warm-up teacher epochs 4; combination weights [0.8, 0.8, 0.8, 0.6, 1]
  * _Reference:_ [Sections 2.3, 3.2, Pages 4, 7]

* **Computational resources mentioned?**
  * Three NVIDIA T4 Tesla GPUs with 16GB memory each; model training details for DINO
  * _Reference:_ [Section 3.2, Page 7]

* **Random seed / initialization:** Not specified; Codebook constructed by randomly sampling 15k RiCo images

---

## 🏷️ Tags

`#Vision` `#ViT` `#DINO` `#OCR` `#VideoAnalysis` `#DuplicateDetection` `#GUI-Testing` `#Android` `#BugReporting` `#TF-IDF` `#SequentialAlignment`

---

## 📝 Notes / Comments

* Personal observations: JANUS is the only paper in this set focused on **duplicate detection** rather than bug **reproduction**. It's the vision-pioneer in the group. Key insight: ViT >> CNN for GUI understanding.
* Questions to ask: Could JANUS's video representations be used to extract reproduction steps (not just detect duplicates)? The LCS alignment implicitly finds the "common path" between two videos.
* Connection to other papers: JANUS's video processing pipeline (frame sampling → ViT → BoVW) is conceptually adjacent to what a video-based reproduction system (ViBR, GIFdroid) would need for understanding bug video content.

---

**Template Version:** 1.0
**Last Updated:** 2026-04-10
