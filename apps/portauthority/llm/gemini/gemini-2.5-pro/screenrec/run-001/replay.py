#!/usr/bin/env python3
"""
Replay script — com.aaronjwood.portauthority / apps/portauthority/videos/screenrec/srv-001.mp4
Generated: 2026-04-10T06:00:02.591073+00:00
Video: apps/portauthority/videos/screenrec/srv-001.mp4
Task summary: The user opens the Port Authority app and scans their local network for hosts. After the scan completes, they select the host with the IP address `fec0::2`. The user then initiates a scan of all...

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
    {'step': 1, 'type': 'tap', 'resource_id': 'com.aaronjwood.portauthority:id/discoverHosts', 'coordinates': [540, 1783], 'text': 'DISCOVER HOSTS', 'direction': None, 'target_description': "the 'DISCOVER HOSTS' button"},  # The first step in the task is to scan the local network for hosts. The 'DISCOVER HOSTS' button on...
    {'step': 3, 'type': 'tap', 'resource_id': None, 'coordinates': [540, 908], 'text': None, 'direction': None, 'target_description': 'the host with IP address fec0::2'},  # The user wants to scan the ports of the host with the IP address `fec0::2`. The current screen...
    {'step': 4, 'type': 'tap', 'resource_id': 'com.aaronjwood.portauthority:id/scanPortRange', 'coordinates': [533, 1720], 'text': 'SCAN PORT RANGE', 'direction': None, 'target_description': "the 'SCAN PORT RANGE' button"},  # The user wants to scan all ports on the selected host. The 'SCAN PORT RANGE' button will allow...
    {'step': 5, 'type': 'tap', 'resource_id': 'com.aaronjwood.portauthority:id/startPortRangeScan', 'coordinates': [539, 1354], 'text': 'SCAN PORT RANGE', 'direction': None, 'target_description': "the 'SCAN PORT RANGE' button"},  # The task is to scan all ports from 1 to 65535. The port range is already correctly set, so the...
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
