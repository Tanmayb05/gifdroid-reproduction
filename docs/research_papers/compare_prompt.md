# 📄 Research Paper Comparison Template

**Domain:** Android Bug Reproduction (LLM / Vision / GUI Testing)

---

## 🧾 Paper Info

* **Title:**
* **Authors:**
* **Year / Venue:**
* **Link:**
* **Code Available:** Yes / No → [link]

---

## 🎯 Problem Statement

* **What problem is this paper solving?**
  * _Reference:_ [Section X, Page Y]
  
* **Why is this problem important?**
  * _Reference:_ [Section X, Page Y]
  
* **What assumptions does the paper make?**
  * _Reference:_ [Section X, Lines Y-Z]
  
* **Gap addressed:** What existing approaches fail to do?
  * _Reference:_ [Section X, Page Y]

---

## 📥 Input Representation (CRITICAL)

* **What is the input to the system?**
   * [ ] Text bug report
   * [ ] GUI screenshots
   * [ ] Execution traces
   * [ ] Video (screen / handheld)
   * [ ] Source code
   * [ ] APK file
   * [ ] Crash logs / Stack traces
   * [ ] Other: ___________
   
   _Reference:_ [Section X, Figure Y, Page Z]

* **Input quality:**
   * Structured / Semi-structured / Unstructured?
   * Clean or noisy?
   * Preprocessing required?
   
   _Reference:_ [Section X, Page Y]

* **Limitations of input:**
   * Missing information?
   * Ambiguity?
   * Real-world feasibility?
   * Human effort required?
   
   _Reference:_ [Section X, Page Y]

---

## 🧠 Role of LLM (if applicable)

* **Is LLM used?** → Yes / No  
  _Reference:_ [Section X, Page Y]

**If YES:**

* **Usage:**
   * [ ] Action prediction
   * [ ] Test oracle (bug detection)
   * [ ] GUI understanding
   * [ ] Exploration planning
   * [ ] Bug report understanding/parsing
   * [ ] Code generation
   * [ ] Other: ___________
   
   _Reference:_ [Section X, Figure Y, Page Z]

* **Which LLM?**
   * GPT-3.5 / GPT-4 / Claude / Gemini / Open-source (specify)
   * Model size / version?
   
   _Reference:_ [Section X, Page Y]

* **Prompting strategy:**
   * Zero-shot / Few-shot / In-context learning?
   * Multi-prompt decomposition?
   * Chain-of-thought?
   * Feedback-driven / Self-refinement?
   * Prompt templates provided in paper?
   
   _Reference:_ [Section X, Listing Y, Page Z]

* **Key observation:**
   * What unique capability does LLM provide here?
   * Could this be done without LLM? If yes, what's the advantage?
   
   _Reference:_ [Section X, Page Y]

---

## 👁️ Vision Component (if applicable)

* **Is vision/image understanding used?** → Yes / No  
  _Reference:_ [Section X, Page Y]

**If YES:**

* **Vision model:**
   * OCR / Object detection / Screenshot understanding / Video analysis
   * Model: GPT-4V / Claude Vision / Custom CNN / Other
   
   _Reference:_ [Section X, Page Y]

* **What visual information is extracted?**
   * UI element detection
   * Layout understanding
   * Text recognition
   * Widget identification
   * Screen state comparison
   
   _Reference:_ [Section X, Figure Y, Page Z]

* **Integration with other components:**
   * How does vision feed into action selection?
   
   _Reference:_ [Section X, Page Y]

---

## 🔁 System Design / Pipeline

**Describe full pipeline (step-by-step):**

1. **Input Processing:**
   * _Reference:_ [Section X, Page Y]

2. **GUI State Extraction:**
   * _Reference:_ [Section X, Page Y]

3. **Action Generation:**
   * _Reference:_ [Section X, Algorithm Y, Page Z]

4. **Execution:**
   * _Reference:_ [Section X, Page Y]

5. **Oracle / Verification:**
   * _Reference:_ [Section X, Page Y]

6. **Feedback Loop (if any):**
   * _Reference:_ [Section X, Page Y]

**Architecture diagram:**  
_Reference:_ [Figure X, Page Y]

**Key algorithms/techniques:**  
_Reference:_ [Algorithm X, Section Y, Page Z]

**Novelty:** What's new compared to prior work?  
_Reference:_ [Section X, Page Y]

---

## 🎬 Action Space & Execution

* **What actions can the system perform?**
   * [ ] Tap / Click
   * [ ] Swipe / Scroll
   * [ ] Type text
   * [ ] Back button
   * [ ] System actions (rotate, home, etc.)
   * [ ] Other: ___________
   
   _Reference:_ [Section X, Table Y, Page Z]

* **How are actions selected?**
   * Rule-based / Heuristic / Model-based / LLM-driven
   
   _Reference:_ [Section X, Algorithm Y, Page Z]

* **How are actions executed?**
   * Real device / Emulator / Simulator
   * Tool: UIAutomator / Espresso / Appium / ADB / Custom
   
   _Reference:_ [Section X, Page Y]

* **Handling dynamic/complex UIs:**
   * How does it deal with popups, dialogs, permissions?
   
   _Reference:_ [Section X, Page Y]

---

## 🔍 Oracle / Bug Detection

* **How does the system know a bug is reproduced?**
   * [ ] Crash detection
   * [ ] Visual comparison (screenshots)
   * [ ] Assertion checking
   * [ ] LLM-based judgment
   * [ ] Human verification
   * [ ] Execution trace matching
   * [ ] Other: ___________
   
   _Reference:_ [Section X, Page Y]

* **False positive/negative handling:**
  * _Reference:_ [Section X, Page Y]

---

## 📊 Evaluation

### **Dataset:**

* **Name/Source:**
  * _Reference:_ [Section X, Table Y, Page Z]

* **Size:** (# apps, # bugs)
  * _Reference:_ [Table X, Page Y]

* **Bug types:** (crash, functional, UI, performance, etc.)
  * _Reference:_ [Section X, Table Y, Page Z]

* **Real-world or synthetic?**
  * _Reference:_ [Section X, Page Y]

* **Publicly available?** Yes / No
  * _Reference:_ [Section X, Footnote Y, Page Z]

### **Baselines:**

* **What is this paper compared against?**
  * _Reference:_ [Section X, Table Y, Page Z]

* **Are baselines strong/recent?**
  * _Reference:_ [Section X, Page Y]

### **Metrics:**

* [ ] **Reproduction rate** (%)
* [ ] **Precision / Recall / F1**
* [ ] **Time to reproduce**
* [ ] **# steps required**
* [ ] **Success rate**
* [ ] **Code coverage**
* [ ] **Human effort required**
* [ ] Other: ___________

_Reference:_ [Section X, Table Y, Page Z]

### **Results Summary:**

* **Main quantitative findings:**
  * _Reference:_ [Table X, Page Y, Lines Z-W]

* **Best performing configuration:**
  * _Reference:_ [Table X, Page Y]

* **Ablation studies:** (What components matter most?)
  * _Reference:_ [Section X, Table Y, Page Z]

* **Statistical significance:** (p-values, confidence intervals)
  * _Reference:_ [Section X, Page Y]

### **Qualitative Analysis:**

* **Case studies?**
  * _Reference:_ [Section X, Figure Y, Page Z]

* **Failure analysis?**
  * _Reference:_ [Section X, Page Y]

* **What types of bugs does it handle well/poorly?**
  * _Reference:_ [Section X, Table Y, Page Z]

---

## 💪 Strengths

* **What does this approach do really well?**
  * _Reference:_ [Section X, Page Y]

* **What's the biggest contribution?**
  * _Reference:_ [Abstract, Section X, Page Y]

---

## ⚠️ Limitations / Weaknesses

### **Technical:**
* Scalability issues?
  * _Reference:_ [Section X, Page Y]
* Reproducibility concerns?
  * _Reference:_ [Section X, Page Y]
* Computational cost?
  * _Reference:_ [Section X, Table Y, Page Z]

### **Experimental:**
* Limited evaluation?
  * _Reference:_ [Section X, Page Y]
* Weak baselines?
  * _Reference:_ [Section X, Page Y]
* Dataset issues?
  * _Reference:_ [Section X, Page Y]

### **Practical:**
* Generalizability?
  * _Reference:_ [Section X, Page Y]
* Real-world deployment feasibility?
  * _Reference:_ [Section X, Page Y]
* Human-in-the-loop requirements?
  * _Reference:_ [Section X, Page Y]

### **Threats to Validity:**
* What do the authors acknowledge?
  * _Reference:_ [Section X, Page Y]

---

## 🔮 Future Work / Open Questions

* **What do the authors suggest as next steps?**
  * _Reference:_ [Section X (Future Work/Discussion), Page Y]

* **What's still unsolved?**
  * _Reference:_ [Section X, Page Y]

---

## 💡 Key Takeaways

* **One-line summary:**

* **Most interesting insight:**
  * _Reference:_ [Section X, Page Y]

* **Relevance to my work:**

* **Ideas to borrow/adapt:**

---

## 📎 Related Work

* **Prior work this builds on:**
  * _Reference:_ [Section X (Related Work), Page Y]

* **Concurrent work:**
  * _Reference:_ [Section X, Page Y]

* **Key citations to follow up:**
  * [Author et al., Year] - 
  * [Author et al., Year] - 

---

## 🔬 Reproducibility

* **Enough detail to reimplement?** Yes / Partial / No

* **Hyperparameters provided?**
  * _Reference:_ [Section X, Table Y, Page Z]

* **Computational resources mentioned?**
  * _Reference:_ [Section X, Page Y]

* **Random seed / initialization?**
  * _Reference:_ [Section X, Page Y]

---

## 🏷️ Tags

`#LLM` `#Vision` `#GUI-Testing` `#Bug-Reproduction` `#Android` `#Evaluation` `#Dataset-X`

---

## 📝 Notes / Comments

* Personal observations:
* Questions to ask authors:
* Connection to other papers:

---

## 📊 Quick Comparison Table (for multiple papers)

| Aspect | This Paper | Paper 2 | Paper 3 |
|--------|------------|---------|---------|
| Input Type | | | |
| Uses LLM? | | | |
| Uses Vision? | | | |
| Dataset Size | | | |
| Repro Rate | | | |
| Baseline | | | |
| Code Available | | | |

---

**Template Version:** 1.0  
**Last Updated:** 2026-04-10