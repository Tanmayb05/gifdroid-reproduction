# GIFdroid Run Analysis

## Comparison Points

- `utg.json`: event count, unique screens, and execution-result distribution.
- Input artifacts: total PNGs, screenshots excluding `artifacts_sitemap.png`, and whether the sitemap exists.
- Outputs: presence of `execution_<hhv/srv>_<app>.json`, replay-trace count, total trace length, max trace length, and action-type mix.
- Logs: keyframe count, screenshots loaded, mapping diversity, average mapping score, skipped runs, incomplete pipelines, and warnings.

## Per-Run Summary

| App | Run | UTG events | Screens | Artifacts | HHV | SRV |
| --- | --- | ---: | ---: | ---: | --- | --- |
| AdAway | utg01 | 50 | 20 | 19 | out:1 trace(s), 3 step(s), kf:39, map:1 unique | out:1 trace(s), 8 step(s), kf:3, map:3 unique |
| AdAway | utg02 | 5 | 4 | 4 | out:1 trace(s), 2 step(s) | skipped, out:1 trace(s), 1 step(s) |
| AntennaPod | utg01 | 218 | 96 | 96 | skipped, out:1 trace(s), 10 step(s) | out:1 trace(s), 10 step(s), kf:9, map:7 unique |
| AntennaPod | utg02 | 403 | 151 | 151 | out:1 trace(s), 3 step(s) | skipped, out:1 trace(s), 9 step(s) |
| DeadHash | utg01 | - | - | - | missing | missing |
| DeadHash | utg02 | - | - | 0 | missing | missing |
| HomeMedkit | utg01 | 127 | 49 | 48 | out:1 trace(s), 2 step(s), kf:54, map:1 unique | skipped, out:1 trace(s), 1 step(s) |
| HomeMedkit | utg02 | 298 | 80 | 80 | out:1 trace(s), 4 step(s) | skipped, out:1 trace(s), 14 step(s) |
| Jigsaw | utg01 | 3 | 2 | 1 | skipped, out:1 trace(s), 1 step(s) | out:1 trace(s), 1 step(s), kf:6, map:1 unique |
| Jigsaw | utg02 | 2 | 2 | 2 | out:0 trace(s), 0 step(s), kf:16, map:1 unique, warning | out:0 trace(s), 0 step(s), kf:6, map:1 unique, warning |
| LuxAlarm | utg01 | 298 | 96 | 95 | out:1 trace(s), 1 step(s), kf:11, map:2 unique | out:1 trace(s), 12 step(s), kf:8, map:4 unique |
| LuxAlarm | utg02 | 331 | 25 | 25 | missing | no output, kf:8, map:4 unique, incomplete |
| Pomodorot | utg01 | - | - | - | missing | missing |
| Pomodorot | utg02 | - | - | 0 | missing | missing |
| PortAuthority | utg01 | 207 | 41 | 41 | out:4 trace(s), 32 step(s), kf:22, map:2 unique | skipped, out:1 trace(s), 10 step(s) |
| PortAuthority | utg02 | 254 | 88 | 88 | no output, kf:22, map:1 unique, incomplete | out:4 trace(s), 36 step(s), kf:7, map:4 unique |
| SimpleNotes | utg01 | 190 | 48 | 47 | out:1 trace(s), 1 step(s), kf:35, map:1 unique | missing |
| SimpleNotes | utg02 | 297 | 34 | 34 | missing | out:1 trace(s), 2 step(s), kf:7, map:3 unique |
| WifiAnalyzer | utg01 | 135 | 48 | 47 | out:1 trace(s), 13 step(s), kf:15, map:2 unique | out:1 trace(s), 3 step(s), kf:16, map:11 unique |
| WifiAnalyzer | utg02 | 232 | 50 | 50 | missing | out:2 trace(s), 28 step(s), kf:16, map:10 unique |

## UTG01 vs UTG02 Deltas

| App | Events delta | Screen delta | Artifact delta |
| --- | ---: | ---: | ---: |
| AdAway | -45 | -16 | -15 |
| AntennaPod | 185 | 55 | 55 |
| DeadHash | - | - | - |
| HomeMedkit | 171 | 31 | 32 |
| Jigsaw | -1 | 0 | 1 |
| LuxAlarm | 33 | -71 | -70 |
| Pomodorot | - | - | - |
| PortAuthority | 47 | 47 | 47 |
| SimpleNotes | 107 | -14 | -13 |
| WifiAnalyzer | 97 | 2 | 3 |

## Notable Findings

- AdAway utg01 HHV: all or nearly all keyframes collapsed onto `artifacts_5.png` (39/39 matches).
- HomeMedkit utg01 HHV: all or nearly all keyframes collapsed onto `artifacts_15.png` (54/54 matches).
- Jigsaw utg01 SRV: all or nearly all keyframes collapsed onto `artifacts_1.png` (6/6 matches).
- Jigsaw utg02 HHV: output exists but contains zero replay traces.
- Jigsaw utg02 HHV: all or nearly all keyframes collapsed onto `artifacts_2.png` (16/16 matches).
- Jigsaw utg02 SRV: output exists but contains zero replay traces.
- Jigsaw utg02 SRV: all or nearly all keyframes collapsed onto `artifacts_2.png` (6/6 matches).
- LuxAlarm utg02 SRV: log exists but pipeline did not complete.
- PortAuthority utg02 HHV: log exists but pipeline did not complete.
- PortAuthority utg02 HHV: all or nearly all keyframes collapsed onto `artifacts_13.png` (20/20 matches).
- SimpleNotes utg01 HHV: all or nearly all keyframes collapsed onto `artifacts_1.png` (35/35 matches).

## Raw Data

See `gifdroid_run_analysis.json` for the full machine-readable extraction.
