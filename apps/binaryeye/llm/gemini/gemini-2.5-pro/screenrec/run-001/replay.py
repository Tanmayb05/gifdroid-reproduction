#!/usr/bin/env python3
"""
Replay script — de.markusfisch.android.binaryeye / apps/BinaryEye/videos/srv-001.mp4
Generated: 2026-05-01T15:51:42.082451+00:00
Video: apps/BinaryEye/videos/srv-001.mp4
Task summary: The user is in a barcode scanning app and navigates to the settings menu. They scroll down through the various options and enable the "Go back after copying or sharing" feature. After enabling this...

Usage:
    python replay.py [--serial SERIAL] [--delay SECONDS] [--skip-install]
"""
import argparse
import subprocess
import sys
import time

import uiautomator2 as u2

APK_PATH = 'apps/BinaryEye/apk/BinaryEye.apk'
PACKAGE  = 'de.markusfisch.android.binaryeye'
ACTIVITY = 'de.markusfisch.android.binaryeye.activity.SplashActivity'

ACTIONS = [
    {'step': 1, 'type': 'tap', 'resource_id': 'de.markusfisch.android.binaryeye:id/simple', 'coordinates': None, 'text': None, 'direction': None, 'target_description': "the 'Simple' button with text 'I just want to read barcodes and have them opened immediately.'"},  # The current screen is a welcome screen requiring the user to choose a mode. To proceed to the...
    {'step': 2, 'type': 'tap', 'resource_id': 'com.android.permissioncontroller:id/permission_allow_foreground_only_button', 'coordinates': [540, 961], 'text': 'While using the app', 'direction': None, 'target_description': "the 'While using the app' button"},  # The app is requesting camera permission, which is necessary for its core function of scanning...
    {'step': 3, 'type': 'tap', 'resource_id': None, 'coordinates': [1027, 136], 'text': None, 'direction': None, 'target_description': 'the three-dot menu icon'},  # The task is to navigate to the settings menu. The standard way to access settings in an Android...
    {'step': 4, 'type': 'tap', 'resource_id': None, 'coordinates': [812, 766], 'text': None, 'direction': None, 'target_description': "the 'Settings' option in the menu"},  # The user wants to navigate to the settings menu to change a setting. The 'Settings' option is...
    {'step': 5, 'type': 'scroll', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': 'down', 'target_description': 'the settings screen'},  # The target setting 'Go back after copying or sharing' is not visible on the current screen. I...
    {'step': 6, 'type': 'scroll', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': 'down', 'target_description': 'the settings screen'},  # The target setting 'Go back after copying or sharing' is not visible on the current screen. I...
    {'step': 7, 'type': 'scroll', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': 'down', 'target_description': 'the settings list'},  # The target setting 'Go back after copying or sharing' is not yet visible on the screen. I need to...
    {'step': 8, 'type': 'scroll', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': 'down', 'target_description': 'the settings screen'},  # The target setting 'Go back after copying or sharing' is not visible on the current screen. I...
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
