---
app: Baker's Percentage Calculator
goal: To import a recipe from a previously created backup file.
outcome: success - The app displayed a "Recipe imported" confirmation toast.
---

## Session Summary
The user started on the main screen of the "Baker's Percentage Calculator" app. They opened the overflow menu, selected the "Import Recipe" option, and were taken to the system file picker. After selecting a `.json` backup file from their downloads, the app returned to the main screen and displayed a toast message confirming the successful import.

## Steps

### 1. Open Overflow Menu — 1s
- **Screen:** Main Screen
- **Action:** tap → Overflow Menu Icon (three vertical dots)
- **Details:** The main screen is titled "Baker's Percentage Calculator" and appears to be empty.
- **Result:** A dropdown menu appeared with options: "Import Recipe", "Backup Recipes", "Restore Recipes".
- **Confidence:** 1.0

### 2. Select Import Option — 3s
- **Screen:** Main Screen with Menu
- **Action:** tap → `Import Recipe`
- **Details:** The user selects the first option from the overflow menu.
- **Result:** The native Android file picker interface opened, displaying the "Downloads" folder.
- **Confidence:** 1.0

### 3. Select Backup File — 7s
- **Screen:** Downloads (File Picker)
- **Action:** tap → `bakers_percentage_backup.json`
- **Details:** The user selects a JSON file from the list of downloaded files.
- **Result:** The file picker closed, and the view returned to the app's main screen.
- **Confidence:** 1.0

### 4. Confirm Import — 9s
- **Screen:** Main Screen
- **Action:** wait → `(system feedback)`
- **Details:** A toast notification appeared at the bottom of the screen.
- **Result:** The toast message "Recipe imported" was displayed briefly.
- **Confidence:** 1.0

## Key Observations
- The app supports importing data from a `.json` file format.
- The import functionality is accessed through an overflow menu.
- A system toast message, "Recipe imported", is used to confirm a successful import operation.
- The app utilizes the standard Android system file picker for selecting the import file.