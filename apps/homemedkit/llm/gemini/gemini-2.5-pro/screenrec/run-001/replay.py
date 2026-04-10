#!/usr/bin/env python3
"""
Replay script — ru.application.homemedkit / apps/homemedkit/videos/screenrec/srv-001.mp4
Generated: 2026-04-10T05:21:48.259816+00:00
Video: apps/homemedkit/videos/screenrec/srv-001.mp4
Task summary: The user opens the Medkit app and adds a new medication entry manually. They tap the plus button, select "Add," and fill in details such as the product name, expiration date, and package opened...

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
    {'step': 1, 'type': 'tap', 'resource_id': None, 'coordinates': [964, 1573], 'text': None, 'direction': None, 'target_description': 'the plus button'},  # The user wants to add a new medication. The video summary indicates the first step is to tap the...
    {'step': 2, 'type': 'tap', 'resource_id': None, 'coordinates': [893, 1405], 'text': None, 'direction': None, 'target_description': "the 'Add' button"},  # The video summary indicates the user adds a new medication manually. After tapping the plus...
    {'step': 3, 'type': 'tap', 'resource_id': None, 'coordinates': [724, 357], 'text': None, 'direction': None, 'target_description': "the 'Product name' text input field"},  # The task is to add a new medication, which involves filling out the form. The next step is to...
    {'step': 4, 'type': 'type_text', 'resource_id': None, 'coordinates': [724, 357], 'text': 'Test Med', 'direction': None, 'target_description': 'the Product name text input field'},  # The user has tapped on the 'Product name' field, and the cursor is now active there. The next...
    {'step': 5, 'type': 'tap', 'resource_id': None, 'coordinates': [724, 693], 'text': None, 'direction': None, 'target_description': 'the expiration date field'},  # The user has entered the product name. According to the video summary, the next step is to enter...
    {'step': 6, 'type': 'tap', 'resource_id': None, 'coordinates': [842, 1466], 'text': None, 'direction': None, 'target_description': 'the Save button'},  # The user has selected the expiration date (April 2026) for the new medication. The next step is...
    {'step': 7, 'type': 'tap', 'resource_id': None, 'coordinates': [724, 861], 'text': None, 'direction': None, 'target_description': "the 'Package opened' date field"},  # The user has filled in the product name and expiration date. According to the video summary, the...
    {'step': 8, 'type': 'tap', 'resource_id': None, 'coordinates': [891, 1659], 'text': 'Save', 'direction': None, 'target_description': 'Save button'},  # The user has selected the expiration date (April 10, 2026). The next step is to confirm this...
    {'step': 9, 'type': 'tap', 'resource_id': None, 'coordinates': [920, 1805], 'text': None, 'direction': None, 'target_description': 'the Save button'},  # The user has selected a date (April 10, 2026) in the date picker. The next logical step is to...
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
