#!/usr/bin/env python3
"""
Replay script — io.gitlab.derjosef.jigsaw / apps/jigsaw/videos/handheld/hhv-001.mp4
Generated: 2026-04-10T05:17:56.271170+00:00
Video: apps/jigsaw/videos/handheld/hhv-001.mp4
Task summary: The user opens the "Jigsaw" puzzle app from its app store page. On the main menu, they adjust the "Puzzle Size" settings, changing the number of horizontal and vertical pieces for the puzzle....

Usage:
    python replay.py [--serial SERIAL] [--delay SECONDS] [--skip-install]
"""
import argparse
import subprocess
import sys
import time

import uiautomator2 as u2

APK_PATH = 'apps/jigsaw/apk/jigsaw.apk'
PACKAGE  = 'io.gitlab.derjosef.jigsaw'
ACTIVITY = 'com.godot.game.GodotApp'

ACTIONS = [
    {'step': 1, 'type': 'tap', 'resource_id': None, 'coordinates': [400, 520], 'text': None, 'direction': None, 'target_description': 'slider to adjust the number of horizontal puzzle pieces'},  # The video summary states that the user adjusts the puzzle size settings before generating a...
    {'step': 2, 'type': 'press_home', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': None, 'target_description': 'the home button'},  # The current screen is a file manager. To open the Jigsaw app from the app store, I need to first...
    {'step': 3, 'type': 'tap', 'resource_id': None, 'coordinates': [540, 1538], 'text': 'Play Store', 'direction': None, 'target_description': 'the Play Store app icon'},  # The task requires opening an app from the Play Store. The previous step was `press_home`, which...
    {'step': 4, 'type': 'tap', 'resource_id': 'com.android.vending:id/0_resource_name_obfuscated', 'coordinates': [539, 1341], 'text': 'Sign in', 'direction': None, 'target_description': "the 'Sign in' button"},  # The task requires opening an app from the app store. The current screen is the Google Play Store,...
    {'step': 5, 'type': 'press_back', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': None, 'target_description': 'the back button'},  # The current screen shows a menu open in the Google Play Store. To proceed with the task of...
    {'step': 6, 'type': 'press_back', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': None, 'target_description': 'the back button'},  # The current screen is the Google Play sign-in page, which is a detour from the main task of...
    {'step': 7, 'type': 'scroll', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': 'up', 'target_description': 'the home screen'},  # The task is to open the 'Jigsaw' puzzle app. The app is not on the home screen, so I need to...
    {'step': 8, 'type': 'scroll', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': 'up', 'target_description': 'the app drawer'},  # The task is to open the 'Jigsaw' puzzle app. The app is not on the current home screen. I need to...
    {'step': 9, 'type': 'tap', 'resource_id': None, 'coordinates': [540, 1538], 'text': 'Play Store', 'direction': None, 'target_description': 'the Play Store app icon'},  # The task is to open the 'Jigsaw' app from its app store page. The current screen is the Android...
    {'step': 10, 'type': 'tap', 'resource_id': 'com.android.vending:id/0_resource_name_obfuscated', 'coordinates': [539, 1341], 'text': 'Sign in', 'direction': None, 'target_description': "the 'Sign in' button"},  # The user needs to sign in to the Google Play Store to find and open the 'Jigsaw' app as described...
    {'step': 11, 'type': 'press_back', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': None, 'target_description': 'the back button'},  # The current screen is a sign-in prompt which is not part of the main task. Pressing back should...
    {'step': 12, 'type': 'press_home', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': None, 'target_description': 'the home button'},  # The current screen is a Google Play sign-in page, which is a deviation from the task of...
    {'step': 13, 'type': 'scroll', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': 'up', 'target_description': 'the screen to open the app drawer'},  # The task is to open the 'Jigsaw' puzzle app. The app is not on the home screen, so I need to open...
    {'step': 14, 'type': 'tap', 'resource_id': None, 'coordinates': [540, 1538], 'text': None, 'direction': None, 'target_description': 'Play Store'},  # The task is to open the 'Jigsaw' puzzle app from its app store page. The first step is to open...
    {'step': 15, 'type': 'tap', 'resource_id': 'com.android.vending:id/0_resource_name_obfuscated', 'coordinates': [539, 1341], 'text': 'Sign in', 'direction': None, 'target_description': "the 'Sign in' button"},  # The task is to open the 'Jigsaw' puzzle app from the app store. The current screen is the Google...
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
