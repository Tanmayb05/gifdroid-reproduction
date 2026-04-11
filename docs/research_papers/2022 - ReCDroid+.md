# 📄 ReCDroid+: Automated End-to-End Crash Reproduction from Bug Reports for Android Apps

**Domain:** Android Bug Reproduction (NLP / Deep Learning / GUI Testing)

---

## 🧾 Paper Info

* **Title:** ReCDroid+: Automated End-to-End Crash Reproduction from Bug Reports for Android Apps
* **Authors:** Yu Zhao, Ting Su, Yang Liu, Wei Zheng, Xiaoxue Wu, Ramakanth Kavuluru, William G. J. Halfond, Tingting Yu
* **Year / Venue:** 2022 / ACM Transactions on Software Engineering and Methodology (TOSEM), Vol. 31, No. 3, Article 36
* **Link:** https://doi.org/10.1145/3488244
* **Code Available:** Yes → [artifacts link referenced in paper, Section 1]

---

## 🎯 Problem Statement

* **What problem is this paper solving?**
  * Automatically reproducing crash failures for Android apps directly from the textual description in bug reports
  * _Reference:_ [Abstract, Page 36:1]

* **Why is this problem important?**
  * Bug reports are often written in informal natural language; manually reproducing crashes is time-consuming and error-prone; developers abandon ~88% of apps on first encountering a recurring crash
  * _Reference:_ [Section 1, Page 36:2]

* **What assumptions does the paper make?**
  * Bug reports are crash reports with textual reproduction steps (S2R); input is an HTML bug report + APK file; target crash is deterministic enough to reproduce
  * _Reference:_ [Section 2.1, Page 36:3; Section 4.1, Page 36:19]

* **Gap addressed:** Prior work (ReCDroid, Yakusu) relied on manually-crafted grammar patterns for S2R extraction and greedy GUI exploration, failing when steps were missing or imprecisely described
  * _Reference:_ [Section 1, Page 36:2]

---

## 📥 Input Representation (CRITICAL)

* **What is the input to the system?**
   * [x] Text bug report (HTML format from GitHub, Google Code, Bitbucket, GitLab)
   * [ ] GUI screenshots
   * [ ] Execution traces
   * [ ] Video
   * [ ] Source code
   * [x] APK file
   * [ ] Crash logs / Stack traces
   * Other: error message string (to verify crash)

   _Reference:_ [Section 3, Figure 2, Page 36:6]

* **Input quality:**
   * Unstructured natural language; often incomplete, imprecise, or missing steps
   * Noisy HTML requiring parsing
   * Preprocessing: HTML parsing → sentence segmentation → S2R/crash classification
   * _Reference:_ [Section 2.2, Pages 36:4–5; Section 3.1, Page 36:7]

* **Limitations of input:**
   * Steps may be missing or poorly described
   * Reporters may use different words than UI component labels
   * May reference account credentials, special app states not reproducible without setup
   * _Reference:_ [Section 2.2, Page 36:4; Section 4.1, Page 36:19]

---

## 🧠 Role of LLM (if applicable)

* **Is LLM used?** → No (uses classical NLP + deep learning)
  _Reference:_ [Section 3, Page 36:6]

**Deep learning models used instead:**

* **Usage:**
   * [x] Bug report understanding/parsing (CNN+LSTM for S2R and crash sentence classification)
   * [x] GUI understanding (Word2vec for semantic matching between bug report and UI elements)

* **Which model?**
   * CNN + LSTM (sentence feature extraction + sequential dependency modeling)
   * Word2vec (word embeddings for semantic similarity)
   * _Reference:_ [Sections 3.1.2, 3.2.2, Pages 36:8–16]

* **Prompting strategy:** N/A — rule-based S2R refining + NLP pattern matching

* **Key observation:**
   * Deep learning (CNN+LSTM) outperforms pattern-based S2R extraction; Word2vec bridges lexical gap between bug report vocabulary and actual UI labels
   * _Reference:_ [Section 4.3.2, Page 36:20]

---

## 👁️ Vision Component (if applicable)

* **Is vision/image understanding used?** → No
  _Reference:_ [Section 3, Page 36:6]

---

## 🔁 System Design / Pipeline

**Describe full pipeline (step-by-step):**

1. **Input Processing (Preprocessing):**
   * HTML parsing (lxml) to extract title + comments from bug tracking systems
   * Sentence segmentation via SpaCy
   * `numDot` substitution for list items
   * _Reference:_ [Section 3.1.1, Page 36:7]

2. **S2R and Crash Sentence Extraction:**
   * CNN extracts sentence feature vectors from Word2vec embeddings
   * LSTM models inter-sentence dependencies
   * Binary classification: S2R vs. non-S2R, crash vs. non-crash
   * 11 S2R refining rules applied to reduce false positives/negatives
   * _Reference:_ [Sections 3.1.2–3.1.3, Pages 36:8–12]

3. **Event Representation Extraction (Bug Report Analysis):**
   * 15 grammar patterns (derived from SpaCy dependency parsing) extract event tuples: {action, GUI component, input}
   * Three event categories: Click, Edit, Gesture
   * _Reference:_ [Section 3.2, Pages 36:12–14]

4. **Guided Dynamic Exploration:**
   * Builds a Dynamic Ordered Event Tree (DOET) representing app GUI state space
   * GUI components matched to bug report via Word2vec (cosine similarity ≥ 0.8) and n-gram matching
   * Leftmost-first traversal prioritizes relevant components; backtracking on failure
   * _Reference:_ [Section 3.3, Pages 36:14–18; Algorithm 1]

5. **Oracle / Verification:**
   * Crash detected when AUT produces the specified error message
   * Stack trace comparison when available
   * _Reference:_ [Section 4.3.1, Page 36:20]

6. **Output:**
   * Replay script (sequence of GUI events) that reproduces the crash
   * _Reference:_ [Section 3, Figure 2, Page 36:6]

**Architecture diagram:**

```text
┌─────────────────────────────────────────────────────────────────────┐
│                        INPUT                                        │
│          HTML Bug Report (GitHub/GitLab/etc.)  +  APK File          │
└────────────────────────────┬────────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────────┐
│  STAGE 1: Preprocessing                                             │
│  • lxml parses HTML → extracts title + comments                     │
│  • SpaCy segments text into sentences                               │
│  • numDot substitution normalizes list items                        │
└────────────────────────────┬────────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────────┐
│  STAGE 2: S2R & Crash Sentence Classification  (CNN + LSTM)         │
│  • Word2vec embeds each sentence                                    │
│  • CNN extracts local feature vectors per sentence                  │
│  • LSTM models inter-sentence dependencies                          │
│  • Binary classifiers: S2R / non-S2R  &  Crash / non-Crash         │
│  • 11 refining rules reduce false positives / negatives             │
└────────────────────────────┬────────────────────────────────────────┘
                             │  Ordered list of S2R sentences
                             ▼
┌─────────────────────────────────────────────────────────────────────┐
│  STAGE 3: Event Representation Extraction                           │
│  • SpaCy dependency parsing + 15 grammar patterns                  │
│  • Each S2R sentence → event tuple {action, GUI component, input}  │
│  • Action categories: Click | Edit | Gesture                        │
└────────────────────────────┬────────────────────────────────────────┘
                             │  Ordered event list
                             ▼
┌─────────────────────────────────────────────────────────────────────┐
│  STAGE 4: Guided Dynamic Exploration  (DOET)                        │
│  • Launches AUT on device/emulator (Robotium + UI Automator)        │
│  • Builds Dynamic Ordered Event Tree from live UI state             │
│  • Matches UI widgets to event tuples via:                          │
│      – Word2vec cosine similarity (threshold ≥ 0.8)                 │
│      – n-gram string matching                                        │
│  • Leftmost-first traversal of DOET; backtrack on mismatch          │
│  • Loop detection: marks node dead if sequence repeats 3×           │
└────────────────────────────┬────────────────────────────────────────┘
                             │  Executed GUI actions
                             ▼
┌─────────────────────────────────────────────────────────────────────┐
│  STAGE 5: Oracle / Verification                                     │
│  • Monitors AUT for the specified error message                     │
│  • Optionally compares stack trace if provided                      │
│  • Crash confirmed → stop exploration                               │
└────────────────────────────┬────────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────────┐
│  OUTPUT: Replay Script (sequence of GUI events that reproduce crash)│
└─────────────────────────────────────────────────────────────────────┘
```

_Reference:_ [Figure 2, Page 36:6]

**Key algorithms/techniques:**
* DOET-based guided DFS exploration (Algorithm 1)
* IsMatch algorithm with Word2vec similarity (Algorithm 2)
* Mean-shift clustering for S2R refining rule prioritization
* _Reference:_ [Algorithms 1–2, Section 3.3, Pages 36:15–16]

**Novelty:**
* End-to-end automation from raw HTML bug report to replay script
* CNN+LSTM for S2R extraction (vs. pattern-only in prior work)
* DOET exploration guided by extracted S2R (vs. exhaustive DFS)
* _Reference:_ [Section 1, Page 36:2]

---

## 🎬 Action Space & Execution

* **What actions can the system perform?**
   * [x] Tap / Click
   * [x] Swipe / Scroll (gesture: rotate)
   * [x] Type text (edit events)
   * [x] Back button (gesture: back)
   * [ ] System actions (rotate partially supported)

   _Reference:_ [Section 3.2, Table 2, Page 36:13]

* **How are actions selected?**
   * DOET-based guided exploration: leftmost relevant leaf node selected; Word2vec + n-gram matching determines relevance
   * _Reference:_ [Section 3.3.1, Algorithm 1, Page 36:15]

* **How are actions executed?**
   * Real devices and emulators
   * Tools: Robotium + UI Automator
   * _Reference:_ [Section 4.2, Page 36:20]

* **Handling dynamic/complex UIs:**
   * Loop detection: if subsequence appears 3× in path, set node to dead
   * Same-screen detection to avoid redundant exploration
   * _Reference:_ [Section 3.3.4, Page 36:18]

---

## 🔍 Oracle / Bug Detection

* **How does the system know a bug is reproduced?**
   * [x] Crash detection (AUT crashes with specified error message)
   * [x] Execution trace matching (stack trace comparison when available)

   _Reference:_ [Section 4.3.1, Page 36:20]

* **False positive/negative handling:**
   * When crash occurs, user prompted to confirm if it matches the reported crash
   * Stack trace used as additional signal when provided
   * _Reference:_ [Section 3.3.1, Page 36:15; Section 4.3.1, Page 36:20]

---

## 📊 Evaluation

### **Dataset:**

* **Name/Source:** 66 bug reports from 37 Android apps (filtered from 400 candidates crawled from GitHub + FUSION paper apps)
  * _Reference:_ [Section 4.1, Page 36:19]

* **Size:** 66 bug reports, 37 apps
  * _Reference:_ [Section 4.1, Page 36:19]

* **Bug types:** Crash bugs only
  * _Reference:_ [Abstract, Page 36:1]

* **Real-world or synthetic?** Real-world (GitHub bug reports)
  * _Reference:_ [Section 4.1, Page 36:19]

* **Publicly available?** Yes (artifacts including dataset, apks, user study)
  * _Reference:_ [Section 1, Page 36:3]

### **Baselines:**

* **What is this paper compared against?**
  * ReCDroid (predecessor) and Yakusu (state-of-the-art at time)
  * ReCDroid+_N (no grammar patterns, only RL exploration) and ReCDroid+_D (no dynamic matching, no grammar patterns) — ablation variants
  * _Reference:_ [Section 4.3, Pages 36:20–21]

* **Are baselines strong/recent?** Yes — ReCDroid and Yakusu were the state-of-the-art at submission time
  * _Reference:_ [Section 5, Page 36:21]

### **Metrics:**

* [x] **Reproduction rate** (% of bug reports successfully reproduced)
* [x] **Precision / Recall / F1** (for S2R extraction)
* [x] **Time to reproduce**
* [x] **Human effort required** (user study: time to manually reproduce)

_Reference:_ [Section 4.3, Pages 36:20–22]

### **Results Summary:**

* **Main quantitative findings:**
  * ReCDroid+ reproduced 42/66 crashes (63.6% success rate)
  * 88% of 630 mutated (degraded) bug reports still successfully reproduced
  * S2R extraction: F1 > 0.7 (considered good); crash sentence: higher F1
  * Faster than ReCDroid (avg 1,334s vs. 1,991s per reproduction)
  * _Reference:_ [Abstract; Section 4.3, Pages 36:20–22]

* **Best performing configuration:** Full ReCDroid+ (NLP + dynamic matching)
  * _Reference:_ [Section 4.4.3, Page 36:21]

* **Ablation studies:**
  * ReCDroid+_N (no grammar patterns) reproduced 8 more bugs than ReCDroid but less than full system — grammar patterns critical
  * ReCDroid+_D (no dynamic matching) reproduced 2 fewer bugs — dynamic matching helps bridge missing steps
  * _Reference:_ [Section 4.4.3, Pages 36:21–22]

* **Statistical significance:** Not reported explicitly

### **Qualitative Analysis:**

* **Case studies?** Yes — running example (LibreNews crash) traced through full pipeline
  * _Reference:_ [Section 3.3.3, Figure 7, Page 36:17]

* **Failure analysis?** Yes — 5 categories of irreproducible bugs identified (lack of APK, environmental issues, missing credentials, etc.)
  * _Reference:_ [Section 4.1, Page 36:19]

* **What types of bugs does it handle well/poorly?**
  * Well: crashes with clear textual S2R, standard UI interactions
  * Poorly: crashes requiring account credentials, app-specific setup, or unclear natural language descriptions
  * _Reference:_ [Section 4.1, Page 36:19]

---

## 💪 Strengths

* **What does this approach do really well?**
  * Fully automated end-to-end pipeline; handles low-quality/incomplete bug reports via guided exploration; outperforms prior state-of-the-art on both S2R extraction and reproduction
  * _Reference:_ [Abstract; Section 4.4, Page 36:21]

* **What's the biggest contribution?**
  * CNN+LSTM-based S2R extraction replacing hand-crafted patterns + DOET-guided exploration that bridges missing steps
  * _Reference:_ [Section 1, Page 36:2]

---

## ⚠️ Limitations / Weaknesses

### **Technical:**
* Crash-only scope — cannot handle functional/non-crash bugs
  * _Reference:_ [Section 4.1, Page 36:19]
* Word2vec similarity (threshold 0.8) may miss valid matches or cause false positives
  * _Reference:_ [Section 3.3.2, Page 36:16]
* 22-hour time limit per bug; 3 hours per reproduction attempt
  * _Reference:_ [Section 4.3.1, Page 36:20]

### **Experimental:**
* Only 66 bug reports — relatively small evaluation set
  * _Reference:_ [Section 4.1, Page 36:19]
* Manual cost of ground-truth labeling: ~500 researcher hours
  * _Reference:_ [Section 4.1, Page 36:19]

### **Practical:**
* Requires APK file — unavailable for some apps (failed-to-compile, removed from store)
  * _Reference:_ [Section 4.1, Page 36:19]
* Supports only 4 bug tracking systems (GitHub, Google Code, Bitbucket, GitLab)
  * _Reference:_ [Section 3.1.1, Page 36:7]

### **Threats to Validity:**
* External validity: evaluation dataset may not represent all bug reports; crash-only focus limits generalizability
* Internal validity: randomness in RL-based matching; mitigated by running 3× and taking consensus
* _Reference:_ [Section 4.5, Pages 36:22–23]

---

## 🔮 Future Work / Open Questions

* **What do the authors suggest as next steps?**
  * Extend to non-crash functional bugs
  * Support more bug tracking systems
  * Improve handling of rotate and other gesture events
  * _Reference:_ [Section 8, Page 36:23]

* **What's still unsolved?**
  * Crashes requiring external accounts, specific device states, or network conditions
  * Handling apps with complex dynamic UIs (e.g., web-based content)
  * _Reference:_ [Section 4.1, Page 36:19]

---

## 💡 Key Takeaways

* **One-line summary:** ReCDroid+ automates Android crash reproduction by combining CNN+LSTM S2R extraction with DOET-guided GUI exploration.

* **Most interesting insight:**
  * 12 of the 24 unreproduced crashes could have been reproduced if execution engine limitations (e.g., failing to click certain buttons) were removed — the bottleneck shifts from NLP to execution
  * _Reference:_ [Abstract, Page 36:1]

* **Relevance to my work:** Strong baseline for text-based crash reproduction; represents the "NLP without vision" approach.

* **Ideas to borrow/adapt:**
  * DOET exploration strategy for guiding app traversal
  * S2R extraction pipeline as a preprocessing step
  * Grammar patterns taxonomy (click/edit/gesture) for event classification

---

## 📎 Related Work

* **Prior work this builds on:**
  * ReCDroid (predecessor — conference version), Yakusu, FUSION
  * _Reference:_ [Section 6, Page 36:21]

* **Key citations to follow up:**
  * [Zhao et al., 2019] ReCDroid — original conference paper
  * [Fazzini et al., 2018] Yakusu — translating bug reports to test cases
  * [Su et al., 2017] DroidBot — automated Android GUI exploration

---

## 🔬 Reproducibility

* **Enough detail to reimplement?** Yes (algorithms provided, grammar patterns described)

* **Hyperparameters provided?**
  * Word2vec similarity threshold: 0.8; LSTM: 4 neighbor sentences; epochs: 2000
  * _Reference:_ [Sections 3.1.2, 3.3.2, Pages 36:9, 36:16]

* **Computational resources mentioned?**
  * x86 Ubuntu 16.04, i7-4790 CPU @ 3.60GHz, 32GB RAM, no GPU
  * _Reference:_ [Section 4.2, Page 36:20]

* **Random seed / initialization:** Not specified

---

## 🏷️ Tags

`#NLP` `#DeepLearning` `#CNN` `#LSTM` `#Word2vec` `#GUI-Testing` `#Crash-Reproduction` `#Android` `#S2R-Extraction` `#DOET`

---

## 📝 Notes / Comments

* Personal observations: This is the journal extension of the original ReCDroid (ICSE 2019). The key upgrade is replacing purely pattern-based S2R extraction with CNN+LSTM. Still entirely text-based — no vision.
* Questions to ask: How does the system handle multi-screen workflows where intermediate screens are not mentioned in the bug report?
* Connection to other papers: Direct predecessor to ReproBot; contrasts with ADBGPT/ReBL which use LLMs instead of classical NLP.

---

## 📊 Quick Comparison Table

| Aspect | ReCDroid+ | ReproBot | JANUS |
|--------|-----------|---------|-------|
| Input Type | Text bug report + APK | Text bug report | Video bug reports |
| Uses LLM? | No (CNN+LSTM) | Yes (NLP+RL) | No (ViT + OCR) |
| Uses Vision? | No | No | Yes |
| Dataset Size | 66 reports, 37 apps | 77 reports | 7,290 tasks, 270 videos |
| Repro Rate | 63.6% | 64% | 89.8% mRR |
| Baseline | ReCDroid, Yakusu | ReCDroid, Yakusu | TANGO (prior duplicate detector) |
| Code Available | Yes | Yes | Not mentioned |

---

**Template Version:** 1.0
**Last Updated:** 2026-04-10
