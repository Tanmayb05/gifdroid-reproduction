---
app: AntennaPod
goal: To find and play a podcast episode without subscribing to the podcast.
outcome: success - The user successfully found, streamed, and paused a podcast episode.
---

## Session Summary
The user launched the AntennaPod app from its Play Store page. After a brief tour of the empty navigation tabs, they navigated to the "Add podcast" screen. From there, they selected a suggested podcast, chose an episode, and began streaming it. The session ended after the user paused the playback from the full-screen player.

## Steps

### 1. Launch App — 2s
- **Screen:** Google Play Store
- **Action:** tap → `Open` button
- **Details:** The user is on the app store page for AntennaPod.
- **Result:** The AntennaPod app launches to the "Home" screen.
- **Confidence:** 1.0

### 2. Navigate to Add Podcast — 14s
- **Screen:** Subscriptions
- **Action:** tap → `+` (plus) icon
- **Details:** The user first cycles through the "Home", "Queue", "Inbox", and "Subscriptions" tabs in the bottom navigation bar before tapping the add button.
- **Result:** The "Add podcast" screen is displayed, showing a grid of suggested podcasts.
- **Confidence:** 1.0

### 3. Select Podcast — 17s
- **Screen:** Add podcast
- **Action:** tap → `BRIDGE OF LIES` podcast cover art
- **Details:** The user selects a podcast from the suggested list.
- **Result:** The app navigates to the details page for the "Bridge of Lies" podcast.
- **Confidence:** 1.0

### 4. Select Episode — 19s
- **Screen:** Add podcast (Bridge of Lies)
- **Action:** tap → `The Search` episode list item
- **Details:** The user selects the first episode from the "Episodes preview" list.
- **Result:** The app navigates to the episode detail screen for "The Search".
- **Confidence:** 1.0

### 5. Stream Episode — 21s
- **Screen:** Add podcast (The Search)
- **Action:** tap → `Stream` button
- **Details:** The episode detail screen shows a "Stream" and "Download" button.
- **Result:** The podcast begins to play, the button changes to "Pause", and a mini-player appears at the bottom of the screen.
- **Confidence:** 1.0

### 6. Expand Player — 28s
- **Screen:** Add podcast
- **Action:** tap → Mini-player at the bottom of the screen
- **Details:** The user first navigated back from the episode detail screen, then tapped the persistent mini-player.
- **Result:** The full-screen player view is displayed.
- **Confidence:** 1.0

### 7. Pause Episode — 31s
- **Screen:** Player
- **Action:** tap → `Pause` button
- **Details:** The user taps the central pause icon in the player controls.
- **Result:** The podcast playback stops, and the icon changes back to a "Play" icon.
- **Confidence:** 1.0

## Key Observations
- The user can stream an episode directly from the "Add podcast" flow without needing to subscribe to the podcast first.
- A content warning is displayed on the episode detail screen: "WARNING: This program includes discussions of suicide."
- The "Queue" screen (viewed at 0:08) contained two episodes, suggesting this was not a completely fresh install or that data was restored from a backup.
- A mini-player persists at the bottom of the screen after playback starts, allowing navigation to other parts of the app while the audio controls remain accessible.