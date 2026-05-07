#!/usr/bin/env python3
"""
Replay script — de.danoeh.antennapod / None
Generated: 2026-05-07T23:21:19.041939+00:00
Video: None
Task summary: --- app: AntennaPod goal: The user wants to find and listen to a podcast episode without subscribing. outcome: success - The user successfully found a podcast and started streaming an episode. ---...

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
    {'step': 1, 'type': 'tap', 'resource_id': 'de.danoeh.antennapod:id/bottom_navigation_queue', 'coordinates': None, 'text': None, 'direction': None, 'target_description': 'Queue tab'},  # Based on the video summary, the user first explores the different sections of the app. Since the...
    {'step': 2, 'type': 'tap', 'resource_id': 'de.danoeh.antennapod:id/bottom_navigation_subscriptions', 'coordinates': None, 'text': None, 'direction': None, 'target_description': 'the Subscriptions tab in the bottom navigation bar'},  # The user is exploring the app's main sections. Following the video summary, after checking the...
    {'step': 3, 'type': 'tap', 'resource_id': 'de.danoeh.antennapod:id/subscriptions_add', 'coordinates': [964, 1573], 'text': None, 'direction': None, 'target_description': 'the plus floating action button'},  # The task is to find and listen to a podcast. The current screen is the empty 'Subscriptions'...
    {'step': 4, 'type': 'tap', 'resource_id': 'de.danoeh.antennapod:id/errorRetryButton', 'coordinates': None, 'text': None, 'direction': None, 'target_description': "the 'Show suggestions' button"},  # The user wants to find a podcast to listen to. The video summary indicates that the user first...
    {'step': 5, 'type': 'tap', 'resource_id': 'de.danoeh.antennapod:id/discover_more', 'coordinates': [861, 1293], 'text': 'Discover more »', 'direction': None, 'target_description': "the 'Discover more' button"},  # The user wants to find a podcast to listen to. The video summary indicates that the user loads...
    {'step': 6, 'type': 'tap', 'resource_id': None, 'coordinates': [540, 1396], 'text': None, 'direction': None, 'target_description': 'Up First from NPR podcast'},  # The user wants to find and listen to an episode of 'Up First from NPR' without subscribing. The...
    {'step': 7, 'type': 'tap', 'resource_id': None, 'coordinates': None, 'text': "Trump's Iran Progress Claims, Oil Industry Profit From Iran War, Rubio...", 'direction': None, 'target_description': "the first episode in the 'Episodes preview' list, titled 'Trump's Iran Progress Claims...'"},  # The user wants to listen to a podcast episode without subscribing. The current screen shows the...
    {'step': 8, 'type': 'tap', 'resource_id': None, 'coordinates': [540, 1292], 'text': None, 'direction': None, 'target_description': "the first episode in the 'Episodes preview' list, titled 'Trump's Iran Progress Claims...'"},  # The user wants to listen to a podcast episode without subscribing. The current screen shows the...
    {'step': 9, 'type': 'tap', 'resource_id': 'de.danoeh.antennapod:id/butAction1', 'coordinates': [312, 698], 'text': None, 'direction': None, 'target_description': 'Stream button'},  # The user wants to listen to the podcast episode. Tapping the 'Stream' button will start playback,...
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
