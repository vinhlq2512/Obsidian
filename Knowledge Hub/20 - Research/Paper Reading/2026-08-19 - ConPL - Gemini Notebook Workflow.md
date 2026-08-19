---
type: paper-reading
date: 2026-08-19
status: draft
workflow: gemini-notebook
template: "[[Paper Reading Gemini Notebook Workflow]]"
paper: "[[Consistent Prototype Learning for Few-Shot Continual Relation Extraction]]"
pdf: "[[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf]]"
paper_note: "[[Consistent Prototype Learning for Few-Shot Continual Relation Extraction]]"
notebook_url:
target_minutes: 90
actual_minutes:
reading_goal: "Hiểu ConPL theo workflow Gemini Notebook: problem/gap, method ba stage, losses, protocol NK-CRE, claim-evidence, ablation và reproducibility."
current_phase: scaffolded
completed: false
need_review: true
review_date:
created_at: 2026-08-19
updated_at: 2026-08-19
tags:
  - paper-reading
  - gemini-notebook
  - relation-extraction
  - continual-learning
  - few-shot-learning
---

# 2026-08-19 - ConPL - Gemini Notebook Workflow

> [!note] Ranh giới
> Đây là working note đã được scaffold từ paper note/PDF để hỗ trợ đọc với Gemini Notebook. Các phần “mình tự trả lời”, “closed-book recall”, “oral exam” vẫn để trống vì chưa có câu trả lời cá nhân của bạn; không coi note này là bằng chứng đã đọc xong paper.

## Setup

- Paper: [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction]]
- PDF: [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf]]
- Paper note chính: [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction]]
- Gemini Notebook / NotebookLM URL:
- Mục tiêu buổi đọc: hiểu vì sao ConPL cần cả sample memory và prototype memory, cách ba stage huấn luyện vận hành, và ablation chứng minh gì.
- Phần cần đọc trước: Introduction, Section 3, Section 4, Table 1-3, limitations.
- PDF count đã kiểm tra: 14 trang.

## Phase 1 — Paper Map

### Prompt gửi Gemini

```text
Do not summarize the paper in detail yet. Create a structural map of this paper and identify problem, motivation, gap, contributions, pipeline, components, losses, datasets, baselines, metrics, main experiments, ablations, and limitations. For every item, point to the relevant section, figure, table, or equation. The purpose is to tell me WHERE to read, not to replace my reading.
```

### Paper map — scaffold từ nguồn

- **Problem:** Few-shot continual relation extraction: model học relation mới theo chuỗi task nhưng vẫn phải phân loại đúng tất cả relation đã thấy. Đọc Introduction và Section 3. [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=1|PDF tr. 1]], [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=3|PDF tr. 3]]
- **Motivation:** replay ít exemplar có thể không giữ representation/prototype cũ ổn định; relation gần nghĩa như `father`/`mother` dễ bị confusion. [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=1|PDF tr. 1]]
- **Gap:** protocol CFRL trước đó không strict few-shot cho task đầu; các phương pháp memory trước đó chưa giải quyết đủ prototype distortion và confusing classes. [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=2|PDF tr. 2]]
- **Main idea:** lưu cả sample memory và prototype memory; dùng prototype classifier, consistency losses và confusing-class classification.
- **Main contributions:** NK-CRE setting, ConPL architecture, multi-information memory, ba-stage training, evaluation trên FewRel/TACRED.
- **Important figure:** Figure 1 về prototype distortion/forgetting; Figure 2 về distribution của class gần nhau.
- **Important equations:** Eq. 1 prompt encoder; Eq. 2 prototype; Eq. 3 classifier; Eq. 5 $L_{cc}$; Eq. 7 $L_{fc}$; Eq. 8 $L_{dc}$; Eq. 9-10 objectives. [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=4|PDF tr. 4]], [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=5|PDF tr. 5]]
- **Main result table:** Table 1 accuracy theo task. [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=7|PDF tr. 7]]
- **Ablation table:** Table 2 component ablation; Figure 4 consistency loss analysis. [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=8|PDF tr. 8]], [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=9|PDF tr. 9]]
- **Limitations:** storage overhead của prototype memory, outlier distortion-forgetting chưa phân tích, domain adaptability để future work. [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=10|PDF tr. 10]]

### Chỗ cần đọc trước

- [ ] Abstract + Introduction
- [ ] Section 3 NK-CRE
- [ ] Section 4.1-4.4 method và Algorithm 1
- [ ] Table 1-3
- [ ] Limitations + Appendix prototype distortion

## Phase 2 — Pass 1 Recall

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

Compare my understanding against the paper. Return what is correct, inaccurate, missing, confusing, and which sections/citations I should revisit. Do not rewrite the entire paper for me.
```

## Phase 3 — Problem / Motivation / Gap

| Mục | Diễn giải bằng lời của tôi | Evidence / citation |
|---|---|---|
| General problem | Continual relation extraction yêu cầu học relation mới tuần tự và vẫn phân loại được relation cũ. | [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=1\|PDF tr. 1]] |
| Why it matters | Relation mới xuất hiện liên tục, nhãn ít, và relation gần nghĩa dễ gây nhầm lẫn sau khi model update. | [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=1\|PDF tr. 1]] |
| What prior work solves | Replay/prototype/prompt/data augmentation giúp giảm forgetting ở CFRE/CRE. | [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=2\|PDF tr. 2]] |
| What prior work fails to solve | Một số protocol không few-shot đồng đều; memory exemplar ít không đủ giữ class geometry; confusing classes chưa được nhấn mạnh đủ. | [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=2\|PDF tr. 2]] |
| Exact research gap | Strict N-way K-shot cho mọi task và giảm forgetting/prototype distortion trong điều kiện memory cực nhỏ. | [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=3\|PDF tr. 3]] |
| Hypothesis / intuition | Giữ prototype ổn định và ép phân biệt confusing negatives sẽ giảm catastrophic forgetting. | [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=4\|PDF tr. 4]] |
| Contribution addressing the gap | ConPL kết hợp prototype memory, sample memory, $L_{cc}$, $L_{dc}$ và $L_{fc}$ trong training ba stage. | [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=5\|PDF tr. 5]] |

### Câu hỏi tự kiểm tra

- [ ] NK-CRE khác CFRL ở task đầu như thế nào?
- [ ] Vì sao một exemplar/relation chưa đủ để giữ representation cũ?
- [ ] Vì sao confusing negatives quan trọng trong relation extraction?

## Phase 4 — Method / Architecture

### Tôi tự vẽ trước

```text
Sentence + head/tail entity
-> discrete prompt với [MASK]
-> BERTBASE
-> [MASK] relation embedding
-> temporary prototypes cho relation mới
-> merge với prototype memory cũ
-> prototype classifier + confusing prototype set
-> Stage 1 train task mới + memory cũ
-> Stage 2 chọn exemplar gần center và refine memory mới
-> Stage 3 memory-only consolidation
-> classify trong toàn bộ relation đã thấy
```

### Component map

| Component | Input | Operation | Output | Purpose | Evidence |
|---|---|---|---|---|---|
| Prompt encoder | sentence, head, tail | `[CLS], head, [MASK], tail, [SEP], sentence, [SEP]` vào BERT | relation embedding tại `[MASK]` | khai thác PLM cho RE | [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=4\|PDF tr. 4]] |
| Prototype classifier | embedding + prototypes | cosine-softmax | relation probability | classify bằng class anchors | [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=4\|PDF tr. 4]] |
| Confusing class selection | sample embedding + prototype set | chọn nearest negative và negatives trong margin $\alpha$ | $P_i^{sim}$ | tập trung vào class dễ nhầm | [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=5\|PDF tr. 5]] |
| Sample memory | selected exemplar | lưu một sample/relation | replay data | nhắc model bằng input thật | [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=5\|PDF tr. 5]] |
| Prototype memory | selected feature/prototype | lưu một vector/relation | class anchor | giữ geometry cũ | [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=5\|PDF tr. 5]] |
| Consistent learning | memory samples + prototypes | $L_{cc}$ và $L_{dc}$ | regularized embedding geometry | cân bằng old/new và giữ relative similarity | [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=5\|PDF tr. 5]] |

### Điều tôi vẫn chưa hiểu

- [ ] $P^k$, $\hat P^k$, $\bar P^k$, $\tilde P^k$ khác nhau chính xác ở mỗi stage ra sao?
- [ ] Code có triển khai Eq. 7 đúng như paper hay có focal modulation không?

## Phase 5 — Section Recall

### Section 4.1 — Prototype-based classification

- **Input:** current task samples, old sample memory, old prototype memory.
- **Process:** tạo prompt, encode `[MASK]`, tính temporary prototype, phân loại bằng cosine-softmax, thêm $L_{cc}$ và $L_{fc}$.
- **Output:** updated encoder parameters và temporary/current prototype representations.
- **Purpose:** học relation mới trong khi vẫn giữ activation của relation cũ qua memory/prototype.
- **Still unclear:** vì sao paper gọi Eq. 7 là focal loss dù công thức giống restricted cross-entropy?

### Section 4.2-4.3 — Memory-enhanced + Consistent learning

- **Input:** selected key samples, sample memory, prototype memory.
- **Process:** chọn exemplar gần prototype nhất; lưu sample + prototype; chạy memory-only consolidation với $L_{dc}$.
- **Output:** memory cân bằng cho tất cả relation đã thấy và prototype geometry ổn định hơn.
- **Purpose:** giảm lệch old/new relation và hạn chế prototype distortion.

## Phase 6 — Equations

| Eq. | Dùng để làm gì? | Biến chính | Behavior được khuyến khích | Evidence / ablation | Status |
|---:|---|---|---|---|---|
| 1 | Encode prompt thành relation representation | $f_\theta(x_{input})$, `[MASK]` | dùng PLM cho relation embedding | [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=4\|PDF tr. 4]] | todo |
| 2 | Tính prototype class mới | $D_j^k$, $p_j$ | gom K-shot samples thành class anchor | [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=4\|PDF tr. 4]] | todo |
| 3-4 | Prototype classifier + CE | $f_\theta(x_i)$, $p_l$, $\hat R^k$ | phân loại theo similarity tới prototypes | [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=4\|PDF tr. 4]] | todo |
| 5 | Classification consistency | memory sample, prototype đúng | kéo old sample embedding về đúng anchor | ablation Table 2/Figure 4 | todo |
| 7 | Confusing-class loss | $P_i^{sim}$, $\alpha$ | ép phân biệt positive với hard/confusing negatives | bỏ $L_{fc}$ giảm 10.66 tại T8 | todo |
| 8 | Distribution consistency | vector similarity tới $\hat P^k$ | giữ relative class geometry | Figure 4 tăng 2.0 khi dùng sample memory | todo |
| 9-10 | Objective theo stage | $\lambda_{ce},\lambda_{cc},\lambda_{fc},\lambda_{dc}$ | Stage 3 thêm $L_{dc}$ trên memory | [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=5\|PDF tr. 5]] | todo |

## Phase 7 — Loss Functions

```text
Total training
├── L_ce -> classify current/memory samples by prototype similarity
├── L_cc -> keep memory sample close to its stored prototype
├── L_fc -> focus on confusing negative prototypes
└── L_dc -> preserve relative similarity distribution in memory-only consolidation
```

| Loss | Equation | Inputs | Trains component | Behavior | Weight | Ablation |
|---|---|---|---|---|---|---|
| $L_{ce}$ | Eq. 4 | current task + sample memory | encoder/classifier via prototypes | correct relation classification | $\lambda_{ce}=1$ | core loss, not individually removed |
| $L_{cc}$ | Eq. 5 | old/current memory samples + prototypes | encoder | sample-prototype consistency | $\lambda_{cc}=1$ | small individual gain; larger when classifier uses sample memory |
| $L_{fc}$ | Eq. 7 | restricted confusing prototype set | encoder/classifier | hard-negative discrimination | $\lambda_{fc}=1$ | strongest: -10.66 when removed |
| $L_{dc}$ | Eq. 8 | memory samples + prototype memory | encoder | relative distribution consistency | $\lambda_{dc}=1$ | small individual gain; +2.0 in Figure 4 variant |

## Phase 8 — Experiments

| Experiment | Research question | Dataset | Baselines | Metric | Table/Figure | Main result | Caveat |
|---|---|---|---|---|---|---|---|
| Main NK-CRE accuracy | ConPL có tốt hơn continual baselines trong strict few-shot không? | FewRel/TACRED | EMAR, RP-CRE, ERDA, PT variants | whole accuracy after each task | Table 1 | ConPL dẫn đầu đa số T2-T8 và toàn bộ TACRED | các baseline không † có budget task đầu khác |
| Ablation components | Thành phần nào đóng góp? | FewRel 10-way 5-shot | ConPL variants | T8 accuracy | Table 2 | bỏ $L_{fc}$ giảm mạnh nhất; bỏ PM giảm 3.56 | chỉ một setting chính |
| Consistency loss importance | $L_{cc}$/$L_{dc}$ còn hữu ích khi không dùng prototype memory cho logits? | FewRel 10-way 5-shot | variants dùng sample memory | accuracy curve | Figure 4 | $L_{dc}$ tăng 2.0, $L_{cc}$ tăng 0.73 | hyperparameter retuned |
| Forgetting | ConPL giảm forgetting đến đâu? | FewRel 10-way 5-shot | SeqRun, JointTrain, baselines | mean forgetting | Table 3 | ConPL 3.31 gần JointTrain 3.29 | JointTrain dùng toàn bộ dữ liệu cũ |
| Distortion-forgetting | Prototype distortion có liên hệ forgetting không? | FewRel analysis, 50 task sequences | scatter analysis | distortion vs forgetting | Appendix/Figure | xu hướng distortion cao đi cùng forgetting cao | không báo correlation coefficient |

### Protocol fingerprint

- Dataset and split: FewRel 80 public relations, 8 tasks x 10 relations; TACRED bỏ `n/a`, còn 41 relations.
- Scenario / label space: N-way K-shot continual relation extraction, evaluation trên tất cả relation đã thấy.
- Backbone: BERTBASE với discrete prompt.
- Seeds / number of runs: main experiments dùng 6 random task sequences; distortion analysis dùng 50 task sequences.
- Metric and averaging: accuracy sau từng task; forgetting metric theo Chaudhry et al.
- Baseline implementation: PT variants và ConPL dùng cùng seeds/task sequences; một số baseline legacy lấy từ CFRL.
- External data: ERDA(PT) dùng Wikipedia augmentation; ConPL không dùng LLM augmentation.
- Memory budget: một raw sample và một prototype vector mỗi relation.
- Evaluation after each task: yes, T1-T8.

## Phase 9 — Claim → Evidence

| Claim | Where claim appears | Experiment | Evidence | My judgment | Caveat |
|---|---|---|---|---|---|
| ConPL cải thiện NK-CRE accuracy. | Abstract/Results | Table 1 | FewRel 10-way 5-shot T8: ConPL 85.77 vs EMAR(PT) 81.34; TACRED 5-shot T8: 76.38 vs 68.67. [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=7\|PDF tr. 7]] | Strong reported evidence | chưa reproduced local |
| Prototype memory hữu ích. | Method/Ablation | Table 2 | bỏ Prototype Memory giảm 85.77 -> 82.21. [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=8\|PDF tr. 8]] | Supported | chỉ FewRel 10-way 5-shot |
| $L_{fc}$ là thành phần mạnh nhất. | Ablation | Table 2 | bỏ $L_{fc}$ giảm 85.77 -> 75.11. [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=8\|PDF tr. 8]] | Strong | tên "focal loss" cần kiểm code/công thức |
| ConPL giảm forgetting gần JointTrain. | Forgetting analysis | Table 3 | mean forgetting ConPL 3.31, JointTrain 3.29. [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=9\|PDF tr. 9]] | Interesting | JointTrain có full old data |
| Prototype distortion liên hệ forgetting. | Appendix analysis | distortion scatter | paper quan sát xu hướng qua 50 task sequences. [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf#page=11\|PDF tr. 11]] | Partial | không causal/correlation coefficient |

## Phase 10 — Ablation Study

| Component | Intended purpose | With component | Without component | Difference | Conclusion justified | Not justified |
|---|---|---:|---:|---:|---|---|
| Prototype Memory | giữ class anchors cũ | 85.77 | 82.21 | -3.56 | PM có ích rõ trong FewRel 5-shot | PM luôn đủ cho class đa mode |
| Consistent Learning Module | memory-only consolidation | 85.77 | 84.25 | -1.52 | consolidation có ích | chứng minh mọi consistency term đều quan trọng ngang nhau |
| $L_{cc}$ | sample-prototype consistency | 85.77 | 85.69 | -0.08 | đóng góp nhỏ khi dùng PM logits | loss này vô dụng nói chung |
| $L_{dc}$ | relative distribution consistency | 85.77 | 85.40 | -0.37 | đóng góp nhỏ trong setting chính | không cần trong setting khác |
| $L_{fc}$ | confusing-class discrimination | 85.77 | 75.11 | -10.66 | thành phần quan trọng nhất theo ablation | focal loss chuẩn được validate |

## Phase 11 — Critical Reading

- Strongest contribution: strict NK-CRE framing + prototype/sample memory với ablation rõ thành phần $L_{fc}$.
- Weakest part: Eq. 7 naming và thiếu phân tích sâu vì sao prototype outliers không theo distortion-forgetting trend.
- Main assumption: task boundary và relation set mới được biết; được phép lưu raw exemplar.
- Alternative explanation: gains có thể đến nhiều từ prompt + hard-negative discrimination hơn là consistency losses riêng lẻ.
- Missing experiment: sensitivity cho $\alpha$, memory size, nhiều prototypes/class, macro-F1/calibration.
- Generalization risk: chỉ BERTBASE, FewRel/TACRED, English relation extraction.
- Reproducibility risk: chi tiết compute/GPU hours không rõ, code cần kiểm Eq. 7.

## Phase 12 — Reproduction Check

| Item | Status | Detail | Missing detail / risk |
|---|---|---|---|
| Dataset and split | Partially specified | FewRel/TACRED task setup, public FewRel 80 relations | exact task order files/seeds cần code |
| Preprocessing | Partially specified | discrete prompt with entities | entity markers/tokenization details cần code |
| Input representation | Clearly specified | `[CLS], head, [MASK], tail, [SEP], sentence, [SEP]` |  |
| Model / backbone | Clearly specified | BERTBASE | checkpoint variant cần code |
| Training procedure | Clearly specified | 3 stages, epochs 1/1/3 | batching details |
| Sampling procedure | Clearly specified | exemplar gần prototype nhất | tie cases/multi-mode not discussed |
| Memory / replay strategy | Clearly specified | one sample + one prototype per relation | byte budget not reported |
| Loss functions | Partially specified | Eq. 4/5/7/8/9/10 | Eq. 7 naming/code mismatch risk |
| Optimizer | Clearly specified | Adam |  |
| Learning rate | Clearly specified | $2e^{-5}$ | schedule unclear |
| Batch size | Missing | not in note/PDF scaffold | reproduction risk |
| Epochs | Clearly specified | 1, 1, 3 |  |
| Hyperparameters | Partially specified | $\alpha=0.1$, lambdas=1, clipping=10 | sensitivity absent |
| Random seeds | Partially specified | 6 sequences; same seeds for reruns | exact seed values need code |
| Evaluation protocol | Clearly specified | cumulative test set after each task |  |
| Inference procedure | Partially specified | prototype classifier over known relations | task identity assumptions should be checked |

## Phase 13 — Completeness / Oral Exam

- [ ] Giải thích NK-CRE không nhìn paper.
- [ ] Phân biệt CFRL vs NK-CRE ở task đầu.
- [ ] Vẽ ba stage ConPL.
- [ ] Giải thích $L_{cc}$ vs $L_{dc}$.
- [ ] Giải thích vì sao $L_{fc}$ có impact lớn nhất.
- [ ] Đọc Table 1-3 và nêu caveat.
- [ ] Nêu ít nhất 3 limitation/assumption.
- [ ] So sánh ConPL với CPL/WAVE++ ở mức protocol, không chỉ headline.

### Prompt oral exam

```text
Act as my PhD advisor. Quiz me on ConPL one question at a time. Start from NK-CRE problem/gap, then method stages, equations/losses, experiments/ablation, assumptions/limitations, and finally ask me to propose improvements. Do not reveal the ideal answer before I attempt it.
```

## Final Paper Note Handoff

Chỉ chuyển sang paper note chính những ý đã tự kiểm tra lại bằng PDF citation.

### Ý cần chuyển sang paper note

- [ ] Problem/gap: strict NK-CRE và task đầu few-shot.
- [ ] Method overview: prompt encoder + prototype classifier + dual memory + 3 stages.
- [ ] Important equations: Eq. 2/3/5/7/8/9/10.
- [ ] Protocol fingerprint: FewRel/TACRED, 6 sequences, memory one exemplar + one vector.
- [ ] Main results: Table 1 T8 và Appendix mean/std.
- [ ] Ablation: $L_{fc}$ strongest, PM meaningful, consistency smaller under PM logits.
- [ ] Limitations: rehearsal-based, task boundary, no macro-F1/calibration, no sensitivity.
- [ ] Concepts: [[Prototype Learning]], [[Embedding Space Regularization]], [[Replay in Continual Learning]], [[Continual Few-Shot Relation Extraction]].

## Liên kết

- Paper note: [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction]]
- PDF: [[Consistent Prototype Learning for Few-Shot Continual Relation Extraction.pdf]]
- Related reading log: [[2026-08-16 - Consistent Prototype Learning for Few-Shot Continual Relation Extraction]]
- Concepts: [[Prototype Learning]], [[Embedding Space Regularization]], [[Replay in Continual Learning]], [[Continual Few-Shot Relation Extraction]]
