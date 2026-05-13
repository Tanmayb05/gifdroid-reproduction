#!/usr/bin/env python3
"""
Replay script — barilyuk.batterytemperature / None
Generated: 2026-05-06T05:15:41.555547+00:00
Video: None
Task summary: --- app: Battery Temperature goal: The user wanted to test the temperature logging feature by starting and then stopping it. outcome: success - The user successfully started and stopped the...

Usage:
    python replay.py [--serial SERIAL] [--delay SECONDS] [--skip-install]
"""
import argparse
import subprocess
import sys
import time

import uiautomator2 as u2

APK_PATH = 'apps/batterytemperaturedisplay/apk/batterytemperaturedisplay.apk'
PACKAGE  = 'barilyuk.batterytemperature'
ACTIVITY = 'barilyuk.batterytemperature.MainActivity'

ACTIONS = [
    {'step': 1, 'type': 'tap', 'resource_id': 'com.android.permissioncontroller:id/permission_allow_button', 'coordinates': [540, 1039], 'text': 'Allow', 'direction': None, 'target_description': "the 'Allow' button in the notification permission dialog"},  # The task is to test the temperature logging feature, which the summary indicates creates a...
    {'step': 2, 'type': 'tap', 'resource_id': 'barilyuk.batterytemperature:id/startStopLoggingButton', 'coordinates': [821, 919], 'text': None, 'direction': None, 'target_description': 'START LOGGING button'},  # The first step of the task is to start the temperature logging. The 'START LOGGING' button is...
    {'step': 3, 'type': 'tap', 'resource_id': 'barilyuk.batterytemperature:id/startStopLoggingButton', 'coordinates': [821, 919], 'text': 'START LOGGING', 'direction': None, 'target_description': "the 'START LOGGING' button"},  # The task is to start and then stop temperature logging. The previous step was to tap 'START...
    {'step': 4, 'type': 'type_text', 'resource_id': 'barilyuk.batterytemperature:id/durationEditText', 'coordinates': [238, 919], 'text': '1', 'direction': None, 'target_description': "The duration input field with the value '1' and an error icon."},  # The application is showing an error 'Please enter duration' and an exclamation mark next to the...
    {'step': 5, 'type': 'tap', 'resource_id': 'barilyuk.batterytemperature:id/startStopLoggingButton', 'coordinates': [821, 919], 'text': 'START LOGGING', 'direction': None, 'target_description': "The 'START LOGGING' button to begin recording the battery temperature."},  # The user wants to test the logging feature. The first step is to start the logging process by...
    {'step': 6, 'type': 'tap', 'resource_id': 'barilyuk.batterytemperature:id/startStopLoggingButton', 'coordinates': [812, 919], 'text': None, 'direction': None, 'target_description': "the 'STOP LOGGING' button"},  # The user has started the logging process, as indicated by the button text 'STOP LOGGING'....
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
