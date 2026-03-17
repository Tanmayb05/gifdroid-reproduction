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