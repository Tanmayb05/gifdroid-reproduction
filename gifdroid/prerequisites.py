"""
prerequisites.py — GIFdroid pre-run setup script

Usage:
    python gifdroid/prerequisites.py                           # checks + generate commands.txt for all utg slots
    python gifdroid/prerequisites.py --handheld                # also converts MOV -> mp4
    python gifdroid/prerequisites.py --app SimpleNotes         # single app, all utg slots
    python gifdroid/prerequisites.py --utg utg02               # all apps, specific utg slot
    python gifdroid/prerequisites.py --handheld --app SimpleNotes --utg utg01
"""

import argparse
import glob
import os
import shutil
import subprocess
import sys
import time


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def find_utg_dirs(root, app_filter=None, utg_filter=None):
    """Return sorted list of app_*/utg*/ directories under root."""
    utg_dirs = []
    for app_dir in sorted(glob.glob(os.path.join(root, "app_*"))):
        if not os.path.isdir(app_dir):
            continue
        if app_filter and os.path.basename(app_dir) != f"app_{app_filter}":
            continue
        for utg_dir in sorted(glob.glob(os.path.join(app_dir, "utg*"))):
            if not os.path.isdir(utg_dir):
                continue
            if utg_filter and os.path.basename(utg_dir) != utg_filter:
                continue
            utg_dirs.append(utg_dir)

    if not utg_dirs:
        filters = []
        if app_filter:
            filters.append(f"app={app_filter}")
        if utg_filter:
            filters.append(f"utg={utg_filter}")
        desc = ", ".join(filters) if filters else "any"
        print(f"[ERROR] No app_*/utg*/ directories found matching: {desc}")
        sys.exit(1)

    return utg_dirs


def app_name_from_utg_dir(utg_dir):
    """Extract app name from app_<name>/utg<NN> path."""
    basename = os.path.basename(os.path.dirname(utg_dir))
    return basename[len("app_"):] if basename.startswith("app_") else basename


def utg_id_from_dir(utg_dir):
    """Return the utg slot name, e.g. 'utg01'."""
    return os.path.basename(utg_dir)


# ---------------------------------------------------------------------------
# Check 1: ffmpeg
# ---------------------------------------------------------------------------

def check_ffmpeg():
    if shutil.which("ffmpeg") is None:
        print("[WARNING] ffmpeg not found in PATH. Handheld MOV -> mp4 conversion will fail.")
        return False
    print("[OK] ffmpeg found.")
    return True


# ---------------------------------------------------------------------------
# Check 2: Python dependencies
# ---------------------------------------------------------------------------

def check_dependencies():
    required = {
        "cv2": "opencv-python / opencv-contrib-python",
        "numpy": "numpy",
        "skimage": "scikit-image",
        "sklearn": "scikit-learn",
        "matplotlib": "matplotlib",
    }
    missing = []
    for module, pkg in required.items():
        try:
            __import__(module)
        except ImportError:
            missing.append(pkg)

    if missing:
        print(f"[WARNING] Missing Python packages: {', '.join(missing)}")
        print("         Run: pip install -r gifdroid/requirements.txt")
    else:
        print("[OK] All Python dependencies found.")


# ---------------------------------------------------------------------------
# Check 3: UTG directory structure + output dir creation
# ---------------------------------------------------------------------------

def check_utg_structure(utg_dirs):
    all_ok = True
    for utg_dir in utg_dirs:
        name = app_name_from_utg_dir(utg_dir)
        utg_id = utg_id_from_dir(utg_dir)
        label = f"{name} [{utg_id}]"

        utg_json = os.path.join(utg_dir, "input", "utg.json")
        artifacts = os.path.join(utg_dir, "input", "artifacts")
        output_dir = os.path.join(utg_dir, "output")

        issues = []
        if not os.path.isfile(utg_json):
            issues.append("missing input/utg.json")
        if not os.path.isdir(artifacts) or not glob.glob(os.path.join(artifacts, "*.png")):
            issues.append("missing or empty input/artifacts/")

        os.makedirs(output_dir, exist_ok=True)

        if issues:
            print(f"[WARNING] {label}: {', '.join(issues)}")
            all_ok = False
        else:
            print(f"[OK] {label}: structure valid, output dir ready ({output_dir})")

    return all_ok


# ---------------------------------------------------------------------------
# Handheld MOV -> mp4 conversion
# ---------------------------------------------------------------------------

def get_video_resolution(mov_path):
    """Use ffprobe to get WxH of source video."""
    result = subprocess.run(
        [
            "ffprobe", "-v", "error",
            "-select_streams", "v:0",
            "-show_entries", "stream=width,height",
            "-of", "csv=p=0",
            mov_path,
        ],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    out = result.stdout.decode("utf-8").strip()
    if not out:
        return None, None
    parts = out.split(",")
    if len(parts) == 2:
        return parts[0].strip(), parts[1].strip()
    return None, None


def convert_handheld(utg_dirs):
    print("\n--- Handheld MOV -> mp4 conversion ---")
    for utg_dir in utg_dirs:
        name = app_name_from_utg_dir(utg_dir)
        utg_id = utg_id_from_dir(utg_dir)
        label = f"{name} [{utg_id}]"
        handheld_dir = os.path.join(utg_dir, "input", "handheld")
        mov_path = os.path.join(handheld_dir, f"hhv_app_{name}.MOV")
        mp4_path = os.path.join(handheld_dir, f"hhv_app_{name}.mp4")

        if not os.path.isfile(mov_path):
            print(f"[SKIP] {label}: hhv_app_{name}.MOV not found, skipping handheld conversion.")
            continue

        if os.path.isfile(mp4_path) and os.path.getmtime(mp4_path) >= os.path.getmtime(mov_path):
            print(f"[SKIP] {label}: converted mp4 already up to date.")
            continue

        width, height = get_video_resolution(mov_path)
        if width is None:
            print(f"[WARNING] {label}: could not determine resolution, using source as-is scale.")
            scale_filter = "format=yuv420p"
        else:
            scale_filter = f"scale={width}:{height},format=yuv420p"

        print(f"[CONVERT] {label}: {mov_path} -> {mp4_path} ({width}x{height})")
        t_start = time.time()
        result = subprocess.run(
            [
                "ffmpeg", "-i", mov_path,
                "-vf", scale_filter,
                "-c:v", "libx264",
                "-pix_fmt", "yuv420p",
                "-color_range", "1",
                "-colorspace", "bt709",
                "-color_trc", "bt709",
                "-color_primaries", "bt709",
                mp4_path, "-y",
            ],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        elapsed = time.time() - t_start
        if result.returncode == 0:
            print("[OK] %s: conversion successful. (%.1fs)" % (label, elapsed))
        else:
            print("[ERROR] %s: ffmpeg failed after %.1fs.\n%s" % (label, elapsed, result.stderr.decode("utf-8")[-500:]))


# ---------------------------------------------------------------------------
# Generate commands.txt
# ---------------------------------------------------------------------------

def generate_commands(utg_dirs, root, include_handheld):
    lines = []
    lines.append("# GIFdroid run commands")
    lines.append("# Run from the project root: " + root)
    lines.append("")

    for utg_dir in utg_dirs:
        name = app_name_from_utg_dir(utg_dir)
        utg_id = utg_id_from_dir(utg_dir)
        utg_json = os.path.join(utg_dir, "input", "utg.json")
        artifacts = os.path.join(utg_dir, "input", "artifacts")

        # Screen-recorded video
        srv_path = os.path.join(utg_dir, "input", "screenrec", f"srv_app_{name}.mp4")
        if os.path.isfile(srv_path):
            out = os.path.join(utg_dir, "output", f"execution_srv_{name}.json")
            lines.append(f"# {name} [{utg_id}] — screen recording")
            lines.append(
                f"python -m gifdroid.main"
                f" --video {srv_path}"
                f" --utg {utg_json}"
                f" --artifact {artifacts}"
                f" --out {out}"
            )
            lines.append("")
        else:
            lines.append(f"# {name} [{utg_id}] — screen recording: srv_app_{name}.mp4 not found, skipped")
            lines.append("")

        # Handheld video
        if include_handheld:
            mp4_path = os.path.join(utg_dir, "input", "handheld", f"hhv_app_{name}.mp4")
            mov_path = os.path.join(utg_dir, "input", "handheld", f"hhv_app_{name}.MOV")
            if os.path.isfile(mp4_path):
                out = os.path.join(utg_dir, "output", f"execution_hhv_{name}.json")
                lines.append(f"# {name} [{utg_id}] — handheld")
                lines.append(
                    f"python -m gifdroid.main"
                    f" --video {mp4_path}"
                    f" --utg {utg_json}"
                    f" --artifact {artifacts}"
                    f" --out {out}"
                )
                lines.append("")
            elif os.path.isfile(mov_path):
                lines.append(f"# {name} [{utg_id}] — handheld: MOV found but not yet converted to mp4, skipped")
                lines.append("")
            else:
                lines.append(f"# {name} [{utg_id}] — handheld: hhv_app_{name}.MOV not found, skipped")
                lines.append("")

    commands_path = os.path.join(root, "gifdroid_analyse", "commands.txt")
    with open(commands_path, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"\n[OK] commands.txt written to: {commands_path}")
    print("\n" + "\n".join(lines))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def parse_args():
    parser = argparse.ArgumentParser(description="GIFdroid prerequisites checker and command generator")
    parser.add_argument("--handheld", action="store_true",
                        help="Convert handheld MOV videos to mp4 and include handheld commands")
    parser.add_argument("--app", type=str, default=None,
                        help="Process a single app by name (e.g. SimpleNotes)")
    parser.add_argument("--utg", type=str, default=None,
                        help="Process a single UTG slot (e.g. utg01 or utg02)")
    return parser.parse_args()


def main():
    args = parse_args()

    # Root is two levels up from this file (gifdroid/prerequisites.py -> project root)
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    print(f"Project root: {root}\n")

    print("--- Dependency checks ---")
    check_ffmpeg()
    check_dependencies()

    utg_dirs = find_utg_dirs(root, app_filter=args.app, utg_filter=args.utg)
    print(f"\n--- UTG structure check ({len(utg_dirs)} slot(s)) ---")
    check_utg_structure(utg_dirs)

    if args.handheld:
        convert_handheld(utg_dirs)

    print("\n--- Generating commands.txt ---")
    generate_commands(utg_dirs, root, include_handheld=args.handheld)


if __name__ == "__main__":
    main()