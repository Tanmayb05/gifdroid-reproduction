---
app: Port Authority
goal: To scan the local network for hosts and explore the application's settings.
outcome: success — The user successfully scanned the network and adjusted a setting.
---

## Session Summary
The user initiated a network scan to discover hosts on their local subnet. After the scan completed, they briefly viewed the details of one host before returning to the list. They then navigated to the app's settings menu and enabled the option to fetch the device's external IP address.

## Steps

### 1. Discover Network Hosts — 0s
- **Screen:** Main Screen
- **Action:** tap → `DISCOVER HOSTS (16)` button
- **Details:** The button is on the right side of the screen.
- **Result:** A "Scanning For Hosts" progress dialog appears, scans 254 hosts, and then populates the main screen with a list of discovered devices.
- **Confidence:** 1.0

### 2. View Host Details — 7s
- **Screen:** Discovered Hosts List
- **Action:** tap → `192.168.0.1` list item
- **Details:** The user taps the first item in the list, which is the router.
- **Result:** The app navigates to a detail screen for the selected host, showing its IP address and options like "Open Ports".
- **Confidence:** 1.0

### 3. Navigate Back to Host List — 11s
- **Screen:** Host Details (192.168.0.1)
- **Action:** back → `System back gesture`
- **Details:** The user swipes from the right edge of the screen to go back.
- **Result:** The app returns to the list of discovered hosts.
- **Confidence:** 0.9

### 4. Open Navigation Menu — 13s
- **Screen:** Discovered Hosts List
- **Action:** tap → `Hamburger menu icon`
- **Details:** The icon is in the top-left corner.
- **Result:** A side navigation drawer opens from the left.
- **Confidence:** 1.0

### 5. Open Settings — 15s
- **Screen:** Navigation Menu
- **Action:** tap → `Settings`
- **Details:** The user taps the "Settings" option in the navigation menu.
- **Result:** The app navigates to the Settings screen.
- **Confidence:** 1.0

### 6. Enable External IP Fetching — 21s
- **Screen:** Settings
- **Action:** tap → `Checkbox for "Fetch device's external IP"`
- **Details:** The user taps the empty checkbox under the "Privacy" section.
- **Result:** The checkbox becomes checked, enabling the feature.
- **Confidence:** 1.0

## Key Observations
- The application is a network utility named "Port Authority".
- The local network being scanned is on the `192.168.0.x` subnet.
- The discovered hosts include devices with IP addresses like `192.168.0.1`, `192.168.0.5`, `192.168.0.70`, and `192.168.0.95`.
- The settings screen allows configuration of Host Scans, Port Scans (including threads and timeouts), and a Privacy option to fetch the external IP.