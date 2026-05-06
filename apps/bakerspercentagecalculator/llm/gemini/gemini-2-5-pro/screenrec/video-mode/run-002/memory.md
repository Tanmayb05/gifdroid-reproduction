---
app: Baker's Percentage Calculator
goal: The user wants to create and save a new recipe with a name, notes, and oven temperature.
outcome: success - The new recipe was created and displayed on the main screen.
---

## Session Summary
The user started on the app's empty home screen and tapped the add button to open the new recipe form. They proceeded to fill in the recipe name as "cake", added "nuts" to the notes, and entered "400" for the oven temperature. After saving, the app returned to the home screen, which now listed the newly created "cake" recipe.

## Steps

### 1. Add New Recipe — 2s
- **Screen:** Home
- **Action:** tap → `+` floating action button
- **Details:** The screen shows the text "Press the + button to add your first recipe!".
- **Result:** Navigated to the new recipe creation screen.
- **Confidence:** 1.0

### 2. Enter Recipe Name — 5s
- **Screen:** New Recipe
- **Action:** type → `Recipe Name` text input
- **Details:** Typed "cake".
- **Result:** The text "cake" appeared in the input field.
- **Confidence:** 1.0

### 3. Enter Notes — 8s
- **Screen:** New Recipe
- **Action:** type → `Notes (e.g., seeds, nuts)` text input
- **Details:** Typed "nuts".
- **Result:** The text "nuts" appeared in the input field.
- **Confidence:** 1.0

### 4. Enter Oven Temperature — 15s
- **Screen:** New Recipe
- **Action:** type → `Oven Temp & Time` text input
- **Details:** Typed "400".
- **Result:** The text "400" appeared in the input field.
- **Confidence:** 1.0

### 5. Save Recipe — 16s
- **Screen:** New Recipe
- **Action:** tap → `Save Recipe` button
- **Details:** The form was filled with "cake", "nuts", and "400".
- **Result:** The app returned to the home screen, which now displays a list item for the "cake" recipe.
- **Confidence:** 1.0

## Key Observations
- The new recipe form automatically includes a default ingredient, "Flour", set to 100%. The user did not modify this.
- The default unit for ingredients is "grams", which the user also did not change.
- The final recipe list item includes a share icon and a delete icon.