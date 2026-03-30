# HHV Keyframe Fix Comparison — AdAway utg02

**Video:** `app_AdAway/utg02/input/handheld/hhv_app_AdAway.mp4`
**Total frames:** 1331 (1330 frame pairs)
**UTG:** 4 vertices, 5 edges
**Artifacts:** 4 screenshots

---

## Fix Definitions

### Baseline
The original GIFdroid algorithm. Decodes all frames, computes pairwise SSIM on luma (grayscale) channels sequentially, and marks a frame as a keyframe when the SSIM to the next frame drops below a stable threshold (default 2). No compensation for camera shake — any physical movement of the handheld device that reduces SSIM will be detected as a "transition" and produce a spurious keyframe.

**Why this is the problem:** Handheld video introduces involuntary camera movement (shake, tilt, pan) between frames. Even when the UI screen hasn't changed, these micro-movements lower the SSIM score enough to cross the detection threshold, generating many false-positive keyframes.

---

### Fix 1 — Video Stabilization (`stabilize`)
**Approach:** Two-pass FFmpeg stabilization applied to the entire video _before_ SSIM is computed.
- Pass 1: `vidstabdetect` analyses motion and writes a transform file (`.trf`).
- Pass 2: `vidstabtransform` warps each frame to cancel detected motion, producing a stabilized `.mp4`.
- The baseline algorithm then runs unchanged on the stabilized video.

**Why this fix:** If camera motion is removed at the pixel level before SSIM is measured, the similarity scores between stable-screen frames should stay high and not cross the keyframe threshold. This is a pre-processing approach — the core detector is unmodified.

---

### Fix 2 — Temporal Hysteresis (`hysteresis`)
**Approach:** Instead of declaring a keyframe on a single-frame SSIM dip, a frame is only accepted as stable if the next `k=3` consecutive frames also all have SSIM > 0.95.
- Camera shake causes short-lived dips (1–2 frames) that recover quickly.
- Genuine screen transitions keep SSIM low for many frames.
- The stable run-length requirement filters out transient shake-induced dips.

**Why this fix:** The problem with the baseline is that it reacts to instantaneous SSIM values. By requiring sustained stability, we separate real transitions (sustained low SSIM) from shake artefacts (brief dip, then recovery).

---

### Fix 3 — Homography-corrected SSIM (`homography`)
**Approach:** For each consecutive frame pair, SIFT keypoints are extracted and matched. A homography (projective transformation) is estimated via RANSAC from the matches. The second frame is warped onto the first using this homography before SSIM is computed.
- If < 4 good matches are found (blurry/featureless frame), raw SSIM is used as fallback.
- The detector (`detect_keyframes`) then runs on the homography-corrected similarity sequence.

**Why this fix:** Camera pan/tilt/zoom changes the apparent pixel positions of UI elements. Estimating and correcting for this geometric transformation means SSIM compares the same content at the same position, giving an accurate measure of _content_ change rather than _camera_ change.

---

### Fix 4 — CLIP Clustering (`clip`)
**Approach:** Runs the baseline detector first to get candidate keyframes, then encodes each candidate with a CLIP vision model (`openai/clip-vit-base-patch32`). Agglomerative clustering groups visually similar frames by cosine similarity in the CLIP embedding space. Only the medoid of each cluster is kept.

**Why this fix:** Even if the baseline over-detects, semantically identical screens (same UI state, slightly different camera angle) will cluster tightly in CLIP space. Post-hoc deduplication removes these without touching the detection algorithm.

---

### Fix 5 — VLM Pair Classification (`vlm`)
**Approach:** Runs the baseline detector first, then uses a local vision-language model (Llama 3.2-Vision via Ollama) to classify each consecutive keyframe pair: `SAME` or `DIFFERENT` UI screen. Pairs classified as `SAME` are dropped (the earlier frame is kept).

**Why this fix:** A VLM can reason at a semantic/UI level — it understands that two frames show "the same settings screen" despite camera angle differences, without needing to tune thresholds or rely on pixel-level similarity. Requires no new algorithm design, just a sufficiently capable local model.

---

## Log Comparison

| Method | Keyframes Detected | Keyframe Indices | Total Time | Step 1 Time | Step 2 (Mapping) Time | Mapped Sequence | Trace Found |
|---|---|---|---|---|---|---|---|
| **baseline** | 39 | [11, 20, 74, 149, 169, 231, 245, 366, 421, 428, 454, 527, 550, 608, 626, 643, 677, 683, 714, 745, 764, 792, 802, 812, 819, 857, 880, 943, 1016, 1097, 1126, 1161, 1173, 1187, 1221, 1227, 1262, 1270, 1330] | 163.97s | ~143s | 17.63s | All 2 | [0,1,2] |
| **hysteresis** | 44 | [10, 19, 27, 73, 148, 168, 230, 244, 365, 420, 427, 453, 526, 549, 607, 625, 635, 642, 676, 682, 713, 717, 744, 763, 791, 801, 811, 818, 825, 833, 856, 879, 942, 1015, 1096, 1125, 1160, 1172, 1186, 1220, 1226, 1261, 1269, 1330] | 186.03s | ~160s | 21.65s | All 2 | [0,1,2] |
| **stabilize** | 24 | [20, 74, 168, 231, 245, 366, 454, 608, 617, 629, 718, 794, 834, 880, 942, 1003, 1014, 1096, 1128, 1161, 1173, 1227, 1271, 1330] | 305.29s | ~293s (incl. FFmpeg) | 11.07s | All 2 | [0,1,2] |
| **homography** | 20 | [21, 74, 161, 231, 245, 366, 453, 834, 943, 968, 1010, 1015, 1039, 1097, 1133, 1161, 1174, 1226, 1271, 1330] | 746.25s | ~733s | 10.84s | All 2 | [0,1,2] |
| **clip** | 39 *(fallback)* | same as baseline | 173.99s | ~153s | 17.40s | All 2 | [0,1,2] |
| **vlm** | 39 *(fallback)* | same as baseline | 170.71s | ~150s | 17.95s | All 2 | [0,1,2] |

---

## Observations

### 1. Baseline over-detects, producing 39 keyframes
The baseline detected 39 keyframes from 1331 frames. Given that AdAway utg02 has only 4 UTG screens and a 3-step trace `[0→1→2]`, most of the 39 are false positives caused by handheld camera shake. The mapping step correctly collapsed all 39 into screen 2, showing that the keyframes are all from the same or closely-related UI state.

### 2. Hysteresis made things worse (44 keyframes)
Counter-intuitively, hysteresis with k=3 produced _more_ keyframes (44 vs 39 baseline). The off-by-one indexing in the hysteresis implementation (detected indices are ~1 earlier than baseline: e.g., 10 vs 11, 19 vs 20) suggests the groupby logic scans slightly differently. The higher count indicates the hysteresis condition is too loose for this video — brief stable runs interrupted by shake are still triggering multiple keyframe boundaries that the baseline was merging.

### 3. Stabilization cut keyframes nearly in half (24 keyframes)
FFmpeg stabilization removed the majority of shake-induced false positives, reducing to 24 keyframes. The indices are noticeably different from baseline (e.g., frames 617, 629, 718, 794 appear that baseline missed, while many baseline detections in the 400–850 range disappear). The stabilized video apparently reveals some transitions that were hidden by shake and suppresses others. Cost: ~2× wall time (305s vs 164s) due to two FFmpeg passes.

### 4. Homography achieved the fewest keyframes (20), but is extremely slow
Homography-corrected SSIM produced the most aggressive reduction to 20 keyframes — almost half of stabilize's count. The SIFT+RANSAC per-frame-pair computation took ~733s for 1330 pairs (~0.55s/pair), making it ~4.5× slower than baseline. The different index set (e.g., 161, 834, 943, 968, 1010, 1015, 1039 are new; many baseline indices vanish) shows the geometric correction is genuinely changing which frames are detected as transitions.

### 5. CLIP and VLM both fell back to baseline
- **CLIP:** `transformers` package not installed → graceful fallback to baseline. No deduplication was performed.
- **VLM:** `ollama` package not installed → graceful fallback to baseline. No pair filtering was performed.

Both produced identical results to baseline (39 keyframes, same indices, same mapping). Their fallback paths worked correctly with a warning.
These methods cannot be evaluated until their dependencies are installed.

### 6. GUI mapping is identical across all methods — all map to screen 2
Every method mapped 100% of its keyframes to `artifacts_2.png` (screen index 2), and the execution trace `[0, 1, 2]` was found in all cases. The mapping scores are uniformly low (0.25–0.35), suggesting the HHV frames are visually quite different from the UTG artifact screenshots — likely due to the handheld camera angle, lighting, and scale differences. This is a separate problem: the keyframe method affects _how many_ keyframes reach the mapper, but the mapper itself struggles to differentiate between screens in HHV video.

### 7. Fewer keyframes = faster mapping
The mapping step scales linearly with keyframe count:
- 39 keyframes → ~17–18s
- 44 keyframes → ~21s
- 24 keyframes → ~11s
- 20 keyframes → ~10s

Methods that reduce keyframe count provide a secondary speed benefit in mapping.

---

## Summary Table

| Method | Keyframes | Reduction vs Baseline | Total Time | Dependencies Met | Recommended |
|---|---|---|---|---|---|
| baseline | 39 | — | 164s | Yes | Reference only |
| hysteresis | 44 | **+13% worse** | 186s | Yes | No — increases count |
| stabilize | 24 | **−38%** | 305s | Yes (FFmpeg) | Promising |
| homography | 20 | **−49%** | 746s | Yes (OpenCV/SIFT) | Only if accuracy critical |
| clip | 39 (fallback) | 0% | 174s | **No** (`transformers` missing) | Install deps first |
| vlm | 39 (fallback) | 0% | 171s | **No** (`ollama` missing) | Install deps first |

---

## Key Open Questions

1. **Why does every keyframe map to screen 2?** The mapping scores (0.25–0.35) are very low. The HHV video may be dominated by a single screen state, or the SSIM-based matcher is degraded by the handheld perspective. This needs investigation independent of the keyframe method.
2. **Hysteresis k=3 needs tuning.** A larger k or a different stable threshold might bring hysteresis below baseline.
3. **CLIP and VLM need to be installed and re-run** to get meaningful results.
4. **Homography accuracy vs speed tradeoff** — 746s is impractical for interactive use. GPU SIFT or approximate matching could help.