#!/usr/bin/env python3
"""
Replay script — de.markusfisch.android.binaryeye / None
Generated: 2026-05-07T03:47:02.058621+00:00
Video: None
Task summary: --- app: Barcode Scanner goal: To enable the setting that automatically returns to the scan screen after an action. outcome: success - The user successfully located and enabled the desired setting....

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
    {'step': 1, 'type': 'tap', 'resource_id': 'de.markusfisch.android.binaryeye:id/expert', 'coordinates': [540, 1237], 'text': None, 'direction': None, 'target_description': 'Advanced button'},  # The task is to change a setting in the app. The current screen is a first-time setup screen. To...
    {'step': 2, 'type': 'tap', 'resource_id': 'com.android.permissioncontroller:id/permission_allow_foreground_only_button', 'coordinates': None, 'text': 'While using the app', 'direction': None, 'target_description': "the 'While using the app' button"},  # The app requires camera permission to function as a barcode scanner. The task starts from the...
    {'step': 3, 'type': 'tap', 'resource_id': None, 'coordinates': [1028, 136], 'text': None, 'direction': None, 'target_description': 'three-dot menu icon'},  # The first step to reach the settings is to open the overflow menu. The three-dot menu icon,...
    {'step': 4, 'type': 'tap', 'resource_id': None, 'coordinates': [812, 766], 'text': None, 'direction': None, 'target_description': 'Settings'},  # The task is to enable a setting. The current screen shows an overflow menu. The next logical step...
    {'step': 5, 'type': 'scroll', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': 'up', 'target_description': 'the settings list'},  # The user needs to find the 'Content' section to enable the 'Go back after copying or sharing'...
    {'step': 6, 'type': 'scroll', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': 'up', 'target_description': 'the settings list'},  # The target setting, 'Go back after copying or sharing', is not visible on the current screen....
    {'step': 7, 'type': 'scroll', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': 'up', 'target_description': 'the settings list'},  # The target setting, 'Go back after copying or sharing', is not visible on the current screen....
    {'step': 8, 'type': 'scroll', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': 'up', 'target_description': 'the settings list'},  # The target setting, 'Go back after copying or sharing', is not yet visible on the screen. Based...
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
