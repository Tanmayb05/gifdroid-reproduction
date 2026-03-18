"""
Prepares app_<name> directories for GIFdroid by migrating to the expected structure:

  app_<name>/input/utg.json
  app_<name>/input/artifacts/artifacts_<N>.png  (1-based)
  app_<name>/input/screenrec/
  app_<name>/input/handheld/

Handles two cases:
  - Old structure: app_<name>/utg.json and app_<name>/artifacts/<N>.png
  - New structure: files already under app_<name>/input/ (validates/renames in place)
"""

import os
import glob
import shutil

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def _numeric_sort_key(p):
    name = os.path.splitext(os.path.basename(p))[0]
    try:
        return (0, int(name))
    except ValueError:
        return (1, name)


def prepare_app_dir(app_dir):
    app_name = os.path.basename(app_dir)
    print(f"\n[{app_name}]")

    input_dir = os.path.join(app_dir, "input")
    artifacts_input_dir = os.path.join(input_dir, "artifacts")
    screenrec_dir = os.path.join(input_dir, "screenrec")
    handheld_dir = os.path.join(input_dir, "handheld")

    # --- Detect old structure ---
    old_utg = os.path.join(app_dir, "utg.json")
    old_artifacts_dir = os.path.join(app_dir, "artifacts")
    has_old_utg = os.path.exists(old_utg)
    has_old_artifacts = os.path.isdir(old_artifacts_dir)

    if has_old_utg or has_old_artifacts:
        print(f"  Detected old structure. Migrating to input/...")
        os.makedirs(artifacts_input_dir, exist_ok=True)

        # Migrate utg.json
        if has_old_utg:
            dest_utg = os.path.join(input_dir, "utg.json")
            if os.path.exists(dest_utg):
                print(f"  utg.json: already exists in input/, skipping migration")
            else:
                shutil.move(old_utg, dest_utg)
                print(f"  utg.json: Moved app_<name>/utg.json -> input/utg.json")

        # Migrate artifacts
        if has_old_artifacts:
            png_files = glob.glob(os.path.join(old_artifacts_dir, "*.png"))
            # Separate already-prefixed from bare numeric
            prefixed = sorted([f for f in png_files if os.path.basename(f).startswith("artifacts_")])
            unprefixed = sorted([f for f in png_files if not os.path.basename(f).startswith("artifacts_")],
                                key=_numeric_sort_key)

            moved = 0
            renamed = 0

            # Move already-prefixed as-is
            for f in prefixed:
                dest = os.path.join(artifacts_input_dir, os.path.basename(f))
                shutil.move(f, dest)
                moved += 1

            # Rename unprefixed: <N>.png -> artifacts_<N+1>.png
            for f in unprefixed:
                name = os.path.splitext(os.path.basename(f))[0]
                try:
                    new_num = int(name) + 1
                except ValueError:
                    new_num = None

                if new_num is not None:
                    new_name = f"artifacts_{new_num}.png"
                else:
                    new_name = f"artifacts_{os.path.basename(f)}"

                dest = os.path.join(artifacts_input_dir, new_name)
                shutil.move(f, dest)
                renamed += 1

            if renamed > 0:
                print(f"  artifacts: Renamed and moved {renamed} file(s) to input/artifacts/artifacts_<N>.png")
            if moved > 0:
                print(f"  artifacts: Moved {moved} already-prefixed file(s) to input/artifacts/")

            # Remove old artifacts dir if now empty
            if not os.listdir(old_artifacts_dir):
                os.rmdir(old_artifacts_dir)
                print(f"  artifacts: Removed empty artifacts/ directory")
            else:
                remaining = os.listdir(old_artifacts_dir)
                print(f"  artifacts: WARNING — artifacts/ not empty after migration: {remaining}")

    # --- Ensure input/ subdirs exist ---
    os.makedirs(artifacts_input_dir, exist_ok=True)
    os.makedirs(screenrec_dir, exist_ok=True)
    os.makedirs(handheld_dir, exist_ok=True)

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

            if new_num is not None:
                new_name = f"artifacts_{new_num}.png"
            else:
                new_name = f"artifacts_{os.path.basename(f)}"

            os.rename(f, os.path.join(artifacts_input_dir, new_name))
            renamed += 1
        print(f"  input/artifacts: Renamed {renamed} unprefixed file(s) to artifacts_<N>.png format")
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

    if missing:
        print(f"  VALIDATION FAILED — missing: {', '.join(missing)}")
    else:
        print(f"  READY for GIFdroid")


def main():
    app_dirs = sorted(glob.glob(os.path.join(ROOT_DIR, "app_*")))
    app_dirs = [d for d in app_dirs if os.path.isdir(d)]

    if not app_dirs:
        print("No app_* directories found in:", ROOT_DIR)
        return

    print(f"Found {len(app_dirs)} app director(ies): {[os.path.basename(d) for d in app_dirs]}")

    for app_dir in app_dirs:
        prepare_app_dir(app_dir)

    print("\nDone.")


if __name__ == "__main__":
    main()
