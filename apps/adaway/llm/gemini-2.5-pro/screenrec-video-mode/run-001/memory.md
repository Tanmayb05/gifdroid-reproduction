---
app: AdAway
goal: To add a specific hostname to the ad blocker's whitelist.
outcome: success - The hostname was added to the list but the configuration was not applied.
---

## Session Summary
The user launched the AdAway application from the home screen. They navigated through the app's menu to the "Your lists" section and switched to the "Allowed" tab. After a brief, abandoned search, the user added the hostname "utl.web" to the whitelist. The session ended on the list screen, with a prompt to apply the new configuration.

## Steps

### 1. Launch App — 0s
- **Screen:** Android Home Screen
- **Action:** `tap` → `AdAway` app icon
- **Details:** The user taps the AdAway icon to open the application.
- **Result:** The AdAway app opens to its main dashboard.
- **Confidence:** 1.0

### 2. Navigate to Lists — 3s
- **Screen:** AdAway Main Dashboard
- **Action:** `tap` → `hamburger menu icon` (bottom-left)
- **Details:** The user opens the main navigation menu.
- **Result:** A side menu appears.
- **Confidence:** 1.0

### 3. Open Allowed List — 5s
- **Screen:** AdAway Main Dashboard with Navigation Menu
- **Action:** `tap` → `Your lists`
- **Details:** The user selects "Your lists" from the menu, then taps the "Allowed" tab at the bottom of the next screen.
- **Result:** The app displays the "Your lists" screen, focused on the "Allowed" (whitelist) tab. An existing entry "yguy" is visible.
- **Confidence:** 1.0

### 4. Initiate Add Host — 14s
- **Screen:** Your lists (Allowed)
- **Action:** `tap` → `red "+" button`
- **Details:** After a brief, abandoned search, the user taps the floating action button to add a new entry.
- **Result:** The "Add host to whitelist" dialog appears.
- **Confidence:** 1.0

### 5. Add Hostname to Whitelist — 17s
- **Screen:** Your lists (Allowed) with "Add host to whitelist" dialog
- **Action:** `type` → `Hostname` text field
- **Details:** The user types "utl.web" into the hostname field and taps "ADD".
- **Result:** The dialog closes. The hostname "utl.web" is added to the list, and a banner appears at the bottom stating "Your configuration changed. You need to apply it."
- **Confidence:** 1.0

## Key Observations
- The app version is 6.1.4, as seen on the main dashboard.
- Modifying lists is a two-step process: add/remove the entry, then tap an "APPLY" button to make the changes active. The user did not complete the second step.
- The "Allowed" list contained a pre-existing entry named "yguy".