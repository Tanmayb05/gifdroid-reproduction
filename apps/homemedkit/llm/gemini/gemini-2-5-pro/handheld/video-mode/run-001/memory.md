---
app: Home Medkit
goal: The user wants to manually add a new medication to their inventory.
outcome: success - The user successfully added a new medication, and it appeared on the main list.
---

## Session Summary
The user launched the "Home Medkit" app from its Play Store page. On the main screen, which was initially empty, they tapped the add button and chose to add a new medication manually. They proceeded to fill out a form with details like product name, expiration date, and release form before saving the entry. The session concluded with the user navigating back to the main screen and confirming the new medication was successfully added to the list.

## Steps

### 1. Launch App — 1s
- **Screen:** Google Play Store
- **Action:** tap → `Open` button
- **Details:** The user is on the app's store page and taps "Open" to launch it.
- **Result:** The "Home Medkit" application starts.
- **Confidence:** 1.0

### 2. Initiate Add Medicine — 5s
- **Screen:** Medicine
- **Action:** tap → `+` floating action button
- **Details:** The main screen shows "No medications found."
- **Result:** Two new buttons, "Scan" and "Add", appear above the `+` button.
- **Confidence:** 1.0

### 3. Select Manual Add — 8s
- **Screen:** Medicine
- **Action:** tap → `Add` button
- **Details:** The user chooses the manual entry option.
- **Result:** The app navigates to the "Add Medicine" form.
- **Confidence:** 1.0

### 4. Enter Product Name — 13s
- **Screen:** Add Medicine
- **Action:** type → `Product name` text field
- **Details:** Typed "Twfh".
- **Result:** The text "Twfh" is entered into the field.
- **Confidence:** 1.0

### 5. Attempt to Select Group — 16s
- **Screen:** Add Medicine
- **Action:** tap → `Group` text field
- **Details:** The field shows "Empty".
- **Result:** A dialog appears with the title "Medication groups" and the message "There are no groups found. You can add groups in the application settings."
- **Confidence:** 1.0

### 6. Set Expiration Date — 19s
- **Screen:** Add Medicine
- **Action:** tap → `Exp. date` text field
- **Details:** The user taps the expiration date field.
- **Result:** A date picker dialog appears, showing months for the year 2026.
- **Confidence:** 1.0

### 7. Save Expiration Date — 20s
- **Screen:** Add Medicine (Date Picker)
- **Action:** select → `APR` and `Save`
- **Details:** The user selects "APR" from the month grid.
- **Result:** The dialog closes, and the "Exp. date" field is updated to "April 30, 2026".
- **Confidence:** 1.0

### 8. Enter Display Name — 30s
- **Screen:** Add Medicine
- **Action:** type → `Display name` text field
- **Details:** Typed "Ygjj".
- **Result:** The text "Ygjj" is entered into the field.
- **Confidence:** 1.0

### 9. Enter Release Form — 33s
- **Screen:** Add Medicine
- **Action:** type → `Release form` text field
- **Details:** Typed "Trgh".
- **Result:** The text "Trgh" is entered into the field.
- **Confidence:** 1.0

### 10. Save New Medicine — 35s
- **Screen:** Add Medicine
- **Action:** tap → `✓` (Save) icon
- **Details:** The user taps the checkmark icon in the top-right corner to save the form.
- **Result:** The app saves the data and transitions to the details view for the newly created medicine.
- **Confidence:** 1.0

### 11. Return to Main List — 38s
- **Screen:** Medicine Details
- **Action:** tap → `←` (Back) icon
- **Details:** The user is on the details screen for the new medicine.
- **Result:** The app navigates back to the main "Medicine" screen.
- **Confidence:** 1.0

## Key Observations
- When the user tried to assign a "Group", a dialog informed them that no groups exist and must be created in settings first. This interrupts the add-medicine workflow.
- The user entered gibberish text ("Twfh", "Ygjj", "Trgh") for the medication details, indicating a test or exploratory session.
- The final list item on the main screen uses the "Release form" text ("Trgh") as the primary title and the "Display name" text ("Ygjj") as the subtitle. The "Product name" ("Twfh") is not displayed in the list view.