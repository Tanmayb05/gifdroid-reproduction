#!/usr/bin/env python3
"""
Replay script — io.gitlab.derjosef.jigsaw / apps/jigsaw/videos/screenrec/srv-001.mp4
Generated: 2026-04-10T05:13:32.720125+00:00
Video: apps/jigsaw/videos/screenrec/srv-001.mp4
Task summary: The user opens the Jigsaw puzzle app from their home screen. On the main menu, they tap the "Generate Puzzle" button to begin a new game. The user then solves the resulting four-piece puzzle by...

Usage:
    python replay.py [--serial SERIAL] [--delay SECONDS] [--skip-install]
"""
import argparse
import subprocess
import sys
import time

import uiautomator2 as u2

APK_PATH = 'apps/jigsaw/apk/jigsaw.apk'
PACKAGE  = 'io.gitlab.derjosef.jigsaw'
ACTIVITY = 'com.godot.game.GodotApp'

ACTIONS = [
    {'step': 1, 'type': 'tap', 'resource_id': None, 'coordinates': [540, 1558], 'text': None, 'direction': None, 'target_description': "the 'Generate Puzzle' button"},  # The video summary indicates that the next step is to start a new game by tapping the 'Generate...
    {'step': 2, 'type': 'tap', 'resource_id': None, 'coordinates': None, 'text': 'Generate Puzzle', 'direction': None, 'target_description': "the 'Generate Puzzle' button"},  # The user is on the puzzle configuration screen. The video summary states that the user generates...
    {'step': 3, 'type': 'tap', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': None, 'target_description': 'the Generate Puzzle button'},  # The video summary states that the user taps the 'Generate Puzzle' button to start a new game....
    {'step': 4, 'type': 'tap', 'resource_id': None, 'coordinates': None, 'text': 'Generate Puzzle', 'direction': None, 'target_description': "the 'Generate Puzzle' button"},  # The user is on the puzzle generation screen. According to the video summary, the user generates a...
    {'step': 5, 'type': 'tap', 'resource_id': None, 'coordinates': None, 'text': 'Generate Puzzle', 'direction': None, 'target_description': "the 'Generate Puzzle' button"},  # The video summary states that the user taps the 'Generate Puzzle' button to start a new game....
    {'step': 6, 'type': 'tap', 'resource_id': None, 'coordinates': None, 'text': 'Generate Puzzle', 'direction': None, 'target_description': "the 'Generate Puzzle' button"},  # The task is to generate a new puzzle. The current screen is the puzzle generation menu, and the...
    {'step': 7, 'type': 'tap', 'resource_id': None, 'coordinates': None, 'text': 'Generate Puzzle', 'direction': None, 'target_description': "the 'Generate Puzzle' button"},  # The video summary explicitly states that the user taps the 'Generate Puzzle' button to begin a...
    {'step': 8, 'type': 'tap', 'resource_id': None, 'coordinates': None, 'text': 'Generate Puzzle', 'direction': None, 'target_description': "the 'Generate Puzzle' button"},  # The task is to generate a new puzzle. The current screen is the puzzle generation menu, and the...
    {'step': 9, 'type': 'tap', 'resource_id': None, 'coordinates': [540, 1295], 'text': None, 'direction': None, 'target_description': "the 'Generate Puzzle' button"},  # The video summary states that the user taps the 'Generate Puzzle' button to start a new game. The...
    {'step': 10, 'type': 'tap', 'resource_id': None, 'coordinates': [540, 1100], 'text': None, 'direction': None, 'target_description': 'the bottom half of the empty puzzle frame'},  # The previous action was a tap near the two connected puzzle pieces at the bottom of the screen,...
    {'step': 11, 'type': 'tap', 'resource_id': None, 'coordinates': [338, 414], 'text': None, 'direction': None, 'target_description': 'the top-left puzzle piece'},  # The puzzle is partially solved with two pieces in place at the bottom. The next step is to place...
    {'step': 12, 'type': 'tap', 'resource_id': None, 'coordinates': [435, 985], 'text': None, 'direction': None, 'target_description': 'the top-left quadrant of the empty puzzle frame'},  # The previous step (11) was to tap the top-left puzzle piece, which selects it. The next logical...
    {'step': 13, 'type': 'tap', 'resource_id': None, 'coordinates': [753, 353], 'text': None, 'direction': None, 'target_description': 'the top-right puzzle piece'},  # The user has placed three of the four puzzle pieces. The next step is to select the final piece,...
    {'step': 14, 'type': 'tap', 'resource_id': None, 'coordinates': [441, 762], 'text': None, 'direction': None, 'target_description': 'the empty top-left slot in the puzzle frame'},  # The puzzle is almost complete, with three of the four pieces already placed in the central frame....
    {'step': 15, 'type': 'tap', 'resource_id': None, 'coordinates': [350, 350], 'text': None, 'direction': None, 'target_description': 'the top-left puzzle piece'},  # The puzzle is almost complete with only one piece remaining outside the frame. The next logical...
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
            mapping = {
                "up":    (x, y, x, y - dist),
                "down":  (x, y, x, y + dist),
                "left":  (x, y, x - dist, y),
                "right": (x, y, x + dist, y),
            }
            fx, fy, tx, ty = mapping.get(direction, (x, y, x, y - dist))
            d.swipe(fx, fy, tx, ty)
        else:
            d.swipe(540, 960, 540, 560)
    elif atype == "press_back":
        d.press("back")
    elif atype == "press_home":
        d.press("home")
    else:
        print(f"  [SKIP] Unknown action type: {atype}", file=sys.stderr)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Replay recorded automation actions on a device"
    )
    parser.add_argument("--serial", default=None, help="ADB device serial")
    parser.add_argument("--delay", type=float, default=1.5, help="Seconds between actions")
    parser.add_argument("--skip-install", action="store_true", help="Skip APK install + launch step")
    args = parser.parse_args()

    if not args.skip_install:
        subprocess.run(
            ["adb", "install", "-r", APK_PATH],
            check=True, capture_output=True
        )
        subprocess.run(
            ["adb", "shell", "am", "start", "-n", f"{PACKAGE}/{ACTIVITY}"],
            check=True, capture_output=True
        )
        time.sleep(2)

    d = u2.connect()
    print(f"Connected to device: {d.info.get('productName', 'unknown')}")
    print(f"Running {len(ACTIONS)} action(s)...")

    for action in ACTIONS:
        step = action["step"]
        desc = action.get("target_description") or action.get("type", "?")
        print(f"  Step {step}: {action['type']} → {desc}")
        try:
            _execute(d, action)
        except Exception as exc:
            print(f"  [ERROR] Step {step} failed: {exc}", file=sys.stderr)
            return 1
        time.sleep(args.delay)

    print("Replay complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
