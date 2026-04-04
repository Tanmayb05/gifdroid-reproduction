---
app: Port Authority
goal: To scan the local network for connected devices and view their details.
outcome: success - The user successfully scanned the network, viewed the list of hosts, and inspected a specific device.
---

## Session Summary
The user launched the Port Authority app and initiated a scan to discover hosts on their local network. After the scan completed, they scrolled through the list of 12 discovered devices. They then selected a specific host to view its details before navigating back to the host list and finally exiting back to the app's info page.

## Steps

### 1. Launch App — 1s
- **Screen:** App Info
- **Action:** tap → `Open` button
- **Details:** The user is on the app's info page and taps "Open" to start the application.
- **Result:** The Port Authority app launches and displays the main network information screen.
- **Confidence:** 1.0

### 2. Start Host Scan — 3s
- **Screen:** Port Authority (Main)
- **Action:** tap → `DISCOVER HOSTS` button
- **Details:** The main screen shows the device's LAN IP as 192.168.0.193/24.
- **Result:** A dialog appears with a progress bar, "Scanning For Hosts", which scans 254 hosts in the subnet.
- **Confidence:** 1.0

### 3. View Scan Results — 13s
- **Screen:** Port Authority (Main)
- **Action:** wait → Scan completes
- **Details:** The scan finishes, and the dialog disappears.
- **Result:** A list of 12 discovered hosts is displayed on the main screen. The button at the bottom updates to "DISCOVER HOSTS (12)".
- **Confidence:** 1.0

### 4. Select Host — 20s
- **Screen:** Port Authority (Main)
- **Action:** tap → Host list item `192.168.0.21`
- **Details:** The user taps on a specific device from the list of discovered hosts.
- **Result:** The app navigates to a details screen for the host with IP address 192.168.0.21.
- **Confidence:** 1.0

### 5. Navigate Back from Host Details — 26s
- **Screen:** Host Details (192.168.0.21)
- **Action:** swipe_right → Screen content
- **Details:** The user swipes right on the screen, which functions as a back gesture.
- **Result:** The app returns to the previous screen showing the list of discovered hosts.
- **Confidence:** 1.0

### 6. Navigate Back to App Info — 28s
- **Screen:** Port Authority (Main)
- **Action:** back → System back button
- **Details:** The user presses the system back button.
- **Result:** The app closes, and the view returns to the initial App Info screen.
- **Confidence:** 1.0

## Key Observations
- The app displays a message "Unavailable for non-privileged apps starting with Android 11" for the MAC address field.
- The app was unable to retrieve the external WAN IP, displaying "Couldn't get your external IP".
- The SSID was reported as `<unknown ssid>` and the BSSID was a generic `02:00:00:00:00:00`.
- The user's device has the LAN IP `192.168.0.193`.
- The network scan discovered a total of 12 hosts.