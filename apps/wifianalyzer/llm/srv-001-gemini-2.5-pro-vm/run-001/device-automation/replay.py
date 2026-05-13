#!/usr/bin/env python3
"""
Replay script — com.vrem.wifianalyzer / None
Generated: 2026-05-07T22:22:46.901378+00:00
Video: None
Task summary: --- app: WiFiAnalyzer (open-source) goal: The user wanted to analyze the current Wi-Fi network and export the collected data. outcome: success - The user successfully generated and copied the...

Usage:
    python replay.py [--serial SERIAL] [--delay SECONDS] [--skip-install]
"""
import argparse
import subprocess
import sys
import time

import uiautomator2 as u2

APK_PATH = 'apps/wifianalyzer/apk/wifianalyzer.apk'
PACKAGE  = 'com.vrem.wifianalyzer'
ACTIVITY = 'com.vrem.wifianalyzer.MainActivity'

ACTIONS = [
    {'step': 1, 'type': 'tap', 'resource_id': 'android:id/button1', 'coordinates': [894, 1580], 'text': 'OK', 'direction': None, 'target_description': 'the OK button'},  # The user is presented with an informational dialog upon opening the app. To proceed to the main...
    {'step': 2, 'type': 'tap', 'resource_id': 'com.android.permissioncontroller:id/permission_allow_foreground_only_button', 'coordinates': [540, 1199], 'text': 'While using the app', 'direction': None, 'target_description': "the 'While using the app' button to grant location permission"},  # The WiFiAnalyzer app requires location permission to scan for and analyze Wi-Fi networks. To...
    {'step': 3, 'type': 'tap', 'resource_id': 'com.vrem.wifianalyzer:id/nav_bottom_channel_rating', 'coordinates': [405, 1783], 'text': None, 'direction': None, 'target_description': 'Channel Rating tab'},  # The first step of the task is to navigate to the 'Channel Rating' screen. The current screen is...
    {'step': 4, 'type': 'tap', 'resource_id': 'com.vrem.wifianalyzer:id/nav_bottom_channel_graph', 'coordinates': None, 'text': None, 'direction': None, 'target_description': "the 'Channel Graph' tab"},  # The user is currently on the 'Channel Rating' screen. According to the task summary, the next...
    {'step': 5, 'type': 'tap', 'resource_id': 'com.vrem.wifianalyzer:id/nav_bottom_time_graph', 'coordinates': [945, 1783], 'text': None, 'direction': None, 'target_description': "the 'Time Graph' tab in the bottom navigation bar"},  # Based on the video summary, after viewing the 'Channel Graph', the user proceeds to the 'Time...
    {'step': 6, 'type': 'tap', 'resource_id': 'com.vrem.wifianalyzer:id/nav_bottom_channel_graph', 'coordinates': [675, 1783], 'text': None, 'direction': None, 'target_description': 'Channel Graph tab'},  # The user has finished viewing the 'Time Graph'. Based on the provided steps, the next action is...
    {'step': 7, 'type': 'tap', 'resource_id': None, 'coordinates': [660, 650], 'text': None, 'direction': None, 'target_description': "the graph bar for the 'AndroidWifi 8' network"},  # Based on the video summary, after navigating through the different graph views, the user taps on...
    {'step': 8, 'type': 'tap', 'resource_id': None, 'coordinates': [73, 136], 'text': None, 'direction': None, 'target_description': 'hamburger menu icon'},  # Based on the video summary, after exploring the different graph views, the user opens the side...
    {'step': 9, 'type': 'tap', 'resource_id': 'com.vrem.wifianalyzer:id/nav_drawer_export', 'coordinates': None, 'text': None, 'direction': None, 'target_description': 'Export menu item'},  # The user's goal is to export the Wi-Fi data. The navigation menu is currently open, and the next...
    {'step': 10, 'type': 'tap', 'resource_id': 'com.android.intentresolver:id/copy', 'coordinates': [964, 984], 'text': None, 'direction': None, 'target_description': 'Copy icon'},  # The user has exported the Wi-Fi data and is now presented with a sharing dialog. According to the...
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
