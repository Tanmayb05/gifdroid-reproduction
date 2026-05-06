---
app: AdAway
goal: The user wants to add a new hostname to the whitelist (allowed list).
outcome: incomplete — The hostname was added to the list, but the user did not apply the configuration changes to make them active.
---

## Session Summary
The user launched the AdAway ad blocker, navigated to the "Your lists" section, and viewed the "Allowed" list. After a brief, unsuccessful search, they added the new hostname "utl.web" to the whitelist. A banner prompted them to apply the new configuration, but the user navigated between tabs without applying the changes, leaving the task unfinished.

## Steps

### 1. Launch App — 0s
- **Screen:** Android Home Screen
- **Action:** tap → "AdAway" app icon
- **Details:** The user is on their home screen and taps the AdAway icon.
- **Result:** The AdAway app launched and displayed its main dashboard.
- **Confidence:** 1.0

### 2. Navigate to Lists — 5s
- **Screen:** AdAway Dashboard
- **Action:** tap → Hamburger menu icon (bottom-left)
- **Details:** The user tapped the menu icon at the bottom-left of the screen.
- **Result:** The app navigated to the "Your lists" screen, defaulting to the "Allowed" tab.
- **Confidence:** 1.0

### 3. Search for Hostname — 9s
- **Screen:** Your lists
- **Action:** type → "Search hostname..." field
- **Details:** The user tapped the search icon and typed "edhb".
- **Result:** The text was entered, but the list remained unchanged as there were no matching entries.
- **Confidence:** 1.0

### 4. Initiate Add Host — 14s
- **Screen:** Your lists
- **Action:** tap → Red "+" button
- **Details:** The user tapped the floating action button to add a new entry.
- **Result:** An "Add host to whitelist" dialog appeared.
- **Confidence:** 1.0

### 5. Enter Hostname — 17s
- **Screen:** Add host to whitelist
- **Action:** type → "Hostname" text field
- **Details:** Typed "utl.web".
- **Result:** The text "utl.web" was entered into the input field.
- **Confidence:** 1.0

### 6. Confirm Add Host — 21s
- **Screen:** Add host to whitelist
- **Action:** tap → "ADD" button
- **Details:** The user confirmed the addition of the new hostname.
- **Result:** The dialog closed, "utl.web" appeared in the list, and a banner appeared at the bottom stating "Your configuration changed. You need to apply it."
- **Confidence:** 1.0

### 7. View Redirected List — 27s
- **Screen:** Your lists
- **Action:** tap → "Redirected" tab
- **Details:** The user tapped the "Redirected" tab in the bottom navigation bar.
- **Result:** The view switched to the "Redirected" list, which was empty. The "Apply" banner remained visible.
- **Confidence:** 1.0

### 8. View Allowed List — 29s
- **Screen:** Your lists
- **Action:** tap → "Allowed" tab
- **Details:** The user tapped the "Allowed" tab to return to the previous view.
- **Result:** The view switched back to the "Allowed" list, showing the new "utl.web" entry. The "Apply" banner was still present.
- **Confidence:** 1.0

## Key Observations
- The app version is 6.1.4, as seen on the main dashboard.
- Adding a hostname to a list is a two-step process: adding the entry, and then separately applying the configuration changes.
- The user did not complete the process by tapping the "APPLY" button, leaving the new whitelist rule in a pending, inactive state.
- The main dashboard indicates the app has blocked 80,065 requests and is using a VPN-based configuration.