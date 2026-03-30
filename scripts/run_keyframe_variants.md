# run_keyframe_variants.py

Runs all (or selected) keyframe detection methods for specified app/utg pairs, using handheld video as input.

## What it does

For each `app` + `utg` entry in the config, it invokes `python -m gifdroid.main` once per keyframe method. The 6 available methods are:

| Method | Description |
|---|---|
| `baseline` | SSIM-based consecutive-frame similarity |
| `stabilize` | FFmpeg video stabilization before SSIM |
| `hysteresis` | Requires k following frames to also be stable |
| `homography` | Homography transformation to remove camera motion |
| `clip` | Baseline + CLIP clustering to deduplicate similar screens |
| `vlm` | Baseline + VLM (llama3.2-vision via Ollama) filtering |

Runs are **idempotent** — a run is skipped if its output JSON already exists. Use `--force` to override.

## Usage

```bash
# Run all 6 methods for entries in the default config
python scripts/run_keyframe_variants.py

# Use a custom config file
python scripts/run_keyframe_variants.py --config path/to/config.yml

# Run only specific methods
python scripts/run_keyframe_variants.py --methods baseline stabilize

# Preview commands without executing
python scripts/run_keyframe_variants.py --dry-run

# Re-run even if output already exists
python scripts/run_keyframe_variants.py --force
```

Default config path: `scripts/data/keyframe_runs.yml`

## Config format

```yaml
runs:
  - app: AdAway
    utg: utg01             # single utg slot

  - app: LuxAlarm
    utg: [utg01, utg02]    # multiple utg slots
```

- `app` must match the folder name `app_<AppName>/`
- `utg` is `utg01`, `utg02`, or `utg03` (string or list)

## Expected input structure

Each app/utg entry must have:

```
app_<AppName>/
  <utg>/
    input/
      handheld/hhv_app_<AppName>.mp4
      utg.json
      artifacts/
```

The script validates these paths before running and skips the entry with an error message if any are missing.

## Output

```
app_<AppName>/
  <utg>/
    output/
      execution_hhv_<AppName>_<method>.json
      keyframes_<method>/
```

## Exit behaviour

- Exits `0` if all runs succeeded (or were skipped).
- Exits `1` if any run failed, and lists the failed entries.