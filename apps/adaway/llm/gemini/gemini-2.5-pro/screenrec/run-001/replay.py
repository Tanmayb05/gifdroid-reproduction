#!/usr/bin/env python3
"""
Replay script — org.adaway / apps/adaway/videos/screenrec/srv-001.mp4
Generated: 2026-04-10T04:51:52.495088+00:00
Video: apps/adaway/videos/screenrec/srv-001.mp4
Task summary: The user opens the AdAway app from their home screen. They then navigate to the "Your lists" section from the menu in the bottom-left corner. On the "Allowed" tab, the user taps the plus button to...

Usage:
    python replay.py [--serial SERIAL] [--delay SECONDS] [--skip-install]
"""
import argparse
import subprocess
import sys
import time

import uiautomator2 as u2

APK_PATH = 'apps/adaway/apk/adaway.apk'
PACKAGE  = 'org.adaway'
ACTIVITY = 'org.adaway.ui.home.HomeActivity'

ACTIONS = [
    {'step': 1, 'type': 'tap', 'resource_id': None, 'coordinates': [73, 1783], 'text': None, 'direction': None, 'target_description': 'the menu icon in the bottom-left corner'},  # The first step in the task is to navigate to the 'Your lists' section. This is typically done by...
    {'step': 2, 'type': 'tap', 'resource_id': 'org.adaway:id/allowedHostCardView', 'coordinates': [540, 511], 'text': None, 'direction': None, 'target_description': "the 'Allowed' card with the number 2"},  # The task is to add a host to the allowed list. The current screen is the main dashboard of the...
    {'step': 3, 'type': 'tap', 'resource_id': 'org.adaway:id/lists_add', 'coordinates': [964, 1594], 'text': None, 'direction': None, 'target_description': 'the red plus button'},  # The user needs to add a new host to the allowed list. The red plus button is the standard UI...
    {'step': 4, 'type': 'type_text', 'resource_id': 'org.adaway:id/list_dialog_hostname', 'coordinates': [540, 950], 'text': 'utl.web', 'direction': None, 'target_description': "the text input field with the current text 'The hosts source URL'"},  # The user needs to enter the hostname 'utl.web' into the text field before adding it to the...
    {'step': 5, 'type': 'tap', 'resource_id': 'android:id/button1', 'coordinates': [884, 1170], 'text': 'ADD', 'direction': None, 'target_description': 'the ADD button'},  # The user has entered the hostname 'utl.web' and now needs to confirm adding it to the whitelist...
    {'step': 6, 'type': 'type_text', 'resource_id': 'org.adaway:id/list_dialog_hostname', 'coordinates': None, 'text': 'utl.web', 'direction': None, 'target_description': "the hostname input field with placeholder text 'The hosts source URL'"},  # The task is to add 'utl.web' to the whitelist. The screenshot shows the 'Add host to whitelist'...
    {'step': 7, 'type': 'type_text', 'resource_id': 'org.adaway:id/list_dialog_hostname', 'coordinates': None, 'text': 'utl.web', 'direction': None, 'target_description': "the text input field with the current text 'The hosts source URL'"},  # The task is to add 'utl.web' to the whitelist. The 'Add host to whitelist' dialog is currently...
    {'step': 8, 'type': 'type_text', 'resource_id': 'org.adaway:id/list_dialog_hostname', 'coordinates': [540, 950], 'text': 'utl.web', 'direction': None, 'target_description': "the text input field with current text 'The hosts source URL'"},  # The task is to add 'utl.web' to the whitelist. The screenshot shows the 'Add host to whitelist'...
    {'step': 9, 'type': 'type_text', 'resource_id': 'org.adaway:id/list_dialog_hostname', 'coordinates': None, 'text': 'utl.web', 'direction': None, 'target_description': "the hostname text input field with current text 'The hosts source URL'"},  # The task is to add 'utl.web' to the whitelist. The screenshot shows the 'Add host to whitelist'...
    {'step': 10, 'type': 'tap', 'resource_id': 'android:id/button1', 'coordinates': None, 'text': None, 'direction': None, 'target_description': 'the ADD button'},  # The user has typed 'utl.web' into the hostname field. The next step is to tap the 'ADD' button to...
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
