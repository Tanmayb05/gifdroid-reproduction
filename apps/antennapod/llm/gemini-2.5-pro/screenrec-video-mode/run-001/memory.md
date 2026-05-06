---
app: AntennaPod
goal: To find and listen to a podcast episode without subscribing to the podcast.
outcome: success - The user successfully found and started streaming a podcast episode.
---

## Session Summary
The user launched the AntennaPod app for the first time, which opened to the "Add podcast" screen. After briefly exploring the empty Home, Queue, and Subscriptions tabs, the user returned to the "Add podcast" screen. They then viewed suggestions, selected the "Up First from NPR" podcast, chose an episode, and successfully began streaming it without subscribing.

## Steps

### 1. App Launch — 7s
- **Screen:** Android Home Screen
- **Action:** tap → "AntennaPod" app icon
- **Details:** The icon is blue with a white antenna symbol.
- **Result:** The AntennaPod app opens to the "Add podcast" screen.
- **Confidence:** 1.0

### 2. Navigate to Home — 10s
- **Screen:** Add podcast
- **Action:** tap → "Home" tab
- **Details:** Tapped the "Home" icon in the bottom navigation bar.
- **Result:** The app navigates to the "Home" screen, which displays a "Welcome to AntennaPod!" message.
- **Confidence:** 1.0

### 3. Navigate to Queue — 12s
- **Screen:** Home
- **Action:** tap → "Queue" tab
- **Details:** Tapped the "Queue" icon in the bottom navigation bar.
- **Result:** The app navigates to the "Queue" screen, which shows "No queued episodes".
- **Confidence:** 1.0

### 4. Navigate to Subscriptions — 16s
- **Screen:** Queue
- **Action:** tap → "Subscriptions" tab
- **Details:** Tapped the "Subscriptions" icon in the bottom navigation bar.
- **Result:** The app navigates to the "Subscriptions" screen, which shows "No subscriptions".
- **Confidence:** 1.0

### 5. Initiate Add Podcast — 17s
- **Screen:** Subscriptions
- **Action:** tap → "+" floating action button
- **Details:** The button is in the bottom-right corner.
- **Result:** The "Add podcast" screen is displayed again.
- **Confidence:** 1.0

### 6. View Suggestions — 20s
- **Screen:** Add podcast
- **Action:** tap → "Show suggestions" button
- **Details:** The button is centered on the screen.
- **Result:** The placeholder squares are replaced with a grid of popular podcast cover art.
- **Confidence:** 1.0

### 7. Select Podcast — 22s
- **Screen:** Add podcast
- **Action:** tap → "Up First" podcast cover art
- **Details:** The podcast is from NPR.
- **Result:** A dialog appears, showing details for the "Up First from NPR" podcast, including a description and an episode preview.
- **Confidence:** 1.0

### 8. Select Episode — 24s
- **Screen:** Add podcast (with details dialog)
- **Action:** tap → "US & Iran Plan To Meet Again..." episode
- **Details:** The first episode in the preview list.
- **Result:** The screen transitions to the detailed view for that specific episode.
- **Confidence:** 1.0

### 9. Stream Episode — 27s
- **Screen:** Episode Details
- **Action:** tap → "Stream" button
- **Details:** The button has a cloud icon.
- **Result:** The "Stream" button changes to a "Pause" button, indicating the episode has started playing.
- **Confidence:** 1.0

## Key Observations
- For a new user, the app opens directly to the "Add podcast" screen.
- The user can preview and stream individual episodes without being required to subscribe to the podcast. A banner provides a non-blocking suggestion to subscribe.
- The episode selected was "US & Iran Plan To Meet Again, CBS: Colbert & Cooper, Social Media On Trial" from the "Up First from NPR" podcast, dated Feb 18.