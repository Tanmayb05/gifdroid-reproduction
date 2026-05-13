#!/usr/bin/env python3
"""
Replay script — com.codedead.deadhash / None
Generated: 2026-05-07T04:35:30.595169+00:00
Video: None
Task summary: --- app: DeadHash goal: To explore the app's features for calculating hashes from text and to configure the available hashing algorithms. outcome: success — The user successfully calculated a hash,...

Usage:
    python replay.py [--serial SERIAL] [--delay SECONDS] [--skip-install]
"""
import argparse
import subprocess
import sys
import time

import uiautomator2 as u2

APK_PATH = 'apps/deadhash/apk/deadhash.apk'
PACKAGE  = 'com.codedead.deadhash'
ACTIVITY = 'com.codedead.deadhash.gui.MainActivity'

ACTIONS = [
    {'step': 2, 'type': 'tap', 'resource_id': 'com.codedead.deadhash:id/ImgBtnFileData', 'coordinates': None, 'text': None, 'direction': None, 'target_description': 'the folder icon to select a file'},  # The task is to reproduce a sequence of actions from a video summary. The provided steps indicate...
    {'step': 3, 'type': 'tap', 'resource_id': 'com.android.permissioncontroller:id/permission_allow_button', 'coordinates': [540, 1039], 'text': 'Allow', 'direction': None, 'target_description': "the 'Allow' button to grant storage permissions"},  # The task requires exploring the file hashing feature, which necessitates storage access. The...
    {'step': 4, 'type': 'tap', 'resource_id': 'com.android.permissioncontroller:id/permission_allow_all_button', 'coordinates': [540, 1118], 'text': 'Allow all', 'direction': None, 'target_description': "the 'Allow all' button in the permission dialog"},  # The task requires navigating to the file hashing section and attempting to open a file. This...
    {'step': 5, 'type': 'tap', 'resource_id': 'android:id/button3', 'coordinates': [201, 1092], 'text': 'CANCEL', 'direction': None, 'target_description': "The 'CANCEL' button in the 'Review' dialog."},  # The 'Review' dialog is an interruption to the main task flow. To continue exploring the app's...
    {'step': 6, 'type': 'tap', 'resource_id': None, 'coordinates': [73, 136], 'text': None, 'direction': None, 'target_description': 'a hamburger menu icon'},  # The task goal is to explore both text and file hashing. The video summary indicates the user...
    {'step': 7, 'type': 'tap', 'resource_id': 'com.codedead.deadhash:id/nav_text', 'coordinates': None, 'text': None, 'direction': None, 'target_description': "The 'Text' option in the navigation menu"},  # The task is to explore text hashing features. The video summary shows the user starting with text...
    {'step': 8, 'type': 'type_text', 'resource_id': 'com.codedead.deadhash:id/EdtText_Content', 'coordinates': None, 'text': 'qwerty', 'direction': None, 'target_description': "the text input field with the hint 'Enter your text here'"},  # Based on the session summary, the first action after launching the app is to enter 'qwerty' into...
    {'step': 9, 'type': 'tap', 'resource_id': None, 'coordinates': [73, 136], 'text': None, 'direction': None, 'target_description': 'Hamburger menu icon'},  # The user has entered the text 'qwerty' to be hashed. According to the task summary, the next step...
    {'step': 10, 'type': 'tap', 'resource_id': None, 'coordinates': [367, 630], 'text': None, 'direction': None, 'target_description': 'File'},  # The user has entered text and opened the navigation menu. According to the video summary, the...
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
