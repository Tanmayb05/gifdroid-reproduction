"""
Flatten existing ViBR artifact directories from:
  artifacts/<video_stem>/step_N/<file>
to:
  artifacts/<video_stem>/step_N_<file>

Run in dry-run mode by default. Pass --apply to execute.
"""

import argparse
import re
import shutil
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
APPS_DIR = PROJECT_ROOT / "apps"

STEP_DIR_RE = re.compile(r"^step_(\d+)$")


def find_artifact_dirs() -> list[Path]:
    return sorted(APPS_DIR.glob("*/llm/ViBR/*/run-*/artifacts"))


def flatten_video_stem_dir(stem_dir: Path, apply: bool) -> list[str]:
    """
    Flatten one <video_stem> directory inside an artifacts/ dir.
    Returns a list of error strings (empty if all went well).
    """
    errors = []
    step_dirs = sorted(
        (d for d in stem_dir.iterdir() if d.is_dir() and STEP_DIR_RE.match(d.name)),
        key=lambda d: int(STEP_DIR_RE.match(d.name).group(1)),
    )

    if not step_dirs:
        return errors

    for step_dir in step_dirs:
        step_prefix = step_dir.name  # e.g. "step_0"
        for src in sorted(step_dir.iterdir()):
            if not src.is_file():
                errors.append(f"  unexpected non-file inside {step_dir}: {src.name}")
                continue
            dst = stem_dir / f"{step_prefix}_{src.name}"
            if dst.exists():
                errors.append(f"  destination already exists, skipping: {dst}")
                continue
            print(f"  {'MOVE' if apply else 'dry'}: {src.relative_to(PROJECT_ROOT)} -> {dst.relative_to(PROJECT_ROOT)}")
            if apply:
                try:
                    shutil.move(str(src), str(dst))
                except Exception as e:
                    errors.append(f"  failed to move {src}: {e}")
                    continue

        if apply and step_dir.exists():
            remaining = list(step_dir.iterdir())
            if remaining:
                errors.append(f"  dir not empty after moves, leaving it: {step_dir}")
            else:
                try:
                    step_dir.rmdir()
                except Exception as e:
                    errors.append(f"  failed to remove dir {step_dir}: {e}")

    return errors


def process_artifacts_dir(artifacts_dir: Path, apply: bool) -> list[str]:
    """
    Process one run's artifacts/ directory.
    Returns a list of (path, error) strings for failed items.
    """
    failures = []

    if not artifacts_dir.exists():
        failures.append(f"[MISSING] {artifacts_dir}")
        return failures

    if not artifacts_dir.is_dir():
        failures.append(f"[NOT A DIR] {artifacts_dir}")
        return failures

    stem_dirs = sorted(d for d in artifacts_dir.iterdir() if d.is_dir())

    if not stem_dirs:
        print(f"  (no video stem dirs in {artifacts_dir.relative_to(PROJECT_ROOT)}, skipping)")
        return failures

    for stem_dir in stem_dirs:
        step_dirs = [d for d in stem_dir.iterdir() if d.is_dir() and STEP_DIR_RE.match(d.name)]
        if not step_dirs:
            print(f"  (no step_N dirs in {stem_dir.relative_to(PROJECT_ROOT)}, skipping)")
            continue

        print(f"\n  {stem_dir.relative_to(PROJECT_ROOT)}")
        errors = flatten_video_stem_dir(stem_dir, apply=apply)
        for err in errors:
            failures.append(f"{stem_dir}: {err.strip()}")

    return failures


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="Actually move files (default is dry run)")
    args = parser.parse_args()

    apply = args.apply
    mode = "APPLY" if apply else "DRY RUN"
    print(f"=== flatten_vibr_artifacts.py [{mode}] ===\n")

    artifact_dirs = find_artifact_dirs()
    if not artifact_dirs:
        print(f"No artifact directories found under {APPS_DIR}")
        sys.exit(0)

    all_failures = []

    for artifacts_dir in artifact_dirs:
        print(f"\n[{artifacts_dir.relative_to(PROJECT_ROOT)}]")
        failures = process_artifacts_dir(artifacts_dir, apply=apply)
        all_failures.extend(failures)

    print(f"\n{'=' * 60}")
    if all_failures:
        print(f"FAILURES ({len(all_failures)}):")
        for f in all_failures:
            print(f"  {f}")
        sys.exit(1)
    else:
        action = "moved" if apply else "would move"
        print(f"Done. No failures.")
        if not apply:
            print("Re-run with --apply to execute.")


if __name__ == "__main__":
    main()
