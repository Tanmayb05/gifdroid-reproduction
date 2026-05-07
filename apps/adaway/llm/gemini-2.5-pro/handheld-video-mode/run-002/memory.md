---
app: AdAway
goal: To add a new hostname to the ad blocker's whitelist.
outcome: success - The user successfully added "pol" to the allowed list and verified the change.
---

## Session Summary
The user started on the AdAway main screen and navigated to the "Allowed" list. They used the search and add functionality to add the hostname "pol" to the whitelist. After applying the configuration change, they navigated back to the main screen, where the "Allowed" count had updated to 1, and then returned to the list to confirm the new entry was present.

## Steps

### 1. Navigate to Allowed List — 2s
- **Screen:** AdAway Main Screen
- **Action:** tap → `Allowed` button
- **Details:** The "Allowed" count is 0.
- **Result:** Navigated to the "Your lists" screen.
- **Confidence:** 1.0

### 2. Initiate Search — 3s
- **Screen:** Your lists
- **Action:** tap → `Search` icon
- **Details:** The list is currently empty.
- **Result:** A "Search hostname..." input field appears at the top of the screen.
- **Confidence:** 1.0

### 3. Add New Host — 12s
- **Screen:** Your lists (Search)
- **Action:** tap → `+` floating action button
- **Details:** The user had previously typed "uhkh" into the search bar.
- **Result:** An "Add host to whitelist" dialog appears.
- **Confidence:** 1.0

### 4. Enter Hostname — 25s
- **Screen:** Your lists (Search)
- **Action:** type → `Hostname` input field
- **Details:** Typed "pol" into the dialog's input field.
- **Result:** The text "pol" is visible in the field.
- **Confidence:** 1.0

### 5. Confirm Add Host — 27s
- **Screen:** Your lists (Search)
- **Action:** tap → `ADD` button
- **Details:** The dialog contains the hostname "pol".
- **Result:** The dialog closes and a banner appears with the message: "Your configuration changed. You need to apply it".
- **Confidence:** 1.0

### 6. Apply Configuration — 29s
- **Screen:** Your lists (Search)
- **Action:** tap → `Apply` button
- **Details:** Tapped the "Apply" button on the configuration change banner.
- **Result:** The banner text changes to "Applying new configuration...".
- **Confidence:** 1.0

### 7. Return to Main Screen — 35s
- **Screen:** Your lists
- **Action:** back → `Back` arrow
- **Details:** The user tapped the back arrow twice to exit the search view and then the list view.
- **Result:** Returned to the AdAway main screen.
- **Confidence:** 1.0

### 8. Verify Change on Main Screen — 39s
- **Screen:** AdAway Main Screen
- **Action:** tap → `Allowed` button
- **Details:** The "Allowed" count is now "1".
- **Result:** Navigated back to the "Your lists" screen.
- **Confidence:** 1.0

### 9. Final Verification — 41s
- **Screen:** Your lists
- **Action:** wait →
- **Details:** The list now contains one entry: "pol".
- **Result:** The user has successfully verified that the hostname was added to the whitelist.
- **Confidence:** 1.0

## Key Observations
- After adding a host to the whitelist, the user must perform a separate "Apply" action for the change to take effect.
- The main dashboard's "Allowed" counter correctly updated from 0 to 1 after the configuration was applied.
- The app provides clear feedback via a banner when a configuration change is pending and when it is being applied.