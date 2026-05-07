---
app: Port Authority
goal: To disable the feature that fetches the device's external IP address.
outcome: success - The user successfully navigated to settings and disabled the option.
---

## Session Summary
The user started on the main screen of the Port Authority app, where an error message indicated the external IP could not be fetched. After running a host scan and briefly inspecting a device, the user opened the side menu, navigated to the settings screen, and successfully disabled the "Fetch device's external IP" option.

## Steps

### 1. Discover Network Hosts — 2s
- **Screen:** Main Screen
- **Action:** `tap` → `DISCOVER HOSTS` button
- **Details:** The main screen shows "Couldn't get your external IP" for the WAN IP field.
- **Result:** A "Scanning For Hosts" dialog appears with a progress bar.

### 2. View Discovered Hosts — 8s
- **Screen:** Main Screen
- **Action:** `wait` → Host scan completes
- **Details:** The scan found 4 hosts.
- **Result:** The main screen updates to show a list of discovered hosts, including both IPv4 and IPv6 addresses.

### 3. Inspect Host Details — 10s
- **Screen:** Main Screen (Host List)
- **Action:** `tap` → Host with IP `fec0::2`
- **Result:** Navigates to the details screen for the selected host.

### 4. Attempt to Wake Host — 13s
- **Screen:** Host Details
- **Action:** `tap` → `WAKE UP` button
- **Details:** The host IP is `fec0::2`.
- **Result:** A toast notification "Waking up fec0::2..." appears briefly.

### 5. Navigate Back to Main Screen — 18s
- **Screen:** Host Details
- **Action:** `back`
- **Result:** Returns to the main screen showing the list of discovered hosts.

### 6. Open Navigation Menu — 18s
- **Screen:** Main Screen
- **Action:** `open_menu` → Hamburger menu icon
- **Result:** The side navigation menu slides in from the left.

### 7. Open Settings — 22s
- **Screen:** Navigation Menu
- **Action:** `tap` → `Settings`
- **Result:** Navigates to the Settings screen.

### 8. Disable External IP Fetching — 24s
- **Screen:** Settings
- **Action:** `tap` → `Fetch device's external IP` checkbox
- **Details:** The checkbox was initially checked.
- **Result:** The checkbox becomes unchecked, disabling the feature.

## Key Observations
- The app displayed an error, "Couldn't get your external IP," on the main screen, which likely prompted the user's actions.
- The app notes that MAC addresses are "Unavailable for non-privileged apps starting with Android 11".
- The device's LAN IP is `10.0.2.16/24`.
- The BSSID is shown as `02:00:00:00:00:00`, which is a locally administered MAC address, often used in virtualized environments or for privacy.