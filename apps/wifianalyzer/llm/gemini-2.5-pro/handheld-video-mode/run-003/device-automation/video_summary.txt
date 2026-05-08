---
app: WiFi Analyzer
goal: To export the current Wi-Fi scan data.
outcome: success - The user successfully copied the scan data to the clipboard.
---

## Session Summary
The user started on the "Access Points" screen of a Wi-Fi analysis application. They navigated through the "Channel Rating" and "Channel Graph" views to visualize the network environment. After briefly inspecting the details of a specific network, the user opened the main menu, selected the export function, and successfully copied the scan data to the clipboard.

## Steps

### 1. Navigate to Channel Rating — 1s
- **Screen:** Access Points
- **Action:** tap → `Channel Rating` tab
- **Details:** The user taps the middle tab at the bottom of the screen.
- **Result:** The view changes to the "Channel Rating" screen, which shows a star-based rating for each Wi-Fi channel.
- **Confidence:** 1.0

### 2. Navigate to Channel Graph — 2s
- **Screen:** Channel Rating
- **Action:** tap → `Channel Graph` tab
- **Details:** The user taps the rightmost tab at the bottom of the screen.
- **Result:** The view changes to the "Channel Graph" screen, displaying a bar graph of Wi-Fi networks by signal strength and channel.
- **Confidence:** 1.0

### 3. Inspect Network Details — 4s
- **Screen:** Channel Graph
- **Action:** tap → `ThodesdaSignal` network bar
- **Details:** The user taps on the bar representing the "ThodesdaSignal" network on the graph.
- **Result:** A dialog box appears, showing detailed information for the selected network, including its MAC address, frequency, and manufacturer (TP LINK SYSTEMS INC).
- **Confidence:** 1.0

### 4. Open Navigation Menu — 8s
- **Screen:** Channel Graph
- **Action:** tap → Hamburger menu icon
- **Details:** The user taps the three-line menu icon in the top-left corner.
- **Result:** A side navigation drawer slides out from the left, revealing options like "Access Points", "Export", and "Settings".
- **Confidence:** 1.0

### 5. Select Export — 10s
- **Screen:** Channel Graph (with Navigation Menu open)
- **Action:** tap → `Export`
- **Details:** The user taps the "Export" option in the navigation menu.
- **Result:** The Android system share sheet appears, presenting the data to be exported and sharing options.
- **Confidence:** 1.0

### 6. Copy Data to Clipboard — 13s
- **Screen:** Android Share Sheet
- **Action:** tap → `Copy`
- **Details:** The user taps the "Copy" button within the share sheet.
- **Result:** A toast notification with the text "Copied" appears at the bottom of the screen, and the user is returned to the "Channel Graph" view.
- **Confidence:** 1.0

## Key Observations
- A persistent warning message, "Wi-Fi scan throttling is enabled," is displayed at the top of the app, indicating a potential limitation on the frequency of Wi-Fi scans by the Android OS.
- The exported data appears to be in a CSV-like format, with the header visible in the share sheet: `Time,BSSID,SSID,Capabilities,Frequency,CenterFrequency0,CenterFrequency1,Width(Range),Level`.
- The app provides multiple data visualization modes: a detailed list ("Access Points"), a channel quality summary ("Channel Rating"), and a signal strength graph ("Channel Graph").