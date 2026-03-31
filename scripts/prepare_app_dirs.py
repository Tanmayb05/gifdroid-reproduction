"""
Prepares apps/<name>/utgs/<utg-id>/ directories for GIFdroid.

Expected final structure per UTG slot:

  apps/<name>/videos/handheld/hhv-001.mp4
  apps/<name>/videos/screenrec/srv-001.mp4
  apps/<name>/utgs/<utg-id>/input/utg.json
  apps/<name>/utgs/<utg-id>/input/artifacts/artifact-001.png

Handles:
  - Renames unprefixed PNGs in artifacts/ to artifact-NNN.png (1-based, 3-digit)
  - Ensures all required subdirs exist

Usage:
    python scripts/prepare_app_dirs.py                        # all apps, all utg slots
    python scripts/prepare_app_dirs.py --app homemedkit       # single app, all utg slots
    python scripts/prepare_app_dirs.py --utg utg-02           # all apps, specific utg slot
    python scripts/prepare_app_dirs.py --app homemedkit --utg utg-02
"""

import argparse
import os
import glob
import shutil
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _numeric_sort_key(p):
    name = os.path.splitext(os.path.basename(p))[0]
    # Strip any non-numeric prefix (e.g. "artifact-", "artifacts_")
    import re
    m = re.search(r"(\d+)$", name)
    try:
        return (0, int(m.group(1))) if m else (1, name)
    except (ValueError, AttributeError):
        return (1, name)


def prepare_utg_dir(utg_dir):
    # utg_dir = apps/<name>/utgs/<utg-id>
    app_name = os.path.basename(os.path.dirname(os.path.dirname(utg_dir)))
    utg_id = os.path.basename(utg_dir)
    label = f"{app_name}/{utg_id}"
    print(f"\n[{label}]")

    input_dir = os.path.join(utg_dir, "input")
    artifacts_dir = os.path.join(input_dir, "artifacts")
    app_root = os.path.dirname(os.path.dirname(utg_dir))  # apps/<name>
    handheld_dir = os.path.join(app_root, "videos", "handheld")
    screenrec_dir = os.path.join(app_root, "videos", "screenrec")

    # Ensure required directories exist
    os.makedirs(artifacts_dir, exist_ok=True)
    os.makedirs(handheld_dir, exist_ok=True)
    os.makedirs(screenrec_dir, exist_ok=True)

    # Rename artifacts to artifact-NNN.png format
    existing_pngs = glob.glob(os.path.join(artifacts_dir, "*.png"))
    import re
    already_named = [f for f in existing_pngs if re.match(r"artifact-\d{3}\.png$", os.path.basename(f))]
    needs_rename = [f for f in existing_pngs if f not in already_named]

    if needs_rename:
        needs_rename_sorted = sorted(needs_rename, key=_numeric_sort_key)
        renamed = 0
        for i, f in enumerate(needs_rename_sorted, start=len(already_named) + 1):
            new_name = f"artifact-{i:03d}.png"
            new_path = os.path.join(artifacts_dir, new_name)
            if not os.path.exists(new_path):
                os.rename(f, new_path)
                renamed += 1
        if renamed:
            print(f"  input/artifacts: renamed {renamed} file(s) to artifact-NNN.png format")
    else:
        skipped = len(already_named)
        if skipped > 0:
            print(f"  input/artifacts: {skipped} file(s) already correctly named, skipped")
        elif not existing_pngs:
            print(f"  input/artifacts: WARNING — no .png files found")

    # Final validation
    missing = []
    if not os.path.exists(os.path.join(input_dir, "utg.json")):
        missing.append("input/utg.json")
    if not os.path.isdir(artifacts_dir):
        missing.append("input/artifacts/")
    if not os.path.isdir(handheld_dir):
        missing.append("videos/handheld/")
    if not os.path.isdir(screenrec_dir):
        missing.append("videos/screenrec/")

    if missing:
        print(f"  VALIDATION FAILED — missing: {', '.join(missing)}")
    else:
        print(f"  READY for GIFdroid")


def find_utg_dirs(root, app_filter=None, utg_filter=None):
    """Return sorted list of apps/*/utgs/utg-*/ dirs under root."""
    utg_dirs = []
    apps_root = os.path.join(root, "apps")
    for app_dir in sorted(glob.glob(os.path.join(apps_root, "*"))):
        if not os.path.isdir(app_dir):
            continue
        app_basename = os.path.basename(app_dir)
        if app_filter and app_basename.lower() != app_filter.lower():
            continue
        utgs_dir = os.path.join(app_dir, "utgs")
        for utg_dir in sorted(glob.glob(os.path.join(utgs_dir, "utg-*"))):
            if not os.path.isdir(utg_dir):
                continue
            if utg_filter and os.path.basename(utg_dir) != utg_filter:
                continue
            utg_dirs.append(utg_dir)
    return utg_dirs


def parse_args():
    parser = argparse.ArgumentParser(description="Prepare apps/*/utgs/utg-*/ directories for GIFdroid")
    parser.add_argument("--app", type=str, default=None,
                        help="Process a single app by name (e.g. homemedkit)")
    parser.add_argument("--utg", type=str, default=None,
                        help="Process a single UTG slot (e.g. utg-01 or utg-02)")
    return parser.parse_args()


def main():
    args = parse_args()
    utg_dirs = find_utg_dirs(ROOT_DIR, app_filter=args.app, utg_filter=args.utg)

    if not utg_dirs:
        print("No apps/*/utgs/utg-*/ directories found matching filters.")
        sys.exit(1)

    print(f"Found {len(utg_dirs)} utg slot(s):")
    for d in utg_dirs:
        rel = os.path.relpath(d, ROOT_DIR)
        print(f"  {rel}")

    for utg_dir in utg_dirs:
        prepare_utg_dir(utg_dir)

    print("\nDone.")


if __name__ == "__main__":
    main()
