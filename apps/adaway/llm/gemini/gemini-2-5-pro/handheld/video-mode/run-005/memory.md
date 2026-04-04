---
app: AdAway
goal: To add a new hostname to the whitelist (allowed list).
outcome: success — The user successfully added a hostname to the allowed list and verified its presence.
---

## Session Summary
The user started on the AdAway home screen and navigated to the "Allowed" list. They then added a new hostname, "pol", to the whitelist via a dialog. After adding the entry, they applied the new configuration and navigated back to the "Allowed" list to confirm that the hostname had been successfully saved.

## Steps

### 1. Navigate to Allowed List — 2s
- **Screen:** AdAway Home
- **Action:** tap → `Allowed` button
- **Details:** The "Allowed" count is 0.
- **Result:** Navigated to the "Your lists" screen.
- **Confidence:** 1.0

### 2. Initiate Add Host — 5s
- **Screen:** Your lists
- **Action:** tap → `+` (add) button
- **Details:** The list is currently empty.
- **Result:** The "Add host to whitelist" dialog appeared.
- **Confidence:** 1.0

### 3. Enter Hostname — 26s
- **Screen:** Your lists
- **Action:** type → `Hostname` text field
- **Details:** Typed "pol" into the field.
- **Result:** The text "pol" is visible in the input field.
- **Confidence:** 1.0

### 4. Add Host to List — 27s
- **Screen:** Your lists
- **Action:** tap → `ADD` button
- **Details:** Submitting the "Add host to whitelist" dialog.
- **Result:** A banner appeared with the message "Your configuration changed. You need to apply it".
- **Confidence:** 1.0

### 5. Apply Configuration — 29s
- **Screen:** Your lists
- **Action:** tap → `Apply` button
- **Details:** The banner prompts the user to apply the change.
- **Result:** A loading message "Applying new configuration..." appeared briefly.
- **Confidence:** 1.0

### 6. Return to Home Screen — 36s
- **Screen:** Your lists
- **Action:** back → `Back arrow` icon
- **Details:** User taps the back arrow twice to exit the list and search views.
- **Result:** Returned to the AdAway home screen.
- **Confidence:** 1.0

### 7. Verify Addition — 39s
- **Screen:** AdAway Home
- **Action:** tap → `Allowed` button
- **Details:** The "Allowed" count is now 1.
- **Result:** Navigated to the "Your lists" screen.
- **Confidence:** 1.0

### 8. View Updated List — 41s
- **Screen:** Your lists
- **Action:** wait → `None`
- **Details:** The list now contains the entry "pol".
- **Result:** The user successfully verified that the hostname was added to the list.
- **Confidence:** 1.0

## Key Observations
- The app requires a two-step process to modify lists: first, add the entry, and second, explicitly tap an "Apply" button to save the configuration change.
- The home screen dashboard correctly updated the "Allowed" count from 0 to 1 after the configuration was applied.
- The app version is 6.1.4, as seen on the home screen.