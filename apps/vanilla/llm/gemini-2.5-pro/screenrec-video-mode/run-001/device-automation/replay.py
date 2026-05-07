#!/usr/bin/env python3
"""
Replay script — com.sosauce.cutecalc / None
Generated: 2026-05-07T15:21:43.936653+00:00
Video: None
Task summary: --- app: Calculator goal: The user wants to perform a multi-step arithmetic calculation (36 * 6 - 6). outcome: success - The calculator correctly computed the expression and displayed the final...

Usage:
    python replay.py [--serial SERIAL] [--delay SECONDS] [--skip-install]
"""
import argparse
import subprocess
import sys
import time

import uiautomator2 as u2

APK_PATH = 'apps/vanilla/apk/vanilla.apk'
PACKAGE  = 'com.sosauce.cutecalc'
ACTIVITY = 'com.sosauce.vanilla.MainActivity'

ACTIONS = [
    {'step': 1, 'type': 'tap', 'resource_id': None, 'coordinates': [671, 1211], 'text': None, 'direction': None, 'target_description': '3 button'},  # The first step of the task is to calculate '36 * 6 - 6'. To do this, I need to first input the...
    {'step': 2, 'type': 'tap', 'resource_id': None, 'coordinates': [671, 948], 'text': None, 'direction': None, 'target_description': '6 button'},  # The user wants to calculate `36 * 6 - 6`. The previous step was tapping the '3' button. The next...
    {'step': 3, 'type': 'tap', 'resource_id': None, 'coordinates': [934, 685], 'text': None, 'direction': None, 'target_description': 'x button'},  # The user has entered the number 36. The next step in the calculation '36 * 6 - 6' is to select...
    {'step': 4, 'type': 'tap', 'resource_id': None, 'coordinates': [671, 948], 'text': None, 'direction': None, 'target_description': '6 button'},  # The task is to calculate 36 * 6 - 6. The previous steps have entered '36' and the multiplication...
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
