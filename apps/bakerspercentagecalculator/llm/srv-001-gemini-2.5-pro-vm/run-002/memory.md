---
app: Baker's Percentage Calculator
goal: The user wants to create and save a new recipe in the application.
outcome: success - The user successfully created a new recipe named "cake" and it appeared on the main list.
---

## Session Summary
The user started on the app's empty home screen and tapped the add button to create a new recipe. They filled in the recipe name, notes, and oven temperature on the "Add Recipe" screen. After saving, the app returned to the home screen, which now displayed the newly created "cake" recipe in the list.

## Steps

### 1. Add New Recipe — 2s
- **Screen:** Home
- **Action:** tap → `+` floating action button
- **Details:** The screen shows the text "Press the + button to add your first recipe!".
- **Result:** Navigated to the "Add Recipe" screen.
- **Confidence:** 1.0

### 2. Enter Recipe Name — 5s
- **Screen:** Add Recipe
- **Action:** type → `Recipe Name` text field
- **Details:** Typed "cake".
- **Result:** The text "cake" appeared in the "Recipe Name" field.
- **Confidence:** 1.0

### 3. Enter Notes — 8s
- **Screen:** Add Recipe
- **Action:** type → `Notes` text field
- **Details:** Typed "nuts".
- **Result:** The text "nuts" appeared in the "Notes" field.
- **Confidence:** 1.0

### 4. Enter Oven Temperature — 15s
- **Screen:** Add Recipe
- **Action:** type → `Oven Temp & Time` text field
- **Details:** Typed "400".
- **Result:** The text "400" appeared in the "Oven Temp & Time" field.
- **Confidence:** 1.0

### 5. Save Recipe — 16s
- **Screen:** Add Recipe
- **Action:** tap → `Save Recipe` button
- **Details:** The user saved the recipe with the name "cake", notes "nuts", and oven temp "400".
- **Result:** The app returned to the home screen, which now displayed a list item for the "cake" recipe.
- **Confidence:** 1.0

## Key Observations
- When creating a new recipe, the app automatically populates the ingredients list with "Flour" at 100.0%, which is the base for baker's percentage calculations.
- The default unit for ingredients is "grams".
- The user did not add or modify any ingredients, only the recipe name and optional notes/temp fields.