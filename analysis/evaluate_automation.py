"""Milestone 5 — Evaluation script.

Compares a session_trace.json (active automation loop) against an execution_trace.json
(passive LLM pipeline) using Longest Common Subsequence (LCS) of action types.

Usage — single app:
    python analysis/evaluate_automation.py \\
        --session-trace artifacts/milestone4/run-001/session_trace.json \\
        --execution-trace apps/adaway/llm/gemini/gemini-2-5-pro/screenrec/fps1-5__max100__llm-assisted__gap1/run-001/execution_trace.json

Usage — batch (produces analysis/automation_results.md):
    python analysis/evaluate_automation.py \\
        --batch \\
        --apps adaway antennapod luxalarm \\
        --session-dir artifacts/milestone5 \\
        --execution-trace-dir apps
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


# ---------------------------------------------------------------------------
# Action type normalisation
# ---------------------------------------------------------------------------

_NORMALISE = {
    # session_trace types → canonical
    "tap": "tap",
    "scroll": "scroll",
    "swipe": "scroll",
    "type_text": "input",
    "input": "input",
    "press_back": "back",
    "press_home": "home",
    "done": "done",
    "wait": "wait",
    # execution_trace types (uppercase) → canonical
    "tap": "tap",
    "swipe": "scroll",
    "scroll": "scroll",
    "input": "input",
    "none": "none",
    "start": "start",
    "end": "done",
    "launch_app": "launch",
}

# These action types are considered non-task noise and excluded from LCS
_IGNORE = {"none", "start", "end", "done", "launch", "wait"}


def _normalise(action_type: str) -> str:
    return _NORMALISE.get(action_type.lower(), action_type.lower())


def _extract_session_types(session_trace: dict) -> list[str]:
    """Extract normalised action type sequence from session_trace.json."""
    types = []
    for step in session_trace.get("steps", []):
        action = step.get("action", {})
        t = _normalise(action.get("type", "unknown"))
        types.append(t)
    return types


def _extract_execution_types(execution_trace: dict) -> list[str]:
    """Extract normalised action type sequence from execution_trace.json."""
    types = []
    for step in execution_trace.get("replay_trace", []):
        action = step.get("action", {})
        t = _normalise(action.get("type", "unknown"))
        types.append(t)
    return types


# ---------------------------------------------------------------------------
# LCS
# ---------------------------------------------------------------------------

def _lcs(a: list[str], b: list[str]) -> list[str]:
    """Return the LCS of two sequences (DP, O(mn))."""
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack
    seq = []
    i, j = m, n
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            seq.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return list(reversed(seq))


def _meaningful(types: list[str]) -> list[str]:
    """Filter out non-task types for LCS comparison."""
    return [t for t in types if t not in _IGNORE]


# ---------------------------------------------------------------------------
# Single-app evaluation
# ---------------------------------------------------------------------------

def evaluate_single(
    session_trace_path: Path,
    execution_trace_path: Path,
    app_name: str = "",
) -> dict:
    """Evaluate one session trace against one execution trace.

    Returns a result dict with keys: app, gt_steps, auto_steps, lcs_score,
    matched_types, missed_types, extra_types.
    """
    session = json.loads(session_trace_path.read_text())
    execution = json.loads(execution_trace_path.read_text())

    app = app_name or session.get("video", "").split("/")[1] if session.get("video") else "unknown"

    raw_auto = _extract_session_types(session)
    raw_gt = _extract_execution_types(execution)

    auto_types = _meaningful(raw_auto)
    gt_types = _meaningful(raw_gt)

    lcs_seq = _lcs(auto_types, gt_types)
    lcs_len = len(lcs_seq)
    gt_len = len(gt_types)
    auto_len = len(auto_types)

    lcs_score = round(lcs_len / gt_len, 4) if gt_len > 0 else 0.0

    matched = lcs_seq
    missed = [t for t in gt_types if t not in set(lcs_seq)]
    extra = [t for t in auto_types if t not in set(lcs_seq)]

    return {
        "app": app,
        "gt_steps_raw": len(raw_gt),
        "auto_steps_raw": len(raw_auto),
        "gt_steps": gt_len,
        "auto_steps": auto_len,
        "lcs_length": lcs_len,
        "lcs_score": lcs_score,
        "matched_types": matched,
        "missed_types": missed,
        "extra_types": extra,
        "session_trace": str(session_trace_path),
        "execution_trace": str(execution_trace_path),
    }


def print_single(result: dict) -> None:
    """Pretty-print a single evaluation result."""
    print(f"\nApp: {result['app']}")
    print(f"  Ground truth steps (meaningful): {result['gt_steps']}  (raw: {result['gt_steps_raw']})")
    print(f"  Automation steps  (meaningful): {result['auto_steps']}  (raw: {result['auto_steps_raw']})")
    print(f"  LCS score:          {result['lcs_score']:.2f}  ({result['lcs_length']}/{result['gt_steps']} actions matched)")
    print(f"  Action types matched: {', '.join(result['matched_types']) or '(none)'}")
    print(f"  Action types missed:  {', '.join(result['missed_types']) or '(none)'}")
    print(f"  Action types extra:   {', '.join(result['extra_types']) or '(none)'}")


# ---------------------------------------------------------------------------
# Batch evaluation
# ---------------------------------------------------------------------------

def _find_execution_trace(apps_dir: Path, app: str) -> Path | None:
    """Find the best execution_trace.json for an app."""
    # Prefer gemini-2-5-pro screenrec llm-assisted run-001
    candidates = [
        apps_dir / app / "llm/gemini/gemini-2-5-pro/screenrec/fps1-5__max100__llm-assisted__gap1/run-001/execution_trace.json",
        apps_dir / app / "llm/gemini/gemini-2-5-flash/screenrec/fps1-5__max100__llm-assisted__gap1/run-001/execution_trace.json",
    ]
    for c in candidates:
        if c.exists():
            return c
    # Fall back to first execution_trace found
    for p in sorted((apps_dir / app / "llm").rglob("execution_trace.json")):
        return p
    return None


def _find_session_trace(session_dir: Path, app: str) -> Path | None:
    """Find session_trace.json for an app in the session directory."""
    # Look for <session_dir>/<app>/session_trace.json or <session_dir>/<app>/run-*/session_trace.json
    for p in sorted(session_dir.rglob(f"{app}*/session_trace.json")):
        return p
    for p in sorted(session_dir.rglob("session_trace.json")):
        data = json.loads(p.read_text())
        vid = data.get("video", "")
        if app in vid:
            return p
    return None


def evaluate_batch(
    apps: list[str],
    session_dir: Path,
    apps_dir: Path,
) -> list[dict]:
    results = []
    for app in apps:
        session_path = _find_session_trace(session_dir, app)
        exec_path = _find_execution_trace(apps_dir, app)

        if session_path is None:
            print(f"[WARN] No session_trace.json found for {app} in {session_dir}")
            continue
        if exec_path is None:
            print(f"[WARN] No execution_trace.json found for {app} under {apps_dir}")
            continue

        result = evaluate_single(session_path, exec_path, app_name=app)
        results.append(result)
        print_single(result)

    return results


def write_results_md(results: list[dict], out_path: Path) -> None:
    """Write automation_results.md with summary table and per-app details."""
    lines = [
        "# Automation Evaluation Results — Milestone 5",
        "",
        "Metric: Longest Common Subsequence (LCS) of meaningful action types,  ",
        "normalised by ground-truth sequence length.  ",
        "Ground truth = passive Gemini-2.5-Pro execution trace (`execution_trace.json`).  ",
        "Automation = active video-guided loop session trace (`session_trace.json`).",
        "",
        "## Summary Table",
        "",
        "| App | GT Steps | Auto Steps | LCS Score |",
        "|-----|----------|------------|-----------|",
    ]
    for r in results:
        lines.append(
            f"| {r['app']} | {r['gt_steps']} | {r['auto_steps']} | {r['lcs_score']:.2f} |"
        )

    if results:
        avg_lcs = sum(r["lcs_score"] for r in results) / len(results)
        avg_gt = sum(r["gt_steps"] for r in results) / len(results)
        avg_auto = sum(r["auto_steps"] for r in results) / len(results)
        lines.append(
            f"| **Average** | {avg_gt:.1f} | {avg_auto:.1f} | **{avg_lcs:.2f}** |"
        )

    lines += ["", "## Per-App Details", ""]
    for r in results:
        lines += [
            f"### {r['app']}",
            "",
            f"- Session trace: `{r['session_trace']}`",
            f"- Execution trace: `{r['execution_trace']}`",
            f"- GT steps (meaningful): {r['gt_steps']} (raw: {r['gt_steps_raw']})",
            f"- Auto steps (meaningful): {r['auto_steps']} (raw: {r['auto_steps_raw']})",
            f"- LCS score: **{r['lcs_score']:.2f}** ({r['lcs_length']}/{r['gt_steps']})",
            f"- Matched types: {', '.join(r['matched_types']) or '(none)'}",
            f"- Missed types:  {', '.join(r['missed_types']) or '(none)'}",
            f"- Extra types:   {', '.join(r['extra_types']) or '(none)'}",
            "",
        ]

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines))
    print(f"\nResults written to {out_path}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate automation session traces against execution traces")
    parser.add_argument("--session-trace", type=Path, help="Path to session_trace.json (single-app mode)")
    parser.add_argument("--execution-trace", type=Path, help="Path to execution_trace.json (single-app mode)")
    parser.add_argument("--batch", action="store_true", help="Batch mode: evaluate multiple apps")
    parser.add_argument("--apps", nargs="+", default=["adaway", "antennapod", "luxalarm"], help="App names for batch mode")
    parser.add_argument(
        "--session-dir",
        type=Path,
        default=Path("artifacts/milestone5"),
        help="Directory containing session traces (batch mode)",
    )
    parser.add_argument(
        "--execution-trace-dir",
        type=Path,
        default=Path("apps"),
        help="Root apps/ directory for finding execution traces",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("analysis/automation_results.md"),
        help="Output markdown file path",
    )
    args = parser.parse_args()

    if args.batch:
        results = evaluate_batch(args.apps, args.session_dir, args.execution_trace_dir)
        if results:
            write_results_md(results, args.output)
        else:
            print("No results to write.")
    else:
        if not args.session_trace or not args.execution_trace:
            parser.error("--session-trace and --execution-trace are required in single-app mode")
        result = evaluate_single(args.session_trace, args.execution_trace)
        print_single(result)


if __name__ == "__main__":
    main()
