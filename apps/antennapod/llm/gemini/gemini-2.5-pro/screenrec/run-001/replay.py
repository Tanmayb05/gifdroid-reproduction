#!/usr/bin/env python3
"""
Replay script — de.danoeh.antennapod / apps/AntennaPod/videos/srv-001.mp4
Generated: 2026-05-01T15:44:20.985924+00:00
Video: apps/AntennaPod/videos/srv-001.mp4
Task summary: The user opens the AntennaPod app to find a new podcast to listen to. They navigate to the "Add podcast" screen, tap "Show suggestions," and select the "Up First from NPR" podcast from the list....

Usage:
    python replay.py [--serial SERIAL] [--delay SECONDS] [--skip-install]
"""
import argparse
import subprocess
import sys
import time

import uiautomator2 as u2

APK_PATH = 'apps/AntennaPod/apk/AntennaPod.apk'
PACKAGE  = 'de.danoeh.antennapod'
ACTIVITY = 'de.danoeh.antennapod.activity.SplashActivity'

ACTIONS = [
    {'step': 1, 'type': 'tap', 'resource_id': 'de.danoeh.antennapod:id/bottom_navigation_more', 'coordinates': None, 'text': None, 'direction': None, 'target_description': "the 'More' button in the bottom navigation bar"},  # The task is to add a new podcast. The current screen instructs the user to 'Open the menu to add...
    {'step': 2, 'type': 'tap', 'resource_id': None, 'coordinates': [752, 1352], 'text': None, 'direction': None, 'target_description': "the 'Add podcast' menu item"},  # The user wants to add a new podcast. The current screen shows a menu with an 'Add podcast'...
    {'step': 3, 'type': 'tap', 'resource_id': 'de.danoeh.antennapod:id/errorRetryButton', 'coordinates': [539, 913], 'text': None, 'direction': None, 'target_description': "the 'Show suggestions' button"},  # The task is to find a new podcast by looking at suggestions. The next step in the video summary...
    {'step': 4, 'type': 'tap', 'resource_id': None, 'coordinates': [166, 1094], 'text': None, 'direction': None, 'target_description': "the 'Up First' podcast suggestion"},  # The user wants to listen to the 'Up First from NPR' podcast. Based on the video summary, the next...
    {'step': 5, 'type': 'tap', 'resource_id': None, 'coordinates': [540, 1292], 'text': None, 'direction': None, 'target_description': "the first episode preview for 'Stalemate In The Strait Of Hormuz, DHS Shutdown Ends, Trump's Surge...'"},  # The user wants to play the first episode of the podcast. The next step according to the video...
    {'step': 6, 'type': 'tap', 'resource_id': 'de.danoeh.antennapod:id/butAction1', 'coordinates': [312, 698], 'text': None, 'direction': None, 'target_description': 'the Stream button'},  # The user wants to listen to the podcast. The video summary indicates that the next step is to...
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
