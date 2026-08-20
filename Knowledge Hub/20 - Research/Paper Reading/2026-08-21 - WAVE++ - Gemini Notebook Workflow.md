---
type: paper-reading
date: 2026-08-21
status: draft
workflow: gemini-notebook
template: "[[Paper Reading Gemini Notebook Workflow]]"
paper: "[[WAVE++ - Capturing Within-Task Variance for Continual Relation Extraction]]"
pdf: "[[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf]]"
paper_note: "[[WAVE++ - Capturing Within-Task Variance for Continual Relation Extraction]]"
notebook_url:
target_minutes: 90
actual_minutes:
reading_goal: "Hiểu WAVE++ như bản mở rộng của WAVE-CRE: prompt pool, label descriptions, cascade voting, latent replay, significance/appendix và protocol caveats."
current_phase: scaffolded
completed: false
need_review: true
review_date:
created_at: 2026-08-21
updated_at: 2026-08-21
tags:
  - paper-reading
  - gemini-notebook
  - relation-extraction
  - continual-learning
---

# 2026-08-21 - WAVE++ - Gemini Notebook Workflow

> [!note] Ranh giới
> Đây là working note scaffold từ paper note/PDF để hỗ trợ đọc với Gemini Notebook. Các phần “closed-book recall”, “mình tự trả lời”, “oral exam” vẫn để trống vì chưa có câu trả lời cá nhân của bạn; không coi note này là bằng chứng đã đọc xong paper.

## Setup

- Paper: [[WAVE++ - Capturing Within-Task Variance for Continual Relation Extraction]]
- PDF: [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf]]
- Paper note chính: [[WAVE++ - Capturing Within-Task Variance for Continual Relation Extraction]]
- Gemini Notebook / NotebookLM URL:
- Mục tiêu buổi đọc: tách rõ WAVE++ thêm gì so với WAVE-CRE, mỗi component được chứng minh bằng result/ablation nào.
- Phần cần đọc trước: Introduction, Method, Main Results, Ablation, Appendix label descriptions/significance/time.
- PDF count đã kiểm tra: 30 trang.

## Phase 1 - Paper Map

### Prompt gửi Gemini

```text
Do not summarize the paper in detail yet. Create a structural map of this paper and identify problem, motivation, gap, contributions, pipeline, components, losses, datasets, baselines, metrics, main experiments, ablations, appendix analyses, and limitations. For every item, point to the relevant section, figure, table, or equation. The purpose is to tell me WHERE to read, not to replace my reading.
```

### Paper map - scaffold từ nguồn

- **Problem:** continual relation extraction cần học nhiều task liên tiếp và giữ performance trên relation cũ. [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=4|PDF tr. 4]]
- **Motivation:** WAVE-CRE nêu within-task variance; WAVE++ thêm label semantics và cascade voting để cải thiện task/relation inference.
- **Gap:** prompt pool đơn thuần chưa tận dụng đủ label descriptions và task prediction vẫn là nguồn lỗi.
- **Main idea:** kết hợp prompt pool, label-description alignment, cascade voting và latent generative replay.
- **Main contributions:** adaptive prompt pool, label description contrastive alignment, cascade voting, stronger experiments/appendix.
- **Important figure/equations:** formalization và method ở đầu phần method. [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=4|PDF tr. 4]], [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=5|PDF tr. 5]]
- **Main result table:** final-stage results. [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=16|PDF tr. 16]]
- **Ablation table:** prompt pool, label descriptions, generative replay. [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=18|PDF tr. 18]]
- **Appendix cần đọc:** label descriptions, statistical tests, task prediction, running time. [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=27|PDF tr. 27]], [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=30|PDF tr. 30]]

### Chỗ cần đọc trước

- [ ] Abstract + Introduction
- [ ] Problem formalization
- [ ] Prompt pool
- [ ] Label-description alignment
- [ ] Cascade voting
- [ ] Generative replay
- [ ] Table main results
- [ ] Ablation + appendix

## Phase 2 - Pass 1 Recall

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

## Phase 3 - Problem / Motivation / Gap

| Mục | Diễn giải bằng lời của tôi | Evidence / citation |
|---|---|---|
| General problem | CRE là class-incremental RE, nơi label space mở rộng theo task và model phải phân loại trên labels đã thấy. | [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=4\|PDF tr. 4]] |
| Why it matters | Dữ liệu quan hệ cũ khó giữ đầy đủ, còn relation mới xuất hiện liên tục. | [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=2\|PDF tr. 2]] |
| What prior work solves | WAVE-CRE dùng prompt pools và latent replay để bắt within-task variance và giảm forgetting. | [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=16\|PDF tr. 16]] |
| What prior work fails to solve | Task prediction và label semantics vẫn có thể làm relation gần nghĩa bị nhầm. | inferred |
| Exact research gap | Cần khai thác label descriptions và cascade decision để chọn task/relation ổn định hơn. | [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=5\|PDF tr. 5]] |
| Hypothesis / intuition | Label anchors giúp representation của input có điểm neo ngữ nghĩa; cascade voting giảm lỗi chọn task. | inferred |
| Contribution addressing the gap | WAVE++ thêm label-description alignment và cascade voting lên nền WAVE-CRE. | [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=5\|PDF tr. 5]] |

### Câu hỏi tự kiểm tra

- [ ] WAVE++ thêm gì không có trong WAVE-CRE?
- [ ] Label description giúp relation classifier hay task predictor?
- [ ] Cascade voting có đổi inference assumption không?

## Phase 4 - Method / Architecture

### Tôi tự vẽ trước

```text
Sentence + entity pair
-> PLM + task-specific prompt pool
-> input representation
-> label description representation
-> contrastive/alignment objective
-> cascade voting for task/relation candidate
-> relation classifier over seen relations
-> latent generative replay for old relation features
```

### Component map

| Component | Input | Operation | Output | Purpose | Evidence |
|---|---|---|---|---|---|
| Prompt pool | input + task/prompt keys | route input to prompt experts | prompted representation | capture within-task variance | [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=5\|PDF tr. 5]] |
| Label descriptions | relation label text/descriptions | encode label semantics | label anchors | align input with relation meaning | [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=7\|PDF tr. 7]] |
| Contrastive alignment | input/label representations | pull positives, push negatives | aligned embedding space | reduce semantic confusion | [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=7\|PDF tr. 7]] |
| Cascade voting | candidate task/relation scores | staged voting | task/relation decision | improve task identity inference | [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=9\|PDF tr. 9]] |
| Generative replay | old latent distributions | sample old features | replay data | retain old relations | [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=11\|PDF tr. 11]] |

### Điều tôi vẫn chưa hiểu

- [ ] Label descriptions được viết thủ công, lấy từ dataset, hay generated?
- [ ] Cascade voting có thử mọi task/pool không, hay dùng shortlist?
- [ ] Generative replay và label alignment tương tác thế nào trong loss tổng?

## Phase 5 - Section Recall

### Prompt pool + label descriptions

- **Input:** sentence/entity pair và relation label descriptions.
- **Process:** prompt pool encode input; label encoder tạo anchors; alignment kéo input đúng về label đúng.
- **Output:** representation có cả signal context và label semantics.
- **Purpose:** giảm nhầm relation gần nghĩa và làm prompt selection có ngữ nghĩa hơn.
- **Still unclear:** chất lượng label description ảnh hưởng bao nhiêu.

### Cascade voting + replay

- **Input:** scores từ nhiều prompt/task candidates và old latent samples.
- **Process:** cascade voting chọn task/relation; replay giữ classifier không trôi về task mới.
- **Output:** prediction trên relation đã thấy.
- **Purpose:** giảm task identity error và catastrophic forgetting.
- **Still unclear:** trade-off latency so với WAVE-CRE.

## Phase 6 - Equations

| Eq/block | Dùng để làm gì? | Biến chính | Behavior được khuyến khích | Evidence / ablation | Status |
|---|---|---|---|---|---|
| CRE formalization | định nghĩa stream/task/relations | tasks, relations, examples | evaluate trên labels đã thấy | [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=4\|PDF tr. 4]] | todo |
| Prompt pool scoring | chọn prompt experts | input query, expert keys | input-specific adaptation | prompt pool ablation | todo |
| Label alignment loss | align input với label text | input embedding, label embedding | semantic separation | label-description ablation | todo |
| Cascade voting | task/relation decision | candidate scores | robust task inference | task prediction analysis | todo |
| Replay objective | retain old classes | latent old samples | reduce forgetting | replay ablation | todo |

## Phase 7 - Loss Functions

```text
WAVE++ training signal
├── current-task relation classification
├── prompt pool routing / adaptive prompting
├── label-description alignment
├── latent generative replay
└── task/relation decision via cascade voting
```

| Loss/block | Inputs | Trains component | Behavior | Weight | Ablation |
|---|---|---|---|---|---|
| Relation classification | current examples | encoder/classifier | classify new relations | cần đọc lại | main result |
| Label-description contrastive/alignment | input + label descriptions | representation/label anchors | reduce semantic confusion | cần đọc lại | label description ablation |
| Replay loss | generated old latent samples | classifier/shared space | retain old relations | cần đọc lại | replay ablation |
| Cascade voting objective/score | task/relation candidates | task predictor/voting | improve task identity | cần đọc lại | task prediction analysis |

## Phase 8 - Experiments

| Experiment | Research question | Dataset | Baselines | Metric | Table/Figure | Main result | Caveat |
|---|---|---|---|---|---|---|---|
| Main results | WAVE++ có hơn WAVE-CRE/SOTA không? | FewRel/TACRED | WAVE-CRE, EoE, rehearsal baselines | final-stage accuracy | main table | paper note ghi FewRel T10 87.7, TACRED T10 82.5 | protocol-specific |
| Ablation | component nào đóng góp? | FewRel/TACRED | WAVE++ variants | accuracy drop | ablation table | replay drop lớn nhất theo note hiện có | cần điền full numbers |
| Task prediction | cascade voting có tốt hơn WAVE-CRE predictor không? | FewRel/TACRED | WAVE-CRE | task prediction accuracy | analysis | paper note ghi WAVE++ hơn WAVE-CRE ở T10 | latency tăng |
| Label description appendix | label wording/semantics có ảnh hưởng không? | FewRel/TACRED | description variants | accuracy | appendix | cần đọc lại | description quality sensitive |
| Running time | cost tăng bao nhiêu? | FewRel/TACRED | WAVE-CRE vs WAVE++ | ms/sample hoặc time | appendix | inference latency tăng | trade-off deployment |

### Protocol fingerprint

- Dataset and split: FewRel và TACRED, chi tiết appendix. [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=30|PDF tr. 30]]
- Scenario / label space: continual relation extraction, evaluate sau mỗi learning stage.
- Backbone: PLM với prefix/prompt style; cần đọc implementation chi tiết.
- Seeds / number of runs: cần kiểm từ experiment section.
- Metric and averaging: final-stage accuracy và stage-wise accuracy.
- Replay/memory: latent generative replay.
- Task identity at inference: cascade voting/prediction, không nên giả định task oracle.
- Inference cost: appendix có running time. [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=30|PDF tr. 30]]

## Phase 9 - Claim to Evidence

| Claim | Where claim appears | Experiment | Evidence | My judgment | Caveat |
|---|---|---|---|---|---|
| WAVE++ mở rộng WAVE-CRE bằng label descriptions/cascade voting. | Method | architecture | [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=5\|PDF tr. 5]] | supported | cần tách inherited/new components |
| Main results tốt hơn WAVE-CRE ở stage cuối. | Results | main table | [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=16\|PDF tr. 16]] | observed | chưa reproduced |
| Generative replay là component mạnh. | Ablation | component removal | [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=18\|PDF tr. 18]] | strong within framework | không chứng minh Gaussian replay là tối ưu |
| Task prediction cải thiện so với WAVE-CRE. | Analysis | task prediction | [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=19\|PDF tr. 19]] | important | latency/cost tăng |
| Appendix kiểm thêm label descriptions/significance/time. | Appendix | extra analyses | [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=27\|PDF tr. 27]], [[Capturing Within-Task Variance for Continual Relation Extraction with Adaptive Prompting.pdf#page=30\|PDF tr. 30]] | useful | cần đọc kỹ trước khi cite |

## Phase 10 - Ablation Study

| Component | Intended purpose | With component | Without component | Difference | Conclusion justified | Not justified |
|---|---|---:|---:|---:|---|---|
| Prompt pool | capture within-task variance | cần điền | cần điền | cần điền | adaptive prompting có ích | variance đã được đo trực tiếp |
| Label descriptions | semantic anchors | cần điền | cần điền | cần điền | label semantics hỗ trợ model | description nào cũng tốt |
| Generative replay | retain old relations | cần điền | cần điền | cần điền | replay rất quan trọng | rehearsal-free conclusion |
| Cascade voting | task identity inference | cần điền | cần điền | cần điền | task prediction cải thiện | không có inference overhead |

## Phase 11 - Critical Reading

- Strongest contribution: biến WAVE-CRE thành system hoàn chỉnh hơn bằng label semantics và cascade voting.
- Weakest part cần kiểm: nhiều component cùng thêm vào làm attribution khó.
- Main assumption: label descriptions có chất lượng tốt và task boundary/training stream rõ.
- Alternative explanation: phần gain lớn có thể đến từ replay/task prediction hơn là label descriptions.
- Missing experiment: standardized description generation, cross-domain descriptions, prompt utilization.
- Generalization risk: label descriptions có thể yếu khi relation labels mơ hồ hoặc domain-specific.
- Reproducibility risk: cần code/hyperparams cho cascade voting và description construction.

## Phase 12 - Reproduction Check

| Item | Trạng thái | Cần làm |
|---|---|---|
| PDF local | done | đã có 30 trang |
| Code | todo | tìm official repo nếu cần reproduce |
| Dataset split | todo | đối chiếu appendix |
| Label descriptions | todo | trích nguồn/format descriptions |
| Main table | todo | điền full stage/result numbers |
| Ablation | todo | điền drops từng component |
| Task prediction | todo | điền accuracy/latency cụ thể |
| Statistical tests | todo | kiểm p-value/test setup trong appendix |

## Phase 13 - Completeness / Oral Exam

### Mình tự trả lời sau khi đọc

1. WAVE++ khác WAVE-CRE ở những component nào?
2. Label descriptions được đưa vào representation/loss thế nào?
3. Cascade voting giải quyết task identity bằng cách nào?
4. Replay trong WAVE++ giữ tri thức cũ ở cấp data, feature hay prototype?
5. Ablation nào chứng minh prompt pool, label descriptions, replay?
6. Khi nào WAVE++ không nên so sánh trực tiếp với CPL/ConPL?
7. Chi phí inference tăng ở đâu?

### Prompt oral exam

```text
Quiz me on WAVE++. Ask one question at a time. Focus on differences from WAVE-CRE, label descriptions, cascade voting, generative replay, ablations, task prediction, protocol fingerprint, and latency caveats. Do not give the answer until I respond.
```

## Final Paper Note Handoff

### Ý cần chuyển sang paper note

- [ ] Bổ sung exact equations/losses nếu cần.
- [ ] Điền full ablation numbers từ PDF.
- [ ] Ghi rõ component nào inherited từ WAVE-CRE, component nào mới.
- [ ] Thêm caveat về inference latency và task prediction.

## Liên kết

- [[WAVE++ - Capturing Within-Task Variance for Continual Relation Extraction]]
- [[Adaptive Prompting for Continual Relation Extraction]]
- [[Prompt Pool]]
- [[Task Identity Inference]]
- [[Replay in Continual Learning]]
- [[Continual Relation Extraction]]
