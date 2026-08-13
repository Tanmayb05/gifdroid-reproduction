# Issues: hhv-002 run-001

## Video vs memory.md gaps

### 1. Third account misidentified ("alfred" → "Outlook")
Video shows 3 accounts: Ezio, bruce, alfred. Memory lists Ezio, bruce, **Outlook** — Outlook never appears in video.

**Reason:** Gemini video understanding samples at default ~1fps (no `fps`/`video_metadata` override passed in `_send_video_request`, [providers.py:938](../../../../../src_llm/providers.py#L938) — raw bytes sent with no sampling config). Accounts-list frame is on screen briefly and partly finger-occluded (see f_006). At low sample rate + occlusion, model's OCR confidence on the 3rd row was low, so it guessed a plausible generic label ("Outlook" is a common stock account name in test fixtures) instead of abstaining or flagging uncertainty.

### 2. Recents/close/relaunch sequence fabricated (memory steps 7–11)
Memory: drawer closes clean at step 7 → recents → force-close → relaunch → reopen drawer at step 11 (25s) → pink chip appears on Ezio for the first time.
Video: pink chip already visible on Ezio's nav drawer at 18s (f_018) — before any close/relaunch action is visible on screen at all.

**Reason:** The memory-extraction prompt ([gemini_video_prompt.txt](../../../../../src_llm/input/prompts/gemini_video_prompt.txt)) asks the model to identify "meaningful user interactions" and produce a step trace. Under sparse 1fps sampling, gaps in evidence got filled with the *templated* K-9 color-swap bug-repro shape (explore account settings → back out → force-close → relaunch → reveal bug) — the same shape appears near-verbatim in the hhv-001 memory.md for this app. Model imposed a causal narrative (force-close causes the chip swap) onto footage where the anomaly was already present earlier. Narrative plausibility won over frame-level grounding.

### 3. FTP Server screen (f_022, ~22s) omitted entirely
Frame at 22s shows an unrelated screen — "FTP Server" app, `ftp://192.168.1.250:2211`, with a system "Screenshot" toast. Not mentioned anywhere in memory.md.

**Reason:** Prompt explicitly instructs: *"Ignore idle frames, loading spinners, and system UI transitions that the user did not initiate."* Model likely classified this as an incidental/non-task app switch (possibly a screenshot-tool artifact) and filtered it per instruction. Correct per the letter of the prompt, but it silently drops a real screen from the ground truth — prompt-driven omission, not hallucination.

### 4. Timeline truncated (memory ends 25s, video runs 28.8s)
Final video frame (f_029, ~29s) shows Ezio inbox again with pink chip still present — consistent with the claimed bug, but memory's 11-step trace stops at 25s and never accounts for the tail ~4s.

**Reason:** Once the model's internal narrative reached its expected climax (bug revealed), it stopped transcribing further steps even though real footage remained. Prompt has no requirement to account for every second of video or to keep emitting steps until end-of-video — so the model exhibits template-completion bias: story arc closes, transcription stops.

### Common root cause
No frame-level grounding constraint in the prompt (no per-frame citation/timestamp requirement, no confidence check against uniform sampling), combined with default ~1fps video ingestion that misses fast or occluded UI states. Result: Gemini produces a coherent plausible story rather than a strict transcript, and narrative plausibility wins whenever frames are ambiguous, blurred, or filtered as "not meaningful."

---

## memory.md vs device-automation gap

Automation stopped at step 4 with `Stall detected: action ('tap', None, None) repeated 4 times`. Steps 5–11 of memory.md never executed on-device — no screenshots/logs past `step_004.png`.

**Root cause (code bug, not LLM failure):** `_action_key()` in [automation.py:20-23](../../../../../src_llm/automation.py#L20-L23) builds its dedup signature as `(action.type, action.direction, action.resource_id)` — **coordinates are excluded**. Gemini's vision-coordinate actions always have `resource_id=null`, so every tap step collapses to the identical key `("tap", None, None)` regardless of actual tap location. Steps 1–4 tapped four different coordinates on four different screens (`[73,136]` → `[420,2211]` → `[540,650]` → `[540,280]`) — real progress — but the stall detector saw 4 identical keys and killed the run as a false positive.

**Fix:** fall back to coordinates when `resource_id` is `None`:
```python
return (action.get("type"), action.get("direction"), action.get("resource_id") or tuple(action.get("coordinates") or []))
```

**Implication:** the on-device run was never a fair test of whether the memory.md bug-repro narrative (steps 5–11) is reproducible — it was cut off by faulty tooling before reaching that point. Independent of this, the video-gap findings above suggest the narrative itself is already inaccurate even before considering device reproduction.
