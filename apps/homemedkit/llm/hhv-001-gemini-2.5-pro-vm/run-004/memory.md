---
app: Home Medkit
goal: To add a new medication to the app manually.
outcome: success - The user successfully added a new medication, and it appeared on the main list.
---

## Session Summary
The user launched the "Home Medkit" app from its Play Store page. Finding the medicine list empty, they initiated the process to add a new entry. They navigated to the "Add Medicine" form, filled in several fields with test data, and saved the new medication. The session concluded successfully with the new entry appearing on the main "Medicine" screen.

## Steps

### 1. Launch App — 1s
- **Screen:** Google Play Store - Home Medkit
- **Action:** tap → "Open" button
- **Details:** The app page for "Home Medkit" is visible.
- **Result:** The "Home Medkit" application launches to its main screen.
- **Confidence:** 1.0

### 2. Open Add Options — 5s
- **Screen:** Medicine
- **Action:** tap → green "+" floating action button
- **Details:** The screen displays the message "No medications found. Add them or change the filter."
- **Result:** Two new buttons, "Scan" and "Add", appear above the tapped button.
- **Confidence:** 1.0

### 3. Navigate to Add Medicine Form — 8s
- **Screen:** Medicine
- **Action:** tap → "Add" button
- **Result:** The app navigates to the "Add Medicine" form.
- **Confidence:** 1.0

### 4. Enter Product Name — 13s
- **Screen:** Add Medicine
- **Action:** type → "Product name" field
- **Details:** Typed "Twfh".
- **Result:** The text "Twfh" is entered into the field.
- **Confidence:** 1.0

### 5. Attempt to Select Group — 16s
- **Screen:** Add Medicine
- **Action:** tap → "Group" field
- **Result:** A dialog titled "Medication groups" appears, stating that no groups are found and must be added in settings.
- **Confidence:** 1.0

### 6. Dismiss Group Dialog — 17s
- **Screen:** Add Medicine (with "Medication groups" dialog)
- **Action:** tap → "OK" button
- **Result:** The dialog is dismissed, returning focus to the form.
- **Confidence:** 1.0

### 7. Set Expiration Date — 19s
- **Screen:** Add Medicine
- **Action:** select → "Exp. date" field
- **Details:** The user opens a date picker, selects "APR" in the year "2026", and taps "Save".
- **Result:** The "Exp. date" field is populated with "April 30, 2026".
- **Confidence:** 1.0

### 8. Enter Display Name — 30s
- **Screen:** Add Medicine
- **Action:** type → "Display name" field
- **Details:** Typed "Ygjj".
- **Result:** The text "Ygjj" is entered into the field.
- **Confidence:** 1.0

### 9. Enter Release Form — 34s
- **Screen:** Add Medicine
- **Action:** type → "Release form" field
- **Details:** Typed "Trgh".
- **Result:** The text "Trgh" is entered into the field.
- **Confidence:** 1.0

### 10. Save New Medicine — 35s
- **Screen:** Add Medicine
- **Action:** tap → checkmark icon (top right)
- **Result:** The form is submitted, and the app transitions to a details view of the newly created medicine.
- **Confidence:** 1.0

### 11. Return to Medicine List — 38s
- **Screen:** Medicine Details
- **Action:** back → back arrow icon (top left)
- **Result:** The app navigates back to the main "Medicine" screen, which now shows the newly added item.
- **Confidence:** 1.0

## Key Observations
- The user entered gibberish text ("Twfh", "Ygjj", "Trgh") for the medicine names, suggesting a test of the input fields.
- When attempting to assign a group, a dialog informed the user that no groups exist and must be created in settings. It is not possible to create a group from within the "Add Medicine" workflow.
- The date picker automatically selected the last day of the chosen month (April 30th) when only the month and year were selected.
- On the main list, the "Release form" text ("Trgh") is used as the primary title for the medicine entry, with the "Display name" ("Ygjj") as the subtitle.