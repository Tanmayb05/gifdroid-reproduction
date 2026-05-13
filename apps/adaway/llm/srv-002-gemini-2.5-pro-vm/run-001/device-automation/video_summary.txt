---
app: AdAway
goal: To add a specific hostname to the ad blocker's whitelist (allowed list).
outcome: success - The user successfully added "abc.com" to the allowed list and applied the new configuration.
---

## Session Summary
The user launched the AdAway ad blocker, enabled it, and then navigated to the "Your lists" section. They switched to the "Allowed" tab, added the hostname "abc.com" to the whitelist, and then applied the configuration change, which successfully updated the ad-blocking rules.

## Steps

### 1. Launch App & Enable Blocker — 3s
- **Screen:** AdAway App Info
- **Action:** tap → `Open` button
- **Details:** The user is on the app's info page, likely from an app store or system settings.
- **Result:** The AdAway app's main screen is displayed. The user then taps the red circular button to enable the ad blocker.

### 2. Navigate to Lists — 10s
- **Screen:** AdAway Main Screen
- **Action:** tap → `hamburger menu icon` (bottom-left)
- **Details:** A navigation menu slides up from the bottom. The user then taps "Your lists".
- **Result:** The user is navigated to the "Your lists" screen, showing the "Blocked" list by default.

### 3. Select Allowed List — 11s
- **Screen:** Your lists
- **Action:** tap → `Allowed` tab
- **Details:** The user switches from the "Blocked" tab to the "Allowed" tab at the bottom of the screen.
- **Result:** The view changes to show the (currently empty) list of allowed hostnames.

### 4. Open Add Host Dialog — 12s
- **Screen:** Your lists (Allowed)
- **Action:** tap → `+` floating action button
- **Details:** The user taps the red circular plus button in the bottom-right corner.
- **Result:** An "Add host to whitelist" dialog appears.

### 5. Enter Hostname — 14s
- **Screen:** Your lists (Allowed)
- **Action:** type → `Hostname` text field
- **Details:** The user types "abc.com" into the input field.
- **Result:** The text "abc.com" is visible in the "Hostname" field.

### 6. Add Host — 18s
- **Screen:** Your lists (Allowed)
- **Action:** tap → `ADD` button
- **Details:** The user confirms the entry in the "Add host to whitelist" dialog.
- **Result:** The dialog closes, "abc.com" appears in the allowed list, and a banner appears at the bottom stating "Your configuration changed. You need to apply it."

### 7. Apply Configuration — 20s
- **Screen:** Your lists (Allowed)
- **Action:** tap → `APPLY` button
- **Details:** The user taps the "APPLY" button on the banner at the bottom of the screen.
- **Result:** The user is returned to the AdAway main screen. A message "VPN configuration successfully updated" appears, and the "Allowed" count is now 1.

## Key Observations
- The app version is 6.1.4, visible in the top-right corner of the main screen.
- Adding a host to the whitelist is a two-step process: first adding the entry, and then explicitly tapping "APPLY" to update the configuration.
- The main screen dashboard updates in real-time, showing the "Allowed" count changing from 0 to 1 after the configuration was applied.
- The app displays a "VPN configuration successfully updated" toast message after enabling the service and after applying list changes, indicating it uses a VPN-based blocking method.