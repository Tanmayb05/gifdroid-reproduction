#!/usr/bin/env python3
"""
Replay script — dev.dettmer.simplenotes / None
Generated: 2026-05-08T16:50:47.552254+00:00
Video: None
Task summary: --- app: Simple Notes goal: The user wants to create a new text note and then delete it. outcome: success - The user successfully created a note and then deleted it from the main list. --- ##...

Usage:
    python replay.py [--serial SERIAL] [--delay SECONDS] [--skip-install]
"""
import argparse
import subprocess
import sys
import time

import uiautomator2 as u2

APK_PATH = 'apps/simplenotes/apk/simplenotes.apk'
PACKAGE  = 'dev.dettmer.simplenotes'
ACTIVITY = 'dev.dettmer.simplenotes.ui.main.ComposeMainActivity'

ACTIONS = [
    {'step': 1, 'type': 'tap', 'resource_id': 'com.android.permissioncontroller:id/permission_deny_button', 'coordinates': [540, 1196], 'text': None, 'direction': None, 'target_description': 'Don’t allow button'},  # The current screen is a notification permission dialog. To proceed with the main task of creating...
    {'step': 2, 'type': 'tap', 'resource_id': None, 'coordinates': [540, 1753], 'text': None, 'direction': None, 'target_description': 'Got it! button'},  # The 'What's New' dialog is obscuring the main application interface. To proceed with the task of...
    {'step': 3, 'type': 'tap', 'resource_id': None, 'coordinates': [964, 1741], 'text': None, 'direction': None, 'target_description': 'the floating action button with a plus sign'},  # The goal is to create a new note. The screen displays 'Tap + to create a new note', and there is...
    {'step': 4, 'type': 'tap', 'resource_id': None, 'coordinates': [822, 1334], 'text': None, 'direction': None, 'target_description': 'Text Note button'},  # The user wants to create a new text note. The screen shows the options to create a 'Text Note' or...
    {'step': 5, 'type': 'type_text', 'resource_id': None, 'coordinates': [540, 357], 'text': 'Abc', 'direction': None, 'target_description': 'Title text input'},  # The current screen is for creating a new note. The next step according to the task summary is to...
    {'step': 6, 'type': 'type_text', 'resource_id': None, 'coordinates': [540, 1075], 'text': 'Xyz', 'direction': None, 'target_description': 'Content text area'},  # The user has entered the title of the note. The next step in the task is to type the content...
    {'step': 7, 'type': 'tap', 'resource_id': None, 'coordinates': [75, 148], 'text': None, 'direction': None, 'target_description': 'Back arrow icon'},  # The user has finished typing the title and content of the new note. According to the task...
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
