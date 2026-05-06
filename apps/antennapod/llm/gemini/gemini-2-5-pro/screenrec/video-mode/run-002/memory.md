---
app: AntennaPod
goal: To find and play a podcast episode without subscribing to the podcast.
outcome: success — The user successfully started streaming a podcast episode.
---

## Session Summary
The user launched the AntennaPod app for the first time, which opened directly to the "Add podcast" screen. After briefly exploring the main navigation tabs (Home, Queue, Subscriptions), the user returned to the "Add podcast" screen, loaded suggestions, and selected the "Up First from NPR" podcast. They then selected a specific episode and successfully began streaming it.

## Steps

### 1. App Launch — 0s
- **Screen:** Android Home Screen
- **Action:** `launch` → `AntennaPod` app icon
- **Details:** The app icon is a blue circle with a white antenna symbol.
- **Result:** The AntennaPod app opens to the "Add podcast" screen.
- **Confidence:** 1.0

### 2. Navigate to Home Screen — 8s
- **Screen:** Add podcast
- **Action:** `back` → `Back arrow` in the top-left corner
- **Details:** The user navigates away from the initial "Add podcast" screen.
- **Result:** The app's "Home" screen is displayed, showing a welcome message.
- **Confidence:** 1.0

### 3. Navigate to Queue — 11s
- **Screen:** Home
- **Action:** `tap` → `Queue` tab in the bottom navigation bar
- **Details:** The Queue tab has an icon of three horizontal lines with a play arrow.
- **Result:** The "Queue" screen is displayed, showing "No queued episodes".
- **Confidence:** 1.0

### 4. Navigate to Subscriptions — 16s
- **Screen:** Queue
- **Action:** `tap` → `Subscriptions` tab in the bottom navigation bar
- **Details:** The Subscriptions tab has an icon of four squares.
- **Result:** The "Subscriptions" screen is displayed, showing "No subscriptions".
- **Confidence:** 1.0

### 5. Open Add Podcast Screen — 17s
- **Screen:** Subscriptions
- **Action:** `tap` → `+` floating action button
- **Details:** The button is in the bottom-right corner.
- **Result:** The "Add podcast" screen is displayed again.
- **Confidence:** 1.0

### 6. Load Podcast Suggestions — 20s
- **Screen:** Add podcast
- **Action:** `tap` → `Show suggestions` button
- **Details:** The screen initially shows grey placeholder tiles.
- **Result:** The placeholder tiles are populated with cover art for suggested podcasts.
- **Confidence:** 1.0

### 7. Select Podcast — 21s
- **Screen:** Add podcast
- **Action:** `tap` → `Up First` podcast cover art
- **Details:** The podcast is from NPR.
- **Result:** A loading spinner appears briefly, followed by a dialog showing the podcast's details and episode list.
- **Confidence:** 1.0

### 8. Select Episode — 24s
- **Screen:** Podcast details dialog ("Up First from NPR")
- **Action:** `tap` → Episode titled "US & Iran Plan To Meet Again..."
- **Details:** The episode is dated Feb 18.
- **Result:** The app navigates to a detailed view for the selected episode.
- **Confidence:** 1.0

### 9. Start Streaming — 27s
- **Screen:** Episode details
- **Action:** `tap` → `Stream` button
- **Details:** A banner is visible stating "You are not subscribed to this podcast yet."
- **Result:** The `Stream` button changes to a `Pause` button, indicating that audio playback has started.
- **Confidence:** 1.0

## Key Observations
- On first launch, the app opens directly to the "Add podcast" screen, providing a clear starting point for new users.
- The app allows users to stream individual episodes without requiring a subscription to the podcast.
- Podcast suggestions are explicitly sourced from "Apple Podcasts".
- The selected episode was "Up First from NPR" from Feb 18, titled "US & Iran Plan To Meet Again, CBS: Colbert & Cooper, Social Media On Trial".