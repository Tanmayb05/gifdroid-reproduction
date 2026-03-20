"""
Prepares app_<name>/<utg_id>/ directories for GIFdroid.

Expected final structure per UTG slot:

  app_<name>/<utg_id>/input/utg.json
  app_<name>/<utg_id>/input/artifacts/artifacts_<N>.png  (1-based)
  app_<name>/<utg_id>/input/screenrec/
  app_<name>/<utg_id>/input/handheld/
  app_<name>/<utg_id>/output/

Handles:
  - Files dropped directly in <utg_id>/ (utg.json, artifacts/) — migrates into input/
  - Files already under <utg_id>/input/ — validates and renames unprefixed PNGs in place

Usage:
    python prepare_app_dirs.py                        # all apps, all utg slots
    python prepare_app_dirs.py --app HomeMedkit       # single app, all utg slots
    python prepare_app_dirs.py --utg utg02            # all apps, specific utg slot
    python prepare_app_dirs.py --app HomeMedkit --utg utg02
"""

import argparse
import os
import glob
import shutil
import sys

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def _numeric_sort_key(p):
    name = os.path.splitext(os.path.basename(p))[0]
    try:
        return (0, int(name))
    except ValueError:
        return (1, name)


def prepare_utg_dir(utg_dir):
    app_name = os.path.basename(os.path.dirname(utg_dir))
    utg_id = os.path.basename(utg_dir)
    label = f"{app_name}/{utg_id}"
    print(f"\n[{label}]")

    input_dir = os.path.join(utg_dir, "input")
    artifacts_input_dir = os.path.join(input_dir, "artifacts")
    screenrec_dir = os.path.join(input_dir, "screenrec")
    handheld_dir = os.path.join(input_dir, "handheld")
    output_dir = os.path.join(utg_dir, "output")

    # --- Detect files dropped directly in utg_dir (without input/ sub-folder) ---
    old_utg = os.path.join(utg_dir, "utg.json")
    old_artifacts_dir = os.path.join(utg_dir, "artifacts")
    has_old_utg = os.path.exists(old_utg)
    has_old_artifacts = os.path.isdir(old_artifacts_dir)

    if has_old_utg or has_old_artifacts:
        print(f"  Detected files directly in {utg_id}/. Migrating into input/...")
        os.makedirs(artifacts_input_dir, exist_ok=True)

        # Migrate utg.json
        if has_old_utg:
            dest_utg = os.path.join(input_dir, "utg.json")
            if os.path.exists(dest_utg):
                print(f"  utg.json: already exists in input/, skipping migration")
            else:
                shutil.move(old_utg, dest_utg)
                print(f"  utg.json: moved {utg_id}/utg.json -> {utg_id}/input/utg.json")

        # Migrate artifacts
        if has_old_artifacts:
            png_files = glob.glob(os.path.join(old_artifacts_dir, "*.png"))
            prefixed = sorted([f for f in png_files if os.path.basename(f).startswith("artifacts_")])
            unprefixed = sorted(
                [f for f in png_files if not os.path.basename(f).startswith("artifacts_")],
                key=_numeric_sort_key,
            )

            moved = 0
            renamed = 0

            for f in prefixed:
                dest = os.path.join(artifacts_input_dir, os.path.basename(f))
                shutil.move(f, dest)
                moved += 1

            for f in unprefixed:
                name = os.path.splitext(os.path.basename(f))[0]
                try:
                    new_num = int(name) + 1
                except ValueError:
                    new_num = None
                new_name = f"artifacts_{new_num}.png" if new_num is not None else f"artifacts_{os.path.basename(f)}"
                shutil.move(f, os.path.join(artifacts_input_dir, new_name))
                renamed += 1

            if renamed > 0:
                print(f"  artifacts: renamed and moved {renamed} file(s) to input/artifacts/artifacts_<N>.png")
            if moved > 0:
                print(f"  artifacts: moved {moved} already-prefixed file(s) to input/artifacts/")

            if not os.listdir(old_artifacts_dir):
                os.rmdir(old_artifacts_dir)
                print(f"  artifacts: removed empty artifacts/ directory")
            else:
                print(f"  artifacts: WARNING — artifacts/ not empty after migration: {os.listdir(old_artifacts_dir)}")

    # --- Ensure all required subdirs exist ---
    os.makedirs(artifacts_input_dir, exist_ok=True)
    os.makedirs(screenrec_dir, exist_ok=True)
    os.makedirs(handheld_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    # --- Rename any unprefixed PNGs already in input/artifacts/ ---
    existing_pngs = glob.glob(os.path.join(artifacts_input_dir, "*.png"))
    unprefixed_in_input = sorted(
        [f for f in existing_pngs if not os.path.basename(f).startswith("artifacts_")],
        key=_numeric_sort_key,
    )
    if unprefixed_in_input:
        renamed = 0
        for f in unprefixed_in_input:
            name = os.path.splitext(os.path.basename(f))[0]
            try:
                new_num = int(name) + 1
            except ValueError:
                new_num = None
            new_name = f"artifacts_{new_num}.png" if new_num is not None else f"artifacts_{os.path.basename(f)}"
            os.rename(f, os.path.join(artifacts_input_dir, new_name))
            renamed += 1
        print(f"  input/artifacts: renamed {renamed} unprefixed file(s) to artifacts_<N>.png format")
    else:
        skipped = len([f for f in existing_pngs if os.path.basename(f).startswith("artifacts_")])
        if skipped > 0:
            print(f"  input/artifacts: {skipped} file(s) already correctly named, skipped")
        elif not has_old_artifacts:
            print(f"  input/artifacts: WARNING — no .png files found")

    # --- Final validation ---
    missing = []
    if not os.path.exists(os.path.join(input_dir, "utg.json")):
        missing.append("input/utg.json")
    if not os.path.isdir(artifacts_input_dir):
        missing.append("input/artifacts/")
    if not os.path.isdir(screenrec_dir):
        missing.append("input/screenrec/")
    if not os.path.isdir(handheld_dir):
        missing.append("input/handheld/")
    if not os.path.isdir(output_dir):
        missing.append("output/")

    if missing:
        print(f"  VALIDATION FAILED — missing: {', '.join(missing)}")
    else:
        print(f"  READY for GIFdroid")


def find_utg_dirs(root, app_filter=None, utg_filter=None):
    """Return sorted list of app_*/utg*/ dirs under root."""
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
    return utg_dirs


def parse_args():
    parser = argparse.ArgumentParser(description="Prepare app_*/utg*/ directories for GIFdroid")
    parser.add_argument("--app", type=str, default=None,
                        help="Process a single app by name (e.g. HomeMedkit)")
    parser.add_argument("--utg", type=str, default=None,
                        help="Process a single UTG slot (e.g. utg01 or utg02)")
    return parser.parse_args()


def main():
    args = parse_args()
    utg_dirs = find_utg_dirs(ROOT_DIR, app_filter=args.app, utg_filter=args.utg)

    if not utg_dirs:
        print("No app_*/utg*/ directories found matching filters.")
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