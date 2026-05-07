#!/usr/bin/env python3
"""
Replay script — com.studio4plus.homerplayer2 / None
Generated: 2026-05-07T04:57:36.967059+00:00
Video: None
Task summary: --- app: Audiobook Player goal: The user wanted to hide the settings button from the main player screen. outcome: success - The user successfully enabled the "Hide settings button" option, and the...

Usage:
    python replay.py [--serial SERIAL] [--delay SECONDS] [--skip-install]
"""
import argparse
import subprocess
import sys
import time

import uiautomator2 as u2

APK_PATH = 'apps/homeraudioplayer/apk/homeraudioplayer.apk'
PACKAGE  = 'com.studio4plus.homerplayer2'
ACTIVITY = 'com.studio4plus.homerplayer2.app.MainActivity'

ACTIONS = [
    {'step': 1, 'type': 'tap', 'resource_id': None, 'coordinates': [936, 1753], 'text': None, 'direction': None, 'target_description': 'Next button'},  # The user wants to hide the settings button, which is accessible from the main player screen. The...
    {'step': 2, 'type': 'tap', 'resource_id': None, 'coordinates': [540, 531], 'text': None, 'direction': None, 'target_description': 'Sample books card'},  # The user wants to hide the settings button, which is on the main player screen. The current...
    {'step': 3, 'type': 'tap', 'resource_id': None, 'coordinates': [936, 1753], 'text': None, 'direction': None, 'target_description': 'Next button'},  # The current screen is the initial setup screen for adding audiobooks. To proceed to the main...
    {'step': 4, 'type': 'tap', 'resource_id': None, 'coordinates': [932, 1753], 'text': None, 'direction': None, 'target_description': 'Done button'},  # The current screen is for "Speak book titles" settings. To find the "Lockdown settings" as...
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
