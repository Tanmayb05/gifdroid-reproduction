import time
import json
import os

# Human-readable action parser and execution script for Android ADB automation

def _load_app_launch_commands(project_root=None):
    """
    Load app launch commands from JSON file.

    Args:
        project_root: Optional path to project root. If None, tries to infer from __file__.

    Returns:
        Dict mapping app_name to {'package': str, 'launch_command': str}
    """
    if project_root is None:
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    commands_file = os.path.join(project_root, "src_ViBR", "input", "app_launch_commands.json")
    if os.path.exists(commands_file):
        with open(commands_file, 'r') as f:
            return json.load(f)
    return {}


def execute_actions(device, actions, app_launch_commands=None):
    """
    Execute a list of UI actions on an Android device via ADB.

    Args:
        device: An instance of ADBDeviceController
        actions: List of action dicts, each with:
            - 'action': str (e.g. 'tap', 'swipe', 'input_text', 'home', 'app_open', ...)
            - plus relevant keys (e.g. 'position', 'text', 'from', 'to', 'duration', 'app_name').
        app_launch_commands: Optional dict of app launch commands (loaded from JSON if not provided).

    Unknown actions are ignored with a warning.
    """
    if app_launch_commands is None:
        app_launch_commands = _load_app_launch_commands()
    for i, action in enumerate(actions):
        print(f"[{i+1}] {action.get('description', 'Executing action')} -> {action['action']}")

        if action["action"] == "tap":
            x, y = action["position"]
            device.click(x, y)

        elif action["action"] == "double_tap":
            x, y = action["position"]
            device.click(x, y)
            time.sleep(0.1)
            device.click(x, y)

        elif action["action"] == "long_press":
            x, y = action["position"]
            duration = action.get("duration", 1000)
            device.long_click(x, y, duration)

        elif action["action"] == "swipe":
            x1, y1 = action["from"]
            x2, y2 = action["to"]
            duration = action.get("duration", 500)
            device.swipe(x1, y1, x2, y2, duration)

        elif action["action"] == "input_text":
            text = action["text"]
            device.input_text(text)

        elif action["action"] == "back":
            device.back()

        elif action["action"] == "home":
            # 'input keyevent 3' is the Android HOME key
            device.shell("input keyevent 3")

        elif action["action"] == "app_open":
            app_name = action.get("app_name")
            if not app_name:
                print(f"❌ app_open action requires 'app_name' key")
                continue

            if app_name not in app_launch_commands:
                print(f"❌ app '{app_name}' not found in launch commands")
                continue

            launch_cmd = app_launch_commands[app_name]["launch_command"]
            print(f"🚀 Opening app: {app_name} with command: {launch_cmd}")
            device.shell(launch_cmd)

        elif action["action"] == "wait" or action["action"] == "no action":
            # 'wait' and 'no action' both just pause for the given duration (ms)
            duration = action.get("duration", 1000)
            time.sleep(duration / 1000.0)

        else:
            print(f"Unknown action type: {action['action']}")
