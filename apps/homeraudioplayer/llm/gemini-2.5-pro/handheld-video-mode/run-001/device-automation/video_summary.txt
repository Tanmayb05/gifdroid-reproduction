---
app: Audiobook Player
goal: To explore the app's settings and enable the "kiosk mode" feature while an audiobook is playing.
outcome: success - The user successfully enabled the lockdown setting and returned to the player.
---

## Session Summary
The user started on the book selection screen, swiped from "Alice's Adventures in Wonderland" to "Hamlet," and began playback. They then navigated into the app's settings, located and enabled the "Application lockdown (kiosk mode)," and returned to the player screen. Finally, they stopped the audiobook, which returned them to the book selection screen.

## Steps

### 1. Select Book — 1s
- **Screen:** Book Selection
- **Action:** `swipe_left` → `Alice's Adventures in Wonderland` title
- **Details:** The title on the screen changes from "Alice's Adventures in Wonderland" to "Hamlet".
- **Result:** The selected book is now "Hamlet".
- **Confidence:** 1.0

### 2. Start Playback — 2s
- **Screen:** Book Selection
- **Action:** `tap` → `Play button`
- **Details:** The large green play button is tapped.
- **Result:** The app transitions to the Player screen, and audio playback for "Hamlet" begins.
- **Confidence:** 1.0

### 3. Rewind Audio — 6s
- **Screen:** Player
- **Action:** `tap` → `Rewind 10s button`
- **Details:** The user taps the button to rewind the audio by 10 seconds.
- **Result:** The audio playback jumps back 10 seconds.
- **Confidence:** 1.0

### 4. Rewind Audio Again — 8s
- **Screen:** Player
- **Action:** `tap` → `Rewind 10s button`
- **Details:** The user taps the rewind 10s button a second time.
- **Result:** The audio playback jumps back another 10 seconds.
- **Confidence:** 1.0

### 5. Open Settings — 12s
- **Screen:** Player
- **Action:** `tap` → `Settings (gear) icon`
- **Details:** The user taps the gear icon in the top left corner.
- **Result:** The app navigates to the main "Settings" screen. The audio continues to play in the background.
- **Confidence:** 1.0

### 6. Open Lockdown Settings — 14s
- **Screen:** Settings
- **Action:** `tap` → `Lockdown settings`
- **Details:** The user taps the "Lockdown settings" menu item.
- **Result:** The app navigates to the "Lockdown settings" screen.
- **Confidence:** 1.0

### 7. Enable Kiosk Mode — 17s
- **Screen:** Lockdown settings
- **Action:** `tap` → `Application lockdown (kiosk mode) toggle`
- **Details:** The user taps the toggle switch, which turns from off to on (green).
- **Result:** The kiosk mode setting is enabled.
- **Confidence:** 1.0

### 8. Navigate Back to Player — 18s
- **Screen:** Lockdown settings
- **Action:** `back` → `Back arrow`
- **Details:** The user taps the back arrow twice, first returning to the main Settings screen, then to the Player screen.
- **Result:** The user is returned to the Player screen, with audio still playing.
- **Confidence:** 1.0

### 9. Stop Playback — 21s
- **Screen:** Player
- **Action:** `tap` → `Stop button`
- **Details:** The user taps the large orange stop button.
- **Result:** Audio playback stops, and the app returns to the "Hamlet" book selection screen.
- **Confidence:** 1.0

## Key Observations
- The app contains a "Lockdown settings (kiosk mode)" feature, which can be enabled to restrict the device to only running the app.
- Audio playback continues in the background while navigating through the app's settings menus.
- The player interface includes controls for play/stop, volume, and rewinding by 10 or 30 seconds.
- Swiping left or right on the initial screen changes the selected audiobook.