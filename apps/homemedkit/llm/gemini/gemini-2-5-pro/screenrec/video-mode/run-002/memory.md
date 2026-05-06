---
app: Medicine Tracker
goal: To manually add a new medication to the user's inventory.
outcome: success - The user successfully filled out the form and saved the new medication, landing on its details page.
---

## Session Summary
The user started on the main "Medicine" list screen and initiated the process to add a new medication. They tapped the add button, which took them to a form where they entered the product name, expiration date, package opened date, display name, release form, and a comment. After successfully submitting the form, the app created the new medication and displayed its details.

## Steps

### 1. Open Add Options — 2s
- **Screen:** Medicine List
- **Action:** `tap` → `+` floating action button
- **Details:** The main list shows three existing medications: "dasd", "ert", and "uyvhy".
- **Result:** Two new buttons, "Scan" and "Add", appear above the `+` button.

### 2. Navigate to Add Form — 4s
- **Screen:** Medicine List
- **Action:** `tap` → `Add` button
- **Result:** The app navigates to a blank form for adding a new medication.

### 3. Enter Product Name — 6s
- **Screen:** Add Medication Form
- **Action:** `type` → `Product name` field
- **Details:** Typed "medA".

### 4. Attempt to Select Group — 9s
- **Screen:** Add Medication Form
- **Action:** `tap` → `Group` field
- **Result:** A dialog titled "Medication groups" appears, stating "There are no groups found. You can add groups in the application settings."

### 5. Close Group Dialog — 12s
- **Screen:** Add Medication Form (with dialog)
- **Action:** `tap` → `Save` button in the dialog
- **Result:** The dialog closes, and the user returns to the form. The "Group" field remains empty.

### 6. Set Expiration Date — 14s
- **Screen:** Add Medication Form
- **Action:** `tap` → `Exp. date` field
- **Details:** A month/year picker opens, defaulting to May 2026.
- **Result:** The user taps "Save", and the field is populated with "May 31, 2026".

### 7. Set Package Opened Date — 19s
- **Screen:** Add Medication Form
- **Action:** `tap` → `Package opened` field
- **Details:** A full calendar date picker opens. The user selects the 22nd.
- **Result:** The user taps "Save", and the field is populated with "May 22, 2026".

### 8. Enter Display Name — 25s
- **Screen:** Add Medication Form
- **Action:** `type` → `Display name` field
- **Details:** Typed "medA".

### 9. Enter Release Form — 30s
- **Screen:** Add Medication Form
- **Action:** `type` → `Release form` field
- **Details:** Typed "medB".

### 10. Enter Comment — 37s
- **Screen:** Add Medication Form
- **Action:** `type` → `Comment` field
- **Details:** Typed "abc".

### 11. Save New Medication — 39s
- **Screen:** Add Medication Form
- **Action:** `tap` → `✓` (check) icon in the top app bar
- **Result:** The form is submitted, and the app navigates to the details screen for the newly created medication.

## Key Observations
- When trying to assign a medication group, the app displayed a dialog indicating that no groups have been created yet and must be added in the settings.
- The "Exp. date" picker automatically selected the last day of the chosen month (May 31, 2026).
- The final details screen shows the "Group" as "Unspecified" and the "Status" as "Added manually".
- The "Dose" and "Amount" fields were not filled in, resulting in values of "Empty" and "0" on the details page.