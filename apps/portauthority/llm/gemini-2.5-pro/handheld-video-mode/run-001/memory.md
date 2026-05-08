---
app: Port Authority
goal: The user wants to scan their local network to discover connected devices and view their details.
outcome: success - The app successfully scanned the network, listed the hosts, and allowed the user to view details for a selected host.
---

## Session Summary
The user started on the app's information page and launched the "Port Authority" application. They immediately initiated a network scan, which successfully discovered 12 hosts on the local subnet. The user then scrolled through the results, selected a specific host to view its details, and then navigated back to the app's info page, completing the task.

## Steps

### 1. Launch App — 1s
- **Screen:** Port Authority App Info
- **Action:** `tap` → `Open` button
- **Details:** The app info page shows the app name "Port Authority" by Aaron Wood.
- **Result:** The "Port Authority" app launches to its main screen.
- **Confidence:** 1.0

### 2. Discover Hosts — 3s
- **Screen:** Port Authority Main Screen
- **Action:** `tap` → `DISCOVER HOSTS` button
- **Details:** The screen displays the device's network information, including LAN IP `192.168.0.193/24`.
- **Result:** A "Scanning For Hosts" progress dialog appears and shows the scan progressing.
- **Confidence:** 1.0

### 3. Review Scan Results — 13s
- **Screen:** Port Authority Main Screen
- **Action:** `swipe_up` → Host list
- **Details:** The scan has completed, and a list of 12 discovered hosts is displayed.
- **Result:** The user scrolls down the list, revealing more discovered devices.
- **Confidence:** 1.0

### 4. Select Host — 20s
- **Screen:** Port Authority Main Screen
- **Action:** `tap` → Host entry `192.168.0.21`
- **Result:** The app navigates to a details screen for the selected host.
- **Confidence:** 1.0

### 5. Navigate Back from Host Details — 26s
- **Screen:** Host Details (192.168.0.21)
- **Action:** `swipe_right` → Screen area
- **Details:** The screen shows the MAC address `a2:de:89:a8:37:d7` for the selected IP.
- **Result:** The app returns to the previous screen showing the list of all discovered hosts.
- **Confidence:** 1.0

### 6. Navigate Back to App Info — 27s
- **Screen:** Port Authority Main Screen
- **Action:** `back` → System back gesture
- **Result:** The app closes, and the view returns to the initial App Info screen.
- **Confidence:** 1.0

## Key Observations
- The app is unable to retrieve the device's own MAC address, displaying a message: "Unavailable for non-privileged apps starting with Android 11".
- The app failed to get the external WAN IP, showing "Couldn't get your external IP".
- The SSID is displayed as `<unknown ssid>` and the BSSID is a generic `02:00:00:00:00:00`, indicating a potential lack of permissions or an unusual network configuration.
- The network scan successfully discovered 12 hosts on the `192.168.0.0/24` subnet.