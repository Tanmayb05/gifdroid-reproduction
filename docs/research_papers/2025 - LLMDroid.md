# 📄 LLMDroid: Enhancing Automated Mobile App GUI Testing Coverage with Large Language Model Guidance

**Domain:** Android GUI Testing (LLM / Code Coverage / Automated Testing — NOT bug reproduction)

---

## 🧾 Paper Info

* **Title:** LLMDroid: Enhancing Automated Mobile App GUI Testing Coverage with Large Language Model Guidance
* **Authors:** Chenxu Wang, Tianming Liu, Yanjie Zhao, Minghui Yang, Haoyu Wang
* **Year / Venue:** 2025 / Proceedings of the ACM on Software Engineering, Vol. 2, No. FSE, Article FSE046 (July 2025)
* **Link:** https://doi.org/10.1145/3715763
* **Code Available:** Yes → https://github.com/security-pride/LLMDroid

---

## 🎯 Problem Statement

* **What problem is this paper solving?**
  * Enhancing **code coverage** of existing automated Android GUI testing tools by selectively leveraging LLMs to overcome testing bottlenecks (tools getting trapped in loops or focused on limited page subsets)
  * _Reference:_ [Abstract, Page FSE046-1]

* **Why is this problem important?**
  * Automated GUI testing tools frequently plateau in code coverage by looping among a limited set of pages; constant LLM querying (step-by-step) is too expensive; a hybrid approach maximizes coverage while controlling cost
  * _Reference:_ [Section 1, Pages FSE046-1–2]

* **What assumptions does the paper make?**
  * An existing automated testing tool (Droidbot, Humanoid, Fastbot) runs the app autonomously; LLMDroid enhances it by adding LLM guidance when coverage growth stalls; apps are closed-source (black-box); Android platform
  * _Reference:_ [Section 3, Page FSE046-4; Section 4.1, Page FSE046-11]

* **Gap addressed:** Existing LLM-for-testing approaches (GPTDroid, DroidAgent) run LLM at every step — expensive and slow; LLMDroid only calls LLM when autonomous tool plateaus, dramatically reducing LLM interaction cost
  * _Reference:_ [Section 1, Pages FSE046-1–2; Section 4.3, Pages FSE046-16–17]

---

## 📥 Input Representation (CRITICAL)

* **What is the input to the system?**
   * [ ] Text bug report
   * [x] GUI screenshots (implicitly via view hierarchy)
   * [x] Execution traces (code coverage data, UI transition history)
   * [ ] Video
   * [ ] Source code (black-box — uses black-box coverage via AndroLog)
   * [x] APK file (closed-source apps from Google Play)
   * [ ] Crash logs

   _Reference:_ [Section 4.1, Pages FSE046-11–12]

* **Input quality:**
   * Real commercial apps from Google Play (not open-source); 14 apps across popular categories
   * Code coverage tracked in real-time via AndroLog (static APK instrumentation, black-box)
   * UI page represented as HTML-converted view hierarchy
   * _Reference:_ [Section 4.1, Pages FSE046-11–12]

* **Limitations of input:**
   * Some apps crash after Soot instrumentation (used by AndroLog)
   * HTML representation may lack semantic info for widgets with no text/resource-ID
   * _Reference:_ [Section 5, Page FSE046-18; Section 4.1, Page FSE046-12]

---

## 🧠 Role of LLM (if applicable)

* **Is LLM used?** → Yes
  _Reference:_ [Abstract, Page FSE046-1]

* **Usage:**
   * [x] Exploration planning (GUI Summary: understand page functionalities; Target Selection: select next target page/functionality)
   * [x] Action prediction (Guided Functionality Execution: step-by-step action guidance for target functionality)
   * [x] GUI understanding (HTML-based page summarization; functionality importance ranking)

   _Reference:_ [Sections 3.1–3.2, Pages FSE046-4–10]

* **Which LLM?**
   * GPT-4o (primary for evaluation); also tested GPT-3.5-turbo, GPT-4o-mini
   * _Reference:_ [Section 4.1, Page FSE046-12; Section 4.3, Table 4, Page FSE046-16]

* **Prompting strategy:**
   * **GUI Summary prompt**: App Information + HTML Description + Top P1 Pages + Query Summary
   * **Target Selection prompt**: App Information + Top P2 Pages + Query Target
   * **Functionality Execution prompt**: App Information + HTML Description + Query Step
   * Functionality-oriented and importance-aware: asks LLM to rank functionalities by exploratory potential
   * No few-shot examples; relies on instruction-following
   * P1=5, P2=10, Q1=5, Q2=5 (empirically determined)
   * _Reference:_ [Sections 3.1.2, 3.2.1, Table 1, Pages FSE046-5–8]

* **Key observation:**
   * Running LLM concurrently with autonomous exploration (not blocking test execution) eliminates the major overhead that plagues step-by-step LLM approaches (DroidAgent, GPTDroid)
   * LLM is only invoked when new PageClusters form (~once per distinct app page) — dramatically fewer calls than step-by-step
   * _Reference:_ [Sections 3.1, 4.3, Pages FSE046-4, FSE046-16–17]

---

## 👁️ Vision Component (if applicable)

* **Is vision/image understanding used?** → No (uses HTML text representation of UI, not screenshots)
  _Reference:_ [Section 3.1.2, Page FSE046-5]

* Note: LLMs are noted to have limited page comprehension when widget HTML lacks semantic information; future work suggests incorporating multimodal models (pix2struct, MM-Navigator)
  * _Reference:_ [Section 5, Page FSE046-18]

---

## 🔁 System Design / Pipeline

**Describe full pipeline (step-by-step):**

1. **Autonomous Exploration Stage (main loop):**
   * Existing testing tool (Droidbot/Humanoid/Fastbot) runs normally
   * **Coverage Monitoring module**: tracks code coverage growth rate in real-time
     * Dynamic threshold T adjusted by exponential function: T_n = T_{n-1} × e^{Δg}
     * Window W=80 consecutive low-growth actions → transition to LLM Guidance
   * **GUI Summary module**: concurrently summarizes each new PageCluster
     * UI State Clustering: pages grouped into PageClusters by Dice Coefficient widget similarity (threshold T_S=0.6)
     * LLM queried once per new PageCluster (not per action) — runs concurrently
     * Output: page overview + ranked functionality list + top-5 importance score
   * _Reference:_ [Sections 3.1.1–3.1.3, Pages FSE046-4–9]

2. **Transition to LLM Guidance:**
   * When Coverage Monitoring detects sustained low growth → interrupt autonomous exploration
   * Switch to LLM Guidance stage to overcome bottleneck
   * _Reference:_ [Section 3.1.3, Page FSE046-8]

3. **LLM Guidance Stage:**
   * **Target Selection**: LLM selects target page + target functionality from top-P2 important pages
   * **Offline Page Navigation**: navigate to target page using existing autonomous traces (Dijkstra's algorithm on UI transition graph) — no LLM needed for navigation
   * **Guided Functionality Execution**: step-by-step LLM dialogue to execute target functionality (max 5 steps)
   * Return to Autonomous Exploration stage after completion
   * _Reference:_ [Sections 3.2.1–3.2.3, Pages FSE046-8–10]

4. **Feedback Loop:**
   * After Guided Functionality Execution, tool transitions back to Autonomous Exploration
   * If navigation fails (3 attempts with decreasing threshold): revert to LLM for new target
   * _Reference:_ [Section 3.2.2, Page FSE046-9]

**Architecture diagram:**

```text
┌───────────────────────────────────────────────────────────────────┐
│                          INPUT                                    │
│     APK File  +  Existing Automated Testing Tool (Droidbot /      │
│                   Humanoid / Fastbot)                             │
└────────────────────┬──────────────────────────────────────────────┘
                     │
                     ▼
┌───────────────────────────────────────────────────────────────────┐
│  AUTONOMOUS EXPLORATION STAGE  (underlying tool runs freely)      │
│                                                                   │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │  Coverage Monitor  (runs in parallel)                        │ │
│  │  • Tracks method-level code coverage via AndroLog            │ │
│  │  • Dynamic threshold: T_n = T_{n-1} × e^{Δg}                │ │
│  │  • Window W=80 consecutive low-growth actions                │ │
│  │    → triggers transition to LLM Guidance                     │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                                                                   │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │  GUI Summary Module  (runs concurrently — non-blocking)      │ │
│  │  • UI State Clustering: pages grouped into PageClusters      │ │
│  │    via Dice Coefficient widget similarity (threshold 0.6)    │ │
│  │  • LLM queried once per new PageCluster (not per action)     │ │
│  │    Prompt: App Info + HTML page description + top-5 pages    │ │
│  │  • Output: page overview + ranked functionality list         │ │
│  │    + importance scores stored for later use                  │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                                                                   │
│  [Coverage growth stalls → hand off to LLM Guidance Stage]       │
└────────────────────┬──────────────────────────────────────────────┘
                     │  bottleneck detected
                     ▼
┌───────────────────────────────────────────────────────────────────┐
│  LLM GUIDANCE STAGE                                               │
│                                                                   │
│  STEP 1 – Target Selection                                        │
│  • LLM selects target page + target functionality                 │
│    from top-P2 (P2=10) highest-importance pages                   │
│    Prompt: App Info + top-P2 pages + query                        │
│                                                                   │
│  STEP 2 – Offline Page Navigation  (no LLM needed)               │
│  • Dijkstra's algorithm on UI transition graph                    │
│    (built from historical execution traces)                       │
│  • Navigates to target page using known widget sequences          │
│  • If navigation fails 3× → reduce similarity threshold by 0.05  │
│    and retry; if still failing → pick new target                  │
│                                                                   │
│  STEP 3 – Guided Functionality Execution                          │
│  • Step-by-step LLM dialogue (max 5 steps)                        │
│    Prompt: App Info + current HTML page + query step              │
│  • LLM suggests one action at a time toward target functionality  │
│  • Actions executed by underlying testing tool                    │
└────────────────────┬──────────────────────────────────────────────┘
                     │  functionality executed → return to Autonomous
                     ▼
┌───────────────────────────────────────────────────────────────────┐
│  OUTPUT: Improved code coverage across app pages and activities   │
│  (cycle repeats until 60-minute testing window ends)              │
└───────────────────────────────────────────────────────────────────┘
```

_Reference:_ [Figure 1, Page FSE046-4]

**Key algorithms/techniques:**
* PageCluster similarity (Dice Coefficient on shared widgets)
* Dynamic threshold adjustment for coverage growth detection
* Dijkstra-based offline page navigation using execution trace graph
* Concurrent LLM summarization (non-blocking)
* _Reference:_ [Sections 3.1.1–3.1.3, Pages FSE046-4–9]

**Novelty:**
* **Hybrid approach**: autonomous testing + selective LLM guidance only when needed
* **Concurrent LLM interaction**: GUI Summary runs parallel to testing (not blocking)
* **Offline page navigation**: uses historical traces for navigation — not LLM — saving significant cost
* **Coverage-driven transition**: automatic detection of testing bottlenecks
* _Reference:_ [Abstract; Section 1, Pages FSE046-1–2]

---

## 🎬 Action Space & Execution

* **What actions can the system perform?**
   * Inherits from underlying testing tool (Droidbot/Humanoid/Fastbot)
   * [x] Tap / Click
   * [x] Swipe / Scroll
   * [x] Type text
   * [x] Back button
   * [x] System actions

   _Reference:_ [Section 4.1, Page FSE046-11]

* **How are actions selected?**
   * During Autonomous Exploration: underlying testing tool's strategy (model-based, DL-based, RL-based)
   * During LLM Guidance: LLM-driven step-by-step for target functionality execution
   * _Reference:_ [Sections 3.1, 3.2.3, Pages FSE046-4, FSE046-10]

* **How are actions executed?**
   * Real device: Google Pixel 4, Android 11
   * Via underlying testing tools (Droidbot, Humanoid, Fastbot)
   * _Reference:_ [Section 4.1, Page FSE046-12]

* **Handling dynamic/complex UIs:**
   * Fuzzy matching for offline navigation (similarity threshold T_S)
   * Step Skipping for navigation when current page doesn't match expected
   * _Reference:_ [Section 3.2.2, Page FSE046-9]

---

## 🔍 Oracle / Bug Detection

* **How does the system know a bug is reproduced?**
   * N/A — LLMDroid is a **GUI testing coverage tool**, not a bug reproduction tool
   * Primary metric is code coverage improvement, not bug detection
   * _Reference:_ [Abstract, Page FSE046-1]

* Note: Authors explicitly exclude fault detection metrics due to instrumentation-induced crashes and metric instability
  * _Reference:_ [Section 4.1, Page FSE046-12]

---

## 📊 Evaluation

### **Dataset:**

* **Name/Source:** 14 popular closed-source commercial apps from Google Play (top listings across app categories)
  * _Reference:_ [Section 4.1, Table 2, Pages FSE046-11–12]

* **Size:** 14 apps; categories: Shopping, Entertainment, Education, Tools, Health, Sports, Life, Book, Commercial
  * _Reference:_ [Table 2, Page FSE046-12]

* **Bug types:** N/A (coverage testing, not bug reproduction)

* **Real-world or synthetic?** Real-world commercial apps

* **Publicly available?** Yes (GitHub artifact)
  * _Reference:_ [Data Availability, Page FSE046-20]

### **Baselines:**

* **What is this paper compared against?**
  * Three underlying testing tools: Droidbot, Humanoid, Fastbot (original and LLMDroid-enhanced)
  * DroidAgent and GPTDroid (step-by-step LLM approaches) — for cost comparison
  * Android Monkey (random testing) — reference baseline
  * _Reference:_ [Section 4.2, Table 3, Page FSE046-13; Section 4.3, Table 4, Page FSE046-16]

* **Are baselines strong/recent?** Yes — DroidAgent and GPTDroid are current LLM-based SOTA testing tools
  * _Reference:_ [Section 2.1, Pages FSE046-2–3]

### **Metrics:**

* [x] **Code coverage** (%) — method-level, via AndroLog black-box instrumentation
* [x] **Activity coverage** (%)
* [x] **LLM API cost** ($/app-hour)
* [x] **LLM interaction frequency** (calls/hour)

_Reference:_ [Section 4.2, Table 3, Pages FSE046-13–14]

### **Results Summary:**

* **Main quantitative findings:**
  * LLMDroid achieves average +26.16% code coverage improvement and +29.31% activity coverage improvement across three underlying tools
  * LLMDroid-Fastbot: +30.30% code coverage (best); LLMDroid-Humanoid: +21.29%; LLMDroid-Droidbot: +26.90%
  * Cost: LLMDroid-Fastbot with GPT-4o: $0.49/hr; GPT-4o-mini: $0.03/hr; GPT-3.5-turbo: $0.09/hr
  * GPT-4o-mini achieves 94% of GPT-4o performance at 6.7% of cost ($0.03 vs $0.49/hr)
  * Outperforms DroidAgent and GPTDroid by 19.47%–31.59% in code coverage at lower cost
  * _Reference:_ [Sections 4.2–4.3, Tables 3–4, Pages FSE046-13–17]

* **Best performing configuration:** LLMDroid-Fastbot with GPT-4o (31.59% improvement over DroidAgent)
  * _Reference:_ [Table 4, Page FSE046-16]

* **Ablation studies:**
  * UI Page Similarity Threshold T_S: 0.6 achieves highest code coverage (21.72%); 0.5 and 0.7 slightly lower; 0.8 worst (18.15%)
  * _Reference:_ [Section 4.4, Figure 4, Page FSE046-18]

* **Statistical significance:** Not explicitly reported (no p-values)

### **Qualitative Analysis:**

* **Case studies?** Code coverage progression graph for Wish app (Figure 3) shows clear LLM guidance effect
  * _Reference:_ [Figure 3, Page FSE046-14]

* **Failure analysis?** Yes — four categories of ineffective LLM guidance instances:
  * A1: Insufficient exploration after new page discovery
  * A2: Newly discovered page lacks exploratory potential
  * B1: LLM misinterpretation of UI control functionality
  * B2: Navigation to previously explored pages
  * B3: Unexplored functionalities with small coverage increases
  * B4: Previously explored functionalities accessible from other paths
  * _Reference:_ [Section 4.2 (Effectiveness), Pages FSE046-14–15]

* **What types of bugs does it handle well/poorly?** N/A (coverage tool, not bug reproduction)

---

## 💪 Strengths

* **What does this approach do really well?**
  * Dramatically reduces LLM interaction frequency (~100 calls/hr vs. 1,761/hr for DroidAgent) — 617% fewer calls
  * Achieves better coverage than step-by-step LLM approaches at fraction of cost
  * Works with any existing automated testing tool (model-agnostic enhancement)
  * GPT-4o-mini achieves 94% of GPT-4o performance at $0.03/hr — excellent cost-effectiveness
  * _Reference:_ [Abstract; Table 4, Pages FSE046-16–17]

* **What's the biggest contribution?**
  * Novel hybrid testing paradigm: autonomous exploration + selective LLM guidance only at bottlenecks — the first to effectively combine both without the overhead of constant LLM querying
  * _Reference:_ [Abstract; Section 6, Page FSE046-20]

---

## ⚠️ Limitations / Weaknesses

### **Technical:**
* Limited page comprehension when widgets lack semantic HTML (no text/resource-ID)
  * _Reference:_ [Section 5, Page FSE046-18]
* Offline navigation failures when app state changes dynamically (pop-ups, dynamic content)
  * _Reference:_ [Section 3.2.2, Page FSE046-9]
* AndroLog (Soot-based) causes some apps to crash after instrumentation
  * _Reference:_ [Section 4.1, Page FSE046-12]

### **Experimental:**
* Only 14 apps — relatively small dataset
  * _Reference:_ [Section 4.1, Page FSE046-11]
* 60-minute testing window per app — may not capture long-term coverage behavior
  * _Reference:_ [Section 4.1, Page FSE046-12]
* Activity coverage metric may not align with code coverage (Lan et al. finding)
  * _Reference:_ [Section 4.2, Page FSE046-13]

### **Practical:**
* Multiple interdependent hyperparameters (T_0, W, P1, P2, Q1, Q2) — empirically set, not systematically optimized
  * _Reference:_ [Section 5, Page FSE046-19]
* Android-only; authentication-required apps handled by pre-logging in manually
  * _Reference:_ [Section 4.1, Page FSE046-12]

### **Threats to Validity:**
* Closed-source commercial apps — cannot open-source apps for reproducibility
* AndroLog instrumentation may introduce behavioral changes
* Pre-registration for authenticated apps reduces generalizability
* _Reference:_ [Section 4.1, Page FSE046-12]

---

## 🔮 Future Work / Open Questions

* **What do the authors suggest as next steps?**
  * Incorporate multimodal LLMs (pix2struct, MM-Navigator) for better page comprehension
  * Develop correlation mechanism for pages accessible via different functionalities
  * More systematic parameter optimization
  * _Reference:_ [Section 5, Pages FSE046-18–19]

* **What's still unsolved?**
  * Distinguishing navigation-related from non-navigation functionalities reliably
  * Handling apps with extremely dynamic content or frequent UI changes
  * _Reference:_ [Section 5, Pages FSE046-18–19]

---

## 💡 Key Takeaways

* **One-line summary:** LLMDroid enhances existing Android GUI testing tools by selectively invoking LLMs only when coverage growth stalls, achieving +26% code coverage at ~100× lower LLM interaction cost vs. step-by-step approaches.

* **Most interesting insight:**
  * Running LLM summarization **concurrently** with autonomous testing (not blocking execution) eliminates the major overhead bottleneck — LLM inference time (~seconds) becomes nearly free because the testing tool runs while LLM processes
  * _Reference:_ [Section 3.1, Page FSE046-4; Section 4.3, Page FSE046-16]

* **Relevance to my work:** Tangential — LLMDroid is about coverage testing, not bug reproduction. However, the hybrid architecture (autonomous + selective LLM) and PageCluster concept (UI page similarity grouping) are useful design patterns for any LLM-driven app interaction system.

* **Ideas to borrow/adapt:**
  * PageCluster concept (Dice Coefficient widget similarity) for deduplicating UI states
  * Coverage-based bottleneck detection pattern for any iterative app exploration
  * Concurrent LLM processing while execution continues
  * HTML-based UI encoding for LLM prompts (same as AdbGPT/ReBL)

---

## 📎 Related Work

* **Prior work this builds on:**
  * GPTDroid, DroidAgent — step-by-step LLM testing baselines
  * Droidbot, Humanoid, Fastbot — underlying automated testing tools enhanced
  * _Reference:_ [Sections 2.1–2.2, Pages FSE046-2–3]

* **Key citations to follow up:**
  * [GPTDroid] — step-by-step LLM testing; direct comparison baseline
  * [DroidAgent] — intent-driven LLM testing; direct comparison baseline
  * [AdbGPT, ReBL] — bug reproduction cousins; share HTML encoding approach
  * [AndroLog] — black-box code coverage tool used

---

## 🔬 Reproducibility

* **Enough detail to reimplement?** Yes (detailed prompt designs in Table 1; algorithm described; PageCluster similarity defined; parameters specified)

* **Hyperparameters provided?**
  * T_0=0.05 (initial growth threshold), W=80 (window size), T_S=0.6 (page similarity), P1=5, P2=10, Q1=5, Q2=5; max 3 navigation attempts; threshold reduction 0.05 per failure
  * _Reference:_ [Sections 3.1.1–3.2.2, Pages FSE046-4–9]

* **Computational resources mentioned?**
  * Google Pixel 4, Android 11; 60-minute testing duration; 3-second action interval
  * _Reference:_ [Section 4.1, Page FSE046-12]

* **Random seed / initialization:** Not specified; 3 runs per tool per app; highest coverage taken

---

## 🏷️ Tags

`#LLM` `#GPT-4o` `#GUITesting` `#CodeCoverage` `#Android` `#HybridTesting` `#AutonomousExploration` `#PageCluster` `#CostEfficiency` `#NotBugReproduction`

---

## 📝 Notes / Comments

* Personal observations: **Importantly, LLMDroid is NOT a bug reproduction paper** — it's about maximizing GUI test coverage. Included here because it uses similar LLM-for-Android-GUI techniques and cites AdbGPT/ReBL. The hybrid autonomous+LLM architecture is interesting for the field but the goal is orthogonal to the other papers.
* Questions to ask: Could LLMDroid's coverage-driven exploration be combined with ReBL's feedback-driven reproduction to create a tool that both maximizes coverage AND reproduces specific bugs?
* Connection to other papers: Shares HTML GUI encoding with AdbGPT/ReBL; cites them as related work. The PageCluster deduplication concept could be useful in bug reproduction to avoid revisiting the same screens.

---

**Template Version:** 1.0
**Last Updated:** 2026-04-10
