---
app: Baker's Percentage Calculator
goal: The user wants to back up their saved recipes to a file on their device.
outcome: success - The user successfully created and saved a backup file.
---

## Session Summary
The user started on the main screen of the Baker's Percentage Calculator, which listed a single recipe. They opened the overflow menu, selected the "Backup Recipes" option, and used the system file manager to save the backup file. The process completed successfully, confirmed by a toast message on the main screen.

## Steps

### 1. Open Overflow Menu — 1s
- **Screen:** Baker's Percentage Calculator
- **Action:** `tap` → `three-dot menu icon`
- **Details:** The screen shows one recipe named "cake".
- **Result:** A dropdown menu appears with options: "Import Recipe", "Backup Recipes", and "Restore Recipes".
- **Confidence:** 1.0

### 2. Select Backup Option — 3s
- **Screen:** Baker's Percentage Calculator
- **Action:** `tap` → `Backup Recipes`
- **Details:** The user selects the second option from the menu.
- **Result:** The system file manager opens, defaulting to the "Downloads" folder.
- **Confidence:** 1.0

### 3. Save Backup File — 5s
- **Screen:** Downloads
- **Action:** `tap` → `SAVE` button
- **Details:** The default filename "bakers_percentage_backup.j" is used.
- **Result:** The app returns to the main screen and a toast message "Backup successful!" appears at the bottom.
- **Confidence:** 1.0

## Key Observations
- The app contained a single recipe named "cake" at the time of backup.
- The backup file was saved with the name `bakers_percentage_backup.j`. The file extension is `.j`.
- The backup process was confirmed with a "Backup successful!" toast notification.