from __future__ import annotations

import logging
from dataclasses import dataclass
from itertools import groupby
from pathlib import Path
from typing import Any, Dict, List

import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

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

        if cfg.method == "ssim":
            return self._select_ssim(sampled_frames, cfg, logger)
        return self._select_motion(sampled_frames, cfg, logger)

    def _select_motion(
        self,
        sampled_frames: List[SampledFrame],
        cfg: KeyframeSelectionConfig,
        logger: logging.Logger,
    ) -> List[Keyframe]:
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

    def _select_ssim(
        self,
        sampled_frames: List[SampledFrame],
        cfg: KeyframeSelectionConfig,
        logger: logging.Logger,
    ) -> List[Keyframe]:
        if len(sampled_frames) == 1:
            frame = sampled_frames[0]
            return [
                Keyframe(
                    sequence_index=0,
                    frame_number=frame.frame_number,
                    timestamp_sec=frame.timestamp_sec,
                    motion_score=frame.motion_from_prev,
                    image_bgr=frame.image_bgr,
                )
            ]

        sim_sequence = self._calculate_ssim_sequence(sampled_frames)
        candidate_indices = self._detect_keyframe_indices(
            sim_sequence=sim_sequence,
            stable_threshold=cfg.stable_threshold,
            ssim_threshold=cfg.ssim_threshold,
            frame_count=len(sampled_frames),
        )
        selected = self._indices_to_keyframes(
            sampled_frames=sampled_frames,
            indices=candidate_indices,
            min_gap_seconds=cfg.min_gap_seconds,
        )

        if len(selected) < min(5, len(sampled_frames)):
            selected = self._fallback_even_selection(sampled_frames, max_count=min(8, len(sampled_frames)))

        logger.info(
            "Keyframe selection complete | method=ssim ssim_threshold=%.3f stable_threshold=%d selected=%d sampled=%d",
            cfg.ssim_threshold,
            cfg.stable_threshold,
            len(selected),
            len(sampled_frames),
        )
        return selected

    def _calculate_ssim_sequence(self, sampled_frames: List[SampledFrame]) -> List[float]:
        y_frames = [self._extract_luma(frame.image_bgr) for frame in sampled_frames]
        return [
            float(ssim(y_frames[i], y_frames[i + 1]))
            for i in range(len(y_frames) - 1)
        ]

    def _extract_luma(self, image_bgr: np.ndarray) -> np.ndarray:
        img_yuv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2YUV)
        y_channel, _, _ = cv2.split(img_yuv)
        if y_channel.shape[0] > 25:
            return y_channel[25:]
        return y_channel

    def _is_stable(
        self,
        idx: int,
        sim_sequence: List[float],
        stable_threshold: int,
        ssim_threshold: float,
    ) -> bool:
        start = max(0, idx - stable_threshold)
        end = min(len(sim_sequence), idx + stable_threshold)
        for sim_value in sim_sequence[start:end]:
            if sim_value <= ssim_threshold:
                return False
        return True

    def _detect_keyframe_indices(
        self,
        sim_sequence: List[float],
        stable_threshold: int,
        ssim_threshold: float,
        frame_count: int,
    ) -> List[int]:
        stable_list = [
            self._is_stable(
                idx=idx,
                sim_sequence=sim_sequence,
                stable_threshold=stable_threshold,
                ssim_threshold=ssim_threshold,
            )
            for idx in range(len(sim_sequence))
        ]
        stable_list.reverse()

        group_starts: List[int] = []
        idx = 0
        for is_stable_group, values in groupby(stable_list):
            group_len = sum(1 for _ in values)
            if is_stable_group:
                group_starts.append(idx)
            idx += group_len

        detected = [len(stable_list) - x for x in group_starts]
        detected.reverse()

        candidates = set(detected)
        candidates.add(0)
        candidates.add(frame_count - 1)
        return sorted(candidates)

    def _indices_to_keyframes(
        self,
        sampled_frames: List[SampledFrame],
        indices: List[int],
        min_gap_seconds: float,
    ) -> List[Keyframe]:
        selected: List[Keyframe] = []
        last_time = -1e9
        for idx in indices:
            frame = sampled_frames[idx]
            if selected and (frame.timestamp_sec - last_time) < min_gap_seconds:
                continue
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
