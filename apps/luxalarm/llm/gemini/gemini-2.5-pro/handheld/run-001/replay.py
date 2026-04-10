#!/usr/bin/env python3
"""
Replay script — com.dsalmun.luxalarm / apps/luxalarm/videos/handheld/hhv-001.mp4
Generated: 2026-04-10T05:39:09.839339+00:00
Video: apps/luxalarm/videos/handheld/hhv-001.mp4
Task summary: The user opens the Lux Alarm app and taps the plus button to create a new alarm. They set the time to 01:25 using the clock interface and confirm the new alarm. The user then expands the alarm's...

Usage:
    python replay.py [--serial SERIAL] [--delay SECONDS] [--skip-install]
"""
import argparse
import subprocess
import sys
import time

import uiautomator2 as u2

APK_PATH = 'apps/luxalarm/apk/luxalarm.apk'
PACKAGE  = 'com.dsalmun.luxalarm'
ACTIVITY = 'com.dsalmun.luxalarm.MainActivity'

ACTIONS = [
    {'step': 1, 'type': 'press_back', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': None, 'target_description': 'the back button'},  # The video summary indicates that the user briefly opens and then closes the ringtone selection...
    {'step': 2, 'type': 'scroll', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': 'up', 'target_description': 'the app drawer'},  # The task is to open the Lux Alarm app. The app is not on the home screen, so I need to open the...
    {'step': 3, 'type': 'scroll', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': 'up', 'target_description': 'the home screen to open the app drawer'},  # The task is to open the Lux Alarm app. Since the app is not on the current home screen, I need to...
    {'step': 4, 'type': 'scroll', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': 'up', 'target_description': 'app drawer'},  # The Lux Alarm app is not on the home screen. I need to open the app drawer to find and open it....
    {'step': 5, 'type': 'scroll', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': 'up', 'target_description': 'the screen to open the app drawer'},  # The task is to open the Lux Alarm app. The app is not visible on the current home screen. To find...
    {'step': 6, 'type': 'tap', 'resource_id': 'com.google.android.apps.nexuslauncher:id/search_container_hotseat', 'coordinates': [540, 1727], 'text': None, 'direction': None, 'target_description': 'Google search bar'},  # To begin the task, I need to open the 'Lux Alarm' app. Since it's not on the home screen, I will...
    {'step': 7, 'type': 'type_text', 'resource_id': 'com.google.android.apps.nexuslauncher:id/input', 'coordinates': None, 'text': 'Lux Alarm', 'direction': None, 'target_description': "the search bar with text 'Search web and more'"},  # The task is to open the Lux Alarm app. The current screen is a search interface, so typing the...
    {'step': 8, 'type': 'tap', 'resource_id': None, 'coordinates': [140, 387], 'text': 'Lux Alarm', 'direction': None, 'target_description': 'the Lux Alarm app icon'},  # The user has searched for the 'Lux Alarm' app. The next step is to tap on the app icon to open...
    {'step': 9, 'type': 'tap', 'resource_id': None, 'coordinates': [964, 1741], 'text': None, 'direction': None, 'target_description': 'the plus button to add a new alarm'},  # The task is to create a new alarm. The current screen shows the main alarm list. The next step is...
    {'step': 10, 'type': 'tap', 'resource_id': None, 'coordinates': [698, 513], 'text': None, 'direction': None, 'target_description': "the minute display showing '37'"},  # The current view is for setting the alarm hour, as indicated by the highlighted '01' and the...
    {'step': 11, 'type': 'tap', 'resource_id': None, 'coordinates': [673, 1279], 'text': None, 'direction': None, 'target_description': 'the number 25 on the clock face'},  # The user wants to set the alarm time to 01:25. The hour is already set to 01. I need to change...
    {'step': 12, 'type': 'tap', 'resource_id': None, 'coordinates': [821, 1575], 'text': None, 'direction': None, 'target_description': 'Set button'},  # The task requires setting the alarm time to 01:25 and then confirming it. The time is already...
    {'step': 13, 'type': 'tap', 'resource_id': None, 'coordinates': [249, 777], 'text': None, 'direction': None, 'target_description': 'the time 01:25'},  # The task is to expand the options for the newly created alarm at 01:25. Tapping on the time...
    {'step': 14, 'type': 'tap', 'resource_id': None, 'coordinates': [698, 513], 'text': None, 'direction': None, 'target_description': "the minutes '25' in the digital time display"},  # The user has set the hour to '01'. The next step in setting the alarm time to 01:25 is to select...
    {'step': 15, 'type': 'tap', 'resource_id': None, 'coordinates': [821, 1575], 'text': None, 'direction': None, 'target_description': 'the Set button'},  # The alarm time has been set to 01:25 as per the video. The next step is to confirm this time by...
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
