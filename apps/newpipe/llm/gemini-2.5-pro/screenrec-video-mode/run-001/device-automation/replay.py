#!/usr/bin/env python3
"""
Replay script — org.schabi.newpipe / None
Generated: 2026-05-07T14:52:19.965405+00:00
Video: None
Task summary: ```markdown app: NewPipe goal: The user wanted to find a trending music video and increase its playback speed. outcome: success — The user successfully found a video and adjusted its tempo. --- ##...

Usage:
    python replay.py [--serial SERIAL] [--delay SECONDS] [--skip-install]
"""
import argparse
import subprocess
import sys
import time

import uiautomator2 as u2

APK_PATH = 'apps/newpipe/apk/newpipe.apk'
PACKAGE  = 'org.schabi.newpipe'
ACTIVITY = 'org.schabi.newpipe.MainActivity'

ACTIONS = [
    {'step': 2, 'type': 'tap', 'resource_id': 'com.android.permissioncontroller:id/permission_deny_button', 'coordinates': [540, 1196], 'text': 'Don’t allow', 'direction': None, 'target_description': "the 'Don't allow' button to dismiss the notification permission request"},  # The current screen shows a notification permission dialog which is blocking the main app...
    {'step': 3, 'type': 'tap', 'resource_id': 'android:id/button1', 'coordinates': [894, 1254], 'text': 'OK', 'direction': None, 'target_description': 'the OK button'},  # The current screen shows a pop-up dialog titled 'Keep Android Open'. To proceed with the main...
    {'step': 4, 'type': 'tap', 'resource_id': None, 'coordinates': [73, 136], 'text': None, 'direction': None, 'target_description': 'Hamburger menu icon'},  # The first step of the task is to open the navigation menu. The current screen is the 'Live'...
    {'step': 5, 'type': 'tap', 'resource_id': None, 'coordinates': [367, 1305], 'text': None, 'direction': None, 'target_description': 'Trending music'},  # The user wants to find a trending music video. The current screen shows the navigation menu. The...
    {'step': 6, 'type': 'tap', 'resource_id': 'org.schabi.newpipe:id/itemRoot', 'coordinates': [540, 334], 'text': None, 'direction': None, 'target_description': "Fallin' video by ChrisBrownVEVO"},  # The task is to select a trending music video to adjust its playback speed. The current screen is...
    {'step': 7, 'type': 'tap', 'resource_id': 'org.schabi.newpipe:id/detail_thumbnail_root_layout', 'coordinates': [540, 366], 'text': None, 'direction': None, 'target_description': 'the video player area'},  # The task requires adjusting the playback speed. The first step to do this from the video screen...
    {'step': 8, 'type': 'tap', 'resource_id': 'org.schabi.newpipe:id/playbackSpeed', 'coordinates': [756, 120], 'text': None, 'direction': None, 'target_description': "playback speed button with text '1x'"},  # The user wants to change the playback speed of the video. The current screen shows the video...
    {'step': 9, 'type': 'tap', 'resource_id': 'org.schabi.newpipe:id/queueButton', 'coordinates': [876, 120], 'text': None, 'direction': None, 'target_description': 'List icon with three horizontal lines and dots, located to the right of the playback speed indicator.'},  # The goal is to change the playback speed. The detailed task summary specifies that the user...
    {'step': 10, 'type': 'tap', 'resource_id': 'org.schabi.newpipe:id/moreOptionsButton', 'coordinates': None, 'text': None, 'direction': None, 'target_description': 'the more options button (three vertical dots) in the top right of the video player'},  # The goal is to open the playback settings to adjust the video speed. The task description...
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
