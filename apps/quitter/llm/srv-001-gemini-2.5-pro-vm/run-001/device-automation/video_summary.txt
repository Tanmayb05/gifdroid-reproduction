---
app: Quitter
goal: The user wants to disable the Journal tab from the app's settings.
outcome: success — The Journal tab was successfully removed from the main navigation.
---

## Session Summary
The user started on the main "Quitter" screen, which lists addictions. They swiped to the "Journal" tab and made a brief entry, then swiped to the "Settings" tab. In settings, they located and disabled the "Show journal" option. Finally, they returned to the main screen and confirmed the "Journal" tab was no longer present in the top navigation.

## Steps

### 1. Navigate to Journal — 3s
- **Screen:** Quitter
- **Action:** `swipe_left`
- **Details:** Swiped from the "Quitter" tab to the "Journal" tab.
- **Result:** The "Journal" screen is displayed, showing a calendar and an entry field for "Friday, May 1, 2026".
- **Confidence:** 1.0

### 2. Create Journal Entry — 11s
- **Screen:** Journal
- **Action:** `type` → "How was your day?" text field
- **Details:** Typed "it was good".
- **Result:** The text "it was good" appears in the journal entry field.
- **Confidence:** 1.0

### 3. Navigate to Settings — 12s
- **Screen:** Journal
- **Action:** `swipe_left`
- **Details:** Swiped from the "Journal" tab to the "Settings" tab.
- **Result:** The "Settings" screen is displayed.
- **Confidence:** 1.0

### 4. Disable Journal Tab — 15s
- **Screen:** Settings
- **Action:** `tap` → "Show journal" toggle
- **Details:** The toggle was in the "on" state.
- **Result:** The "Show journal" toggle switches to the "off" state.
- **Confidence:** 1.0

### 5. Return to Main Screen — 16s
- **Screen:** Settings
- **Action:** `swipe_right`
- **Details:** Swiped from the "Settings" tab towards the main screen.
- **Result:** The "Quitter" screen is displayed, and the "Journal" tab is no longer visible in the top navigation bar.
- **Confidence:** 1.0

## Key Observations
- The app features a tabbed navigation for "Quitter", "Journal", and "Settings".
- The "Journal" tab's visibility can be controlled from the "Settings" screen via a "Show journal" toggle.
- The journal entry is dated for "Friday, May 1, 2026".
- The "Swipe between tabs" setting is enabled, allowing the user to navigate by swiping horizontally across the screen.