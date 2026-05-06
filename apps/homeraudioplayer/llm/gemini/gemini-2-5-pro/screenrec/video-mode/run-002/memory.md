---
app: Audiobook Player
goal: The user wants to hide the settings button from the main player screen.
outcome: success - The user successfully navigated to the lockdown settings and enabled the "Hide settings button" option.
---

## Session Summary
The user started on the main player screen for an audiobook titled "Alice's Adventures in Wonderland." After briefly interacting with the playback controls and swiping to another book, "Hamlet," the user navigated into the app's settings. They located the "Lockdown settings," enabled the "Hide settings button" toggle, and returned to the main player screen to confirm the button was gone.

## Steps

### 1. Play Audiobook — 0s
- **Screen:** Main Player
- **Action:** tap → "Play" button
- **Details:** The screen shows the title "Alice's Adventures in Wonderland".
- **Result:** The play button changes to a stop button, and playback controls (volume, skip, rewind) appear.
- **Confidence:** 1.0

### 2. Stop Audiobook — 2s
- **Screen:** Main Player (Playing)
- **Action:** tap → "Stop" button
- **Details:** The large button is now a red circle with a white square.
- **Result:** The playback controls disappear, and the button reverts to a green play icon.
- **Confidence:** 1.0

### 3. Change Audiobook — 8s
- **Screen:** Main Player
- **Action:** swipe_left → "Alice's Adventures in Wonderland" title area
- **Result:** The title on the screen changes to "Hamlet".
- **Confidence:** 1.0

### 4. Play "Hamlet" — 9s
- **Screen:** Main Player
- **Action:** tap → "Play" button
- **Details:** The screen shows the title "Hamlet".
- **Result:** Playback controls appear, and audio for "Hamlet" begins.
- **Confidence:** 1.0

### 5. Stop "Hamlet" — 13s
- **Screen:** Main Player (Playing)
- **Action:** tap → "Stop" button
- **Result:** The playback controls disappear, and the button reverts to a green play icon.
- **Confidence:** 1.0

### 6. Open Settings — 15s
- **Screen:** Main Player
- **Action:** tap → "Settings" icon (gear)
- **Result:** The "Settings" screen is displayed.
- **Confidence:** 1.0

### 7. Open Lockdown Settings — 18s
- **Screen:** Settings
- **Action:** tap → "Lockdown settings..."
- **Result:** The "Lockdown settings" screen is displayed.
- **Confidence:** 1.0

### 8. Hide Settings Button — 20s
- **Screen:** Lockdown settings
- **Action:** tap → "Hide settings button" toggle
- **Result:** The toggle switch moves to the "on" position.
- **Confidence:** 1.0

### 9. Return to Settings Screen — 21s
- **Screen:** Lockdown settings
- **Action:** back → "Back" arrow
- **Result:** The app returns to the "Settings" screen. The settings icon in the top-right corner is now gone.
- **Confidence:** 1.0

### 10. Return to Main Player — 22s
- **Screen:** Settings
- **Action:** back → "Back" arrow
- **Result:** The app returns to the main player screen for "Hamlet". The settings icon in the top-right corner is no longer visible.
- **Confidence:** 1.0

## Key Observations
- The application features a "Lockdown settings" (kiosk mode) which allows for UI customization.
- One of the lockdown options is to hide the settings button, which takes effect immediately upon leaving the "Lockdown settings" screen.
- The settings icon disappears from the header of the "Settings" screen itself after the option is enabled, even before returning to the main player.
- The user can switch between audiobooks by swiping left or right on the main player screen.