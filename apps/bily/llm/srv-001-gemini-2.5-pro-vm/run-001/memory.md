---
app: Global Bill
goal: The user wants to clear all existing expenses from the bill and then adjust the bill's settings.
outcome: success - The user successfully reset the bill and then modified the tax setting.
---

## Session Summary
The user started on the main bill screen, which displayed a total of $111.00. They navigated to the overflow menu and chose to reset the bill, which cleared all expenses and zeroed out all balances after a confirmation. The user then re-entered the menu, opened the "Modify Bill" settings, and successfully disabled the taxes option.

## Steps

### 1. Open Overflow Menu — 2s
- **Screen:** Global Bill
- **Action:** tap → `three-dot menu icon`
- **Details:** The screen shows a "Global Bill" of $111.00.
- **Result:** A context menu appeared with options "Modify Bill", "Reset Bill", and "Settings".
- **Confidence:** 1.0

### 2. Select Reset Bill — 5s
- **Screen:** Global Bill
- **Action:** tap → `Reset Bill`
- **Details:** The user selects the "Reset Bill" option from the context menu.
- **Result:** An "Are You Sure?" confirmation dialog appeared, warning that this action will remove all expenses.
- **Confidence:** 1.0

### 3. Confirm Bill Reset — 6s
- **Screen:** Are You Sure? Dialog
- **Action:** tap → `Reset` button
- **Details:** The user confirms the action to reset the bill.
- **Result:** The dialog closed. The "Global Bill" total, user balances, and expenses list were all cleared and set to $0.00.
- **Confidence:** 1.0

### 4. Open Overflow Menu Again — 8s
- **Screen:** Global Bill
- **Action:** tap → `three-dot menu icon`
- **Details:** The bill is now empty.
- **Result:** The context menu reappeared.
- **Confidence:** 1.0

### 5. Open Modify Bill Settings — 9s
- **Screen:** Global Bill
- **Action:** tap → `Modify Bill`
- **Details:** The user selects the "Modify Bill" option from the context menu.
- **Result:** A settings dialog appeared with options for "Currency", "Taxes", and "Discount".
- **Confidence:** 1.0

### 6. Disable Taxes — 10s
- **Screen:** Modify Bill Dialog
- **Action:** tap → `Taxes toggle switch`
- **Details:** The toggle switch for "Taxes" was initially in the 'on' state.
- **Result:** The "Taxes" toggle switch moved to the 'off' position.
- **Confidence:** 1.0

## Key Observations
- The initial state of the bill was a total of $111.00, split between user "abc" ($81.50) and "xyz" ($29.50).
- Resetting the bill is a destructive action that requires user confirmation.
- The "Modify Bill" settings reveal a default tax rate of 14.975%.