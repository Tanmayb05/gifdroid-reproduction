#!/usr/bin/env python3
"""
Replay script — org.fossify.gallery / None
Generated: 2026-07-31T19:26:13.188640+00:00
Video: None
Task summary: --- app: Simple Gallery goal: To enable and use the feature for changing images by tapping the sides of the screen. outcome: failure — The feature did not work; tapping the screen sides only...

Usage:
    python replay.py [--serial SERIAL] [--delay SECONDS] [--skip-install]
"""
import argparse
import subprocess
import sys
import time

import uiautomator2 as u2

APK_PATH = 'apps/fossifygallery/apk/fossifygallery.apk'
PACKAGE  = 'org.fossify.gallery'
ACTIVITY = None

ACTIONS = [
    {'step': 1, 'type': 'tap', 'resource_id': 'com.android.permissioncontroller:id/permission_allow_button', 'coordinates': [540, 1263], 'text': 'Allow', 'direction': None, 'target_description': 'Allow button to grant media access'},  # The application requires permission to access photos and media to display the gallery. Granting...
    {'step': 2, 'type': 'tap', 'resource_id': 'android:id/button1', 'coordinates': [831, 1459], 'text': 'All files', 'direction': None, 'target_description': 'All files button'},  # The app is requesting file access, which is a prerequisite for the main task of viewing and...
    {'step': 3, 'type': 'tap', 'resource_id': None, 'coordinates': [950, 990], 'text': None, 'direction': None, 'target_description': "toggle switch for 'Allow access to manage all files'"},  # To reproduce the task, the app first needs permission to access and manage files. The current...
    {'step': 4, 'type': 'press_back', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': None, 'target_description': 'Back button'},  # The necessary file access permission has been granted. To continue with the task, I need to...
    {'step': 5, 'type': 'tap', 'resource_id': None, 'coordinates': [810, 1041], 'text': None, 'direction': None, 'target_description': 'Download folder with a purple and orange sci-fi image'},  # The first step of the task is to open an image. The video summary specifies that the user taps an...
    {'step': 6, 'type': 'tap', 'resource_id': 'org.fossify.gallery:id/media_item_holder', 'coordinates': [180, 411], 'text': None, 'direction': None, 'target_description': 'Image thumbnail'},  # The task starts from the gallery's folder view. The first step is to open an image to get to the...
    {'step': 7, 'type': 'tap', 'resource_id': None, 'coordinates': [270, 1200], 'text': None, 'direction': None, 'target_description': 'Left side of the image'},  # I am following step 8 of the task description, which is to test the 'change media by tapping...
    {'step': 8, 'type': 'tap', 'resource_id': 'android:id/ok', 'coordinates': [859, 527], 'text': 'Got it', 'direction': None, 'target_description': "the 'Got it' button"},  # The screen displays a 'Viewing full screen' informational overlay. To proceed with the task, I...
    {'step': 9, 'type': 'tap', 'resource_id': None, 'coordinates': [1000, 1200], 'text': None, 'direction': None, 'target_description': 'Right side of the image'},  # I have successfully enabled the setting and returned to the image viewer. The next step is to...
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
    elif atype in ("long_tap", "long_press"):
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
            ["adb", "shell", "monkey", "-p", PACKAGE, "-c",
             "android.intent.category.LAUNCHER", "1"],
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
