---
app: Barcode Scanner
goal: To enable the setting that automatically returns to the scan screen after an action.
outcome: success - The user successfully located and enabled the desired setting.
---

## Session Summary
The user started on the main "Scan code" screen, opened the overflow menu, and navigated to the settings page. They scrolled down the list of options, enabled the "Go back after copying or sharing" setting, and then returned to the initial scanning screen.

## Steps

### 1. Open Overflow Menu — 2s
- **Screen:** Scan code
- **Action:** tap → `More options` (three dots icon)
- **Details:** The user is on the main scanning screen.
- **Result:** A context menu appears with several options.
- **Confidence:** 1.0

### 2. Navigate to Settings — 3s
- **Screen:** Scan code (with menu open)
- **Action:** tap → `Settings`
- **Details:** The context menu is open.
- **Result:** The "Settings" screen is displayed.
- **Confidence:** 1.0

### 3. Scroll Settings — 5s
- **Screen:** Settings
- **Action:** swipe_up → `Settings list`
- **Details:** The user scrolls down the settings list to reveal more options.
- **Result:** The "Content" section of the settings becomes visible.
- **Confidence:** 1.0

### 4. Enable 'Go Back' Setting — 11s
- **Screen:** Settings
- **Action:** tap → `Go back after copying or sharing` toggle
- **Details:** The toggle is initially in the 'off' state.
- **Result:** The toggle switches to the 'on' state, indicated by it turning green.
- **Confidence:** 1.0

### 5. Return to Scanner — 14s
- **Screen:** Settings
- **Action:** back → `Back arrow`
- **Details:** The user is finished with the settings screen.
- **Result:** The app navigates back to the "Scan code" screen.
- **Confidence:** 1.0

## Key Observations
- The user enabled the "Go back after copying or sharing" setting, which changes the app's workflow after a successful scan and action.
- The settings screen reveals a comprehensive list of features, including support for numerous barcode formats, clipboard integration, scan forwarding via URL or Bluetooth, and various UI customizations.