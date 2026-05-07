---
app: Blood Pressure Tracker
goal: To view the statistical analysis and charts for a recorded blood pressure measurement.
outcome: success - The user successfully navigated to the statistics screen and viewed the available charts.
---

## Session Summary
The user started on the main log screen of a blood pressure tracking app, which displayed a single data entry. They tapped the statistics button to navigate to a dedicated statistics page. On this page, they toggled between the systolic, diastolic, and pulse value distribution charts and then scrolled down to view an empty "Metrics by time of day" radar chart.

## Steps

### 1. Navigate to Statistics — 2s
- **Screen:** Main Log
- **Action:** `tap` → `Statistics button`
- **Details:** The user tapped the button with a graph icon to view data analysis. The main screen showed one entry: Systolic 98, Diastolic 70, Pulse 123.
- **Result:** The app navigated to the "Statistics" screen.
- **Confidence:** 1.0

### 2. View Diastolic Stats — 3s
- **Screen:** Statistics
- **Action:** `tap` → `Diastolic tab`
- **Details:** The "Value distribution" chart was initially showing the Systolic value (98).
- **Result:** The chart updated to show the Diastolic value (70), and the chart color changed from teal to green.
- **Confidence:** 1.0

### 3. View Pulse Stats — 4s
- **Screen:** Statistics
- **Action:** `tap` → `Pulse tab`
- **Details:** The user tapped the "Pulse" tab in the "Value distribution" section.
- **Result:** The chart updated to show the Pulse value (123), and the chart color changed from green to red.
- **Confidence:** 1.0

### 4. View Time of Day Metrics — 6s
- **Screen:** Statistics
- **Action:** `swipe_up` → `Screen`
- **Details:** The user scrolled down the "Statistics" page.
- **Result:** A "Metrics by time of day" section with a circular radar chart became visible.
- **Confidence:** 1.0

## Key Observations
- The single data point recorded was Systolic: 98, Diastolic: 70, Pulse: 123.
- The main screen states "Not enough data to draw a graph" for a single entry, but the statistics screen is able to generate a "Value distribution" chart from that same entry.
- The "Metrics by time of day" chart is a radar chart representing a 24-hour clock.
- There is a date range inconsistency: the main screen shows "Apr 1, 2026 - May 1, 2026" while the statistics screen shows "Apr 14, 2026 - Apr 21, 2026".