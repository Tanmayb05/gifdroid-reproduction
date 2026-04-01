from __future__ import annotations

import argparse
import json
import shutil
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple

import yaml

from gifdroid_llm.config import ConfigError, _normalize_utg_number
from gifdroid_llm.io_utils import write_json


@dataclass(frozen=True)
class ResetTarget:
    app_name: str
    utg_id: str


@dataclass(frozen=True)
class ResetConfig:
    dry_run: bool
    targets: List[ResetTarget]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Wipe run directories and reset UTG manifest run info "
            "for selected app/UTG targets."
        )
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("gifdroid_llm/input/reset_runs.yml"),
        help="Path to reset config YAML.",
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview only; do not delete files or modify manifests.",
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


def _parse_target_entry(entry: Any, idx: int) -> List[ResetTarget]:
    if not isinstance(entry, dict):
        raise ConfigError(f"targets[{idx}] must be a mapping")
    app_name = _require_non_empty_str(entry, "app_name")
    utg_raw = entry.get("utg_number")
    if isinstance(utg_raw, list):
        if len(utg_raw) == 0:
            raise ConfigError(f"targets[{idx}].utg_number list must be non-empty")
        return [ResetTarget(app_name=app_name, utg_id=_normalize_utg_number(v)) for v in utg_raw]
    return [ResetTarget(app_name=app_name, utg_id=_normalize_utg_number(utg_raw))]


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

    targets: List[ResetTarget] = []
    for i, entry in enumerate(targets_raw):
        targets.extend(_parse_target_entry(entry, i))

    return ResetConfig(dry_run=dry_run_raw, targets=targets)


def _is_within(path: Path, root: Path) -> bool:
    try:
        path.resolve(strict=False).relative_to(root.resolve(strict=False))
        return True
    except ValueError:
        return False


def _collect_run_paths(utg_root: Path, manifest_data: Dict[str, Any]) -> List[Path]:
    run_paths: List[Path] = []
    runs = manifest_data.get("runs", [])
    if not isinstance(runs, list):
        raise ConfigError(f"Invalid manifest at {utg_root / 'manifest.json'}: 'runs' must be a list")

    for i, entry in enumerate(runs):
        if not isinstance(entry, dict):
            raise ConfigError(
                f"Invalid manifest at {utg_root / 'manifest.json'}: runs[{i}] must be an object"
            )
        rel_path = entry.get("path")
        if not isinstance(rel_path, str) or not rel_path.strip():
            raise ConfigError(
                f"Invalid manifest at {utg_root / 'manifest.json'}: runs[{i}].path must be a non-empty string"
            )
        candidate = (utg_root / rel_path).resolve(strict=False)
        if not _is_within(candidate, utg_root):
            raise ConfigError(
                f"Unsafe run path in manifest ({rel_path!r}) escapes UTG root: {utg_root}"
            )
        run_paths.append(candidate)
    return run_paths


def _write_manifest_backup(manifest_path: Path) -> Path:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%SZ")
    backup_path = manifest_path.with_name(f"manifest.backup.{ts}.json")
    shutil.copy2(manifest_path, backup_path)
    return backup_path


def _reset_target(project_root: Path, target: ResetTarget, dry_run: bool) -> Tuple[int, bool]:
    app_slug = target.app_name.lower()
    utg_root = project_root / "apps" / app_slug / "utgs" / target.utg_id
    manifest_path = utg_root / "manifest.json"

    if not utg_root.exists():
        print(f"[reset_runs] SKIP {app_slug}/{target.utg_id}: UTG directory not found")
        return 0, False
    if not manifest_path.exists():
        print(f"[reset_runs] SKIP {app_slug}/{target.utg_id}: manifest.json not found")
        return 0, False

    with manifest_path.open("r", encoding="utf-8") as f:
        manifest_data = json.load(f)
    if not isinstance(manifest_data, dict):
        raise ConfigError(f"Invalid manifest at {manifest_path}: root must be an object")

    run_paths = _collect_run_paths(utg_root, manifest_data)
    run_count = len(run_paths)

    print(f"[reset_runs] Target {app_slug}/{target.utg_id}: {run_count} run(s)")
    for p in run_paths:
        if dry_run:
            print(f"[reset_runs]   would delete: {p}")
        else:
            if p.exists():
                if p.is_dir():
                    shutil.rmtree(p)
                else:
                    p.unlink()
                print(f"[reset_runs]   deleted: {p}")
            else:
                print(f"[reset_runs]   missing (already absent): {p}")

    if dry_run:
        print(f"[reset_runs]   would update manifest: {manifest_path}")
        return run_count, False

    backup_path = _write_manifest_backup(manifest_path)
    manifest_data["runs"] = []
    manifest_data["latest"] = {}
    write_json(manifest_path, manifest_data)
    print(f"[reset_runs]   backup: {backup_path}")
    print(f"[reset_runs]   updated manifest: {manifest_path}")
    return run_count, True


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
        {(t.app_name.lower(), t.utg_id): t for t in cfg.targets}.values(),
        key=lambda t: (t.app_name.lower(), t.utg_id),
    )
    print(
        f"[reset_runs] mode={'DRY-RUN' if dry_run else 'APPLY'} "
        f"targets={len(unique_targets)} config={args.config}"
    )

    project_root = Path.cwd()
    total_runs = 0
    manifests_updated = 0
    for target in unique_targets:
        runs_removed, manifest_updated = _reset_target(project_root, target, dry_run=dry_run)
        total_runs += runs_removed
        manifests_updated += 1 if manifest_updated else 0

    print(
        f"[reset_runs] done: targets={len(unique_targets)} "
        f"runs={'would_remove' if dry_run else 'removed'}={total_runs} "
        f"manifests={'would_update' if dry_run else 'updated'}={manifests_updated if not dry_run else len(unique_targets)}"
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
