---
app: Blood Pressure Tracker
goal: To view statistical analysis of recorded blood pressure data.
outcome: success - The user successfully navigated to the statistics screen and viewed the available data visualizations.
---

## Session Summary
The user started on the main log screen of a blood pressure app, which displayed a single data entry. They tapped the statistics button to open the statistics page, where they toggled between viewing the value distribution for systolic, diastolic, and pulse readings. Finally, they scrolled down to reveal an empty "Metrics by time of day" chart.

## Steps

### 1. Navigate to Statistics — 2s
- **Screen:** Main Log
- **Action:** `tap` → `Statistics button` (graph icon)
- **Details:** The main screen shows one entry: Systolic 98, Diastolic 70, Pulse 123.
- **Result:** The app navigates to the "Statistics" screen.
- **Confidence:** 1.0

### 2. View Diastolic Statistics — 3s
- **Screen:** Statistics
- **Action:** `tap` → `Diastolic` tab
- **Details:** The user taps the "Diastolic" tab in the "Value distribution" section.
- **Result:** The graph updates to show the diastolic value (70 min, 70 avg, 70 max) and its color changes to green.
- **Confidence:** 1.0

### 3. View Pulse Statistics — 4s
- **Screen:** Statistics
- **Action:** `tap` → `Pulse` tab
- **Details:** The user taps the "Pulse" tab in the "Value distribution" section.
- **Result:** The graph updates to show the pulse value (123 min, 123 avg, 123 max) and its color changes to red.
- **Confidence:** 1.0

### 4. View Metrics by Time of Day — 6s
- **Screen:** Statistics
- **Action:** `swipe_up` → `Screen`
- **Details:** The user scrolls down the statistics page.
- **Result:** The "Metrics by time of day" section, containing a circular 24-hour chart, becomes fully visible.
- **Confidence:** 1.0

## Key Observations
- The app contained a single data point at the start of the session: Systolic 98, Diastolic 70, Pulse 123.
- The "Metrics by time of day" visualization is a radial chart representing a 24-hour clock.
- The date range filter on the main screen ("Apr 1, 2026 - May 1, 2026") is different from the one on the statistics screen ("Apr 14, 2026 - Apr 21, 2026"), suggesting they are controlled independently.