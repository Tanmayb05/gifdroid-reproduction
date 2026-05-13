---
app: Audiobook Player
goal: The user wanted to hide the settings button from the main player screen.
outcome: success - The user successfully enabled the "Hide settings button" option, and the button was removed from the UI.
---

## Session Summary
The user started on the main screen of an audiobook player, swiped to change the book from "Alice's Adventures in Wonderland" to "Hamlet," and then navigated into the app's settings. They located the "Lockdown settings" and enabled the "Hide settings button" option. Upon returning to the main player screen, the settings button was successfully hidden as intended.

## Steps

### 1. Play Audiobook — 2s
- **Screen:** Main Player (Paused)
- **Action:** tap → Play button
- **Details:** The screen shows the title "Alice's Adventures in Wonderland".
- **Result:** The player controls appear, and the play button changes to a red stop button.

### 2. Change Audiobook — 8s
- **Screen:** Main Player (Playing)
- **Action:** swipe_left → Full screen
- **Details:** The user swipes left on the screen.
- **Result:** The audiobook title changes to "Hamlet" and begins playing.

### 3. Pause Audiobook — 13s
- **Screen:** Main Player (Playing)
- **Action:** tap → Stop button
- **Details:** The audiobook "Hamlet" is playing.
- **Result:** The audio stops, and the red stop button reverts to a green play button.

### 4. Open Settings — 15s
- **Screen:** Main Player (Paused)
- **Action:** tap → Settings icon (gear)
- **Details:** The settings icon is in the top-right corner.
- **Result:** Navigated to the "Settings" screen.

### 5. Navigate to Lockdown Settings — 18s
- **Screen:** Settings
- **Action:** tap → "Lockdown settings..." list item
- **Details:** The user selects the "Lockdown settings" option from the list.
- **Result:** Navigated to the "Lockdown settings" screen.

### 6. Hide Settings Button — 20s
- **Screen:** Lockdown settings
- **Action:** tap → "Hide settings button" toggle
- **Details:** The toggle is initially in the off position.
- **Result:** The "Hide settings button" toggle switches to the on (enabled) position.

### 7. Return to Player Screen — 22s
- **Screen:** Lockdown settings
- **Action:** back → Back arrow
- **Details:** The user taps the back arrow in the top-left corner.
- **Result:** The app returns to the main player screen, and the settings icon in the top-right corner is no longer visible.
- **Confidence:** 1.0

## Key Observations
- The app features a "Lockdown settings" or "kiosk mode" that allows for the removal of UI elements, such as the settings button.
- The user can switch between audiobooks on the main player screen by swiping left or right.
- The "Lockdown settings" screen contains an advanced option to "Become a Home screen app" which is dependent on kiosk mode being enabled.