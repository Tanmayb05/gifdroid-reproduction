# ViBR Analysis Guide - Practical Examples

## Quick Start: Analyze Any App

### Step 1: Identify Your App Components

Run this to find all videos and runs for an app:

```bash
# For bloodpressuremonitor
find apps/bloodpressuremonitor/llm -maxdepth 1 -type d | grep -E "(vibr|gemini)" | sort

# For bakerspercentagecalculator
find apps/bakerspercentagecalculator/llm -maxdepth 1 -type d | grep -E "(vibr|gemini)" | sort

# For any app
find apps/[APP_NAME]/llm -maxdepth 1 -type d | grep -E "(vibr|gemini)" | sort
```

### Step 2: Prepare Your Analysis Request

Format your request exactly like this:

```
analyze ViBR failure for [APP_NAME]

app: [APP_NAME]
videos: [extracted from directory names, e.g., hhv-002, srv-001]
vibr_runs: [list all -vibr directories with run numbers]
gemini_runs: [list all -gemini-2.5-pro-vm directories with run numbers]
base_path: apps/[APP_NAME]/llm

analysis:
1. Extract ground truth steps from each gemini run's memory.md
2. For each ViBR run, compare steps against corresponding Gemini memory.md
3. Identify which step ViBR diverges from ground truth
4. Analyze failure root cause with evidence from logs
5. Provide detailed explanation with specific reasons

output format:
- Run-by-run breakdown
- Step comparison table (Gemini steps vs ViBR execution)
- Failure analysis with root causes
- Log evidence where applicable
```

## Real Examples from Your Projects

### Example 1: bloodpressuremonitor

**Videos found:**
- hhv-002 → hhv-002-vibr/run-001, hhv-002-gemini-2.5-pro-vm/run-001
- srv-001 → srv-001-vibr/run-001 + run-002, srv-001-gemini-2.5-pro-vm/run-001 + run-002

**Your request should be:**

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
- Run-by-run breakdown with numbered steps
- Step comparison table showing Gemini ground truth vs ViBR execution
- Clear divergence point identification
- Failure analysis with specific reasons and evidence
```

### Example 2: bakerspercentagecalculator

**Videos found:**
- hhv-002 → hhv-002-vibr/run-001, hhv-002-gemini-2.5-pro-vm/run-001
- srv-001 → srv-001-vibr/run-001, srv-001-gemini-2.5-pro-vm/run-001
- srv-002 → srv-002-vibr/run-001, srv-002-gemini-2.5-pro-vm/run-001
- hhv-001 → hhv-001-vibr/run-001, hhv-001-gemini-2.5-pro-vm/run-001

**Your request should be:**

```
analyze ViBR failure for bakerspercentagecalculator

app: bakerspercentagecalculator
videos: hhv-001, hhv-002, srv-001, srv-002
vibr_runs: hhv-001-vibr/run-001, hhv-002-vibr/run-001, srv-001-vibr/run-001, srv-002-vibr/run-001
gemini_runs: hhv-001-gemini-2.5-pro-vm/run-001, hhv-002-gemini-2.5-pro-vm/run-001, srv-001-gemini-2.5-pro-vm/run-001, srv-002-gemini-2.5-pro-vm/run-001
base_path: apps/bakerspercentagecalculator/llm

analysis:
1. Extract ground truth steps from gemini memory.md files
2. Compare each ViBR run against its corresponding Gemini ground truth
3. Identify divergence points and failure modes
4. Analyze root causes with evidence from logs
5. Categorize: detection failure, interpretation failure, execution failure, timing issue, or context loss

output format:
- Run-by-run breakdown with clear step numbering
- Comparison table: Gemini steps vs ViBR actual execution
- Divergence analysis for each run
- Root cause explanation with log references
```

## File Locations to Know

For any app analysis:

```
apps/[APP_NAME]/llm/
├── [VIDEO_ID]-vibr/run-00X/
│   ├── memory.md or log.md          ← ViBR steps/logs
│   ├── logs/                        ← Detailed execution logs
│   └── artifacts/                   ← Screenshots, labeled images
│
└── [VIDEO_ID]-gemini-2.5-pro-vm/run-00X/
    ├── memory.md                    ← GROUND TRUTH steps
    ├── logs/                        ← Gemini execution logs
    └── artifacts/                   ← Screenshots, labeled images
```

## What to Look For in Analysis

### In Gemini memory.md (Ground Truth)
- **Step sequence**: exact order of UI interactions
- **Element detection**: what was found/clicked
- **State transitions**: before/after states
- **Success criteria**: what confirms step completion

### In ViBR logs/memory
- **Missed steps**: steps Gemini took that ViBR skipped
- **Wrong steps**: ViBR did something different than Gemini
- **Failed detections**: UI elements ViBR couldn't locate
- **Error messages**: explicit failures in logs

### Common Failure Patterns
1. **Detection**: "Button not found" → ViBR's vision/OCR issue
2. **Interpretation**: Took action X instead of action Y → LLM reasoning
3. **Timing**: Clicked before UI settled → async wait issue
4. **Memory**: Lost previous context → state management problem
5. **State**: Assumed wrong app state → detection feedback issue

## Tips for Effective Analysis

1. **Load memory.md first** - Gemini's is the source of truth for correct steps
2. **Compare side-by-side** - Make a table: step #, Gemini action, ViBR action, match?
3. **Mark divergence** - Circle the first step where they differ
4. **Examine logs** - Look at timestamps and error messages at divergence point
5. **Classify failure** - Is it detection? reasoning? timing? This guides fixes
6. **Find evidence** - Quote specific log lines that explain the failure

## Template for Your Request

Copy and modify this for any app:

```
analyze ViBR failure for [APP_NAME]

app: [APP_NAME]
videos: [comma-separated video IDs]
vibr_runs: [comma-separated vibr run paths with run numbers]
gemini_runs: [comma-separated gemini run paths with run numbers]
base_path: apps/[APP_NAME]/llm

analysis:
1. Extract ground truth steps from each gemini run's memory.md
2. For each ViBR run, compare steps against corresponding Gemini memory.md  
3. Identify which step ViBR diverges from ground truth
4. Analyze failure root cause: detection, interpretation, execution, timing, context loss
5. Cross-reference with logs/ directory for specific evidence

output format:
- Run-by-run breakdown with detailed step analysis
- Step comparison table (Gemini steps vs ViBR execution)
- Clear divergence point identification  
- Failure analysis with specific reasons and log evidence
```

That's it! Customize the bracketed sections and paste into Claude Code.
