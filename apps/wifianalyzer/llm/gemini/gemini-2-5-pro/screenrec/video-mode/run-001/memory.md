---
app: WiFiAnalyzer
goal: To explore the features of the WiFi analyzer app and export the scanned network data.
outcome: success - The user successfully navigated the app and generated the export data, which was presented in the system share sheet.
---

## Session Summary
The user launched the WiFiAnalyzer app, granted the necessary location permission, and explored the different data views (Channel Graph, Access Points, Time Graph). They inspected the details of the currently connected WiFi network. Finally, the user opened the navigation menu, selected the export option, and successfully generated a text-based report of the scanned WiFi access points, which appeared in the system share sheet.

## Steps

### 1. App Launch — 1s
- **Screen:** Android Home Screen
- **Action:** `tap` → `WiFiAnalyzer` app icon
- **Details:** The user taps the WiFiAnalyzer app icon to start the application.
- **Result:** The app opens and immediately displays an informational dialog.
- **Confidence:** 1.0

### 2. Acknowledge Information Dialog — 3s
- **Screen:** WiFiAnalyzer (open-source) Dialog
- **Action:** `tap` → `OK` button
- **Details:** The dialog explains that location permissions are required for Wi-Fi scanning and that Wi-Fi scan throttling might be active.
- **Result:** The informational dialog closes, and a system permission request for location access is displayed.
- **Confidence:** 1.0

### 3. Grant Location Permission — 4s
- **Screen:** System Location Permission Dialog
- **Action:** `tap` → `While using the app` button
- **Details:** The user grants the app permission to access the device's location while the app is in use.
- **Result:** The permission is granted, and the app's main "Channel Graph" screen is displayed, showing data for the current WiFi network.
- **Confidence:** 1.0

### 4. Navigate to Access Points — 8s
- **Screen:** Channel Graph
- **Action:** `tap` → `Access Points` tab
- **Details:** The user taps the "Access Points" icon in the bottom navigation bar.
- **Result:** The view changes to the "Access Points" screen, listing available networks.
- **Confidence:** 1.0

### 5. View Network Details — 9s
- **Screen:** Access Points
- **Action:** `tap` → `AndroidWifi` list item
- **Details:** The user taps on the "AndroidWifi" network in the list.
- **Result:** A dialog appears, showing detailed information about the selected network.
- **Confidence:** 1.0

### 6. Close Network Details — 10s
- **Screen:** WiFi Details Dialog
- **Action:** `tap` → `OK` button
- **Result:** The details dialog is dismissed, returning to the "Access Points" screen.
- **Confidence:** 1.0

### 7. Navigate to Time Graph — 13s
- **Screen:** Access Points
- **Action:** `tap` → `Time Graph` tab
- **Details:** The user taps the "Time Graph" icon in the bottom navigation bar.
- **Result:** The view changes to the "Time Graph" screen, showing signal strength over time.
- **Confidence:** 1.0

### 8. Return to Channel Graph — 16s
- **Screen:** Time Graph
- **Action:** `tap` → `Channel Graph` tab
- **Details:** The user taps the "Channel Graph" icon in the bottom navigation bar.
- **Result:** The view returns to the "Channel Graph" screen.
- **Confidence:** 1.0

### 9. Open Navigation Menu — 20s
- **Screen:** Channel Graph
- **Action:** `open_menu` → `Hamburger menu icon`
- **Details:** The user taps the menu icon in the top-left corner.
- **Result:** The side navigation drawer slides out from the left.
- **Confidence:** 1.0

### 10. Select Export — 22s
- **Screen:** Navigation Drawer
- **Action:** `tap` → `Export` menu item
- **Result:** The Android system share sheet appears, displaying the exported WiFi data as "Sharing text".
- **Confidence:** 1.0

### 11. Dismiss Share Sheet — 25s
- **Screen:** System Share Sheet
- **Action:** `swipe_down` → `Share sheet handle`
- **Result:** The share sheet is dismissed, and the user is returned to the app's "Channel Graph" screen.
- **Confidence:** 1.0

## Key Observations
- A persistent warning, "Wi-Fi scan throttling is enabled," is displayed across all main screens of the app. The initial dialog provides instructions on how to disable this in Android's Developer Options.
- The app requires precise location permission to function, which it explains is a system requirement for Wi-Fi scanning since Android Marshmallow.
- The exported data is a structured text block containing a timestamp and pipe-separated values for access point details like SSID, BSSID, Strength, and Channel.
- The user's current connection is to "AndroidWifi" on Channel 8 (2447MHz) with a signal strength of -50dBm. The BSSID is `00:13:10:85:fe:01`.