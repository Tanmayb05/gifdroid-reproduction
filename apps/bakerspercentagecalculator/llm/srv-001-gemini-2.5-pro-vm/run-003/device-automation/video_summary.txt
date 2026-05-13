---
app: Baker's Percentage Calculator
goal: The user wants to add a new recipe for a cake to the app.
outcome: success — The recipe was successfully created and displayed on the main screen.
---

## Session Summary
The user started on the app's empty home screen and tapped the add button to create a new recipe. They navigated to the "Add Recipe" form, entered a name ("cake"), notes ("nuts"), and oven temperature ("400"). After saving, the app returned to the home screen, which now listed the newly created "cake" recipe.

## Steps

### 1. Tap Add Recipe — 2s
- **Screen:** Main Screen (Empty State)
- **Action:** `tap` → `+` floating action button
- **Details:** The screen displays the message "Press the + button to add your first recipe!".
- **Result:** Navigated to the "Add Recipe" screen.
- **Confidence:** 1.0

### 2. Enter Recipe Name — 4s
- **Screen:** Add Recipe
- **Action:** `type` → `Recipe Name` input field
- **Details:** Typed "cake".
- **Result:** The text "cake" is entered into the field.
- **Confidence:** 1.0

### 3. Enter Notes — 7s
- **Screen:** Add Recipe
- **Action:** `type` → `Notes` input field
- **Details:** Typed "nuts".
- **Result:** The text "nuts" is entered into the field.
- **Confidence:** 1.0

### 4. Enter Oven Temp & Time — 10s
- **Screen:** Add Recipe
- **Action:** `type` → `Oven Temp & Time` input field
- **Details:** Typed "400".
- **Result:** The text "400" is entered into the field.
- **Confidence:** 1.0

### 5. Save Recipe — 16s
- **Screen:** Add Recipe
- **Action:** `tap` → `Save Recipe` button
- **Details:** The form is filled with the recipe details.
- **Result:** The app navigates back to the main screen, which now displays a list item for the "cake" recipe.
- **Confidence:** 1.0

## Key Observations
- When creating a new recipe, the form automatically populates with a default ingredient "Flour" at 100.0%.
- The default unit for a new recipe is "grams".
- The user did not add or modify any ingredients besides the default "Flour".
- The saved recipe on the main screen includes a share icon and a delete icon.