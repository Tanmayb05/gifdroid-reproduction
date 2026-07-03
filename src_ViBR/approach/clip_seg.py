"""
clip_seg.py — CLIP-based video stable-segment detection.

Splits a video into stable segments by computing cosine similarity
between CLIP image embeddings of consecutive frames.

Usage (standalone):
    python clip_seg.py <video_path> [--threshold 0.95] [--interval 3] [--frame-step 1]

As a library:
    from clip_seg import VideoStableSegmentCLIP

    segmenter = VideoStableSegmentCLIP()
    frames    = segmenter.read_frames_from_video("demo.mp4")
    sim_list  = segmenter.calculate_clip_sim_seq(frames)
    segments  = segmenter.detect_keyframes(sim_list)
"""

import argparse
from itertools import groupby

import cv2
import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel


class VideoStableSegmentCLIP:
    """
    Video segmenter based on CLIP frame similarity.

    Splits a video into stable segments using CLIP-based cosine
    similarity between consecutive frames.
    """

    def __init__(
        self,
        stable_sim_threshold: float = 0.95,
        stable_interval_threshold: int = 3,
        model_name: str = "openai/clip-vit-base-patch32",
        device: str | None = None,
    ):
        """
        Args:
            stable_sim_threshold: Similarity threshold; frames below this
                are considered *unstable* (i.e. a transition is happening).
            stable_interval_threshold: How many frames around an unstable
                frame are also marked unstable (smoothing window).
            model_name: HuggingFace model identifier for CLIP.
            device: 'cuda' or 'cpu'. Auto-detected if None.
        """
        self.sim_threshold = stable_sim_threshold
        self.interval_threshold = stable_interval_threshold
        if device:
            self.device = device
        elif torch.cuda.is_available():
            self.device = "cuda"
        elif torch.backends.mps.is_available():
            self.device = "mps"
        else:
            self.device = "cpu"
        self.model = CLIPModel.from_pretrained(model_name).to(self.device)
        self.processor = CLIPProcessor.from_pretrained(model_name)

    # ------------------------------------------------------------------
    # Frame I/O
    # ------------------------------------------------------------------

    @staticmethod
    def read_frames_from_video(video_path: str, frame_step: int = 1) -> list[Image.Image]:
        """
        Read frames from a video file at the given step interval.

        Returns:
            List of PIL Images (RGB).
        """
        print(f"Reading frames from {video_path} (step={frame_step})...")
        frames: list[Image.Image] = []
        cap = cv2.VideoCapture(video_path)
        idx = 0
        while True:
            ok, frame = cap.read()
            if not ok:
                break
            if idx % frame_step == 0:
                frames.append(Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
            idx += 1
            if idx % 100 == 0:
                print(f"  frame {idx}", end="\r")
        cap.release()
        print(f"\nTotal frames read: {len(frames)}")
        return frames

    # ------------------------------------------------------------------
    # Similarity computation
    # ------------------------------------------------------------------

    @staticmethod
    def _to_feature_tensor(feature_output) -> torch.Tensor:
        """Normalize CLIP output shape across transformers versions."""
        if isinstance(feature_output, torch.Tensor):
            return feature_output

        pool = getattr(feature_output, "pooler_output", None)
        if isinstance(pool, torch.Tensor):
            return pool

        hidden = getattr(feature_output, "last_hidden_state", None)
        if isinstance(hidden, torch.Tensor):
            if hidden.dim() == 3:
                return hidden[:, 0, :]
            return hidden

        raise TypeError(
            f"Unsupported CLIP feature output type: {type(feature_output).__name__}"
        )

    def _encode_frames(self, frame_list: list[Image.Image]) -> list[torch.Tensor]:
        """Encode a list of PIL images into L2-normalised CLIP embeddings."""
        import time
        import sys
        embeddings: list[torch.Tensor] = []
        batch_size = 1
        sys.stdout.write(f"[CLIP] Starting encoding for {len(frame_list)} frames on device: {self.device}\n")
        sys.stdout.write(f"[CLIP] Batch size: {batch_size}\n")
        sys.stdout.flush()

        start_time = time.time()
        last_log_time = start_time
        with torch.no_grad():
            for batch_start in range(0, len(frame_list), batch_size):
                batch_end = min(batch_start + batch_size, len(frame_list))
                batch_frames = frame_list[batch_start:batch_end]

                batch_start_time = time.time()
                inputs = self.processor(images=batch_frames, return_tensors="pt").to(self.device)
                processor_time = time.time() - batch_start_time

                model_start_time = time.time()
                feat_out = self.model.get_image_features(**inputs)
                model_time = time.time() - model_start_time

                feat = self._to_feature_tensor(feat_out)
                feat = feat / feat.norm(p=2, dim=-1, keepdim=True)
                for emb in feat:
                    embeddings.append(emb.cpu())

                elapsed = time.time() - start_time
                # Log every 100 frames or every 60 seconds, whichever comes first
                time_since_last_log = elapsed - (last_log_time - start_time)
                if batch_end % 100 == 0 or batch_end == len(frame_list) or time_since_last_log >= 60:
                    sys.stdout.write(f"[CLIP] Encoded {batch_end}/{len(frame_list)} | Batch time: {model_time:.2f}s (model) + {processor_time:.2f}s (proc) | Total: {elapsed:.1f}s\n")
                    sys.stdout.flush()
                    last_log_time = time.time()

        total_time = time.time() - start_time
        sys.stdout.write(f"[CLIP] ✅ Encoding complete: {total_time:.2f}s for {len(frame_list)} frames\n")
        sys.stdout.flush()
        return embeddings

    def calculate_clip_sim_seq(self, frame_list: list[Image.Image]) -> list[float]:
        """
        Compute a sequence of CLIP cosine-similarities between consecutive frames.

        Args:
            frame_list: List of PIL Images (RGB).
        Returns:
            List of float similarity scores (length = len(frame_list) - 1).
        """
        import time
        import sys
        sys.stdout.write("[CLIP] Starting calculate_clip_sim_seq...\n")
        sys.stdout.flush()

        start_time = time.time()
        embeddings = self._encode_frames(frame_list)
        embed_time = time.time() - start_time
        sys.stdout.write(f"[CLIP] Embedding phase took {embed_time:.2f}s\n")
        sys.stdout.flush()

        sys.stdout.write(f"[CLIP] Computing similarity for {len(embeddings) - 1} frame pairs...\n")
        sys.stdout.flush()
        sim_start = time.time()
        sim_list: list[float] = []
        for i in range(len(embeddings) - 1):
            sim = torch.nn.functional.cosine_similarity(
                embeddings[i], embeddings[i + 1], dim=0
            )
            sim_list.append(sim.item())
        sim_time = time.time() - sim_start
        sys.stdout.write(f"[CLIP] Similarity computation took {sim_time:.2f}s\n")
        sys.stdout.write(f"[CLIP] Total time: {time.time() - start_time:.2f}s\n")
        sys.stdout.flush()
        return sim_list

    # ------------------------------------------------------------------
    # Stable-segment detection
    # ------------------------------------------------------------------

    def _stable_flags(self, sim_sequence: list[float]) -> list[bool]:
        """
        Return a boolean mask over *frames* (same length as sim_sequence).
        True  → frame belongs to a stable region.
        False → frame is in or near a transition.
        """
        n = len(sim_sequence)
        flags = [True] * n
        for i, s in enumerate(sim_sequence):
            if s <= self.sim_threshold:
                lo = max(0, i - self.interval_threshold)
                hi = min(n, i + self.interval_threshold + 1)
                for j in range(lo, hi):
                    flags[j] = False
        return flags

    def detect_keyframes(self, sim_sequence: list[float]) -> list[tuple[int, int]]:
        """
        Detect stable segments from a similarity sequence.

        Args:
            sim_sequence: List of per-frame similarity scores.
        Returns:
            List of (start_frame, end_frame) tuples for each stable segment.
            Within each segment, frames[start] … frames[end] are stable.
        """
        flags = self._stable_flags(sim_sequence)

        segments: list[tuple[int, int]] = []
        idx = 0
        for is_stable, group in groupby(flags):
            length = sum(1 for _ in group)
            if is_stable:
                segments.append((idx, idx + length - 1))
            idx += length

        return segments


# ------------------------------------------------------------------
# CLI entry-point (for standalone testing)
# ------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="CLIP-based video stable-segment detection.",
    )
    parser.add_argument("video_path", help="Path to input video")
    parser.add_argument("--threshold", type=float, default=0.95,
                        help="Similarity threshold (default: 0.95)")
    parser.add_argument("--interval", type=int, default=3,
                        help="Stable interval threshold (default: 3)")
    parser.add_argument("--frame-step", type=int, default=1,
                        help="Read every N-th frame (default: 1)")
    args = parser.parse_args()

    segmenter = VideoStableSegmentCLIP(
        stable_sim_threshold=args.threshold,
        stable_interval_threshold=args.interval,
    )

    frames = segmenter.read_frames_from_video(args.video_path, frame_step=args.frame_step)
    sim_list = segmenter.calculate_clip_sim_seq(frames)
    segments = segmenter.detect_keyframes(sim_list)

    print(f"\nFound {len(segments)} stable segments:")
    for i, (s, e) in enumerate(segments):
        print(f"  Segment {i}: frames {s} – {e}")


if __name__ == "__main__":
    main()
