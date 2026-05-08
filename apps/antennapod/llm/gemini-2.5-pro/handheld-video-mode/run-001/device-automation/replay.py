#!/usr/bin/env python3
"""
Replay script — de.danoeh.antennapod / None
Generated: 2026-05-08T07:00:16.538239+00:00
Video: None
Task summary: --- app: AntennaPod goal: The user wants to find and subscribe to a new podcast. outcome: success - The user successfully subscribed to "The Daily" podcast. --- ## Session Summary The user started...

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
    {'step': 1, 'type': 'tap', 'resource_id': 'de.danoeh.antennapod:id/bottom_navigation_subscriptions', 'coordinates': [756, 1773], 'text': None, 'direction': None, 'target_description': 'the Subscriptions tab in the bottom navigation bar'},  # The first step to subscribing to a new podcast is to navigate to the subscriptions section. The...
    {'step': 2, 'type': 'tap', 'resource_id': 'de.danoeh.antennapod:id/subscriptions_add', 'coordinates': [964, 1573], 'text': None, 'direction': None, 'target_description': 'Plus icon'},  # The user wants to subscribe to a new podcast. The current screen is the empty subscriptions list....
    {'step': 3, 'type': 'tap', 'resource_id': 'de.danoeh.antennapod:id/errorRetryButton', 'coordinates': None, 'text': 'Show suggestions', 'direction': None, 'target_description': 'Show suggestions button'},  # The user wants to subscribe to a podcast from the suggestions. The suggestions are not currently...
    {'step': 4, 'type': 'tap', 'resource_id': None, 'coordinates': [166, 596], 'text': None, 'direction': None, 'target_description': 'The Daily podcast suggestion'},  # The user wants to subscribe to a new podcast. The video summary shows the user selecting 'The...
    {'step': 5, 'type': 'tap', 'resource_id': 'de.danoeh.antennapod:id/butSubscribe', 'coordinates': [578, 714], 'text': 'Subscribe', 'direction': None, 'target_description': "the 'Subscribe' button"},  # The user's goal is to subscribe to the podcast. The current screen is the detail page for 'The...
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
