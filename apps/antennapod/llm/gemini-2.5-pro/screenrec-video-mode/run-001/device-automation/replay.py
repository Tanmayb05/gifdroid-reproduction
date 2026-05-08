#!/usr/bin/env python3
"""
Replay script — de.danoeh.antennapod / None
Generated: 2026-05-08T07:07:51.015136+00:00
Video: None
Task summary: --- app: AntennaPod goal: To explore and modify various application settings. outcome: success - The user successfully navigated through different settings screens, modified two options, and...

Usage:
    python replay.py [--serial SERIAL] [--delay SECONDS] [--skip-install]
"""
import argparse
import subprocess
import sys
import time

import uiautomator2 as u2

APK_PATH = 'apps/antennapod/apk/antennapod.apk'
PACKAGE  = 'de.danoeh.antennapod'
ACTIVITY = 'de.danoeh.antennapod.activity.SplashActivity'

ACTIONS = [
    {'step': 1, 'type': 'tap', 'resource_id': None, 'coordinates': [1027, 146], 'text': None, 'direction': None, 'target_description': 'More options menu (three dots)'},  # The first step in the task is to attempt a refresh. To do this, the user first taps the 'More...
    {'step': 2, 'type': 'tap', 'resource_id': None, 'coordinates': [798, 168], 'text': None, 'direction': None, 'target_description': 'the Refresh option in the dropdown menu'},  # The user has opened the options menu on the home screen. According to the task summary, the first...
    {'step': 3, 'type': 'tap', 'resource_id': 'de.danoeh.antennapod:id/bottom_navigation_more', 'coordinates': [972, 1773], 'text': None, 'direction': None, 'target_description': 'More'},  # The user needs to navigate to the settings menu. According to the video summary and step-by-step...
    {'step': 4, 'type': 'tap', 'resource_id': None, 'coordinates': [752, 1606], 'text': None, 'direction': None, 'target_description': 'Settings'},  # The user wants to explore and modify application settings. The previous step opened the 'More'...
    {'step': 5, 'type': 'tap', 'resource_id': None, 'coordinates': [540, 687], 'text': None, 'direction': None, 'target_description': 'Playback'},  # The user is on the main settings screen. According to the task summary, the next step is to...
    {'step': 6, 'type': 'tap', 'resource_id': None, 'coordinates': [956, 489], 'text': None, 'direction': None, 'target_description': 'Headphones or Bluetooth disconnect toggle'},  # The user is on the Playback settings screen. According to the video summary, the next step is to...
    {'step': 7, 'type': 'press_back', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': None, 'target_description': 'Back arrow'},  # The user has finished modifying the playback settings. According to the session summary, the next...
    {'step': 8, 'type': 'tap', 'resource_id': None, 'coordinates': [73, 146], 'text': None, 'direction': None, 'target_description': 'Back arrow'},  # The current screen is the 'Playback' settings screen. According to the video summary, the next...
    {'step': 9, 'type': 'tap', 'resource_id': None, 'coordinates': [1027, 146], 'text': None, 'direction': None, 'target_description': 'More options menu (three dots)'},  # The first step of the task is to attempt a refresh by tapping the more options menu in the top...
    {'step': 10, 'type': 'press_back', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': None, 'target_description': 'Back button'},  # Based on the task summary, after modifying the 'Downloads' settings, the user returns to the home...
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
