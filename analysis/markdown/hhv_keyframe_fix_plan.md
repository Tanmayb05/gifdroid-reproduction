# HHV Keyframe Over-Detection: Fix Plan

**Problem:** GIFdroid's SSIM threshold (0.95) designed for pixel-stable ADB recordings fires on camera motion, producing 5–18× more keyframes than SRV for the same session.

---

## Architecture

Each fix is a standalone function in a new file `gifdroid/hhv_keyframe.py` with identical signature to `keyframe_location()` in `location.py`:

```python
def keyframe_location_<method>(video, stable_threshold=2, visualize=False, **kwargs)
    -> (keyframes: list, keyframes_index: list)
```

`main.py` gets one new arg `--keyframe-method` to select which function runs. Keyframes are saved to `output/keyframes_<method>/` automatically.

### Output folder layout per run

```
app_AdAway/utg01/output/
  execution_hhv_AdAway_baseline.json
  execution_hhv_AdAway_fix1.json
  execution_hhv_AdAway_fix2.json
  execution_hhv_AdAway_fix3.json
  execution_hhv_AdAway_fix4.json
  execution_hhv_AdAway_fix5.json
  keyframes_baseline/
  keyframes_stabilize/
  keyframes_hysteresis/
  keyframes_homography/
  keyframes_clip/
  keyframes_vlm/
```

---

## Fix 1 — Video Stabilization (FFmpeg)

**Function:** `keyframe_location_stabilized(video, stable_threshold=2, visualize=False)`

**Steps:**
1. Create temp file path `<video>_stabilized.mp4`
2. Two-pass FFmpeg stabilization:
   - Pass 1: `ffmpeg -i video -vf vidstabdetect=shakiness=5:accuracy=15 -f null -` (writes `transforms.trf`)
   - Pass 2: `ffmpeg -i video -vf vidstabtransform=smoothing=10:input=transforms.trf stabilized.mp4`
3. Call existing `keyframe_location(stabilized_video)` from `location.py` — zero logic change
4. Delete temp files, return result

**New deps:** `ffmpeg` with `libvidstab` (`brew install ffmpeg`)

---

## Fix 2 — Temporal Hysteresis

**Function:** `keyframe_location_hysteresis(video, stable_threshold=2, hysteresis_k=3, visualize=False)`

**Steps:**
1. Call `read_frames_from_video()` and `calculate_sim_seq()` from `location.py` — unchanged
2. Replace `is_stable()` with hysteresis version — require `hysteresis_k` *forward-consecutive* frames all above 0.95:
   ```
   stable[i] = True  iff  sim[i], sim[i+1], ..., sim[i+k-1]  all > 0.95
   ```
   Camera shake dips recover in 1 frame; real transitions stay low for many frames.
3. Feed the new stable list into `detect_keyframes()` logic (same groupby pass from `location.py:83`)

**New deps:** None.

---

## Fix 3 — Homography-corrected SSIM

**Function:** `keyframe_location_homography(video, stable_threshold=2, visualize=False)`

**Steps:**
1. `read_frames_from_video()` as usual (reuse luma frames)
2. For each consecutive luma frame pair `(y_i, y_{i+1})`:
   - Detect SIFT keypoints: `cv2.SIFT_create().detectAndCompute()`
   - Match with BFMatcher + Lowe's ratio 0.75
   - If ≥4 matches: estimate homography `H` via `cv2.findHomography(..., cv2.RANSAC)`
   - Warp `y_{i+1}` onto `y_i` frame: `cv2.warpPerspective(y_{i+1}, H, size)`
   - Compute SSIM on `(y_i, warped_{i+1})` pair
   - If <4 matches (too blurry): fall back to raw SSIM
3. Feed corrected `sim_list` into `detect_keyframes()` unchanged

**New deps:** SIFT already available via `opencv-contrib-python==3.4.2.16` in the venv.

---

## Fix 4 — Post-hoc CLIP Clustering

**Function:** `keyframe_location_clip_cluster(video, stable_threshold=2, cluster_threshold=0.85, visualize=False)`

**Steps:**
1. Run `keyframe_location()` (baseline) to get initial inflated keyframe set
2. Encode each keyframe with CLIP `openai/clip-vit-base-patch32` via `transformers`:
   ```python
   features = clip_model.get_image_features(processor(images=frames, return_tensors="pt").pixel_values)
   ```
3. Compute cosine similarity matrix between all keyframe embeddings
4. Agglomerative clustering (`sklearn.cluster.AgglomerativeClustering`) with `distance_threshold = 1 - cluster_threshold`
5. From each cluster, keep the **medoid** (frame with highest mean similarity to other cluster members)
6. Return deduplicated `(keyframes, keyframes_index)` preserving original ordering

**New deps:** `transformers`, `torch`

---

## Fix 5 — VLM Pair Classification (Llama 3.2-Vision via Ollama)

**Model choice:** Llama 3.2-Vision (11B or 90B) — first Llama model with native multimodal support. Llama 3.1 is text-only and cannot process image frames. Run locally via Ollama, no API key needed.

**Function:** `keyframe_location_vlm(video, stable_threshold=2, model="llama3.2-vision", visualize=False)`

**Steps:**
1. Run `keyframe_location()` (baseline) to get initial candidate keyframes
2. For each consecutive pair `(k_i, k_{i+1})`:
   - Encode both frames as base64 JPEG strings
   - POST to Ollama local API (`http://localhost:11434/api/chat`) with both images and prompt:
     *"These are two frames from an Android screen recording. Do they show the SAME UI screen or DIFFERENT UI screens? Reply with only: SAME or DIFFERENT"*
   - If response is `SAME`: drop `k_{i+1}`
3. Return filtered `(keyframes, keyframes_index)`

**New deps:** `pip install ollama` + `ollama pull llama3.2-vision` (one-time ~7GB download)

---

## Changes to `main.py`

**1. New argument in `parse_args()`:**
```python
parser.add_argument('--keyframe-method',
                    choices=['baseline', 'stabilize', 'hysteresis', 'homography', 'clip', 'vlm'],
                    default='baseline',
                    help='Keyframe detection method (default: baseline)')
```

**2. Replace line 156** (`keyframe_sequence, keyframe_index = keyframe_location(video)`) with:
```python
from gifdroid.hhv_keyframe import get_keyframe_fn
keyframe_fn = get_keyframe_fn(args.keyframe_method)
keyframe_sequence, keyframe_index = keyframe_fn(video)
```

**3. Keyframes dir uses method name:**
```python
keyframes_dir = os.path.join(out_dir, f"keyframes_{args.keyframe_method}")
```

---

## Example Commands (AdAway, utg01, HHV)

```bash
# Baseline (unchanged)
python -m gifdroid.main \
  --video app_AdAway/utg01/input/handheld/hhv_app_AdAway.mp4 \
  --utg   app_AdAway/utg01/input/utg.json \
  --artifact app_AdAway/utg01/input/artifacts \
  --out   app_AdAway/utg01/output/execution_hhv_AdAway_baseline.json \
  --keyframe-method baseline

# Fix 1 — Video Stabilization
python -m gifdroid.main \
  --video app_AdAway/utg01/input/handheld/hhv_app_AdAway.mp4 \
  --utg   app_AdAway/utg01/input/utg.json \
  --artifact app_AdAway/utg01/input/artifacts \
  --out   app_AdAway/utg01/output/execution_hhv_AdAway_fix1.json \
  --keyframe-method stabilize

# Fix 2 — Hysteresis
python -m gifdroid.main \
  --video app_AdAway/utg01/input/handheld/hhv_app_AdAway.mp4 \
  --utg   app_AdAway/utg01/input/utg.json \
  --artifact app_AdAway/utg01/input/artifacts \
  --out   app_AdAway/utg01/output/execution_hhv_AdAway_fix2.json \
  --keyframe-method hysteresis

# Fix 3 — Homography
python -m gifdroid.main \
  --video app_AdAway/utg01/input/handheld/hhv_app_AdAway.mp4 \
  --utg   app_AdAway/utg01/input/utg.json \
  --artifact app_AdAway/utg01/input/artifacts \
  --out   app_AdAway/utg01/output/execution_hhv_AdAway_fix3.json \
  --keyframe-method homography

# Fix 4 — CLIP clustering
python -m gifdroid.main \
  --video app_AdAway/utg01/input/handheld/hhv_app_AdAway.mp4 \
  --utg   app_AdAway/utg01/input/utg.json \
  --artifact app_AdAway/utg01/input/artifacts \
  --out   app_AdAway/utg01/output/execution_hhv_AdAway_fix4.json \
  --keyframe-method clip

# Fix 5 — VLM (requires: ollama serve + ollama pull llama3.2-vision)
python -m gifdroid.main \
  --video app_AdAway/utg01/input/handheld/hhv_app_AdAway.mp4 \
  --utg   app_AdAway/utg01/input/utg.json \
  --artifact app_AdAway/utg01/input/artifacts \
  --out   app_AdAway/utg01/output/execution_hhv_AdAway_fix5.json \
  --keyframe-method vlm
```

---

## Validation Steps

**1. Visual inspection**
Open `output/keyframes_<method>/` — should show ~3–5 distinct screens for AdAway HHV, not 39 near-identical frames.

**2. Metric extraction**
Run `analyze_gifdroid.py --extract` pointing at new log files, produce one `gifdroid_data_<method>.json` per fix.

**3. Comparison table** (target: HHV ≈ SRV)

| Metric | SRV baseline | HHV baseline | Fix1 | Fix2 | Fix3 | Fix4 | Fix5 |
|---|---|---|---|---|---|---|---|
| Avg keyframes | 8.0 | 25.5 | ? | ? | ? | ? | ? |
| Avg unique screens | 4.42 | 1.15 | ? | ? | ? | ? | ? |
| Avg score spread | 0.35 | 0.07 | ? | ? | ? | ? | ? |
| Avg LCS | 2.32 | 1.07 | ? | ? | ? | ? | ? |
| Avg time (s) | 218 | 1922 | ? | ? | ? | ? | ? |

**Pass criteria per run:** keyframes ≤ SRV×2, unique screens ≥ 2, spread ≥ 0.15.

**4. Pathological case test**
Run Fix 1 + Fix 2 on AntennaPod utg03 HHV — must complete in <600s (vs 27,517s baseline).

**5. SRV regression check**
Run all 5 fixes on SRV inputs — keyframe counts should not change significantly (fixes should be neutral on clean video).

---

## Implementation Phases

### Phase 1 — Core infrastructure (no new deps) ✅

**Files:** `gifdroid/hhv_keyframe.py` (new), `gifdroid/main.py`

**Tasks:**

1. Create `gifdroid/hhv_keyframe.py` with:
   - `keyframe_location_hysteresis(video, stable_threshold=2, hysteresis_k=3, visualize=False)` — replace `is_stable()` with a forward-k consecutive check; reuse `read_frames_from_video`, `calculate_sim_seq`, `detect_keyframes` from `location.py`
   - `get_keyframe_fn(method)` dispatcher — returns the right function for `'baseline' | 'stabilize' | 'hysteresis' | 'homography' | 'clip' | 'vlm'`; raises `ValueError` for unknown methods

2. Modify `gifdroid/main.py`:
   - Add `--keyframe-method` arg to `parse_args()` (choices + default=`'baseline'`)
   - Replace line 156 (`keyframe_location(video)`) with `get_keyframe_fn(args.keyframe_method)(video)`
   - Change `keyframes_dir` to use `keyframes_{method}` subfolder name instead of `keyframes`
   - Log the active method at startup

**Deps:** None

---

### Phase 2 — Fix 1: Video Stabilization (FFmpeg) ✅

**Files:** `gifdroid/hhv_keyframe.py`

**Tasks:**

1. Add `keyframe_location_stabilized(video, stable_threshold=2, visualize=False)`:
   - Build temp path `<video_stem>_stabilized.mp4` in the same dir
   - Run 2-pass ffmpeg via `subprocess.run`: pass 1 `vidstabdetect`, pass 2 `vidstabtransform`
   - Call `keyframe_location(stabilized_video, stable_threshold, visualize)` unchanged
   - Clean up `_stabilized.mp4` and `transforms.trf` in a `finally` block
2. Register `'stabilize'` in `get_keyframe_fn`

**Deps:** `ffmpeg` with `libvidstab` (`brew install ffmpeg`)

---

### Phase 3 — Fix 3: Homography-corrected SSIM ✅

**Files:** `gifdroid/hhv_keyframe.py`

**Tasks:**

1. Add `keyframe_location_homography(video, stable_threshold=2, visualize=False)`:
   - Decode frames with `read_frames_from_video`
   - For each consecutive luma pair: detect SIFT keypoints, BFMatcher + Lowe ratio 0.75, if ≥4 matches compute homography `H` via RANSAC, warp `y_{i+1}` onto `y_i`, compute SSIM on warped pair; else fall back to raw SSIM
   - Feed corrected `sim_list` to `detect_keyframes`
2. Register `'homography'` in `get_keyframe_fn`

**Deps:** `opencv-contrib-python==3.4.2.16` (already in venv — SIFT available)

---

### Phase 4 — Fix 4: CLIP Clustering

**Files:** `gifdroid/hhv_keyframe.py`

**Tasks:**

1. Add `keyframe_location_clip_cluster(video, stable_threshold=2, cluster_threshold=0.85, visualize=False)`:
   - Run `keyframe_location(video)` for the initial set
   - Encode keyframes with `openai/clip-vit-base-patch32` via `transformers`
   - Build cosine similarity matrix; agglomerative cluster with `distance_threshold = 1 - cluster_threshold`
   - Keep medoid per cluster; return deduplicated frames + indices in original order
2. Register `'clip'` in `get_keyframe_fn`

**Deps:** `pip install transformers torch` (lazy import at function call time to avoid slowing baseline)

---

### Phase 5 — Fix 5: VLM Pair Classification (Ollama) ✅

**Files:** `gifdroid/hhv_keyframe.py`

**Tasks:**

1. Add `keyframe_location_vlm(video, stable_threshold=2, model="llama3.2-vision", visualize=False)`:
   - Run `keyframe_location(video)` for candidates
   - For each consecutive pair: base64-encode both frames as JPEG, POST to `http://localhost:11434/api/chat` with the "SAME or DIFFERENT" prompt
   - Drop `k_{i+1}` if response is `"SAME"`; keep all on connection error (graceful fallback with warning)
2. Register `'vlm'` in `get_keyframe_fn`

**Deps:** `pip install ollama` + `ollama pull llama3.2-vision` (one-time, ~7GB)

---

### Execution Order

| Phase | Content | Depends on |
| ----- | ------- | ---------- |
| 1 | Infrastructure + hysteresis + main.py wiring | — |
| 2 | Fix 1: Video Stabilization | Phase 1 |
| 3 | Fix 3: Homography SSIM | Phase 1 |
| 4 | Fix 4: CLIP Clustering | Phase 1 |
| 5 | Fix 5: VLM Classification | Phase 1 |

Phases 2–5 are independent and can be implemented in any order once Phase 1 is complete.