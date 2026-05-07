---
app: Port Authority
goal: The user wants to scan their local network for connected devices and view details about one of them.
outcome: success - The user successfully scanned the network, viewed the list of hosts, and inspected a specific device.
---

## Session Summary
The user launched the Port Authority app from its details page and initiated a scan to discover hosts on the local network. After the scan completed, they scrolled through the resulting list of 12 devices. They then selected one host to view its details before navigating back to the host list and then back to the initial app details screen.

## Steps

### 1. Open App — 1s
- **Screen:** App Details
- **Action:** tap → `Open` button
- **Details:** The user is on the app's info/store page and opens it.
- **Result:** The Port Authority app launches to its main screen.
- **Confidence:** 1.0

### 2. Start Host Scan — 3s
- **Screen:** Port Authority (Main)
- **Action:** tap → `DISCOVER HOSTS` button
- **Details:** The main screen displays network info like LAN IP `192.168.0.193/24`.
- **Result:** A "Scanning For Hosts" progress dialog appears and the scan begins.
- **Confidence:** 1.0

### 3. View Scan Results — 13s
- **Screen:** Port Authority (Main)
- **Action:** wait → Scan completes
- **Details:** The scan finishes, and the progress dialog disappears.
- **Result:** A list of 12 discovered hosts is displayed on the main screen. The button text updates to `DISCOVER HOSTS (12)`.
- **Confidence:** 1.0

### 4. Select Host — 20s
- **Screen:** Port Authority (Main)
- **Action:** tap → `192.168.0.21` list item
- **Details:** The user selects a specific host from the discovered list.
- **Result:** Navigates to a details screen for the host `192.168.0.21`.
- **Confidence:** 1.0

### 5. Navigate Back from Host Details — 26s
- **Screen:** Host Details (192.168.0.21)
- **Action:** swipe_right → Screen content
- **Details:** The user swipes from the left edge to go back.
- **Result:** The app navigates back to the main screen showing the list of discovered hosts.
- **Confidence:** 0.95

### 6. Navigate Back to App Details — 28s
- **Screen:** Port Authority (Main)
- **Action:** back → System back gesture
- **Details:** The user performs a system back action.
- **Result:** The app closes, and the user is returned to the initial App Details screen.
- **Confidence:** 1.0

## Key Observations
- The app displays a message "MAC: Unavailable for non-privileged apps starting with Android 11", indicating a known OS-level restriction.
- The app was unable to retrieve the WAN IP, displaying "Couldn't get your external IP".
- The SSID is shown as `<unknown ssid>` and the BSSID is `02:00:00:00:00:00`, which is a randomized MAC address used by Android for privacy.
- The local network scan successfully discovered 12 hosts on the `192.168.0.193/24` subnet.