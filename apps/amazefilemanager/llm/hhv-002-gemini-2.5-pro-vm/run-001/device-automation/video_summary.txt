---
app: Amaze File Manager
goal: To start the in-app FTP server, stop it from the system notification, and verify its state.
outcome: success — the user successfully started and stopped the server, though the app UI had a minor state inconsistency.
---

## Session Summary
The user started in the Amaze File Manager's main file browser, opened the navigation menu, and navigated to the FTP Server screen. They started the server, which created a persistent notification. The user then went to the home screen, stopped the server via the notification, and returned to the app to find the UI had not updated. They tapped the "STOP" button in the app, which correctly synchronized the UI with the server's actual state.

## Steps

### 1. Open Navigation Menu — 1s
- **Screen:** File Browser
- **Action:** tap → `Hamburger menu icon`
- **Details:** The user is in the `/storage/emulated/0` directory.
- **Result:** The navigation drawer opened from the left side of the screen.
- **Confidence:** 1.0

### 2. Navigate to FTP Server — 4s
- **Screen:** File Browser with Navigation Drawer
- **Action:** tap → `FTP Server`
- **Details:** The user tapped the "FTP Server" item in the navigation drawer.
- **Result:** The screen transitioned to the "FTP Server" view.
- **Confidence:** 1.0

### 3. Start FTP Server — 6s
- **Screen:** FTP Server
- **Action:** tap → `START` button
- **Details:** The initial status was "Not Running".
- **Result:** The server started, the status changed to "Secure Connection", the button changed to "STOP", and a URL was displayed. A system notification appeared.
- **Confidence:** 1.0

### 4. Go to Home Screen — 10s
- **Screen:** FTP Server
- **Action:** back → `System back/home button`
- **Details:** The user pressed the system home button.
- **Result:** The app was backgrounded and the Android home screen was displayed. The app's notification is visible in the status bar.
- **Confidence:** 1.0

### 5. Open Notification Shade — 13s
- **Screen:** Android Home Screen
- **Action:** swipe_down → `Status bar`
- **Details:** The user swiped down from the top of the screen.
- **Result:** The system notification shade opened, revealing the "Amaze FTP Server running" notification.
- **Confidence:** 1.0

### 6. Stop Server from Notification — 16s
- **Screen:** Notification Shade
- **Action:** tap → `STOP` button on notification
- **Details:** The notification had "STOP" and "History" action buttons.
- **Result:** The "Amaze FTP Server running" notification was dismissed.
- **Confidence:** 1.0

### 7. Open Recent Apps — 21s
- **Screen:** Android Home Screen
- **Action:** tap → `Recent Apps system button`
- **Details:** The user tapped the square system navigation button.
- **Result:** The recent apps switcher view was displayed.
- **Confidence:** 1.0

### 8. Return to App — 23s
- **Screen:** Recent Apps
- **Action:** tap → `Amaze app card`
- **Details:** The user tapped on the Amaze File Manager app preview.
- **Result:** The Amaze app returned to the foreground, showing the FTP Server screen.
- **Confidence:** 1.0

### 9. Stop Server in App — 27s
- **Screen:** FTP Server
- **Action:** tap → `STOP` button
- **Details:** The UI incorrectly showed the server was still running ("Secure Connection", "STOP" button) after it was stopped from the notification.
- **Result:** The UI updated correctly. The status changed to "Not Running" and the button text changed to "START".
- **Confidence:** 1.0

## Key Observations
- When the FTP server is started, it provides a URL: `ftps://192.168.1.250:2211`.
- The app creates a persistent notification with a "STOP" action button when the server is active.
- There is a UI state synchronization bug. After the server is stopped via the system notification, the in-app UI does not automatically update to reflect this change. It continues to show the server as "Running" until the user manually taps the "STOP" button within the app.