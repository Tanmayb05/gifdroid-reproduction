# ViBR vs Gemini 2.5 Pro VM Analysis Template

Use this template to compare ViBR runs against Gemini 2.5 Pro VM ground truth for any app.

## How to Use

Replace the bracketed placeholders with your specific values and paste into Claude Code:

```
analyze ViBR failure for [APP_NAME]

app: [APP_NAME]
videos: [VIDEO_IDS] (comma-separated, e.g., "hhv-002, srv-001")
vibr_runs: [VIBR_RUN_PATHS] (comma-separated, e.g., "hhv-002-vibr/run-001, srv-001-vibr/run-001, srv-001-vibr/run-002")
gemini_runs: [GEMINI_RUN_PATHS] (comma-separated, e.g., "hhv-002-gemini-2.5-pro-vm/run-001, srv-001-gemini-2.5-pro-vm/run-001, srv-001-gemini-2.5-pro-vm/run-002")
base_path: apps/[APP_NAME]/llm

analysis:
1. Extract ground truth steps from each gemini run's memory.md
2. For each ViBR run, compare steps against corresponding Gemini memory.md
3. Identify which step ViBR diverges from ground truth
4. Analyze failure root cause: missing detection, wrong interpretation, timing issue, etc.
5. Cross-reference with logs/ directory for error details

output format:
- Run-by-run breakdown
- Step comparison table (Gemini steps vs ViBR execution)
- Failure analysis with specific reasons
- Log evidence where applicable
```

## Template Fields Explained

| Field | Description | Example |
|-------|-------------|---------|
| `APP_NAME` | Name of the app being tested | `bloodpressuremonitor`, `bakerspercentagecalculator` |
| `VIDEO_IDS` | Unique video identifiers from filenames | `hhv-002`, `srv-001` |
| `VIBR_RUN_PATHS` | Relative paths to ViBR runs (from base_path) | `hhv-002-vibr/run-001` |
| `GEMINI_RUN_PATHS` | Relative paths to Gemini runs (from base_path) | `hhv-002-gemini-2.5-pro-vm/run-001` |
| `base_path` | Root directory containing all runs | `apps/[APP_NAME]/llm` |

## Directory Structure Expected

```
apps/[APP_NAME]/llm/
├── [VIDEO_ID]-vibr/
│   ├── run-001/
│   │   ├── memory.md (or log.md)
│   │   ├── logs/
│   │   └── artifacts/
│   └── run-00X/...
├── [VIDEO_ID]-gemini-2.5-pro-vm/
│   ├── run-001/
│   │   ├── memory.md (ground truth steps)
│   │   ├── logs/
│   │   └── artifacts/
│   └── run-00X/...
```

## Analysis Checklist

- [ ] Load all memory.md files from Gemini runs (ground truth)
- [ ] Load all log.md or memory.md files from ViBR runs
- [ ] Extract step sequences from each run
- [ ] Create side-by-side comparison table
- [ ] Mark divergence point(s) where ViBR deviates
- [ ] Categorize failure type:
  - **Detection Failure**: ViBR missed UI element/state
  - **Interpretation Failure**: ViBR misunderstood what to do
  - **Execution Failure**: ViBR executed wrong action
  - **Timing Issue**: ViBR acted before state settled
  - **Context Loss**: ViBR lost track of previous steps
- [ ] Provide specific evidence from logs
- [ ] Suggest root cause and improvement area

## Example Filled Template

```
analyze ViBR failure for bloodpressuremonitor

app: bloodpressuremonitor
videos: hhv-002, srv-001
vibr_runs: hhv-002-vibr/run-001, srv-001-vibr/run-001, srv-001-vibr/run-002
gemini_runs: hhv-002-gemini-2.5-pro-vm/run-001, srv-001-gemini-2.5-pro-vm/run-001, srv-001-gemini-2.5-pro-vm/run-002
base_path: apps/bloodpressuremonitor/llm

analysis:
1. Extract ground truth steps from each gemini run's memory.md
2. For each ViBR run, compare steps against corresponding Gemini memory.md
3. Identify which step ViBR diverges from ground truth
4. Analyze failure root cause: missing detection, wrong interpretation, timing issue, etc.
5. Cross-reference with logs/ directory for error details

output format:
- Run-by-run breakdown
- Step comparison table (Gemini steps vs ViBR execution)
- Failure analysis with specific reasons
- Log evidence where applicable
```

