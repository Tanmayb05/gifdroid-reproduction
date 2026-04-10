#!/usr/bin/env python3
"""
Replay script — com.aaronjwood.portauthority / apps/portauthority/videos/handheld/hhv-001.mp4
Generated: 2026-04-10T06:01:48.250047+00:00
Video: apps/portauthority/videos/handheld/hhv-001.mp4
Task summary: The user opens the Port Authority app and initiates a network scan by tapping "DISCOVER HOSTS". After the scan completes and displays a list of devices on the local network, the user selects one of...

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
    {'step': 1, 'type': 'tap', 'resource_id': 'android:id/button1', 'coordinates': [844, 1162], 'text': 'OK', 'direction': None, 'target_description': 'the OK button to dismiss the permission explanation dialog'},  # The current screen shows a dialog explaining the need for location permission to access the SSID....
    {'step': 2, 'type': 'tap', 'resource_id': 'com.android.permissioncontroller:id/permission_allow_foreground_only_button', 'coordinates': None, 'text': 'While using the app', 'direction': None, 'target_description': "the 'While using the app' button"},  # The app requires location permission to discover hosts on the network. To proceed with the task,...
    {'step': 3, 'type': 'tap', 'resource_id': 'android:id/button1', 'coordinates': [844, 1187], 'text': 'OK', 'direction': None, 'target_description': 'the OK button to generate the port database'},  # The task is to discover hosts on the network. The current screen shows a dialog asking to...
    {'step': 4, 'type': 'tap', 'resource_id': 'android:id/button1', 'coordinates': [844, 1211], 'text': None, 'direction': None, 'target_description': 'the OK button'},  # The task is to discover hosts on the network. The current screen shows a dialog box asking to...
    {'step': 5, 'type': 'tap', 'resource_id': 'com.aaronjwood.portauthority:id/discoverHosts', 'coordinates': [540, 1783], 'text': None, 'direction': None, 'target_description': 'the DISCOVER HOSTS button'},  # The task is to discover hosts on the network. The 'DISCOVER HOSTS' button is the primary action...
    {'step': 7, 'type': 'tap', 'resource_id': None, 'coordinates': [540, 1412], 'text': None, 'direction': None, 'target_description': 'discovered host with IP 10.0.2.2'},  # The task requires selecting a discovered host from the list. The video summary mentions selecting...
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
