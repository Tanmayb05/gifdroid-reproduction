"""Write a self-contained replay.py script from a session trace.

Usage (internal):
    from gifdroid_llm.replay_writer import write_replay_script
    path = write_replay_script(output_dir, trace, apk_path, package, activity, device_serial)
"""
from __future__ import annotations

import json
import textwrap
from datetime import datetime, timezone
from pathlib import Path

# Action types that represent real device interactions (exclude done/wait/none)
_EXECUTABLE_TYPES = {"tap", "scroll", "type_text", "press_back", "press_home", "long_tap"}


def _filter_actionable(steps: list[dict]) -> list[dict]:
    """Return only steps that have a real executable action."""
    result = []
    for step in steps:
        action = step.get("action")
        if not action:
            continue
        if action.get("type") in _EXECUTABLE_TYPES:
            result.append(step)
    return result


def _render_action_dispatch(action: dict) -> str:
    """Render the Python code lines that execute one action."""
    atype = action.get("type")
    resource_id = action.get("resource_id")
    coords = action.get("coordinates")
    text = action.get("text")
    direction = action.get("direction")

    lines: list[str] = []

    if atype == "tap":
        if resource_id:
            lines.append(f'        d(resourceId={resource_id!r}).click()')
        elif coords:
            lines.append(f'        d.click({coords[0]}, {coords[1]})')
        else:
            lines.append('        pass  # no target info for tap')

    elif atype == "long_tap":
        if resource_id:
            lines.append(f'        d(resourceId={resource_id!r}).long_click()')
        elif coords:
            lines.append(f'        d.long_click({coords[0]}, {coords[1]})')
        else:
            lines.append('        pass  # no target info for long_tap')

    elif atype == "type_text":
        if text is not None:
            if resource_id:
                lines.append(f'        d(resourceId={resource_id!r}).set_text({text!r})')
            elif coords:
                lines.append(f'        d.click({coords[0]}, {coords[1]})')
                lines.append(f'        d.send_keys({text!r})')
            else:
                lines.append(f'        d.send_keys({text!r})')

    elif atype == "scroll":
        direction_str = (direction or "down").lower()
        if resource_id:
            lines.append(f'        d(resourceId={resource_id!r}).scroll("{direction_str}")')
        elif coords:
            # uiautomator2 swipe: map direction to delta
            x, y = coords[0], coords[1]
            dist = 400
            mapping = {
                "up": (x, y, x, y - dist),
                "down": (x, y, x, y + dist),
                "left": (x, y, x - dist, y),
                "right": (x, y, x + dist, y),
            }
            fx, fy, tx, ty = mapping.get(direction_str, (x, y, x, y - dist))
            lines.append(f'        d.swipe({fx}, {fy}, {tx}, {ty})')
        else:
            lines.append(f'        d.swipe(540, 960, 540, 560)')  # default down

    elif atype == "press_back":
        lines.append('        d.press("back")')

    elif atype == "press_home":
        lines.append('        d.press("home")')

    return "\n".join(lines) if lines else "        pass"


def write_replay_script(
    output_dir: Path,
    trace: dict,
    apk_path: Path,
    package: str,
    activity: str | None,
    device_serial: str | None = None,
) -> Path:
    """Render a self-contained replay.py into output_dir. Returns the path."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    actionable = _filter_actionable(trace.get("steps", []))
    video = trace.get("video", "")
    summary_raw = trace.get("video_summary", "")
    summary = textwrap.shorten(summary_raw, width=200, placeholder="...")
    timestamp = datetime.now(timezone.utc).isoformat()

    # Build the ACTIONS list as a Python literal
    actions_lines: list[str] = []
    for step in actionable:
        action = step["action"]
        entry = {
            "step": step["step"],
            "type": action.get("type"),
            "resource_id": action.get("resource_id"),
            "coordinates": action.get("coordinates"),
            "text": action.get("text"),
            "direction": action.get("direction"),
            "target_description": action.get("target_description", ""),
        }
        # Inline comment with step reasoning (truncated)
        reasoning = step.get("reasoning", "")
        comment = textwrap.shorten(reasoning, width=100, placeholder="...") if reasoning else ""
        actions_lines.append(f"    {entry!r},  # {comment}")

    actions_block = "\n".join(actions_lines) if actions_lines else "    # (no actionable steps)"

    # Build per-action dispatch inside the loop
    dispatch_cases: list[str] = []
    # We generate a unified dispatch at runtime — simpler to embed inline executor
    # The script will use a helper function that dispatches based on action["type"]

    connect_expr = f'u2.connect({device_serial!r})' if device_serial else 'u2.connect()'
    apk_str = str(apk_path)

    if activity:
        launch_lines = [
            'subprocess.run(',
            '    ["adb", "install", "-r", APK_PATH],',
            '    check=True, capture_output=True',
            ')',
            'subprocess.run(',
            '    ["adb", "shell", "am", "start", "-n", f"{PACKAGE}/{ACTIVITY}"],',
            '    check=True, capture_output=True',
            ')',
        ]
        activity_line = f'ACTIVITY = {activity!r}'
    else:
        launch_lines = [
            'subprocess.run(',
            '    ["adb", "install", "-r", APK_PATH],',
            '    check=True, capture_output=True',
            ')',
            'subprocess.run(',
            '    ["adb", "shell", "monkey", "-p", PACKAGE, "-c",',
            '     "android.intent.category.LAUNCHER", "1"],',
            '    check=True, capture_output=True',
            ')',
        ]
        activity_line = 'ACTIVITY = None'

    # Indent 8 spaces (inside `if not args.skip_install:` which is 4, then body 4 more)
    launch_indented = "\n".join("        " + line for line in launch_lines)

    script = f'''\
#!/usr/bin/env python3
"""
Replay script — {package} / {video}
Generated: {timestamp}
Video: {video}
Task summary: {summary}

Usage:
    python replay.py [--serial SERIAL] [--delay SECONDS] [--skip-install]
"""
import argparse
import subprocess
import sys
import time

import uiautomator2 as u2

APK_PATH = {apk_str!r}
PACKAGE  = {package!r}
{activity_line}

ACTIONS = [
{actions_block}
]


def _execute(d: u2.Device, action: dict) -> None:
    atype = action["type"]
    resource_id = action.get("resource_id")
    coords = action.get("coordinates")
    text = action.get("text")
    direction = (action.get("direction") or "down").lower()

    if atype == "tap":
        if resource_id:
            d(resourceId=resource_id).click()
        elif coords:
            d.click(coords[0], coords[1])
    elif atype == "long_tap":
        if resource_id:
            d(resourceId=resource_id).long_click()
        elif coords:
            d.long_click(coords[0], coords[1])
    elif atype == "type_text":
        if text is not None:
            if resource_id:
                d(resourceId=resource_id).set_text(text)
            elif coords:
                d.click(coords[0], coords[1])
                d.send_keys(text)
            else:
                d.send_keys(text)
    elif atype == "scroll":
        dist = 400
        if resource_id:
            d(resourceId=resource_id).scroll(direction)
        elif coords:
            x, y = coords[0], coords[1]
            mapping = {{
                "up":    (x, y, x, y - dist),
                "down":  (x, y, x, y + dist),
                "left":  (x, y, x - dist, y),
                "right": (x, y, x + dist, y),
            }}
            fx, fy, tx, ty = mapping.get(direction, (x, y, x, y - dist))
            d.swipe(fx, fy, tx, ty)
        else:
            d.swipe(540, 960, 540, 560)
    elif atype == "press_back":
        d.press("back")
    elif atype == "press_home":
        d.press("home")
    else:
        print(f"  [SKIP] Unknown action type: {{atype}}", file=sys.stderr)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Replay recorded automation actions on a device"
    )
    parser.add_argument("--serial", default=None, help="ADB device serial")
    parser.add_argument("--delay", type=float, default=1.5, help="Seconds between actions")
    parser.add_argument("--skip-install", action="store_true", help="Skip APK install + launch step")
    args = parser.parse_args()

    if not args.skip_install:
{launch_indented}
        time.sleep(2)

    d = {connect_expr}
    print(f"Connected to device: {{d.info.get('productName', 'unknown')}}")
    print(f"Running {{len(ACTIONS)}} action(s)...")

    for action in ACTIONS:
        step = action["step"]
        desc = action.get("target_description") or action.get("type", "?")
        print(f"  Step {{step}}: {{action[\'type\']}} → {{desc}}")
        try:
            _execute(d, action)
        except Exception as exc:
            print(f"  [ERROR] Step {{step}} failed: {{exc}}", file=sys.stderr)
            return 1
        time.sleep(args.delay)

    print("Replay complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
'''

    replay_path = output_dir / "replay.py"
    replay_path.write_text(script, encoding="utf-8")
    return replay_path
