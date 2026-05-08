---
app: NewPipe
goal: To play a trending music video and adjust its playback speed.
outcome: success - The user successfully navigated to a video and changed its playback speed.
---

## Session Summary
The user started on the NewPipe home screen, opened the navigation menu, and selected "Trending music". They then chose a video to play. Once the video player was open, the user accessed the playback speed controls, significantly increased the speed, and then reset it back to the default, confirming the feature works as expected.

## Steps

### 1. Open Navigation Menu — 0s
- **Screen:** Home
- **Action:** `tap` → `Hamburger Menu Icon`
- **Details:** The home screen shows a feed of recommended videos.
- **Result:** The main navigation drawer slides in from the left side of the screen.
- **Confidence:** 1.0

### 2. Navigate to Trending Music — 2s
- **Screen:** Navigation Drawer
- **Action:** `tap` → `Trending music`
- **Details:** The menu contains options like "YouTube", "Subscriptions", "History", and "Trending".
- **Result:** The app transitions to the "Trending music" screen, which begins to load content.
- **Confidence:** 1.0

### 3. Select Video — 6s
- **Screen:** Trending music
- **Action:** `tap` → `Video Thumbnail (PODCATERA)`
- **Details:** The user selects the video titled "PODCATERA" from the list of trending music videos.
- **Result:** The app navigates to the video player screen for the selected video.
- **Confidence:** 1.0

### 4. Open Playback Speed Controls — 10s
- **Screen:** Video Player
- **Action:** `tap` → `Playback Speed Indicator (1x)`
- **Details:** The video "MICHAEL FLORES X ALOFOKE MUSIC X JEY ONE X YOVAN..." is playing.
- **Result:** A "Playback speed" dialog appears, showing controls for Tempo and Pitch.
- **Confidence:** 1.0

### 5. Increase Playback Speed — 14s
- **Screen:** Video Player (Playback speed dialog)
- **Action:** `tap` → `Tempo +25% button`
- **Details:** The user taps the "+25%" button multiple times, increasing the tempo to 1.83x.
- **Result:** The tempo value in the dialog updates with each tap.
- **Confidence:** 1.0

### 6. Confirm Speed Change — 16s
- **Screen:** Video Player (Playback speed dialog)
- **Action:** `tap` → `OK button`
- **Result:** The dialog closes, and the video continues playing at the new, faster speed (1.83x).
- **Confidence:** 1.0

### 7. Re-open Playback Speed Controls — 21s
- **Screen:** Video Player
- **Action:** `tap` → `Playback Speed Indicator (1.83x)`
- **Details:** The video is playing at a noticeably faster speed.
- **Result:** The "Playback speed" dialog re-appears.
- **Confidence:** 1.0

### 8. Reset Playback Speed — 23s
- **Screen:** Video Player (Playback speed dialog)
- **Action:** `tap` → `RESET button`
- **Result:** The Tempo and Pitch values in the dialog are reset to their defaults (1.0x and 100%).
- **Confidence:** 1.0

### 9. Confirm Speed Reset — 24s
- **Screen:** Video Player (Playback speed dialog)
- **Action:** `tap` → `OK button`
- **Result:** The dialog closes, and the video's playback speed returns to normal (1x).
- **Confidence:** 1.0

## Key Observations
- The application being used is NewPipe, an open-source YouTube client.
- The playback speed control allows for independent adjustment of Tempo and Pitch.
- A transient error message, "Could not parse website," is visible at the bottom of the video player screen, suggesting a potential issue with loading comments or related content.