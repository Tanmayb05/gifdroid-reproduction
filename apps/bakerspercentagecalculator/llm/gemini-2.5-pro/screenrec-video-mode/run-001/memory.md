---
app: Baker's Percentage Calculator
goal: To add a new recipe for a cake to the application.
outcome: success - The user successfully created and saved a new recipe, which appeared on the main list.
---

## Session Summary
The user launched the app to an empty home screen and tapped the add button to navigate to the "Add Recipe" form. They proceeded to fill in the recipe name, notes, and oven temperature. After saving, the app returned to the home screen, which now displayed the newly created "cake" recipe.

## Steps

### 1. Start Adding Recipe — 2s
- **Screen:** Home
- **Action:** tap → `+`
- **Details:** The screen shows the text "Press the + button to add your first recipe!".
- **Result:** Navigated to the "Add Recipe" screen.
- **Confidence:** 1.0

### 2. Enter Recipe Name — 5s
- **Screen:** Add Recipe
- **Action:** type → `Recipe Name`
- **Details:** Typed "cake".
- **Result:** The text "cake" was entered into the "Recipe Name" field.
- **Confidence:** 1.0

### 3. Enter Notes — 8s
- **Screen:** Add Recipe
- **Action:** type → `Notes (e.g., seeds, nuts)`
- **Details:** Typed "nuts".
- **Result:** The text "nuts" was entered into the "Notes" field.
- **Confidence:** 1.0

### 4. Enter Oven Details — 15s
- **Screen:** Add Recipe
- **Action:** type → `Oven Temp & Time`
- **Details:** Typed "400".
- **Result:** The text "400" was entered into the "Oven Temp & Time" field.
- **Confidence:** 1.0

### 5. Save Recipe — 16s
- **Screen:** Add Recipe
- **Action:** tap → `Save Recipe`
- **Result:** The recipe was saved, and the app navigated back to the home screen, which now displays a card for the "cake" recipe.
- **Confidence:** 1.0

## Key Observations
- When creating a new recipe, the app automatically adds "Flour" as the first ingredient at 100%, which is the standard base for baker's percentages.
- The default unit for recipes is "grams".
- The user did not add or modify any ingredients, only the recipe name, notes, and oven details.