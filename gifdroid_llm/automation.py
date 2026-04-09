"""Automation loop orchestration — video-free (blind) mode for Milestone 3."""
from __future__ import annotations

import json
import logging
import time
from pathlib import Path
from typing import Any

from gifdroid_llm.device import DeviceController
from gifdroid_llm.session import AutomationSession, ConversationTurn

import numpy as np


def _screenshot_to_array(img: Any) -> np.ndarray:
    return np.array(img)


def run_blind_loop(
    task_description: str,
    provider: Any,
    device: DeviceController,
    max_steps: int,
    output_dir: Path | None = None,
    history_window: int = 3,
    step_delay: float = 1.5,
    logger: logging.Logger | None = None,
) -> dict:
    """Run the LLM-driven automation loop without video context.

    Loop: capture screenshot → ask LLM for next action → execute → repeat.

    Returns a session trace dict.
    """
    if logger is None:
        logger = logging.getLogger(__name__)

    if output_dir is not None:
        output_dir.mkdir(parents=True, exist_ok=True)

    session = AutomationSession(max_steps=max_steps, history_window=history_window)
    steps_log: list[dict] = []
    status = "max_steps_reached"

    for step_num in range(max_steps):
        logger.info("Automation step %d/%d", step_num + 1, max_steps)

        # Capture current state
        screenshot = device.capture_screenshot()
        xml = device.dump_accessibility_tree()
        activity = device.get_current_activity()

        # Save screenshot
        screenshot_path: str | None = None
        if output_dir is not None:
            screenshot_path = str(output_dir / f"step_{step_num + 1:03d}.png")
            screenshot.save(screenshot_path)

        # Ask LLM for next action
        history = session.get_history()
        decision = provider.decide_next_action(
            history=history,
            screenshot=screenshot,
            accessibility_tree=xml,
            task_description=task_description,
        )

        logger.info(
            "Step %d: continue=%s action_type=%s reasoning=%s",
            step_num + 1,
            decision.continue_automation,
            decision.action.type if decision.action else "none",
            decision.reasoning[:80] if decision.reasoning else "",
        )

        step_entry: dict = {
            "step": step_num + 1,
            "activity": activity,
            "screenshot": screenshot_path,
            "continue": decision.continue_automation,
            "reasoning": decision.reasoning,
            "confidence": decision.confidence,
        }

        if decision.action:
            step_entry["action"] = {
                "type": decision.action.type,
                "resource_id": decision.action.resource_id,
                "coordinates": decision.action.coordinates,
                "text": decision.action.text,
                "direction": decision.action.direction,
                "target_description": decision.action.target_description,
            }
        else:
            step_entry["action"] = {"type": "done"}

        steps_log.append(step_entry)

        # Record turn in session
        session.add_turn(ConversationTurn(
            step_index=step_num,
            screenshot=_screenshot_to_array(screenshot),
            action_taken=decision.action,
        ))

        if not decision.continue_automation or decision.action is None or decision.action.type == "done":
            status = "done"
            logger.info("Automation loop complete at step %d", step_num + 1)
            break

        # Execute the action
        device.execute_action(decision.action)
        time.sleep(step_delay)

    trace = {
        "task": task_description,
        "total_steps": len(steps_log),
        "status": status,
        "steps": steps_log,
    }

    if output_dir is not None:
        trace_path = output_dir / "session_trace.json"
        trace_path.write_text(json.dumps(trace, indent=2))
        logger.info("Session trace saved to %s", trace_path)

    return trace
