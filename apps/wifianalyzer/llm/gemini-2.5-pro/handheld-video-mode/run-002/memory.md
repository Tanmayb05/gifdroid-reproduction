---
app: WIFIAnalyzer
goal: The user wants to explore the different data visualization features of the WIFIAnalyzer app.
outcome: success - The user successfully navigated through all the main tabs and viewed the different analysis screens.
---

## Session Summary
The user started on the Google Play Store page for the WIFIAnalyzer app and launched it. They landed on the "Access Points" list, then systematically tapped through the bottom navigation tabs to view the "Channel Rating", "Time Graph", and "Channel Graph" screens. The user finished the session by cycling back through the tabs, ending on the "Channel Rating" screen.

## Steps

### 1. Launch App — 1s
- **Screen:** Google Play Store - WIFIAnalyzer App Page
- **Action:** `tap` → `Open` button
- **Details:** The app page shows the app was "Updated 2 months ago".
- **Result:** The WIFIAnalyzer app launches and displays the "Access Points" screen.
- **Confidence:** 1.0

### 2. Scroll Network List — 3s
- **Screen:** Access Points
- **Action:** `swipe_up` → `Network List`
- **Details:** The list contains numerous Wi-Fi networks, including "ThodaSaSignal", "TrapLordRicky", and "TroysAbedintheModem". A warning "Wi-Fi scan throttling is enabled" is visible.
- **Result:** The list of available Wi-Fi networks scrolls up, revealing more entries at the bottom.
- **Confidence:** 1.0

### 3. View Channel Rating — 5s
- **Screen:** Access Points
- **Action:** `tap` → `Channel Rating` tab
- **Result:** The app switches to the "Channel Rating" view, which displays a star-based rating for each Wi-Fi channel.
- **Confidence:** 1.0

### 4. View Time Graph — 7s
- **Screen:** Channel Rating
- **Action:** `tap` → `Time Graph` tab
- **Result:** The app switches to the "Time Graph" view. The graph begins to populate with signal strength data over time.
- **Confidence:** 1.0

### 5. View Channel Graph — 12s
- **Screen:** Time Graph
- **Action:** `tap` → `Channel Graph` tab
- **Result:** The app switches to the "Channel Graph" view, showing a bar chart of signal strength for networks on different channels.
- **Confidence:** 1.0

### 6. Return to Channel Rating — 15s
- **Screen:** Channel Graph
- **Action:** `tap` → `Channel Rating` tab
- **Result:** The app navigates back to the "Channel Rating" screen.
- **Confidence:** 1.0

### 7. Return to Access Points — 17s
- **Screen:** Channel Rating
- **Action:** `tap` → `Access Points` tab
- **Result:** The app navigates back to the "Access Points" screen.
- **Confidence:** 1.0

### 8. End on Channel Rating — 19s
- **Screen:** Access Points
- **Action:** `tap` → `Channel Rating` tab
- **Result:** The app navigates back to the "Channel Rating" screen, where the session ends.
- **Confidence:** 1.0

## Key Observations
- A persistent warning, "Wi-Fi scan throttling is enabled," is displayed across all screens, indicating a potential Android system limitation on scan frequency.
- The user's device is connected to the "ThodaSaSignal" network on channel 6, with a link speed of 39Mbps and an IP address of 192.168.0.193.
- The "Channel Rating" screen suggests that channels 9, 10, and 11 are the best available options in the 2.4 GHz band.
- The "Channel Graph" shows significant congestion on channels 1-6, with multiple overlapping networks.