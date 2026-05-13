---
app: Brethap
goal: The user wants to record a few short breathing sessions and then clear the session history.
outcome: success - The user successfully recorded and then cleared all session data.
---

## Session Summary
The user started on the main screen of the Brethap app and initiated two very short breathing sessions. They then navigated to the "Sessions" screen via the side menu, viewed the recorded sessions, and used the "Clear All" option from the overflow menu to successfully delete the history, confirming the action in a dialog.

## Steps

### 1. Start Session 1 — 2s
- **Screen:** Main Screen
- **Action:** tap → Play button
- **Details:** The screen was displaying "Press Start" and a timer set to "0:02:00".
- **Result:** The breathing exercise started, displaying "Inhale" and a countdown timer.

### 2. Stop Session 1 — 7s
- **Screen:** Breathing Session
- **Action:** tap → Stop button
- **Details:** The session was in the "Exhale" phase.
- **Result:** The session ended and the app returned to the main screen. A message "0:00:05 Session, 0 Breaths" appeared at the bottom.

### 3. Start Session 2 — 9s
- **Screen:** Main Screen
- **Action:** tap → Play button
- **Details:** The user starts a new session immediately after the first one.
- **Result:** A new breathing exercise started, displaying "Inhale" and a countdown timer.

### 4. Stop Session 2 — 15s
- **Screen:** Breathing Session
- **Action:** tap → Stop button
- **Details:** The session was in the "Exhale" phase.
- **Result:** The session ended and the app returned to the main screen. A message "0:00:06 Session, 0 Breaths" appeared at the bottom.

### 5. Open Navigation Menu — 16s
- **Screen:** Main Screen
- **Action:** tap → Hamburger menu icon
- **Details:** The user opens the side navigation drawer.
- **Result:** The navigation drawer opened, showing options: Preferences, Sessions, Calendar, About Brethap.

### 6. Navigate to Sessions — 18s
- **Screen:** Navigation Drawer
- **Action:** tap → Sessions
- **Details:** The user selects the "Sessions" list item.
- **Result:** The app navigated to the "Sessions" screen, displaying a list of two previously recorded sessions.

### 7. Open Sessions Menu — 20s
- **Screen:** Sessions
- **Action:** tap → Three-dot menu icon
- **Details:** The user opens the overflow menu on the Sessions screen.
- **Result:** A dropdown menu appeared with options: Clear All, Backup, Restore, Export.

### 8. Select Clear All — 21s
- **Screen:** Sessions
- **Action:** tap → Clear All
- **Details:** The user selects the "Clear All" option from the menu.
- **Result:** A confirmation dialog appeared asking "Are you sure you want to clear all sessions?".

### 9. Confirm Deletion — 22s
- **Screen:** Clear All Dialog
- **Action:** tap → Continue
- **Details:** The user confirms the deletion action.
- **Result:** The dialog closed, the session list became empty, and a "Sessions cleared" toast message appeared.

## Key Observations
- The app records sessions even if they are very short and no full breaths are completed (the UI shows "0 Breaths").
- The session log displays a future date of "2026-05-01", which could indicate a bug or a misconfigured device/emulator date.