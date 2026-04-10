"""Automation loop orchestration — blind mode (Milestone 3) and video-guided mode (Milestone 4)."""
from __future__ import annotations

import json
import logging
import time
from pathlib import Path
from typing import Any, List, Optional

from gifdroid_llm.device import DeviceController
from gifdroid_llm.session import AutomationSession, ConversationTurn

import numpy as np


def _screenshot_to_array(img: Any) -> np.ndarray:
    return np.array(img)


def _action_key(step_entry: dict) -> tuple:
    """Return a hashable key representing the action taken in a step."""
    action = step_entry.get("action") or {}
    return (action.get("type"), action.get("direction"), action.get("resource_id"))


def run_blind_loop(
    task_description: str,
    provider: Any,
    device: DeviceController,
    max_steps: int,
    output_dir: Path | None = None,
    history_window: int = 3,
    step_delay: float = 1.5,
    stall_repeat_threshold: int = 4,
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

        # Stall detection: same action repeated stall_repeat_threshold times → stop
        if len(steps_log) >= stall_repeat_threshold:
            recent_keys = [_action_key(s) for s in steps_log[-stall_repeat_threshold:]]
            if len(set(recent_keys)) == 1:
                status = "stalled"
                logger.info(
                    "Stall detected: action %s repeated %d times — stopping at step %d",
                    recent_keys[0], stall_repeat_threshold, step_num + 1,
                )
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


def run_automation(
    video_path: Path,
    task_description: str,
    provider: Any,
    device: DeviceController,
    max_steps: int,
    output_dir: Path | None = None,
    history_window: int = 3,
    step_delay: float = 1.5,
    stall_repeat_threshold: int = 4,
    logger: logging.Logger | None = None,
) -> dict:
    """Run the full video-guided automation loop (Milestone 4).

    Video summarization strategy (in priority order):

    1. **Direct-video path** — if the provider exposes
       ``summarize_video_task_from_video(video_path)``, the raw video is sent
       directly to the model (e.g. Gemini inline video).  This lets the model
       reason over motion and temporal flow rather than still frames.
    2. **Keyframe fallback** — if direct-video is unsupported or raises an
       exception, frames are extracted, keyframes are selected, and
       ``provider.summarize_video_task(keyframes)`` is called as before.

    After summarization, the feedback loop runs using the summary as initial
    context for each LLM call.

    Returns a session trace dict.
    """
    if logger is None:
        logger = logging.getLogger(__name__)

    if output_dir is not None:
        output_dir.mkdir(parents=True, exist_ok=True)

    # --- Step 1 & 2: Summarize the video task ---
    # Prefer direct-video summarization when the provider supports it; fall
    # back to the keyframe pipeline for providers that do not.
    video_summary: str | None = None

    if hasattr(provider, "summarize_video_task_from_video"):
        logger.info(
            "Provider supports direct-video summarization — attempting raw-video path | video=%s",
            video_path,
        )
        try:
            video_summary = provider.summarize_video_task_from_video(video_path)
            logger.info(
                "Direct-video summary obtained (skipping keyframe extraction) | summary=%s",
                video_summary[:200],
            )
            if output_dir is not None:
                (output_dir / "video_summary.txt").write_text(video_summary, encoding="utf-8")
                logger.info("Video summary saved to %s", output_dir / "video_summary.txt")
        except Exception as exc:  # noqa: BLE001
            logger.warning(
                "Direct-video summarization failed (%s) — falling back to keyframe pipeline",
                exc,
            )
            video_summary = None
    else:
        logger.info(
            "Provider does not support direct-video summarization — using keyframe pipeline"
        )

    if video_summary is None:
        # --- Keyframe fallback ---
        from gifdroid_llm.video import VideoFrameExtractor
        from gifdroid_llm.keyframes import KeyframeSelector
        from gifdroid_llm.config import FrameSamplingConfig, KeyframeSelectionConfig

        frame_cfg = FrameSamplingConfig(strategy="uniform", fps=1.5, max_frames=100)
        kf_cfg = KeyframeSelectionConfig(
            method="ssim",
            min_gap_seconds=0.0,
            stable_threshold=2,
            ssim_threshold=0.95,
        )

        logger.info("Extracting frames from video: %s", video_path)
        extractor = VideoFrameExtractor()
        frames, _ = extractor.extract(video_path, frame_cfg, logger=logger)

        selector = KeyframeSelector()
        keyframes = selector.select(frames, kf_cfg, logger=logger)
        logger.info("Keyframes selected: %d", len(keyframes))

        logger.info("Requesting video task summary from LLM via keyframe pipeline")
        video_summary = provider.summarize_video_task(keyframes)
        logger.info("Keyframe-based task summary: %s", video_summary[:200])
        if output_dir is not None:
            (output_dir / "video_summary.txt").write_text(video_summary, encoding="utf-8")
            logger.info("Video summary saved to %s", output_dir / "video_summary.txt")

    # --- Step 3: Run the feedback loop ---
    session = AutomationSession(max_steps=max_steps, history_window=history_window)
    steps_log: list[dict] = []
    status = "max_steps_reached"

    for step_num in range(max_steps):
        logger.info("Step %d/%d", step_num + 1, max_steps)

        screenshot = device.capture_screenshot()
        xml = device.dump_accessibility_tree()
        activity = device.get_current_activity()

        screenshot_path: str | None = None
        if output_dir is not None:
            step_dir = output_dir / "steps"
            step_dir.mkdir(parents=True, exist_ok=True)
            screenshot_path = str(step_dir / f"step_{step_num + 1:03d}.png")
            screenshot.save(screenshot_path)

        history = session.get_history()
        decision = provider.decide_next_action_with_video_context(
            history=history,
            screenshot=screenshot,
            accessibility_tree=xml,
            task_description=task_description,
            video_summary=video_summary,
        )

        logger.info(
            "Step %d: continue=%s action_type=%s",
            step_num + 1,
            decision.continue_automation,
            decision.action.type if decision.action else "none",
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

        session.add_turn(ConversationTurn(
            step_index=step_num,
            screenshot=_screenshot_to_array(screenshot),
            action_taken=decision.action,
        ))

        if not decision.continue_automation or decision.action is None or decision.action.type == "done":
            status = "done"
            logger.info("Automation loop complete at step %d", step_num + 1)
            break

        # Stall detection: same action repeated stall_repeat_threshold times → stop
        if len(steps_log) >= stall_repeat_threshold:
            recent_keys = [_action_key(s) for s in steps_log[-stall_repeat_threshold:]]
            if len(set(recent_keys)) == 1:
                status = "stalled"
                logger.info(
                    "Stall detected: action %s repeated %d times — stopping at step %d",
                    recent_keys[0], stall_repeat_threshold, step_num + 1,
                )
                break

        device.execute_action(decision.action)
        time.sleep(step_delay)

    trace = {
        "task": task_description,
        "video": str(video_path),
        "video_summary": video_summary,
        "keyframes_used": len(keyframes) if "keyframes" in dir() else 0,
        "total_steps": len(steps_log),
        "status": status,
        "steps": steps_log,
    }

    if output_dir is not None:
        trace_path = output_dir / "session_trace.json"
        trace_path.write_text(json.dumps(trace, indent=2))
        logger.info("Session trace saved to %s", trace_path)

        summary_path = output_dir / "video_summary.txt"
        if not summary_path.exists():
            summary_path.write_text(video_summary or "", encoding="utf-8")
            logger.info("Video summary saved to %s", summary_path)

    return trace
