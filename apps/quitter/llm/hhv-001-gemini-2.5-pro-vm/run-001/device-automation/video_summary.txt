---
app: Addiction Tracker
goal: The user wants to explore the alcohol sobriety tracker, change their quit date, and view the details of a recovery milestone.
outcome: success — The user successfully updated their quit date and viewed the details of a milestone on the recovery timeline.
---

## Session Summary
The user started on the app's main dashboard, which lists various addictions to track. They selected the "Alcohol" tracker, which took them to a timeline of their sobriety journey. On this screen, they successfully changed their quit date, which updated the total days counted. Finally, they tapped on a specific health milestone to read more details before the session ended.

## Steps

### 1. Select Alcohol Tracker — 0s
- **Screen:** Addictions Dashboard
- **Action:** tap → `Alcohol` tile
- **Details:** The tile shows "Alcohol", "15 days", and a quit date of "Apr 17, 2026".
- **Result:** The app navigates to the "Sober & sparkling" timeline screen for alcohol.
- **Confidence:** 1.0

### 2. Open Date Picker — 2s
- **Screen:** Sober & sparkling (Timeline)
- **Action:** tap → `Quit date` field
- **Details:** The current quit date is displayed as "Apr 17, 2026 (15 days)".
- **Result:** A calendar dialog appears with the title "Select date".
- **Confidence:** 1.0

### 3. Change Quit Date — 4s
- **Screen:** Sober & sparkling (Timeline)
- **Action:** select → `9` (on calendar)
- **Details:** The user selects April 9th from the calendar.
- **Result:** The selected date in the dialog changes to "Thu, Apr 9".
- **Confidence:** 1.0

### 4. Confirm New Date — 5s
- **Screen:** Sober & sparkling (Timeline)
- **Action:** tap → `OK` button
- **Details:** The user confirms the new date selection in the calendar dialog.
- **Result:** The dialog closes. The "Quit date" on the timeline screen updates to "Apr 9, 2026 (23 days)".
- **Confidence:** 1.0

### 5. View Milestone Details — 8s
- **Screen:** Sober & sparkling (Timeline)
- **Action:** tap → `Brain Volume Recovery Begins` milestone
- **Details:** The user taps on the first milestone on the updated timeline.
- **Result:** The app navigates to a new screen with detailed information about "Brain Volume Recovery Begins".
- **Confidence:** 1.0

### 6. Scroll Details Page — 10s
- **Screen:** Brain Volume Recovery Begins
- **Action:** swipe_up → `Text content`
- **Details:** The user scrolls down to view the rest of the article.
- **Result:** The bottom of the page is revealed, showing a button to "Open Original Source" and the source URL.
- **Confidence:** 1.0

## Key Observations
- The app features a dynamic timeline that visualizes health recovery milestones after quitting a substance.
- Changing the "Quit date" automatically recalculates and updates the number of days sober and the user's position on the recovery timeline.
- The information for recovery milestones is sourced from external websites, such as `priorygroup.com`, and the app provides a link to the original source.