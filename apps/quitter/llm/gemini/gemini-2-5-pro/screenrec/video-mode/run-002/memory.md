---
app: Quitter
goal: The user wanted to test the journal feature and then disable it via the settings.
outcome: success — The user successfully disabled the journal tab.
---

## Session Summary
The user started on the "Quitter" home screen, which lists various addictions to track. They swiped to the "Journal" tab, made a brief entry, and then navigated to the "Settings" screen. In settings, they toggled off the "Show journal" option and returned to the main screen, confirming the "Journal" tab was no longer visible in the bottom navigation.

## Steps

### 1. Navigate to Journal — 3s
- **Screen:** Quitter Home
- **Action:** swipe_left → `Journal` tab
- **Details:** The user swiped from the "Quitter" tab to the "Journal" tab.
- **Result:** The "Journal" screen is displayed, showing a calendar for May 2026 and a text entry field.
- **Confidence:** 1.0

### 2. Add Journal Entry — 11s
- **Screen:** Journal
- **Action:** type → `How was your day?` text field
- **Details:** The user typed "it was good" into the journal entry field for Friday, May 1, 2026.
- **Result:** The text "it was good" appears in the input field.
- **Confidence:** 1.0

### 3. Navigate to Settings — 12s
- **Screen:** Journal
- **Action:** swipe_left → `Settings` tab
- **Details:** The user swiped from the "Journal" tab to the "Settings" tab.
- **Result:** The "Settings" screen is displayed.
- **Confidence:** 1.0

### 4. Disable Journal Tab — 15s
- **Screen:** Settings
- **Action:** tap → `Show journal` toggle
- **Details:** The toggle switch for "Enable the journal tab for logging your thoughts" was turned off.
- **Result:** The toggle becomes inactive (greyed out). The "Journal" tab immediately disappears from the bottom navigation bar.
- **Confidence:** 1.0

### 5. Return to Home Screen — 16s
- **Screen:** Settings
- **Action:** swipe_right → `Quitter` tab
- **Details:** The user swiped from the "Settings" tab back to the main "Quitter" screen.
- **Result:** The "Quitter" home screen is displayed. The bottom navigation bar now only shows "Quitter" and "Settings".
- **Confidence:** 1.0

## Key Observations
- The app allows users to enable or disable the "Journal" tab from the settings menu.
- The navigation bar updates in real-time to reflect the change in the "Show journal" setting.
- The app supports both tapping on the bottom navigation icons and swiping left/right to switch between the main tabs.
- The journal entry for "Friday, May 1, 2026" was "it was good".