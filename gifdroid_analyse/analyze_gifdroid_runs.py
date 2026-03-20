#!/usr/bin/env python3

import json
import pathlib
import re
import statistics
from collections import Counter


SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent


def load_json(path: pathlib.Path):
    try:
        return json.loads(path.read_text())
    except Exception:
        return None


def parse_utg(path: pathlib.Path) -> dict:
    data = load_json(path)
    if not isinstance(data, dict):
        return {}
    events = data.get("events") or []
    sources = set()
    destinations = set()
    exec_results = Counter()
    launch_events = 0
    for event in events:
        if not isinstance(event, dict):
            continue
        if "sourceScreenId" in event:
            sources.add(event["sourceScreenId"])
        if "destinationScreenId" in event:
            destinations.add(event["destinationScreenId"])
        if event.get("launch"):
            launch_events += 1
        if event.get("executionResult") is not None:
            exec_results[event["executionResult"]] += 1
    return {
        "utg_events": len(events),
        "utg_unique_sources": len(sources),
        "utg_unique_destinations": len(destinations),
        "utg_unique_screens": len(sources | destinations),
        "utg_launch_events": launch_events,
        "utg_exec_results": dict(exec_results),
    }


def parse_artifacts(path: pathlib.Path) -> dict:
    if not path.exists():
        return {}
    pngs = sorted(path.glob("*.png"))
    main_pngs = [p for p in pngs if p.name != "artifacts_sitemap.png"]
    return {
        "artifact_pngs": len(pngs),
        "artifact_main_pngs": len(main_pngs),
        "has_sitemap": any(p.name == "artifacts_sitemap.png" for p in pngs),
    }


def parse_execution(path: pathlib.Path) -> dict:
    data = load_json(path)
    if not isinstance(data, dict):
        return {"output_exists": path.exists()}
    replay_traces = data.get("replay_traces") or []
    trace_lengths = []
    action_types = Counter()
    destinations = set()
    for replay_trace in replay_traces:
        trace = replay_trace.get("trace") or []
        trace_lengths.append(len(trace))
        for step in trace:
            if not isinstance(step, dict):
                continue
            action = step.get("action") or {}
            action_type = action.get("type")
            if action_type:
                action_types[action_type] += 1
            if "destinationScreenId" in step:
                destinations.add(step["destinationScreenId"])
    return {
        "output_exists": True,
        "replay_traces": len(replay_traces),
        "trace_lengths": trace_lengths,
        "trace_len_total": sum(trace_lengths),
        "trace_len_max": max(trace_lengths) if trace_lengths else 0,
        "trace_action_types": dict(action_types),
        "trace_unique_destinations": len(destinations),
    }


def parse_log(path: pathlib.Path) -> dict:
    if not path.exists():
        return {}
    text = path.read_text(errors="replace")
    info = {
        "log_exists": True,
        "log_lines": len(text.splitlines()),
        "skipped_existing_output": "Output already exists, skipping" in text,
        "has_error": bool(re.search(r"\b(ERROR|Traceback)\b", text)),
        "pipeline_complete": "Pipeline complete." in text,
    }
    scalar_patterns = {
        "keyframes_found": r"Keyframes found\s*:\s*(\d+)",
        "screenshots_loaded": r"load_screenshots:\s*(\d+) screenshots loaded",
        "candidate_traces_found": r"Candidate traces found\s*:\s*(\d+)",
        "duration_seconds": r"Duration\s*:\s*([0-9.]+)s",
        "total_time_seconds": r"Total time:\s*([0-9.]+)s",
    }
    for key, pattern in scalar_patterns.items():
        match = re.search(pattern, text)
        if match:
            value = match.group(1)
            info[key] = float(value) if "." in value else int(value)
    mapping_matches = re.findall(r'mapping: best match "([^"]+)" \(score=([0-9.]+)\)', text)
    if mapping_matches:
        scores = [float(score) for _, score in mapping_matches]
        artifacts = [name for name, _ in mapping_matches]
        top_artifact, top_count = Counter(artifacts).most_common(1)[0]
        info.update(
            {
                "mapping_steps": len(mapping_matches),
                "mapping_unique_artifacts": len(set(artifacts)),
                "mapping_score_avg": round(statistics.mean(scores), 3),
                "mapping_score_min": min(scores),
                "mapping_score_max": max(scores),
                "mapping_top_artifact": top_artifact,
                "mapping_top_artifact_hits": top_count,
            }
        )
    warning_lines = [line for line in text.splitlines() if "WARNING" in line]
    if warning_lines:
        info["warnings"] = warning_lines[-3:]
    return info


def collect_records() -> list[dict]:
    records = []
    for app_dir in sorted(p for p in ROOT.iterdir() if p.is_dir() and p.name.startswith("app_")):
        app_name = app_dir.name.removeprefix("app_")
        for utg_name in ("utg01", "utg02"):
            run_dir = app_dir / utg_name
            if not run_dir.exists():
                continue
            record = {"app": app_name, "utg": utg_name}
            record.update(parse_utg(run_dir / "input" / "utg.json"))
            record.update(parse_artifacts(run_dir / "input" / "artifacts"))
            for mode in ("hhv", "srv"):
                prefix = f"{mode}_"
                log_files = sorted(run_dir.glob(f"gifdroid_*_{mode}.log"))
                output_path = run_dir / "output" / f"execution_{mode}_{app_name}.json"
                record[prefix + "log_file"] = str(log_files[-1].relative_to(ROOT)) if log_files else None
                record[prefix + "output_file"] = str(output_path.relative_to(ROOT)) if output_path.exists() else None
                for key, value in parse_execution(output_path).items():
                    record[prefix + key] = value
                if log_files:
                    for key, value in parse_log(log_files[-1]).items():
                        record[prefix + key] = value
            records.append(record)
    return records


def fmt_mode(record: dict, mode: str) -> str:
    prefix = f"{mode}_"
    if not record.get(prefix + "output_exists") and not record.get(prefix + "log_file"):
        return "missing"
    parts = []
    skipped = bool(record.get(prefix + "skipped_existing_output"))
    if skipped:
        parts.append("skipped")
    if record.get(prefix + "output_exists"):
        traces = record.get(prefix + "replay_traces", 0)
        trace_total = record.get(prefix + "trace_len_total", 0)
        parts.append(f"out:{traces} trace(s), {trace_total} step(s)")
    else:
        parts.append("no output")
    if record.get(prefix + "keyframes_found") is not None:
        parts.append(f"kf:{record[prefix + 'keyframes_found']}")
    if record.get(prefix + "mapping_unique_artifacts") is not None:
        parts.append(f"map:{record[prefix + 'mapping_unique_artifacts']} unique")
    if record.get(prefix + "log_file") and not skipped and record.get(prefix + "pipeline_complete") is False:
        parts.append("incomplete")
    warnings = record.get(prefix + "warnings") or []
    if warnings:
        parts.append("warning")
    return ", ".join(parts)


def build_markdown(records: list[dict]) -> str:
    lines = []
    lines.append("# GIFdroid Run Analysis")
    lines.append("")
    lines.append("## Comparison Points")
    lines.append("")
    lines.append("- `utg.json`: event count, unique screens, and execution-result distribution.")
    lines.append("- Input artifacts: total PNGs, screenshots excluding `artifacts_sitemap.png`, and whether the sitemap exists.")
    lines.append("- Outputs: presence of `execution_<hhv/srv>_<app>.json`, replay-trace count, total trace length, max trace length, and action-type mix.")
    lines.append("- Logs: keyframe count, screenshots loaded, mapping diversity, average mapping score, skipped runs, incomplete pipelines, and warnings.")
    lines.append("")
    lines.append("## Per-Run Summary")
    lines.append("")
    lines.append("| App | Run | UTG events | Screens | Artifacts | HHV | SRV |")
    lines.append("| --- | --- | ---: | ---: | ---: | --- | --- |")
    for record in records:
        lines.append(
            f"| {record['app']} | {record['utg']} | {record.get('utg_events', '-')}"
            f" | {record.get('utg_unique_screens', '-')}"
            f" | {record.get('artifact_main_pngs', '-')}"
            f" | {fmt_mode(record, 'hhv')}"
            f" | {fmt_mode(record, 'srv')} |"
        )
    lines.append("")
    lines.append("## UTG01 vs UTG02 Deltas")
    lines.append("")
    lines.append("| App | Events delta | Screen delta | Artifact delta |")
    lines.append("| --- | ---: | ---: | ---: |")
    grouped = {}
    for record in records:
        grouped.setdefault(record["app"], {})[record["utg"]] = record
    for app, app_records in sorted(grouped.items()):
        first = app_records.get("utg01", {})
        second = app_records.get("utg02", {})
        def delta(key: str):
            a = first.get(key)
            b = second.get(key)
            if a is None or b is None:
                return "-"
            return b - a
        lines.append(
            f"| {app} | {delta('utg_events')} | {delta('utg_unique_screens')} | {delta('artifact_main_pngs')} |"
        )
    lines.append("")
    lines.append("## Notable Findings")
    lines.append("")
    issues = []
    for record in records:
        app_run = f"{record['app']} {record['utg']}"
        for mode in ("hhv", "srv"):
            prefix = f"{mode}_"
            if record.get(prefix + "log_file") and not record.get(prefix + "pipeline_complete") and not record.get(prefix + "skipped_existing_output"):
                issues.append(f"- {app_run} {mode.upper()}: log exists but pipeline did not complete.")
            if record.get(prefix + "output_exists") and record.get(prefix + "replay_traces") == 0:
                issues.append(f"- {app_run} {mode.upper()}: output exists but contains zero replay traces.")
            if record.get(prefix + "mapping_unique_artifacts") == 1 and record.get(prefix + "mapping_steps", 0) >= 5:
                top = record.get(prefix + "mapping_top_artifact")
                hits = record.get(prefix + "mapping_top_artifact_hits")
                issues.append(
                    f"- {app_run} {mode.upper()}: all or nearly all keyframes collapsed onto `{top}` ({hits}/{record.get(prefix + 'mapping_steps')} matches)."
                )
    if issues:
        lines.extend(issues)
    else:
        lines.append("- No obvious anomalies detected by the current heuristics.")
    lines.append("")
    lines.append("## Raw Data")
    lines.append("")
    lines.append("See `gifdroid_run_analysis.json` for the full machine-readable extraction.")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    records = collect_records()
    json_path = SCRIPT_DIR / "gifdroid_run_analysis.json"
    md_path = SCRIPT_DIR / "gifdroid_run_analysis.md"
    json_path.write_text(json.dumps(records, indent=2, sort_keys=True))
    md_path.write_text(build_markdown(records))
    print(f"Wrote {json_path.relative_to(ROOT)}")
    print(f"Wrote {md_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
