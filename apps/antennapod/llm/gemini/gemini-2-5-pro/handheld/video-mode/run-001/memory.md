---
app: AntennaPod
goal: The user wants to find and play a podcast episode without subscribing to the podcast.
outcome: success - The user successfully found, streamed, and paused a podcast episode.
---

## Session Summary
The user launched the AntennaPod app from its Play Store page. After a brief tour of the main navigation tabs, which were mostly empty, they navigated to the "Add podcast" screen. From there, they selected a suggested podcast, chose an episode, and began streaming it, confirming that playback is possible without a subscription. The session concluded with the user pausing the episode from the full-screen player.

## Steps

### 1. Launch App — 1s
- **Screen:** Google Play Store - AntennaPod
- **Action:** tap → Open button
- **Details:** The user is on the app's store page and taps "Open" to launch it.
- **Result:** The AntennaPod app opens.
- **Confidence:** 1.0

### 2. View Queue — 6s
- **Screen:** Home
- **Action:** tap → Queue tab
- **Details:** The home screen shows a "Welcome to AntennaPod!" message.
- **Result:** The app navigates to the "Queue" screen.
- **Confidence:** 1.0

### 3. View Inbox — 8s
- **Screen:** Queue
- **Action:** tap → Inbox tab
- **Details:** The queue screen surprisingly contains two episodes already.
- **Result:** The app navigates to the "Inbox" screen.
- **Confidence:** 1.0

### 4. View Subscriptions — 11s
- **Screen:** Inbox
- **Action:** tap → Subscriptions tab
- **Details:** The inbox is empty.
- **Result:** The app navigates to the "Subscriptions" screen.
- **Confidence:** 1.0

### 5. Open Add Podcast Screen — 14s
- **Screen:** Subscriptions
- **Action:** tap → Plus (+) icon
- **Details:** The subscriptions screen is empty, prompting the user to add a podcast.
- **Result:** The "Add podcast" screen appears.
- **Confidence:** 1.0

### 6. Select Suggested Podcast — 16s
- **Screen:** Add podcast
- **Action:** tap → "Bridge of Lies" podcast tile
- **Details:** The user selects a podcast from the "Suggestions by Apple Podcasts" grid.
- **Result:** The app navigates to the details page for the "Bridge of Lies" podcast.
- **Confidence:** 1.0

### 7. Select Episode — 18s
- **Screen:** Add podcast - Bridge of Lies
- **Action:** tap → "The Search" episode
- **Details:** The user selects the episode from the "Episodes preview" list.
- **Result:** The app navigates to the episode detail/playback screen.
- **Confidence:** 1.0

### 8. Stream Episode — 20s
- **Screen:** Add podcast - The Search
- **Action:** tap → Stream button
- **Details:** The user initiates playback for the selected episode.
- **Result:** The episode begins to play, and the "Stream" button changes to a "Pause" button. A mini-player appears at the bottom of the screen.
- **Confidence:** 1.0

### 9. Navigate Back — 25s
- **Screen:** Add podcast - The Search
- **Action:** back → Back arrow icon
- **Details:** The user navigates back while the episode is playing.
- **Result:** The app returns to the "Add podcast" suggestions screen, with the mini-player still active at the bottom.
- **Confidence:** 1.0

### 10. Expand Mini-Player — 28s
- **Screen:** Add podcast
- **Action:** tap → Mini-player bar
- **Details:** The user taps the mini-player at the bottom of the screen.
- **Result:** The full-screen player view is displayed.
- **Confidence:** 1.0

### 11. Pause Playback — 31s
- **Screen:** Player
- **Action:** tap → Pause button
- **Details:** The user taps the central pause button to stop the audio.
- **Result:** The podcast playback is paused.
- **Confidence:** 1.0

## Key Observations
- Even on what appears to be a fresh launch with no subscriptions, the "Queue" screen was pre-populated with two episodes: "#2466 - Francis Foster & Konstantin Kisin" and "The Search".
- The app allows users to stream individual episodes without requiring them to subscribe to the podcast first.
- A persistent mini-player appears at the bottom of the screen once playback starts, allowing the user to continue browsing while listening.
- The selected episode, "The Search," displays a content warning regarding discussions of suicide.