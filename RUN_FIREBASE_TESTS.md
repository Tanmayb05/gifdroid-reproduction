# run_firebase_tests.py — Quick Reference

Runs Firebase Robo tests for all APKs, downloads results, and organizes them into `app_<Name>/` directories.

---

## TL;DR — Most Common Commands

```bash
# Run everything with 10m timeout (default)
python run_firebase_tests.py

# Run everything with explicit 10m timeout
python run_firebase_tests.py --test-timeout 10m

# Run for a second UTG slot (utg02)
python run_firebase_tests.py --utg utg02 --test-timeout 10m

# Skip gcloud verification (faster if already verified)
python run_firebase_tests.py --skip-verify --test-timeout 10m
```

---

## Prerequisites

1. APKs placed in `apps/` directory (e.g. `apps/PortAuthority.apk`)
2. `gcloud` authenticated: `gcloud auth login`
3. Project set: `gcloud config set project gifdroid-reproduction`
4. APIs enabled:
   ```bash
   gcloud services enable testing.googleapis.com toolresults.googleapis.com
   ```

---

## What It Does (5 Phases)

| Phase | What happens |
|-------|-------------|
| 1 | Verifies gcloud install, auth, project, and APIs |
| 2 | Submits Robo tests for all APKs in `apps/` in parallel (blocks until done) |
| 3 | Verifies GCS result buckets are accessible |
| 4 | Downloads results from GCS to `firebase_downloads/<AppName>/` |
| 5 | Organizes into `app_<Name>/<utg>/input/` (utg.json + artifacts/) |

---

## Output Structure

```
app_<Name>/
└── utg01/                        # or utg02
    ├── input/
    │   ├── utg.json              # actions.json from Firebase
    │   ├── artifacts/            # screenshots (artifacts_1.png, ...)
    │   ├── screenrec/
    │   └── handheld/
    └── output/
```

---

## Run a Single Phase

```bash
python run_firebase_tests.py --phase 1   # verify gcloud
python run_firebase_tests.py --phase 2   # submit tests only
python run_firebase_tests.py --phase 3   # verify GCS buckets
python run_firebase_tests.py --phase 4   # download results
python run_firebase_tests.py --phase 5   # organize into app_* dirs
python run_firebase_tests.py --phase 5 --utg utg02   # organize into utg02 slot
```

---

## All Options

| Flag | Default | Description |
|------|---------|-------------|
| `--test-timeout` | `10m` | Robo test timeout per app. Use `1m` for quick testing. |
| `--utg` | `utg01` | UTG slot for Phase 5 output (`utg01` or `utg02`) |
| `--skip-verify` | off | Skip Phase 1 gcloud verification |
| `--phase` | all | Run only a specific phase (1–5) |

---

## Logs

All runs logged to `logs/run_<timestamp>.log`.

---

## Resuming After Failure

The script saves progress to `result_buckets.json` after each APK completes. Re-running will skip APKs already in that file. To re-run a specific APK, remove its entry from `result_buckets.json`.

---

## Device Used

All tests run on: `Pixel2.arm, Android 28, portrait, en`