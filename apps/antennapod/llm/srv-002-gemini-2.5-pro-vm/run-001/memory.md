---
app: AntennaPod
goal: To explore and modify various application settings.
outcome: success - The user successfully navigated through different settings screens, modified two options, and returned to the home screen.
---

## Session Summary
The user started on the empty home screen of the AntennaPod app. After an unsuccessful attempt to refresh, they navigated to the settings menu via the "More" tab in the bottom navigation bar. They explored the "Playback" and "Downloads" settings, toggling off the "Headphones or Bluetooth disconnect" feature and toggling on the "Delete removes from queue" feature before returning to the home screen.

## Steps

### 1. Attempt to Refresh — 4s
- **Screen:** Home
- **Action:** tap → `More options menu (three dots)`
- **Details:** The menu is in the top right corner.
- **Result:** A context menu with "Refresh" and "Configure home screen" options appeared.

### 2. Select Refresh — 4s
- **Screen:** Home
- **Action:** tap → `Refresh`
- **Details:** The user selected the "Refresh" option from the context menu.
- **Result:** A toast notification appeared at the bottom of the screen with the message: "Please wait some time before refreshing podcasts again."

### 3. Open More Menu — 9s
- **Screen:** Home
- **Action:** tap → `More`
- **Details:** The user tapped the "More" icon in the bottom navigation bar.
- **Result:** A menu sheet appeared from the bottom with options like "Episodes", "Downloads", "Settings", etc.

### 4. Navigate to Settings — 10s
- **Screen:** Home
- **Action:** tap → `Settings`
- **Details:** The user selected "Settings" from the "More" menu.
- **Result:** The app navigated to the main "Settings" screen.

### 5. Open Playback Settings — 12s
- **Screen:** Settings
- **Action:** tap → `Playback`
- **Details:** The user tapped on the "Playback" category.
- **Result:** The app navigated to the "Playback" settings screen.

### 6. Disable Headphone Disconnect Pause — 14s
- **Screen:** Playback
- **Action:** tap → `Headphones or Bluetooth disconnect toggle`
- **Details:** The toggle was initially enabled.
- **Result:** The toggle for "Pause playback when headphones or Bluetooth devices get disconnected" was disabled.

### 7. Return to Main Settings — 15s
- **Screen:** Playback
- **Action:** back → `Back arrow`
- **Details:** The user tapped the back arrow in the top left corner.
- **Result:** The app returned to the main "Settings" screen.

### 8. Open Downloads Settings — 17s
- **Screen:** Settings
- **Action:** tap → `Downloads`
- **Details:** The user tapped on the "Downloads" category.
- **Result:** The app navigated to the "Downloads" settings screen.

### 9. Enable Delete Removes from Queue — 20s
- **Screen:** Downloads
- **Action:** tap → `Delete removes from queue toggle`
- **Details:** The toggle was initially disabled.
- **Result:** The toggle for "Automatically remove an episode from the queue when it is deleted" was enabled.

### 10. Return to Home Screen — 22s
- **Screen:** Downloads
- **Action:** back → `Back arrow`
- **Details:** The user tapped the back arrow twice.
- **Result:** The app returned first to the "Settings" screen, and then to the "Home" screen.

## Key Observations
- The user attempted to refresh podcasts but was prevented by a rate-limiting message: "Please wait some time before refreshing podcasts again."
- The user modified two settings:
    - **Playback:** Disabled "Pause playback when headphones or Bluetooth devices get disconnected".
    - **Downloads:** Enabled "Automatically remove an episode from the queue when it is deleted".