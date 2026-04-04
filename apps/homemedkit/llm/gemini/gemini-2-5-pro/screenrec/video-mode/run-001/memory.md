---
app: Medkit
goal: The user wants to add a new medication to their inventory in the app.
outcome: success - The user successfully added a new medication and viewed its details.
---

## Session Summary
The user launched the Medkit app from their home screen and navigated to the "Add Medicine" form. They proceeded to fill out several fields for a new medication, including the product name, expiration date, and package opening date. After successfully saving the new entry, the session concluded on the details screen for the newly added medication.

## Steps

### 1. App Launch — 2s
- **Screen:** Android Home Screen
- **Action:** `tap` → `Medkit` app icon
- **Details:** The app icon is a white first-aid kit with a red cross on a red background.
- **Result:** The Medkit app launches and displays the "Medicine" list screen.
- **Confidence:** 1.0

### 2. Initiate Add Medicine — 6s
- **Screen:** Medicine List
- **Action:** `tap` → `+` floating action button
- **Details:** The screen shows one existing medication named "ert".
- **Result:** A menu with "Scan" and "Add" options appears.
- **Confidence:** 1.0

### 3. Select Manual Add — 7s
- **Screen:** Medicine List
- **Action:** `tap` → `Add` button
- **Result:** The app navigates to the "Add Medicine" form.
- **Confidence:** 1.0

### 4. Enter Product Name — 9s
- **Screen:** Add Medicine Form
- **Action:** `type` → `Product name` field
- **Details:** Typed "rt".
- **Result:** The text "rt" is entered into the field.
- **Confidence:** 1.0

### 5. Attempt to Select Group — 11s
- **Screen:** Add Medicine Form
- **Action:** `tap` → `Group` field
- **Result:** A dialog titled "Medication groups" appears.
- **Details:** The dialog states: "There are no groups found. You can add groups in the application settings."
- **Confidence:** 1.0

### 6. Close Group Dialog — 14s
- **Screen:** Add Medicine Form (with dialog)
- **Action:** `tap` → `Clear` button
- **Result:** The "Medication groups" dialog is dismissed.
- **Confidence:** 1.0

### 7. Set Expiration Date — 15s
- **Screen:** Add Medicine Form
- **Action:** `tap` → `Exp. date` field
- **Result:** A month and year picker dialog appears, defaulted to "2026".
- **Confidence:** 1.0

### 8. Select Expiration Month — 16s
- **Screen:** Add Medicine Form (with date picker)
- **Action:** `select` → `MAY`
- **Details:** The user then taps the "Save" button in the dialog.
- **Result:** The "Exp. date" field is populated with "May 31, 2026".
- **Confidence:** 1.0

### 9. Set Package Opened Date — 18s
- **Screen:** Add Medicine Form
- **Action:** `tap` → `Package opened` field
- **Result:** A calendar view date picker appears.
- **Confidence:** 1.0

### 10. Select Package Opened Day — 20s
- **Screen:** Add Medicine Form (with date picker)
- **Action:** `select` → `17`
- **Details:** The user then taps the "Save" button in the dialog.
- **Result:** The "Package opened" field is populated with "February 17, 2026".
- **Confidence:** 1.0

### 11. Enter Display Name — 22s
- **Screen:** Add Medicine Form
- **Action:** `type` → `Display name` field
- **Details:** Typed "dasd".
- **Result:** The text "dasd" is entered into the field.
- **Confidence:** 1.0

### 12. Save New Medication — 24s
- **Screen:** Add Medicine Form
- **Action:** `tap` → `✓` (check mark) icon in the top app bar
- **Result:** The form is saved, and the app transitions to the details screen for the newly created medication.
- **Confidence:** 1.0

## Key Observations
- When attempting to assign a medication group, the user was blocked by a dialog informing them that no groups exist and must be created in the settings first.
- When selecting only a month and year for the expiration date (May 2026), the app automatically set the date to the last day of that month (May 31, 2026).
- On the final details screen, the unselected "Group" field defaulted to "Unspecified".
- The "Dose" and "Amount" fields, which were left empty, defaulted to "Empty" and "0" respectively on the details screen.
- The new medication's status is displayed as "Added manually" in red text.