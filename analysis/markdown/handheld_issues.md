# Handheld Video Issues

## OpenCV Can't Read Video Stream

**Error:**
```
OpenCV: Couldn't read video stream from file "..."
cv2.error: Assertion failed VScn::contains(scn) in CvtHelper
```

**Root causes:**
1. **Wrong path** — video was at `app_AdAway/handheld_video_AdAway.mp4` but command passed `app_AdAway/handheld/handheld_video_AdAway.mp4`
2. **bt2020 color space** — iPhone/handheld videos recorded with HDR use bt2020 color space; OpenCV 3.4.2 cannot decode this

**Fix:** Convert the video to standard H.264 with bt709 color space before running GIFdroid:
```bash
ffmpeg -i <input.mp4> \
  -vf "scale=1080:1920,format=yuv420p" \
  -c:v libx264 -pix_fmt yuv420p \
  -color_range 1 -colorspace bt709 -color_trc bt709 -color_primaries bt709 \
  <output_in_correct_path.mp4> -y
```

Place the output at the path expected by the `--video` argument.

**Why:** OpenCV 3.4.2 does not support wide-gamut/HDR color spaces (bt2020). Converting to bt709 makes it compatible.

---

## No Execution Trace Found (Empty Output)

**Error:**

```text
ValueError: min() arg is an empty sequence
```

**Root cause:** The UTG has no path from node 0 to the last screen ID in the keyframe sequence. This happens when the keyframe location maps to a screen that is unreachable from the start node in the UTG graph — common with handheld videos where extra frames or motion artifacts push the final keyframe to a wrong screen ID.

**Fix applied:** `find_execution_trace` in `trace.py` now guards against an empty candidate set and returns `[]` with a warning log instead of crashing:

```text
WARNING  gifdroid.trace: no paths found from node 0 to screen X in the UTG (sequence=[...]). Returning empty trace.
```

The output JSON is still written with an empty `replay_traces` list, and the run is marked complete (idempotent — won't re-run).

**Why:** The LCS-based path search requires a reachable path in the UTG. If the mapped screen ID is wrong or the UTG is incomplete, no candidate paths exist and the min() call fails on an empty list.
