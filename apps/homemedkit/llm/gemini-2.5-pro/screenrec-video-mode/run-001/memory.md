---
app: Medicine Tracker
goal: To manually add a new medication to the application's inventory.
outcome: success - The user successfully filled out the form and saved the new medication.
---

## Session Summary
The user started on the main "Medicine" list screen and tapped the add button to create a new entry. They proceeded to fill out a detailed form for a new medication, including its name, expiration date, and other attributes. After completing the form, the user saved the entry and was taken to a details page confirming the new medication was successfully added to the system.

## Steps

### 1. Initiate Add Medication — 2s
- **Screen:** Medicine List
- **Action:** tap → `+` floating action button
- **Details:** The button is located in the bottom right corner.
- **Result:** Two new buttons, "Scan" and "Add", appeared above the initial button.
- **Confidence:** 1.0

### 2. Select Manual Add — 4s
- **Screen:** Medicine List
- **Action:** tap → `Add` button
- **Details:** The user chose the manual add option.
- **Result:** The app navigated to the "Add Medication" form screen.
- **Confidence:** 1.0

### 3. Enter Product Name — 6s
- **Screen:** Add Medication
- **Action:** type → `Product name` field
- **Details:** Typed "medA".
- **Result:** The text "medA" appeared in the "Product name" field.
- **Confidence:** 1.0

### 4. Check Medication Groups — 10s
- **Screen:** Add Medication
- **Action:** tap → `Group` field
- **Details:** The field initially showed "Empty".
- **Result:** A dialog titled "Medication groups" appeared, stating "There are no groups found. You can add groups in the application settings."
- **Confidence:** 1.0

### 5. Dismiss Group Dialog — 13s
- **Screen:** Add Medication
- **Action:** tap → `Save` button in dialog
- **Details:** The user dismissed the "Medication groups" dialog.
- **Result:** The dialog closed, and the user returned to the "Add Medication" form.
- **Confidence:** 1.0

### 6. Set Expiration Date — 14s
- **Screen:** Add Medication
- **Action:** tap → `Exp. date` field
- **Details:** The user selected "MAY" from the year 2026 and tapped "Save".
- **Result:** The "Exp. date" field was populated with "May 31, 2026".
- **Confidence:** 1.0

### 7. Set Package Opened Date — 19s
- **Screen:** Add Medication
- **Action:** tap → `Package opened` field
- **Details:** The user selected "22" from the calendar for May 2026 and tapped "Save".
- **Result:** The "Package opened" field was populated with "May 22, 2026".
- **Confidence:** 1.0

### 8. Enter Display Name — 25s
- **Screen:** Add Medication
- **Action:** type → `Display name` field
- **Details:** Typed "medA".
- **Result:** The text "medA" appeared in the "Display name" field.
- **Confidence:** 1.0

### 9. Enter Release Form — 29s
- **Screen:** Add Medication
- **Action:** type → `Release form` field
- **Details:** Typed "medB".
- **Result:** The text "medB" appeared in the "Release form" field.
- **Confidence:** 1.0

### 10. Enter Comment — 37s
- **Screen:** Add Medication
- **Action:** type → `Comment` field
- **Details:** Typed "abc".
- **Result:** The text "abc" appeared in the "Comment" field.
- **Confidence:** 1.0

### 11. Save New Medication — 39s
- **Screen:** Add Medication
- **Action:** tap → `✓` (check) icon
- **Details:** The save icon is in the top right corner of the screen.
- **Result:** The app saved the form and navigated to the details screen for the newly created medication.
- **Confidence:** 1.0

## Key Observations
- When attempting to assign a medication to a group, a dialog appears informing the user that no groups exist and must be added in the settings.
- The application uses two different UI styles for date selection: a month/year picker for the expiration date and a full calendar view for the package opened date.
- After successfully adding a new medication, the user is directed to its details page, not back to the main medicine list.
- The newly created item is automatically assigned a status of "Added manually" and a group of "Unspecified".