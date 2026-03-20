"""
run_all.py — Execute all GIFdroid commands from commands.txt

Usage:
    python run_all.py                        # run all commands sequentially
    python run_all.py --commands commands.txt  # specify a different commands file
    python run_all.py --dry-run              # print commands without executing

Each non-comment, non-empty line in commands.txt is treated as a shell command.
Already-completed runs are skipped automatically (idempotency is handled by main.py).
"""

import argparse
import os
import subprocess
import sys
import time
from datetime import datetime


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def parse_args():
    parser = argparse.ArgumentParser(description='Run all GIFdroid commands from commands.txt')
    parser.add_argument('--commands', default='commands.txt',
                        help='Path to commands file (default: commands.txt)')
    parser.add_argument('--dry-run', action='store_true',
                        help='Print commands without executing them')
    return parser.parse_args()


def load_commands(commands_file):
    """Parse commands.txt and return only executable (non-comment, non-empty) lines."""
    with open(commands_file, 'r') as f:
        lines = f.readlines()
    commands = []
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith('#'):
            commands.append(stripped)
    return commands


def fmt_elapsed(seconds):
    m, s = divmod(int(seconds), 60)
    return f'{m}m {s}s' if m else f'{s}s'


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

def run_all(commands, dry_run=False):
    total = len(commands)
    print(f'\n{"="*60}')
    print(f'GIFdroid batch runner — {total} command(s) to execute')
    print(f'Started : {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    if dry_run:
        print('[DRY RUN — no commands will be executed]')
    print(f'{"="*60}\n')

    results = []  # list of (label, status, elapsed)
    batch_start = time.time()

    for idx, cmd in enumerate(commands, 1):
        # Extract a short label from the --out path for display
        label = cmd
        if '--out' in cmd:
            out_val = cmd.split('--out')[1].strip().split()[0]
            label = os.path.basename(out_val)

        print(f'[{idx}/{total}] {label}')
        print(f'  CMD: {cmd}')

        if dry_run:
            print('  [SKIPPED — dry run]\n')
            results.append((label, 'dry-run', 0.0))
            continue

        t0 = time.time()
        result = subprocess.run(cmd, shell=True, universal_newlines=True)
        elapsed = time.time() - t0

        if result.returncode == 0:
            status = 'OK'
            print(f'  [OK] finished in {fmt_elapsed(elapsed)}')
        else:
            status = 'FAILED'
            print(f'  [FAILED] exit code {result.returncode} after {fmt_elapsed(elapsed)}')

        results.append((label, status, elapsed))
        print()

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    total_elapsed = time.time() - batch_start
    ok    = sum(1 for _, s, _ in results if s == 'OK')
    failed = sum(1 for _, s, _ in results if s == 'FAILED')

    print(f'{"="*60}')
    print(f'Batch complete in {fmt_elapsed(total_elapsed)}')
    print(f'  OK     : {ok}')
    print(f'  Failed : {failed}')
    if dry_run:
        print(f'  (dry-run, no commands executed)')
    print(f'{"="*60}')

    if failed:
        print('\nFailed commands:')
        for label, status, _ in results:
            if status == 'FAILED':
                print(f'  - {label}')
        sys.exit(1)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    args = parse_args()

    if not os.path.isfile(args.commands):
        print(f'[ERROR] Commands file not found: {args.commands}')
        sys.exit(1)

    commands = load_commands(args.commands)
    if not commands:
        print(f'[ERROR] No executable commands found in: {args.commands}')
        sys.exit(1)

    run_all(commands, dry_run=args.dry_run)
