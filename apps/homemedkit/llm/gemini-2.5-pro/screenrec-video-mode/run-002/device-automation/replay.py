#!/usr/bin/env python3
"""
Replay script — ru.application.homemedkit / None
Generated: 2026-05-07T04:44:51.034329+00:00
Video: None
Task summary: app: Medicine Tracker goal: To manually add a new medication to the application. outcome: success - The user successfully filled out the form and saved a new medication, landing on its details...

Usage:
    python replay.py [--serial SERIAL] [--delay SECONDS] [--skip-install]
"""
import argparse
import subprocess
import sys
import time

import uiautomator2 as u2

APK_PATH = 'apps/homemedkit/apk/homemedkit.apk'
PACKAGE  = 'ru.application.homemedkit'
ACTIVITY = 'ru.application.homemedkit.MainActivity'

ACTIONS = [
    {'step': 2, 'type': 'tap', 'resource_id': None, 'coordinates': [964, 1573], 'text': None, 'direction': None, 'target_description': "'+' floating action button"},  # The first step in the task is to initiate adding a new medicine by tapping the '+' button, which...
    {'step': 3, 'type': 'tap', 'resource_id': None, 'coordinates': [893, 1405], 'text': 'Add', 'direction': None, 'target_description': 'Add button with a pencil icon'},  # The goal is to manually add a medication. The previous step was to tap the floating action...
    {'step': 4, 'type': 'type_text', 'resource_id': None, 'coordinates': [724, 357], 'text': 'medA', 'direction': None, 'target_description': 'Product name text input'},  # The user is on the 'Add Medicine' screen. According to the task steps, the next action is to...
    {'step': 5, 'type': 'tap', 'resource_id': None, 'coordinates': [724, 525], 'text': None, 'direction': None, 'target_description': 'Group field'},  # The user has entered the product name. According to the task summary, the next step is to attempt...
    {'step': 6, 'type': 'tap', 'resource_id': None, 'coordinates': [821, 1150], 'text': 'Save', 'direction': None, 'target_description': "the Save button in the 'Medication groups' dialog"},  # The user is presented with a dialog indicating no medication groups are available. According to...
    {'step': 7, 'type': 'tap', 'resource_id': None, 'coordinates': [724, 693], 'text': None, 'direction': None, 'target_description': 'Exp. date field'},  # Based on the video summary, after entering the product name and attempting to select a group, the...
    {'step': 8, 'type': 'tap', 'resource_id': None, 'coordinates': [842, 1466], 'text': 'Save', 'direction': None, 'target_description': 'the Save button'},  # The user has selected the month 'MAY' for the year 2026. To confirm this selection and proceed,...
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
