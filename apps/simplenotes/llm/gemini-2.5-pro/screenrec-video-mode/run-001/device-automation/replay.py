#!/usr/bin/env python3
"""
Replay script — dev.dettmer.simplenotes / None
Generated: 2026-05-07T15:17:42.119215+00:00
Video: None
Task summary: --- app: Simple Notes goal: To create, edit, and then delete a checklist note. outcome: success - The user successfully created, added items to, and deleted a checklist note. --- ## Session Summary...

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
    {'step': 1, 'type': 'tap', 'resource_id': 'com.android.permissioncontroller:id/permission_deny_button', 'coordinates': [540, 1196], 'text': None, 'direction': None, 'target_description': "Don't allow button"},  # The application is requesting notification permissions, which is blocking the main UI. The task...
    {'step': 2, 'type': 'tap', 'resource_id': None, 'coordinates': [540, 1903], 'text': 'Got it!', 'direction': None, 'target_description': 'Got it! button'},  # The current screen is a 'What's New' dialog that is overlaying the main application. To begin the...
    {'step': 3, 'type': 'tap', 'resource_id': None, 'coordinates': [540, 1753], 'text': None, 'direction': None, 'target_description': "the 'Got it!' button"},  # The 'What's New' dialog is obscuring the main application screen. To proceed with the task of...
    {'step': 4, 'type': 'tap', 'resource_id': None, 'coordinates': [964, 1741], 'text': None, 'direction': None, 'target_description': 'plus button'},  # The task is to create a new note. The screen displays 'No notes yet' and 'Tap + to create a new...
    {'step': 5, 'type': 'tap', 'resource_id': None, 'coordinates': [826, 1546], 'text': 'Checklist', 'direction': None, 'target_description': 'Checklist button'},  # The user wants to create a new checklist note. The current screen shows a menu with options to...
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
