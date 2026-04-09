# Automation Evaluation Results — Milestone 5

Metric: Longest Common Subsequence (LCS) of meaningful action types,  
normalised by ground-truth sequence length.  
Ground truth = passive Gemini-2.5-Pro execution trace (`execution_trace.json`).  
Automation = active video-guided loop session trace (`session_trace.json`).

## Summary Table

| App | GT Steps | Auto Steps | LCS Score |
|-----|----------|------------|-----------|
| adaway | 3 | 7 | 0.67 |
| antennapod | 9 | 5 | 0.56 |
| luxalarm | 8 | 12 | 0.75 |
| **Average** | 6.7 | 8.0 | **0.66** |

## Per-App Details

### adaway

- Session trace: `artifacts/milestone5/adaway/run-001/session_trace.json`
- Execution trace: `apps/adaway/llm/gemini/gemini-2-5-pro/screenrec/fps1-5__max100__llm-assisted__gap1/run-001/execution_trace.json`
- GT steps (meaningful): 3 (raw: 8)
- Auto steps (meaningful): 7 (raw: 8)
- LCS score: **0.67** (2/3)
- Matched types: tap, tap
- Missed types:  scroll
- Extra types:   (none)

### antennapod

- Session trace: `artifacts/milestone5/antennapod/run-001/session_trace.json`
- Execution trace: `apps/antennapod/llm/gemini/gemini-2-5-pro/screenrec/fps1-5__max100__llm-assisted__gap1/run-001/execution_trace.json`
- GT steps (meaningful): 9 (raw: 10)
- Auto steps (meaningful): 5 (raw: 6)
- LCS score: **0.56** (5/9)
- Matched types: tap, tap, tap, tap, tap
- Missed types:  scroll, scroll, input, input
- Extra types:   (none)

### luxalarm

- Session trace: `artifacts/milestone5/luxalarm/run-001/session_trace.json`
- Execution trace: `apps/luxalarm/llm/gemini/gemini-2-5-pro/screenrec/fps1-5__max100__llm-assisted__gap1/run-001/execution_trace.json`
- GT steps (meaningful): 8 (raw: 9)
- Auto steps (meaningful): 12 (raw: 12)
- LCS score: **0.75** (6/8)
- Matched types: tap, tap, tap, tap, tap, tap
- Missed types:  input, scroll
- Extra types:   scroll, scroll
