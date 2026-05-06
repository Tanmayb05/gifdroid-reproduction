#!/usr/bin/env python3
"""
Replay script — com.derdilla.bloodPressureApp / apps/BloodPressureMonitor/videos/srv-001.mp4
Generated: 2026-05-01T15:53:33.740078+00:00
Video: apps/BloodPressureMonitor/videos/srv-001.mp4
Task summary: The user starts on a blood pressure tracking screen and taps the statistics icon. On the statistics page, they cycle through the value distribution graphs for systolic, diastolic, and pulse...

Usage:
    python replay.py [--serial SERIAL] [--delay SECONDS] [--skip-install]
"""
import argparse
import subprocess
import sys
import time

import uiautomator2 as u2

APK_PATH = 'apps/BloodPressureMonitor/apk/BloodPressureMonitor.apk'
PACKAGE  = 'com.derdilla.bloodPressureApp'
ACTIVITY = 'com.derdilla.blood_pressure_app.MainActivity'

ACTIONS = [
    {'step': 1, 'type': 'tap', 'resource_id': None, 'coordinates': [939, 1518], 'text': None, 'direction': None, 'target_description': 'the statistics icon'},  # The first step in the task is to tap the statistics icon. Based on the screenshot, the middle...
    {'step': 2, 'type': 'tap', 'resource_id': None, 'coordinates': [540, 869], 'text': None, 'direction': None, 'target_description': "the 'Diastolic' button"},  # The user is on the statistics page and has already viewed the systolic data. The next step in the...
    {'step': 3, 'type': 'tap', 'resource_id': None, 'coordinates': [872, 869], 'text': None, 'direction': None, 'target_description': 'Pulse button'},  # The video summary indicates the user cycles through the value distribution graphs. The previous...
    {'step': 4, 'type': 'scroll', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': 'down', 'target_description': 'the main content area'},  # The user has finished cycling through the 'Value distribution' tabs (Systolic, Diastolic, Pulse)....
    {'step': 5, 'type': 'scroll', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': 'down', 'target_description': "the page to view the 'Metrics by time of day' graph"},  # The task summary indicates the user scrolls down to view the 'Metrics by time of day' circular...
    {'step': 6, 'type': 'scroll', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': 'down', 'target_description': "the screen to view the 'Metrics by time of day' circular graph"},  # The video summary indicates that the user scrolls down to view a circular graph under 'Metrics by...
    {'step': 7, 'type': 'scroll', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': 'down', 'target_description': "the bottom of the screen to reveal the 'Metrics by time of day' graph"},  # The video summary indicates the user scrolls down to view a circular graph for 'Metrics by time...
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
