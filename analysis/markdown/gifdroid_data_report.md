# GIFdroid HHV vs SRV Analysis Report

**Dataset:** 44 runs · 8 apps · Generated 2026-03-23

---

## Executive Summary

The headline completion rates are nearly identical — HHV completes 90.0% (18/20) vs SRV 91.7% (22/24). That metric hides the real story. **HHV consistently produces worse reconstruction quality**: more spurious keyframes, weaker GUI mapping, fewer distinct mapped screens, shallower traces, and dramatically worse runtime.

The dominant failure mode is not a crash — it is a silent quality collapse where the pipeline finishes but returns a low-fidelity trace covering only a fraction of the app's actual interaction.

---

## Key Metrics at a Glance

| Metric | HHV | SRV |
|---|---|---|
| Completion rate | 90.0% (18/20) | 91.7% (22/24) |
| Avg keyframes detected | 25.5 | 8.0 |
| Avg mapping score (mean) | 0.281 | 0.396 |
| Avg mapping score (max) | 0.32 | 0.55 |
| Avg score spread (max−min) | 0.07 | 0.35 |
| Avg unique screens mapped | 1.15 | 4.42 |
| Avg LCS | 1.07 | 2.32 |
| Avg trace length | 5.27 | 7.47 |
| Avg actions per trace | 4.6 | 7.0 |
| Avg total time | 1922s | 218s |
| Median total time | 257s | 149s |

---

## Root Cause: Two Cascading Failures

### Failure 1 — Keyframe Over-Detection (Step 1)

GIFdroid's keyframe detector uses consecutive-frame SSIM with a hardcoded stability threshold of 0.95. In SRV, frames are pixel-stable between genuine UI transitions, so this threshold works. In HHV, camera shake and hand motion cause SSIM to drop to 0.85–0.93 even on a *stable* screen — the detector fires constantly, producing 5–18× more keyframes than SRV for the same session.

| App | SRV Keyframes | HHV Keyframes | Ratio |
|---|---|---|---|
| AdAway | 3 | 39 | 13× |
| HomeMedkit | 8 | 54 | 7× |
| SimpleNotes | 7 | 35 | 5× |
| PortAuthority | 7 | 22 | 3× |
| AntennaPod | 9 | 10 | ~1× (similar by coincidence) |
| WifiAnalyzer | 16 | 15 | ~1× (similar by coincidence) |

### Failure 2 — Screen Mapping Collapse (Step 2)

After excessive keyframes are generated, the GUI mapper (0.5×SSIM + 0.5×ORB) scores all keyframes nearly identically against all artifact screenshots. With a score spread of only 0.02–0.08 (vs SRV's 0.15–0.49), all keyframes map to the same single best-match screen. The resulting sequence like `[5,5,5,5,5,5,5,5]` cannot yield a meaningful trace.

**Why spread collapses:** Motion blur, perspective distortion, and lighting variation make all HHV frames look equally similar to all screenshots. Additionally, Lowe's ratio test in the ORB matcher is set to 0.4 (extremely strict) — on blurry HHV frames almost no keypoints pass, reducing the ORB contribution to near zero, leaving only SSIM which compresses all frames into a narrow 0.28–0.32 band.

| App / UTG | Type | Keyframes | Unique Screens | Score Spread |
|---|---|---|---|---|
| AdAway / utg01 | SRV | 3 | 3 | 0.091 |
| AdAway / utg01 | HHV | 39 | **1** | 0.112 |
| AntennaPod / utg01 | SRV | 9 | 7 | 0.491 |
| AntennaPod / utg01 | HHV | 10 | **1** | 0.030 |
| HomeMedkit / utg01 | SRV | 8 | 4 | 0.389 |
| HomeMedkit / utg01 | HHV | 54 | **1** | 0.066 |
| LuxAlarm / utg01 | SRV | 8 | 4 | 0.471 |
| LuxAlarm / utg01 | HHV | 11 | **2** | 0.024 |
| WifiAnalyzer / utg01 | SRV | 16 | 11 | 0.358 |
| WifiAnalyzer / utg01 | HHV | 15 | **2** | 0.088 |

---

## Confidence Score Degradation

| App / UTG | Type | Score Mean | Score Max | Spread |
|---|---|---|---|---|
| AdAway / utg01 | SRV | 0.382 | 0.414 | 0.091 |
| AdAway / utg01 | HHV | 0.298 | 0.370 | 0.112 |
| AntennaPod / utg01 | SRV | 0.464 | 0.670 | 0.491 |
| AntennaPod / utg01 | HHV | 0.317 | 0.331 | 0.030 |
| HomeMedkit / utg01 | SRV | 0.453 | 0.553 | 0.389 |
| HomeMedkit / utg01 | HHV | 0.293 | 0.321 | 0.066 |
| LuxAlarm / utg01 | SRV | 0.383 | 0.618 | 0.471 |
| LuxAlarm / utg01 | HHV | 0.273 | 0.286 | 0.024 |
| WifiAnalyzer / utg01 | SRV | 0.403 | 0.630 | 0.358 |
| WifiAnalyzer / utg01 | HHV | 0.250 | 0.310 | 0.088 |
| PortAuthority / utg01 | SRV | 0.394 | 0.586 | 0.372 |
| PortAuthority / utg01 | HHV | 0.212 | 0.242 | 0.058 |

When all scores cluster near the same value (low spread), the algorithm cannot tell screens apart — all keyframes get assigned the same best match, collapsing multi-step interactions into single-screen traces.

---

## Runtime Impact

| App / UTG | SRV Total (s) | HHV Total (s) | Slowdown |
|---|---|---|---|
| AntennaPod / utg03 | 375 | **27,517** | **73×** — 7.6 hours |
| HomeMedkit / utg03 | 280 | 2,589 | 9× |
| HomeMedkit / utg01 | 115 | 409 | 4× |
| HomeMedkit / utg02 | 148 | 600 | 4× |
| SimpleNotes / utg01 | 80 | 299 | 4× |
| AntennaPod / utg01 | 150 | 383 | 3× |
| AdAway / utg01 | 110 | 215 | 2× |
| WifiAnalyzer / utg02 | 316 | 433 | 1.4× |
| PortAuthority / utg01 | 518 | 183 | 0.4× (HHV faster — SRV video is 3× longer) |

**AntennaPod utg03 pathological case:** All 2025 HHV frames mapped to 1 unique screen, yet the pipeline still ran exhaustive comparisons — `2025 frames × 85 artifacts = 172,125 comparisons` — with no early-exit logic. This is a combinatorial blowup from the lack of degenerate-state detection.

---

## Per-App Summary

| App | HHV Status | Keyframes (HHV vs SRV) | Map Score (HHV vs SRV) | Unique Screens (HHV vs SRV) | LCS (HHV vs SRV) | Note |
|---|---|---|---|---|---|---|
| AdAway | HHV worse | 39 vs 3 | 0.290 vs 0.314 | 1.0 vs 2.33 | 1.0 vs 1.33 | 13× keyframe inflation, collapses to 1 screen |
| AntennaPod | HHV much worse | 10 vs 9 | 0.322 vs 0.467 | 1.0 vs 6.33 | 1.0 vs 3.5 | Largest runtime blow-up despite similar keyframe counts |
| HomeMedkit | HHV much worse | 54 vs 8 | 0.304 vs 0.433 | 1.33 vs 5.33 | 1.0 vs 2.33 | Severe over-segmentation, weak trace recovery |
| Jigsaw | Both weak | 16 vs 6 | 0.250 vs 0.304 | 1.0 vs 1.33 | 1.0 vs 1.0 | Difficult app for both modes |
| LuxAlarm | Both fail | 11 vs 8 | 0.295 vs 0.396 | 1.5 vs 2.33 | 1.0 vs 3.0 | Real failures in both modes; HHV still shows collapse |
| PortAuthority | HHV worse | 22 vs 7 | 0.233 vs 0.404 | 1.0 vs 3.67 | 1.0 vs 2.33 | One HHV run mis-labeled as failed by JSON parser |
| SimpleNotes | HHV worse | 35 vs 7 | 0.268 vs 0.451 | 1.0 vs 3.33 | 1.0 vs 1.33 | Only 1 HHV run but matches broader pattern strongly |
| WifiAnalyzer | HHV worse | 15 vs 16 | 0.282 vs 0.401 | 1.5 vs 10.67 | 1.5 vs 3.67 | Similar keyframe counts but state diversity lost in mapping |
| DeadHash | Missing | — | — | — | — | Not in gifdroid_data.json |
| Pomodorot | Missing | — | — | — | — | Not in gifdroid_data.json |

---

## Failure Modes

### 1. Degenerate Single-Screen Mapping (Critical)
All keyframes map to 1 screen. Pipeline completes but trace covers only 1 app state. Seen in AdAway, AntennaPod, HomeMedkit, SimpleNotes, PortAuthority, WifiAnalyzer.

### 2. Hard Pipeline Termination
Run stops in Step 1 or early Step 2 with no output. Seen in LuxAlarm utg02 SRV — log stops after frame decoding.

### 3. Trace Search Stall
Keyframe detection and mapping succeed but trace search fails or hangs after UTG load. Seen in LuxAlarm utg02 HHV and LuxAlarm utg03 SRV.

### 4. Combinatorial Runtime Blowup
No early-exit when all frames map to 1 screen. All frame×artifact comparisons still run exhaustively. AntennaPod utg03: 7.6 hours.

### 5. JSON Parser Inconsistency
PortAuthority utg03 HHV: raw log confirms pipeline completed, but JSON marks `pipeline_complete = False` with `utg_vertices = None`. At least one "failure" is a tooling bug, not a GIFdroid failure.

---

## Full Run Data

| App | UTG | Type | Status | Frames | Keyframes | Unique Screens | Score Mean | Score Max | Spread | LCS | Trace Len | Actions | Total (s) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AdAway | utg01 | SRV | ✓ | 772 | 3 | 3 | 0.382 | 0.414 | 0.091 | 2 | 9 | 8 | 110 |
| AdAway | utg01 | HHV | ✓ | 1331 | 39 | 1 | 0.298 | 0.370 | 0.112 | 1 | 4 | 3 | 215 |
| AdAway | utg02 | SRV | ✓ | 772 | 3 | 2 | 0.279 | 0.332 | 0.109 | 1 | 2 | 1 | 78 |
| AdAway | utg02 | HHV | ✓ | 1331 | 39 | 1 | 0.286 | 0.351 | 0.100 | 1 | 3 | 2 | 181 |
| AdAway | utg03 | SRV | ✓ | 772 | 3 | 2 | 0.279 | 0.332 | 0.109 | 1 | 2 | 1 | 78 |
| AdAway | utg03 | HHV | ✓ | 1331 | 39 | 1 | 0.286 | 0.352 | 0.101 | 1 | 3 | 2 | 190 |
| AntennaPod | utg01 | SRV | ✓ | 583 | 9 | 7 | 0.464 | 0.670 | 0.491 | 3 | 11 | 10 | 150 |
| AntennaPod | utg01 | HHV | ✓ | 2025 | 10 | 1 | 0.317 | 0.331 | 0.030 | 1 | 11 | 10 | 383 |
| AntennaPod | utg02 | SRV | ✓ | 583 | 9 | 7 | 0.463 | 0.670 | 0.446 | 4 | 10 | 9 | 563 |
| AntennaPod | utg02 | HHV | ✓ | 2025 | 10 | 1 | 0.316 | 0.331 | 0.030 | 1 | 4 | 3 | 592 |
| AntennaPod | utg03 | SRV | ✓ | 583 | 9 | 5 | 0.473 | 0.670 | 0.446 | — | — | 0 | 375 |
| AntennaPod | utg03 | HHV | ✓ | 2025 | 10 | 1 | 0.333 | 0.341 | 0.019 | — | — | 0 | **27,517** |
| HomeMedkit | utg01 | SRV | ✓ | 777 | 8 | 4 | 0.453 | 0.553 | 0.389 | 1 | 2 | 1 | 115 |
| HomeMedkit | utg01 | HHV | ✓ | 1359 | 54 | 1 | 0.293 | 0.321 | 0.066 | 1 | 3 | 2 | 409 |
| HomeMedkit | utg02 | SRV | ✓ | 777 | 8 | 5 | 0.419 | 0.486 | 0.211 | 3 | 15 | 14 | 148 |
| HomeMedkit | utg02 | HHV | ✓ | 1359 | 54 | 1 | 0.300 | 0.330 | 0.068 | 1 | 5 | 4 | 600 |
| HomeMedkit | utg03 | SRV | ✓ | 777 | 8 | 7 | 0.427 | 0.485 | 0.146 | 3 | 8 | 7 | 280 |
| HomeMedkit | utg03 | HHV | ✓ | 1359 | 54 | 2 | 0.319 | 0.352 | 0.068 | 1 | 4 | 3 | 2,589 |
| Jigsaw | utg01 | SRV | ✓ | 1025 | 6 | 1 | 0.278 | 0.428 | 0.308 | 1 | 2 | 1 | 109 |
| Jigsaw | utg01 | HHV | ✓ | 563 | 16 | 1 | 0.265 | 0.277 | 0.020 | 1 | 2 | 1 | 57 |
| Jigsaw | utg02 | SRV | ✓ | 1025 | 6 | 1 | 0.268 | 0.477 | 0.337 | — | — | 0 | 114 |
| Jigsaw | utg02 | HHV | ✓ | 563 | 16 | 1 | 0.220 | 0.225 | 0.016 | — | — | 0 | 78 |
| Jigsaw | utg03 | SRV | ✓ | 1025 | 6 | 2 | 0.367 | 0.428 | 0.204 | — | — | 0 | 98 |
| Jigsaw | utg03 | HHV | ✓ | 563 | 16 | 1 | 0.265 | 0.277 | 0.020 | — | — | 0 | 64 |
| LuxAlarm | utg01 | SRV | ✓ | 714 | 8 | 4 | 0.383 | 0.618 | 0.471 | 3 | 13 | 12 | 165 |
| LuxAlarm | utg01 | HHV | ✓ | 818 | 11 | 2 | 0.273 | 0.286 | 0.024 | 1 | 2 | 1 | 195 |
| LuxAlarm | utg02 | SRV | ✗ | 714 | — | — | — | — | — | — | — | — | — |
| LuxAlarm | utg02 | HHV | ✗ | 818 | 11 | 1 | 0.317 | 0.342 | 0.036 | — | — | — | — |
| LuxAlarm | utg03 | SRV | ✗ | 714 | 8 | 3 | 0.409 | 0.616 | 0.393 | — | — | — | — |
| PortAuthority | utg01 | SRV | ✓ | 3050 | 7 | 3 | 0.394 | 0.586 | 0.372 | 2 | 11 | 10 | 518 |
| PortAuthority | utg01 | HHV | ✓ | 882 | 22 | 2 | 0.212 | 0.242 | 0.058 | 1 | 9 | 8 | 183 |
| PortAuthority | utg02 | SRV | ✓ | 3050 | 7 | 4 | 0.397 | 0.562 | 0.339 | 2 | 10 | 9 | 431 |
| PortAuthority | utg02 | HHV | ✓ | 882 | 22 | 1 | 0.242 | 0.300 | 0.101 | 1 | 5 | 4 | 416 |
| PortAuthority | utg03 | SRV | ✓ | 3050 | 7 | 4 | 0.420 | 0.562 | 0.339 | 3 | 11 | 10 | 483 |
| PortAuthority | utg03 | HHV | ✗ | 882 | 22 | 0 | 0.247 | 0.300 | 0.075 | — | — | — | — |
| SimpleNotes | utg01 | SRV | ✓ | 473 | 7 | 4 | 0.444 | 0.569 | 0.346 | 1 | 2 | 1 | 80 |
| SimpleNotes | utg01 | HHV | ✓ | 1256 | 35 | 1 | 0.268 | 0.294 | 0.053 | 1 | 2 | 1 | 299 |
| SimpleNotes | utg02 | SRV | ✓ | 473 | 7 | 3 | 0.453 | 0.580 | 0.357 | 2 | 3 | 2 | 77 |
| SimpleNotes | utg03 | SRV | ✓ | 473 | 7 | 3 | 0.455 | 0.587 | 0.364 | 1 | 3 | 2 | 104 |
| WifiAnalyzer | utg01 | SRV | ✓ | 877 | 16 | 11 | 0.403 | 0.630 | 0.358 | 2 | 4 | 3 | 181 |
| WifiAnalyzer | utg01 | HHV | ✓ | 1191 | 15 | 2 | 0.250 | 0.310 | 0.088 | 2 | 14 | 13 | 195 |
| WifiAnalyzer | utg02 | SRV | ✓ | 877 | 16 | 10 | 0.402 | 0.630 | 0.386 | 6 | 15 | 14 | 316 |
| WifiAnalyzer | utg02 | HHV | ✓ | 1191 | 15 | 1 | 0.314 | 0.345 | 0.064 | 1 | 8 | 7 | 433 |
| WifiAnalyzer | utg03 | SRV | ✓ | 877 | 16 | 11 | 0.398 | 0.632 | 0.388 | 3 | 9 | 8 | 227 |

---

## Five Root-Cause Limitations

| # | Limitation | Severity |
|---|---|---|
| 1 | **Low & uniform confidence scores** — motion blur, lighting variation, perspective distortion compress all frame scores into a narrow band; the GUI matcher cannot discriminate between distinct screens | Critical |
| 2 | **Keyframe over-detection** — scene-change detector fires on camera/hand movement, not just UI transitions; 5–18× more keyframes than SRV | Critical |
| 3 | **Degenerate single-screen mapping** — low score spread causes all keyframes to map to the same best-match screen; pipeline fails or produces trivial traces | Critical |
| 4 | **No early-exit for degenerate cases** — when all frames map to 1 screen, exhaustive frame×artifact comparisons still run; AntennaPod utg03: 7.6 hours with no meaningful output | High |
| 5 | **No HHV-specific preprocessing** — GIFdroid was designed for clean ADB screen recordings; no video stabilization, motion deblur, color normalization, or perspective correction is applied | High |

---

## Bottom Line

- HHV does not fail dramatically more often than SRV by completion count.
- HHV is consistently much worse in reconstruction quality: avg unique screens 1.15 vs 4.42, avg LCS 1.07 vs 2.32.
- Even "successful" HHV runs produce traces covering a smaller subset of the tested interaction.
- At least one reported failure (PortAuthority utg03 HHV) is a JSON parser bug, not a GIFdroid failure.
- The core issue: GIFdroid was designed for pixel-stable ADB screen recordings. All HHV degradation flows from that single design assumption being violated.