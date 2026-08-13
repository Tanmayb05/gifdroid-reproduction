---
app: Email App
goal: To search for an email in the inbox.
outcome: success - the user found a search result and returned to the inbox.
---

## Session Summary
The user started in the "Unified Inbox" of an email application. They initiated a search by tapping the search icon and typing "Hi". The app displayed a single search result, and the user then tapped the system back button to return to the main inbox screen.

## Steps

### 1. Initiate Search — 1s
- **Screen:** Unified Inbox
- **Action:** tap → `Search icon`
- **Details:** The search icon is located in the top action bar.
- **Result:** The view changed to a search interface, and the on-screen keyboard appeared.
- **Confidence:** 1.0

### 2. Enter Search Query — 2s
- **Screen:** Search
- **Action:** type → `Search text field`
- **Details:** Typed text: "Hi"
- **Result:** The text "Hi" appeared in the search input field.
- **Confidence:** 1.0

### 3. Execute Search — 4s
- **Screen:** Search
- **Action:** tap → `Search button (on keyboard)`
- **Details:** The user tapped the magnifying glass icon on the keyboard to submit the search.
- **Result:** The keyboard was dismissed, and the screen transitioned to display the search results.
- **Confidence:** 1.0

### 4. Navigate Back — 7s
- **Screen:** Search results
- **Action:** back → `System back button`
- **Details:** The user tapped the triangle-shaped system back button in the navigation bar.
- **Result:** The app returned to the initial "Unified Inbox" screen.
- **Confidence:** 1.0

## Key Observations
- A search for the term "Hi" returned an email with the subject "Hello World".
- The single search result was from/to the email address `xtoxoeleartart1524@gmail.com`.