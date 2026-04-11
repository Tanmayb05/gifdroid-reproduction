#!/bin/bash
set -e

cd "$(dirname "$0")/.."
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate gifdroid

LOG="$(dirname "$0")/run_hhv_missing.log"
exec > >(tee -a "$LOG") 2>&1
echo "=== Run started: $(date) ==="

echo "[1/10] AdAway utg03 HHV"
python -m src_gifdroid.main \
  --video app_AdAway/utg03/input/handheld/hhv_app_AdAway.mp4 \
  --utg app_AdAway/utg03/input/utg.json \
  --artifact app_AdAway/utg03/input/artifacts \
  --out app_AdAway/utg03/output/execution_hhv_AdAway.json

echo "[2/10] AntennaPod utg02 HHV"
python -m src_gifdroid.main \
  --video app_AntennaPod/utg02/input/handheld/hhv_app_AntennaPod.mp4 \
  --utg app_AntennaPod/utg02/input/utg.json \
  --artifact app_AntennaPod/utg02/input/artifacts \
  --out app_AntennaPod/utg02/output/execution_hhv_AntennaPod.json

echo "[3/10] AntennaPod utg03 HHV"
python -m src_gifdroid.main \
  --video app_AntennaPod/utg03/input/handheld/hhv_app_AntennaPod.mp4 \
  --utg app_AntennaPod/utg03/input/utg.json \
  --artifact app_AntennaPod/utg03/input/artifacts \
  --out app_AntennaPod/utg03/output/execution_hhv_AntennaPod.json

echo "[4/10] HomeMedkit utg03 HHV"
python -m src_gifdroid.main \
  --video app_HomeMedkit/utg03/input/handheld/hhv_app_HomeMedkit.mp4 \
  --utg app_HomeMedkit/utg03/input/utg.json \
  --artifact app_HomeMedkit/utg03/input/artifacts \
  --out app_HomeMedkit/utg03/output/execution_hhv_HomeMedkit.json

echo "[5/10] Jigsaw utg03 HHV"
python -m src_gifdroid.main \
  --video app_Jigsaw/utg03/input/handheld/hhv_app_Jigsaw.mp4 \
  --utg app_Jigsaw/utg03/input/utg.json \
  --artifact app_Jigsaw/utg03/input/artifacts \
  --out app_Jigsaw/utg03/output/execution_hhv_Jigsaw.json

# echo "[6/10] LuxAlarm utg02 HHV"
# python -m src_gifdroid.main \
#   --video app_LuxAlarm/utg02/input/handheld/hhv_app_LuxAlarm.mp4 \
#   --utg app_LuxAlarm/utg02/input/utg.json \
#   --artifact app_LuxAlarm/utg02/input/artifacts \
#   --out app_LuxAlarm/utg02/output/execution_hhv_LuxAlarm.json

echo "[7/10] LuxAlarm utg03 HHV"
python -m src_gifdroid.main \
  --video app_LuxAlarm/utg03/input/handheld/hhv_app_LuxAlarm.mp4 \
  --utg app_LuxAlarm/utg03/input/utg.json \
  --artifact app_LuxAlarm/utg03/input/artifacts \
  --out app_LuxAlarm/utg03/output/execution_hhv_LuxAlarm.json

echo "[8/10] PortAuthority utg03 HHV"
python -m src_gifdroid.main \
  --video app_PortAuthority/utg03/input/handheld/hhv_app_PortAuthority.mp4 \
  --utg app_PortAuthority/utg03/input/utg.json \
  --artifact app_PortAuthority/utg03/input/artifacts \
  --out app_PortAuthority/utg03/output/execution_hhv_PortAuthority.json

echo "[9/10] SimpleNotes utg02 HHV"
python -m src_gifdroid.main \
  --video app_SimpleNotes/utg02/input/handheld/hhv_app_SimpleNotes.mp4 \
  --utg app_SimpleNotes/utg02/input/utg.json \
  --artifact app_SimpleNotes/utg02/input/artifacts \
  --out app_SimpleNotes/utg02/output/execution_hhv_SimpleNotes.json

echo "[10/10] SimpleNotes utg03 HHV"
python -m src_gifdroid.main \
  --video app_SimpleNotes/utg03/input/handheld/hhv_app_SimpleNotes.mp4 \
  --utg app_SimpleNotes/utg03/input/utg.json \
  --artifact app_SimpleNotes/utg03/input/artifacts \
  --out app_SimpleNotes/utg03/output/execution_hhv_SimpleNotes.json

echo "[11/11] WifiAnalyzer utg03 HHV"
python -m src_gifdroid.main \
  --video app_WifiAnalyzer/utg03/input/handheld/hhv_app_WifiAnalyzer.mp4 \
  --utg app_WifiAnalyzer/utg03/input/utg.json \
  --artifact app_WifiAnalyzer/utg03/input/artifacts \
  --out app_WifiAnalyzer/utg03/output/execution_hhv_WifiAnalyzer.json

echo "Done."
echo "=== Run finished: $(date) ==="