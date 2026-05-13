#!/usr/bin/env python3
"""Rename .MOV files in apps/*/videos to hhv-<number>.MOV format."""

import re
from pathlib import Path

def extract_hhv_number(filename: str) -> int | None:
    """Extract hhv number from filenames like hhv-001.mp4."""
    match = re.match(r'hhv-(\d+)', filename, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return None

def rename_mov_files_in_app(app_dir: Path) -> None:
    """Rename .MOV files in app_dir/videos to hhv-<next_number>.MOV."""
    videos_dir = app_dir / "videos"
    if not videos_dir.exists():
        return

    # Find all existing hhv numbers
    existing_hhv_numbers = set()
    for file in videos_dir.iterdir():
        if file.is_file():
            hhv_num = extract_hhv_number(file.name)
            if hhv_num is not None:
                existing_hhv_numbers.add(hhv_num)

    # Find the next available number
    next_hhv_num = 1
    if existing_hhv_numbers:
        next_hhv_num = max(existing_hhv_numbers) + 1

    # Find all .MOV files and rename them
    mov_files = sorted(videos_dir.glob("*.MOV"))
    for mov_file in mov_files:
        new_name = f"hhv-{next_hhv_num:03d}.MOV"
        new_path = mov_file.parent / new_name

        print(f"  {mov_file.name} → {new_name}")
        mov_file.rename(new_path)
        next_hhv_num += 1

def main():
    """Rename .MOV files in all apps/*/videos directories."""
    apps_dir = Path("/Users/tanmaybhuskute/Documents/gifdroid-reproduction/apps")

    if not apps_dir.exists():
        print(f"Error: {apps_dir} not found")
        return

    # Get all app directories (exclude 0_analysis)
    app_dirs = sorted([d for d in apps_dir.iterdir()
                      if d.is_dir() and d.name != "0_analysis"])

    total_renamed = 0
    for app_dir in app_dirs:
        videos_dir = app_dir / "videos"
        if not videos_dir.exists():
            continue

        mov_files = list(videos_dir.glob("*.MOV"))
        if not mov_files:
            continue

        print(f"{app_dir.name}:")
        rename_mov_files_in_app(app_dir)
        total_renamed += len(mov_files)

    print(f"\nTotal files renamed: {total_renamed}")

if __name__ == "__main__":
    main()
