---
app: WIFIAnalyzer
goal: To explore the different data visualization features of the WIFIAnalyzer application.
outcome: success — The user successfully navigated through all the main tabs and viewed the different analysis screens.
---

## Session Summary
The user launched the WIFIAnalyzer app from its Google Play Store page. They then systematically navigated through the app's main features by tapping the bottom navigation tabs, viewing the "Access Points" list, "Channel Rating", "Time Graph", and "Channel Graph". The session concluded after the user returned to the "Channel Rating" screen.

## Steps

### 1. Launch App — 1s
- **Screen:** Google Play Store - WIFIAnalyzer
- **Action:** tap → `Open` button
- **Details:** The user is on the app's store page and decides to open it.
- **Result:** The WIFIAnalyzer app launches and displays the "Access Points" screen.
- **Confidence:** 1.0

### 2. View Channel Ratings — 5s
- **Screen:** Access Points
- **Action:** tap → `Channel Rating` tab
- **Details:** The user navigates from the default list view to the channel rating analysis.
- **Result:** The app switches to the "Channel Rating" screen, showing a ranked list of Wi-Fi channels.
- **Confidence:** 1.0

### 3. View Time Graph — 7s
- **Screen:** Channel Rating
- **Action:** tap → `Time Graph` tab
- **Details:** The user taps the rightmost tab in the bottom navigation bar.
- **Result:** The app switches to the "Time Graph" screen, which shows signal strength over time.
- **Confidence:** 1.0

### 4. View Channel Graph — 11s
- **Screen:** Time Graph
- **Action:** tap → `Channel Graph` tab
- **Details:** The user navigates to the channel graph visualization.
- **Result:** The app switches to the "Channel Graph" screen, showing a bar graph of signal strength per Wi-Fi channel.
- **Confidence:** 1.0

### 5. Return to Channel Rating — 15s
- **Screen:** Channel Graph
- **Action:** tap → `Channel Rating` tab
- **Details:** The user taps the "Channel Rating" tab to return to that view.
- **Result:** The app switches back to the "Channel Rating" screen.
- **Confidence:** 1.0

## Key Observations
- A persistent warning "Wi-Fi scan throttling is enabled" is visible on all screens, indicating a potential limitation in the frequency of Wi-Fi scans imposed by the Android OS.
- The user's device is connected to the "ThodaSaSignal" Wi-Fi network on Channel 6.
- The "Channel Rating" screen recommends channels 9, 10, and 11 as the "Best Channels" for the 2.4 GHz band, as they have the lowest access point count (1).
- The "Channel Graph" provides a visual confirmation of the channel rating, showing significant signal overlap and congestion on channels 1-7.