---
app: Bill Splitter
goal: The user wants to reset all expenses and then explore the app's settings.
outcome: success - The user successfully reset the bill and interacted with the settings menu.
---

## Session Summary
The user started on the main bill screen, which displayed a list of expenses. They navigated to the overflow menu and chose to reset the bill, confirming the action in a pop-up dialog. After successfully clearing the expenses, the user opened the settings menu, toggled two options off, and then closed the menu to return to the cleared main screen.

## Steps

### 1. Open Overflow Menu — 0s
- **Screen:** Main Bill Screen
- **Action:** tap → Overflow Menu Icon (three dots)
- **Details:** The screen shows a "Global Bill" of $0.00 and a list of users and expenses.
- **Result:** A dropdown menu appeared with options "Modify Bill", "Reset Bill", and "Settings".
- **Confidence:** 1.0

### 2. Select Reset Bill — 1s
- **Screen:** Main Bill Screen
- **Action:** tap → "Reset Bill" menu item
- **Details:** The user selects the "Reset Bill" option from the overflow menu.
- **Result:** A confirmation dialog appeared.
- **Confidence:** 1.0

### 3. Confirm Reset — 3s
- **Screen:** "Are You Sure?" Dialog
- **Action:** tap → "Reset" button
- **Details:** The dialog text reads "This will remove all expenses."
- **Result:** The dialog closed, and the expense list on the main screen was cleared. The "$689.00" expense is no longer visible.
- **Confidence:** 1.0

### 4. Open Settings — 5s
- **Screen:** Main Bill Screen
- **Action:** tap → "Settings" menu item
- **Details:** The user re-opened the overflow menu (action not shown) and tapped "Settings".
- **Result:** A settings dialog appeared in the middle of the screen.
- **Confidence:** 0.9

### 5. Toggle First Setting Off — 7s
- **Screen:** Settings Dialog
- **Action:** tap → Left Toggle Switch
- **Details:** The user taps the first of two unnamed toggle switches at the top of the dialog.
- **Result:** The left toggle switch moved to the "off" position.
- **Confidence:** 1.0

### 6. Toggle Second Setting Off — 9s
- **Screen:** Settings Dialog
- **Action:** tap → Right Toggle Switch
- **Details:** The user taps the second toggle switch.
- **Result:** The right toggle switch moved to the "off" position.
- **Confidence:** 1.0

### 7. Close Settings — 10s
- **Screen:** Settings Dialog
- **Action:** tap → Area outside the dialog
- **Details:** The user taps the background to dismiss the settings dialog.
- **Result:** The settings dialog closed, returning the user to the main bill screen.
- **Confidence:** 1.0

## Key Observations
- The app provides a "Reset Bill" function that clears all expenses after user confirmation.
- The settings menu is presented as a modal dialog rather than a full-screen view.
- The app settings include configurations for Currency (US Dollar), Taxes, and Discount.
- A tax rate of 14.975% is visible in the settings.
- The settings dialog contains two unnamed toggle switches at the top, suggesting their function might not be immediately obvious to a user.