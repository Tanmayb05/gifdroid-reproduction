---
app: AntennaPod
goal: The user wants to find and play a podcast episode without subscribing.
outcome: success - The user successfully located and played an episode from a suggested podcast.
---

## Session Summary
The user launched the AntennaPod app from its Play Store page. After a brief exploration of the main navigation tabs, they proceeded to the "Add podcast" screen. They selected a suggested podcast, chose an episode, and successfully started streaming it. The session ended after they paused the playback from the full player screen.

## Steps

### 1. Launch App — 2s
- **Screen:** Google Play Store
- **Action:** tap → Open button
- **Details:** The user is on the app listing page for "AntennaPod".
- **Result:** The AntennaPod app launched and displayed the "Home" screen.
- **Confidence:** 1.0

### 2. Explore Navigation — 6s
- **Screen:** Home
- **Action:** tap → Queue tab
- **Details:** The Home screen shows a "Welcome to AntennaPod!" message.
- **Result:** The app navigated to the "Queue" screen.
- **Confidence:** 1.0

### 3. Explore Navigation — 10s
- **Screen:** Queue
- **Action:** tap → Inbox tab
- **Details:** The Queue screen is empty.
- **Result:** The app navigated to the "Inbox" screen.
- **Confidence:** 1.0

### 4. Explore Navigation — 11s
- **Screen:** Inbox
- **Action:** tap → Subscriptions tab
- **Details:** The Inbox screen shows "No episodes in the Inbox".
- **Result:** The app navigated to the "Subscriptions" screen.
- **Confidence:** 1.0

### 5. Open Add Podcast Screen — 14s
- **Screen:** Subscriptions
- **Action:** tap → `+` (plus) icon
- **Details:** The Subscriptions screen shows "No subscriptions".
- **Result:** The "Add podcast" screen appeared.
- **Confidence:** 1.0

### 6. Select Podcast — 16s
- **Screen:** Add podcast
- **Action:** tap → "Bridge of Lies" podcast cover
- **Details:** The user selected a podcast from the "Suggestions by Apple Podcasts" grid.
- **Result:** The app navigated to the details page for the "Bridge of Lies" podcast.
- **Confidence:** 1.0

### 7. Select Episode — 19s
- **Screen:** Add podcast (Bridge of Lies)
- **Action:** tap → "The Search" episode
- **Details:** The user tapped on the episode from the "Episodes preview" list.
- **Result:** The app navigated to the episode details screen for "The Search".
- **Confidence:** 1.0

### 8. Stream Episode — 21s
- **Screen:** Add podcast (The Search)
- **Action:** tap → Stream button
- **Details:** The button has a play icon and the text "Stream".
- **Result:** The podcast audio began playing, and the button changed to "Pause". A mini-player appeared at the bottom of the screen.
- **Confidence:** 1.0

### 9. Navigate Back — 25s
- **Screen:** Add podcast (The Search)
- **Action:** tap → Back arrow
- **Details:** The podcast is playing in the background.
- **Result:** The app returned to the main "Add podcast" screen, with the mini-player still visible and active at the bottom.
- **Confidence:** 1.0

### 10. Open Full Player — 28s
- **Screen:** Add podcast
- **Action:** tap → Mini-player
- **Details:** The mini-player at the bottom shows the currently playing episode, "The Search".
- **Result:** The full-screen player view was displayed.
- **Confidence:** 1.0

### 11. Pause Playback — 31s
- **Screen:** Player
- **Action:** tap → Pause button
- **Details:** The user tapped the central pause button in the player controls.
- **Result:** The podcast audio stopped, and the icon changed back to a play button.
- **Confidence:** 1.0

## Key Observations
- The app allows users to discover and stream individual podcast episodes without requiring a subscription to the podcast itself.
- When playback begins, a persistent mini-player appears at the bottom of the UI, allowing navigation to other screens while the audio continues.
- The "Add podcast" screen includes a "Suggestions by Apple Podcasts" section to aid discovery.
- The first audio played from the episode was an advertisement for "Avocado Mattress".