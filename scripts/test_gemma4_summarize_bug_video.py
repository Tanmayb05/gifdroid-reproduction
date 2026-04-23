#!/usr/bin/env python3
"""Summarize a bug reproduction video using Ollama gemma4:e4b.

Extracts frames from the video, encodes them as base64 PNG, and sends them
to the local Ollama API for a plain-text description of the bug shown.

Hardcode VIDEO_PATH below to point at your target video.
"""

import base64
import json
import sys
import time
from pathlib import Path
from urllib import error as url_error
from urllib import request as url_request

import cv2

# ---------------------------------------------------------------------------
# CONFIGURATION — edit these two values before running
# ---------------------------------------------------------------------------
VIDEO_PATH = Path("apps/adaway/videos/screenrec/srv-001.mp4")
OLLAMA_MODEL = "gemma4:e4b"
OLLAMA_BASE_URL = "http://localhost:11434"
MAX_FRAMES = 8       # number of evenly-spaced frames to sample
TIMEOUT_SEC = 300    # Ollama request timeout in seconds
# ---------------------------------------------------------------------------


def extract_frames(video_path: Path, max_frames: int) -> list[tuple[float, bytes]]:
    """Return up to max_frames evenly-spaced (timestamp_sec, png_bytes) pairs."""
    print(f"[extract_frames] Opening video: {video_path}")
    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        print(f"[extract_frames] ERROR: cannot open video {video_path}", file=sys.stderr)
        sys.exit(1)

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    duration = total_frames / fps
    print(f"[extract_frames] total_frames={total_frames} fps={fps:.2f} duration={duration:.2f}s")

    # Pick evenly-spaced frame indices
    if max_frames >= total_frames:
        indices = list(range(total_frames))
    else:
        step = total_frames / max_frames
        indices = [int(i * step) for i in range(max_frames)]

    print(f"[extract_frames] Sampling {len(indices)} frames at indices: {indices}")

    frames: list[tuple[float, bytes]] = []
    for idx in indices:
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ret, frame = cap.read()
        if not ret:
            print(f"[extract_frames] WARNING: could not read frame {idx}, skipping")
            continue
        success, buf = cv2.imencode(".png", frame)
        if not success:
            print(f"[extract_frames] WARNING: could not encode frame {idx}, skipping")
            continue
        timestamp = idx / fps
        frames.append((timestamp, buf.tobytes()))
        print(f"[extract_frames] Captured frame idx={idx} timestamp={timestamp:.2f}s size={len(buf.tobytes())} bytes")

    cap.release()
    print(f"[extract_frames] Done — {len(frames)} frames extracted")
    return frames


def build_ollama_payload(frames: list[tuple[float, bytes]], model: str) -> dict:
    """Build the Ollama /api/chat payload with images embedded as base64."""
    print(f"[build_payload] Building payload with {len(frames)} frames for model '{model}'")

    # Ollama multimodal: images are base64-encoded strings in the images field
    images_b64 = [base64.b64encode(png_bytes).decode("ascii") for _, png_bytes in frames]

    frame_descriptions = "\n".join(
        f"  Frame {i + 1} at {ts:.2f}s"
        for i, (ts, _) in enumerate(frames)
    )
    prompt = (
        "You are a QA engineer analysing a screen recording of an Android app bug reproduction.\n"
        "The images below are evenly-spaced frames from the video:\n"
        f"{frame_descriptions}\n\n"
        "Your goal is to produce a precise bug reproduction report.\n\n"
        "Return ONLY the following sections, in this exact format:\n\n"
        "PRECONDITIONS:\n"
        "- List the app state or setup required before starting (e.g. app installed, logged in, specific setting enabled).\n\n"
        "STEPS TO REPRODUCE:\n"
        "- Number each user action as a concrete UI gesture: tap, long-press, swipe, type, scroll, press back/home.\n"
        "- Name the specific UI element acted on (button label, field name, menu item).\n"
        "- Be precise enough that someone could follow the steps without watching the video.\n\n"
        "OBSERVED BEHAVIOUR:\n"
        "- Describe exactly what goes wrong (crash, wrong screen, missing element, incorrect value, freeze, etc.).\n\n"
        "EXPECTED BEHAVIOUR:\n"
        "- Describe what should have happened instead."
    )

    return {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt,
                "images": images_b64,
            }
        ],
        "stream": False,
        "options": {"temperature": 0.0},
    }


def call_ollama(payload: dict, base_url: str, timeout_sec: int) -> str:
    """POST to Ollama /api/chat and return the assistant message text."""
    url = f"{base_url.rstrip('/')}/api/chat"
    payload_bytes = json.dumps(payload).encode("utf-8")
    req = url_request.Request(
        url=url,
        data=payload_bytes,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    print(f"[call_ollama] Sending request to {url} (timeout={timeout_sec}s) ...")
    start = time.perf_counter()
    try:
        with url_request.urlopen(req, timeout=timeout_sec) as resp:
            raw = resp.read().decode("utf-8")
    except url_error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        print(f"[call_ollama] HTTP error {exc.code}: {body[:300]}", file=sys.stderr)
        sys.exit(1)
    except url_error.URLError as exc:
        print(f"[call_ollama] Connection error: {exc}", file=sys.stderr)
        sys.exit(1)

    elapsed = time.perf_counter() - start
    print(f"[call_ollama] Response received in {elapsed:.2f}s ({len(raw)} chars)")

    data = json.loads(raw)
    message = data.get("message", {})
    content = message.get("content", "")
    if not content:
        print(f"[call_ollama] WARNING: empty content in response. Full response:\n{raw[:500]}")
    return content


def main() -> None:
    video_path = VIDEO_PATH
    if not video_path.is_absolute():
        # Resolve relative to repo root (two levels up from scripts/)
        repo_root = Path(__file__).parent.parent
        video_path = repo_root / video_path

    print(f"[main] Video path resolved to: {video_path}")
    if not video_path.exists():
        print(f"[main] ERROR: video file not found: {video_path}", file=sys.stderr)
        sys.exit(1)

    frames = extract_frames(video_path, MAX_FRAMES)
    if not frames:
        print("[main] ERROR: no frames extracted", file=sys.stderr)
        sys.exit(1)

    payload = build_ollama_payload(frames, OLLAMA_MODEL)
    summary = call_ollama(payload, OLLAMA_BASE_URL, TIMEOUT_SEC)

    print("\n" + "=" * 60)
    print("VIDEO SUMMARY")
    print("=" * 60)
    print(summary)
    print("=" * 60)


if __name__ == "__main__":
    main()
