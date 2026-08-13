---
app: Simple Gallery
goal: To enable and use the feature for changing images by tapping the sides of the screen.
outcome: failure — The feature did not work; tapping the screen sides only toggled the UI visibility.
---

## Session Summary
The user started in the gallery's folder view and opened an image. They then navigated to the settings menu, enabled the "Allow instantly changing media by clicking on screen sides" option, and returned to the image. Upon trying to use the newly enabled feature, tapping the sides of the screen failed to change the image and instead only toggled the visibility of the UI toolbars.

## Steps

### 1. Open Image — 2s
- **Screen:** Folder View
- **Action:** tap → Image thumbnail in "Download" folder
- **Details:** The user taps an image thumbnail showing a purple and orange sci-fi scene.
- **Result:** The app transitions to the full-screen image viewer.
- **Confidence:** 1.0

### 2. Open Options Menu — 4s
- **Screen:** Image Viewer
- **Action:** tap → "More options" (three-dot icon)
- **Details:** The image displayed is "Samus_vs_Quadraxis...".
- **Result:** A context menu appears over the image.
- **Confidence:** 1.0

### 3. Open Settings — 5s
- **Screen:** Image Viewer
- **Action:** tap → "Settings" menu item
- **Details:** The user selects "Settings" from the bottom of the context menu.
- **Result:** The app navigates to the main Settings screen.
- **Confidence:** 1.0

### 4. Scroll Settings — 8s
- **Screen:** Settings
- **Action:** swipe_up → Settings list
- **Details:** The user scrolls down to reveal more options.
- **Result:** The list scrolls, showing the "Fullscreen media" section.
- **Confidence:** 1.0

### 5. Enable Setting — 11s
- **Screen:** Settings
- **Action:** tap → Toggle switch
- **Details:** The user enables the setting "Allow instantly changing media by clicking on screen sides".
- **Result:** The toggle switch turns on (changes color).
- **Confidence:** 1.0

### 6. Navigate Back — 13s
- **Screen:** Settings
- **Action:** back → System back gesture
- **Details:** The user performs a swipe-from-edge back gesture.
- **Result:** The app returns to the Image Viewer screen.
- **Confidence:** 1.0

### 7. Test Feature (Right Tap) — 16s
- **Screen:** Image Viewer
- **Action:** tap → Right side of the image
- **Details:** The user taps the right edge of the screen, expecting the next image to appear.
- **Result:** The top and bottom UI bars disappear, but the image does not change.
- **Confidence:** 1.0

### 8. Test Feature (Left Tap) — 19s
- **Screen:** Image Viewer
- **Action:** tap → Left side of the image
- **Details:** After the UI reappears, the user taps the left edge of the screen, expecting the previous image to appear.
- **Result:** The top and bottom UI bars disappear again. The image does not change.
- **Confidence:** 1.0

## Key Observations
- **Bug:** The setting "Allow instantly changing media by clicking on screen sides" does not function as expected. When enabled, tapping the screen sides only toggles the UI visibility, which is the default behavior, instead of navigating between media files.
- **Image Details:** The image being viewed is named "Samus_vs_Quadraxis...", with a resolution of 1666 x 1666 (2.8MP) and a creation date of 31 July 2020.