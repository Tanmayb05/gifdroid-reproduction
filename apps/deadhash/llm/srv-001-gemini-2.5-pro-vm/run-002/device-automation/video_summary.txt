---
app: DeadHash
goal: To explore the app's features for calculating hashes from text and to configure the available hashing algorithms.
outcome: success — The user successfully calculated a hash, navigated between app sections, and modified a setting.
---

## Session Summary
The user started on the text hashing screen of the DeadHash app and entered "qwerty" to generate its corresponding hashes. They then explored the file hashing feature via the navigation menu but did not select a file. Finally, the user navigated to the settings screen and disabled the MD5 hashing algorithm.

## Steps

### 1. App Launch — 0s
- **Screen:** DeadHash Text Hashing
- **Action:** launch → `app: DeadHash`
- **Details:** The app opens to the main screen for calculating hashes from text.
- **Result:** The text hashing interface is displayed, showing fields for text input and hash comparison, along with a list of hash types.
- **Confidence:** 1.0

### 2. Enter Text for Hashing — 3s
- **Screen:** DeadHash Text Hashing
- **Action:** type → `EditText` with hint "Enter your text here"
- **Details:** Typed text: "qwerty"
- **Result:** The app automatically calculates and displays the hashes for "qwerty" in the list below.
- **Confidence:** 1.0

### 3. Open Navigation Menu — 9s
- **Screen:** DeadHash Text Hashing
- **Action:** tap → `Hamburger menu icon`
- **Details:** The user taps the menu icon in the top-left corner.
- **Result:** A side navigation drawer opens, showing "Tools" (File, Text) and "Info" (Help, About) sections.
- **Confidence:** 1.0

### 4. Navigate to File Hashing — 11s
- **Screen:** DeadHash Navigation Menu
- **Action:** tap → `File`
- **Details:** The user selects the "File" option from the "Tools" section in the navigation menu.
- **Result:** The app transitions to the file hashing screen.
- **Confidence:** 1.0

### 5. Open File Picker — 14s
- **Screen:** DeadHash File Hashing
- **Action:** tap → `Folder icon`
- **Details:** The user taps the folder icon to select a file for hashing.
- **Result:** The system's file picker interface ("Recent") appears.
- **Confidence:** 1.0

### 6. Return to App — 18s
- **Screen:** System File Picker
- **Action:** back → `System back button`
- **Details:** The user presses the back button without selecting a file.
- **Result:** The file picker closes, and the user returns to the app's file hashing screen.
- **Confidence:** 1.0

### 7. Open Settings — 20s
- **Screen:** DeadHash File Hashing
- **Action:** tap → `Settings icon`
- **Details:** The user taps the gear icon in the top-right corner.
- **Result:** The app navigates to the "Settings" screen.
- **Confidence:** 1.0

### 8. Disable MD5 Hashing — 23s
- **Screen:** Settings
- **Action:** tap → `Toggle switch` for "MD5"
- **Details:** The user taps the toggle next to the "MD5" option under the "Hashing" section.
- **Result:** The toggle for MD5 is set to the "off" position.
- **Confidence:** 1.0

## Key Observations
- The app calculates hashes in real-time as the user types, without requiring a tap on the "CALCULATE" button.
- The MD5 hash calculated for the text "qwerty" is `d8578edf8458ce06fbc5bb76a58c5ca4`.
- The settings allow the user to enable or disable specific hashing algorithms (MD5, SHA-1, SHA-224, etc.) from being displayed.
- The app provides separate interfaces for hashing text and hashing files.