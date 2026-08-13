#!/usr/bin/env python3
"""
Replay script — com.amaze.filemanager / None
Generated: 2026-08-07T18:02:14.437564+00:00
Video: None
Task summary: --- app: Amaze goal: The user was trying to create a new text file in a directory. outcome: success — the app created the requested file, and then unexpectedly allowed the creation of a second file...

Usage:
    python replay.py [--serial SERIAL] [--delay SECONDS] [--skip-install]
"""
import argparse
import subprocess
import sys
import time

import uiautomator2 as u2

APK_PATH = 'apps/amazefilemanager/apk/amazefilemanager.apk'
PACKAGE  = 'com.amaze.filemanager'
ACTIVITY = 'com.amaze.filemanager.activities.MainActivity'

ACTIONS = [
    {'step': 1, 'type': 'tap', 'resource_id': 'com.amaze.filemanager:id/fab_expand_menu_button', 'coordinates': [965, 2158], 'text': None, 'direction': None, 'target_description': '+ Floating Action Button'},  # The first step of the task is to open the 'New' menu by tapping the floating action button. The...
    {'step': 2, 'type': 'tap', 'resource_id': 'com.amaze.filemanager:id/menu_new_file', 'coordinates': [965, 1843], 'text': None, 'direction': None, 'target_description': "the 'File' menu option"},  # The user has opened the 'New' menu by tapping the floating action button. The next step to create...
    {'step': 3, 'type': 'type_text', 'resource_id': 'com.amaze.filemanager:id/singleedittext_input', 'coordinates': [540, 1114], 'text': 'demo.txt', 'direction': None, 'target_description': 'input field with current text .txt'},  # The current screen shows the 'New File' dialog. According to the task steps, the next action is...
    {'step': 4, 'type': 'tap', 'resource_id': 'com.amaze.filemanager:id/md_buttonDefaultPositive', 'coordinates': [875, 1392], 'text': 'CREATE', 'direction': None, 'target_description': 'CREATE button'},  # The user has entered the filename in the 'New File' dialog. According to the task steps, the next...
    {'step': 5, 'type': 'tap', 'resource_id': 'com.amaze.filemanager:id/fab_expand_menu_button', 'coordinates': [965, 2158], 'text': None, 'direction': None, 'target_description': 'the floating action button with a plus icon'},  # The first file has been created. The next step in the task is to create the second file with the...
    {'step': 6, 'type': 'tap', 'resource_id': 'com.amaze.filemanager:id/menu_new_file', 'coordinates': None, 'text': None, 'direction': None, 'target_description': "the 'File' menu option"},  # The automation has successfully created the first file and opened the 'New' menu again (Step 6)....
    {'step': 7, 'type': 'type_text', 'resource_id': 'com.amaze.filemanager:id/singleedittext_input', 'coordinates': None, 'text': 'demo.txt', 'direction': None, 'target_description': 'text input with current value .txt'},  # The current screen shows the 'New File' dialog. According to the task steps, the next action is...
    {'step': 8, 'type': 'tap', 'resource_id': 'com.amaze.filemanager:id/md_buttonDefaultPositive', 'coordinates': [875, 1392], 'text': 'CREATE', 'direction': None, 'target_description': 'CREATE button'},  # According to the provided step-by-step summary, after entering the filename (Step 4), the next...
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
    elif atype in ("long_tap", "long_press"):
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
