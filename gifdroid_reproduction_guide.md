# GIFdroid Reproduction Guide - Firebase Robo Setup

## Overview
This guide helps you reproduce the GIFdroid paper results using Firebase Test Lab's Robo test for UTG generation.

## Prerequisites

### 1. Install Required Tools
```bash
# Install gcloud CLI
# For Ubuntu/Debian:
curl https://sdk.cloud.google.com | bash
exec -l $SHELL

# Initialize gcloud
gcloud init

# Install Firebase CLI
npm install -g firebase-tools
firebase login
```

### 2. Set Up Google Cloud Project
```bash
# Create a new project (or use existing)
gcloud projects create gifdroid-reproduction --name="GIFdroid Reproduction"

# Set the project
gcloud config set project gifdroid-reproduction

# Enable required APIs
gcloud services enable testing.googleapis.com
gcloud services enable toolresults.googleapis.com
gcloud services enable firebasehosting.googleapis.com
```

### 3. Authenticate
```bash
# Authenticate with Google Cloud
gcloud auth login

# Set up application default credentials
gcloud auth application-default login
```

## Step 1: Collect Android APKs

### Option A: Use Apps from Android-Functional-bugs-study
The repository you mentioned contains bug reports. Download APKs from:
- F-Droid (https://f-droid.org/)
- GitHub releases of open-source apps
- The paper used 31 apps - see Table 5 in the paper for app names

### Option B: Paper's Original Apps
From Table 5 in the paper, the apps include:
- Token, TimeTracker, TrackerControl, YoloSec
- DeadHash, GNUCash, aFreeRDP, AntennaPod
- ProtonVPN, FastNFitness, JioFi, WiFiAnalyzer
- PSLab, DroidWeight, openScale, KeePassDX
- Trigger, ADBungFu, EteSyncNotes, PortAuthority
- ATime, AdAway, StinglePhoto, InviZible
- (and more - see full table in paper)

### Download Example Apps
```bash
# Create apps directory
mkdir -p ~/gifdroid-reproduction/apps
cd ~/gifdroid-reproduction/apps

# Example: Download from F-Droid
# You'll need to find the package names and download APKs manually
# Or use f-droid API/mirror sites
```

## Step 2: Run Firebase Robo Test to Generate UTG

### Basic Robo Test Command
```bash
# Run Robo test for a single app
gcloud firebase test android run \
  --type robo \
  --app path/to/your-app.apk \
  --device model=Pixel2,version=28,locale=en,orientation=portrait \
  --timeout 5m \
  --results-bucket=gs://your-bucket-name \
  --results-dir=your-app-name

# The paper used varied configurations:
# - Multiple device models
# - Android API levels
# - Different exploration times
```

### Recommended Configuration (Based on Paper)
```bash
# For comprehensive UTG generation
gcloud firebase test android run \
  --type robo \
  --app your-app.apk \
  --device model=Pixel2,version=28 \
  --robo-script robo-script.json \
  --timeout 10m \
  --num-flaky-test-attempts=0 \
  --directories-to-pull /sdcard \
  --results-bucket=gs://gifdroid-utg-results \
  --results-dir=$(date +%Y%m%d_%H%M%S)_app-name
```

### Batch Processing Multiple Apps
```bash
#!/bin/bash
# batch_robo_test.sh

APPS_DIR="./apps"
RESULTS_BUCKET="gs://gifdroid-utg-results"

for apk in $APPS_DIR/*.apk; do
    APP_NAME=$(basename "$apk" .apk)
    echo "Running Robo test for: $APP_NAME"
    
    gcloud firebase test android run \
      --type robo \
      --app "$apk" \
      --device model=Pixel2,version=28,locale=en,orientation=portrait \
      --timeout 10m \
      --results-bucket=$RESULTS_BUCKET \
      --results-dir="${APP_NAME}_$(date +%Y%m%d_%H%M%S)"
    
    echo "Completed: $APP_NAME"
    echo "---"
done
```

## Step 3: Download UTG Data

### Understanding Robo Test Outputs
Firebase Robo generates:
- **Screenshots**: PNG files of each UI state
- **activity_map.json**: Activity transitions and UI hierarchy
- **logcat**: System logs
- **video.mp4**: Screen recording of exploration
- **crawl_graph.png**: Visual representation of UTG

### Download Results
```bash
# List available test results
gsutil ls gs://gifdroid-utg-results/

# Download specific test results
gsutil -m cp -r gs://gifdroid-utg-results/your-app-name ~/gifdroid-reproduction/utg-data/

# Or download all
gsutil -m cp -r gs://gifdroid-utg-results/* ~/gifdroid-reproduction/utg-data/
```

### Extract UTG Information
```python
# extract_utg.py
import json
import os
from pathlib import Path

def extract_utg_from_robo(robo_results_dir):
    """
    Extract UTG information from Firebase Robo test results
    """
    utg_data = {
        'nodes': [],  # GUI states
        'edges': [],  # Transitions
        'screenshots': {}  # State -> screenshot mapping
    }
    
    # Parse activity_map.json
    activity_map_path = os.path.join(robo_results_dir, 'activity_map.json')
    if os.path.exists(activity_map_path):
        with open(activity_map_path, 'r') as f:
            activity_data = json.load(f)
            # Extract nodes and edges
            # This depends on Firebase's JSON structure
    
    # Map screenshots to states
    screenshots_dir = os.path.join(robo_results_dir, 'artifacts')
    if os.path.exists(screenshots_dir):
        for screenshot in Path(screenshots_dir).glob('*.png'):
            # Extract state information from filename/metadata
            pass
    
    return utg_data

# Usage
robo_dir = './utg-data/your-app-name'
utg = extract_utg_from_robo(robo_dir)
```

## Step 4: Collect/Create Visual Bug Recordings

### Option A: Use Existing Recordings
From the Android-Functional-bugs-study repository:
```bash
cd ~/gifdroid-reproduction
git clone https://github.com/Android-Functional-bugs-study/home
cd home

# Look for GIF/video files in bug reports
find . -type f \( -name "*.gif" -o -name "*.mp4" \) > recordings_list.txt
```

### Option B: Create Artificial Recordings (Paper's Approach)
The paper created 61 recordings with:
- **Different tools**: video conversion (32), mobile apps (22), emulator recording (7)
- **Varied resolutions**: 1920×1080 (27), 1280×800 (23), 900×600 (11)
- **Diverse length**: 30-305 frames
- **Different FPS**: 7-30 fps

```bash
# Using Android emulator screen recording
adb shell screenrecord /sdcard/bug_recording.mp4

# Pull the recording
adb pull /sdcard/bug_recording.mp4 ./recordings/

# Convert to GIF if needed
ffmpeg -i bug_recording.mp4 -vf "fps=15,scale=1280:-1:flags=lanczos" bug_recording.gif
```

## Step 5: Set Up GIFdroid

### Clone GIFdroid Repository
```bash
cd ~/gifdroid-reproduction
git clone https://github.com/sidongfeng/gifdroid
cd gifdroid
```

### Install Dependencies
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install required packages
pip install --upgrade pip
pip install numpy opencv-python scikit-image pillow

# Additional dependencies (check requirements.txt if available)
pip install matplotlib networkx
```

### Verify Installation
```bash
python -c "import cv2, skimage; print('OpenCV:', cv2.__version__); print('scikit-image:', skimage.__version__)"
```

## Step 6: Prepare Data for GIFdroid

### Directory Structure
```
gifdroid-reproduction/
├── apps/                   # APK files
├── utg-data/              # Firebase Robo results
│   ├── app1/
│   │   ├── screenshots/
│   │   ├── activity_map.json
│   │   └── crawl_graph.png
│   └── app2/
├── recordings/            # GIF/video bug recordings
│   ├── app1_bug1.gif
│   └── app2_bug1.mp4
├── ground-truth/          # Manual annotations (for evaluation)
│   ├── keyframes/
│   ├── gui-mapping/
│   └── traces/
└── gifdroid/             # GIFdroid code
```

### Convert Robo Results to GIFdroid Format
```python
# prepare_utg.py
import json
import os
import shutil
from pathlib import Path

def prepare_utg_for_gifdroid(robo_results_dir, output_dir, app_name):
    """
    Convert Firebase Robo results to GIFdroid-compatible format
    """
    app_output = os.path.join(output_dir, app_name)
    os.makedirs(app_output, exist_ok=True)
    
    # Copy screenshots
    screenshots_src = os.path.join(robo_results_dir, 'artifacts')
    screenshots_dst = os.path.join(app_output, 'screenshots')
    if os.path.exists(screenshots_src):
        shutil.copytree(screenshots_src, screenshots_dst, dirs_exist_ok=True)
    
    # Parse and convert activity map to UTG format
    activity_map = os.path.join(robo_results_dir, 'activity_map.json')
    if os.path.exists(activity_map):
        with open(activity_map, 'r') as f:
            data = json.load(f)
        
        # Convert to GIFdroid UTG format
        utg = {
            'nodes': [],
            'edges': [],
            'package_name': app_name
        }
        
        # TODO: Parse activity_map and populate UTG structure
        # This depends on the exact format Firebase returns
        
        with open(os.path.join(app_output, 'utg.json'), 'w') as f:
            json.dump(utg, f, indent=2)
    
    print(f"Prepared UTG for {app_name}")

# Usage
for app_dir in Path('./utg-data').iterdir():
    if app_dir.is_dir():
        prepare_utg_for_gifdroid(
            str(app_dir),
            './gifdroid-input',
            app_dir.name
        )
```

## Step 7: Run GIFdroid

### Basic Usage
```bash
cd ~/gifdroid-reproduction/gifdroid

# Run on a single recording
python gifdroid.py \
  --recording ../recordings/app1_bug1.gif \
  --utg ../gifdroid-input/app1/utg.json \
  --screenshots ../gifdroid-input/app1/screenshots \
  --output ../results/app1_bug1

# Check the paper's GitHub for exact command syntax
```

### Batch Processing
```python
# run_gifdroid_batch.py
import os
import subprocess
from pathlib import Path

RECORDINGS_DIR = "../recordings"
UTG_DIR = "../gifdroid-input"
OUTPUT_DIR = "../results"

for recording in Path(RECORDINGS_DIR).glob("*.gif"):
    app_name = recording.stem.split('_')[0]  # Extract app name
    
    utg_path = os.path.join(UTG_DIR, app_name, "utg.json")
    screenshots_path = os.path.join(UTG_DIR, app_name, "screenshots")
    output_path = os.path.join(OUTPUT_DIR, recording.stem)
    
    if os.path.exists(utg_path):
        cmd = [
            "python", "gifdroid.py",
            "--recording", str(recording),
            "--utg", utg_path,
            "--screenshots", screenshots_path,
            "--output", output_path
        ]
        
        print(f"Processing: {recording.name}")
        subprocess.run(cmd)
    else:
        print(f"WARNING: UTG not found for {app_name}")
```

## Step 8: Evaluate Results

### Manual Ground Truth Annotation
Following the paper's methodology (Section 4):

1. **Keyframe Location Ground Truth**:
   - Use VirtualDub or similar tool
   - Mark fully-rendered GUI states
   - Two annotators independently, then reconcile

2. **GUI Mapping Ground Truth**:
   - For each keyframe, manually select matching GUI from UTG
   - Record the mapping pairs

3. **Execution Trace Ground Truth**:
   - Manually determine optimal trace from app launch to bug
   - Record the sequence of GUI states

### Evaluation Metrics

```python
# evaluate_gifdroid.py
import json
import numpy as np

def evaluate_keyframe_location(predicted, ground_truth, tolerance=3):
    """
    Calculate precision, recall, F1 for keyframe location
    tolerance: ±3 frames as mentioned in paper
    """
    tp = 0
    fp = 0
    fn = 0
    
    for gt_frame in ground_truth:
        if any(abs(pred - gt_frame) <= tolerance for pred in predicted):
            tp += 1
        else:
            fn += 1
    
    fp = len([p for p in predicted if not any(abs(p - gt) <= tolerance for gt in ground_truth)])
    
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
    
    return {
        'precision': precision,
        'recall': recall,
        'f1': f1
    }

def evaluate_gui_mapping(predicted_mapping, ground_truth_mapping, utg, k=3):
    """
    Calculate Precision@k for GUI mapping
    """
    correct_at_k = {1: 0, 2: 0, 3: 0}
    total = len(ground_truth_mapping)
    
    for keyframe_id, gt_gui_id in ground_truth_mapping.items():
        if keyframe_id in predicted_mapping:
            pred_top_k = predicted_mapping[keyframe_id][:k]
            for i, pred_gui in enumerate(pred_top_k, 1):
                if pred_gui == gt_gui_id:
                    for j in range(i, k+1):
                        correct_at_k[j] += 1
                    break
    
    precision_at_k = {k: correct_at_k[k] / total for k in correct_at_k}
    return precision_at_k

def evaluate_trace_generation(predicted_trace, ground_truth_trace):
    """
    Calculate sequence similarity using LCS
    """
    # Longest Common Subsequence
    def lcs_length(seq1, seq2):
        m, n = len(seq1), len(seq2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if seq1[i-1] == seq2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]
    
    lcs_len = lcs_length(predicted_trace, ground_truth_trace)
    similarity = (2 * lcs_len) / (len(predicted_trace) + len(ground_truth_trace))
    
    return similarity

# Example usage
if __name__ == "__main__":
    # Load results
    with open('../results/app1_bug1/keyframes.json') as f:
        keyframes_pred = json.load(f)
    
    with open('../ground-truth/app1_bug1_keyframes.json') as f:
        keyframes_gt = json.load(f)
    
    # Evaluate
    kf_metrics = evaluate_keyframe_location(keyframes_pred, keyframes_gt)
    print(f"Keyframe Location - P: {kf_metrics['precision']:.3f}, R: {kf_metrics['recall']:.3f}, F1: {kf_metrics['f1']:.3f}")
```

## Step 9: Compare with Paper Results

### Expected Results (from Paper - Table 2, 3, 4)

**Keyframe Location**:
- Precision: 85.8%
- Recall: 90.4%
- F1-score: 88.0%

**GUI Mapping**:
- Precision@1: 85.4%
- Precision@2: 90.0%
- Precision@3: 91.3%

**Trace Generation**:
- Sequence Similarity: 89.59%
- Successfully reproduced: 82% (50/61 recordings)

### Generate Comparison Report
```python
# generate_report.py
import json
import pandas as pd

def generate_comparison_report(results_dir, paper_results):
    """
    Compare reproduction results with paper results
    """
    # Load all evaluation results
    my_results = {
        'keyframe_location': {},
        'gui_mapping': {},
        'trace_generation': {}
    }
    
    # TODO: Aggregate results from all test cases
    
    # Create comparison table
    comparison = pd.DataFrame({
        'Metric': [
            'KF Precision', 'KF Recall', 'KF F1',
            'GUI P@1', 'GUI P@2', 'GUI P@3',
            'Trace Similarity', 'Success Rate'
        ],
        'Paper': [
            0.858, 0.904, 0.880,
            0.854, 0.900, 0.913,
            0.8959, 0.82
        ],
        'Reproduction': [
            # Fill with your results
        ],
        'Difference': [
            # Calculate differences
        ]
    })
    
    print(comparison)
    comparison.to_csv('reproduction_comparison.csv', index=False)

# Usage
generate_comparison_report('./results', './paper_results.json')
```

## Troubleshooting

### Common Issues with Firebase Robo

1. **Authentication errors**:
   ```bash
   gcloud auth application-default login
   gcloud auth login
   ```

2. **API not enabled**:
   ```bash
   gcloud services enable testing.googleapis.com
   gcloud services enable toolresults.googleapis.com
   ```

3. **Insufficient permissions**:
   - Go to Google Cloud Console
   - IAM & Admin → Add roles: Firebase Test Lab Admin, Cloud Storage Admin

4. **Robo test doesn't explore well**:
   - Increase timeout: `--timeout 15m`
   - Use robo directives/scripts to guide exploration
   - Try different devices/API levels

### Common Issues with GIFdroid

1. **Missing dependencies**:
   ```bash
   pip install opencv-python scikit-image numpy pillow
   ```

2. **UTG format mismatch**:
   - Check the exact format GIFdroid expects
   - May need to write adapter code for Firebase format

3. **Image processing errors**:
   - Verify OpenCV installation: `python -c "import cv2; print(cv2.__version__)"`
   - Check image file permissions and formats

## Alternative: Use DroidBot Instead of Firebase

If Firebase Robo is too complex, consider DroidBot (also generates UTG):

```bash
# Install DroidBot
pip install droidbot

# Run DroidBot to generate UTG
droidbot -a your-app.apk -o ./output -timeout 300

# DroidBot generates:
# - utg.json (UI Transition Graph)
# - Screenshots in states/ directory
```

## Resources

### Official Documentation
- Firebase Test Lab: https://firebase.google.com/docs/test-lab
- gcloud CLI: https://cloud.google.com/sdk/gcloud
- GIFdroid Paper: https://doi.org/10.1145/3510003.3510048
- GIFdroid Code: https://github.com/sidongfeng/gifdroid

### Related Tools
- DroidBot: https://github.com/honeynet/droidbot
- Android Bug Study: https://github.com/Android-Functional-bugs-study/home
- F-Droid Apps: https://f-droid.org/

### Community
- Firebase Slack/Discord
- GIFdroid GitHub Issues
- Android Testing community forums

## Next Steps

1. Start with 1-2 apps first (don't try all 31 immediately)
2. Manually verify each step before automation
3. Document any deviations from the paper
4. Keep detailed logs of issues encountered
5. Consider reaching out to paper authors if stuck

## Reporting to Prof. Zhao

Structure your report with:
1. **Environment Setup**: Tools, versions, configurations used
2. **What Worked**: Successfully reproduced components
3. **What Didn't Work**: Failures, errors, deviations from paper
4. **Limitations Identified**: 
   - Firebase Robo vs paper's described Firebase approach
   - Missing implementation details
   - Ambiguities in methodology
5. **Suggestions for Improvement**:
   - Better documentation needs
   - Missing hyperparameters
   - Dataset availability issues
6. **Early Ideas**: How to extend this work (manual recordings, etc.)

Good luck with your reproduction!
