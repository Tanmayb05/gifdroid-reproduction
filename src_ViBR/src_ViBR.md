# src_ViBR: Runtime, Inputs/Outputs, Working, and Comparison with src_llm

## 1. What `src_ViBR` is

`src_ViBR` is a video-to-device bug replay pipeline. It:
1. Segments a bug-report video into stable action scenes.
2. Compares scene state to current device GUI with GPT-4o.
3. Infers and executes the next action on Android via ADB.

Core implementation lives in `src_ViBR/approach/`.

## 2. How `src_ViBR` runs

Main entry point:
- `src_ViBR/approach/segment_replay.py`

CLI usage (from `src_ViBR/approach`):
```bash
python segment_replay.py <video_path> <algorithm>
# algorithm: ssim | clip
```

Example:
```bash
python segment_replay.py /path/to/video.mp4 clip
```

Important runtime requirements:
- Android device/emulator connected via ADB.
- OpenAI API key hardcoded in `src_ViBR/approach/openai_api.py` (`OpenAI(api_key=...)`).
- GroundingDINO repository + weights present (used by `dino_detection.py`).
- Python packages from `src_ViBR/requirements.txt`.

## 3. `src_ViBR` input

Required inputs:
- A GUI recording video file (`<video_path>`).
- Boundary algorithm: `ssim` or `clip`.

Live runtime inputs from device:
- Current screenshot (`adb screencap` + `adb pull`).
- UI hierarchy XML (`uiautomator dump`).

Model inputs generated per segment:
- Start frame (segment start).
- Stop frame (next segment boundary frame).
- Current live device screenshot.
- GroundingDINO annotated regions.
- XML-derived clickable element overlays.

## 4. `src_ViBR` output

Primary output is operational side effects (actions executed on device), plus intermediate artifacts:

Local artifacts:
- `temp/<video_stem>/...`
  - `step_i/tmp_start.png`, `tmp_stop.png`
  - `step_i/screenshot-0.png`
  - `step_i/labeled.png` (XML element labels)
  - `step_i/dino.png` (all DINO detections)
  - `step_i/relevant_regions.png` (filtered DINO regions)
- `cache/sim_list_ssim_<video_stem>.pkl` or `cache/sim_list_clip_<video_stem>.pkl`

Device-side output:
- Tap/swipe/text/back/home/wait/no-op actions executed through ADB.

Notably, `src_ViBR` does not generate a structured run summary JSON equivalent to `execution_trace.json` in `src_llm`.

## 5. How `src_ViBR` works (pipeline)

### Step A: Video segmentation
- Reads all frames (`yyh_utils.read_frames_from_video`), plus cropped luminance frames for SSIM path.
- Boundary detection:
  - `ssim`: consecutive-frame SSIM sequence (`yyh_utils.calculate_sim_seq`) + stable segment detector.
  - `clip`: CLIP embeddings + cosine similarity (`clip_seg.VideoStableSegmentCLIP`).
- Produces stable segments as frame index ranges.

### Step B: Scene-to-device grounding
Per segment:
1. Capture live screenshot from device.
2. Dump UI XML and parse candidates (`input_formatter.parse_xml_string`).
3. Label candidate elements on screenshot (`label_screenshot`).
4. Run GroundingDINO on start frame (`run_grounding_dino`).
5. Ask GPT-4o to select relevant transition regions and predicted action (`ask_gpt_for_relevant_regions`).
6. Annotate selected regions (`annotate_relevant_regions`).

### Step C: GUI state consistency check
- GPT-4o compares relevant start context vs current live GUI (`ask_gpt_state_consistency`).
- If inconsistent: up to 3 recovery attempts.
  - Infer recovery action (`ask_gpt_for_action_region`).
  - Map region/text/position to current elements.
  - Execute recovery action, re-screenshot, re-check consistency.

### Step D: Action inference + execution
- If state is consistent:
  - Ask GPT-4o for replay action (`ask_gpt_for_action_region`).
  - Resolve to coordinates/element match.
  - Execute using `execute_action.execute_actions` on `ADBDeviceController`.
- If still inconsistent after retries: skip step and continue.

## 6. Quick module map (`src_ViBR/approach`)

- `segment_replay.py`: end-to-end orchestrator.
- `yyh_utils.py`: SSIM segmentation primitives.
- `clip_seg.py`: CLIP-based segmentation alternative.
- `dino_detection.py`: GroundingDINO region detection/annotation.
- `input_formatter.py`: UI XML parsing + screenshot labeling.
- `openai_api.py`: GPT-4o prompts for region selection, consistency, action inference.
- `execute_action.py`: action dispatch abstraction.
- `adb_device_controller.py`: ADB shell/tap/swipe/screenshot/XML wrappers.

## 7. Comparison: `src_ViBR` vs `src_llm`

`src_llm` has two flows:
- `python -m src_llm.main`: video -> keyframes -> LLM action trace JSON.
- `python -m src_llm.automate`: installs APK, summarizes video, and runs closed-loop device automation with structured logs and replay script generation.

### High-level differences

| Area | `src_ViBR` | `src_llm` |
|---|---|---|
| Primary goal | Reproduce bug directly from segmented scenes | Generate trace (`main`) and/or perform automation (`automate`) |
| Config style | Positional CLI args + hardcoded API key file edit | YAML config + `.env` validation |
| LLM providers | OpenAI GPT-4o only | Multi-provider (`gemini`, `llama`, `qwen`, `llava`, `minicpm`, `gemma`, etc.) |
| Segmentation | Stable-scene segmentation first (`ssim` or `clip`) | Frame sampling + keyframe selection (`ssim`/heuristic) |
| Region grounding | GroundingDINO + GPT region selection | No GroundingDINO dependency in core pipeline |
| GUI matching | Explicit GPT state-consistency check + retry recovery | Feedback loop via `decide_next_action_with_video_context` |
| Device control backend | Raw ADB commands | `uiautomator2` device wrapper + ADB for install/launch |
| Output artifacts | Temp images + cache; no canonical trace schema | `execution_trace.json`, `frames_manifest.json`, `metadata.json`, `session_trace.json`, `video_summary.txt`, `replay.py` |
| Multi-run orchestration | Not built-in | Built-in run lists in YAML |
| Error/fallback behavior | Mostly imperative flow, fewer typed exceptions | Strong config/env/path/provider exception structure + deterministic fallback in provider layer |

### Architectural contrast

1. **Control philosophy**
- `src_ViBR`: scene-by-scene deterministic loop with GPT checks around each scene transition.
- `src_llm`: configurable pipeline abstractions (extract/select/infer/build trace), plus optional autonomous replay loop.

2. **Data products**
- `src_ViBR`: optimized for immediate execution and visual debugging.
- `src_llm`: optimized for reproducibility and downstream tooling via structured JSON and logs.

3. **Reproducibility and scale**
- `src_ViBR`: easier to run single case quickly but less standardized outputs and config management.
- `src_llm`: better for batch experiments and comparisons because run layout, configs, and metadata are standardized.

4. **Dependency profile**
- `src_ViBR`: heavier CV stack for grounding (`torch`, `transformers`, `supervision`, GroundingDINO clone/weights).
- `src_llm`: lighter default dependencies in `requirements.txt`; provider-specific capabilities layered in code.

## 8. Practical takeaway

- Use `src_ViBR` when you want explicit region-grounded replay with per-scene visual alignment logic.
- Use `src_llm` when you need configurable, provider-agnostic pipelines with robust run artifacts and batch automation support.
