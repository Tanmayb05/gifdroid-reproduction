---
app: Brethap
goal: To clear all recorded session history from the application.
outcome: success - The user successfully navigated to the sessions list and cleared all entries.
---

## Session Summary
The user started on the main breathing exercise screen. After briefly starting and stopping a session, they opened the navigation menu, went to the "Sessions" screen, and used the overflow menu to select "Clear All". They confirmed the action in a dialog, successfully deleting all session history.

## Steps

### 1. Open Navigation Menu — 15s
- **Screen:** Main Breathing Screen
- **Action:** tap → Hamburger Menu Icon
- **Details:** The user taps the three-line menu icon in the bottom-left corner.
- **Result:** A navigation drawer slides out from the left, revealing menu options.
- **Confidence:** 1.0

### 2. Navigate to Sessions — 17s
- **Screen:** Main Breathing Screen (with Navigation Drawer)
- **Action:** tap → `Sessions`
- **Details:** The navigation drawer contains "Preferences", "Sessions", "Calendar", and "About Brethap".
- **Result:** The app navigates to the "Sessions" screen, which displays a list of past sessions.
- **Confidence:** 1.0

### 3. Open Sessions Menu — 19s
- **Screen:** Sessions
- **Action:** tap → Three-dot Menu Icon
- **Details:** The user taps the overflow menu icon in the top-right corner of the "Sessions" screen.
- **Result:** A context menu appears with options: "Clear All", "Backup", "Restore", "Export".
- **Confidence:** 1.0

### 4. Select Clear All — 20s
- **Screen:** Sessions
- **Action:** tap → `Clear All`
- **Details:** The user selects the "Clear All" option from the context menu.
- **Result:** A confirmation dialog appears.
- **Confidence:** 1.0

### 5. Confirm Deletion — 21s
- **Screen:** Sessions
- **Action:** tap → `Continue`
- **Details:** The dialog asks, "Are you sure you want to clear all sessions?" with "Cancel" and "Continue" buttons.
- **Result:** The dialog closes, and the list of sessions on the screen is now empty.
- **Confidence:** 1.0

## Key Observations
- The app records very short, interrupted sessions (e.g., 0:00:05, 0:00:07) if the user stops them early.
- The "Clear All" function is protected by a confirmation dialog to prevent accidental data loss.
- The sessions list displays the date, time, duration, and a count of breaths for each entry.