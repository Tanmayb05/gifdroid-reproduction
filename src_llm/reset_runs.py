from __future__ import annotations

import argparse
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List

import yaml

from src_llm.config import ConfigError
from src_llm.io_utils import write_json


@dataclass(frozen=True)
class ResetTarget:
    app_name: str


@dataclass(frozen=True)
class ResetConfig:
    dry_run: bool
    targets: List[ResetTarget]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Wipe apps/{app}/llm/ run directories for selected apps."
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("src_llm/input/reset_runs.yml"),
        help="Path to reset config YAML.",
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview only; do not delete files.",
    )
    mode.add_argument(
        "--apply",
        action="store_true",
        help="Force apply mode regardless of config dry_run value.",
    )
    return parser.parse_args()


def _require_mapping(data: Any, section: str) -> Dict[str, Any]:
    if not isinstance(data, dict):
        raise ConfigError(f"Section '{section}' must be a mapping")
    return data


def _require_non_empty_str(data: Dict[str, Any], key: str) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ConfigError(f"Field '{key}' must be a non-empty string")
    return value.strip()


def _parse_target_entry(entry: Any, idx: int) -> ResetTarget:
    if not isinstance(entry, dict):
        raise ConfigError(f"targets[{idx}] must be a mapping")
    app_name = _require_non_empty_str(entry, "app_name")
    return ResetTarget(app_name=app_name)


def load_reset_config(path: Path) -> ResetConfig:
    if not path.exists():
        raise ConfigError(f"Reset config file not found: {path}")

    with path.open("r", encoding="utf-8") as f:
        raw = yaml.safe_load(f)

    root_obj = _require_mapping(raw, "config")
    root = root_obj["config"] if "config" in root_obj and isinstance(root_obj["config"], dict) else root_obj

    dry_run_raw = root.get("dry_run", True)
    if not isinstance(dry_run_raw, bool):
        raise ConfigError("Field 'dry_run' must be a boolean when provided")

    targets_raw = root.get("targets")
    if not isinstance(targets_raw, list) or len(targets_raw) == 0:
        raise ConfigError("Field 'targets' must be a non-empty list")

    targets = [_parse_target_entry(entry, i) for i, entry in enumerate(targets_raw)]
    return ResetConfig(dry_run=dry_run_raw, targets=targets)


def _reset_target(project_root: Path, target: ResetTarget, dry_run: bool) -> int:
    app_slug = target.app_name.lower()
    llm_dir = project_root / "apps" / app_slug / "llm"

    if not llm_dir.exists():
        print(f"[reset_runs] SKIP {app_slug}: no llm/ directory found at {llm_dir}")
        return 0

    run_dirs = sorted(llm_dir.rglob("run-[0-9][0-9][0-9]"))
    run_count = len(run_dirs)

    print(f"[reset_runs] Target {app_slug}: {run_count} run(s) under {llm_dir}")
    for p in run_dirs:
        if dry_run:
            print(f"[reset_runs]   would delete: {p}")
        else:
            if p.exists():
                shutil.rmtree(p)
                print(f"[reset_runs]   deleted: {p}")

    if not dry_run and run_count > 0:
        # Remove any empty provider/model/source dirs left behind
        for d in sorted(llm_dir.rglob("*"), reverse=True):
            if d.is_dir():
                try:
                    d.rmdir()  # only removes if empty
                except OSError:
                    pass

    return run_count


def main() -> int:
    args = parse_args()
    cfg = load_reset_config(args.config)

    if args.apply:
        dry_run = False
    elif args.dry_run:
        dry_run = True
    else:
        dry_run = cfg.dry_run

    unique_targets = sorted(
        {t.app_name.lower(): t for t in cfg.targets}.values(),
        key=lambda t: t.app_name.lower(),
    )
    print(
        f"[reset_runs] mode={'DRY-RUN' if dry_run else 'APPLY'} "
        f"targets={len(unique_targets)} config={args.config}"
    )

    project_root = Path.cwd()
    total_runs = 0
    for target in unique_targets:
        total_runs += _reset_target(project_root, target, dry_run=dry_run)

    print(
        f"[reset_runs] done: targets={len(unique_targets)} "
        f"runs={'would_remove' if dry_run else 'removed'}={total_runs}"
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ConfigError as exc:
        print(f"[reset_runs] ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
    except Exception as exc:  # pragma: no cover
        print(f"[reset_runs] UNEXPECTED ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
