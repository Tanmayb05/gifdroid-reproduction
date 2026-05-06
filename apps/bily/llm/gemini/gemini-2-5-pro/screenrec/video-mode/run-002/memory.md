---
app: Global Bill
goal: To reset all expenses on the bill and then modify the bill's settings.
outcome: success - The user successfully cleared all expenses and then disabled the tax setting.
---

## Session Summary
The user began on the main bill screen, which displayed a total of $111.00. They navigated to the overflow menu and chose to reset the bill, confirming this action in a pop-up dialog. After the bill was successfully cleared, they re-opened the menu, selected "Modify Bill," and disabled the "Taxes" toggle before dismissing the settings dialog and returning to the empty bill screen.

## Steps

### 1. Open Overflow Menu — 2s
- **Screen:** Global Bill
- **Action:** `tap` → `three-dot menu icon`
- **Details:** The screen shows a "Global Bill" of $111.00.
- **Result:** A context menu appeared with options "Modify Bill", "Reset Bill", and "Settings".
- **Confidence:** 1.0

### 2. Select Reset Bill — 4s
- **Screen:** Global Bill
- **Action:** `tap` → `Reset Bill`
- **Details:** The user selects the "Reset Bill" option from the context menu.
- **Result:** An "Are You Sure?" confirmation dialog appeared, warning that this action will remove all expenses.
- **Confidence:** 1.0

### 3. Confirm Bill Reset — 6s
- **Screen:** Global Bill
- **Action:** `tap` → `Reset`
- **Details:** The user confirms the action in the "Are You Sure?" dialog.
- **Result:** The dialog closed. The "Global Bill" total, user balances, and the expenses list were all reset to $0.00 and empty, respectively.
- **Confidence:** 1.0

### 4. Open Overflow Menu Again — 8s
- **Screen:** Global Bill
- **Action:** `tap` → `three-dot menu icon`
- **Details:** The bill is now at $0.00.
- **Result:** The same context menu appeared again.
- **Confidence:** 1.0

### 5. Select Modify Bill — 9s
- **Screen:** Global Bill
- **Action:** `tap` → `Modify Bill`
- **Details:** The user selects the "Modify Bill" option from the context menu.
- **Result:** A dialog appeared with settings for "Currency", "Taxes", and "Discount".
- **Confidence:** 1.0

### 6. Disable Taxes — 10s
- **Screen:** Global Bill
- **Action:** `tap` → `Taxes toggle`
- **Details:** The "Taxes" toggle was initially in the 'on' state.
- **Result:** The "Taxes" toggle switched to the 'off' state.
- **Confidence:** 1.0

### 7. Dismiss Settings Dialog — 12s
- **Screen:** Global Bill
- **Action:** `tap` → `(outside the dialog)`
- **Details:** The user taps on the dimmed background area to close the dialog.
- **Result:** The "Modify Bill" dialog closed, and the user returned to the main "Global Bill" screen.
- **Confidence:** 1.0

## Key Observations
- The app provides a confirmation dialog for destructive actions like resetting the bill.
- The "Modify Bill" settings reveal a default tax rate of 14.975%.
- Resetting the bill successfully clears the total amount, individual user balances, and the list of expenses.