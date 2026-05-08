#!/usr/bin/env python3
"""
Replay script — org.adaway / None
Generated: 2026-05-08T06:48:15.035992+00:00
Video: None
Task summary: --- app: AdAway goal: The user wants to add a new domain to the whitelist. outcome: success - The domain "abc.com" was successfully added to the whitelist. --- ## Session Summary The user opened...

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
    {'step': 1, 'type': 'tap', 'resource_id': 'org.adaway:id/vpnCardView', 'coordinates': [799, 1236], 'text': None, 'direction': None, 'target_description': 'VPN based ad blocking card'},  # The user is on the initial setup screen of AdAway. To proceed to the main application and add a...
    {'step': 2, 'type': 'tap', 'resource_id': 'android:id/button1', 'coordinates': [894, 1247], 'text': 'OK', 'direction': None, 'target_description': "The 'OK' button in the 'Connection request' dialog."},  # The app is requesting permission to set up a VPN connection, which is a necessary step for it to...
    {'step': 3, 'type': 'tap', 'resource_id': 'org.adaway:id/next_button', 'coordinates': [964, 1794], 'text': 'NEXT', 'direction': None, 'target_description': "The 'NEXT' button to proceed with the setup."},  # The current screen is the initial setup wizard for AdAway. To proceed to the main dashboard where...
    {'step': 5, 'type': 'tap', 'resource_id': 'com.android.permissioncontroller:id/permission_allow_button', 'coordinates': None, 'text': 'Allow', 'direction': None, 'target_description': "the 'Allow' button for notifications"},  # The app is requesting permission to send notifications, which is part of the initial setup...
    {'step': 6, 'type': 'tap', 'resource_id': 'org.adaway:id/next_button', 'coordinates': [964, 1794], 'text': 'NEXT', 'direction': None, 'target_description': 'the NEXT button'},  # The current screen is part of the initial setup wizard for the AdAway app. To get to the main...
    {'step': 7, 'type': 'tap', 'resource_id': 'org.adaway:id/next_button', 'coordinates': [964, 1794], 'text': 'FINISH', 'direction': None, 'target_description': 'the FINISH button'},  # The current screen is the final step of the initial app setup. To proceed to the main dashboard...
    {'step': 8, 'type': 'tap', 'resource_id': 'org.adaway:id/sourcesCardView', 'coordinates': None, 'text': None, 'direction': None, 'target_description': "the card with text '3 up-to-date sources'"},  # Based on the video summary, the user navigates to the 'Your lists' section to manage the...
    {'step': 9, 'type': 'press_back', 'resource_id': None, 'coordinates': None, 'text': None, 'direction': None, 'target_description': 'Back arrow'},  # The current screen is titled "Hosts sources" and the UI elements confirm it's for managing...
    {'step': 10, 'type': 'tap', 'resource_id': 'org.adaway:id/sourcesCardView', 'coordinates': [540, 874], 'text': None, 'direction': None, 'target_description': '3 up-to-date sources'},  # Based on the video summary, the user needs to navigate to the 'Your lists' section to add a...
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
