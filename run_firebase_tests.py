#!/usr/bin/env python3
"""
GIFdroid Reproduction - Firebase Robo Test Runner

This script:
1. Verifies gcloud setup (project, auth, APIs)
2. Runs Firebase Robo tests for all APKs in apps/ (in parallel)
3. Saves result bucket paths to result_buckets.json
4. Monitors test completion status
5. Downloads results via gsutil
6. Organizes results into app_<name>/ directories with utg.json and artifacts/

All output is logged to logs/run_<timestamp>.log
"""

import subprocess
import json
import os
import sys
import glob
import shutil
import time
import re
import argparse
import logging
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
APPS_DIR = os.path.join(PROJECT_ROOT, "apps")
RESULT_BUCKETS_FILE = os.path.join(PROJECT_ROOT, "result_buckets.json")
DOWNLOAD_DIR = os.path.join(PROJECT_ROOT, "firebase_downloads")
LOGS_DIR = os.path.join(PROJECT_ROOT, "logs")

DEVICE = "model=Pixel2.arm,version=28,locale=en,orientation=portrait"

# Ensure gcloud/gsutil are on PATH (installed via google-cloud-sdk)
_home = os.path.expanduser("~")
GCLOUD_SDK_PATH = os.path.join(_home, "google-cloud-sdk", "bin")
if os.path.isdir(GCLOUD_SDK_PATH) and GCLOUD_SDK_PATH not in os.environ.get("PATH", ""):
    os.environ["PATH"] = GCLOUD_SDK_PATH + ":" + os.environ.get("PATH", "")

# --- Logging setup ---
os.makedirs(LOGS_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOGS_DIR, f"run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

logger = logging.getLogger("gifdroid")
logger.setLevel(logging.DEBUG)

# File handler — everything goes to log file
fh = logging.FileHandler(LOG_FILE)
fh.setLevel(logging.DEBUG)
fh.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
logger.addHandler(fh)

# Console handler — also print to stdout
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
ch.setFormatter(logging.Formatter("%(message)s"))
logger.addHandler(ch)


def log(msg, level="info"):
    getattr(logger, level)(msg)


def run_cmd(cmd, capture=True, check=True):
    """Run a shell command and return stdout."""
    log(f"  $ {cmd}", "debug")
    result = subprocess.run(
        cmd, shell=True, capture_output=capture, text=True,
        env=os.environ,
    )
    if capture:
        if result.stdout:
            log(f"  STDOUT: {result.stdout.strip()}", "debug")
        if result.stderr:
            log(f"  STDERR: {result.stderr.strip()}", "debug")
    if check and result.returncode != 0:
        log(f"  Command failed (rc={result.returncode}): {result.stderr.strip()}", "warning")
        return None
    return result.stdout.strip() if capture else ""


def phase1_verify_gcloud():
    """Phase 1: Verify gcloud installation, project, auth, and APIs."""
    log("\n" + "=" * 60)
    log("PHASE 1: Verifying gcloud setup")
    log("=" * 60)

    # 1. gcloud version
    log("\n[1/5] Checking gcloud version...")
    version = run_cmd("gcloud version 2>&1 | head -1", check=False)
    if version and "Google Cloud SDK" in version:
        log(f"  gcloud installed: {version}")
    else:
        log(f"  ERROR: gcloud not found. Output: {version}", "error")
        sys.exit(1)

    # 2. Check current project
    log("\n[2/5] Checking current project...")
    project = run_cmd("gcloud config get-value project 2>/dev/null")
    log(f"  Current project: {project}")

    # 3. Set project if needed
    if project != "gifdroid-reproduction":
        log("\n[3/5] Setting project to gifdroid-reproduction...")
        run_cmd("gcloud config set project gifdroid-reproduction")
        project = run_cmd("gcloud config get-value project 2>/dev/null")
        log(f"  Project now: {project}")
    else:
        log("\n[3/5] Project already set to gifdroid-reproduction. Skipping.")

    # 4. Verify auth
    log("\n[4/5] Checking authentication...")
    auth = run_cmd("gcloud auth list --format='value(account)' --filter='status:ACTIVE'")
    if auth:
        log(f"  Authenticated as: {auth}")
    else:
        log("  ERROR: No active authentication found. Run: gcloud auth login", "error")
        sys.exit(1)

    # 5. Verify APIs
    log("\n[5/5] Checking required APIs...")
    apis = run_cmd(
        'gcloud services list --enabled --filter="name:(testing.googleapis.com OR toolresults.googleapis.com)" --format="value(name)"'
    )
    if apis:
        for api in apis.split("\n"):
            log(f"  Enabled: {api}")
    else:
        log("  ERROR: Required APIs not enabled.", "error")
        log("  Run: gcloud services enable testing.googleapis.com toolresults.googleapis.com")
        sys.exit(1)

    log("\n  Phase 1 complete. All checks passed.")


def _run_single_robo_test(apk_path, test_timeout):
    """Run a single Robo test. Returns (apk_name, result_dict)."""
    apk_name = os.path.basename(apk_path).replace(".apk", "")

    log(f"  [{apk_name}] Launching Robo test (timeout={test_timeout})...")

    cmd = (
        f"gcloud firebase test android run"
        f" --type robo"
        f" --app {apk_path}"
        f" --device {DEVICE}"
        f" --timeout {test_timeout}"
        f" 2>&1"
    )

    result = subprocess.run(
        cmd, shell=True, capture_output=True, text=True, env=os.environ,
    )
    output = result.stdout.strip()

    # Log full output to file
    log(f"  [{apk_name}] Full gcloud output:\n{output}", "debug")

    # Log last 15 lines to console
    tail_lines = output.split("\n")[-15:]
    log(f"\n  [{apk_name}] Output (last 15 lines):")
    for line in tail_lines:
        log(f"    {line}")

    result_info = {"status": "submitted"}

    # Check if test was skipped (incompatible environment)
    if "Incompatible Environment" in output or "does not support" in output:
        result_info["status"] = "skipped"
        log(f"  [{apk_name}] Test SKIPPED (incompatible environment).", "warning")

    # Parse GCS result bucket from output
    # Format: https://console.developers.google.com/storage/browser/<bucket>/<path>/
    gcs_url_match = re.search(
        r"console\.developers\.google\.com/storage/browser/([^/\]]+)/([^\]\s]+)",
        output,
    )
    if gcs_url_match:
        bucket = gcs_url_match.group(1)
        path = gcs_url_match.group(2).rstrip("/")
        gcs_path = f"gs://{bucket}/{path}/"
        result_info["gcs_path"] = gcs_path
        log(f"  [{apk_name}] Result bucket: {gcs_path}")
    else:
        # Fallback: try gs:// format directly
        gcs_match = re.search(r"\[?(gs://[^\]\s]+)\]?", output)
        if gcs_match:
            gcs_path = gcs_match.group(1)
            result_info["gcs_path"] = gcs_path
            log(f"  [{apk_name}] Result bucket: {gcs_path}")
        else:
            log(f"  [{apk_name}] WARNING: Could not parse GCS path from output.", "warning")
            result_info["gcs_path"] = None
            if result_info["status"] == "submitted":
                result_info["status"] = "unknown"
            result_info["raw_output_tail"] = tail_lines

    # Parse test matrix ID
    matrix_match = re.search(r"Test \[matrix-([a-zA-Z0-9]+)\]", output)
    if matrix_match:
        matrix_id = f"matrix-{matrix_match.group(1)}"
        result_info["matrix_id"] = matrix_id
        log(f"  [{apk_name}] Matrix ID: {matrix_id}")

    return apk_name, result_info


def phase2_run_robo_tests(test_timeout="10m"):
    """Phase 2: Run Firebase Robo tests for all APKs in parallel."""
    log("\n" + "=" * 60)
    log(f"PHASE 2: Running Firebase Robo Tests (parallel, timeout={test_timeout})")
    log("=" * 60)

    apk_files = sorted(glob.glob(os.path.join(APPS_DIR, "*.apk")))
    if not apk_files:
        log("  ERROR: No APK files found in apps/", "error")
        sys.exit(1)

    log(f"  Found {len(apk_files)} APKs:")
    for apk in apk_files:
        log(f"    - {os.path.basename(apk)}")

    # Load existing results if any (to allow resuming)
    result_buckets = {}
    if os.path.exists(RESULT_BUCKETS_FILE):
        with open(RESULT_BUCKETS_FILE, "r") as f:
            result_buckets = json.load(f)
        log(f"\n  Loaded {len(result_buckets)} existing results from result_buckets.json")

    # Filter out APKs that already have results
    apks_to_run = []
    for apk_path in apk_files:
        apk_name = os.path.basename(apk_path).replace(".apk", "")
        if apk_name in result_buckets:
            log(f"  [{apk_name}] Already has results. Skipping.")
        else:
            apks_to_run.append(apk_path)

    if not apks_to_run:
        log("  All APKs already have results. Nothing to do.")
        return result_buckets

    log(f"\n  Launching {len(apks_to_run)} Robo tests in parallel...")

    # Run all tests in parallel using ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=len(apks_to_run)) as executor:
        futures = {
            executor.submit(_run_single_robo_test, apk_path, test_timeout): apk_path
            for apk_path in apks_to_run
        }

        for future in as_completed(futures):
            apk_path = futures[future]
            try:
                apk_name, result_info = future.result()
                result_buckets[apk_name] = result_info
                log(f"  [{apk_name}] Test submission complete.")
            except Exception as e:
                apk_name = os.path.basename(apk_path).replace(".apk", "")
                log(f"  [{apk_name}] ERROR: {e}", "error")
                result_buckets[apk_name] = {"status": "error", "error": str(e)}

            # Save after each completion (for resilience)
            with open(RESULT_BUCKETS_FILE, "w") as f:
                json.dump(result_buckets, f, indent=2)

    log(f"\n  Phase 2 complete. Results saved to result_buckets.json")
    return result_buckets


def phase3_monitor_tests(result_buckets):
    """Phase 3: Verify test results exist in GCS buckets.

    Note: `gcloud firebase test android run` blocks until the test finishes,
    so by the time Phase 2 completes, all tests are already done.
    This phase verifies results are available by listing the GCS bucket.
    """
    log("\n" + "=" * 60)
    log("PHASE 3: Verifying Test Results in GCS")
    log("=" * 60)

    for apk_name, info in result_buckets.items():
        gcs_path = info.get("gcs_path")
        if not gcs_path:
            log(f"  [{apk_name}] No GCS path. Status: {info.get('status', 'unknown')}")
            continue

        log(f"  [{apk_name}] Listing {gcs_path} ...")
        cmd = f"gsutil ls {gcs_path} 2>&1"
        output = run_cmd(cmd, check=False)
        if output and "CommandException" not in output:
            file_count = len([l for l in output.strip().split("\n") if l.strip()])
            log(f"  [{apk_name}] Found {file_count} entries in GCS. Test completed.")
            info["status"] = "completed"
            # Log first few entries
            for line in output.strip().split("\n")[:5]:
                log(f"    {line}", "debug")
        else:
            log(f"  [{apk_name}] GCS bucket not accessible or empty. Output: {output[:200]}", "warning")
            info["status"] = "unknown"

    # Save updated statuses
    with open(RESULT_BUCKETS_FILE, "w") as f:
        json.dump(result_buckets, f, indent=2)

    # Summary
    log("\n  Summary:")
    for apk_name, info in result_buckets.items():
        log(f"    {apk_name}: status={info.get('status')}, gcs={info.get('gcs_path', 'N/A')}")

    return result_buckets


def phase4_download_results(result_buckets):
    """Phase 4: Download results using gsutil."""
    log("\n" + "=" * 60)
    log("PHASE 4: Downloading Results")
    log("=" * 60)

    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    for apk_name, info in result_buckets.items():
        gcs_path = info.get("gcs_path")
        if not gcs_path:
            log(f"  [{apk_name}] No GCS path. Skipping download.")
            continue

        local_dir = os.path.join(DOWNLOAD_DIR, apk_name)
        if os.path.exists(local_dir) and os.listdir(local_dir):
            log(f"  [{apk_name}] Already downloaded. Skipping.")
            continue

        os.makedirs(local_dir, exist_ok=True)

        log(f"  [{apk_name}] Downloading from {gcs_path} ...")
        cmd = (
            f'gsutil -o "GSUtil:parallel_process_count=1"'
            f" -m cp -r {gcs_path} {local_dir}/"
        )
        run_cmd(cmd, capture=False, check=False)

        # Verify download
        downloaded_files = []
        for root, dirs, files in os.walk(local_dir):
            for f in files:
                downloaded_files.append(os.path.join(root, f))
        log(f"  [{apk_name}] Downloaded {len(downloaded_files)} files.")
        info["download_dir"] = local_dir
        info["file_count"] = len(downloaded_files)

    # Save updated info
    with open(RESULT_BUCKETS_FILE, "w") as f:
        json.dump(result_buckets, f, indent=2)

    log(f"\n  Phase 4 complete. Files downloaded to {DOWNLOAD_DIR}/")
    return result_buckets


def phase5_organize_results(result_buckets):
    """
    Phase 5: Organize results into app_<name>/ directories.

    Structure:
        app_<Name>/
        ├── utg.json        (activity_map.json renamed)
        └── artifacts/      (all PNG screenshots)
    """
    log("\n" + "=" * 60)
    log("PHASE 5: Organizing Results")
    log("=" * 60)

    for apk_name, info in result_buckets.items():
        download_dir = info.get("download_dir", os.path.join(DOWNLOAD_DIR, apk_name))
        if not os.path.exists(download_dir):
            log(f"  [{apk_name}] Download directory not found. Skipping.")
            continue

        app_dir = os.path.join(PROJECT_ROOT, f"app_{apk_name}")
        artifacts_dir = os.path.join(app_dir, "artifacts")
        os.makedirs(artifacts_dir, exist_ok=True)

        log(f"\n  [{apk_name}] Organizing into {app_dir}/")

        # Find and copy UTG JSON file -> utg.json
        # Firebase Robo produces: actions.json (primary UTG), crawlscript.json
        # Priority: actions.json > activity_map.json > crawlscript.json
        utg_found = False
        utg_candidates = ["actions.json", "activity_map.json", "crawlscript.json"]
        for candidate in utg_candidates:
            if utg_found:
                break
            for root, dirs, files in os.walk(download_dir):
                if candidate in files:
                    src = os.path.join(root, candidate)
                    dest = os.path.join(app_dir, "utg.json")
                    shutil.copy2(src, dest)
                    log(f"    Copied {candidate} -> utg.json")
                    utg_found = True
                    break

        # Copy all PNG screenshots to artifacts/
        for root, dirs, files in os.walk(download_dir):
            for f in files:
                fpath = os.path.join(root, f)
                if f.lower().endswith(".png"):
                    dest = os.path.join(artifacts_dir, f)
                    if os.path.exists(dest):
                        base, ext = os.path.splitext(f)
                        counter = 1
                        while os.path.exists(dest):
                            dest = os.path.join(artifacts_dir, f"{base}_{counter}{ext}")
                            counter += 1
                    shutil.copy2(fpath, dest)

        if not utg_found:
            log(f"    WARNING: No UTG JSON found. Available JSON files:", "warning")
            for root, dirs, files in os.walk(download_dir):
                for f in files:
                    if f.endswith(".json"):
                        log(f"    {os.path.relpath(os.path.join(root, f), download_dir)}")

        png_count = len(glob.glob(os.path.join(artifacts_dir, "*.png")))
        utg_exists = os.path.exists(os.path.join(app_dir, "utg.json"))
        log(f"    PNG screenshots: {png_count}")
        log(f"    utg.json present: {utg_exists}")

    log(f"\n  Phase 5 complete. App directories created in project root.")


def main():
    parser = argparse.ArgumentParser(description="GIFdroid Firebase Robo Test Runner")
    parser.add_argument(
        "--phase", type=int, choices=[1, 2, 3, 4, 5],
        help="Run a specific phase only (1-5). Omit to run all phases."
    )
    parser.add_argument(
        "--skip-verify", action="store_true",
        help="Skip Phase 1 gcloud verification."
    )
    parser.add_argument(
        "--test-timeout", type=str, default="10m",
        help="Timeout for each Robo test (default: 10m). Use 1m for quick testing."
    )
    args = parser.parse_args()

    log("GIFdroid Reproduction - Firebase Robo Test Runner")
    log(f"Project root: {PROJECT_ROOT}")
    log(f"APKs directory: {APPS_DIR}")
    log(f"Log file: {LOG_FILE}")

    if args.phase:
        if args.phase == 1:
            phase1_verify_gcloud()
        elif args.phase == 2:
            phase2_run_robo_tests(test_timeout=args.test_timeout)
        elif args.phase == 3:
            with open(RESULT_BUCKETS_FILE, "r") as f:
                result_buckets = json.load(f)
            phase3_monitor_tests(result_buckets)
        elif args.phase == 4:
            with open(RESULT_BUCKETS_FILE, "r") as f:
                result_buckets = json.load(f)
            phase4_download_results(result_buckets)
        elif args.phase == 5:
            with open(RESULT_BUCKETS_FILE, "r") as f:
                result_buckets = json.load(f)
            phase5_organize_results(result_buckets)
        return

    # Run all phases
    if not args.skip_verify:
        phase1_verify_gcloud()

    result_buckets = phase2_run_robo_tests(test_timeout=args.test_timeout)

    # gcloud firebase test android run blocks until done, so tests are
    # already complete. Phase 3 just verifies GCS results exist.
    result_buckets = phase3_monitor_tests(result_buckets)

    phase4_download_results(result_buckets)
    phase5_organize_results(result_buckets)

    log("\n" + "=" * 60)
    log("ALL PHASES COMPLETE")
    log("=" * 60)
    log(f"\nResult buckets: {RESULT_BUCKETS_FILE}")
    log(f"Downloads:      {DOWNLOAD_DIR}/")
    log(f"Log file:       {LOG_FILE}")
    log(f"App directories:")
    for apk_name in result_buckets:
        app_dir = os.path.join(PROJECT_ROOT, f"app_{apk_name}")
        log(f"  {app_dir}/")


if __name__ == "__main__":
    main()
