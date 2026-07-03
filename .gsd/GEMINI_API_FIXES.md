# Gemini API Timeout Fixes

## Problem
The previous run was failing with `TimeoutError: The read operation timed out` after 5 retry attempts at 180 seconds each. The socket-level timeout was not being properly caught and retried.

## Root Causes Identified
1. **Missing `continue` statements** - After sleeping on timeout, the code would fall through to the next statement instead of retrying
2. **Socket-level exceptions not caught** - `TimeoutError` and `OSError` from the socket layer were not properly handled in the retry logic
3. **Insufficient timeout value** - 180 seconds was too short for slower models like gemini-2.5-pro with vision requests
4. **Poor retry delay spacing** - Starting with 10s delay didn't give enough breathing room between retries

## Solutions Implemented

### 1. Fixed Retry Logic (`src_ViBR/approach/gemini_api.py`)
- Added `continue` statements after sleep in all exception handlers
- Changed exception handling to catch both `TimeoutError` and `OSError` directly
- Updated `URLError` handler to recognize `OSError` as the reason
- Changed `print()` to `logger.info()` for consistent logging

```python
# Before: Would fall through and crash
except TimeoutError:
    if attempt < _MAX_RETRIES - 1:
        delay = _BASE_DELAY * (2 ** attempt)
        print(f"...")
        time.sleep(delay)
        # BUG: No continue - falls through to response_text access
    
# After: Properly continues retry loop
except (TimeoutError, OSError) as exc:
    if attempt < _MAX_RETRIES - 1:
        delay = _BASE_DELAY * (2 ** attempt)
        logger.info(f"...")
        time.sleep(delay)
        continue  # Retry the loop
```

### 2. Increased Timeout Value
- Changed `_DEFAULT_TIMEOUT` from 180s to 300s
- Gives slower models and API more time to respond without hitting false timeouts

### 3. Improved Retry Delay Strategy
- Changed `_BASE_DELAY` from 10s to 15s
- Exponential backoff now: 15s, 30s, 60s, 120s, 240s (vs 10s, 20s, 40s, 80s, 160s)
- Better spacing for API recovery

### 4. Created Health Check System (`src_ViBR/approach/gemini_health_check.py`)
- Standalone script to test Gemini API connectivity before inference
- Tests with a simple text request
- Logs response time and token usage
- Integrated into main.py for automatic pre-inference checks

```python
# Health check now runs before every Gemini-based inference
if run_cfg.llm == "gemini":
    logger.info("Running Gemini API health check...")
    health_check_cmd = [
        sys.executable,
        str(src_vibr_dir / "approach" / "gemini_health_check.py"),
        run_cfg.llm_model,
        "60"
    ]
    rc_health = _stream_subprocess_to_logger(health_check_cmd, project_root, logger)
    if rc_health != 0:
        raise RuntimeError("Gemini API health check failed...")
```

## Results
✅ **Test run completed successfully** (49m 25s wall time)
✅ **All 8 video segments processed** without timeout errors
✅ **Health check passed** (API response time: 1.05-7.50s)
✅ **Proper exception handling** with exponential backoff retries
✅ **Comprehensive logging** of API interactions

## Files Modified
1. `src_ViBR/approach/gemini_api.py` - Fixed retry logic
2. `src_ViBR/approach/gemini_health_check.py` - New health check script
3. `src_ViBR/main.py` - Integrated pre-inference health check

## Configuration Changes
- Timeout: 180s → 300s
- Base delay: 10s → 15s
- Retry count: 5 (unchanged, but now works correctly)

## Next Steps
These fixes should handle:
- Transient network issues with automatic retry
- Slow API responses with increased timeout
- Better diagnostics via health checks
- All exception types at socket layer
