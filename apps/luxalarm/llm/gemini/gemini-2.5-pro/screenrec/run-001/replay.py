#!/usr/bin/env python3
"""
Replay script — com.dsalmun.luxalarm / apps/luxalarm/videos/screenrec/srv-001.mp4
Generated: 2026-04-10T05:34:21.979746+00:00
Video: apps/luxalarm/videos/screenrec/srv-001.mp4
Task summary: The user opens the Lux Alarm app and creates a new alarm for 10:25. They then expand the alarm's options to set it to repeat on Mondays and Fridays. Finally, the user changes the alarm sound from...

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
    {'step': 1, 'type': 'tap', 'resource_id': None, 'coordinates': [950, 320], 'text': None, 'direction': None, 'target_description': 'the downward-pointing arrow to expand the alarm options'},  # The video summary indicates that the next step is to expand the alarm's options to change the...
    {'step': 2, 'type': 'tap', 'resource_id': None, 'coordinates': [368, 815], 'text': None, 'direction': None, 'target_description': "the alarm sound setting, currently 'Default (Cesium)'"},  # The alarm has been set for 10:25 on Monday and Friday. The next step in the task is to change the...
    {'step': 3, 'type': 'scroll', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': 'down', 'target_description': 'the list of sound categories'},  # The user needs to select the 'Brook' sound from the 'Natural Elements' category. The 'Natural...
    {'step': 4, 'type': 'scroll', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': 'down', 'target_description': 'the list of ringtone categories'},  # The user needs to select the 'Brook' ringtone from the 'Natural Elements' category. The 'Natural...
    {'step': 5, 'type': 'scroll', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': 'down', 'target_description': 'the list of sound categories'},  # The user needs to find the 'Natural Elements' sound category to select the 'Brook' sound. This...
    {'step': 6, 'type': 'scroll', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': 'down', 'target_description': 'the list of sound categories'},  # The user needs to select the 'Brook' sound from the 'Natural Elements' category. This category is...
    {'step': 7, 'type': 'scroll', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': 'down', 'target_description': "Scroll down to find the 'Natural Elements' sound category."},  # The user wants to select the 'Brook' sound, which is located in the 'Natural Elements' category....
    {'step': 8, 'type': 'scroll', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': 'down', 'target_description': 'the list of sound categories'},  # The user needs to find the 'Natural Elements' sound category to select the 'Brook' sound. This...
    {'step': 9, 'type': 'scroll', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': 'down', 'target_description': 'the list of sound categories'},  # The task is to select the 'Brook' sound from the 'Natural Elements' category. The 'Natural...
    {'step': 10, 'type': 'scroll', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': 'down', 'target_description': 'the list of sound categories'},  # The user needs to select the 'Brook' sound from the 'Natural Elements' category. The 'Natural...
    {'step': 11, 'type': 'scroll', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': 'down', 'target_description': 'the list of ringtone categories'},  # The user needs to select the 'Brook' sound from the 'Natural Elements' category. This category is...
    {'step': 12, 'type': 'scroll', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': 'down', 'target_description': "Scroll down to find the 'Natural Elements' sound category."},  # The user needs to select the 'Brook' sound from the 'Natural Elements' category. The 'Natural...
    {'step': 13, 'type': 'scroll', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': 'down', 'target_description': 'the list of sound categories'},  # The target sound category, 'Natural Elements', is not visible on the current screen. Therefore, I...
    {'step': 14, 'type': 'scroll', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': 'down', 'target_description': 'the list of sound categories'},  # The user needs to select the 'Brook' sound from the 'Natural Elements' category. The 'Natural...
    {'step': 15, 'type': 'scroll', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': 'down', 'target_description': 'the list of sound categories'},  # The user needs to select the 'Brook' sound from the 'Natural Elements' category. The 'Natural...
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
