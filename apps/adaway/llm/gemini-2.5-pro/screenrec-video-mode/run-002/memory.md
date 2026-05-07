---
app: AdAway
goal: To add a new hostname to the "Allowed" list (whitelist).
outcome: success - The hostname was added to the list, but the configuration was not applied.
---

## Session Summary
The user launched the AdAway app and navigated from the main dashboard to the "Your lists" section. They successfully added a new hostname, "utl.web", to the "Allowed" list. Although the app prompted them to apply the new configuration, the user did not complete this final step and instead browsed other list tabs before the session ended.

## Steps

### 1. App Launch — 2s
- **Screen:** Android Home Screen
- **Action:** tap → `AdAway` app icon
- **Details:** The user taps the AdAway icon, which is a white dove on a red background.
- **Result:** The AdAway app opens to its main dashboard.
- **Confidence:** 1.0

### 2. Open App Menu — 5s
- **Screen:** AdAway Dashboard
- **Action:** tap → hamburger menu icon (bottom-left)
- **Result:** A navigation menu slides up from the bottom, revealing options like "Your lists" and "Host sources".
- **Confidence:** 1.0

### 3. Navigate to Lists — 5s
- **Screen:** AdAway Dashboard with Menu
- **Action:** tap → `Your lists` menu item
- **Result:** The app navigates to the "Your lists" screen, defaulting to the "Allowed" tab.
- **Confidence:** 1.0

### 4. Initiate Add Host — 14s
- **Screen:** Your lists (Allowed)
- **Action:** tap → `+` button (bottom-right)
- **Result:** The "Add host to whitelist" dialog appears.
- **Confidence:** 1.0

### 5. Enter Hostname — 21s
- **Screen:** Your lists (Allowed) with "Add host to whitelist" dialog
- **Action:** type → `Hostname` text field
- **Details:** Text typed: "utl.web"
- **Result:** The text "utl.web" is entered into the field.
- **Confidence:** 1.0

### 6. Confirm Add Host — 22s
- **Screen:** Your lists (Allowed) with "Add host to whitelist" dialog
- **Action:** tap → `ADD` button
- **Result:** The dialog closes, "utl.web" is added to the list, and a banner appears at the bottom stating "Your configuration changed. You need to apply it."
- **Confidence:** 0.9

### 7. View Redirected List — 27s
- **Screen:** Your lists (Allowed)
- **Action:** tap → `Redirected` tab
- **Result:** The view switches to the "Redirected" list, which is empty.
- **Confidence:** 1.0

### 8. Return to Allowed List — 29s
- **Screen:** Your lists (Redirected)
- **Action:** tap → `Allowed` tab
- **Result:** The view switches back to the "Allowed" list, showing the newly added "utl.web" and the existing "yguy" entry.
- **Confidence:** 1.0

## Key Observations
- The app requires an explicit "Apply" action after a configuration change, which the user did not perform in this session.
- The main dashboard shows a running count of blocked requests, which was 80065 at the start of the session.
- The app version is 6.1.4, visible on the main dashboard.
- The "Your lists" screen is organized into three tabs: "Blocked", "Allowed", and "Redirected".