---
app: Simple Notes
goal: To create, edit, and then delete a checklist note.
outcome: success - The user successfully created, added items to, and deleted a checklist note.
---

## Session Summary
The user started on the empty main screen of the "Simple Notes" app. They created a new checklist, gave it a title, and added an initial item. After saving and returning to the main screen, they reopened the note to add a second item. Finally, they selected the note and deleted it locally, returning the app to its initial empty state.

## Steps

### 1. Open New Note Menu — 2s
- **Screen:** Simple Notes (Main)
- **Action:** tap → `+` FAB (Floating Action Button)
- **Details:** The main screen shows "No notes yet".
- **Result:** A menu with "Text Note" and "Checklist" options appears.

### 2. Create New Checklist — 3s
- **Screen:** Simple Notes (Main)
- **Action:** tap → `Checklist` button
- **Details:** The user selects the checklist option from the menu.
- **Result:** The user is navigated to the "New List" screen.

### 3. Add List Title — 8s
- **Screen:** New List
- **Action:** type → `Title` text field
- **Details:** Typed text: "grocery list"
- **Result:** The title "grocery list" is entered into the title field.

### 4. Add First Item — 11s
- **Screen:** New List
- **Action:** type → `New item...` text field
- **Details:** Typed text: "eggs"
- **Result:** The first checklist item "eggs" is created.

### 5. Save and Return to Main — 13s
- **Screen:** New List
- **Action:** back → `Back arrow` icon
- **Details:** The user navigates back from the new list creation screen.
- **Result:** The user is returned to the main "Simple Notes" screen, which now displays a preview of the "grocery list" note.

### 6. Re-open Note to Edit — 14s
- **Screen:** Simple Notes (Main)
- **Action:** tap → `grocery list` note card
- **Details:** The note card shows the title and the first item "eggs".
- **Result:** The user is navigated to the "Edit List" screen for the selected note.

### 7. Add Second Item — 19s
- **Screen:** Edit List
- **Action:** type → `New item...` text field
- **Details:** Typed text: "milk"
- **Result:** A second checklist item "milk" is added to the list.

### 8. Save Edited Note — 20s
- **Screen:** Edit List
- **Action:** back → `Back arrow` icon
- **Details:** The user navigates back from the edit screen.
- **Result:** The user is returned to the main screen. The note preview now shows both "eggs" and "milk".

### 9. Select Note for Deletion — 23s
- **Screen:** Simple Notes (Main)
- **Action:** long_press → `grocery list` note card
- **Details:** The user enters selection mode.
- **Result:** The note card is selected, indicated by a checkmark, and a delete icon appears in the top app bar.

### 10. Initiate Deletion — 25s
- **Screen:** Simple Notes (Main - Selection Mode)
- **Action:** tap → `Delete` (trash can) icon
- **Details:** The header shows "1 selected".
- **Result:** A "Delete note?" bottom sheet dialog appears.

### 11. Confirm Local Deletion — 27s
- **Screen:** Simple Notes (Main)
- **Action:** tap → `Delete local only` button
- **Details:** The dialog offers "Delete everywhere (also server)" and "Delete local only".
- **Result:** The note is deleted, the screen returns to the "No notes yet" state, and a toast message "1 note deleted locally" appears briefly.

## Key Observations
- The app supports two types of notes: "Text Note" and "Checklist".
- The deletion process distinguishes between a local-only deletion and a server-synced deletion ("Delete everywhere").
- The "Delete everywhere (also server)" option is visually emphasized (pink background), suggesting it is the primary or recommended action.
- A confirmation toast message appears at the bottom of the screen after a successful local deletion.