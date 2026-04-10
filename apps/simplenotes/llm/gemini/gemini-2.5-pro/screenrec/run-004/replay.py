#!/usr/bin/env python3
"""
Replay script — dev.dettmer.simplenotes / apps/simplenotes/videos/screenrec/srv-001.mp4
Generated: 2026-04-10T06:19:59.787881+00:00
Video: apps/simplenotes/videos/screenrec/srv-001.mp4
Task summary: The user opens the Simple Notes app and dismisses the "What's New" pop-up. They then create a new text note, titling it "hello" and adding "hiasdb" as the content. After the note is saved, the user...

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
    {'step': 1, 'type': 'tap', 'resource_id': 'com.android.permissioncontroller:id/permission_deny_button', 'coordinates': [540, 1196], 'text': "Don't allow", 'direction': None, 'target_description': "the 'Don't allow' button to dismiss the notification permission request"},  # The task requires interacting with the main app screen to create a note. To proceed, the...
    {'step': 2, 'type': 'tap', 'resource_id': None, 'coordinates': [964, 1741], 'text': None, 'direction': None, 'target_description': 'the plus button to create a new note'},  # The task is to create a new note. The screen prompts the user to 'Tap + to create a new note',...
    {'step': 3, 'type': 'tap', 'resource_id': None, 'coordinates': [881, 1458], 'text': None, 'direction': None, 'target_description': 'Text note'},  # The user wants to create a new text note. After tapping the '+' button, the 'Text note' option...
    {'step': 4, 'type': 'type_text', 'resource_id': None, 'coordinates': [540, 357], 'text': 'hello', 'direction': None, 'target_description': 'the title text field'},  # The user wants to create a new note with the title 'hello'. The current screen is for creating a...
    {'step': 5, 'type': 'type_text', 'resource_id': None, 'coordinates': [540, 1149], 'text': 'hiasdb', 'direction': None, 'target_description': 'the content text field'},  # The user has entered the title of the note. The next step is to enter the content, which is...
    {'step': 6, 'type': 'type_text', 'resource_id': None, 'coordinates': [540, 1149], 'text': 'hiasdb', 'direction': None, 'target_description': "the content text input field with placeholder 'Content'"},  # The task is to create a note with the title 'hello' and content 'hiasdb'. The title has already...
    {'step': 7, 'type': 'type_text', 'resource_id': None, 'coordinates': [540, 357], 'text': 'hello', 'direction': None, 'target_description': "the title text input with current text 'hellohiasdbhiasdb'"},  # The current title of the note is 'hellohiasdbhiasdb', which is incorrect according to the task...
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
