---
type: paper-reading
date: {{date}}
status: planned
workflow: gemini-notebook
paper:
pdf:
paper_note:
notebook_url:
target_minutes: 45
actual_minutes:
reading_goal:
current_phase: map
completed: false
need_review: true
review_date:
created_at: {{date}}
updated_at: {{date}}
tags:
  - paper-reading
  - gemini-notebook
---

# {{title}}

> [!note] Mục đích
> Template này dùng cho **working note** khi đọc paper bằng Gemini Notebook / NotebookLM. Không dùng AI để đọc thay mình: mình tự đọc, tự recall, rồi dùng Gemini để kiểm tra, giải thích, cross-reference và quiz.

## Cách lưu trong vault

- Note tạo từ template này nên đặt ở `20 - Research/Paper Reading/`.
- Paper note tổng hợp cuối đặt ở `20 - Research/Papers/`.
- Concept reusable tách sang `04 - Concepts/`.
- So sánh nhiều paper đặt ở `20 - Research/Literature Notes/`.

## Setup

- Paper:
- PDF:
- Paper note chính:
- Gemini Notebook / NotebookLM URL:
- Mục tiêu buổi đọc:
- Phần cần đọc:
- Thời gian dự kiến:
- Thời gian thực tế:

## Nguyên tắc đọc

```text
Paper gốc
-> Tự đọc / tự đoán
-> Gemini kiểm tra / giải thích
-> Quay lại paper bằng citation
-> Tự recall + tự viết note
-> Gemini kiểm tra phần còn thiếu
```

| Việc | Mình làm | Gemini hỗ trợ |
|---|---|---|
| Hiểu research problem | tự viết trước | kiểm tra |
| Diễn đạt main idea | tự diễn đạt | chỉ ra thiếu/sai |
| Vẽ method / architecture | tự vẽ | bổ sung chi tiết |
| Tìm citation | kiểm tra lại | tìm nhanh vị trí |
| Giải thích equation | thử trước | giải thích sau |
| Đọc bảng kết quả | tự đọc | kiểm tra caveat |
| Critical thinking | tự đánh giá | challenge |
| Final note | tự viết | audit thiếu/sai |

---

## Phase 1 — Paper Map

### Việc cần làm

Trước khi đọc sâu, chỉ xác định paper có những phần nào và nên đọc ở đâu.

### Prompt gửi Gemini

```text
Do not summarize the paper in detail yet.

Create a structural map of this paper.

Identify:

1. Research problem
2. Motivation
3. Research gap
4. Main contributions
5. Overall architecture / pipeline
6. Main components
7. Loss functions
8. Datasets
9. Baselines
10. Evaluation metrics
11. Main experiments
12. Ablation studies
13. Limitations

For every item:
- identify the relevant section
- identify relevant figures/tables/equations if available
- give only a short description

The purpose is to tell me WHERE to read, not to replace my reading.
```

### Paper map của tôi

- Problem:
- Motivation:
- Gap:
- Main idea:
- Main contribution:
- Important figure:
- Important equations:
- Main result table:
- Ablation table:
- Limitations:

### Chỗ cần đọc trước

- [ ] Abstract
- [ ] Introduction
- [ ] Main figure / architecture
- [ ] Main result table
- [ ] Ablation table
- [ ] Limitation / conclusion

---

## Phase 2 — Pass 1 Recall

### Đọc nhanh

Đọc theo thứ tự:

```text
Title
-> Abstract
-> Introduction
-> Figures
-> Main result tables
-> Conclusion
```

### Closed-book recall của tôi

**Problem**

-

**Why does it matter?**

-

**Research gap**

-

**Main idea**

-

**Main contribution**

-

**Main result**

-

### Prompt kiểm tra recall

```text
I have completed the first pass of the paper.

Here is my understanding:

[PASTE MY NOTES]

Compare my understanding against the paper.

Return:

1. What I understood correctly
2. What is inaccurate
3. Important points I missed
4. Concepts that I may be confusing
5. Relevant source citations/sections for every correction

Do not rewrite the entire paper for me.
Focus on diagnosing my understanding.
```

### Gemini feedback cần xử lý

- Correct:
- Inaccurate:
- Missing:
- Confusing concepts:
- Sections cần quay lại:

---

## Phase 3 — Problem / Motivation / Gap

### Bảng phân tách

| Mục | Diễn giải bằng lời của tôi | Evidence / citation |
|---|---|---|
| General problem |  |  |
| Why it matters |  |  |
| What prior work solves |  |  |
| What prior work fails to solve |  |  |
| Exact research gap |  |  |
| Hypothesis / intuition |  |  |
| Contribution addressing the gap |  |  |

### Prompt phân tích gap

```text
Analyze the problem formulation of this paper.

Separate clearly:

1. General research problem
2. Why the problem matters
3. What existing approaches already solve
4. What existing approaches still fail to solve
5. The exact research gap targeted by this paper
6. The paper's hypothesis or intuition
7. The proposed contribution that addresses the gap

For every statement, point me to the supporting section of the paper.

Do not merge "research gap" and "contribution".
```

### Câu hỏi tự kiểm tra

- [ ] Tôi có phân biệt được problem và motivation không?
- [ ] Tôi có phân biệt được gap và contribution không?
- [ ] Tôi có nói được hypothesis bằng lời của mình không?

---

## Phase 4 — Method / Architecture

### Tôi tự vẽ trước

```text
Input
->
->
->
Prediction
->
Loss
```

### Prompt complete data flow

```text
Explain the complete data flow of the proposed method.

Follow ONE training example from raw input to final loss.

For every step provide:

1. Input
2. Operation / module
3. Output
4. Representation or tensor involved, if stated
5. Relevant equation
6. Purpose of this step
7. Relevant paper section

Do not skip intermediate components.

At the end, provide a compact pipeline like:

Input
-> Module A
-> Representation
-> Module B
-> Prediction
-> Loss
```

### Component map

| Component | Input | Operation | Output | Purpose | Evidence |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

### Điều tôi vẫn chưa hiểu

- [ ]

---

## Phase 5 — Section Recall

Sau mỗi subsection: đọc, đóng paper, tự recall, rồi mới hỏi Gemini.

### Section template

### Section [X.X — Name]

### Input

-

### Process

-

### Output

-

### Purpose

-

### Why is this needed?

-

### Difference from previous methods

-

### What I still do not understand

- [ ]

### Prompt kiểm tra section

```text
I have read Section [SECTION].

Here is my current understanding:

[MY EXPLANATION]

Check it against the source.

Identify:

1. Correct understanding
2. Missing mechanisms
3. Incorrect causal relationships
4. Terms I am using incorrectly
5. Important details that affect how the method works
6. Which equations/figures I should revisit

Do not summarize the section unless necessary for a correction.
```

---

## Phase 6 — Equations

### Equation queue

| Eq. | Dùng để làm gì? | Biến chính | Behavior được khuyến khích | Evidence / ablation | Status |
|---:|---|---|---|---|---|
|  |  |  |  |  | todo |
|  |  |  |  |  | todo |
|  |  |  |  |  | todo |

### Prompt equation deep dive

```text
Explain Equation [NUMBER] at three levels.

LEVEL 1 — Intuition
Explain what the equation does without mathematics.

LEVEL 2 — Variables
Explain every symbol, variable, vector, matrix, tensor and hyperparameter.

For each variable tell me:
- where it comes from
- its role
- its shape/dimension if the paper states or implies it

LEVEL 3 — Mathematics
Explain the mathematical operation step by step.

Then answer:

1. Why is this equation needed?
2. What model behavior does it encourage?
3. What would likely happen if it were removed?
4. Which experiment or ablation tests its usefulness?
5. How does it connect to the equations immediately before/after it?

Use only information supported by the paper and explicitly state when an explanation is an inference.
```

---

## Phase 7 — Loss Functions

### Loss decomposition

```text
Total Loss
├── Loss A -> purpose
├── Loss B -> purpose
└── Loss C -> purpose
```

| Loss | Equation | Inputs | Trains component | Behavior | Weight | Ablation |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

### Prompt loss decomposition

```text
Decompose the complete training objective of this paper.

For every loss term provide:

- Name
- Equation
- Inputs
- What behavior it encourages
- Which component it trains
- Weight / hyperparameter
- Why the authors need it
- Whether an ablation validates it

Then explain how all loss terms interact during training.

Finally give me:

Total Loss
├── Loss A -> purpose
├── Loss B -> purpose
└── Loss C -> purpose
```

---

## Phase 8 — Experiments

### Experiment map

| Experiment | Research question | Dataset | Baselines | Metric | Table/Figure | Main result | Caveat |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |

### Protocol fingerprint

- Dataset and split:
- Scenario / label space:
- Backbone:
- Frozen/trainable components:
- Seeds / number of runs:
- Metric and averaging:
- Baseline implementation:
- External data / teacher / generated data:
- Memory budget:
- Evaluation after each task:
- Compute / hardware:

### Prompt experiment map

```text
Create an experiment map for this paper.

For every experiment identify:

1. Research question being tested
2. Dataset
3. Baselines
4. Metric
5. Table/Figure
6. Main result
7. What conclusion the authors draw

Do not merely summarize the numbers.

Explain WHY each experiment exists.
```

---

## Phase 9 — Claim → Evidence

| Claim | Where claim appears | Experiment | Evidence | My judgment | Caveat |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
|  |  |  |  |  |  |

### Prompt claim/evidence audit

```text
List the major claims made by the authors.

For every claim provide:

- Claim
- Where the claim is made
- Experiment supporting it
- Table / figure
- Metric
- Relevant baseline
- Observed evidence
- Whether the evidence strongly, partially, or weakly supports the claim
- Important caveats

Separate facts reported by the paper from your own inference.
```

---

## Phase 10 — Ablation Study

| Component | Intended purpose | With component | Without component | Difference | Conclusion justified | Not justified |
|---|---|---:|---:|---:|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

### Prompt ablation analysis

```text
Analyze every ablation study in this paper.

For each component provide:

Component
-> Intended purpose
-> Result with component
-> Result without component
-> Absolute difference
-> Relative importance
-> What conclusion is justified
-> What conclusion is NOT justified

Then answer:

1. Which component contributes the most?
2. Which contributes the least?
3. Are there interactions between components?
4. Does the ablation fully validate the proposed method?
5. What additional ablation would strengthen the paper?
```

---

## Phase 11 — Critical Reading

### Reviewer notes

- Strongest contribution:
- Weakest part:
- Main assumption:
- Alternative explanation:
- Missing experiment:
- Generalization risk:
- Reproducibility risk:

### Prompt reviewer mode

```text
Act as a critical peer reviewer.

Evaluate this paper on:

1. Problem importance
2. Novelty
3. Soundness of the method
4. Assumptions
5. Experimental design
6. Choice of baselines
7. Evaluation metrics
8. Ablation quality
9. Reproducibility
10. Limitations
11. Generalizability

For every criticism:
- cite supporting evidence from the paper
- distinguish explicit limitations from your inferred limitations

Then provide:

Strongest contribution:
...

Weakest part:
...

One experiment that would make the paper substantially stronger:
...
```

---

## Phase 12 — Reproduction Check

| Item | Status | Detail | Missing detail / risk |
|---|---|---|---|
| Dataset and split |  |  |  |
| Preprocessing |  |  |  |
| Input representation |  |  |  |
| Model / backbone |  |  |  |
| Training procedure |  |  |  |
| Sampling procedure |  |  |  |
| Memory / replay strategy |  |  |  |
| Loss functions |  |  |  |
| Optimizer |  |  |  |
| Learning rate |  |  |  |
| Batch size |  |  |  |
| Epochs |  |  |  |
| Hyperparameters |  |  |  |
| Random seeds |  |  |  |
| Evaluation protocol |  |  |  |
| Inference procedure |  |  |  |

### Prompt reproduction checklist

```text
Assume I want to reproduce this paper.

Extract everything required for implementation:

1. Dataset and split
2. Preprocessing
3. Input representation
4. Model / backbone
5. Architecture
6. Training procedure
7. Sampling procedure
8. Memory / replay strategy if any
9. Loss functions
10. Optimizer
11. Learning rate
12. Batch size
13. Number of epochs
14. Hyperparameters
15. Random seeds
16. Evaluation protocol
17. Inference procedure

For every item classify it as:

- Clearly specified
- Partially specified
- Missing

Tell me which missing details would make reproduction difficult.
```

---

## Phase 13 — Completeness / Oral Exam

### Completion criteria

- [ ] Giải thích research problem không nhìn paper
- [ ] Phân biệt motivation và research gap
- [ ] Nói contribution bằng lời của mình
- [ ] Vẽ toàn bộ architecture
- [ ] Theo một sample từ input đến loss
- [ ] Giải thích các equation quan trọng
- [ ] Giải thích vai trò từng loss
- [ ] Biết dataset và evaluation protocol
- [ ] Biết baseline chính
- [ ] Đọc và giải thích main result table
- [ ] Nói ablation chứng minh điều gì
- [ ] Nối từng major claim với evidence
- [ ] Chỉ ra ít nhất một assumption
- [ ] Chỉ ra limitations
- [ ] Biết phần nào khó reproduce
- [ ] So sánh paper với ít nhất một related method
- [ ] Nói được paper liên quan gì đến research của mình
- [ ] Trả lời oral exam mà không phụ thuộc AI summary

### Prompt oral exam

```text
Act as my PhD advisor.

Quiz me on this paper one question at a time.

Progress through:

LEVEL 1
- Problem
- Motivation
- Research gap
- Contributions

LEVEL 2
- Architecture
- Main components
- Training process

LEVEL 3
- Equations
- Loss functions
- Experiments
- Ablation

LEVEL 4
- Assumptions
- Limitations
- Failure cases
- Comparison with alternatives

LEVEL 5
- Ask me to propose improvements
- Ask me to transfer the idea to another setting
- Ask me to defend or criticize the paper

Rules:

1. Ask ONE question.
2. Wait for my answer.
3. Evaluate my answer against the paper.
4. Tell me what is correct, incomplete, or incorrect.
5. Point me to relevant source citations.
6. Increase difficulty gradually.
7. Do not reveal the ideal answer before I attempt it.
```

---

## Final Paper Note Handoff

Chỉ chuyển sang paper note chính những ý đã được kiểm tra lại bằng paper citation.

### Ý cần chuyển sang paper note

- [ ] Tóm tắt một câu:
- [ ] Problem:
- [ ] Gap:
- [ ] Method overview:
- [ ] Important equations:
- [ ] Protocol fingerprint:
- [ ] Main results:
- [ ] Ablation:
- [ ] Limitations:
- [ ] Critical judgment:
- [ ] Concepts cần tạo/cập nhật:

### Prompt audit paper note cuối

```text
Here is my final note for this paper:

[PASTE NOTE]

Audit it against the source.

Do NOT rewrite the note.

Return only:

## Missing
Important information from the paper that my note omitted.

## Incorrect
Statements in my note that conflict with the paper.

## Ambiguous
Statements that are too vague or could be misunderstood.

## Overstated
Claims stronger than what the experiments support.

## Recommended revisit
Sections, figures, tables or equations I should reread.

Rank findings by importance:
Critical / Important / Optional.
```

## Liên kết

- Paper note:
- PDF:
- Concepts:
- Related papers:
