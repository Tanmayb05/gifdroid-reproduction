from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

import cv2
import numpy as np

from gifdroid_llm_trace.config import FrameSamplingConfig


class VideoError(ValueError):
    """Raised when video reading/extraction fails."""


@dataclass
class SampledFrame:
    frame_number: int
    timestamp_sec: float
    image_bgr: np.ndarray
    motion_from_prev: float


class VideoFrameExtractor:
    """Extract sampled frames from a bug video."""

    def extract(
        self,
        video_path: Path,
        sampling_cfg: FrameSamplingConfig,
        logger: logging.Logger,
    ) -> Tuple[List[SampledFrame], Dict[str, float]]:
        if not video_path.exists():
            raise VideoError(f"Video file not found: {video_path}")

        cap = cv2.VideoCapture(str(video_path))
        if not cap.isOpened():
            raise VideoError(f"Unable to open video: {video_path}")

        native_fps = float(cap.get(cv2.CAP_PROP_FPS) or 0.0)
        if native_fps <= 0:
            native_fps = sampling_cfg.fps

        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT) or 0)
        duration_sec = float(total_frames / native_fps) if native_fps > 0 else 0.0

        stride = max(1, int(round(native_fps / sampling_cfg.fps)))
        sampled: List[SampledFrame] = []
        prev_gray = None
        frame_idx = 0

        logger.info(
            "Starting frame extraction | native_fps=%.3f target_fps=%.3f stride=%d total_frames=%d",
            native_fps,
            sampling_cfg.fps,
            stride,
            total_frames,
        )

        while True:
            ok, frame = cap.read()
            if not ok:
                break

            if frame_idx % stride != 0:
                frame_idx += 1
                continue

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            motion = 0.0
            if prev_gray is not None:
                motion = float(np.mean(cv2.absdiff(gray, prev_gray)))
            prev_gray = gray

            sampled.append(
                SampledFrame(
                    frame_number=frame_idx,
                    timestamp_sec=float(frame_idx / native_fps),
                    image_bgr=frame,
                    motion_from_prev=motion,
                )
            )
            frame_idx += 1

        cap.release()

        if not sampled:
            raise VideoError(f"No frames sampled from video: {video_path}")

        sampled = self._apply_max_frames(sampled, sampling_cfg, logger)
        if sampling_cfg.strategy == "adaptive":
            sampled = self._apply_adaptive_filter(sampled, sampling_cfg.max_frames, logger)

        metadata: Dict[str, float] = {
            "native_fps": native_fps,
            "duration_sec": duration_sec,
            "total_frames": float(total_frames),
            "sampled_frames": float(len(sampled)),
        }

        logger.info("Frame extraction complete | sampled_frames=%d", len(sampled))
        return sampled, metadata

    def _apply_max_frames(
        self,
        sampled: List[SampledFrame],
        sampling_cfg: FrameSamplingConfig,
        logger: logging.Logger,
    ) -> List[SampledFrame]:
        if len(sampled) <= sampling_cfg.max_frames:
            return sampled

        idxs = np.linspace(0, len(sampled) - 1, sampling_cfg.max_frames, dtype=int)
        reduced = [sampled[i] for i in idxs.tolist()]
        logger.info(
            "Applied max_frames constraint | before=%d after=%d",
            len(sampled),
            len(reduced),
        )
        return reduced

    def _apply_adaptive_filter(
        self,
        sampled: List[SampledFrame],
        max_frames: int,
        logger: logging.Logger,
    ) -> List[SampledFrame]:
        if len(sampled) <= 2:
            return sampled

        motions = np.array([f.motion_from_prev for f in sampled[1:]], dtype=float)
        threshold = float(np.percentile(motions, 65))

        keep = [sampled[0]]
        for frame in sampled[1:-1]:
            if frame.motion_from_prev >= threshold:
                keep.append(frame)
        keep.append(sampled[-1])

        if len(keep) > max_frames:
            idxs = np.linspace(0, len(keep) - 1, max_frames, dtype=int)
            keep = [keep[i] for i in idxs.tolist()]

        logger.info(
            "Adaptive filter applied | threshold=%.3f before=%d after=%d",
            threshold,
            len(sampled),
            len(keep),
        )
        return keep
