"""
evaluate_handheld.py

Evaluates GIFdroid's keyframe extraction and GUI mapping pipeline
on a handheld (real-world camera) video recording.

Phases:
  Phase 1 — Extract keyframes from handheld video using SSIM (location.py)
             Saves frames to: app_<App>/handheld/handheld_keyframes_auto/
  Phase 2 — Map keyframes to UTG artifacts using ORB+SSIM (mapping.py)
             Prints match results and scores for robustness analysis
  Phase 2B (optional) — Same mapping but using manually captured photos
             Reads from: app_<App>/handheld/handheld_keyframes_manual/

Usage:
  # Phase 1 + 2A (auto keyframes from handheld video):
  python evaluate_handheld.py \\
      --video   app_AdAway/handheld/handheld_video_AdAway.mp4 \\
      --artifact app_AdAway/artifacts \\
      --app     AdAway

  # Phase 2B only (manually captured keyframe photos):
  python evaluate_handheld.py \\
      --manual  app_AdAway/handheld/handheld_keyframes_manual \\
      --artifact app_AdAway/artifacts \\
      --app     AdAway

  # Skip extraction, re-run mapping on previously extracted auto keyframes:
  python evaluate_handheld.py \\
      --auto    app_AdAway/handheld/handheld_keyframes_auto \\
      --artifact app_AdAway/artifacts \\
      --app     AdAway
"""

import argparse
import glob
import os
import sys
import cv2

# Allow importing from gifdroid/ subfolder
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'gifdroid'))

from location import keyframe_location
from mapping import load_screenshots, mapping_with_scores


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def save_keyframes(keyframes, out_dir, prefix='handheld_keyframe_auto'):
    """Save a list of OpenCV frames to out_dir with zero-padded filenames."""
    os.makedirs(out_dir, exist_ok=True)
    paths = []
    for i, frame in enumerate(keyframes, start=1):
        filename = f'{prefix}_{i:02d}.png'
        path = os.path.join(out_dir, filename)
        cv2.imwrite(path, frame)
        paths.append(path)
    return paths


def load_images_from_dir(directory, extensions=('*.png', '*.jpg', '*.jpeg')):
    """Load all images from a directory, sorted by filename."""
    paths = []
    for ext in extensions:
        paths.extend(glob.glob(os.path.join(directory, ext)))
    paths = sorted(paths)
    images = []
    for p in paths:
        img = cv2.imread(p)
        if img is not None:
            images.append((os.path.basename(p), img))
    return images


def run_mapping(images, artifact_dir):
    """
    Map a list of (filename, frame) pairs against UTG artifacts.

    Returns a list of dicts:
      {
        'keyframe':      original filename,
        'best_match':    artifacts_<N>.png,
        'best_score':    float,
        'runner_up':     artifacts_<M>.png,
        'runner_up_score': float,
        'score_gap':     best - runner_up (higher = more confident),
      }
    """
    index, size = load_screenshots(artifact_dir)
    results = []
    for kf_name, frame in images:
        best_match, scores = mapping_with_scores(frame, index, size)
        best_score = scores[0][0]
        runner_up, runner_up_score = (scores[1][1], scores[1][0]) if len(scores) > 1 else (None, 0.0)
        results.append({
            'keyframe':        kf_name,
            'best_match':      best_match,
            'best_score':      best_score,
            'runner_up':       runner_up,
            'runner_up_score': runner_up_score,
            'score_gap':       best_score - runner_up_score,
        })
    return results


def print_mapping_results(results, label):
    print()
    print(f'{"=" * 60}')
    print(f'  MAPPING RESULTS — {label}')
    print(f'{"=" * 60}')
    print(f'  {"Keyframe":<35} {"Best Match":<20} {"Score":>6}  {"Gap":>6}  Runner-up')
    print(f'  {"-"*35} {"-"*20} {"-"*6}  {"-"*6}  {"-"*20}')
    for r in results:
        print(
            f'  {r["keyframe"]:<35} {r["best_match"]:<20} '
            f'{r["best_score"]:>6.3f}  {r["score_gap"]:>6.3f}  {r["runner_up"]}'
        )
    print()
    avg_score = sum(r['best_score'] for r in results) / len(results) if results else 0
    avg_gap   = sum(r['score_gap']  for r in results) / len(results) if results else 0
    print(f'  Average best score : {avg_score:.3f}')
    print(f'  Average score gap  : {avg_gap:.3f}')
    print(f'  (Higher gap = more confident match)')
    print()


# ---------------------------------------------------------------------------
# Phase 1: Extract keyframes from handheld video
# ---------------------------------------------------------------------------

def phase1_extract(video_path, app_name):
    print()
    print('=' * 60)
    print('  PHASE 1: Keyframe Extraction from Handheld Video (SSIM)')
    print(f'  Input : {video_path}')

    keyframes, keyframe_indices = keyframe_location(video_path)

    out_dir = os.path.join(os.path.dirname(video_path), 'handheld_keyframes_auto')
    saved_paths = save_keyframes(keyframes, out_dir, prefix='handheld_keyframe_auto')

    print(f'  Keyframes found  : {len(keyframes)}')
    print(f'  Frame indices    : {keyframe_indices}')
    print(f'  Saved to         : {out_dir}')
    for p in saved_paths:
        print(f'    {os.path.basename(p)}')

    return keyframes, keyframe_indices, out_dir


# ---------------------------------------------------------------------------
# Phase 2A: Map auto-extracted keyframes
# ---------------------------------------------------------------------------

def phase2a_map_auto(keyframes_or_dir, artifact_dir):
    print()
    print('=' * 60)
    print('  PHASE 2A: ORB+SSIM Mapping — Auto Keyframes')
    print(f'  Artifacts dir : {artifact_dir}')

    if isinstance(keyframes_or_dir, str):
        images = load_images_from_dir(keyframes_or_dir)
        print(f'  Loaded {len(images)} keyframes from {keyframes_or_dir}')
    else:
        # Raw OpenCV frames passed directly
        images = [(f'handheld_keyframe_auto_{i+1:02d}.png', f) for i, f in enumerate(keyframes_or_dir)]

    results = run_mapping(images, artifact_dir)
    print_mapping_results(results, 'Auto Keyframes (Handheld Video)')
    return results


# ---------------------------------------------------------------------------
# Phase 2B: Map manually captured keyframe photos
# ---------------------------------------------------------------------------

def phase2b_map_manual(manual_dir, artifact_dir):
    print()
    print('=' * 60)
    print('  PHASE 2B: ORB+SSIM Mapping — Manual Keyframe Photos')
    print(f'  Manual dir    : {manual_dir}')
    print(f'  Artifacts dir : {artifact_dir}')

    images = load_images_from_dir(manual_dir)
    if not images:
        print(f'  ERROR: No images found in {manual_dir}')
        print(f'  Place your manually captured photos there as:')
        print(f'    handheld_keyframe_manual_01.jpg, _02.jpg, ...')
        return []

    print(f'  Loaded {len(images)} manual keyframes')
    results = run_mapping(images, artifact_dir)
    print_mapping_results(results, 'Manual Keyframe Photos')
    return results


# ---------------------------------------------------------------------------
# Argument parsing
# ---------------------------------------------------------------------------

def parse_args():
    parser = argparse.ArgumentParser(
        description='Evaluate GIFdroid keyframe extraction + mapping on handheld video/photos'
    )
    parser.add_argument('--app',      required=True, help='App name, e.g. AdAway')
    parser.add_argument('--artifact', required=True, help='Path to UTG artifacts dir (artifacts_*.png)')

    source = parser.add_mutually_exclusive_group()
    source.add_argument('--video',  help='Handheld video: handheld_video_<App>.mp4 (runs Phase 1 + 2A)')
    source.add_argument('--auto',   help='Dir of already-extracted auto keyframes (runs Phase 2A only)')
    source.add_argument('--manual', help='Dir of manually captured keyframe photos (runs Phase 2B only)')

    return parser.parse_args()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    args = parse_args()

    if args.video:
        keyframes, _, _ = phase1_extract(args.video, args.app)
        print()
        print('  Inspect handheld_keyframes_auto/ — do the frames look correct?')
        print('  If yes, mapping proceeds automatically below.')
        print('  If no,  re-run with --manual to use your own photos instead.')
        phase2a_map_auto(keyframes, args.artifact)

    elif args.auto:
        phase2a_map_auto(args.auto, args.artifact)

    elif args.manual:
        phase2b_map_manual(args.manual, args.artifact)

    else:
        print('Provide one of: --video, --auto, or --manual')
        print('Run with -h for full usage.')
        sys.exit(1)