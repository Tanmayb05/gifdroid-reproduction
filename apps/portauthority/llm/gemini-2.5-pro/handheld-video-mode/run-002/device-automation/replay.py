#!/usr/bin/env python3
"""
Replay script — com.aaronjwood.portauthority / None
Generated: 2026-05-08T16:43:07.739643+00:00
Video: None
Task summary: --- app: Port Authority goal: To scan the local network for hosts and explore the application's settings. outcome: success — The user successfully scanned the network and adjusted a setting. --- ##...

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
    {'step': 1, 'type': 'tap', 'resource_id': 'android:id/button1', 'coordinates': [844, 1162], 'text': 'OK', 'direction': None, 'target_description': 'OK button'},  # The screen displays an informational dialog explaining that the app requires location permissions...
    {'step': 2, 'type': 'tap', 'resource_id': 'com.android.permissioncontroller:id/permission_allow_foreground_only_button', 'coordinates': None, 'text': 'While using the app', 'direction': None, 'target_description': "the 'While using the app' button"},  # The application requires location permission to scan for network hosts, which is the primary goal...
    {'step': 3, 'type': 'tap', 'resource_id': 'android:id/button1', 'coordinates': [844, 1187], 'text': 'OK', 'direction': None, 'target_description': "The 'OK' button in the 'Generate Port Database' dialog."},  # The application is presenting a setup dialog to download a port database, which is necessary for...
    {'step': 4, 'type': 'tap', 'resource_id': 'android:id/button1', 'coordinates': [844, 1211], 'text': 'OK', 'direction': None, 'target_description': "OK button in the 'Generate OUI Database' dialog"},  # The application is prompting to download the OUI database, which is necessary to resolve MAC...
    {'step': 5, 'type': 'tap', 'resource_id': 'com.aaronjwood.portauthority:id/discoverHosts', 'coordinates': [540, 1783], 'text': None, 'direction': None, 'target_description': 'DISCOVER HOSTS button'},  # The first step of the task is to scan the local network for hosts. The 'DISCOVER HOSTS' button is...
    {'step': 7, 'type': 'tap', 'resource_id': 'com.aaronjwood.portauthority:id/discoverHosts', 'coordinates': [540, 1783], 'text': 'DISCOVER HOSTS (3)', 'direction': None, 'target_description': "the 'DISCOVER HOSTS (3)' button at the bottom of the screen"},  # The first step in the task is to scan the local network for hosts. The 'DISCOVER HOSTS (3)'...
    {'step': 9, 'type': 'tap', 'resource_id': 'com.aaronjwood.portauthority:id/discoverHosts', 'coordinates': None, 'text': None, 'direction': None, 'target_description': "Button with text 'DISCOVER HOSTS (3)'"},  # The first step of the task is to discover network hosts. The button 'DISCOVER HOSTS (3)'...
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
