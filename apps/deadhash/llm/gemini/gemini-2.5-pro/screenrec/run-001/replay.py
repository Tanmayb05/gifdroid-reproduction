#!/usr/bin/env python3
"""
Replay script — com.codedead.deadhash / apps/DeadHash/videos/srv-001.mp4
Generated: 2026-05-01T15:58:52.652879+00:00
Video: apps/DeadHash/videos/srv-001.mp4
Task summary: The user calculates various hashes for the text "qwerty" in the DeadHash app. They then navigate to the file hashing section and open the file picker before returning. Finally, the user enters the...

Usage:
    python replay.py [--serial SERIAL] [--delay SECONDS] [--skip-install]
"""
import argparse
import subprocess
import sys
import time

import uiautomator2 as u2

APK_PATH = 'apps/DeadHash/apk/DeadHash.apk'
PACKAGE  = 'com.codedead.deadhash'
ACTIVITY = 'com.codedead.deadhash.gui.MainActivity'

ACTIONS = [
    {'step': 1, 'type': 'tap', 'resource_id': None, 'coordinates': [73, 136], 'text': None, 'direction': None, 'target_description': 'the hamburger menu icon in the top left corner'},  # The video summary indicates the first part of the task is to calculate hashes for text. The...
    {'step': 2, 'type': 'tap', 'resource_id': 'com.codedead.deadhash:id/nav_text', 'coordinates': [367, 756], 'text': None, 'direction': None, 'target_description': "the 'Text' option in the navigation drawer"},  # The task is to calculate hashes for the text 'qwerty'. The current screen is for file hashing....
    {'step': 3, 'type': 'type_text', 'resource_id': 'com.codedead.deadhash:id/EdtText_Content', 'coordinates': None, 'text': 'qwerty', 'direction': None, 'target_description': "the text input field with current text 'Enter your text here'"},  # The task is to calculate the hash for the text 'qwerty'. The next step is to type 'qwerty' into...
    {'step': 4, 'type': 'tap', 'resource_id': 'android:id/button3', 'coordinates': None, 'text': None, 'direction': None, 'target_description': 'the CANCEL button'},  # A review dialog has appeared, interrupting the task. To continue with the task of calculating the...
    {'step': 5, 'type': 'type_text', 'resource_id': 'com.codedead.deadhash:id/EdtText_Content', 'coordinates': None, 'text': 'qwerty', 'direction': None, 'target_description': "the text input field with current text 'Enter your text here'"},  # The first step of the task is to calculate hashes for the text "qwerty". To do this, I must first...
    {'step': 6, 'type': 'type_text', 'resource_id': 'com.codedead.deadhash:id/EdtText_Content', 'coordinates': None, 'text': 'qwerty', 'direction': None, 'target_description': "the text input field with placeholder 'Enter your text here'"},  # The first step of the task is to calculate a hash for the text 'qwerty'. The input field is...
    {'step': 7, 'type': 'type_text', 'resource_id': 'com.codedead.deadhash:id/EdtText_Content', 'coordinates': None, 'text': 'qwerty', 'direction': None, 'target_description': "the text input field with placeholder 'Enter your text here'"},  # The first step of the task is to calculate the hash for the text 'qwerty'. The input field...
    {'step': 8, 'type': 'tap', 'resource_id': 'com.codedead.deadhash:id/ButtonGenerateText', 'coordinates': None, 'text': None, 'direction': None, 'target_description': 'the CALCULATE button'},  # The video summary states that the user calculates hashes for the text 'qwerty'. After typing the...
    {'step': 9, 'type': 'type_text', 'resource_id': 'com.codedead.deadhash:id/EdtText_Content', 'coordinates': None, 'text': 'qwerty', 'direction': None, 'target_description': "the text input field with placeholder 'Enter your text here'"},  # The previous attempt to calculate the hash failed with the message 'Please enter some text...
    {'step': 10, 'type': 'type_text', 'resource_id': 'com.codedead.deadhash:id/EdtText_Content', 'coordinates': None, 'text': 'qwerty', 'direction': None, 'target_description': "the text input field with placeholder 'Enter your text here'"},  # The first step of the task is to calculate hashes for the text 'qwerty'. To do this, I need to...
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
