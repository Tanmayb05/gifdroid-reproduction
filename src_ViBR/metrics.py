"""Metrics collection and reporting for ViBR runs."""

from __future__ import annotations

import time
from collections import Counter
from dataclasses import dataclass, field
from typing import Any


@dataclass
class LLMCall:
    """Record of a single LLM API call."""
    kind: str  # "region_detection", "state_comparison", "action_inference", etc.
    elapsed_sec: float
    prompt_tokens: int = 0
    output_tokens: int = 0
    error: str | None = None


@dataclass
class RunMetrics:
    """Metrics collected during a ViBR run."""
    app_name: str
    video_type: str
    video_path: str
    status: str = "unknown"  # "success", "failed", "partial"
    total_scenes: int = 0
    scenes_processed: int = 0
    scenes_failed: int = 0
    action_types: dict[str, int] = field(default_factory=dict)
    llm_calls: list[LLMCall] = field(default_factory=list)
    wall_time_sec: float = 0.0

    def add_scene(self, scene_num: int, success: bool = True):
        """Record a scene result."""
        self.total_scenes = max(self.total_scenes, scene_num + 1)
        self.scenes_processed += 1
        if not success:
            self.scenes_failed += 1

    def add_action(self, action_type: str):
        """Record an action."""
        self.action_types[action_type] = self.action_types.get(action_type, 0) + 1

    def add_llm_call(self, kind: str, elapsed_sec: float, prompt_tokens: int = 0, output_tokens: int = 0, error: str | None = None):
        """Record an LLM API call."""
        self.llm_calls.append(LLMCall(
            kind=kind,
            elapsed_sec=elapsed_sec,
            prompt_tokens=prompt_tokens,
            output_tokens=output_tokens,
            error=error,
        ))

    def format_summary(self) -> str:
        """Format metrics as a summary string for logging."""
        lines = []
        lines.append("=" * 72)
        lines.append("RUN SUMMARY")
        lines.append(f"  App         : {self.app_name}")
        lines.append(f"  Video type  : {self.video_type}")
        lines.append(f"  Status      : {self.status}")
        lines.append(f"  Scenes      : {self.scenes_processed}/{self.total_scenes}")

        # Actions breakdown
        if self.action_types:
            actions_str = "  ".join(f"{k}={v}" for k, v in sorted(self.action_types.items()))
        else:
            actions_str = "none"
        lines.append(f"  Actions     : {actions_str}")

        # LLM calls breakdown
        if self.llm_calls:
            call_kinds = Counter(c.kind for c in self.llm_calls if c.error is None)
            calls_str = "  ".join(f"{k}={v}" for k, v in sorted(call_kinds.items()))

            # Latency stats
            latencies = [c.elapsed_sec for c in self.llm_calls if c.error is None]
            if latencies:
                lat_str = (
                    f"min={min(latencies):.1f}s  max={max(latencies):.1f}s  "
                    f"avg={sum(latencies)/len(latencies):.1f}s  total={sum(latencies):.1f}s"
                )
            else:
                lat_str = "n/a"

            # Token stats
            total_prompt = sum(c.prompt_tokens for c in self.llm_calls)
            total_output = sum(c.output_tokens for c in self.llm_calls)
            if total_prompt or total_output:
                tokens_str = (
                    f"prompt={total_prompt:,}  output={total_output:,}  "
                    f"total={total_prompt + total_output:,}"
                )
            else:
                tokens_str = "n/a"
        else:
            calls_str = lat_str = tokens_str = "n/a"

        lines.append(f"  LLM calls   : {calls_str}")
        lines.append(f"  LLM latency : {lat_str}")
        lines.append(f"  Tokens used : {tokens_str}")
        lines.append(f"  Wall time   : {int(self.wall_time_sec) // 60}m {int(self.wall_time_sec) % 60}s")
        lines.append("=" * 72)

        return "\n".join(lines)


class MetricsCollector:
    """Context manager for collecting metrics during a run."""

    def __init__(self, app_name: str, video_type: str, video_path: str):
        self.metrics = RunMetrics(app_name=app_name, video_type=video_type, video_path=str(video_path))
        self.start_time = None

    def __enter__(self) -> RunMetrics:
        self.start_time = time.perf_counter()
        return self.metrics

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.start_time is not None:
            self.metrics.wall_time_sec = time.perf_counter() - self.start_time

        if exc_type is not None:
            self.metrics.status = "failed"
        elif self.metrics.status == "unknown":
            self.metrics.status = "success"

        return False
