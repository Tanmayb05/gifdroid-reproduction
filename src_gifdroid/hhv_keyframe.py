"""
hhv_keyframe.py — Alternative keyframe detection methods for handheld video (HHV).

Each function has the same signature as keyframe_location() in location.py:
    (keyframes: list, keyframes_index: list) = fn(video, stable_threshold=2, visualize=False, **kwargs)

Use get_keyframe_fn(method) to retrieve the right function by name.
"""

import logging
import os
import subprocess
import tempfile
from itertools import groupby
from pathlib import Path

from src_gifdroid.location import (
    keyframe_location,
    read_frames_from_video,
    calculate_sim_seq,
    detect_keyframes,
)

logger = logging.getLogger('src_gifdroid.hhv_keyframe')

# ---------------------------------------------------------------------------
# Fix 1 — Video Stabilization (FFmpeg)
# ---------------------------------------------------------------------------

def keyframe_location_stabilized(video, stable_threshold=2, visualize=False):
    """
    Keyframe detection with FFmpeg video stabilization pre-processing.

    Two-pass FFmpeg stabilization (vidstabdetect + vidstabtransform) removes
    camera shake before SSIM is computed, so the baseline threshold works correctly.
    Temp files are always cleaned up in a finally block.
    """
    import time

    t0 = time.time()
    logger.info(f'keyframe_location_stabilized: starting on "{video}"')

    video_path = Path(video)
    stabilized = video_path.with_name(video_path.stem + '_stabilized.mp4')
    trf_file = Path(tempfile.gettempdir()) / 'transforms.trf'

    try:
        # Pass 1 — detect motion
        subprocess.run(
            [
                'ffmpeg', '-y', '-i', str(video_path),
                '-vf', f'vidstabdetect=shakiness=5:accuracy=15:result={trf_file}',
                '-f', 'null', '-',
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        # Pass 2 — apply stabilization
        subprocess.run(
            [
                'ffmpeg', '-y', '-i', str(video_path),
                '-vf', f'vidstabtransform=smoothing=10:input={trf_file}',
                str(stabilized),
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        result = keyframe_location(str(stabilized), stable_threshold, visualize)
    finally:
        if stabilized.exists():
            stabilized.unlink()
        if trf_file.exists():
            trf_file.unlink()

    elapsed = time.time() - t0
    keyframes, keyframes_index = result
    logger.info(
        f'keyframe_location_stabilized: done — {len(keyframes)} keyframes at indices '
        f'{keyframes_index} ({elapsed:.2f}s)'
    )
    return result


# ---------------------------------------------------------------------------
# Fix 2 — Temporal Hysteresis
# ---------------------------------------------------------------------------

def keyframe_location_hysteresis(video, stable_threshold=2, hysteresis_k=3, visualize=False):
    """
    Keyframe detection with temporal hysteresis to suppress camera-shake false positives.

    Instead of a single-frame stability check, a frame is only considered stable if
    hysteresis_k consecutive forward frames all have SSIM > 0.95.  Camera shake causes
    short dips that recover in 1-2 frames; genuine screen transitions stay low for many frames.
    """
    import time
    import numpy as np
    import matplotlib.pyplot as plt

    t0 = time.time()
    logger.info(f'keyframe_location_hysteresis: starting on "{video}" (k={hysteresis_k})')

    frames, y_frames = read_frames_from_video(video)
    sim_list = calculate_sim_seq(y_frames)

    if visualize:
        plt.plot(np.arange(len(sim_list)), np.array(sim_list))
        plt.xlabel("frame")
        plt.ylabel("similarity")
        plt.title("Hysteresis — similarity sequence")
        plt.show()

    n = len(sim_list)

    # Build hysteresis-stable list: position i is stable iff
    # sim_list[i], sim_list[i+1], ..., sim_list[i+k-1] are all > 0.95
    stable_list = []
    for i in range(n):
        end = min(i + hysteresis_k, n)
        stable = all(sim_list[j] > 0.95 for j in range(i, end))
        stable_list.append(stable)

    # Replicate detect_keyframes groupby logic on hysteresis stable_list
    stable_reversed = list(reversed(stable_list))
    keyframe_list = []
    idx = 0
    for k, g in groupby(stable_reversed):
        if k:
            keyframe_list.append(idx)
        idx += sum(1 for _ in g)

    keyframes_index = [n - x for x in keyframe_list]
    keyframes_index.reverse()

    keyframes = [frames[i] for i in keyframes_index]

    elapsed = time.time() - t0
    logger.info(
        f'keyframe_location_hysteresis: done — {len(keyframes)} keyframes at indices '
        f'{keyframes_index} ({elapsed:.2f}s)'
    )
    return keyframes, keyframes_index


# ---------------------------------------------------------------------------
# Fix 3 — Homography-corrected SSIM
# ---------------------------------------------------------------------------

def keyframe_location_homography(video, stable_threshold=2, visualize=False):
    """
    Keyframe detection with homography-corrected SSIM.

    For each consecutive luma frame pair, SIFT keypoints are matched and a
    homography is estimated via RANSAC.  y_{i+1} is warped onto y_i before
    SSIM is computed, so camera-pan/tilt/zoom is compensated.  If fewer than
    4 matches are found (e.g. very blurry frame), raw SSIM is used as fallback.
    """
    import time
    import numpy as np
    import cv2
    from skimage.metrics import structural_similarity as ssim
    import matplotlib.pyplot as plt

    t0 = time.time()
    logger.info(f'keyframe_location_homography: starting on "{video}"')

    frames, y_frames = read_frames_from_video(video)

    # opencv-contrib 3.4.x: SIFT is patented, lives under xfeatures2d
    try:
        sift = cv2.xfeatures2d.SIFT_create()
    except AttributeError:
        sift = cv2.SIFT_create()
    bf = cv2.BFMatcher(cv2.NORM_L2)

    sim_list = []
    for i in range(len(y_frames) - 1):
        y_a = y_frames[i]
        y_b = y_frames[i + 1]

        kp_a, desc_a = sift.detectAndCompute(y_a, None)
        kp_b, desc_b = sift.detectAndCompute(y_b, None)

        warped = None
        if (desc_a is not None and desc_b is not None
                and len(kp_a) >= 4 and len(kp_b) >= 4):
            matches = bf.knnMatch(desc_a, desc_b, k=2)
            good = [m for m, n in matches if m.distance < 0.75 * n.distance]
            if len(good) >= 4:
                pts_a = np.float32([kp_a[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
                pts_b = np.float32([kp_b[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
                H, mask = cv2.findHomography(pts_b, pts_a, cv2.RANSAC, 5.0)
                if H is not None:
                    h, w = y_a.shape
                    warped = cv2.warpPerspective(y_b, H, (w, h))

        if warped is not None:
            sim = ssim(y_a, warped)
        else:
            sim = ssim(y_a, y_b)

        sim_list.append(sim)

    if visualize:
        plt.plot(np.arange(len(sim_list)), np.array(sim_list))
        plt.xlabel("frame")
        plt.ylabel("similarity")
        plt.title("Homography — similarity sequence")
        plt.show()

    keyframes_index = detect_keyframes(sim_list, stable_threshold=stable_threshold)
    keyframes = [frames[i] for i in keyframes_index]

    elapsed = time.time() - t0
    logger.info(
        f'keyframe_location_homography: done — {len(keyframes)} keyframes at indices '
        f'{keyframes_index} ({elapsed:.2f}s)'
    )
    return keyframes, keyframes_index


# ---------------------------------------------------------------------------
# Fix 4 — Post-hoc CLIP Clustering
# ---------------------------------------------------------------------------

def keyframe_location_clip_cluster(video, stable_threshold=2, cluster_threshold=0.85, visualize=False):
    """
    Keyframe detection with post-hoc CLIP clustering to deduplicate similar screens.

    Runs the baseline keyframe detector first, then encodes each keyframe with
    CLIP (openai/clip-vit-base-patch32) and agglomeratively clusters them by
    cosine similarity.  The medoid of each cluster is kept, removing near-duplicate
    frames caused by camera shake without discarding genuine screen transitions.

    Deps: pip install transformers torch
    """
    import time
    import numpy as np

    t0 = time.time()
    logger.info(f'keyframe_location_clip_cluster: starting on "{video}" (threshold={cluster_threshold})')

    # Step 1 — baseline keyframes
    keyframes, keyframes_index = keyframe_location(video, stable_threshold, visualize)
    n = len(keyframes)
    logger.info(f'keyframe_location_clip_cluster: baseline produced {n} keyframes')

    if n <= 1:
        logger.info('keyframe_location_clip_cluster: <=1 keyframe, skipping clustering')
        return keyframes, keyframes_index

    # Step 2 — lazy imports (avoid slowing baseline runs)
    try:
        import torch
        from transformers import CLIPProcessor, CLIPModel
        from sklearn.cluster import AgglomerativeClustering
    except ImportError as e:
        logger.warning(
            f'keyframe_location_clip_cluster: missing dependency ({e}); '
            'returning baseline result. Install with: pip install transformers torch scikit-learn'
        )
        return keyframes, keyframes_index

    # Step 3 — encode keyframes with CLIP
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = CLIPModel.from_pretrained('openai/clip-vit-base-patch32').to(device)
    processor = CLIPProcessor.from_pretrained('openai/clip-vit-base-patch32')

    import cv2
    pil_frames = []
    for frame in keyframes:
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        from PIL import Image
        pil_frames.append(Image.fromarray(rgb))

    inputs = processor(images=pil_frames, return_tensors='pt').to(device)
    with torch.no_grad():
        features = model.get_image_features(**inputs)

    # L2-normalise so dot product = cosine similarity
    features = features / features.norm(dim=-1, keepdim=True)
    features_np = features.cpu().numpy()  # shape (n, 512)

    # Step 4 — agglomerative clustering
    distance_threshold = 1.0 - cluster_threshold
    clustering = AgglomerativeClustering(
        n_clusters=None,
        metric='cosine',
        linkage='average',
        distance_threshold=distance_threshold,
    )
    labels = clustering.fit_predict(features_np)
    n_clusters = labels.max() + 1
    logger.info(f'keyframe_location_clip_cluster: {n} keyframes → {n_clusters} clusters')

    # Step 5 — pick medoid per cluster
    kept_indices = []
    for cluster_id in range(n_clusters):
        members = np.where(labels == cluster_id)[0]
        if len(members) == 1:
            kept_indices.append(int(members[0]))
        else:
            # Medoid: member with highest mean cosine similarity to others in cluster
            cluster_feats = features_np[members]
            sim_matrix = cluster_feats @ cluster_feats.T
            mean_sims = sim_matrix.mean(axis=1)
            medoid_local = int(np.argmax(mean_sims))
            kept_indices.append(int(members[medoid_local]))

    # Restore original temporal ordering
    kept_indices.sort()
    out_keyframes = [keyframes[i] for i in kept_indices]
    out_indices = [keyframes_index[i] for i in kept_indices]

    elapsed = time.time() - t0
    logger.info(
        f'keyframe_location_clip_cluster: done — {len(out_keyframes)} keyframes at indices '
        f'{out_indices} ({elapsed:.2f}s)'
    )
    return out_keyframes, out_indices


# ---------------------------------------------------------------------------
# Fix 5 — VLM Pair Classification (Ollama / Llama 3.2-Vision)
# ---------------------------------------------------------------------------

def keyframe_location_vlm(video, stable_threshold=2, model="llama3.2-vision", visualize=False):
    """
    Keyframe detection with VLM-based duplicate filtering via Ollama.

    Runs the baseline detector to get candidate keyframes, then asks a local
    vision-language model (Llama 3.2-Vision via Ollama) whether each consecutive
    pair shows the SAME or DIFFERENT UI screen.  Duplicates are dropped.

    On any connection error the candidate set is returned unchanged with a warning.

    Deps: pip install ollama  +  ollama pull llama3.2-vision  (~7 GB one-time)
    """
    import base64
    import time

    import cv2

    t0 = time.time()
    logger.info(f'keyframe_location_vlm: starting on "{video}" (model={model})')

    # Step 1 — baseline candidates
    keyframes, keyframes_index = keyframe_location(video, stable_threshold, visualize)
    n = len(keyframes)
    logger.info(f'keyframe_location_vlm: baseline produced {n} keyframes')

    if n <= 1:
        logger.info('keyframe_location_vlm: <=1 keyframe, skipping VLM filtering')
        return keyframes, keyframes_index

    # Step 2 — lazy import
    try:
        import ollama as _ollama
    except ImportError:
        logger.warning(
            'keyframe_location_vlm: ollama package not installed; '
            'returning baseline result. Install with: pip install ollama'
        )
        return keyframes, keyframes_index

    def _frame_to_b64(frame):
        """Encode a BGR frame as a base64 JPEG string."""
        ok, buf = cv2.imencode('.jpg', frame)
        if not ok:
            raise RuntimeError('cv2.imencode failed')
        return base64.b64encode(buf.tobytes()).decode('utf-8')

    prompt = (
        "These are two frames from an Android screen recording. "
        "Do they show the SAME UI screen or DIFFERENT UI screens? "
        "Reply with only: SAME or DIFFERENT"
    )

    # Step 3 — filter consecutive pairs
    kept_frames = [keyframes[0]]
    kept_indices = [keyframes_index[0]]

    for i in range(1, n):
        prev_b64 = _frame_to_b64(kept_frames[-1])
        curr_b64 = _frame_to_b64(keyframes[i])

        try:
            response = _ollama.chat(
                model=model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                        "images": [prev_b64, curr_b64],
                    }
                ],
            )
            answer = response["message"]["content"].strip().upper()
        except Exception as exc:
            logger.warning(
                f'keyframe_location_vlm: Ollama call failed ({exc}); '
                'keeping frame (graceful fallback)'
            )
            answer = "DIFFERENT"

        if answer == "SAME":
            logger.debug(
                f'keyframe_location_vlm: dropping duplicate frame at index {keyframes_index[i]}'
            )
        else:
            kept_frames.append(keyframes[i])
            kept_indices.append(keyframes_index[i])

    elapsed = time.time() - t0
    logger.info(
        f'keyframe_location_vlm: done — {len(kept_frames)} keyframes at indices '
        f'{kept_indices} ({elapsed:.2f}s)'
    )
    return kept_frames, kept_indices


# ---------------------------------------------------------------------------
# Dispatcher
# ---------------------------------------------------------------------------

def get_keyframe_fn(method):
    """Return the keyframe detection function for the given method name."""
    dispatch = {
        'baseline': keyframe_location,
        'stabilize': keyframe_location_stabilized,
        'hysteresis': keyframe_location_hysteresis,
        'homography': keyframe_location_homography,
        'clip': keyframe_location_clip_cluster,
        'vlm': keyframe_location_vlm,
    }
    if method not in dispatch:
        raise ValueError(
            f"Unknown keyframe method '{method}'. "
            f"Valid options: {sorted(dispatch.keys())}"
        )
    return dispatch[method]