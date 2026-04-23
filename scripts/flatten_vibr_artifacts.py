"""
Manage ViBR artifact directory structure.

Modes:
  flatten    step_N/<file> -> step_N_<file>  (nested dirs -> flat)
  categorize step_N_<file> -> <category>/step_N_<file>  (flat -> category folders)

Run in dry-run mode by default. Pass --apply to execute.

Usage:
  python3 scripts/flatten_vibr_artifacts.py flatten
  python3 scripts/flatten_vibr_artifacts.py flatten --apply
  python3 scripts/flatten_vibr_artifacts.py categorize
  python3 scripts/flatten_vibr_artifacts.py categorize --apply
"""

import argparse
import re
import shutil
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
APPS_DIR = PROJECT_ROOT / "apps"

STEP_DIR_RE = re.compile(r"^step_(\d+)$")
STEP_FILE_RE = re.compile(r"^step_\d+_(.+)$")

# Maps filename suffix (after step_N_) to target category folder name
CATEGORY_MAP = {
    "dino.png":             "dino",
    "labeled.png":          "labeled",
    "relevant_regions.png": "relevant_regions",
    "screenshot-0.png":     "screenshot",
    "tmp_start.png":        "tmp",
    "tmp_stop.png":         "tmp",
}


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

def find_artifact_dirs() -> list[Path]:
    return sorted(APPS_DIR.glob("*/llm/ViBR/*/run-*/artifacts"))


def move_file(src: Path, dst: Path, apply: bool) -> str | None:
    """Move src to dst. Returns an error string on failure, None on success."""
    if dst.exists():
        return f"destination already exists, skipping: {dst.relative_to(PROJECT_ROOT)}"
    print(f"  {'MOVE' if apply else 'dry'}: {src.relative_to(PROJECT_ROOT)} -> {dst.relative_to(PROJECT_ROOT)}")
    if apply:
        try:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dst))
        except Exception as e:
            return f"failed to move {src.relative_to(PROJECT_ROOT)}: {e}"
    return None


def iter_stem_dirs(artifacts_dir: Path) -> tuple[list[Path], list[str]]:
    """Return (stem_dirs, errors) for one artifacts/ directory."""
    errors = []
    if not artifacts_dir.exists():
        errors.append(f"[MISSING] {artifacts_dir.relative_to(PROJECT_ROOT)}")
        return [], errors
    if not artifacts_dir.is_dir():
        errors.append(f"[NOT A DIR] {artifacts_dir.relative_to(PROJECT_ROOT)}")
        return [], errors
    stem_dirs = sorted(d for d in artifacts_dir.iterdir() if d.is_dir())
    if not stem_dirs:
        print(f"  (no video stem dirs in {artifacts_dir.relative_to(PROJECT_ROOT)}, skipping)")
    return stem_dirs, errors


# ---------------------------------------------------------------------------
# Mode: flatten  (step_N/<file> -> step_N_<file>)
# ---------------------------------------------------------------------------

def flatten_stem_dir(stem_dir: Path, apply: bool) -> list[str]:
    errors = []
    step_dirs = sorted(
        (d for d in stem_dir.iterdir() if d.is_dir() and STEP_DIR_RE.match(d.name)),
        key=lambda d: int(STEP_DIR_RE.match(d.name).group(1)),
    )
    if not step_dirs:
        print(f"  (no step_N dirs in {stem_dir.relative_to(PROJECT_ROOT)}, skipping)")
        return errors

    for step_dir in step_dirs:
        for src in sorted(step_dir.iterdir()):
            if not src.is_file():
                errors.append(f"unexpected non-file inside {step_dir.relative_to(PROJECT_ROOT)}: {src.name}")
                continue
            dst = stem_dir / f"{step_dir.name}_{src.name}"
            err = move_file(src, dst, apply)
            if err:
                errors.append(err)

        if apply and step_dir.exists():
            remaining = list(step_dir.iterdir())
            if remaining:
                errors.append(f"dir not empty after moves, leaving it: {step_dir.relative_to(PROJECT_ROOT)}")
            else:
                try:
                    step_dir.rmdir()
                except Exception as e:
                    errors.append(f"failed to remove dir {step_dir.relative_to(PROJECT_ROOT)}: {e}")

    return errors


def run_flatten(apply: bool) -> list[str]:
    all_failures = []
    for artifacts_dir in find_artifact_dirs():
        print(f"\n[{artifacts_dir.relative_to(PROJECT_ROOT)}]")
        stem_dirs, errors = iter_stem_dirs(artifacts_dir)
        all_failures.extend(errors)
        for stem_dir in stem_dirs:
            print(f"\n  {stem_dir.relative_to(PROJECT_ROOT)}")
            errs = flatten_stem_dir(stem_dir, apply)
            all_failures.extend(f"{stem_dir.relative_to(PROJECT_ROOT)}: {e}" for e in errs)
    return all_failures


# ---------------------------------------------------------------------------
# Mode: categorize  (step_N_<file> -> <category>/step_N_<file>)
# ---------------------------------------------------------------------------

def categorize_stem_dir(stem_dir: Path, apply: bool) -> list[str]:
    errors = []
    flat_files = sorted(f for f in stem_dir.iterdir() if f.is_file() and STEP_FILE_RE.match(f.name))

    if not flat_files:
        print(f"  (no step_N_<file> files in {stem_dir.relative_to(PROJECT_ROOT)}, skipping)")
        return errors

    for src in flat_files:
        m = STEP_FILE_RE.match(src.name)
        suffix = m.group(1)
        category = CATEGORY_MAP.get(suffix)
        if category is None:
            errors.append(f"unrecognised suffix '{suffix}' for file {src.relative_to(PROJECT_ROOT)}, skipping")
            continue
        dst = stem_dir / category / src.name
        err = move_file(src, dst, apply)
        if err:
            errors.append(err)

    return errors


def run_categorize(apply: bool) -> list[str]:
    all_failures = []
    for artifacts_dir in find_artifact_dirs():
        print(f"\n[{artifacts_dir.relative_to(PROJECT_ROOT)}]")
        stem_dirs, errors = iter_stem_dirs(artifacts_dir)
        all_failures.extend(errors)
        for stem_dir in stem_dirs:
            print(f"\n  {stem_dir.relative_to(PROJECT_ROOT)}")
            errs = categorize_stem_dir(stem_dir, apply)
            all_failures.extend(f"{stem_dir.relative_to(PROJECT_ROOT)}: {e}" for e in errs)
    return all_failures


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("mode", choices=["flatten", "categorize"], help="flatten: step dirs -> flat files | categorize: flat files -> category folders")
    parser.add_argument("--apply", action="store_true", help="Actually move files (default is dry run)")
    args = parser.parse_args()

    run_label = "APPLY" if args.apply else "DRY RUN"
    print(f"=== flatten_vibr_artifacts.py [{args.mode}] [{run_label}] ===\n")

    artifact_dirs = find_artifact_dirs()
    if not artifact_dirs:
        print(f"No artifact directories found under {APPS_DIR}")
        sys.exit(0)

    if args.mode == "flatten":
        all_failures = run_flatten(args.apply)
    else:
        all_failures = run_categorize(args.apply)

    print(f"\n{'=' * 60}")
    if all_failures:
        print(f"FAILURES ({len(all_failures)}):")
        for f in all_failures:
            print(f"  {f}")
        sys.exit(1)
    else:
        print("Done. No failures.")
        if not args.apply:
            print("Re-run with --apply to execute.")


if __name__ == "__main__":
    main()
