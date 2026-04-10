"""Device control layer using uiautomator2."""
from __future__ import annotations

import subprocess
import time
from pathlib import Path
from typing import Optional

import PIL.Image
import uiautomator2 as u2

_ADB = "adb"


def _adb(*args: str) -> str:
    result = subprocess.run([_ADB, *args], capture_output=True, text=True, check=True)
    return result.stdout.strip()


class DeviceController:
    """Thin wrapper around uiautomator2 for device interaction."""

    def __init__(self) -> None:
        self._d: Optional[u2.Device] = None
        self._serial: Optional[str] = None

    def connect(self, serial: Optional[str] = None) -> None:
        self._serial = serial
        if serial:
            self._d = u2.connect(serial)
        else:
            self._d = u2.connect()

    @property
    def _device(self) -> u2.Device:
        if self._d is None:
            raise RuntimeError("Call connect() before using DeviceController")
        return self._d

    def install_apk(self, apk_path: Path) -> str:
        """Install APK via ADB and return the package name."""
        from gifdroid_llm.apk_utils import extract_package_name

        pkg = extract_package_name(apk_path)
        serial_args = ["-s", self._serial] if self._serial else []

        # Uninstall first to avoid INSTALL_FAILED_VERSION_DOWNGRADE
        subprocess.run([_ADB, *serial_args, "uninstall", pkg], capture_output=True, text=True)

        subprocess.run(
            [_ADB, *serial_args, "install", "-r", str(apk_path)],
            capture_output=True, text=True, check=True,
        )
        return pkg

    def launch_app(self, package: str, activity: str) -> None:
        """Launch an app by package and activity name."""
        component = f"{package}/{activity}"
        adb_args = [_ADB]
        if self._serial:
            adb_args += ["-s", self._serial]
        adb_args += ["shell", "am", "start", "-n", component]
        subprocess.run(adb_args, capture_output=True, text=True, check=True)

    def tap(self, x: int, y: int) -> None:
        self._device.click(x, y)

    def scroll(self, direction: str, x: int, y: int, distance: int = 300) -> None:
        """Scroll in a direction from a given point."""
        d = self._device
        if direction == "up":
            d.swipe(x, y, x, y - distance)
        elif direction == "down":
            d.swipe(x, y, x, y + distance)
        elif direction == "left":
            d.swipe(x, y, x - distance, y)
        elif direction == "right":
            d.swipe(x, y, x + distance, y)
        else:
            raise ValueError(f"Unknown scroll direction: {direction}")

    def type_text(self, text: str) -> None:
        self._device.send_keys(text)

    def press_key(self, key: str) -> None:
        """Press a system key: 'back', 'home', 'recent'."""
        self._device.press(key)

    def capture_screenshot(self) -> PIL.Image.Image:
        return self._device.screenshot()

    def dump_accessibility_tree(self) -> str:
        """Return the current UI hierarchy as XML string."""
        return self._device.dump_hierarchy()

    def get_current_activity(self) -> str:
        """Return the currently focused activity."""
        adb_args = [_ADB]
        if self._serial:
            adb_args += ["-s", self._serial]
        adb_args += ["shell", "dumpsys", "activity", "activities"]
        result = subprocess.run(adb_args, capture_output=True, text=True, check=True)
        for line in result.stdout.splitlines():
            if "mResumedActivity" in line or "ResumedActivity" in line:
                # Extract component name from line like:
                # mResumedActivity: ActivityRecord{... pkg/.Activity ...}
                parts = line.strip().split()
                for part in parts:
                    if "/" in part and "{" not in part and "}" not in part:
                        return part
        return ""

    def execute_action(self, action: "ExecutableAction") -> None:
        """Execute an ExecutableAction on the device."""
        from gifdroid_llm.providers import ExecutableAction as _EA  # noqa: F401

        action_type = action.type.lower()
        if action_type == "tap":
            if action.resource_id:
                el = self._device(resourceId=action.resource_id)
                if el.exists:
                    el.click()
                    return
            if action.coordinates:
                self.tap(action.coordinates[0], action.coordinates[1])
        elif action_type == "scroll":
            direction = action.direction or "down"
            x, y = (action.coordinates or [540, 960])
            self.scroll(direction, int(x), int(y))
        elif action_type == "type_text":
            if action.text:
                self.type_text(action.text)
        elif action_type in ("press_back", "back"):
            self.press_key("back")
        elif action_type in ("press_home", "home"):
            self.press_key("home")
        elif action_type in ("wait", "done"):
            pass
        else:
            pass

    def reset_app(self, package: str) -> None:
        """Return the device to a clean baseline after a run.

        Steps (in order):
        1. Force-stop the app — clears the activity stack.
        2. Clear app data — wipes shared prefs, databases, caches.
        3. Press home — ensures the launcher is in the foreground.
        """
        adb_prefix = [_ADB]
        if self._serial:
            adb_prefix += ["-s", self._serial]

        subprocess.run(adb_prefix + ["shell", "am", "force-stop", package],
                       capture_output=True, text=True)
        subprocess.run(adb_prefix + ["shell", "pm", "clear", package],
                       capture_output=True, text=True)
        self.press_key("home")

    def is_app_running(self, package: str) -> bool:
        """Return True if the package has a running process."""
        adb_args = [_ADB]
        if self._serial:
            adb_args += ["-s", self._serial]
        adb_args += ["shell", "pidof", package]
        result = subprocess.run(adb_args, capture_output=True, text=True)
        return bool(result.stdout.strip())
