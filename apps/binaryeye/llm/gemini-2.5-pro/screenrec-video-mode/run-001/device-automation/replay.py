#!/usr/bin/env python3
"""
Replay script — de.markusfisch.android.binaryeye / None
Generated: 2026-05-07T03:01:02.322634+00:00
Video: None
Task summary: --- app: Barcode Scanner goal: To enable the setting that automatically returns to the scan screen after copying or sharing a scanned code. outcome: success - The user successfully located and...

Usage:
    python replay.py [--serial SERIAL] [--delay SECONDS] [--skip-install]
"""
import argparse
import subprocess
import sys
import time

import uiautomator2 as u2

APK_PATH = 'apps/binaryeye/apk/binaryeye.apk'
PACKAGE  = 'de.markusfisch.android.binaryeye'
ACTIVITY = 'de.markusfisch.android.binaryeye.activity.SplashActivity'

ACTIONS = [
    {'step': 1, 'type': 'tap', 'resource_id': 'de.markusfisch.android.binaryeye:id/expert', 'coordinates': [540, 1237], 'text': None, 'direction': None, 'target_description': "The 'Advanced' button with text 'I would like to check the read content and open it manually.'"},  # The task is to change a specific setting in the app. The current screen is a first-time setup....
    {'step': 2, 'type': 'tap', 'resource_id': 'com.android.permissioncontroller:id/permission_allow_foreground_only_button', 'coordinates': [540, 961], 'text': 'While using the app', 'direction': None, 'target_description': "the 'While using the app' button"},  # The app requires camera permission to function. To proceed to the main scanning screen and begin...
    {'step': 3, 'type': 'tap', 'resource_id': None, 'coordinates': [1027, 136], 'text': None, 'direction': None, 'target_description': 'the overflow menu icon (three dots)'},  # The first step in the task is to open the overflow menu to access the settings. The overflow menu...
    {'step': 4, 'type': 'tap', 'resource_id': None, 'coordinates': [812, 766], 'text': None, 'direction': None, 'target_description': "the 'Settings' option in the overflow menu"},  # The goal is to change a setting. The current screen shows an overflow menu with a 'Settings'...
    {'step': 5, 'type': 'scroll', 'resource_id': None, 'coordinates': [540, 1300], 'text': None, 'direction': 'up', 'target_description': 'the settings list'},  # The target setting, 'Go back after copying or sharing', is not visible on the current screen....
    {'step': 6, 'type': 'scroll', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': 'up', 'target_description': 'the settings list'},  # The current screen shows the 'Scan' section of the settings. According to the task description, I...
    {'step': 7, 'type': 'scroll', 'resource_id': None, 'coordinates': [540, 1300], 'text': None, 'direction': 'up', 'target_description': 'the settings list'},  # The target setting, "Go back after copying or sharing", is not visible on the current screen....
    {'step': 8, 'type': 'scroll', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': 'up', 'target_description': 'settings list'},  # The target setting 'Go back after copying or sharing' is not visible on the current screen. Based...
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
