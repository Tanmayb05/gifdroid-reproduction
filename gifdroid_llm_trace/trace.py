from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List


@dataclass(frozen=True)
class TraceAction:
    action_type: str
    target: str
    details: str


@dataclass(frozen=True)
class TraceStep:
    step_index: int
    timestamp_sec: float
    frame_file: str
    screen_description: str
    action: TraceAction
    confidence: float


class TraceBuilder:
    """Build deterministic execution trace payloads."""

    def build(
        self,
        *,
        video_path: Path,
        llm_name: str,
        video_type: str,
        app_name: str,
        utg_number: str,
        generated_at: datetime,
        steps: List[TraceStep],
    ) -> Dict[str, Any]:
        generated_at_iso = generated_at.astimezone(timezone.utc).isoformat()
        replay_trace = [
            {
                "step_index": step.step_index,
                "timestamp_sec": round(step.timestamp_sec, 3),
                "frame_file": step.frame_file,
                "screen_description": step.screen_description,
                "action": {
                    "type": step.action.action_type,
                    "target": step.action.target,
                    "details": step.action.details,
                },
                "confidence": max(0.0, min(1.0, round(step.confidence, 3))),
            }
            for step in steps
        ]

        return {
            "video": str(video_path),
            "llm": llm_name,
            "video_type": video_type,
            "app_name": app_name,
            "utg_number": utg_number,
            "generated_at": generated_at_iso,
            "replay_trace": replay_trace,
        }
