"""
Prepares app_<name> directories for GIFdroid by renaming files to the expected format:
  - Any *.mp4  -> app_<app_name>.mp4
  - Any *.json -> utg.json
  - artifacts/<N>.png -> artifacts/artifacts_<N>.png
"""

import os
import glob

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def prepare_app_dir(app_dir):
    app_name = os.path.basename(app_dir)
    print(f"\n[{app_name}]")

    # --- Rename .mp4 ---
    expected_mp4 = os.path.join(app_dir, f"{app_name}.mp4")
    if os.path.exists(expected_mp4):
        print(f"  mp4: already correctly named ({app_name}.mp4)")
    else:
        mp4_files = [f for f in glob.glob(os.path.join(app_dir, "*.mp4"))
                     if os.path.basename(f) != f"{app_name}.mp4"]
        if len(mp4_files) == 0:
            print(f"  mp4: WARNING — no .mp4 file found, skipping rename")
        elif len(mp4_files) > 1:
            print(f"  mp4: WARNING — multiple .mp4 files found, skipping rename (ambiguous): {[os.path.basename(f) for f in mp4_files]}")
        else:
            os.rename(mp4_files[0], expected_mp4)
            print(f"  mp4: Renamed '{os.path.basename(mp4_files[0])}' -> '{app_name}.mp4'")

    # --- Rename .json -> utg.json ---
    expected_json = os.path.join(app_dir, "utg.json")
    if os.path.exists(expected_json):
        print(f"  json: already correctly named (utg.json)")
    else:
        json_files = [f for f in glob.glob(os.path.join(app_dir, "*.json"))
                      if os.path.basename(f) != "utg.json"]
        if len(json_files) == 0:
            print(f"  json: WARNING — no .json file found, skipping rename")
        elif len(json_files) > 1:
            print(f"  json: WARNING — multiple .json files found, skipping rename (ambiguous): {[os.path.basename(f) for f in json_files]}")
        else:
            os.rename(json_files[0], expected_json)
            print(f"  json: Renamed '{os.path.basename(json_files[0])}' -> 'utg.json'")

    # --- Rename artifacts/<N>.png -> artifacts/artifacts_<N>.png ---
    artifacts_dir = os.path.join(app_dir, "artifacts")
    if not os.path.isdir(artifacts_dir):
        print(f"  artifacts: WARNING — no artifacts/ directory found")
        return

    renamed = 0
    skipped = 0
    for f in glob.glob(os.path.join(artifacts_dir, "*.png")):
        filename = os.path.basename(f)
        # Skip files already prefixed with artifacts_
        if filename.startswith("artifacts_"):
            skipped += 1
            continue
        new_name = f"artifacts_{filename}"
        os.rename(f, os.path.join(artifacts_dir, new_name))
        renamed += 1

    if renamed == 0 and skipped == 0:
        print(f"  artifacts: WARNING — no .png files found in artifacts/")
    else:
        if renamed > 0:
            print(f"  artifacts: Renamed {renamed} file(s) to artifacts_<N>.png format")
        if skipped > 0:
            print(f"  artifacts: {skipped} file(s) already correctly named, skipped")

    # --- Final validation ---
    missing = []
    if not os.path.exists(expected_mp4):
        missing.append(f"{app_name}.mp4")
    if not os.path.exists(expected_json):
        missing.append("utg.json")
    if not os.path.isdir(artifacts_dir):
        missing.append("artifacts/")

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
