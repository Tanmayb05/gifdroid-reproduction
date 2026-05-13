#!/usr/bin/env python3
"""
Replay script — com.aaronjwood.portauthority / None
Generated: 2026-05-07T15:05:37.921549+00:00
Video: None
Task summary: --- app: Port Authority goal: To disable the feature that fetches the device's external IP address. outcome: success - The user successfully navigated to settings and disabled the option. --- ##...

Usage:
    python replay.py [--serial SERIAL] [--delay SECONDS] [--skip-install]
"""
import argparse
import subprocess
import sys
import time

import uiautomator2 as u2

APK_PATH = 'apps/portauthority/apk/portauthority.apk'
PACKAGE  = 'com.aaronjwood.portauthority'
ACTIVITY = 'com.aaronjwood.portauthority.activity.MainActivity'

ACTIONS = [
    {'step': 1, 'type': 'tap', 'resource_id': 'android:id/button1', 'coordinates': [844, 1162], 'text': None, 'direction': None, 'target_description': "the OK button in the 'Android 10+ SSID Access' dialog"},  # The current screen shows a dialog explaining a permission requirement. To proceed to the main...
    {'step': 2, 'type': 'tap', 'resource_id': 'com.android.permissioncontroller:id/permission_allow_foreground_only_button', 'coordinates': [133, 1126], 'text': 'While using the app', 'direction': None, 'target_description': "the 'While using the app' button"},  # The app is requesting location permission, which is a prerequisite for discovering network hosts,...
    {'step': 3, 'type': 'tap', 'resource_id': 'android:id/button1', 'coordinates': [844, 1187], 'text': None, 'direction': None, 'target_description': 'the OK button'},  # The task is to disable a setting related to fetching the external IP. Currently, a dialog about...
    {'step': 4, 'type': 'tap', 'resource_id': 'android:id/button2', 'coordinates': [659, 1211], 'text': 'CANCEL', 'direction': None, 'target_description': 'CANCEL button'},  # The current screen displays a modal dialog titled "Generate OUI Database" which is blocking the...
    {'step': 5, 'type': 'tap', 'resource_id': 'com.aaronjwood.portauthority:id/discoverHosts', 'coordinates': [540, 1783], 'text': None, 'direction': None, 'target_description': 'the DISCOVER HOSTS button'},  # The goal is to disable the external IP fetching feature. According to the provided video summary,...
    {'step': 7, 'type': 'tap', 'resource_id': None, 'coordinates': [540, 909], 'text': None, 'direction': None, 'target_description': 'host with IP fec0::2'},  # The user is on the main screen after a host scan. According to the video summary, the next step...
    {'step': 8, 'type': 'tap', 'resource_id': 'com.aaronjwood.portauthority:id/wakeOnLan', 'coordinates': None, 'text': 'WAKE UP', 'direction': None, 'target_description': 'the WAKE UP button'},  # The user is on the host details screen. According to the video summary, the next step (Step 4) is...
    {'step': 9, 'type': 'press_back', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': None, 'target_description': 'the back button'},  # The user has just attempted to wake the host, which corresponds to step 4 of the video summary....
    {'step': 10, 'type': 'tap', 'resource_id': 'com.aaronjwood.portauthority:id/leftDrawerIcon', 'coordinates': [89, 152], 'text': None, 'direction': None, 'target_description': 'the hamburger menu icon'},  # The user has returned to the main screen after inspecting a host. To proceed with the task of...
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
