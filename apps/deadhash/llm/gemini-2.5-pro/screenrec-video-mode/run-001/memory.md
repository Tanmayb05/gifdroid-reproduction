---
app: DeadHash
goal: To explore the features of the DeadHash app, including text hashing, file hashing, and settings.
outcome: incomplete — The user explored several features but did not complete a specific end-to-end task.
---

## Session Summary
The user started on the text hashing screen and calculated hashes for the string "qwerty". They then navigated to the file hashing screen via the side menu and briefly opened the system file picker before returning. Finally, the user accessed the settings screen and disabled the MD5 hashing algorithm.

## Steps

### 1. Type Text for Hashing — 3s
- **Screen:** Text Hashing
- **Action:** `type` → `Enter your text here` input field
- **Details:** Typed text: "qwerty"
- **Result:** The list of hashes below (MD5, SHA-1, etc.) updated in real-time to show the calculated hashes for "qwerty".
- **Confidence:** 1.0

### 2. Open Navigation Menu — 9s
- **Screen:** Text Hashing
- **Action:** `tap` → `Hamburger menu icon`
- **Details:** The menu icon is in the top-left corner.
- **Result:** A navigation drawer slid out from the left, showing "Tools" and "Info" sections.
- **Confidence:** 1.0

### 3. Navigate to File Hashing — 11s
- **Screen:** Navigation Drawer
- **Action:** `tap` → `File` menu item
- **Details:** The "File" item is under the "Tools" section.
- **Result:** The screen transitioned to the file hashing interface.
- **Confidence:** 1.0

### 4. Open File Picker — 13s
- **Screen:** File Hashing
- **Action:** `tap` → `Folder icon`
- **Details:** The icon is next to the "File path" input field.
- **Result:** The Android system file picker ("Recent") opened.
- **Confidence:** 1.0

### 5. Close File Picker — 17s
- **Screen:** System File Picker
- **Action:** `back` → `System back button`
- **Details:** The user pressed the system navigation back button.
- **Result:** The file picker closed, and the app returned to the File Hashing screen.
- **Confidence:** 1.0

### 6. Open Settings — 20s
- **Screen:** File Hashing
- **Action:** `tap` → `Settings icon`
- **Details:** The gear icon is in the top-right corner.
- **Result:** The "Settings" screen appeared.
- **Confidence:** 1.0

### 7. Disable MD5 Hashing — 22s
- **Screen:** Settings
- **Action:** `tap` → `MD5 toggle switch`
- **Details:** The toggle switch was initially enabled (on).
- **Result:** The toggle switch for MD5 was set to the disabled (off) position.
- **Confidence:** 1.0

## Key Observations
- The app calculates hashes for text input in real-time as the user types, without requiring a button press.
- The app provides two main hashing tools: one for text and one for files, accessible via a navigation drawer.
- The settings screen allows users to enable or disable individual hashing algorithms, including MD5, SHA-1, SHA-224, SHA-256, SHA-384, SHA-512, and CRC32.
- The MD5 hash for the string "qwerty" is `d8578edf8458ce06fbc5bb76a58c5ca4`.