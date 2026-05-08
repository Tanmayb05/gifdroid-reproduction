---
app: Barcode Scanner
goal: To disable the setting that automatically goes back after copying or sharing a scanned code.
outcome: success - The user successfully located and disabled the target setting.
---

## Session Summary
The user started on the main scanning screen of a barcode app. They opened the overflow menu, navigated to the settings page, scrolled through the options, and successfully disabled the "Go back after copying or sharing" feature.

## Steps

### 1. Open Overflow Menu — 0s
- **Screen:** Main Scanner
- **Action:** tap → `menu icon` (three dots)
- **Details:** The menu icon is located in the top left corner of the screen.
- **Result:** A dropdown menu appeared with several options.
- **Confidence:** 1.0

### 2. Navigate to Settings — 2s
- **Screen:** Main Scanner (with menu open)
- **Action:** tap → `Print settings`
- **Details:** Menu options visible: "Switch camera", "Scan continuously", "Restrict format", "Print settings", "Info", "Profile: Default".
- **Result:** The application navigated to the main "Settings" screen.
- **Confidence:** 1.0

### 3. Scroll Settings List — 3s
- **Screen:** Settings
- **Action:** swipe_up → `settings list`
- **Details:** The user scrolled down the list of available settings.
- **Result:** The view scrolled, revealing more settings options further down the page.
- **Confidence:** 1.0

### 4. Disable "Go Back" Setting — 10s
- **Screen:** Settings
- **Action:** tap → `toggle switch` for "Go back after copying or sharing"
- **Details:** The toggle switch was active (green) before the tap.
- **Result:** The toggle switch for the "Go back after copying or sharing" setting was turned off.
- **Confidence:** 1.0

## Key Observations
- The menu item tapped was labeled "Print settings", but it led to a general "Settings" page, which could be a confusing user experience.
- The user specifically disabled the "Go back after copying or sharing" feature, indicating a desire to remain on the result screen after performing an action on a scanned code.