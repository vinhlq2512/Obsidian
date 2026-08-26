---
type: paper-reading
date: 2026-08-21
status: draft
workflow: gemini-notebook
template: "[[Paper Reading Gemini Notebook Workflow]]"
paper: "[[Adaptive Prompting for Continual Relation Extraction]]"
pdf: "[[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf]]"
paper_note: "[[Adaptive Prompting for Continual Relation Extraction]]"
notebook_url:
target_minutes: 90
actual_minutes:
reading_goal: "Hiểu WAVE-CRE theo deep workflow: within-task variance, prompt pool, sparse MoE routing, latent replay, task prediction, results và ablation."
current_phase: scaffolded
completed: false
need_review: true
review_date:
created_at: 2026-08-21
updated_at: 2026-08-23
tags:
  - paper-reading
  - gemini-notebook
  - relation-extraction
  - continual-learning
---

# 2026-08-21 - WAVE-CRE - Gemini Notebook Workflow

> [!note] Ranh giới
> Đây là working note scaffold từ paper note/PDF để hỗ trợ đọc với Gemini Notebook. Các phần “closed-book recall”, “mình tự trả lời”, “oral exam” vẫn để trống vì chưa có câu trả lời cá nhân của bạn; không coi note này là bằng chứng đã đọc xong paper.

## Setup

- Paper: [[Adaptive Prompting for Continual Relation Extraction]]
- PDF: [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf]]
- Paper note chính: [[Adaptive Prompting for Continual Relation Extraction]]
- Gemini Notebook / NotebookLM URL:
- Mục tiêu buổi đọc: hiểu vì sao một prompt/task chưa đủ, WAVE-CRE route input vào prompt experts thế nào, và replay/task predictor đóng góp gì.
- Phần cần đọc trước: Introduction, Framework, Table 1, Ablations, Conclusion.
- PDF count đã kiểm tra: 9 trang.

## Phase 1 - Paper Map

### Prompt gửi Gemini

```text
Do not summarize the paper in detail yet. Create a structural map of this paper and identify problem, motivation, gap, contributions, pipeline, components, losses, datasets, baselines, metrics, main experiments, ablations, and limitations. For every item, point to the relevant section, figure, table, or equation. The purpose is to tell me WHERE to read, not to replace my reading.
```

### Paper map - scaffold từ nguồn

- **Problem:** CRE phải học relation mới tuần tự nhưng vẫn phân loại trên toàn bộ relation đã thấy. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=2|PDF tr. 2]]
- **Motivation:** trong một task, examples có nhiều mode khác nhau; một prompt cố định có thể underfit within-task variance. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=1|PDF tr. 1]]
- **Gap:** prompt-based CRE trước đó chưa mô hình hóa đủ đa dạng nội bộ của từng task.
- **Main idea:** tạo task-specific prompt pool gồm nhiều prefix experts; input route tới expert phù hợp; latent replay giữ relation cũ.
- **Main contributions:** adaptive prompting, sparse-MoE scoring, latent-space generative replay, task predictor cho inference.
- **Important figure:** framework/method ở phần chính. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=3|PDF tr. 3]]
- **Important equations:** prefix/prompt expert, sparse scoring, objective học task mới, latent replay. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=4|PDF tr. 4]], [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=5|PDF tr. 5]]
- **Main result table:** Table 1. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=6|PDF tr. 6]]
- **Ablation table:** task-specific pool, number of experts, task predictor. [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=7|PDF tr. 7]]
- **Limitations:** task prediction dependency, Gaussian latent replay assumption, prompt pool cost.

### Chỗ cần đọc trước

- [ ] Abstract + Introduction
- [ ] Prefix tuning/MoE formulation
- [ ] Task-specific prompt pool
- [ ] Objective + latent replay
- [ ] Table 1
- [ ] Ablations

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
| General problem | Class-incremental CRE yêu cầu model dự đoán trên tất cả relation đã học, không chỉ relation của task hiện tại. | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=2\|PDF tr. 2]] |
| Why it matters | Relation mới xuất hiện liên tục, còn dữ liệu cũ thường không thể giữ đầy đủ. | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=1\|PDF tr. 1]] |
| What prior work solves | Prompt tuning dùng PLM/prefix để thích nghi task với ít tham số trainable hơn. | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=3\|PDF tr. 3]] |
| What prior work fails to solve | Một prompt/task không đủ bắt nhiều mode trong cùng task. | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=1\|PDF tr. 1]] |
| Exact research gap | Cần adaptive prompt selection ở cấp input/task để mô hình hóa within-task variance. | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=4\|PDF tr. 4]] |
| Hypothesis / intuition | Nhiều prompt experts giúp input khác nhau trong cùng task có adapter phù hợp hơn; latent replay bảo vệ classifier khỏi bias task mới. | inferred |
| Contribution addressing the gap | WAVE-CRE thêm task-specific prompt pool, sparse routing và latent generative replay. | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=4\|PDF tr. 4]], [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=5\|PDF tr. 5]] |

### Câu hỏi tự kiểm tra

- [ ] Within-task variance trong RE khác class imbalance như thế nào?
- [ ] Prompt pool đang giải quyết underfitting trong task hay forgetting giữa task?
- [ ] Task predictor có phải assumption inference quan trọng không?

## Phase 4 - Method / Architecture

### Tôi tự vẽ trước

```text
Sentence + entity markers
-> PLM encoder
-> task-specific prompt pool / prefix experts
-> sparse scoring chọn prompt experts phù hợp với input
-> relation representation
-> relation classifier trên labels đã thấy
-> latent generative replay cho relation cũ
-> task predictor hỗ trợ inference khi task identity không biết
```

### Component map

| Component | Input | Operation | Output | Purpose | Evidence |
|---|---|---|---|---|---|
| Prefix expert | hidden state/query | thêm learned prefix vào self-attention | prompted representation | parameter-efficient adaptation | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=3\|PDF tr. 3]] |
| Task-specific prompt pool | task id, input representation | lưu nhiều experts cho một task | candidate prompts | bắt within-task variance | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=4\|PDF tr. 4]] |
| Sparse-MoE scoring | input query + prompt keys | chọn/pha trộn prompt experts | routed representation | dùng prompt phù hợp từng input | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=4\|PDF tr. 4]] |
| Latent generative replay | old relation latent distribution | sample latent cũ trong training task mới | replay features | giảm classifier forgetting | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=5\|PDF tr. 5]] |
| Task predictor | input representation | dự đoán task/relation candidate | task identity estimate | inference khi không có task label | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=5\|PDF tr. 5]] |

### Điều tôi vẫn chưa hiểu

- [ ] Sparse score có dùng top-k hard selection hay soft mixture?
- [ ] Gaussian latent replay được fit theo relation hay task?
- [ ] Task predictor sai ảnh hưởng bao nhiêu đến relation classifier?

## Phase 5 - Section Recall

### Framework - Adaptive prompting

- **Input:** sentence/entity pair và task hiện tại.
- **Process:** route input tới prompt experts trong task-specific pool.
- **Output:** representation đã được prompt điều kiện hóa.
- **Purpose:** thay một prompt cố định bằng nhiều prompt nhỏ để bao phủ variance.
- **Still unclear:** mức tăng tham số theo số task và số experts.

### Framework - Generative replay

- **Input:** latent statistics của relation cũ.
- **Process:** sample latent replay trong khi học task mới.
- **Output:** synthetic old features cho classifier.
- **Purpose:** tránh classifier bias về relation mới.
- **Still unclear:** replay latent giữ được multimodal relation đến đâu.

## Phase 6 - Equations

### Prompt operational equation walkthrough

```text
Walk me through the key equations or formal blocks in this paper.

For each equation/block, explain:
1. Input: what variables or objects go into it.
2. Output: what it produces.
3. Where it is used in the training/inference pipeline.
4. What behavior it encourages.
5. What would likely break or become weaker if removed.
6. Which table, figure, ablation, or result supports its usefulness.

Do not summarize the whole paper. Focus only on operational understanding of the equations and formal mechanisms.
```

| Eq/block | Dùng để làm gì? | Biến chính | Behavior được khuyến khích | Evidence / ablation | Status |
|---|---|---|---|---|---|
| Prefix tuning | điều kiện hóa self-attention | prefix keys/values | thích nghi PLM không fine-tune toàn bộ | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=3\|PDF tr. 3]] | source-checked |
| Sparse-MoE score | chọn prompt expert | input query, prompt keys, $L\times K=8$ trong ablation | route input tới expert phù hợp; một expert/prompt tốt nhất ở TACRED $T_{10}$ | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=4\|PDF tr. 4]], [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=7\|PDF tr. 7]] | source-checked |
| Training objective | học task mới + bảo vệ cũ | current-task classification, replay query/prompted representations | cân bằng old/new classes và giảm classifier forgetting | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=5\|PDF tr. 5]] | source-checked |
| Latent distribution | sinh replay features | per-relation statistics cho query/prompted representations | giữ vùng representation của relation cũ mà không lưu raw examples | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=5\|PDF tr. 5]] | source-checked |

## Phase 7 - Loss Functions

```text
WAVE-CRE training signal
├── current-task classification
├── sparse prompt routing / expert selection
├── latent replay for old relations
└── task prediction / relation prediction at inference
```

| Loss/block | Inputs | Trains component | Behavior | Weight | Ablation |
|---|---|---|---|---|---|
| Current task classification | current examples | prompt/classifier | learn new relations | source-checked | main training |
| Replay loss | latent old query/prompted samples | classifier/shared representation | retain old relations | source-checked | replay contributes to forgetting control but module-level replay ablation is not fully separated |
| Prompt selection score | input + prompt keys | prompt pool/router | match examples to experts | source-checked | expert number/pool ablation |
| Task predictor objective | input + relation/task labels | relation-level predictor -> task mapping | infer task identity | source-checked | task predictor analysis |

## Phase 8 - Experiments

| Experiment | Research question | Dataset | Baselines | Metric | Table/Figure | Main result | Caveat |
|---|---|---|---|---|---|---|---|
| Main CRE results | WAVE-CRE có tốt hơn CRE baselines không? | FewRel/TACRED | prompt/replay CRE baselines | accuracy by learning stage | Table 1 | FewRel $T_{10}$ 85.0, TACRED $T_{10}$ 78.7 theo paper note chính | reported, not reproduced |
| Prompt pool ablation | nhiều prompt/task có hơn một prompt/task không? | TACRED task-incremental | WAVE-CRE vs không prompt pool | final accuracy | Table 2 | $T_{10}$ tăng từ 83.4 lên 85.2, tức +1.8 | chỉ trong framework này |
| Number of experts | thêm experts có luôn tốt hơn không? | TACRED | $L,K$ variants giữ $L\times K=8$ | accuracy | Table 3 | $L=1,K=8$ đạt 85.2 ở $T_{10}$, tốt nhất trong sweep | cost/routing trade-off |
| Task predictor | task identity inference ảnh hưởng thế nào? | FewRel/TACRED | WAVE-CRE, HiDe-Prompt, EPI | task prediction accuracy | Table 4 | trung bình WAVE-CRE cao hơn HiDe-Prompt/EPI, nhưng không thắng mọi task | predictor vẫn là bottleneck tiềm năng |

### Protocol fingerprint

- Dataset and split: FewRel và TACRED theo setup CRE trong paper.
- Scenario / label space: continual relation extraction, evaluate trên relation đã thấy.
- Backbone: frozen BERT; train prompt pools và classifier theo paper note chính.
- Seeds / number of runs: cần kiểm chứng từ experiment section.
- Metric and averaging: accuracy theo learning stage; cần đọc cách average task order.
- Memory/replay: latent generative replay, không phải chỉ raw exemplar replay.
- Task identity at inference: task predictor được dùng, cần xem assumption.

## Phase 9 - Claim to Evidence

| Claim | Where claim appears | Experiment | Evidence | My judgment | Caveat |
|---|---|---|---|---|---|
| Within-task variance là motivation chính. | Introduction | motivation | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=1\|PDF tr. 1]] | important | paper không nhất thiết đo variance trực tiếp |
| Task-specific prompt pool là novelty method. | Framework | prompt pool | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=4\|PDF tr. 4]] | supported | cần đọc chi tiết routing |
| Latent replay giảm forgetting. | Framework/ablation | replay | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=5\|PDF tr. 5]] | plausible | ablation mới cho evidence định lượng |
| WAVE-CRE cải thiện main accuracy. | Results | Table 1 | [[Adaptive Prompting for Continual Relation Extraction- A Within-Task Variance Perspective.pdf#page=6\|PDF tr. 6]] | reported/observed | protocol-specific |

## Phase 10 - Ablation Study

| Component | Intended purpose | With component | Without component | Difference | Conclusion justified | Not justified |
|---|---|---:|---:|---:|---|---|
| Task-specific prompt pool | bắt within-task variance | TACRED $T_{10}$ 85.2 | không prompt pool 83.4 | +1.8 | pool có ích trong setup này | mọi task đều cần nhiều prompts |
| Number of experts | tăng capacity prompt | $L=1,K=8$: 85.2 | $L=8,K=1$: 84.2 | +1.0 | route độc lập theo expert có lợi | càng nhiều expert càng tốt |
| Latent replay | bảo vệ relation cũ | có query/prompted replay | chưa có ablation tách riêng từng replay module trong note chính | chưa kết luận định lượng riêng | replay là cơ chế bảo vệ classifier | Gaussian replay luôn đủ |
| Task predictor | inference task identity | WAVE-CRE trung bình FewRel 86.17 / TACRED 79.31 | HiDe-Prompt 80.09 / 72.01; EPI 62.67 / 62.53 | WAVE-CRE cao hơn trung bình | predictor ảnh hưởng end-to-end | task identity đã được giải quyết hoàn toàn |

## Phase 11 - Critical Reading

- Strongest contribution: nhìn prompt tuning như expert pool để xử lý within-task variance.
- Weakest part cần kiểm: task predictor và latent Gaussian replay có thể là bottleneck.
- Main assumption: task boundaries trong training rõ; inference có thể cần task prediction.
- Alternative explanation: gain có thể đến từ replay/classifier consolidation hơn là prompt pool riêng.
- Missing experiment: measure prompt utilization, within-task clusters, latency/memory growth.
- Generalization risk: chỉ kiểm trên FewRel/TACRED; relation semantics khác domain có thể làm routing khó hơn.
- Reproducibility risk: cần code/hyperparameter để kiểm selection và replay.

## Phase 12 - Reproduction Check

| Item | Trạng thái | Cần làm |
|---|---|---|
| PDF local | done | đã có 9 trang |
| Code | todo | tìm official repo nếu cần reproduce |
| Dataset split | todo | đối chiếu FewRel/TACRED split |
| Hyperparameters | todo | extract từ paper/code |
| Main table | partial | đã ghi $T_{10}$ FewRel/TACRED; cần full stage table nếu reproduce |
| Ablation | partial | đã điền prompt pool, expert count, task predictor; replay module-level còn thiếu |
| Compute | open | tìm GPU/training cost nếu paper báo |

## Phase 13 - Completeness / Oral Exam

### Mình tự trả lời sau khi đọc

1. WAVE-CRE định nghĩa within-task variance thế nào?
2. Task-specific prompt pool khác một prompt/task ở đâu?
3. Sparse-MoE scoring chọn experts bằng tín hiệu nào?
4. Latent generative replay khác exemplar replay ở đâu?
5. Task predictor có thể làm sai toàn pipeline như thế nào?
6. Kết quả nào chứng minh prompt pool, kết quả nào chứng minh replay?
7. Khi so sánh với WAVE++, phần nào là tiền thân trực tiếp?

### Prompt oral exam

```text
Quiz me on WAVE-CRE. Ask one question at a time. Focus on within-task variance, prompt pools, sparse MoE routing, latent replay, task prediction, ablation interpretation, and protocol caveats. Do not give the answer until I respond.
```

## Final Paper Note Handoff

### Ý cần chuyển sang paper note

- [x] Điền lại equation/formal blocks ở mức operational từ paper note/PDF.
- [x] Điền ablation numbers chính cho prompt pool, expert count và task predictor.
- [ ] Tách định lượng riêng của các replay module nếu paper/code cho phép.
- [ ] Ghi rõ task predictor là assumption/bottleneck.
- [ ] Khi so sánh với WAVE++, tách phần inherited WAVE-CRE và phần WAVE++ thêm mới.

## Liên kết

- [[Adaptive Prompting for Continual Relation Extraction]]
- [[WAVE++ - Capturing Within-Task Variance for Continual Relation Extraction]]
- [[Prompt Pool]]
- [[Prefix Tuning]]
- [[Task Identity Inference]]
- [[Replay in Continual Learning]]
