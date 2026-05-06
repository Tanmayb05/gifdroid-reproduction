---
app: DeadHash
goal: To explore the features of the hash calculator app, including text hashing, file hashing, and settings.
outcome: incomplete - The user explored several features but did not complete a full hashing workflow before the recording ended.
---

## Session Summary
The user started on the text hashing screen and calculated hashes for the string "qwerty". They then used the navigation menu to switch to the file hashing tool, briefly opened the file picker, and then navigated to the settings screen. In settings, they disabled the MD5 hash algorithm before the session concluded.

## Steps

### 1. Enter Text for Hashing — 3s
- **Screen:** DeadHash (Text Hashing)
- **Action:** type → `Enter your text here` input field
- **Details:** The user typed the string "qwerty".
- **Result:** The list of hashes below automatically updated to reflect the new input.
- **Confidence:** 1.0

### 2. Open Navigation Menu — 9s
- **Screen:** DeadHash (Text Hashing)
- **Action:** tap → `Hamburger menu icon`
- **Details:** The menu icon is in the top-left corner.
- **Result:** A navigation drawer slid out from the left, showing "Tools" and "Info" sections.
- **Confidence:** 1.0

### 3. Switch to File Hashing — 11s
- **Screen:** DeadHash (Navigation Menu)
- **Action:** tap → `File` menu item
- **Details:** The "File" option is under the "Tools" section.
- **Result:** The view changed to the file hashing screen, which has a "File path" input field.
- **Confidence:** 1.0

### 4. Open File Picker — 13s
- **Screen:** DeadHash (File Hashing)
- **Action:** tap → `Folder icon`
- **Details:** The icon is to the right of the "File path" input field.
- **Result:** The system's "Recent" files view appeared.
- **Confidence:** 1.0

### 5. Close File Picker — 18s
- **Screen:** Recent (System File Picker)
- **Action:** back → `System back button`
- **Details:** The user did not select a file.
- **Result:** The app returned to the "File Hashing" screen.
- **Confidence:** 1.0

### 6. Open Settings — 20s
- **Screen:** DeadHash (File Hashing)
- **Action:** tap → `Settings (gear) icon`
- **Details:** The icon is in the top-right corner.
- **Result:** The "Settings" screen appeared.
- **Confidence:** 1.0

### 7. Disable MD5 Hash — 22s
- **Screen:** Settings
- **Action:** tap → `MD5 toggle switch`
- **Details:** The toggle switch for the MD5 hashing algorithm was turned off.
- **Result:** The toggle became inactive (greyed out).
- **Confidence:** 1.0

## Key Observations
- The app calculates hashes for text input in real-time, without requiring the user to press the "CALCULATE" button.
- The app provides separate tools for hashing text and hashing files.
- Users can customize which hashing algorithms are active and displayed through a dedicated settings menu.
- The MD5 hash for the string "qwerty" is `d8578edf8458ce06fbc5bb76a58c5ca4`.
- The SHA-1 hash for the string "qwerty" is `b1b3773a05c0ed0176787a4f1574ff0075f7521e`.