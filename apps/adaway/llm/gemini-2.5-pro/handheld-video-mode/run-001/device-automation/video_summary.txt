---
app: AdAway
goal: The user wants to add a new domain to the whitelist.
outcome: success - The domain "abc.com" was successfully added to the whitelist.
---

## Session Summary
The user opened the AdAway app from its F-Droid store page and landed on the main dashboard. They then navigated to the "Your lists" section, where they added the domain "abc.com" to the whitelist. The session concluded after the user successfully added the domain and navigated back to the dashboard.

## Steps

### 1. Open App — 0s
- **Screen:** App Details (F-Droid)
- **Action:** `tap` → `Open` button
- **Details:** The user is on the AdAway app page and opens it.
- **Result:** The AdAway main dashboard screen is displayed.
- **Confidence:** 1.0

### 2. Navigate to Lists — 2s
- **Screen:** AdAway Dashboard
- **Action:** `tap` → `3 up-to-date sources` tile
- **Details:** The dashboard shows 83182 blocked, 3 allowed, and 0 redirected entries.
- **Result:** The app navigates to the "Your lists" screen.
- **Confidence:** 1.0

### 3. Open Add Host Dialog — 7s
- **Screen:** Your lists
- **Action:** `tap` → `+` (Add) icon
- **Details:** The user is on the "Whitelist" tab.
- **Result:** The "Add host to whitelist" dialog appears.
- **Confidence:** 1.0

### 4. Enter Hostname — 10s
- **Screen:** Your lists (Add host to whitelist dialog)
- **Action:** `type` → `Hostname` input field
- **Details:** Typed "abc.com"
- **Result:** The text "abc.com" is entered into the field.
- **Confidence:** 1.0

### 5. Add Host to Whitelist — 16s
- **Screen:** Your lists (Add host to whitelist dialog)
- **Action:** `tap` → `ADD` button
- **Details:** N/A
- **Result:** The dialog closes, "abc.com" appears in the whitelist, and a banner "Your configuration changed. You need to apply it." is displayed.
- **Confidence:** 1.0

### 6. Navigate Back to Dashboard — 19s
- **Screen:** Your lists
- **Action:** `tap` → Back arrow
- **Details:** N/A
- **Result:** The app returns to the main dashboard screen.
- **Confidence:** 1.0

## Key Observations
- After adding an entry to the whitelist, a banner appears stating, "Your configuration changed. You need to apply it." This indicates that modifying lists is a separate step from applying the new rules.
- The dashboard displayed a count of 83,182 blocked hosts before the user's action.