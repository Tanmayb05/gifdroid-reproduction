import sys
import uiautomator2 as u2

try:
    d = u2.connect()
    screenshot = d.screenshot()
    screenshot.save('artifacts/milestone0/milestone0_screenshot.png')
    print(f"Screenshot saved: {screenshot.size}")
except Exception as e:
    print(f"ERROR: {type(e).__name__}: {e}")
    sys.exit(1)
