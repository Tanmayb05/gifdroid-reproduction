import random
import time
import json
import os
import sys
import hashlib
import subprocess
import xml.etree.ElementTree as ET

APPS = {
    "AdAway":       "org.adaway",
    "AntennaPod":   "de.danoeh.antennapod",
    "DeadHash":     "com.codedead.deadhash",
    "HomeMedkit":   "ru.application.homemedkit",
    "Jigsaw":       "io.gitlab.derjosef.jigsaw",
    "LuxAlarm":     "com.dsalmun.luxalarm",
    "Pomodorot":    "app.pomodorot",
    "PortAuthority":"com.aaronjwood.portauthority",
    "SimpleNotes":  "dev.dettmer.simplenotes",
    "WifiAnalyzer": "com.vrem.wifianalyzer",
}

if len(sys.argv) < 2:
    print(f"Usage: python3 monkey_utg.py <AppName>")
    print(f"Available apps: {', '.join(APPS)}")
    sys.exit(1)

APP_NAME = sys.argv[1]
if APP_NAME not in APPS:
    print(f"Unknown app '{APP_NAME}'. Available: {', '.join(APPS)}")
    sys.exit(1)

PACKAGE = APPS[APP_NAME]
ADB = os.path.expanduser("~/Library/Android/sdk/platform-tools/adb")

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), f"app_{APP_NAME}")
SCREENSHOTS_DIR = os.path.join(OUTPUT_DIR, "screenshots")
UTG_PATH = os.path.join(OUTPUT_DIR, "utg.json")

utg = {"nodes": {}, "edges": []}
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)


def adb(*args, check=True):
    result = subprocess.run([ADB] + list(args), capture_output=True, text=True)
    if check and result.returncode != 0:
        raise RuntimeError(f"adb {args} failed: {result.stderr}")
    return result.stdout


def launch_app():
    adb("shell", "monkey", "-p", PACKAGE, "-c", "android.intent.category.LAUNCHER", "1")
    time.sleep(2)


def get_current_activity():
    out = adb("shell", "dumpsys", "activity", "activities")
    for line in out.splitlines():
        if "mResumedActivity" in line or "mCurrentFocus" in line:
            parts = line.strip().split()
            for p in parts:
                if "/" in p and p.startswith(("org.", "com.", "net.", "io.", "android.")):
                    return p
    return "unknown"


def is_in_app():
    out = adb("shell", "dumpsys", "activity", "activities")
    for line in out.splitlines():
        if "mResumedActivity" in line or "mCurrentFocus" in line:
            if PACKAGE in line:
                return True
    return False


def dump_xml():
    """Dump UI hierarchy via adb uiautomator dump."""
    adb("shell", "uiautomator", "dump", "/sdcard/uidump.xml")
    xml = adb("shell", "cat", "/sdcard/uidump.xml")
    return xml


def get_clickable_elements(xml):
    """Parse XML and return list of clickable element dicts."""
    elements = []
    try:
        root = ET.fromstring(xml)
        for node in root.iter("node"):
            if node.attrib.get("clickable") == "true" and node.attrib.get("enabled") == "true":
                bounds_str = node.attrib.get("bounds", "")
                elements.append({
                    "text": node.attrib.get("text", ""),
                    "resourceId": node.attrib.get("resource-id", ""),
                    "className": node.attrib.get("class", ""),
                    "bounds": bounds_str,
                    "contentDesc": node.attrib.get("content-desc", ""),
                })
    except ET.ParseError as e:
        print(f"  XML parse error: {e}")
    return elements


def parse_bounds(bounds_str):
    """Parse '[x1,y1][x2,y2]' -> center (cx, cy)."""
    try:
        parts = bounds_str.replace("][", ",").strip("[]").split(",")
        x1, y1, x2, y2 = int(parts[0]), int(parts[1]), int(parts[2]), int(parts[3])
        return (x1 + x2) // 2, (y1 + y2) // 2
    except Exception:
        return None


def tap(cx, cy):
    adb("shell", "input", "tap", str(cx), str(cy))


def get_screen_id(activity, xml):
    raw = activity + xml
    screen_hash = hashlib.md5(raw.encode()).hexdigest()[:8]
    safe_activity = activity.replace("/", "_").replace(":", "_")
    return f"{safe_activity}_{screen_hash}"


def take_screenshot(path):
    adb("shell", "screencap", "-p", "/sdcard/screen_tmp.png")
    adb("pull", "/sdcard/screen_tmp.png", path)
    adb("shell", "rm", "/sdcard/screen_tmp.png")


def capture_state(screen_id, activity, xml):
    if screen_id not in utg["nodes"]:
        screenshot_path = os.path.join(SCREENSHOTS_DIR, f"{screen_id}.png")
        take_screenshot(screenshot_path)
        utg["nodes"][screen_id] = {
            "activity": activity,
            "screenshot": screenshot_path,
        }
        print(f"  [NEW SCREEN] {screen_id}")
        return True
    return False


def save_utg():
    with open(UTG_PATH, "w") as f:
        json.dump(utg, f, indent=4)


print(f"Launching {PACKAGE}...")
launch_app()
print("Starting UTG explorer (adb-based). Press Ctrl+C to stop.\n")

MAX_STEPS = 200
TIMEOUT_SECS = 5 * 60  # 5 minutes
step = 0
start_time = time.time()

while step < MAX_STEPS and (time.time() - start_time) < TIMEOUT_SECS:
    try:
        step += 1
        print(f"[step {step}/{MAX_STEPS}]", end=" ")

        if not is_in_app():
            print(f"Left {APP_NAME}, relaunching...")
            launch_app()
            continue

        src_activity = get_current_activity()
        src_xml = dump_xml()
        src_id = get_screen_id(src_activity, src_xml)
        capture_state(src_id, src_activity, src_xml)

        elements = get_clickable_elements(src_xml)
        if not elements:
            print("No clickable elements, pressing back.")
            adb("shell", "input", "keyevent", "4")
            time.sleep(1)
            continue

        el = random.choice(elements)
        label = el["text"] or el["contentDesc"] or el["resourceId"] or el["className"]
        print(f"Clicking: {label!r}  bounds={el['bounds']}")

        center = parse_bounds(el["bounds"])
        if center is None:
            print("  (bad bounds, skipping)")
            continue

        tap(*center)
        time.sleep(1.5)

        dst_activity = get_current_activity()
        dst_xml = dump_xml()
        dst_id = get_screen_id(dst_activity, dst_xml)
        capture_state(dst_id, dst_activity, dst_xml)

        edge = {"src": src_id, "dst": dst_id, "action": el}
        if edge not in utg["edges"]:
            utg["edges"].append(edge)

        save_utg()

    except KeyboardInterrupt:
        print("\nStopped by user.")
        break
    except Exception as e:
        print(f"  Error: {e}, pressing back.")
        try:
            adb("shell", "input", "keyevent", "4")
        except Exception:
            pass
        time.sleep(1)

elapsed = time.time() - start_time
print(f"\nDone after {elapsed:.0f}s. {len(utg['nodes'])} screens, {len(utg['edges'])} edges.")
print(f"UTG saved to {UTG_PATH}")
print(f"Screenshots in {SCREENSHOTS_DIR}")
save_utg()
