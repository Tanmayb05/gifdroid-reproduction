#!/usr/bin/env python3
"""
Replay script — com.derdilla.bloodPressureApp / None
Generated: 2026-05-08T14:33:51.909861+00:00
Video: None
Task summary: --- app: Blood Pressure Tracker goal: The user wants to add multiple blood pressure readings and view the resulting graph and statistics. outcome: success - The user successfully added two data...

Usage:
    python replay.py [--serial SERIAL] [--delay SECONDS] [--skip-install]
"""
import argparse
import subprocess
import sys
import time

import uiautomator2 as u2

APK_PATH = 'apps/bloodpressuremonitor/apk/bloodpressuremonitor.apk'
PACKAGE  = 'com.derdilla.bloodPressureApp'
ACTIVITY = 'com.derdilla.blood_pressure_app.MainActivity'

ACTIONS = [
    {'step': 1, 'type': 'tap', 'resource_id': None, 'coordinates': [939, 1716], 'text': None, 'direction': None, 'target_description': 'the plus icon to add a new record'},  # The first step of the task is to add a new blood pressure reading. The current screen is the main...
    {'step': 2, 'type': 'type_text', 'resource_id': None, 'coordinates': [187, 456], 'text': '118', 'direction': None, 'target_description': 'Systolic text input with a cursor'},  # Based on the task summary, the user's first action after navigating to the 'Add Record' screen is...
    {'step': 3, 'type': 'type_text', 'resource_id': None, 'coordinates': [540, 456], 'text': '76', 'direction': None, 'target_description': 'Diastolic input field'},  # Based on the video summary, after entering the systolic value, the user enters the diastolic...
    {'step': 4, 'type': 'type_text', 'resource_id': None, 'coordinates': [893, 456], 'text': '68', 'direction': None, 'target_description': 'Pulse field'},  # The user has entered the systolic and diastolic values. According to the task summary, the next...
    {'step': 5, 'type': 'type_text', 'resource_id': None, 'coordinates': [540, 646], 'text': 'qwert', 'direction': None, 'target_description': "the 'Note (optional)' text input field"},  # Based on the video summary, after entering the blood pressure and pulse values, the user adds a...
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
