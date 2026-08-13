#!/usr/bin/env python3
"""
Replay script — org.fossify.gallery / None
Generated: 2026-07-31T19:22:26.579218+00:00
Video: None
Task summary: --- app: Gallery / ScreenshotEditor goal: The user was trying to edit an image by applying a filter and saving the result. outcome: failure — The image disappeared from the editor after the user...

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
    {'step': 1, 'type': 'tap', 'resource_id': 'com.android.permissioncontroller:id/permission_allow_button', 'coordinates': None, 'text': None, 'direction': None, 'target_description': 'Allow button'},  # The first step of the task is to open an image from the gallery. To do that, the app needs...
    {'step': 2, 'type': 'tap', 'resource_id': 'android:id/button3', 'coordinates': None, 'text': 'Media only', 'direction': None, 'target_description': 'Media only button'},  # The application is requesting file access permissions. To proceed with the task, which starts...
    {'step': 3, 'type': 'tap', 'resource_id': None, 'coordinates': [73, 136], 'text': None, 'direction': None, 'target_description': 'Back arrow'},  # I am currently on a system settings page for media management. To proceed with the task, which...
    {'step': 4, 'type': 'tap', 'resource_id': 'org.fossify.gallery:id/dir_holder', 'coordinates': [810, 1041], 'text': None, 'direction': None, 'target_description': 'Download folder thumbnail'},  # The first step of the task is to open the image from the 'Download' folder. The current screen...
    {'step': 5, 'type': 'tap', 'resource_id': 'org.fossify.gallery:id/media_item_holder', 'coordinates': [180, 411], 'text': None, 'direction': None, 'target_description': 'Image thumbnail'},  # The first step of the task is to open an image from the gallery folder view. I am tapping on the...
    {'step': 6, 'type': 'tap', 'resource_id': 'org.fossify.gallery:id/bottom_edit', 'coordinates': [421, 2179], 'text': None, 'direction': None, 'target_description': 'Edit icon'},  # The current screen is the full-screen image viewer. According to step 2 of the plan, the next...
    {'step': 7, 'type': 'tap', 'resource_id': None, 'coordinates': [221, 1897], 'text': None, 'direction': None, 'target_description': 'Markup'},  # This corresponds to Step 3 of the task, 'Select Editor App'. The original user selected...
    {'step': 8, 'type': 'tap', 'resource_id': 'org.fossify.gallery:id/bottom_primary_filter', 'coordinates': None, 'text': None, 'direction': None, 'target_description': 'Filters icon'},  # The current screen is the editor's crop/rotate view. According to the task steps, the next action...
    {'step': 9, 'type': 'tap', 'resource_id': 'org.fossify.gallery:id/editor_filter_item_holder', 'coordinates': [300, 1988], 'text': None, 'direction': None, 'target_description': 'Struck filter thumbnail'},  # The current screen is the filter selection view in the editor. According to Step 5 of the task...
    {'step': 10, 'type': 'tap', 'resource_id': None, 'coordinates': [300, 1988], 'text': None, 'direction': None, 'target_description': 'Struck filter thumbnail'},  # The current step is to apply a filter to the image. According to the task summary (Step 5), the...
    {'step': 11, 'type': 'tap', 'resource_id': 'org.fossify.gallery:id/save_as', 'coordinates': [784, 146], 'text': None, 'direction': None, 'target_description': 'Save icon'},  # The previous step was to apply the 'Struck' filter, which has been done. The next step in the...
    {'step': 12, 'type': 'tap', 'resource_id': 'android:id/button2', 'coordinates': [647, 1184], 'text': 'Cancel', 'direction': None, 'target_description': 'Cancel button'},  # The current screen shows the 'Save as' dialog. According to the task steps, the next action is to...
    {'step': 13, 'type': 'tap', 'resource_id': 'org.fossify.gallery:id/save_as', 'coordinates': [784, 146], 'text': None, 'direction': None, 'target_description': 'Save icon (checkmark)'},  # The task requires applying a filter and then initiating the save process. The 'Struck' filter has...
    {'step': 14, 'type': 'tap', 'resource_id': 'android:id/button1', 'coordinates': [842, 1184], 'text': 'OK', 'direction': None, 'target_description': "OK button in the 'Save as' dialog"},  # Following the session summary, after re-initiating the save on the blank screen (Step 8), the...
    {'step': 15, 'type': 'tap', 'resource_id': 'android:id/button1', 'coordinates': [802, 1553], 'text': 'Allow', 'direction': None, 'target_description': 'Allow button'},  # I am currently in the process of trying to save the (now blank) image, which corresponds to Step...
    {'step': 16, 'type': 'tap', 'resource_id': 'android:id/button1', 'coordinates': [842, 1716], 'text': 'OK', 'direction': None, 'target_description': "OK button in the 'Confirm folder access' dialog"},  # The previous two actions were also tapping the 'OK' button, and the screen did not change....
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
