---
app: AdAway
goal: To add a new hostname to the ad blocker's whitelist.
outcome: success - The hostname "pol" was successfully added to the "Allowed" list and verified.
---

## Session Summary
The user started on the AdAway home screen and navigated to the "Allowed" list. They used the add function to open a dialog and entered "pol" as a new hostname for the whitelist. After adding the entry, they applied the new configuration and then returned to the list to verify that "pol" was correctly added.

## Steps

### 1. Navigate to Allowed List — 1s
- **Screen:** AdAway Home
- **Action:** tap → "Allowed" button
- **Details:** The "Allowed" counter shows 0.
- **Result:** The app navigates to the "Your lists" screen, filtered to show allowed hosts.
- **Confidence:** 1.0

### 2. Initiate Add Host — 5s
- **Screen:** Your lists (Allowed)
- **Action:** tap → `+` (add) button
- **Result:** The "Add host to whitelist" dialog appears over the screen.
- **Confidence:** 1.0

### 3. Enter Hostname — 26s
- **Screen:** Your lists (Allowed) with "Add host to whitelist" dialog
- **Action:** type → "Hostname" input field
- **Details:** The user types the text "pol".
- **Result:** The text "pol" is visible in the input field.
- **Confidence:** 1.0

### 4. Confirm Add Host — 27s
- **Screen:** Your lists (Allowed) with "Add host to whitelist" dialog
- **Action:** tap → "ADD" button
- **Result:** The dialog closes and a banner appears at the bottom with the message: "Your configuration changed. You need to apply it".
- **Confidence:** 1.0

### 5. Apply Configuration — 29s
- **Screen:** Your lists (Allowed)
- **Action:** tap → "APPLY" button in the banner
- **Result:** A brief "Applying new configuration..." message appears, and the banner disappears.
- **Confidence:** 1.0

### 6. Navigate Back to Home — 35s
- **Screen:** Your lists (Allowed)
- **Action:** tap → Back arrow
- **Result:** The app returns to the AdAway home screen.
- **Confidence:** 1.0

### 7. Verify Addition — 39s
- **Screen:** AdAway Home
- **Action:** tap → "Allowed" button
- **Details:** The "Allowed" counter on the home screen now shows 1.
- **Result:** The app navigates back to the "Your lists" screen.
- **Confidence:** 1.0

### 8. View Updated List — 41s
- **Screen:** Your lists (Allowed)
- **Action:** wait
- **Details:** The list now contains one entry: "pol".
- **Result:** The user successfully verifies that the new hostname has been added to the list.
- **Confidence:** 1.0

## Key Observations
- The app is AdAway, version 6.1.4.
- Adding a new entry to a list requires an explicit second step to "apply" the configuration change before it takes effect.
- The home screen dashboard correctly updated the "Allowed" count from 0 to 1 after the configuration was applied.
- The app indicates it uses a VPN configuration for its functionality.