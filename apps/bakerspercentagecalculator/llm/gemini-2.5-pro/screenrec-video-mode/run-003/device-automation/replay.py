#!/usr/bin/env python3
"""
Replay script — com.pep1lo.bakerspercentagecalculator / None
Generated: 2026-05-13T01:20:50.917848+00:00
Video: None
Task summary: --- app: Baker's Percentage Calculator goal: The user wants to add a new recipe for a cake to the app. outcome: success — The recipe was successfully created and displayed on the main screen. ---...

Usage:
    python replay.py [--serial SERIAL] [--delay SECONDS] [--skip-install]
"""
import argparse
import subprocess
import sys
import time

import uiautomator2 as u2

APK_PATH = 'apps/bakerspercentagecalculator/apk/bakerspercentagecalculator.apk'
PACKAGE  = 'com.pep1lo.bakerspercentagecalculator'
ACTIVITY = 'com.pep1lo.bakerspercentagecalculator.MainActivity'

ACTIONS = [
    {'step': 1, 'type': 'tap', 'resource_id': 'com.pep1lo.bakerspercentagecalculator:id/fabAddRecipe', 'coordinates': None, 'text': None, 'direction': None, 'target_description': 'the plus button to add a new recipe'},  # The user wants to add a new recipe. The current screen is the empty state of the app, which...
    {'step': 2, 'type': 'type_text', 'resource_id': 'com.pep1lo.bakerspercentagecalculator:id/editTextRecipeName', 'coordinates': None, 'text': 'cake', 'direction': None, 'target_description': "the 'Recipe Name' input field"},  # Based on the task description, the user wants to create a new recipe for a 'cake'. The first step...
    {'step': 3, 'type': 'type_text', 'resource_id': 'com.pep1lo.bakerspercentagecalculator:id/editTextNotes', 'coordinates': None, 'text': 'nuts', 'direction': None, 'target_description': "Notes input field with placeholder text 'Notes (e.g., seeds, nuts)'"},  # The user has entered the recipe name. According to the task summary, the next step is to enter...
    {'step': 4, 'type': 'type_text', 'resource_id': 'com.pep1lo.bakerspercentagecalculator:id/editTextOven', 'coordinates': None, 'text': '400', 'direction': None, 'target_description': 'Oven Temp & Time input field'},  # The user has already entered the recipe name and notes. The next step in the task is to enter the...
    {'step': 5, 'type': 'tap', 'resource_id': 'com.pep1lo.bakerspercentagecalculator:id/buttonSaveRecipe', 'coordinates': [539, 1468], 'text': None, 'direction': None, 'target_description': 'Save Recipe button'},  # The user has filled out all the necessary fields for the new recipe (name, notes, oven temp). The...
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
