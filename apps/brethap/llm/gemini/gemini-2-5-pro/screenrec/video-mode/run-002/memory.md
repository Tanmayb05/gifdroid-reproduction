---
app: Brethap
goal: The user wants to clear the history of all recorded breathing sessions.
outcome: success - The user successfully navigated to the sessions list and cleared all entries.
---

## Session Summary
The user started and quickly stopped two short breathing exercises, which were recorded in the app's history. They then navigated to the "Sessions" screen via the side menu, opened the options, and used the "Clear All" function to successfully delete the session records.

## Steps

### 1. Start and Stop First Session — 0s
- **Screen:** Main
- **Action:** tap → play button
- **Details:** The screen shows "Press Start" and a timer at "0:02:00".
- **Result:** The breathing exercise begins, showing "Inhale" and a countdown timer. The user then immediately taps the stop button, returning to the main screen. A message "0:00:05 Session, 0 Breaths" appears at the bottom.

### 2. Start and Stop Second Session — 8s
- **Screen:** Main
- **Action:** tap → play button
- **Details:** The user starts another session.
- **Result:** The breathing exercise begins. The user taps the stop button after a few seconds, returning to the main screen. A message "0:00:06 Session, 0 Breaths" appears at the bottom.

### 3. Open Navigation Menu — 16s
- **Screen:** Main
- **Action:** open_menu → hamburger menu icon
- **Details:** The icon is in the top-left corner.
- **Result:** A navigation drawer slides out from the left, showing options like "Preferences", "Sessions", and "Calendar".

### 4. Navigate to Sessions — 18s
- **Screen:** Main (with Navigation Drawer)
- **Action:** tap → "Sessions" menu item
- **Details:** The user taps the second item in the navigation menu.
- **Result:** The app navigates to the "Sessions" screen, which lists the two previously recorded sessions.

### 5. Open Options Menu — 20s
- **Screen:** Sessions
- **Action:** open_menu → three-dot menu icon
- **Details:** The icon is in the top-right corner of the app bar.
- **Result:** A dropdown menu appears with "Clear All", "Backup", "Restore", and "Export".

### 6. Select Clear All — 21s
- **Screen:** Sessions
- **Action:** tap → "Clear All" menu item
- **Details:** The user selects the first option from the dropdown menu.
- **Result:** A confirmation dialog appears, asking "Are you sure you want to clear all sessions?".

### 7. Confirm Deletion — 22s
- **Screen:** Sessions (with Dialog)
- **Action:** tap → "Continue" button
- **Details:** The user confirms the action in the dialog.
- **Result:** The dialog closes, the list of sessions becomes empty, and a "Sessions cleared" toast message is displayed at the bottom of the screen.

## Key Observations
- The session log displays a future date for the recorded sessions ("2026-05-01"), which could indicate a bug or a misconfigured device clock.
- The app records sessions as short as 5-6 seconds, even if no full breaths are completed (as indicated by "0 Breaths").
- The "Clear All" function includes a confirmation dialog, which is good UX practice to prevent accidental data loss.