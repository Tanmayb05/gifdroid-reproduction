# Running GIFdroid — Quick Reference

---

## Full Workflow (Every Time)

```bash
# 1. Activate venv
source .venv/bin/activate

# 2. Run prerequisites (checks deps, converts MOV→mp4, regenerates commands.txt)
python src_gifdroid/prerequisites.py --handheld --utg utg03

# 3. Run all commands
python run_all.py
```

---

## Step 1 — Activate venv

```bash
source .venv/bin/activate
```

---

## Step 2 — Run prerequisites.py

Must be run before GIFdroid. It:
- Checks Python dependencies (cv2, numpy, skimage, etc.)
- Checks ffmpeg is available
- Validates `input/utg.json` and `input/artifacts/` exist for each app/utg slot
- Converts handheld `.MOV` → `.mp4` (only with `--handheld`)
- Regenerates `commands.txt` with the correct paths

```bash
# All apps, all utg slots (no handheld)
python src_gifdroid/prerequisites.py

# All apps, all utg slots (include handheld videos)
python src_gifdroid/prerequisites.py --handheld

# Specific utg slot only
python src_gifdroid/prerequisites.py --handheld --utg utg03

# Single app, specific utg slot
python src_gifdroid/prerequisites.py --handheld --app PortAuthority --utg utg03
```

---

## Step 3 — Run GIFdroid

### Option A: Run all commands from commands.txt (batch)

```bash
python run_all.py
```

### Option B: Run a single app manually

```bash
# handheld video
python -m src_gifdroid.main \
  --video app_PortAuthority/utg03/input/handheld/hhv_app_PortAuthority.mp4 \
  --utg app_PortAuthority/utg03/input/utg.json \
  --artifact app_PortAuthority/utg03/input/artifacts \
  --out app_PortAuthority/utg03/output/execution_hhv_PortAuthority.json

# screen recording
python -m src_gifdroid.main \
  --video app_PortAuthority/utg03/input/screenrec/srv_app_PortAuthority.mp4 \
  --utg app_PortAuthority/utg03/input/utg.json \
  --artifact app_PortAuthority/utg03/input/artifacts \
  --out app_PortAuthority/utg03/output/execution_srv_PortAuthority.json
```

### Option C: Dry-run (preview commands without executing)

```bash
python run_all.py --dry-run
```

---

## All prerequisites.py Options

| Flag | Default | Description |
|------|---------|-------------|
| `--handheld` | off | Convert `.MOV` → `.mp4` and include handheld commands in `commands.txt` |
| `--utg` | all slots | Filter to a specific UTG slot (e.g. `utg03`) |
| `--app` | all apps | Filter to a single app (e.g. `PortAuthority`) |

---

## Output

Results are written to `app_<Name>/<utg>/output/`:
- `execution_srv_<Name>.json` — screen recording result
- `execution_hhv_<Name>.json` — handheld result
- `keyframes/` — extracted keyframe PNGs (auto-created)

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `ModuleNotFoundError` | Re-activate venv: `source .venv/bin/activate` |
| `ffmpeg not found` | Install ffmpeg: `brew install ffmpeg` |
| `missing input/utg.json` | Run Firebase tests first, then `run_firebase_tests.py --phase 5 --utg utg03` |
| `missing input/artifacts/` | Same as above |
| MOV not converting | Make sure `--handheld` flag is passed to prerequisites.py |