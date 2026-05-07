#!/usr/bin/env python3
"""
Replay script — com.dsalmun.luxalarm / None
Generated: 2026-05-07T14:43:59.504812+00:00
Video: None
Task summary: --- app: Lux Alarm goal: Set a new alarm for a specific time and customize its ringtone. outcome: success — The alarm was created for 12:15 and the ringtone was successfully changed to "Victory...

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
    {'step': 1, 'type': 'tap', 'resource_id': None, 'coordinates': [540, 1123], 'text': None, 'direction': None, 'target_description': 'a large, circular icon of a teal alarm clock with a rising sun'},  # The task is to set a new alarm. The current screen is the app's initial empty state. The first...
    {'step': 2, 'type': 'tap', 'resource_id': None, 'coordinates': [964, 1741], 'text': None, 'direction': None, 'target_description': "the '+' button"},  # The task is to set a new alarm. The current screen is the empty state, which prompts the user to...
    {'step': 3, 'type': 'tap', 'resource_id': None, 'coordinates': [631, 892], 'text': None, 'direction': None, 'target_description': '12 on the clock face'},  # The goal is to set an alarm for 12:15. The current screen is for setting the alarm time, and the...
    {'step': 4, 'type': 'tap', 'resource_id': None, 'coordinates': [383, 513], 'text': None, 'direction': None, 'target_description': "the hour '13' in the digital time display"},  # The goal is to set the alarm for 12:15. The current screen shows the alarm time being set to...
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
