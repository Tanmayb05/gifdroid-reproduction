# GIFdroid HHV Improvement Research

## Root Cause Summary

From the data:
- **Step 1 (location.py)**: Uses hardcoded SSIM threshold `0.95` with ±2-frame window. Camera shake in HHV drops SSIM to 0.85-0.93 even on a *stable* screen → fires constantly → 5-18x over-detection
- **Step 2 (mapping.py)**: Lowe's ratio test is `0.4` (extremely strict — tuned for clean SRV). On blurry HHV frames, almost no ORB matches pass → ORB term ≈ 0 for all candidates → score reduces to pure SSIM → all blurry frames cluster at ~0.28-0.32 → mapping collapses to 1 screen

---

## Step 1: Better Keyframe Detection

### Non-LLM Approaches

| Approach | What It Does | Why It Helps | Complexity |
|---|---|---|---|
| **Temporal Median Frame SSIM** | Compare each frame to pixel-wise median of ±W/2 neighbors instead of the prior frame | Median suppresses hand-shake noise (zero-mean); real UI transitions shift the median itself | Easy — pure NumPy |
| **Adaptive Threshold + Min Spacing** | Set threshold at `percentile(sim, 85) - 0.02`; reject keyframes within 20 frames of each other | Calibrates to HHV's noise floor rather than SRV's clean 0.97-0.99 range; kills tight false-keyframe clusters | Easy — 5-line change |
| **Farneback Optical Flow Gate** | Only emit keyframe if SSIM drops AND median optical flow displacement < 3px | Directly separates camera motion (large coherent flow) from UI transitions (no coherent flow or non-rigid change) | Medium — slower (~3-5x) but in OpenCV |
| **PySceneDetect AdaptiveDetector** | Drop-in HSV histogram-based scene change detector with floating threshold | Self-tunes to video noise floor; `min_scene_len=15` blocks tight false clusters | Easy — 1 pip install |
| **Center-Crop + Homography Alignment** | SSIM only on central 60% of frame; align consecutive crops via ORB homography before comparing | Center has least perspective distortion; homography removes translational camera motion | Medium |

**Top 3 Non-LLM for Step 1:**
1. **Temporal Median Frame** — highest impact, zero new deps
2. **Adaptive Threshold + Min Spacing** — 5-line safety net, always worthwhile
3. **Farneback Optical Flow Gate** — most principled camera vs. content separation

### LLM Approaches

| Approach | What It Does | Complexity |
|---|---|---|
| **CLIP Cosine Similarity** | Replace SSIM signal with CLIP ViT-B/32 cosine similarity — robust to viewpoint/lighting variation | Medium — needs `torch` + GPU for speed |
| **Fine-Tuned ViT/MobileNet Change Detector** | Binary classifier trained on SRV-labeled frame pairs, applied to HHV | Hard — needs training data + GPU |
| **Video Swin Transformer** | Temporal model, sees full clip context around boundaries | Hard — overkill for this task |

**Top 3 LLM for Step 1:**
1. **CLIP Cosine Similarity** — best zero-shot option, no training required
2. **Fine-Tuned ViT/MobileNet** — highest ceiling but needs training infrastructure
3. **Video Swin Transformer** — most powerful, not recommended near-term

---

## Step 2: Better GUI Mapping

### Non-LLM Approaches

| Approach | What It Does | Why It Helps | Complexity |
|---|---|---|---|
| **CLAHE Normalization** | Apply `cv2.createCLAHE(clipLimit=2.0)` before SSIM on both keyframe and artifact | HHV frames are under/over-exposed vs. clean screenshots; CLAHE brings both to comparable intensity range | Easy — 1 line in `load_screenshots()` + `mapping()` |
| **AKAZE + Ratio 0.75 + RANSAC** | Replace ORB with AKAZE (blur-robust); change Lowe's ratio from `0.4` → `0.75`; add RANSAC homography inlier count | The `0.4` ratio is the single biggest bug — almost no HHV matches pass. AKAZE's normalized gradient is more stable under blur | Easy — 1-2 line changes |
| **OCR Text Matching** | OCR keyframe + artifacts with Tesseract; Jaccard similarity of word sets as a scoring component | UI text (button labels, titles, list items) is viewpoint-invariant. Tab names in WifiAnalyzer, note titles in SimpleNotes are uniquely discriminating | Medium — `pytesseract` + upscale 2x before OCR |
| **Rank Score Normalization** | `norm_score[k] = score[k] - median(all_scores)` | Stretches compressed 0.23-0.33 range; amplifies existing ranking signal | Easy — 3-line change (bandage, not cure) |
| **Structural pHash** | 64-bit DCT hash; Hamming distance as coarse layout filter | Blur-invariant at coarse scale; rules out clearly wrong candidate screens | Easy — `pip install imagehash` |

**Top 3 Non-LLM for Step 2:**
1. **CLAHE Normalization** — immediate fix for SSIM floor compression, 2-minute implementation
2. **AKAZE + Ratio 0.75 + RANSAC** — Lowe's ratio `0.4` is almost certainly the root cause of ORB ≈ 0 on all HHV; changing to `0.75` is a 1-line fix
3. **OCR Text Matching** — highest ceiling for text-heavy apps; UI text uniquely identifies screens

### LLM Approaches

| Approach | What It Does | Complexity |
|---|---|---|
| **CLIP Embedding Similarity** | Cosine similarity in CLIP embedding space; robust to blur/viewpoint; expected spread 0.10-0.25 vs. current 0.02-0.08 | Medium — needs torch, ~0.5s/image on CPU |
| **ResNet/EfficientNet CNN Features** | Penultimate-layer features from pretrained ImageNet CNN | Medium — faster than CLIP but less semantically rich |
| **UIBert / Screen2Words** | Android-specific UI embedding model (Google Research) | Hard — research model, needs accessibility XML, not pip-installable |

**Top 3 LLM for Step 2:**
1. **CLIP Embedding Similarity** — best zero-shot option, highest robustness to HHV degradation
2. **ResNet/EfficientNet CNN Features** — faster than CLIP, potentially sufficient
3. **UIBert / Screen2Words** — best theoretical fit, practically hardest; future work

---

## Both Steps Simultaneously

### FFmpeg vidstab Pre-Stabilization

The single highest-leverage intervention. Add to `src_gifdroid/prerequisites.py` `convert_handheld()`:

```bash
# Pass 1: analyze motion
ffmpeg -i hhv.mp4 -vf vidstabdetect=shakiness=10:accuracy=15 -f null -

# Pass 2: stabilize
ffmpeg -i hhv.mp4 -vf vidstabtransform=smoothing=30 -c:v libx264 hhv_stabilized.mp4
```

After stabilization:
- **Step 1**: Consecutive SSIM on the same screen behaves like SRV → original `0.95` threshold works
- **Step 2**: Keyframes match artifacts with higher SSIM and better ORB matches

Uses FFmpeg already in the project, zero new Python dependencies.

### CLIP Unified Pipeline

Compute CLIP embeddings for all video frames once. Use cosine similarity sequence for Step 1 keyframe detection AND as Step 2 mapping scores against artifact embeddings. Single embedding pass unifies both steps. Requires GPU for practical speed.

---

## Priority Matrix

| Rank | Step | Approach | Complexity | Expected Impact |
|---|---|---|---|---|
| 1 | Both | FFmpeg vidstab pre-stabilization | Easy | Very High |
| 2 | Step 2 | CLAHE normalization | Easy | High |
| 3 | Step 2 | Lowe's ratio `0.4` → `0.75` (1-line fix) | Easy | High |
| 4 | Step 1 | Adaptive threshold + min spacing | Easy | High |
| 5 | Step 1 | Temporal median frame SSIM | Easy | High |
| 6 | Step 2 | AKAZE + RANSAC | Easy-Medium | High |
| 7 | Step 2 | OCR text matching | Medium | High (text-heavy apps) |
| 8 | Step 1 | Farneback optical flow gate | Medium | Medium-High |
| 9 | Both | CLIP embeddings | Medium (needs GPU) | High |

**Items 1–6 require zero new Python dependencies and ~2 hours of implementation.**