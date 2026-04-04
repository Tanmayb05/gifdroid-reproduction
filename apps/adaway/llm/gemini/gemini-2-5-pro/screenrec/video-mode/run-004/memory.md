---
app: AdAway
goal: To add a new hostname to the "Allowed" list (whitelist).
outcome: incomplete — The user added the hostname to the list but did not apply the configuration changes.
---

## Session Summary
The user launched the AdAway app from their home screen and navigated to the "Your lists" section. After adding the hostname "utl.web" to the "Allowed" list, a prompt appeared to apply the changes. The user switched between list tabs but did not apply the new configuration before the session ended.

## Steps

### 1. App Launch — 2s
- **Screen:** Android Home Screen
- **Action:** tap → `AdAway` app icon
- **Details:** The user taps the AdAway app icon to open it.
- **Result:** The AdAway app opens to its main dashboard.
- **Confidence:** 1.0

### 2. Open Lists Menu — 5s
- **Screen:** AdAway Dashboard
- **Action:** tap → `hamburger menu` icon (bottom-left)
- **Details:** The dashboard shows 80065 blocked requests and that the VPN configuration is updated.
- **Result:** The "Your lists" screen appears, showing the "Allowed" list by default.
- **Confidence:** 1.0

### 3. Add New Host — 14s
- **Screen:** Your lists
- **Action:** tap → `+` button (bottom-right)
- **Details:** The user is on the "Allowed" list screen.
- **Result:** The "Add host to whitelist" dialog appears.
- **Confidence:** 1.0

### 4. Enter Hostname — 20s
- **Screen:** Add host to whitelist (Dialog)
- **Action:** type → `Hostname` input field
- **Details:** The user types "utl.web".
- **Result:** The text "utl.web" is entered into the input field.
- **Confidence:** 1.0

### 5. Confirm Addition — 21s
- **Screen:** Add host to whitelist (Dialog)
- **Action:** tap → `ADD` button
- **Details:** The user confirms adding the hostname "utl.web".
- **Result:** The dialog closes, "utl.web" is added to the "Allowed" list, and a banner appears at the bottom stating "Your configuration changed. You need to apply it."
- **Confidence:** 1.0

### 6. Switch to Redirected List — 27s
- **Screen:** Your lists
- **Action:** tap → `Redirected` tab
- **Details:** The user taps the "Redirected" tab at the bottom of the screen.
- **Result:** The view switches to show the (empty) "Redirected" list.
- **Confidence:** 1.0

### 7. Switch to Allowed List — 29s
- **Screen:** Your lists
- **Action:** tap → `Allowed` tab
- **Details:** The user taps the "Allowed" tab at the bottom of the screen.
- **Result:** The view switches back to the "Allowed" list, showing the newly added "utl.web" and the existing "yguy".
- **Confidence:** 1.0

## Key Observations
- After adding a hostname to a list, the user must explicitly tap an "APPLY" button for the configuration change to take effect. The user did not complete this step.
- The AdAway app version is 6.1.4, as seen on the main dashboard.
- The main dashboard indicates that the ad blocker has blocked 80,065 requests.