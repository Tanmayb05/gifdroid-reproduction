---
app: Battery Temperature
goal: The user wants to start and complete a battery temperature logging session.
outcome: success - The logging session started and a notification confirmed its completion.
---

## Session Summary
The user was on the main screen of the Battery Temperature app. They initiated a 1-minute logging session by tapping the "START LOGGING" button. The app confirmed the start of the session by changing the button text and adding a temperature icon to the status bar. After a short wait, a toast notification appeared, indicating that the logging had finished.

## Steps

### 1. Start Logging — 7s
- **Screen:** Main Screen
- **Action:** `tap` → `START LOGGING` button
- **Details:** The logging duration is set to "1 minutes".
- **Result:** The button text changes to "STOP LOGGING" and a notification icon showing "25°" appears in the system status bar.

### 2. Logging Finishes — 12s
- **Screen:** Main Screen
- **Action:** `wait` → `for logging to complete`
- **Details:** The app was logging the temperature.
- **Result:** A toast notification "Temperature logging finished" appears at the bottom of the screen, and the button text reverts to "START LOGGING".

### 3. Return to Home Screen — 14s
- **Screen:** Main Screen
- **Action:** `back` → `(system navigation)`
- **Details:** The "Temperature logging finished" toast is still visible.
- **Result:** The user navigates to the Android home screen.

## Key Observations
- The app displays the current battery temperature as 25.0 °C.
- While logging is active, a notification icon with the current temperature is displayed in the system status bar.
- The log file path is displayed on the screen: `/storage/emulated/0/Android/data/barilyuk.batterytemperature/files/Documents/battery_temperature_log.csv`.
- The app is credited to "Eugen Bariyuk" with the URL "eb43.github.io".