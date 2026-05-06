---
app: Simple Notes
goal: The user wants to create, add items to, and then delete a checklist.
outcome: success - The user successfully created, edited, and deleted the checklist note.
---

## Session Summary
The user started on the empty main screen of the "Simple Notes" app. They created a new checklist, titled it "grocery list," and added two items: "eggs" and "milk." After saving and returning to the main screen, they selected the note and deleted it locally, successfully returning the app to its initial empty state.

## Steps

### 1. Initiate New Note Creation — 2s
- **Screen:** Simple Notes (Main Screen)
- **Action:** tap → `+` floating action button
- **Details:** The screen initially shows "No notes yet".
- **Result:** A menu with "Text Note" and "Checklist" options appears.

### 2. Select Checklist Type — 3s
- **Screen:** Simple Notes (Main Screen)
- **Action:** tap → `Checklist` button
- **Details:** The user chooses to create a checklist over a text note.
- **Result:** The app navigates to the "New List" screen.

### 3. Title the Checklist — 8s
- **Screen:** New List
- **Action:** type → `Title` text field
- **Details:** The user types "grocery list".
- **Result:** The title "grocery list" is entered into the title field.

### 4. Add First Item — 11s
- **Screen:** New List
- **Action:** type → `New item...` text field
- **Details:** The user types "eggs".
- **Result:** The first checklist item "eggs" is created.

### 5. Save the New List — 12s
- **Screen:** New List
- **Action:** back → `Back` arrow icon
- **Details:** The user navigates back from the note creation screen.
- **Result:** The app returns to the main screen, which now displays the newly created "grocery list" note.

### 6. Re-open the List to Edit — 14s
- **Screen:** Simple Notes (Main Screen)
- **Action:** tap → `grocery list` note card
- **Details:** The user taps the note they just created.
- **Result:** The app navigates to the "Edit List" screen, showing the existing list.

### 7. Add Second Item — 19s
- **Screen:** Edit List
- **Action:** type → `New item...` text field
- **Details:** The user first taps "Add item" and then types "milk".
- **Result:** A second checklist item, "milk", is added to the list.

### 8. Save Edited List — 20s
- **Screen:** Edit List
- **Action:** back → `Back` arrow icon
- **Details:** The user navigates back from the edit screen.
- **Result:** The app returns to the main screen, where the note preview now shows both "eggs" and "milk".

### 9. Select Note for Deletion — 23s
- **Screen:** Simple Notes (Main Screen)
- **Action:** long_press → `grocery list` note card
- **Details:** The user long-presses the note to enter selection mode.
- **Result:** The app enters a multi-select mode, indicated by a checkmark on the note and a new top app bar showing "1 selected" and a delete icon.

### 10. Initiate Deletion — 25s
- **Screen:** Simple Notes (Selection Mode)
- **Action:** tap → `Delete` (trash can) icon
- **Details:** The user taps the delete icon in the top app bar.
- **Result:** A "Delete note?" confirmation dialog appears from the bottom of the screen.

### 11. Confirm Local Deletion — 27s
- **Screen:** Simple Notes (Main Screen)
- **Action:** tap → `Delete local only` button
- **Details:** The user chooses to delete the note only from the device, not the server.
- **Result:** The note is removed from the main screen, and a toast notification "1 note deleted locally" appears briefly. The app returns to the "No notes yet" state.

## Key Observations
- The app supports both simple text notes and checklists.
- The deletion process distinguishes between deleting a note "locally" and "everywhere (also server)," indicating a cloud sync or backup feature.
- The "Delete everywhere" option is visually highlighted, suggesting it is the primary or recommended action.
- A toast message confirms the successful local deletion of the note.