#!/usr/bin/env python3
"""
Replay script — ru.application.homemedkit / apps/homemedkit/videos/handheld/hhv-001.mp4
Generated: 2026-04-10T05:27:21.374726+00:00
Video: apps/homemedkit/videos/handheld/hhv-001.mp4
Task summary: The user opens the "Home Medkit" app and proceeds to add a new medication manually. They tap the add button and fill out the form with details like the product name, expiration date, display name,...

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
    {'step': 1, 'type': 'tap', 'resource_id': None, 'coordinates': [964, 1573], 'text': None, 'direction': None, 'target_description': 'the plus button to add a new medication'},  # The task is to add a new medication. The first step is to tap the add button, which is the...
    {'step': 2, 'type': 'tap', 'resource_id': None, 'coordinates': [893, 1405], 'text': None, 'direction': None, 'target_description': "the 'Add' button"},  # The user wants to manually add a new medication. After tapping the floating action button, the...
    {'step': 3, 'type': 'type_text', 'resource_id': None, 'coordinates': [724, 357], 'text': 'Aspirin', 'direction': None, 'target_description': 'Product name text input field'},  # The user is on the 'add new medicine' screen. Based on the video summary, the next step is to...
    {'step': 4, 'type': 'tap', 'resource_id': None, 'coordinates': [724, 693], 'text': None, 'direction': None, 'target_description': 'the expiration date text input field'},  # The user has entered the product name. According to the video, the next step is to enter the...
    {'step': 5, 'type': 'tap', 'resource_id': None, 'coordinates': [842, 1466], 'text': None, 'direction': None, 'target_description': 'Save button'},  # The user has selected the expiration month and year for the new medication. The next step is to...
    {'step': 6, 'type': 'type_text', 'resource_id': None, 'coordinates': [540, 1197], 'text': 'My Medicine', 'direction': None, 'target_description': "the 'Display name' text input field with current value 'Empty'"},  # The user is filling out the form to add a new medication. According to the video summary, after...
    {'step': 7, 'type': 'tap', 'resource_id': None, 'coordinates': [540, 1523], 'text': None, 'direction': None, 'target_description': "the 'Release form' input field with the text 'Empty'"},  # The user is in the process of filling out the new medication form. According to the video...
    {'step': 8, 'type': 'type_text', 'resource_id': None, 'coordinates': [540, 1523], 'text': 'Capsules', 'direction': None, 'target_description': "the 'Release form' text input with current value 'Empty'"},  # The user is filling out a form to add a new medication. The 'Release form' field is currently...
    {'step': 9, 'type': 'tap', 'resource_id': None, 'coordinates': [799, 1848], 'text': None, 'direction': None, 'target_description': "the 'Amount' dropdown field which currently shows 'Empty'"},  # The user is in the process of adding a new medication. They have filled out the 'Display name',...
    {'step': 10, 'type': 'tap', 'resource_id': None, 'coordinates': [540, 1131], 'text': None, 'direction': None, 'target_description': "the 'Display name' field with text 'Empty'"},  # The user is in the process of filling out the form. According to the video summary, the 'Display...
    {'step': 11, 'type': 'type_text', 'resource_id': None, 'coordinates': [540, 1131], 'text': 'Aspirin', 'direction': None, 'target_description': 'Display name text input with current value Empty'},  # The user has tapped on the 'Display name' field, which currently shows 'Empty'. The next logical...
    {'step': 12, 'type': 'type_text', 'resource_id': None, 'coordinates': [724, 291], 'text': 'Aspirin', 'direction': None, 'target_description': 'Product name text input'},  # The user is in the process of adding a new medication. The 'Product name' field is currently...
    {'step': 13, 'type': 'tap', 'resource_id': None, 'coordinates': [799, 1783], 'text': None, 'direction': None, 'target_description': 'the Amount dropdown menu'},  # The user is in the process of adding a new medication. They have filled out the display name,...
    {'step': 14, 'type': 'tap', 'resource_id': None, 'coordinates': [1007, 148], 'text': None, 'direction': None, 'target_description': 'the checkmark button to save the new medication'},  # The form for adding a new medication has been filled out. The next logical step is to save the...
    {'step': 15, 'type': 'type_text', 'resource_id': None, 'coordinates': [724, 317], 'text': 'Aspirin', 'direction': None, 'target_description': 'the Product name text input field'},  # The form cannot be saved because the 'Product name' field is empty, as indicated by the red...
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
