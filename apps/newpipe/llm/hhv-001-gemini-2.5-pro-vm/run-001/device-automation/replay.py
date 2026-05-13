#!/usr/bin/env python3
"""
Replay script — org.schabi.newpipe / None
Generated: 2026-05-08T16:38:39.997565+00:00
Video: None
Task summary: --- app: NewPipe goal: To play a trending music video and adjust its playback speed. outcome: success - The user successfully navigated to a video and changed its playback speed. --- ## Session...

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
    {'step': 1, 'type': 'tap', 'resource_id': 'com.android.permissioncontroller:id/permission_deny_button', 'coordinates': [540, 1196], 'text': 'Don’t allow', 'direction': None, 'target_description': "the 'Don't allow' button in the notification permission dialog"},  # The current screen shows a system permission dialog for notifications, which is blocking the main...
    {'step': 2, 'type': 'tap', 'resource_id': 'android:id/button1', 'coordinates': [894, 1254], 'text': None, 'direction': None, 'target_description': 'OK button'},  # The current screen displays a pop-up dialog titled 'Keep Android Open'. To proceed with the task...
    {'step': 3, 'type': 'tap', 'resource_id': None, 'coordinates': [73, 136], 'text': None, 'direction': None, 'target_description': 'Hamburger menu icon'},  # The task is to find and play a trending music video. The first step in the provided task summary...
    {'step': 4, 'type': 'tap', 'resource_id': None, 'coordinates': [367, 1305], 'text': None, 'direction': None, 'target_description': 'Trending music'},  # The task is to play a trending music video. The navigation menu is open, so the next step is to...
    {'step': 5, 'type': 'tap', 'resource_id': 'org.schabi.newpipe:id/itemRoot', 'coordinates': [540, 334], 'text': None, 'direction': None, 'target_description': "Video titled 'NACHO ESTRELLA X JEY ONE X ALOFOKE MUSIC X DIANA LA MISS - HI...'"},  # The current screen shows a list of trending music videos. To proceed with the task of playing a...
    {'step': 6, 'type': 'tap', 'resource_id': 'org.schabi.newpipe:id/detail_thumbnail_root_layout', 'coordinates': [540, 366], 'text': None, 'direction': None, 'target_description': 'the video player area'},  # The user needs to adjust the playback speed. To do this, the player controls must be visible....
    {'step': 7, 'type': 'tap', 'resource_id': 'org.schabi.newpipe:id/playbackSpeed', 'coordinates': [756, 120], 'text': '1x', 'direction': None, 'target_description': 'Playback Speed Indicator (1x)'},  # The task is to adjust the playback speed. The '1x' button in the top control bar of the video...
    {'step': 8, 'type': 'tap', 'resource_id': 'org.schabi.newpipe:id/playbackSpeed', 'coordinates': [756, 120], 'text': '1x', 'direction': None, 'target_description': "the playback speed indicator, currently showing '1x'"},  # The task is to adjust the playback speed. The current screen is the video player. The next step,...
    {'step': 9, 'type': 'tap', 'resource_id': 'org.schabi.newpipe:id/playbackSpeed', 'coordinates': [756, 120], 'text': None, 'direction': None, 'target_description': "Playback speed indicator with text '1x'"},  # The task is to adjust the playback speed. According to the video summary (Step 4) and the UI, the...
    {'step': 10, 'type': 'tap', 'resource_id': 'android:id/button3', 'coordinates': [188, 1289], 'text': None, 'direction': None, 'target_description': 'the RESET button'},  # The user has re-opened the playback speed controls. According to the session summary (Step 8),...
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
