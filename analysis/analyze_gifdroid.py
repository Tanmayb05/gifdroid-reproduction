#!/usr/bin/env python3
"""
analyze_gifdroid.py — GIFdroid SRV vs HHV analysis tool.

Modes:
  --extract   Scan all app/utg dirs, parse logs, build gifdroid_data.json
  --report    Read gifdroid_data.json, print comparison tables to stdout + report.md
  --plot      Read gifdroid_data.json, generate plots/ directory with charts

Usage:
  python analyze_gifdroid.py --extract
  python analyze_gifdroid.py --report
  python analyze_gifdroid.py --plot
  python analyze_gifdroid.py --extract --report --plot   (all at once)
"""

import argparse
import json
import os
import re
import sys
import statistics
from datetime import datetime
from pathlib import Path
from typing import Optional, List, Dict, Any

# ── paths ──────────────────────────────────────────────────────────────────────
ROOT = Path(__file__).parent.parent          # gifdroid-reproduction/
ANALYSIS_DIR = Path(__file__).parent         # gifdroid-reproduction/analysis/
DATA_FILE = ANALYSIS_DIR / "gifdroid_data.json"
REPORT_FILE = ANALYSIS_DIR / "report.md"
PLOTS_DIR = ANALYSIS_DIR / "plots"


# ══════════════════════════════════════════════════════════════════════════════
# EXTRACT
# ══════════════════════════════════════════════════════════════════════════════

def find_latest_log(utg_dir: Path, video_type: str) -> Optional[Path]:
    """Return the most recent gifdroid_*_{video_type}.log in utg_dir."""
    pattern = f"gifdroid_*_{video_type}.log"
    logs = sorted(utg_dir.glob(pattern))  # lexicographic = chronological (YYYYMMDD_HHMMSS)
    # Filter out logs that were just "Output already exists, skipping"
    valid = []
    for log in logs:
        text = log.read_text(errors="replace")
        if "Pipeline complete" in text:
            valid.append(log)
    return valid[-1] if valid else None


def parse_log(log_path: Path) -> dict:
    """Parse a gifdroid log file into a structured dict."""
    text = log_path.read_text(errors="replace")
    lines = text.splitlines()

    result = {
        "log_file": str(log_path),
        "step1_keyframe_location": {},
        "step2_gui_mapping": {},
        "step3_find_trace": {},
        "step4_store": {},
        "total_time_s": None,
    }

    # ── Step 1 ─────────────────────────────────────────────────────────────
    s1 = result["step1_keyframe_location"]

    m = re.search(r"read_frames_from_video: (\d+) frames decoded in ([\d.]+)s", text)
    if m:
        s1["frames_decoded"] = int(m.group(1))
        s1["decode_time_s"] = float(m.group(2))

    m = re.search(r"calculate_sim_seq: (\d+) similarities computed in ([\d.]+)s", text)
    if m:
        s1["similarities_computed"] = int(m.group(1))
        s1["sim_time_s"] = float(m.group(2))

    m = re.search(r"detect_keyframes: (\d+) keyframes detected", text)
    if m:
        s1["keyframes_detected"] = int(m.group(1))

    m = re.search(r"Keyframe indices\s*:\s*\[([^\]]*)\]", text)
    if m:
        raw = m.group(1).strip()
        s1["keyframe_indices"] = [int(x) for x in raw.split(",") if x.strip()] if raw else []

    # Step 1 duration: line after "STEP 1" block — look for "Duration : Xs" within that block
    # Find the Duration line that appears right before STEP 2
    step1_dur = re.search(
        r"STEP 1.*?Duration\s*:\s*([\d.]+)s", text, re.DOTALL
    )
    if step1_dur:
        s1["step_duration_s"] = float(step1_dur.group(1))

    # ── Step 2 ─────────────────────────────────────────────────────────────
    s2 = result["step2_gui_mapping"]

    m = re.search(r"load_screenshots: (\d+) screenshots loaded in ([\d.]+)s", text)
    if m:
        s2["screenshots_loaded"] = int(m.group(1))
        s2["load_time_s"] = float(m.group(2))

    scores = [float(x) for x in re.findall(r"score=([\d.]+)", text)]
    s2["confidence_scores"] = scores
    if scores:
        s2["score_mean"] = round(statistics.mean(scores), 4)
        s2["score_median"] = round(statistics.median(scores), 4)
        s2["score_min"] = round(min(scores), 4)
        s2["score_max"] = round(max(scores), 4)
        s2["score_stdev"] = round(statistics.stdev(scores), 4) if len(scores) > 1 else 0.0
    else:
        s2["score_mean"] = s2["score_median"] = s2["score_min"] = s2["score_max"] = s2["score_stdev"] = None

    m = re.search(r"Mapped index sequence\s*:\s*\[([^\]]*)\]", text)
    if m:
        raw = m.group(1).strip()
        seq = [int(x) for x in raw.split(",") if x.strip()] if raw else []
        s2["mapped_sequence"] = seq
        s2["unique_screens_mapped"] = len(set(seq))
    else:
        s2["mapped_sequence"] = []
        s2["unique_screens_mapped"] = 0

    step2_dur = re.search(
        r"STEP 2.*?Duration\s*:\s*([\d.]+)s", text, re.DOTALL
    )
    if step2_dur:
        s2["step_duration_s"] = float(step2_dur.group(1))

    # ── Step 3 ─────────────────────────────────────────────────────────────
    s3 = result["step3_find_trace"]

    m = re.search(r"read_graph: (\d+) edges, (\d+) vertices", text)
    if m:
        s3["utg_edges"] = int(m.group(1))
        s3["utg_vertices"] = int(m.group(2))

    m = re.search(r"(\d+) candidate paths found", text)
    if m:
        s3["candidate_paths"] = int(m.group(1))

    m = re.search(r"(\d+) trace\(s\) found \(LCS=(\d+), length=(\d+)\)", text)
    if m:
        s3["traces_found"] = int(m.group(1))
        s3["lcs"] = int(m.group(2))
        s3["trace_length"] = int(m.group(3))

    # Extract all trace sequences
    trace_seqs = []
    for tm in re.finditer(r"Trace \d+:\s*\[([^\]]+)\]", text):
        seq = [int(x) for x in tm.group(1).split(",") if x.strip()]
        trace_seqs.append(seq)
    s3["trace_sequences"] = trace_seqs

    step3_dur = re.search(
        r"STEP 3.*?Duration\s*:\s*([\d.]+)s", text, re.DOTALL
    )
    if step3_dur:
        s3["step_duration_s"] = float(step3_dur.group(1))

    # ── Step 4 ─────────────────────────────────────────────────────────────
    s4 = result["step4_store"]

    m = re.search(r"Execution trace written to:\s*(.+)", text)
    if m:
        s4["output_file"] = m.group(1).strip()

    step4_dur = re.search(
        r"STEP 4.*?Duration\s*:\s*([\d.]+)s", text, re.DOTALL
    )
    if step4_dur:
        s4["step_duration_s"] = float(step4_dur.group(1))

    # ── Total ──────────────────────────────────────────────────────────────
    m = re.search(r"Total time:\s*([\d.]+)s", text)
    if m:
        result["total_time_s"] = float(m.group(1))

    return result


def parse_execution_json(json_path: Path) -> dict:
    """Parse an execution_*.json output file."""
    if not json_path.exists():
        return {}
    try:
        data = json.loads(json_path.read_text())
    except Exception:
        return {}

    traces = data.get("replay_traces", [])
    action_types = set()
    trace0_len = 0
    if traces:
        trace0 = traces[0].get("trace", [])
        trace0_len = len(trace0)
        for action in trace0:
            t = action.get("action", {}).get("type")
            if t:
                action_types.add(t)

    return {
        "replay_trace_count": len(traces),
        "trace0_action_count": trace0_len,
        "action_types": sorted(action_types),
    }


def get_video_size_mb(path: Path) -> Optional[float]:
    if path.exists():
        return round(path.stat().st_size / (1024 * 1024), 2)
    return None


def count_files(directory: Path, pattern: str = "*") -> int:
    if not directory.exists():
        return 0
    return len(list(directory.glob(pattern)))


def extract_all() -> dict:
    """Walk the repo and build the full data structure."""
    runs = []

    app_dirs = sorted(ROOT.glob("app_*"))
    for app_dir in app_dirs:
        app_name = app_dir.name.replace("app_", "")
        utg_dirs = sorted(app_dir.glob("utg*"))

        for utg_dir in utg_dirs:
            utg_name = utg_dir.name

            # ── inputs shared between srv/hhv ──────────────────────────────
            artifacts_dir = utg_dir / "input" / "artifacts"
            artifact_count = count_files(artifacts_dir, "*.png")

            utg_json = utg_dir / "input" / "utg.json"

            for video_type in ("srv", "hhv"):
                log_path = find_latest_log(utg_dir, video_type)
                if log_path is None:
                    continue  # no valid run for this type

                # Video file
                if video_type == "srv":
                    vid_glob = list((utg_dir / "input" / "screenrec").glob("*.mp4"))
                else:
                    vid_glob = list((utg_dir / "input" / "handheld").glob("*.mp4"))
                video_size_mb = get_video_size_mb(vid_glob[0]) if vid_glob else None

                # Execution JSON
                exec_json_name = f"execution_{video_type}_{app_name}.json"
                exec_json_path = utg_dir / "output" / exec_json_name
                exec_data = parse_execution_json(exec_json_path)

                # Saved keyframe files in output/keyframes/
                kf_dir = utg_dir / "output" / "keyframes"
                saved_keyframes = count_files(kf_dir, "*.png")

                # Parse log
                log_data = parse_log(log_path)

                # Backfill utg graph info from step3 (same for both types)
                s3 = log_data["step3_find_trace"]

                run = {
                    "app": app_name,
                    "utg": utg_name,
                    "video_type": video_type,
                    "log_file": str(log_path.relative_to(ROOT)),
                    "inputs": {
                        "video_path": str(vid_glob[0].relative_to(ROOT)) if vid_glob else None,
                        "video_size_mb": video_size_mb,
                        "artifact_count": artifact_count,
                        "utg_vertices": s3.get("utg_vertices"),
                        "utg_edges": s3.get("utg_edges"),
                    },
                    "step1_keyframe_location": {
                        **log_data["step1_keyframe_location"],
                        "saved_keyframe_files": saved_keyframes,
                    },
                    "step2_gui_mapping": log_data["step2_gui_mapping"],
                    "step3_find_trace": {k: v for k, v in s3.items()
                                         if k not in ("utg_vertices", "utg_edges")},
                    "step4_store": log_data["step4_store"],
                    "total_time_s": log_data["total_time_s"],
                    "execution_json": exec_data,
                }
                runs.append(run)

    data = {
        "generated_at": datetime.now().isoformat(),
        "root": str(ROOT),
        "run_count": len(runs),
        "runs": runs,
    }
    return data


# ══════════════════════════════════════════════════════════════════════════════
# REPORT
# ══════════════════════════════════════════════════════════════════════════════

def load_data() -> dict:
    if not DATA_FILE.exists():
        print(f"ERROR: {DATA_FILE} not found. Run --extract first.", file=sys.stderr)
        sys.exit(1)
    return json.loads(DATA_FILE.read_text())


def fmt(val, fmt_str="{}", fallback="—"):
    if val is None:
        return fallback
    try:
        return fmt_str.format(val)
    except Exception:
        return str(val)


def build_report(data: dict) -> str:
    runs = data["runs"]
    lines = []

    lines.append(f"# GIFdroid Analysis Report")
    lines.append(f"Generated: {data['generated_at']}")
    lines.append(f"Total runs: {data['run_count']}\n")

    # ── Table 1: Master comparison ─────────────────────────────────────────
    lines.append("## Table 1: Master Comparison (all runs)\n")
    headers = [
        "App", "UTG", "Type",
        "Video MB", "Artifacts", "UTG V", "UTG E",
        "Frames", "Keyframes", "KF Ratio",
        "Score Mean", "Score Median", "Score Min", "Score Max",
        "Unique Screens",
        "Cand Paths", "Traces", "LCS", "Trace Len",
        "Total Time (s)",
    ]
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("| " + " | ".join(["---"] * len(headers)) + " |")

    for r in runs:
        s1 = r["step1_keyframe_location"]
        s2 = r["step2_gui_mapping"]
        s3 = r["step3_find_trace"]
        inp = r["inputs"]
        frames = s1.get("frames_decoded")
        kf = s1.get("keyframes_detected")
        kf_ratio = round(frames / kf, 1) if frames and kf else None

        row = [
            r["app"], r["utg"], r["video_type"].upper(),
            fmt(inp.get("video_size_mb"), "{:.1f}"),
            fmt(inp.get("artifact_count"), "{}"),
            fmt(inp.get("utg_vertices"), "{}"),
            fmt(inp.get("utg_edges"), "{}"),
            fmt(frames, "{}"),
            fmt(kf, "{}"),
            fmt(kf_ratio, "{:.1f}"),
            fmt(s2.get("score_mean"), "{:.3f}"),
            fmt(s2.get("score_median"), "{:.3f}"),
            fmt(s2.get("score_min"), "{:.3f}"),
            fmt(s2.get("score_max"), "{:.3f}"),
            fmt(s2.get("unique_screens_mapped"), "{}"),
            fmt(s3.get("candidate_paths"), "{}"),
            fmt(s3.get("traces_found"), "{}"),
            fmt(s3.get("lcs"), "{}"),
            fmt(s3.get("trace_length"), "{}"),
            fmt(r.get("total_time_s"), "{:.1f}"),
        ]
        lines.append("| " + " | ".join(row) + " |")

    lines.append("")

    # ── Table 2: Timing breakdown ──────────────────────────────────────────
    lines.append("## Table 2: Timing Breakdown per Step (seconds)\n")
    headers2 = ["App", "UTG", "Type", "Step1 (s)", "Step2 (s)", "Step3 (s)", "Step4 (s)", "Total (s)"]
    lines.append("| " + " | ".join(headers2) + " |")
    lines.append("| " + " | ".join(["---"] * len(headers2)) + " |")

    for r in runs:
        s1 = r["step1_keyframe_location"]
        s2 = r["step2_gui_mapping"]
        s3 = r["step3_find_trace"]
        s4 = r["step4_store"]
        row = [
            r["app"], r["utg"], r["video_type"].upper(),
            fmt(s1.get("step_duration_s"), "{:.1f}"),
            fmt(s2.get("step_duration_s"), "{:.1f}"),
            fmt(s3.get("step_duration_s"), "{:.3f}"),
            fmt(s4.get("step_duration_s"), "{:.3f}"),
            fmt(r.get("total_time_s"), "{:.1f}"),
        ]
        lines.append("| " + " | ".join(row) + " |")

    lines.append("")

    # ── Table 3: SRV vs HHV side-by-side per (app, utg) ──────────────────
    lines.append("## Table 3: SRV vs HHV Side-by-Side\n")
    headers3 = [
        "App", "UTG",
        "SRV MB", "HHV MB", "MB Ratio (HHV/SRV)",
        "SRV Frames", "HHV Frames",
        "SRV KF", "HHV KF",
        "SRV Score Mean", "HHV Score Mean",
        "SRV Trace Len", "HHV Trace Len",
        "SRV Time (s)", "HHV Time (s)",
    ]
    lines.append("| " + " | ".join(headers3) + " |")
    lines.append("| " + " | ".join(["---"] * len(headers3)) + " |")

    # Build lookup: (app, utg, type) -> run
    lookup = {(r["app"], r["utg"], r["video_type"]): r for r in runs}
    pairs = sorted(set((r["app"], r["utg"]) for r in runs))

    for app, utg in pairs:
        srv = lookup.get((app, utg, "srv"))
        hhv = lookup.get((app, utg, "hhv"))

        def get_val(run, *keys):
            if run is None:
                return None
            obj = run
            for k in keys:
                if not isinstance(obj, dict):
                    return None
                obj = obj.get(k)
            return obj

        srv_mb = get_val(srv, "inputs", "video_size_mb")
        hhv_mb = get_val(hhv, "inputs", "video_size_mb")
        ratio = round(hhv_mb / srv_mb, 1) if hhv_mb and srv_mb else None

        row = [
            app, utg,
            fmt(srv_mb, "{:.1f}"),
            fmt(hhv_mb, "{:.1f}"),
            fmt(ratio, "{:.1f}x"),
            fmt(get_val(srv, "step1_keyframe_location", "frames_decoded"), "{}"),
            fmt(get_val(hhv, "step1_keyframe_location", "frames_decoded"), "{}"),
            fmt(get_val(srv, "step1_keyframe_location", "keyframes_detected"), "{}"),
            fmt(get_val(hhv, "step1_keyframe_location", "keyframes_detected"), "{}"),
            fmt(get_val(srv, "step2_gui_mapping", "score_mean"), "{:.3f}"),
            fmt(get_val(hhv, "step2_gui_mapping", "score_mean"), "{:.3f}"),
            fmt(get_val(srv, "step3_find_trace", "trace_length"), "{}"),
            fmt(get_val(hhv, "step3_find_trace", "trace_length"), "{}"),
            fmt(get_val(srv, "total_time_s"), "{:.1f}"),
            fmt(get_val(hhv, "total_time_s"), "{:.1f}"),
        ]
        lines.append("| " + " | ".join(row) + " |")

    lines.append("")

    # ── Table 4: Confidence score stats ───────────────────────────────────
    lines.append("## Table 4: Confidence Score Statistics\n")
    headers4 = ["App", "UTG", "Type", "N Scores", "Mean", "Median", "Stdev", "Min", "Max"]
    lines.append("| " + " | ".join(headers4) + " |")
    lines.append("| " + " | ".join(["---"] * len(headers4)) + " |")

    for r in runs:
        s2 = r["step2_gui_mapping"]
        scores = s2.get("confidence_scores", [])
        row = [
            r["app"], r["utg"], r["video_type"].upper(),
            str(len(scores)),
            fmt(s2.get("score_mean"), "{:.4f}"),
            fmt(s2.get("score_median"), "{:.4f}"),
            fmt(s2.get("score_stdev"), "{:.4f}"),
            fmt(s2.get("score_min"), "{:.4f}"),
            fmt(s2.get("score_max"), "{:.4f}"),
        ]
        lines.append("| " + " | ".join(row) + " |")

    lines.append("")

    # ── Table 5: Execution trace output ───────────────────────────────────
    lines.append("## Table 5: Execution JSON Output\n")
    headers5 = ["App", "UTG", "Type", "Replay Traces", "Actions in Trace[0]", "Action Types"]
    lines.append("| " + " | ".join(headers5) + " |")
    lines.append("| " + " | ".join(["---"] * len(headers5)) + " |")

    for r in runs:
        ej = r.get("execution_json", {})
        row = [
            r["app"], r["utg"], r["video_type"].upper(),
            fmt(ej.get("replay_trace_count"), "{}"),
            fmt(ej.get("trace0_action_count"), "{}"),
            ", ".join(ej.get("action_types", [])) or "—",
        ]
        lines.append("| " + " | ".join(row) + " |")

    lines.append("")

    # ── Summary stats ──────────────────────────────────────────────────────
    lines.append("## Summary Statistics\n")

    srv_runs = [r for r in runs if r["video_type"] == "srv"]
    hhv_runs = [r for r in runs if r["video_type"] == "hhv"]

    def agg_key(run_list, *keys):
        vals = []
        for r in run_list:
            obj = r
            for k in keys:
                if isinstance(obj, dict):
                    obj = obj.get(k)
                else:
                    obj = None
                    break
            if obj is not None:
                vals.append(obj)
        if not vals:
            return None, None, None
        return round(statistics.mean(vals), 2), round(min(vals), 2), round(max(vals), 2)

    lines.append("### Total Pipeline Time")
    srv_mean, srv_min, srv_max = agg_key(srv_runs, "total_time_s")
    hhv_mean, hhv_min, hhv_max = agg_key(hhv_runs, "total_time_s")
    lines.append(f"- SRV: mean={srv_mean}s, min={srv_min}s, max={srv_max}s")
    lines.append(f"- HHV: mean={hhv_mean}s, min={hhv_min}s, max={hhv_max}s\n")

    lines.append("### Keyframes Detected")
    srv_mean, srv_min, srv_max = agg_key(srv_runs, "step1_keyframe_location", "keyframes_detected")
    hhv_mean, hhv_min, hhv_max = agg_key(hhv_runs, "step1_keyframe_location", "keyframes_detected")
    lines.append(f"- SRV: mean={srv_mean}, min={srv_min}, max={srv_max}")
    lines.append(f"- HHV: mean={hhv_mean}, min={hhv_min}, max={hhv_max}\n")

    lines.append("### Confidence Score Mean (across all runs)")
    all_srv_scores = [s for r in srv_runs for s in r["step2_gui_mapping"].get("confidence_scores", [])]
    all_hhv_scores = [s for r in hhv_runs for s in r["step2_gui_mapping"].get("confidence_scores", [])]
    if all_srv_scores:
        lines.append(f"- SRV: mean={round(statistics.mean(all_srv_scores),4)}, "
                     f"median={round(statistics.median(all_srv_scores),4)}, "
                     f"stdev={round(statistics.stdev(all_srv_scores),4)}")
    if all_hhv_scores:
        lines.append(f"- HHV: mean={round(statistics.mean(all_hhv_scores),4)}, "
                     f"median={round(statistics.median(all_hhv_scores),4)}, "
                     f"stdev={round(statistics.stdev(all_hhv_scores),4)}")
    lines.append("")

    lines.append("### Trace Length")
    srv_mean, srv_min, srv_max = agg_key(srv_runs, "step3_find_trace", "trace_length")
    hhv_mean, hhv_min, hhv_max = agg_key(hhv_runs, "step3_find_trace", "trace_length")
    lines.append(f"- SRV: mean={srv_mean}, min={srv_min}, max={srv_max}")
    lines.append(f"- HHV: mean={hhv_mean}, min={hhv_min}, max={hhv_max}\n")

    return "\n".join(lines)


# ══════════════════════════════════════════════════════════════════════════════
# PLOT
# ══════════════════════════════════════════════════════════════════════════════

def build_plots(data: dict):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        import matplotlib.patches as mpatches
        import numpy as np
    except ImportError:
        print("matplotlib not installed. Skipping plots.", file=sys.stderr)
        return

    PLOTS_DIR.mkdir(exist_ok=True)
    runs = data["runs"]
    srv_runs = [r for r in runs if r["video_type"] == "srv"]
    hhv_runs = [r for r in runs if r["video_type"] == "hhv"]

    def label(r):
        return f"{r['app'][:6]}\n{r['utg']}"

    # ── Plot 1: Total pipeline time SRV vs HHV ────────────────────────────
    fig, ax = plt.subplots(figsize=(14, 5))
    labels = [f"{r['app'][:8]}/{r['utg']}" for r in srv_runs]
    srv_times = [r.get("total_time_s") or 0 for r in srv_runs]

    # Match HHV runs to SRV order
    hhv_lookup = {(r["app"], r["utg"]): r for r in hhv_runs}
    hhv_times = [hhv_lookup.get((r["app"], r["utg"]), {}).get("total_time_s") or 0 for r in srv_runs]

    x = np.arange(len(labels))
    width = 0.35
    ax.bar(x - width/2, srv_times, width, label="SRV", color="#4C72B0")
    ax.bar(x + width/2, hhv_times, width, label="HHV", color="#DD8452")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha="right", fontsize=8)
    ax.set_ylabel("Total Time (s)")
    ax.set_title("Total Pipeline Time: SRV vs HHV")
    ax.legend()
    plt.tight_layout()
    fig.savefig(PLOTS_DIR / "timing_total.png", dpi=150)
    plt.close(fig)

    # ── Plot 2: Timing stacked bar (step breakdown) ────────────────────────
    fig, axes = plt.subplots(1, 2, figsize=(18, 6), sharey=False)
    colors = ["#4878D0", "#EE854A", "#6ACC65", "#D65F5F"]
    step_keys = [
        ("step1_keyframe_location", "step_duration_s", "Step1 KF"),
        ("step2_gui_mapping", "step_duration_s", "Step2 GUI"),
        ("step3_find_trace", "step_duration_s", "Step3 Trace"),
        ("step4_store", "step_duration_s", "Step4 Store"),
    ]

    for ax, run_list, title in [(axes[0], srv_runs, "SRV"), (axes[1], hhv_runs, "HHV")]:
        lbls = [f"{r['app'][:6]}/{r['utg']}" for r in run_list]
        bottoms = np.zeros(len(run_list))
        for (step, key, name), color in zip(step_keys, colors):
            vals = np.array([r.get(step, {}).get(key) or 0 for r in run_list])
            ax.bar(lbls, vals, bottom=bottoms, label=name, color=color)
            bottoms += vals
        ax.set_title(f"Step Timing Breakdown — {title}")
        ax.set_ylabel("Time (s)")
        ax.set_xticklabels(lbls, rotation=45, ha="right", fontsize=7)
        ax.legend(fontsize=8)

    plt.tight_layout()
    fig.savefig(PLOTS_DIR / "timing_breakdown.png", dpi=150)
    plt.close(fig)

    # ── Plot 3: Keyframes detected ────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(14, 5))
    srv_kf = [r["step1_keyframe_location"].get("keyframes_detected") or 0 for r in srv_runs]
    hhv_kf = [hhv_lookup.get((r["app"], r["utg"]), {}).get("step1_keyframe_location", {}).get("keyframes_detected") or 0 for r in srv_runs]
    ax.bar(x - width/2, srv_kf, width, label="SRV", color="#4C72B0")
    ax.bar(x + width/2, hhv_kf, width, label="HHV", color="#DD8452")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha="right", fontsize=8)
    ax.set_ylabel("Keyframes Detected")
    ax.set_title("Keyframes Detected: SRV vs HHV")
    ax.legend()
    plt.tight_layout()
    fig.savefig(PLOTS_DIR / "keyframe_counts.png", dpi=150)
    plt.close(fig)

    # ── Plot 4: Confidence score distributions (boxplot) ──────────────────
    fig, axes = plt.subplots(1, 2, figsize=(16, 6), sharey=True)
    for ax, run_list, title in [(axes[0], srv_runs, "SRV"), (axes[1], hhv_runs, "HHV")]:
        score_data = [r["step2_gui_mapping"].get("confidence_scores", []) for r in run_list]
        score_data = [s if s else [0] for s in score_data]
        lbls = [f"{r['app'][:6]}/{r['utg']}" for r in run_list]
        ax.boxplot(score_data, tick_labels=lbls, vert=True)
        ax.set_title(f"Confidence Score Distribution — {title}")
        ax.set_ylabel("Confidence Score")
        ax.tick_params(axis="x", rotation=45, labelsize=7)
    plt.tight_layout()
    fig.savefig(PLOTS_DIR / "confidence_scores.png", dpi=150)
    plt.close(fig)

    # ── Plot 5: Video size vs total pipeline time ─────────────────────────
    fig, ax = plt.subplots(figsize=(8, 6))
    for run_list, color, marker, label_str in [
        (srv_runs, "#4C72B0", "o", "SRV"),
        (hhv_runs, "#DD8452", "s", "HHV"),
    ]:
        sizes = [r["inputs"].get("video_size_mb") or 0 for r in run_list]
        times = [r.get("total_time_s") or 0 for r in run_list]
        ax.scatter(sizes, times, c=color, marker=marker, label=label_str, alpha=0.7, s=60)
    ax.set_xlabel("Video Size (MB)")
    ax.set_ylabel("Total Pipeline Time (s)")
    ax.set_title("Video Size vs Pipeline Time")
    ax.legend()
    plt.tight_layout()
    fig.savefig(PLOTS_DIR / "video_size_vs_time.png", dpi=150)
    plt.close(fig)

    # ── Plot 6: Mean confidence per run (scatter, colored by type) ────────
    fig, ax = plt.subplots(figsize=(14, 5))
    for run_list, color, marker, label_str in [
        (srv_runs, "#4C72B0", "o", "SRV"),
        (hhv_runs, "#DD8452", "s", "HHV"),
    ]:
        lbls = [f"{r['app'][:6]}/{r['utg']}" for r in run_list]
        means = [r["step2_gui_mapping"].get("score_mean") or 0 for r in run_list]
        ax.scatter(range(len(lbls)), means, c=color, marker=marker, label=label_str, s=80)
        for i, (lbl, mean) in enumerate(zip(lbls, means)):
            pass  # could annotate
    ax.set_xticks(range(len(srv_runs)))
    ax.set_xticklabels([f"{r['app'][:6]}/{r['utg']}" for r in srv_runs], rotation=45, ha="right", fontsize=7)
    ax.set_ylabel("Mean Confidence Score")
    ax.set_title("Mean Confidence Score per Run")
    ax.legend()
    plt.tight_layout()
    fig.savefig(PLOTS_DIR / "confidence_mean.png", dpi=150)
    plt.close(fig)

    print(f"Plots saved to {PLOTS_DIR}/")


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description="GIFdroid analysis tool")
    parser.add_argument("--extract", action="store_true", help="Scan repo and write gifdroid_data.json")
    parser.add_argument("--report", action="store_true", help="Generate report.md from gifdroid_data.json")
    parser.add_argument("--plot", action="store_true", help="Generate plots from gifdroid_data.json")
    args = parser.parse_args()

    if not any([args.extract, args.report, args.plot]):
        parser.print_help()
        sys.exit(0)

    ANALYSIS_DIR.mkdir(exist_ok=True)

    if args.extract:
        print("Extracting data from all runs...")
        data = extract_all()
        DATA_FILE.write_text(json.dumps(data, indent=2))
        print(f"Written: {DATA_FILE}  ({data['run_count']} runs)")

    if args.report:
        data = load_data()
        report = build_report(data)
        REPORT_FILE.write_text(report)
        print(report)
        print(f"\nReport written: {REPORT_FILE}")

    if args.plot:
        data = load_data()
        build_plots(data)


if __name__ == "__main__":
    main()
