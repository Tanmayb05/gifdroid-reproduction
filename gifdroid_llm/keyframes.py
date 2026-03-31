from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List

import cv2
import numpy as np

from gifdroid_llm.config import KeyframeSelectionConfig
from gifdroid_llm.video import SampledFrame


@dataclass
class Keyframe:
    sequence_index: int
    frame_number: int
    timestamp_sec: float
    motion_score: float
    image_bgr: np.ndarray
    file_name: str = ""


class KeyframeSelector:
    """Select keyframes that best represent execution-relevant state changes."""

    def select(
        self,
        sampled_frames: List[SampledFrame],
        cfg: KeyframeSelectionConfig,
        logger: logging.Logger,
    ) -> List[Keyframe]:
        if not sampled_frames:
            return []

        motions = np.array([f.motion_from_prev for f in sampled_frames], dtype=float)
        median = float(np.median(motions))
        std_dev = float(np.std(motions))
        threshold = max(4.0, median + 0.4 * std_dev)

        selected: List[Keyframe] = []
        min_gap = cfg.min_gap_seconds
        last_time = -1e9

        for idx, frame in enumerate(sampled_frames):
            must_include = idx == 0 or idx == len(sampled_frames) - 1
            changed_enough = frame.motion_from_prev >= threshold
            gap_ok = (frame.timestamp_sec - last_time) >= min_gap

            if (must_include or changed_enough) and gap_ok:
                selected.append(
                    Keyframe(
                        sequence_index=len(selected),
                        frame_number=frame.frame_number,
                        timestamp_sec=frame.timestamp_sec,
                        motion_score=frame.motion_from_prev,
                        image_bgr=frame.image_bgr,
                    )
                )
                last_time = frame.timestamp_sec

        if len(selected) < min(5, len(sampled_frames)):
            selected = self._fallback_even_selection(sampled_frames, max_count=min(8, len(sampled_frames)))

        logger.info(
            "Keyframe selection complete | method=%s threshold=%.3f selected=%d sampled=%d",
            cfg.method,
            threshold,
            len(selected),
            len(sampled_frames),
        )
        return selected

    def save_keyframes(self, keyframes: List[Keyframe], keyframes_dir: Path, video_type: str) -> None:
        keyframes_dir.mkdir(parents=True, exist_ok=True)
        for idx, keyframe in enumerate(keyframes, start=1):
            file_name = f"kf-{idx:04d}.png"
            keyframe.file_name = file_name
            out_path = keyframes_dir / file_name
            cv2.imwrite(str(out_path), keyframe.image_bgr)

    def build_frames_manifest(
        self,
        sampled_frames: List[SampledFrame],
        keyframes: List[Keyframe],
        video_path: Path,
        llm: str,
    ) -> Dict[str, Any]:
        keyframe_frame_numbers = {kf.frame_number for kf in keyframes}
        sampled_payload = [
            {
                "frame_number": frame.frame_number,
                "timestamp_sec": round(frame.timestamp_sec, 3),
                "motion_from_prev": round(frame.motion_from_prev, 3),
                "selected_as_keyframe": frame.frame_number in keyframe_frame_numbers,
            }
            for frame in sampled_frames
        ]

        return {
            "video": str(video_path),
            "llm": llm,
            "sampled_count": len(sampled_frames),
            "keyframe_count": len(keyframes),
            "sampled_frames": sampled_payload,
        }

    def _fallback_even_selection(self, sampled_frames: List[SampledFrame], max_count: int) -> List[Keyframe]:
        idxs = np.linspace(0, len(sampled_frames) - 1, max_count, dtype=int)
        return [
            Keyframe(
                sequence_index=i,
                frame_number=sampled_frames[idx].frame_number,
                timestamp_sec=sampled_frames[idx].timestamp_sec,
                motion_score=sampled_frames[idx].motion_from_prev,
                image_bgr=sampled_frames[idx].image_bgr,
            )
            for i, idx in enumerate(idxs.tolist())
        ]
