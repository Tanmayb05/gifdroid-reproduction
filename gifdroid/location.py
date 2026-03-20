import cv2
import logging
import operator
import time
import numpy as np
import matplotlib.pyplot as plt
from itertools import groupby
from collections import Counter
from skimage.metrics import structural_similarity as ssim

logger = logging.getLogger('gifdroid.location')


def extract_Y(img):
    # Convert BGR frame to YUV and return only the luma (Y) channel
    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    y, _, _ = cv2.split(img_yuv)
    return y


def read_frames_from_video(video):
    """Read all frames from the video and return raw frames + luma-only frames."""
    frames = []
    y_frames = []
    vidcap = cv2.VideoCapture(video)
    t0 = time.time()

    success, frame = vidcap.read()
    frames.append(frame)
    y_frames.append(extract_Y(frame)[25:])  # skip top 25 rows (status bar)

    while success:
        success, frame = vidcap.read()
        if not success:
            break
        frames.append(frame)
        y_frames.append(extract_Y(frame)[25:])

    vidcap.release()
    elapsed = time.time() - t0
    logger.debug(f'read_frames_from_video: {len(frames)} frames decoded in {elapsed:.2f}s')
    return frames, y_frames


def calculate_sim_seq(frame_list):
    """Compute pairwise SSIM between consecutive luma frames."""
    t0 = time.time()
    sim_list = []
    for i in range(len(frame_list) - 1):
        sim = ssim(frame_list[i], frame_list[i + 1])
        sim_list.append(sim)
    elapsed = time.time() - t0
    logger.debug(f'calculate_sim_seq: {len(sim_list)} similarities computed in {elapsed:.2f}s')
    return sim_list


def is_stable(start, end, list_):
    """Return True if all similarity values in [start, end) are above 0.95 (stable screen)."""
    if start < 0:
        start = 0
    if end > len(list_):
        end = len(list_)
    count_candidate = 0
    for x in list_[start:end]:
        if x <= 0.95:
            return False
    return count_candidate <= 1


def detect_keyframes(sim_sequence, stable_threshold=2):
    """
    Identify keyframe indices from a similarity sequence.
    A keyframe marks the start of a stable screen region (transition boundary).
    """
    t0 = time.time()
    stable_list = [
        is_stable(idx - stable_threshold, idx + stable_threshold, sim_sequence)
        for idx in range(len(sim_sequence))
    ]
    stable_list.reverse()
    keyframe_list = []

    idx = 0
    for k, g in groupby(stable_list):
        if k:
            keyframe_list.append(idx)
        idx += sum(1 for i in g)

    keyframes_index = [len(stable_list) - x for x in keyframe_list]
    keyframes_index.reverse()

    elapsed = time.time() - t0
    logger.debug(
        f'detect_keyframes: {len(keyframes_index)} keyframes detected '
        f'from {len(sim_sequence)} frames in {elapsed:.2f}s'
    )
    return keyframes_index


def keyframe_location(video, stable_threshold=2, visualize=False):
    """
    Full keyframe location pipeline:
      1. Decode all video frames
      2. Compute consecutive-frame similarity
      3. Detect stable regions as keyframes
    Returns keyframe images and their frame indices.
    """
    t0 = time.time()
    logger.info(f'keyframe_location: starting on video "{video}"')

    # Step 1: decode frames
    frames, y_frames = read_frames_from_video(video)

    # Step 2: consecutive frame similarity (on luma channel for speed)
    sim_list = calculate_sim_seq(y_frames)

    # Step 3: optional similarity plot for debugging
    if visualize:
        plt.plot(np.arange(len(sim_list)), np.array(sim_list))
        plt.xlabel("frame")
        plt.ylabel("similarity")
        plt.show()

    # Step 4: detect keyframes from stable regions
    keyframes_index = detect_keyframes(sim_list, stable_threshold=stable_threshold)

    keyframes = [frames[i] for i in keyframes_index]

    elapsed = time.time() - t0
    logger.info(
        f'keyframe_location: done — {len(keyframes)} keyframes at indices '
        f'{keyframes_index} ({elapsed:.2f}s total)'
    )
    return keyframes, keyframes_index
