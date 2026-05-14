---
app: Baker's Percentage Calculator
goal: The user wants to create and save a new baking recipe.
outcome: success - The recipe was successfully created and appeared on the main list.
---

## Session Summary
The user started on the app's empty main screen and tapped the add button to create a new recipe. They named the recipe "cake", adjusted the default flour amount, and added a new ingredient named "nuts" without specifying a quantity. After saving, the app returned to the main screen, which now correctly displayed the newly created "cake" recipe.

## Steps

### 1. App Launch — 0s
- **Screen:** Main Screen
- **Action:** launch → `App Icon`
- **Details:** The screen is empty with the message "Press the + button to add your first recipe!".
- **Result:** The application's main screen is displayed.
- **Confidence:** 1.0

### 2. Open New Recipe Form — 1s
- **Screen:** Main Screen
- **Action:** tap → `+` button (top right)
- **Details:** The user taps the floating action button to add a recipe.
- **Result:** The app navigates to the "New Recipe" screen.
- **Confidence:** 1.0

### 3. Enter Recipe Name — 4s
- **Screen:** New Recipe
- **Action:** type → `Recipe Name` field
- **Details:** Typed "cake".
- **Result:** The text "cake" is entered into the recipe name field.
- **Confidence:** 1.0

### 4. Edit Flour Amount — 12s
- **Screen:** New Recipe
- **Action:** type → `grams` field for "Flour"
- **Details:** The user changed the default value from "100.0" to "50.0".
- **Result:** The gram amount for the "Flour" ingredient is updated to "50.0".
- **Confidence:** 1.0

### 5. Add New Ingredient — 14s
- **Screen:** New Recipe
- **Action:** tap → `+` button (in Ingredients section)
- **Details:** The user taps the plus button to add another ingredient to the list.
- **Result:** A new, empty ingredient row appears below the "Flour" ingredient.
- **Confidence:** 1.0

### 6. Name New Ingredient — 16s
- **Screen:** New Recipe
- **Action:** type → `Ingredient Name` field (for the new ingredient)
- **Details:** Typed "nuts".
- **Result:** The text "nuts" is entered as the name for the new ingredient.
- **Confidence:** 1.0

### 7. Save Recipe — 22s
- **Screen:** New Recipe
- **Action:** tap → `Save Recipe` button
- **Details:** The user saves the form with the entered details.
- **Result:** The app navigates back to the main screen, which now shows a list item for "cake".
- **Confidence:** 1.0

## Key Observations
- When creating a new recipe, the form pre-populates with a default "Flour" ingredient set to "100.0" grams.
- The user was able to save the recipe even though the newly added "nuts" ingredient had no gram amount specified. The quantity field for new ingredients appears to be optional or has a default value of zero.