"""
migrate_to_new_structure.py — Migrate existing app_*/utg*/ data to apps/*/utgs/utg-*/ structure.

Non-destructive: copies/moves data to new paths without deleting old directories.
Idempotent: skips files that already exist at the destination.

Usage:
    python scripts/migrate_to_new_structure.py --dry-run       # preview only
    python scripts/migrate_to_new_structure.py                 # execute migration
    python scripts/migrate_to_new_structure.py --app AdAway    # single app
    python scripts/migrate_to_new_structure.py --utg utg01     # single utg slot
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

ROOT_DIR = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

APP_NAME_MAP = {
    "adaway": "adaway",
    "antennapod": "antennapod",
    "deadhash": "deadhash",
    "homemedkit": "homemedkit",
    "jigsaw": "jigsaw",
    "luxalarm": "luxalarm",
    "pomodorot": "pomodorot",
    "portauthority": "portauthority",
    "simplenotes": "simplenotes",
    "wifianalyzer": "wifianalyzer",
}

KEYFRAME_FIXES_METHODS = {"stabilize", "hysteresis", "homography", "clip", "vlm"}


def normalize_app_slug(name: str) -> str:
    return name.lower()


def normalize_utg_id(utg_str: str) -> str:
    m = re.match(r"^(?:utg-?)?(\d+)$", utg_str.strip().lower())
    if not m:
        raise ValueError(f"Cannot parse utg: {utg_str!r}")
    return f"utg-{int(m.group(1)):02d}"


def normalize_model_slug(model_name: str) -> str:
    return re.sub(r"[^a-z0-9-]+", "-", model_name.lower()).strip("-")


def _numeric_sort_key(path: str) -> tuple:
    name = os.path.splitext(os.path.basename(path))[0]
    m = re.search(r"(\d+)", name)
    return (0, int(m.group(1))) if m else (1, name)


def copy_file(src: Path, dst: Path, dry_run: bool) -> bool:
    """Copy src to dst. Returns True if copied, False if skipped."""
    if dst.exists():
        print(f"  [SKIP] {dst.relative_to(ROOT_DIR)} already exists")
        return False
    if dry_run:
        print(f"  [DRY] copy {src.relative_to(ROOT_DIR)} -> {dst.relative_to(ROOT_DIR)}")
        return True
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    print(f"  [COPY] {src.relative_to(ROOT_DIR)} -> {dst.relative_to(ROOT_DIR)}")
    return True


def migrate_artifacts(old_artifacts: Path, new_artifacts: Path, dry_run: bool) -> None:
    """Migrate and rename artifacts_N.png -> artifact-NNN.png."""
    if not old_artifacts.is_dir():
        return
    pngs = sorted(glob.glob(str(old_artifacts / "*.png")), key=_numeric_sort_key)
    if not pngs:
        return
    for i, src in enumerate(pngs, start=1):
        dst = new_artifacts / f"artifact-{i:03d}.png"
        copy_file(Path(src), dst, dry_run)


def migrate_keyframes(old_kf_dir: Path, new_keyframes_dir: Path, dry_run: bool) -> None:
    """Migrate keyframe PNGs, renaming them to kf-NNNN.png."""
    if not old_kf_dir.is_dir():
        return
    pngs = sorted(glob.glob(str(old_kf_dir / "*.png")), key=_numeric_sort_key)
    for i, src in enumerate(pngs, start=1):
        dst = new_keyframes_dir / f"kf-{i:04d}.png"
        copy_file(Path(src), dst, dry_run)


def write_stub_metadata(
    run_dir: Path,
    app_slug: str,
    utg_id: str,
    method: str,
    variant: str,
    source: str,
    video_file: str,
    dry_run: bool,
) -> None:
    """Write a stub metadata.json for a migrated run."""
    meta_path = run_dir / "metadata.json"
    if meta_path.exists():
        return
    payload = {
        "app": app_slug,
        "utg": utg_id,
        "method": method,
        "variant": variant,
        "source": source,
        "video": video_file,
        "config": {},
        "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "duration_sec": 0.0,
        "status": "migrated",
    }
    if dry_run:
        print(f"  [DRY] write metadata.json -> {meta_path.relative_to(ROOT_DIR)}")
        return
    meta_path.parent.mkdir(parents=True, exist_ok=True)
    with meta_path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    print(f"  [META] {meta_path.relative_to(ROOT_DIR)}")


def update_manifest(
    utg_new_dir: Path,
    app_slug: str,
    utg_id: str,
    run_id: str,
    method: str,
    variant: str,
    source: str,
    run_relative_path: str,
    video_file: str,
    video_type: str,
    dry_run: bool,
) -> None:
    manifest_path = utg_new_dir / "manifest.json"
    if dry_run:
        print(f"  [DRY] update manifest.json at {manifest_path.relative_to(ROOT_DIR)}")
        return

    if manifest_path.exists():
        with manifest_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {
            "app": app_slug,
            "utg": utg_id,
            "videos": {"handheld": [], "screenrec": []},
            "runs": [],
            "latest": {},
        }

    vid_source = "handheld" if video_type == "hhv" else "screenrec"
    if video_file and video_file not in data["videos"][vid_source]:
        data["videos"][vid_source].append(video_file)

    entry = {"id": run_id, "method": method, "source": source, "status": "migrated", "path": run_relative_path}
    if variant:
        entry["variant"] = variant
    # Don't add duplicate run entries
    existing_ids = {r["id"] for r in data["runs"]}
    if run_id not in existing_ids:
        data["runs"].append(entry)

    latest_key = method if not variant else f"{method}_{variant.replace('-', '_')}"
    data["latest"][latest_key] = run_id

    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    with manifest_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"  [MANIFEST] updated {manifest_path.relative_to(ROOT_DIR)}")


def find_old_utg_dirs(app_filter=None, utg_filter=None):
    """Find old app_*/utg*/ directories."""
    result = []
    for app_dir in sorted(glob.glob(str(ROOT_DIR / "app_*"))):
        if not os.path.isdir(app_dir):
            continue
        app_name = os.path.basename(app_dir)[len("app_"):]
        if app_filter and app_name.lower() != app_filter.lower():
            continue
        for utg_dir in sorted(glob.glob(os.path.join(app_dir, "utg*"))):
            if not os.path.isdir(utg_dir):
                continue
            utg_name = os.path.basename(utg_dir)
            if utg_filter and utg_name.lower() != utg_filter.lower():
                continue
            result.append((app_name, utg_name, Path(utg_dir)))
    return result


def migrate_utg(app_name: str, utg_old_str: str, old_utg_dir: Path, dry_run: bool) -> None:
    app_slug = normalize_app_slug(app_name)
    utg_id = normalize_utg_id(utg_old_str)

    new_utg_dir = ROOT_DIR / "apps" / app_slug / "utgs" / utg_id
    new_input_dir = new_utg_dir / "input"
    new_artifacts_dir = new_input_dir / "artifacts"
    new_videos_handheld = ROOT_DIR / "apps" / app_slug / "videos" / "handheld"
    new_videos_screenrec = ROOT_DIR / "apps" / app_slug / "videos" / "screenrec"

    print(f"\n{'='*60}")
    print(f"Migrating: {app_name}/{utg_old_str} -> apps/{app_slug}/utgs/{utg_id}/")
    print(f"{'='*60}")

    # 1. Migrate utg.json
    old_utg_json = old_utg_dir / "input" / "utg.json"
    if old_utg_json.exists():
        copy_file(old_utg_json, new_input_dir / "utg.json", dry_run)

    # 2. Migrate artifacts
    old_artifacts = old_utg_dir / "input" / "artifacts"
    if old_artifacts.is_dir():
        migrate_artifacts(old_artifacts, new_artifacts_dir, dry_run)

    # 3. Migrate videos (only copy once per app, not per utg)
    for video_type, subdir, old_filename, new_filename in [
        ("hhv", "handheld", f"hhv_app_{app_name}.mp4", "hhv-001.mp4"),
        ("srv", "screenrec", f"srv_app_{app_name}.mp4", "srv-001.mp4"),
    ]:
        old_video = old_utg_dir / "input" / subdir / old_filename
        new_video_dir = new_videos_handheld if video_type == "hhv" else new_videos_screenrec
        new_video = new_video_dir / new_filename
        if old_video.exists():
            copy_file(old_video, new_video, dry_run)

    # 4. Migrate output runs
    old_output = old_utg_dir / "output"
    if not old_output.is_dir():
        print("  [INFO] No output/ directory found, skipping run migration")
        return

    # 4a. Migrate baseline and keyframe-fix runs from execution_*_<method>.json files
    run_counter = {"baseline": 0, "stabilize": 0, "hysteresis": 0, "homography": 0, "clip": 0, "vlm": 0}
    for json_file in sorted(glob.glob(str(old_output / "execution_*.json"))):
        fname = os.path.basename(json_file)
        # Parse: execution_<vtype>_<App>[_<method>].json
        m = re.match(r"execution_(hhv|srv)_\w+?(?:_(\w+))?\.json$", fname)
        if not m:
            print(f"  [SKIP] unrecognized filename pattern: {fname}")
            continue
        video_type = m.group(1)
        method_suffix = m.group(2) if m.group(2) else "baseline"
        method = method_suffix if method_suffix else "baseline"
        source = "handheld" if video_type == "hhv" else "screenrec"

        run_counter[method] = run_counter.get(method, 0) + 1
        run_id = f"run-{run_counter[method]:03d}"

        if method == "baseline":
            method_path = "baseline"
        elif method in KEYFRAME_FIXES_METHODS:
            method_path = f"keyframe-fixes/{method}"
        else:
            print(f"  [SKIP] unknown method: {method}")
            continue

        new_run_dir = new_utg_dir / "runs" / method_path / source / run_id
        copy_file(Path(json_file), new_run_dir / "execution_trace.json", dry_run)

        # Migrate corresponding keyframes directory
        kf_dir_name = f"keyframes_{method}"
        old_kf_dir = old_output / kf_dir_name
        if old_kf_dir.is_dir():
            migrate_keyframes(old_kf_dir, new_run_dir / "keyframes", dry_run)

        video_file = "hhv-001.mp4" if video_type == "hhv" else "srv-001.mp4"
        write_stub_metadata(new_run_dir, app_slug, utg_id, method, "", source, video_file, dry_run)
        run_rel = str(new_run_dir.relative_to(new_utg_dir)) + "/"
        update_manifest(new_utg_dir, app_slug, utg_id, run_id, method, "", source, run_rel, video_file, video_type, dry_run)

    # 4b. Migrate LLM runs from output/llm_<provider>/
    for llm_dir in sorted(glob.glob(str(old_output / "llm_*"))):
        if not os.path.isdir(llm_dir):
            continue
        provider = os.path.basename(llm_dir)[len("llm_"):]

        # Find execution trace JSON files to determine model runs
        for json_file in sorted(glob.glob(os.path.join(llm_dir, "execution_trace_llm_*.json"))):
            fname = os.path.basename(json_file)
            # Pattern: execution_trace_llm_<vtype>_app_<App>_<model>_<timestamp>.json
            m = re.match(r"execution_trace_llm_(hhv|srv)_app_\w+?_(.+?)_\d{8}_\d{6}\.json$", fname)
            if not m:
                # Try simpler pattern without timestamp
                m = re.match(r"execution_trace_llm_(hhv|srv)_app_\w+?_(.+?)\.json$", fname)
            if not m:
                print(f"  [SKIP] unrecognized LLM filename: {fname}")
                continue

            video_type = m.group(1)
            model_raw = m.group(2)
            model_slug = normalize_model_slug(model_raw)
            source = "handheld" if video_type == "hhv" else "screenrec"

            new_run_dir = new_utg_dir / "runs" / "llm" / provider / model_slug / source / "run-001"

            copy_file(Path(json_file), new_run_dir / "execution_trace.json", dry_run)

            # Migrate keyframes
            old_kf_dir = Path(llm_dir) / f"execution_trace_llm_{video_type}_keyframes"
            if old_kf_dir.is_dir():
                migrate_keyframes(old_kf_dir, new_run_dir / "keyframes", dry_run)

            # Migrate frames manifest
            old_manifest = Path(llm_dir) / f"frames_manifest_{video_type}.json"
            if old_manifest.exists():
                copy_file(old_manifest, new_run_dir / "frames_manifest.json", dry_run)

            video_file = "hhv-001.mp4" if video_type == "hhv" else "srv-001.mp4"
            write_stub_metadata(new_run_dir, app_slug, utg_id, "llm", model_slug, source, video_file, dry_run)
            run_rel = str(new_run_dir.relative_to(new_utg_dir)) + "/"
            update_manifest(new_utg_dir, app_slug, utg_id, "run-001", "llm", model_slug, source, run_rel, video_file, video_type, dry_run)


def parse_args():
    parser = argparse.ArgumentParser(description="Migrate old app_*/utg*/ structure to apps/*/utgs/utg-*/")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without executing")
    parser.add_argument("--app", type=str, default=None, help="Migrate single app (e.g. AdAway)")
    parser.add_argument("--utg", type=str, default=None, help="Migrate single utg slot (e.g. utg01)")
    return parser.parse_args()


def main():
    args = parse_args()
    pairs = find_old_utg_dirs(app_filter=args.app, utg_filter=args.utg)

    if not pairs:
        print("[ERROR] No app_*/utg*/ directories found to migrate.")
        sys.exit(1)

    print(f"Found {len(pairs)} utg slot(s) to migrate:")
    for app_name, utg_str, utg_dir in pairs:
        print(f"  {app_name}/{utg_str} -> apps/{normalize_app_slug(app_name)}/utgs/{normalize_utg_id(utg_str)}/")

    if args.dry_run:
        print("\n[DRY RUN — no files will be written]\n")

    for app_name, utg_str, utg_dir in pairs:
        migrate_utg(app_name, utg_str, utg_dir, dry_run=args.dry_run)

    print(f"\n{'='*60}")
    print("Migration complete." if not args.dry_run else "Dry run complete.")
    print("Original app_*/utg*/ directories were NOT modified.")


if __name__ == "__main__":
    main()
