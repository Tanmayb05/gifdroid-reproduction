---
app: Home Medkit
goal: To manually add a new medication to the application.
outcome: success - The user successfully added a new medication, which then appeared on the main list.
---

## Session Summary
The user launched the "Home Medkit" app from its Play Store page. On the main screen, which was initially empty, they initiated the process to add a new medication. They filled out several fields in the "Add Medication" form, including product name, expiration date, and release form, before saving the entry. The session concluded successfully with the newly created medication visible on the main "Medicine" screen.

## Steps

### 1. Launch App — 1s
- **Screen:** Google Play Store - Home Medkit
- **Action:** tap → `Open` button
- **Details:** The user is on the app's store page and launches it.
- **Result:** The "Home Medkit" application opens.
- **Confidence:** 1.0

### 2. Open Add Menu — 5s
- **Screen:** Medicine
- **Action:** tap → `+` floating action button
- **Details:** The main screen shows "No medications found."
- **Result:** Two new buttons, "Scan" and "Add", appear above the `+` button.
- **Confidence:** 1.0

### 3. Navigate to Add Medication Form — 8s
- **Screen:** Medicine
- **Action:** tap → `Add` button
- **Details:** The user selects the manual add option.
- **Result:** The app navigates to the "Add Medication" form.
- **Confidence:** 1.0

### 4. Enter Product Name — 13s
- **Screen:** Add Medication
- **Action:** type → `Product name` text field
- **Details:** Typed "Twfh".
- **Result:** The text "Twfh" is entered into the field.
- **Confidence:** 1.0

### 5. Check Medication Groups — 16s
- **Screen:** Add Medication
- **Action:** tap → `Group` text field
- **Details:** The field is currently empty.
- **Result:** A dialog appears with the title "Medication groups" and the message "There are no groups found. You can add groups in the application settings."
- **Confidence:** 1.0

### 6. Set Expiration Date — 19s
- **Screen:** Add Medication
- **Action:** tap → `Exp. date` text field
- **Details:** The user selects "APR" from the 2026 year view and taps "Save".
- **Result:** The "Exp. date" field is populated with "April 30, 2026".
- **Confidence:** 1.0

### 7. Enter Display Name — 30s
- **Screen:** Add Medication
- **Action:** type → `Display name` text field
- **Details:** Typed "Ygjj".
- **Result:** The text "Ygjj" is entered into the field.
- **Confidence:** 1.0

### 8. Enter Release Form — 34s
- **Screen:** Add Medication
- **Action:** type → `Release form` text field
- **Details:** Typed "Trgh".
- **Result:** The text "Trgh" is entered into the field.
- **Confidence:** 1.0

### 9. Save New Medication — 36s
- **Screen:** Add Medication
- **Action:** tap → `✓` (Save) icon
- **Details:** The user taps the checkmark icon in the top-right corner.
- **Result:** The form becomes read-only, displaying the saved medication details.
- **Confidence:** 1.0

### 10. Return to Main Screen — 38s
- **Screen:** Medication Details
- **Action:** tap → `←` (Back) icon
- **Details:** The user navigates back from the details view.
- **Result:** The app returns to the "Medicine" screen, which now lists the newly added item.
- **Confidence:** 1.0

## Key Observations
- When attempting to assign a medication to a group, the app displays a dialog informing the user that groups must be created in the settings first. This prevents the user from creating groups on the fly.
- The user did not interact with the "Dose" or "Amount" fields, which had default or pre-filled values.
- After saving a new medication, the user is taken to a read-only detail view of that item, requiring an extra tap to return to the main list.
- The main list view displays the "Release form" ("Trgh") as the primary title and the "Display name" ("Ygjj") as the subtitle for the medication entry.