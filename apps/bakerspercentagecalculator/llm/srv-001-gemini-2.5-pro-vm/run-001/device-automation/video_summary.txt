---
app: Baker's Percentage Calculator
goal: The user wants to create and save a new recipe in the application.
outcome: success — The user successfully created a new recipe which was then displayed on the main screen.
---

## Session Summary
The user started on the app's empty home screen and tapped the add button to navigate to the recipe creation screen. They entered a recipe name, notes, and oven temperature. After saving the recipe, they were returned to the home screen, where the newly created recipe was now listed.

## Steps

### 1. App Launch — 0s
- **Screen:** Home
- **Action:** launch → `Baker's Percentage Calculator`
- **Details:** The screen is empty and displays the message "Press the + button to add your first recipe!".
- **Result:** The application's main screen is displayed.
- **Confidence:** 1.0

### 2. Navigate to Add Recipe — 2s
- **Screen:** Home
- **Action:** tap → `+` button
- **Details:** The floating action button in the bottom-right corner.
- **Result:** The user is taken to a new screen to create a recipe.
- **Confidence:** 1.0

### 3. Enter Recipe Name — 4s
- **Screen:** Add Recipe
- **Action:** type → `Recipe Name` field
- **Details:** "cake"
- **Result:** The text "cake" is entered into the recipe name field.
- **Confidence:** 1.0

### 4. Enter Notes — 8s
- **Screen:** Add Recipe
- **Action:** type → `Notes (e.g., seeds, nuts)` field
- **Details:** "nuts"
- **Result:** The text "nuts" is entered into the notes field.
- **Confidence:** 1.0

### 5. Enter Oven Details — 15s
- **Screen:** Add Recipe
- **Action:** type → `Oven Temp & Time` field
- **Details:** "400"
- **Result:** The text "400" is entered into the oven temp and time field.
- **Confidence:** 1.0

### 6. Save Recipe — 16s
- **Screen:** Add Recipe
- **Action:** tap → `Save Recipe` button
- **Details:** N/A
- **Result:** The app saves the recipe and navigates back to the home screen, which now displays a card for the "cake" recipe.
- **Confidence:** 1.0

## Key Observations
- When creating a new recipe, the app pre-populates the ingredients list with "Flour" at 100.0%, which is the standard for baker's percentage.
- The saved recipe on the home screen includes a share icon and a delete icon.