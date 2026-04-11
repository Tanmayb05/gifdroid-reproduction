"""
run_keyframe_variants.py — Run all (or selected) keyframe methods for specified app/utg pairs.

Usage:
    python scripts/run_keyframe_variants.py                              # use default config
    python scripts/run_keyframe_variants.py --config scripts/data/keyframe_runs.yml
    python scripts/run_keyframe_variants.py --methods baseline stabilize # only these methods
    python scripts/run_keyframe_variants.py --dry-run                    # print commands, no execution
    python scripts/run_keyframe_variants.py --force                      # re-run even if output exists

Input YAML format:
    runs:
      - app: AdAway
        utg: utg01
      - app: LuxAlarm
        utg: [utg01, utg02]   # list form also accepted

Each app/utg must have:
    apps/<app>/
        videos/handheld/hhv-001.mp4
        utgs/<utg>/
            input/
                utg.json
                artifacts/

Output is written to:
    apps/<app>/utgs/<utg>/runs/baseline/handheld/run-NNN/execution_trace.json
    apps/<app>/utgs/<utg>/runs/keyframe-fixes/<method>/handheld/run-NNN/execution_trace.json
    apps/<app>/utgs/<utg>/runs/.../run-NNN/keyframes/kf-NNNN.png
"""

import argparse
import os
import subprocess
import sys
import time
from datetime import datetime

try:
    import yaml
except ImportError:
    print('[ERROR] PyYAML is required: pip install pyyaml')
    sys.exit(1)

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALL_METHODS = ['baseline', 'stabilize', 'hysteresis', 'homography', 'clip', 'vlm']

DEFAULT_CONFIG = os.path.join(PROJECT_ROOT, 'scripts', 'data', 'keyframe_runs.yml')


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def parse_args():
    parser = argparse.ArgumentParser(
        description='Run all keyframe method variants for specified app/utg pairs.'
    )
    parser.add_argument(
        '--config', default=DEFAULT_CONFIG,
        help=f'Path to YAML config file (default: {DEFAULT_CONFIG})'
    )
    parser.add_argument(
        '--methods', nargs='+', choices=ALL_METHODS, metavar='METHOD',
        help=f'Keyframe methods to run (default: all). Choices: {ALL_METHODS}'
    )
    parser.add_argument(
        '--dry-run', action='store_true',
        help='Print commands without executing them'
    )
    parser.add_argument(
        '--force', action='store_true',
        help='Re-run even if output JSON already exists'
    )
    return parser.parse_args()


def load_config(config_path):
    """Load and normalise the YAML config into a flat list of (app, utg) tuples."""
    with open(config_path, 'r') as f:
        data = yaml.safe_load(f)

    if not data or 'runs' not in data:
        print(f'[ERROR] Config must have a top-level "runs" key: {config_path}')
        sys.exit(1)

    pairs = []
    for entry in data['runs']:
        app = entry.get('app')
        utg = entry.get('utg')
        if not app or not utg:
            print(f'[ERROR] Each entry needs "app" and "utg": {entry}')
            sys.exit(1)
        if isinstance(utg, list):
            for u in utg:
                pairs.append((app, str(u)))
        else:
            pairs.append((app, str(utg)))
    return pairs


def build_command(app, utg, method, force=False):
    """
    Build the python -m src_gifdroid.main command for a given app/utg/method.
    Returns (cmd_str, out_dir, skip_reason) where skip_reason is None if the run should proceed.
    """
    app_slug = app.lower()
    # Normalize utg id: accept "utg01" -> "utg-01", "01" -> "utg-01"
    import re as _re
    m = _re.match(r"^(?:utg-?)?(\d+)$", str(utg).strip().lower())
    utg_slug = f"utg-{int(m.group(1)):02d}" if m else str(utg)

    app_root = os.path.join(PROJECT_ROOT, 'apps', app_slug)
    utg_root = os.path.join(app_root, 'utgs', utg_slug)
    video = os.path.join(app_root, 'videos', 'handheld', 'hhv-001.mp4')
    utg_json = os.path.join(utg_root, 'input', 'utg.json')
    artifacts = os.path.join(utg_root, 'input', 'artifacts')

    if method == 'baseline':
        method_path = 'baseline'
    else:
        method_path = f'keyframe-fixes/{method}'

    out_dir = os.path.join(utg_root, 'runs', method_path, 'handheld', 'run-001')
    out_trace = os.path.join(out_dir, 'execution_trace.json')

    # Validate inputs
    missing = [p for p in [video, utg_json, artifacts] if not os.path.exists(p)]
    if missing:
        return None, out_dir, f'missing inputs: {", ".join(os.path.relpath(p, PROJECT_ROOT) for p in missing)}'

    # Skip if already done (unless --force)
    if not force and os.path.isfile(out_trace):
        return None, out_dir, 'output already exists (use --force to re-run)'

    cmd = (
        f'python -m src_gifdroid.main'
        f' --video "{video}"'
        f' --utg "{utg_json}"'
        f' --artifact "{artifacts}"'
        f' --out "{out_dir}"'
        f' --keyframe-method {method}'
    )
    return cmd, out_dir, None


def fmt_elapsed(seconds):
    m, s = divmod(int(seconds), 60)
    return f'{m}m {s}s' if m else f'{s}s'


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

def run_variants(pairs, methods, dry_run=False, force=False):
    print(f'\n{"="*65}')
    print(f'GIFdroid keyframe variant runner')
    print(f'Started : {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    print(f'Apps/UTGs: {len(pairs)}  |  Methods: {methods}')
    print(f'Total planned runs: {len(pairs) * len(methods)}')
    if dry_run:
        print('[DRY RUN — no commands will be executed]')
    print(f'{"="*65}\n')

    results = []  # (label, status, elapsed)
    batch_start = time.time()

    for app, utg in pairs:
        print(f'--- {app} / {utg} ---')
        for method in methods:
            label = f'{app}/{utg}/{method}'
            cmd, out_path, skip_reason = build_command(app, utg, method, force=force)

            if skip_reason:
                print(f'  [{method}] SKIP — {skip_reason}')
                results.append((label, 'skipped', 0.0))
                continue

            out_rel = os.path.relpath(out_path, PROJECT_ROOT)
            print(f'  [{method}] -> {out_rel}/execution_trace.json')
            if dry_run:
                print(f'    CMD: {cmd}')
                print(f'    [SKIPPED — dry run]')
                results.append((label, 'dry-run', 0.0))
                continue

            t0 = time.time()
            result = subprocess.run(cmd, shell=True, cwd=PROJECT_ROOT, universal_newlines=True)
            elapsed = time.time() - t0

            if result.returncode == 0:
                print(f'    [OK] {fmt_elapsed(elapsed)}')
                results.append((label, 'OK', elapsed))
            else:
                print(f'    [FAILED] exit {result.returncode} after {fmt_elapsed(elapsed)}')
                results.append((label, 'FAILED', elapsed))
        print()

    # Summary
    total_elapsed = time.time() - batch_start
    ok      = sum(1 for _, s, _ in results if s == 'OK')
    failed  = sum(1 for _, s, _ in results if s == 'FAILED')
    skipped = sum(1 for _, s, _ in results if s in ('skipped', 'dry-run'))

    print(f'{"="*65}')
    print(f'Done in {fmt_elapsed(total_elapsed)}')
    print(f'  OK      : {ok}')
    print(f'  Failed  : {failed}')
    print(f'  Skipped : {skipped}')
    print(f'{"="*65}')

    if failed:
        print('\nFailed runs:')
        for label, status, _ in results:
            if status == 'FAILED':
                print(f'  - {label}')
        sys.exit(1)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    args = parse_args()

    if not os.path.isfile(args.config):
        print(f'[ERROR] Config file not found: {args.config}')
        print(f'        Create one at that path or pass --config <path>')
        sys.exit(1)

    pairs = load_config(args.config)
    if not pairs:
        print('[ERROR] No app/utg pairs found in config.')
        sys.exit(1)

    methods = args.methods or ALL_METHODS

    run_variants(pairs, methods, dry_run=args.dry_run, force=args.force)
