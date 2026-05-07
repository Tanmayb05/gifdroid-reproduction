---
app: AntennaPod
goal: The user wants to find and listen to a podcast episode without subscribing.
outcome: success - The user successfully found a podcast and started streaming an episode.
---

## Session Summary
The user launched the AntennaPod app for the first time and briefly explored the empty Home, Queue, and Subscriptions tabs. They then returned to the "Add podcast" screen, loaded the suggested podcasts, selected "Up First from NPR", and began streaming the latest episode without subscribing to the show.

## Steps

### 1. App Launch — 7s
- **Screen:** Android Home Screen
- **Action:** tap → `AntennaPod` app icon
- **Details:** The user is on their phone's home screen and taps the AntennaPod icon to open the app.
- **Result:** The AntennaPod app opens to the "Add podcast" screen.
- **Confidence:** 1.0

### 2. Navigate to Home — 10s
- **Screen:** Add podcast
- **Action:** tap → `Home` tab
- **Details:** The user taps the "Home" icon in the bottom navigation bar.
- **Result:** The app navigates to the Home screen, which displays a welcome message.
- **Confidence:** 1.0

### 3. Navigate to Queue — 12s
- **Screen:** Home
- **Action:** tap → `Queue` tab
- **Details:** The user taps the "Queue" icon in the bottom navigation bar.
- **Result:** The app navigates to the Queue screen, which shows there are no queued episodes.
- **Confidence:** 1.0

### 4. Navigate to Subscriptions — 16s
- **Screen:** Queue
- **Action:** tap → `Subscriptions` tab
- **Details:** The user taps the "Subscriptions" icon in the bottom navigation bar.
- **Result:** The app navigates to the Subscriptions screen, which shows there are no subscriptions.
- **Confidence:** 1.0

### 5. Open Add Podcast Screen — 17s
- **Screen:** Subscriptions
- **Action:** tap → `+` floating action button
- **Details:** The user taps the plus icon to add a podcast.
- **Result:** The app returns to the "Add podcast" screen.
- **Confidence:** 1.0

### 6. Load Suggestions — 20s
- **Screen:** Add podcast
- **Action:** tap → `Show suggestions` button
- **Details:** The user taps the blue button to load podcast suggestions.
- **Result:** A grid of podcast cover art appears, replacing the grey placeholders.
- **Confidence:** 1.0

### 7. Select Podcast — 21s
- **Screen:** Add podcast
- **Action:** tap → `Up First` podcast
- **Details:** The user taps on the "Up First" podcast from the suggestions grid.
- **Result:** A modal dialog appears, showing details for the "Up First from NPR" podcast.
- **Confidence:** 1.0

### 8. Select Episode — 24s
- **Screen:** Add podcast (Podcast Details)
- **Action:** tap → `US & Iran Plan To Meet Again...` episode
- **Details:** The user taps the first episode in the "Episodes preview" list.
- **Result:** The app navigates to the episode details screen.
- **Confidence:** 1.0

### 9. Stream Episode — 27s
- **Screen:** Episode Details
- **Action:** tap → `Stream` button
- **Details:** The user taps the "Stream" button to begin playback.
- **Result:** The "Stream" button changes to a "Pause" button, and the podcast begins playing.
- **Confidence:** 1.0

## Key Observations
- For a new user, the app opens directly to the "Add podcast" screen.
- The app allows users to stream individual episodes without subscribing to the podcast. A banner is displayed prompting the user to subscribe.
- Podcast suggestions are sourced from "Apple Podcasts".
- The episode streamed was "US & Iran Plan To Meet Again, CBS: Colbert & Cooper, Social Media On Trial" dated Feb 18.