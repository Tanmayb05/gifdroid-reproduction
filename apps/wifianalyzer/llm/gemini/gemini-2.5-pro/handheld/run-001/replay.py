#!/usr/bin/env python3
"""
Replay script — com.vrem.wifianalyzer / apps/wifianalyzer/videos/handheld/hhv-001.mp4
Generated: 2026-04-10T06:26:19.046089+00:00
Video: apps/wifianalyzer/videos/handheld/hhv-001.mp4
Task summary: The user opens the WIFIAnalyzer app from its store page to analyze local Wi-Fi networks. After scrolling through the list of "Access Points," they use the bottom navigation bar to cycle through the...

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
    {'step': 1, 'type': 'tap', 'resource_id': 'android:id/button1', 'coordinates': [894, 1580], 'text': 'OK', 'direction': None, 'target_description': 'the OK button'},  # The current screen shows an informational pop-up from the WiFiAnalyzer app. To proceed with the...
    {'step': 2, 'type': 'tap', 'resource_id': 'com.android.permissioncontroller:id/permission_allow_foreground_only_button', 'coordinates': [540, 1199], 'text': 'While using the app', 'direction': None, 'target_description': "the 'While using the app' button to grant location permission"},  # The task requires using the WiFiAnalyzer app, which needs location permission to scan for Wi-Fi...
    {'step': 3, 'type': 'tap', 'resource_id': 'com.vrem.wifianalyzer:id/nav_bottom_channel_rating', 'coordinates': [405, 1783], 'text': None, 'direction': None, 'target_description': 'the Channel Rating tab'},  # The task is to navigate through the different views of the app using the bottom navigation bar....
    {'step': 4, 'type': 'tap', 'resource_id': 'com.vrem.wifianalyzer:id/nav_bottom_channel_graph', 'coordinates': None, 'text': None, 'direction': None, 'target_description': 'the Channel Graph icon in the bottom navigation bar'},  # The task is to cycle through the different views. The current view is 'Channel Rating', so the...
    {'step': 5, 'type': 'tap', 'resource_id': 'com.vrem.wifianalyzer:id/nav_bottom_time_graph', 'coordinates': None, 'text': None, 'direction': None, 'target_description': 'Time Graph'},  # The user is currently on the 'Channel Graph' screen. According to the video summary, the next...
    {'step': 6, 'type': 'tap', 'resource_id': 'com.vrem.wifianalyzer:id/nav_bottom_channel_graph', 'coordinates': None, 'text': None, 'direction': None, 'target_description': 'the Channel Graph tab'},  # The task requires navigating back through the views in reverse order. After reaching the 'Time...
    {'step': 7, 'type': 'tap', 'resource_id': 'com.vrem.wifianalyzer:id/nav_bottom_channel_rating', 'coordinates': None, 'text': None, 'direction': None, 'target_description': 'the Channel Rating tab'},  # The user is navigating back through the bottom navigation bar. The previous step was to go from...
    {'step': 8, 'type': 'tap', 'resource_id': 'com.vrem.wifianalyzer:id/nav_bottom_access_points', 'coordinates': None, 'text': None, 'direction': None, 'target_description': 'the Access Points tab in the bottom navigation bar'},  # The task requires navigating back through the screens in reverse order. The current screen is...
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
