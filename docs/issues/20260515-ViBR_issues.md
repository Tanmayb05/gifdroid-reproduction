# ViBR GPU Optimization Issues - May 15, 2026

## Issues Faced & Fixed

### 1. **CLIP Similarity Taking 20 Minutes**
- **Symptom**: Logs show CLIP model loads at 10:59:18, but doesn't log "CLIP similarity list loaded from cache" until 11:19:13 (20-minute gap)
- **Root Cause**: `_encode_frames()` was processing frames one-at-a-time in a loop instead of batching
- **Fix**: Refactored to batch process 32 frames per iteration instead of 1 frame per iteration
- **Location**: [src_ViBR/approach/clip_seg.py:111-128](../../src_ViBR/approach/clip_seg.py)
- **Expected improvement**: 10-20x faster (from ~20min to ~1-2min for 300 frames)

### 2. **CLIP Model Running on CPU Instead of MPS**
- **Symptom**: Device detection logic only checked for CUDA, defaulted to CPU on macOS with MPS available
- **Root Cause**: Line 54 in clip_seg.py: `self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")`
- **Fix**: Added MPS detection: CUDA → MPS → CPU fallback chain
- **Location**: [src_ViBR/approach/clip_seg.py:52-61](../../src_ViBR/approach/clip_seg.py)
- **Impact**: GPU acceleration now properly used on Apple Silicon

### 3. **GroundingDINO Running on CPU Despite GPU Available**
- **Symptom**: Warning "Failed to load custom C++ ops. Running on CPU mode Only!" + hardcoded device to CPU
- **Root Cause**: Line 17 in dino_detection.py hardcoded `device = torch.device("cpu")`
- **Fix**: Applied same device detection chain (CUDA → MPS → CPU) + moved model to device
- **Location**: [src_ViBR/approach/dino_detection.py:16-22, 75-76](../../src_ViBR/approach/dino_detection.py)

### 4. **No Visibility Into CLIP Computation Timing**
- **Symptom**: No logs between CLIP model load and final cache/result message
- **Fix**: Added detailed logging throughout the pipeline:
  - Model initialization time
  - Frame conversion time
  - Per-batch encoding time (processor + model separately)
  - Similarity computation time
  - Total time breakdown
- **Locations**: 
  - [src_ViBR/approach/clip_seg.py:111-145](../../src_ViBR/approach/clip_seg.py)
  - [src_ViBR/approach/segment_replay.py:173-220](../../src_ViBR/approach/segment_replay.py)

### 5. **Redundant venv_gpu Creation**
- **Symptom**: Created `venv_gpu` when `.venv` already existed with PyTorch 2.11.0 + MPS support
- **Fix**: Removed redundant venv and activation script, used existing `.venv`
- **Lesson**: Check existing environment before creating new ones

### 6. **Gemini API Socket-Level Timeout Not Being Retried**

- **Symptom**: `TimeoutError: The read operation timed out` after 5 retry attempts (180s each), causing inference to fail partway through video processing
- **Root Cause**: Multiple issues in exception handling:
  1. Missing `continue` statements after timeout sleep → code fell through to access unset `response_text` variable
  2. Socket-level `TimeoutError` and `OSError` not caught by retry logic
  3. Insufficient timeout value (180s) for slower models like gemini-2.5-pro with vision requests
  4. Poor exponential backoff strategy (10s, 20s, 40s, 80s, 160s) didn't give API enough recovery time
- **Fix**:
  - Added `continue` statements to all exception handlers so retry loop actually continues
  - Added catch for both `TimeoutError` and `OSError` exceptions directly (not just wrapped in URLError)
  - Increased `_DEFAULT_TIMEOUT` from 180s to 300s
  - Increased `_BASE_DELAY` from 10s to 15s for better exponential backoff (15s, 30s, 60s, 120s, 240s)
  - Changed logging from `print()` to `logger.info()` for consistency
- **Location**: [src_ViBR/approach/gemini_api.py:131-182](../../src_ViBR/approach/gemini_api.py)
- **Status**: ✅ Fixed and tested — run completed successfully (49m 25s, all 8 segments processed)

### 7. **No Pre-Inference API Health Check**

- **Symptom**: No way to diagnose API issues before starting long-running inference
- **Fix**: Created standalone health check script that:
  - Tests Gemini API connectivity with a simple text request
  - Logs API response time and token usage
  - Integrated into main.py to run automatically before inference
  - Provides clear error messaging if API is unavailable
- **Location**:
  - [src_ViBR/approach/gemini_health_check.py](../../src_ViBR/approach/gemini_health_check.py) (new file)
  - [src_ViBR/main.py:134-146](../../src_ViBR/main.py)
- **Impact**: Better diagnostics and faster failure detection

## Command to Run with Config

```bash
source .venv/bin/activate && python src_ViBR/main.py --config src_ViBR/input/config.yml
```

## Expected Outcome

After fixes, CLIP stage should complete in **1-2 minutes** instead of 20+ minutes for 300 frames.

## Files Modified

- `src_ViBR/approach/clip_seg.py` — Batching + device detection + logging
- `src_ViBR/approach/dino_detection.py` — Device detection + model.to(device)
- `src_ViBR/approach/segment_replay.py` — Pipeline logging
- `src_ViBR/approach/gemini_api.py` — Fixed retry logic, timeout handling, and logging
- `src_ViBR/approach/gemini_health_check.py` — New health check script (created)
- `src_ViBR/main.py` — Integrated pre-inference health check
