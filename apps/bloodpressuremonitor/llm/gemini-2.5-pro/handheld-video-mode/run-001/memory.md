---
app: Blood Pressure Tracker
goal: The user wants to add multiple blood pressure readings and view the resulting graph and statistics.
outcome: success - The user successfully added two data points, which generated a graph, and then viewed the statistics screen.
---

## Session Summary
The user started on the main screen of a blood pressure tracking application, which initially showed no data. They proceeded to add two separate blood pressure readings, including systolic, diastolic, pulse, and an optional note for each. After saving the second entry, a line graph appeared on the main screen. The user then navigated to the statistics page to view different data visualizations.

## Steps

### 1. Initiate New Record Entry — 0s
- **Screen:** Main Screen
- **Action:** tap → `+` icon
- **Details:** The screen initially displays "Not enough data to draw a graph."
- **Result:** Navigated to the "Add Record" screen.
- **Confidence:** 1.0

### 2. Enter First Blood Pressure Reading — 3s
- **Screen:** Add Record
- **Action:** type → `Systolic`, `Diastolic`, `Pulse` fields
- **Details:** Entered Systolic: 118, Diastolic: 76, Pulse: 68. The date is pre-filled as 2026-05-01.
- **Result:** The respective fields are populated with the entered numbers.
- **Confidence:** 1.0

### 3. Add Note to First Record — 9s
- **Screen:** Add Record
- **Action:** type → `Note (optional)` field
- **Details:** Typed the text "qwert".
- **Result:** The note field is populated with the text.
- **Confidence:** 1.0

### 4. Save First Record — 11s
- **Screen:** Add Record
- **Action:** tap → `Save` button
- **Details:** The user saves the first complete data entry.
- **Result:** Returned to the main screen. A single data point is listed, but the graph area still shows "Not enough data to draw a graph."
- **Confidence:** 1.0

### 5. Initiate Second Record Entry — 13s
- **Screen:** Main Screen
- **Action:** tap → `+` icon
- **Details:** The user begins adding a second data point.
- **Result:** Navigated to the "Add Record" screen.
- **Confidence:** 1.0

### 6. Enter Second Blood Pressure Reading — 16s
- **Screen:** Add Record
- **Action:** type → `Systolic`, `Diastolic`, `Pulse` fields
- **Details:** Entered Systolic: 122, Diastolic: 78, Pulse: 72.
- **Result:** The respective fields are populated with the new values.
- **Confidence:** 1.0

### 7. Add Note to Second Record — 23s
- **Screen:** Add Record
- **Action:** type → `Note (optional)` field
- **Details:** Typed the text "poiu".
- **Result:** The note field is populated with the text.
- **Confidence:** 1.0

### 8. Save Second Record — 25s
- **Screen:** Add Record
- **Action:** tap → `Save` button
- **Details:** The user saves the second complete data entry.
- **Result:** Returned to the main screen. A line graph connecting the two data points is now visible, and both entries are listed below.
- **Confidence:** 1.0

### 9. Navigate to Statistics — 26s
- **Screen:** Main Screen
- **Action:** tap → `Statistics` icon (graph-like icon)
- **Details:** The user taps the icon between the settings gear and the plus sign.
- **Result:** Navigated to the "Statistics" screen.
- **Confidence:** 1.0

### 10. Interact with Statistics Chart — 29s
- **Screen:** Statistics
- **Action:** swipe_left → `Value distribution` chart
- **Details:** The user swipes on the bar chart, cycling through visualizations for Systolic, Diastolic, and Pulse.
- **Result:** The chart's data and color change to reflect the selected metric.
- **Confidence:** 1.0

## Key Observations
- The application requires a minimum of two data points to render a line graph on the main screen.
- The date for the new entries was automatically set to a future date (May 1, 2026).
- The "Statistics" screen features two distinct visualizations: a "Value distribution" bar chart and a "Metrics by time of day" radial chart.
- The "Value distribution" chart is interactive, allowing the user to swipe between Systolic, Diastolic, and Pulse metrics.