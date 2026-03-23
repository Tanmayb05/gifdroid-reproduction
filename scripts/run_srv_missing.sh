#!/bin/bash
set -e

cd "$(dirname "$0")/.."
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate gifdroid

LOG="$(dirname "$0")/run_srv_missing.log"
exec > >(tee -a "$LOG") 2>&1
echo "=== Run started: $(date) ==="

echo "[1/5] HomeMedkit utg02 SRV"
python -m gifdroid.main \
  --video app_HomeMedkit/utg02/input/screenrec/srv_app_HomeMedkit.mp4 \
  --utg app_HomeMedkit/utg02/input/utg.json \
  --artifact app_HomeMedkit/utg02/input/artifacts \
  --out app_HomeMedkit/utg02/output/execution_srv_HomeMedkit.json

echo "[2/5] Jigsaw utg03 SRV"
python -m gifdroid.main \
  --video app_Jigsaw/utg03/input/screenrec/srv_app_Jigsaw.mp4 \
  --utg app_Jigsaw/utg03/input/utg.json \
  --artifact app_Jigsaw/utg03/input/artifacts \
  --out app_Jigsaw/utg03/output/execution_srv_Jigsaw.json

# echo "[3/5] LuxAlarm utg02 SRV"
# python -m gifdroid.main \
#   --video app_LuxAlarm/utg02/input/screenrec/srv_app_LuxAlarm.mp4 \
#   --utg app_LuxAlarm/utg02/input/utg.json \
#   --artifact app_LuxAlarm/utg02/input/artifacts \
#   --out app_LuxAlarm/utg02/output/execution_srv_LuxAlarm.json

# echo "[4/5] LuxAlarm utg03 SRV"
# python -m gifdroid.main \
#   --video app_LuxAlarm/utg03/input/screenrec/srv_app_LuxAlarm.mp4 \
#   --utg app_LuxAlarm/utg03/input/utg.json \
#   --artifact app_LuxAlarm/utg03/input/artifacts \
#   --out app_LuxAlarm/utg03/output/execution_srv_LuxAlarm.json

echo "[5/5] SimpleNotes utg01 SRV"
python -m gifdroid.main \
  --video app_SimpleNotes/utg01/input/screenrec/srv_app_SimpleNotes.mp4 \
  --utg app_SimpleNotes/utg01/input/utg.json \
  --artifact app_SimpleNotes/utg01/input/artifacts \
  --out app_SimpleNotes/utg01/output/execution_srv_SimpleNotes.json

echo "Done."
echo "=== Run finished: $(date) ==="