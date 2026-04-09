"""Milestone 5 — Visualisation script (V5.3).

Produces a side-by-side comparison grid: left column = video keyframes from the
passive execution trace run, right column = screenshots captured by the active
automation session.

Usage:
    python analysis/visualize_comparison.py \\
        --session-dir artifacts/milestone4/run-001 \\
        --keyframes-dir apps/adaway/llm/gemini/gemini-2-5-pro/screenrec/fps1-5__max100__llm-assisted__gap1/run-001/keyframes \\
        --output analysis/adaway_comparison.png

Or auto-discover from app name:
    python analysis/visualize_comparison.py \\
        --app adaway \\
        --session-dir artifacts/milestone5/adaway
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

_THUMB_W = 400
_THUMB_H = 700
_PADDING = 12
_HEADER_H = 36
_LABEL_H = 24
_FONT_SIZE = 16


def _load_thumb(path: Path | str, w: int = _THUMB_W, h: int = _THUMB_H) -> Image.Image:
    """Load an image and resize to thumbnail dimensions."""
    img = Image.open(path).convert("RGB")
    img.thumbnail((w, h), Image.LANCZOS)
    # Pad to exact size
    canvas = Image.new("RGB", (w, h), (30, 30, 30))
    x_off = (w - img.width) // 2
    y_off = (h - img.height) // 2
    canvas.paste(img, (x_off, y_off))
    return canvas


def _label_image(img: Image.Image, text: str, bg: tuple = (50, 50, 50)) -> Image.Image:
    """Add a text label bar below the image."""
    label = Image.new("RGB", (img.width, _LABEL_H), bg)
    draw = ImageDraw.Draw(label)
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", _FONT_SIZE)
    except Exception:
        font = ImageFont.load_default()
    draw.text((6, 4), text, fill=(220, 220, 220), font=font)
    combined = Image.new("RGB", (img.width, img.height + _LABEL_H))
    combined.paste(img, (0, 0))
    combined.paste(label, (0, img.height))
    return combined


def _header_bar(width: int, text: str, bg: tuple = (70, 70, 200)) -> Image.Image:
    """Create a header bar with text."""
    bar = Image.new("RGB", (width, _HEADER_H), bg)
    draw = ImageDraw.Draw(bar)
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", _FONT_SIZE + 2)
    except Exception:
        font = ImageFont.load_default()
    draw.text((8, 8), text, fill=(255, 255, 255), font=font)
    return bar


def _divider(height: int, color: tuple = (80, 80, 80)) -> Image.Image:
    return Image.new("RGB", (_PADDING, height), color)


# ---------------------------------------------------------------------------
# Core comparison builder
# ---------------------------------------------------------------------------

def build_comparison(
    keyframe_paths: list[Path],
    session_step_paths: list[Path],
    output_path: Path,
    app_name: str = "app",
) -> None:
    """Build a side-by-side grid and save to output_path.

    Pairs keyframes (left) with session steps (right). Uses the shorter list
    length to determine row count (minimum 2 pairs).
    """
    pairs = list(zip(keyframe_paths, session_step_paths))
    if not pairs:
        print("[WARN] No pairs to visualise — check input paths")
        return

    # Render each pair as a row
    rows = []
    for i, (kf_path, ss_path) in enumerate(pairs):
        kf_img = _label_image(
            _load_thumb(kf_path),
            f"Video keyframe {i + 1}",
            bg=(40, 80, 40),
        )
        ss_img = _label_image(
            _load_thumb(ss_path),
            f"Automation step {i + 1}",
            bg=(40, 40, 80),
        )
        row_h = kf_img.height
        row = Image.new("RGB", (kf_img.width + _PADDING + ss_img.width, row_h), (20, 20, 20))
        row.paste(kf_img, (0, 0))
        row.paste(ss_img, (kf_img.width + _PADDING, 0))
        rows.append(row)

    row_w = rows[0].width
    row_h = rows[0].height

    # Headers
    kf_header = _header_bar(
        (_THUMB_W),
        "Video Keyframes  (passive pipeline)",
        bg=(30, 100, 30),
    )
    ss_header = _header_bar(
        (_THUMB_W),
        "Automation Screenshots  (active loop)",
        bg=(30, 30, 150),
    )
    header_row = Image.new("RGB", (row_w, _HEADER_H), (20, 20, 20))
    header_row.paste(kf_header, (0, 0))
    header_row.paste(ss_header, (_THUMB_W + _PADDING, 0))

    total_h = _HEADER_H + len(rows) * row_h + (len(rows) - 1) * _PADDING
    canvas = Image.new("RGB", (row_w, total_h), (20, 20, 20))
    canvas.paste(header_row, (0, 0))
    y = _HEADER_H
    for i, row in enumerate(rows):
        canvas.paste(row, (0, y))
        y += row_h
        if i < len(rows) - 1:
            y += _PADDING

    output_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output_path)
    print(f"Saved: {output_path}")
    print(f"       {len(pairs)} matched step pairs shown ({canvas.width}x{canvas.height}px)")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _find_keyframes(keyframes_dir: Path) -> list[Path]:
    return sorted(keyframes_dir.glob("kf-*.png"))


def _find_session_steps(session_dir: Path) -> list[Path]:
    # Try steps/ subdirectory first
    steps_dir = session_dir / "steps"
    if steps_dir.exists():
        return sorted(steps_dir.glob("step_*.png"))
    # Fall back to direct session_dir
    return sorted(session_dir.glob("step_*.png"))


def _auto_find_keyframes(app: str, apps_dir: Path) -> Path | None:
    candidates = [
        apps_dir / app / "llm/gemini/gemini-2-5-pro/screenrec/fps1-5__max100__llm-assisted__gap1/run-001/keyframes",
        apps_dir / app / "llm/gemini/gemini-2-5-flash/screenrec/fps1-5__max100__llm-assisted__gap1/run-001/keyframes",
    ]
    for c in candidates:
        if c.exists() and list(c.glob("kf-*.png")):
            return c
    return None


def main() -> None:
    parser = argparse.ArgumentParser(description="Visualise automation vs. video keyframe comparison")
    parser.add_argument("--session-dir", type=Path, help="Directory with session_trace.json and steps/")
    parser.add_argument("--keyframes-dir", type=Path, help="Directory with kf-XXXX.png keyframes")
    parser.add_argument("--app", default="", help="App name for auto-discovery (overrides --keyframes-dir)")
    parser.add_argument("--apps-dir", type=Path, default=Path("apps"), help="Root apps/ directory")
    parser.add_argument("--output", type=Path, default=None, help="Output PNG path")
    parser.add_argument("--max-pairs", type=int, default=8, help="Maximum pairs to show (default 8)")
    args = parser.parse_args()

    app_name = args.app or (args.session_dir.name if args.session_dir else "app")

    # Resolve keyframes directory
    keyframes_dir = args.keyframes_dir
    if args.app and keyframes_dir is None:
        keyframes_dir = _auto_find_keyframes(args.app, args.apps_dir)
        if keyframes_dir is None:
            print(f"[ERROR] Could not find keyframes for app '{args.app}' under {args.apps_dir}")
            return

    if keyframes_dir is None:
        print("[ERROR] Provide --keyframes-dir or --app")
        return

    if args.session_dir is None:
        print("[ERROR] Provide --session-dir")
        return

    keyframe_paths = _find_keyframes(keyframes_dir)[: args.max_pairs]
    step_paths = _find_session_steps(args.session_dir)[: args.max_pairs]

    if not keyframe_paths:
        print(f"[ERROR] No kf-*.png files found in {keyframes_dir}")
        return
    if not step_paths:
        print(f"[ERROR] No step_*.png files found in {args.session_dir}")
        return

    output_path = args.output or Path(f"analysis/{app_name}_comparison.png")
    build_comparison(keyframe_paths, step_paths, output_path, app_name=app_name)


if __name__ == "__main__":
    main()
