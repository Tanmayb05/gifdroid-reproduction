#!/usr/bin/env python3
"""
Replay script — org.adaway / None
Generated: 2026-05-08T06:54:56.361117+00:00
Video: None
Task summary: --- app: AdAway goal: To add a specific hostname to the ad blocker's whitelist (allowed list). outcome: success - The user successfully added "abc.com" to the allowed list and applied the new...

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
    {'step': 1, 'type': 'tap', 'resource_id': 'org.adaway:id/vpnCardView', 'coordinates': [799, 1236], 'text': None, 'direction': None, 'target_description': 'VPN based ad blocking card'},  # The video summary indicates that the user enabled the ad blocker and that the configuration was...
    {'step': 2, 'type': 'tap', 'resource_id': 'android:id/button1', 'coordinates': [894, 1247], 'text': 'OK', 'direction': None, 'target_description': 'the OK button to accept the VPN connection request'},  # The AdAway app requires setting up a VPN to function as an ad blocker. To proceed with the task...
    {'step': 3, 'type': 'tap', 'resource_id': 'org.adaway:id/next_button', 'coordinates': [964, 1794], 'text': None, 'direction': None, 'target_description': 'the NEXT button'},  # The current screen is the first page of a multi-step setup wizard, as indicated by the pagination...
    {'step': 4, 'type': 'tap', 'resource_id': None, 'coordinates': [972, 1794], 'text': None, 'direction': None, 'target_description': 'Next button'},  # The current screen is part of a multi-page setup wizard, as indicated by the page dots at the...
    {'step': 5, 'type': 'tap', 'resource_id': 'com.android.permissioncontroller:id/permission_allow_button', 'coordinates': None, 'text': 'Allow', 'direction': None, 'target_description': "the 'Allow' button to grant notification permissions"},  # The app is requesting permission to send notifications. To proceed with the main task of...
    {'step': 6, 'type': 'tap', 'resource_id': 'org.adaway:id/next_button', 'coordinates': None, 'text': None, 'direction': None, 'target_description': "the 'NEXT' button"},  # The current screen is part of the initial setup wizard for the AdAway app. To proceed to the main...
    {'step': 7, 'type': 'tap', 'resource_id': 'org.adaway:id/next_button', 'coordinates': [964, 1794], 'text': 'FINISH', 'direction': None, 'target_description': 'the FINISH button'},  # The current screen is the final step of the initial setup for the AdAway app. To proceed to the...
    {'step': 8, 'type': 'tap', 'resource_id': None, 'coordinates': [73, 1783], 'text': None, 'direction': None, 'target_description': 'hamburger menu icon'},  # The task is to add a hostname to the allowed list. According to the session summary, the next...
    {'step': 9, 'type': 'tap', 'resource_id': 'org.adaway:id/allowedHostCardView', 'coordinates': [540, 511], 'text': None, 'direction': None, 'target_description': "the 'Allowed' card which shows a count of 0"},  # The goal is to add a hostname to the allowed list. The main screen has a card showing the number...
    {'step': 10, 'type': 'tap', 'resource_id': 'org.adaway:id/lists_add', 'coordinates': [964, 1594], 'text': None, 'direction': None, 'target_description': 'the red circular plus button to add a new item to the list'},  # The current screen is the 'Allowed' list. To add a new hostname, I need to tap the floating...
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
