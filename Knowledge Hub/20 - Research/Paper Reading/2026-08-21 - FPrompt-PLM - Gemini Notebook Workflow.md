---
type: paper-reading
date: 2026-08-21
status: draft
workflow: gemini-notebook
template: "[[Paper Reading Gemini Notebook Workflow]]"
paper: "[[FPrompt-PLM - Flexible-Prompt on Pretrained Language Model for Continual Few-Shot Relation Extraction]]"
pdf:
paper_note: "[[FPrompt-PLM - Flexible-Prompt on Pretrained Language Model for Continual Few-Shot Relation Extraction]]"
notebook_url:
target_minutes: 90
actual_minutes:
reading_goal: "Chuẩn bị deep workflow cho FPrompt-PLM: flexible prompts, prompt/prototype pools, meta-finetuning, distillation, prototype diversity, và các phần cần kiểm khi có PDF."
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
  - few-shot-learning
---

# 2026-08-21 - FPrompt-PLM - Gemini Notebook Workflow

> [!note] Ranh giới
> Đây là working note scaffold từ metadata/abstract chính thức và repository, vì chưa có PDF local. Các phần cần page-level evidence được đánh dấu `todo` hoặc `chưa có PDF`; không coi note này là bằng chứng đã đọc xong paper.

## Setup

- Paper: [[FPrompt-PLM - Flexible-Prompt on Pretrained Language Model for Continual Few-Shot Relation Extraction]]
- PDF: chưa có local PDF trong vault.
- Paper note chính: [[FPrompt-PLM - Flexible-Prompt on Pretrained Language Model for Continual Few-Shot Relation Extraction]]
- Gemini Notebook / NotebookLM URL:
- Mục tiêu buổi đọc: dựng bản đồ đọc sâu trước, sau đó bổ sung equations/results/ablation khi có PDF.
- Phần cần đọc trước khi có PDF: abstract/metadata, README, dataset/code structure.
- Phần cần đọc khi có PDF: Method, Losses, Experiments, Ablation, Case Study, Limitations.

## Phase 1 - Paper Map

### Prompt gửi Gemini

```text
Do not summarize the paper in detail yet. Create a structural map of this paper and identify problem, motivation, gap, contributions, pipeline, components, losses, datasets, baselines, metrics, main experiments, ablations, case studies, and limitations. For every item, point to the relevant section, figure, table, or equation. The purpose is to tell me WHERE to read, not to replace my reading.
```

### Paper map - scaffold từ nguồn hiện có

- **Problem:** CFS-RE phải học relation mới theo chuỗi từ ít examples, đồng thời tránh catastrophic forgetting và few-shot overfitting.
- **Motivation:** supervised RE cố định không phù hợp khi relation mới xuất hiện liên tục.
- **Gap:** cần framework tận dụng PLM, prompt memory và prototype memory trong continual few-shot setting.
- **Main idea:** Flexible-prompt on PLM kết hợp flexible-prompt embedding, pretrained-language understanding và nearest-prototype learning.
- **Main contributions:** prompt pool, prototype pool, meta-training, continual meta-finetuning, testing, multiple distillation losses, prototype-diversity loss.
- **Important figure:** cần kiểm khi có PDF.
- **Important equations:** flexible prompt, nearest-prototype, distillation losses, prototype-diversity loss.
- **Main result table:** cần kiểm khi có PDF.
- **Ablation table:** cần kiểm khi có PDF.
- **Case study:** README nêu similarity heatmaps giữa 15 prototypes và 3 prompts trên TACRED với BERT Base.
- **Limitations:** chưa có PDF local nên chưa có page evidence và chưa kiểm protocol/số định lượng.

### Chỗ cần đọc trước

- [ ] Abstract/metadata
- [ ] README/code structure
- [ ] Method section trong PDF
- [ ] Loss definitions
- [ ] Main results
- [ ] Ablation
- [ ] Case study
- [ ] Limitations/conclusion

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
| General problem | Relation extraction cần nhận diện quan hệ giữa hai entity trong câu; CFS-RE làm việc này trong stream task và ít mẫu. | [XJTU metadata](https://scholar.xjtu.edu.cn/zh/publications/fprompt-plm-flexible-prompt-on-pretrained-language-model-for-cont/) |
| Why it matters | Quan hệ mới xuất hiện liên tục, còn việc gán nhãn nhiều ví dụ cho relation mới là tốn kém. | [XJTU metadata](https://scholar.xjtu.edu.cn/zh/publications/fprompt-plm-flexible-prompt-on-pretrained-language-model-for-cont/) |
| What prior work solves | Prompt/prototype/memory methods cố giảm forgetting và tận dụng PLM trong low-resource setup. | inferred |
| What prior work fails to solve | CFS-RE vẫn chịu catastrophic forgetting và overfitting khi few-shot. | [XJTU metadata](https://scholar.xjtu.edu.cn/zh/publications/fprompt-plm-flexible-prompt-on-pretrained-language-model-for-cont/) |
| Exact research gap | Cần cập nhật prompt/prototype qua thời gian mà vẫn dự đoán được mọi relation đã thấy. | inferred từ abstract |
| Hypothesis / intuition | Prompt pool lưu cách điều kiện hóa PLM; prototype pool lưu anchors quan hệ; distillation/diversity giữ cân bằng ổn định và phân tách. | inferred |
| Contribution addressing the gap | FPrompt-PLM dùng flexible-prompt embedding, PLM understanding, nearest-prototype learning, prompt/prototype pools, distillation và prototype diversity. | [XJTU metadata](https://scholar.xjtu.edu.cn/zh/publications/fprompt-plm-flexible-prompt-on-pretrained-language-model-for-cont/) |

### Câu hỏi tự kiểm tra

- [ ] FPrompt-PLM khác CPL ở prompt/prototype memory như thế nào?
- [ ] Prompt pool lưu “task knowledge” hay “time-period knowledge”?
- [ ] Prototype-diversity loss có thể gây side effect gì?

## Phase 4 - Method / Architecture

### Tôi tự vẽ trước

```text
Sentence + entity pair
-> PLM encoder
-> flexible-prompt embedding / prompt pool
-> relation representation
-> prototype pool for seen relations
-> nearest-prototype prediction
-> continual meta-finetuning on new relations
-> distillation losses preserve old knowledge
-> prototype-diversity loss separates relation anchors
```

### Component map

| Component | Input | Operation | Output | Purpose | Evidence |
|---|---|---|---|---|---|
| Flexible-prompt embedding | task/time/input context | create or select prompt representation | prompt-conditioned PLM behavior | adapt PLM to CFS-RE | [XJTU metadata](https://scholar.xjtu.edu.cn/zh/publications/fprompt-plm-flexible-prompt-on-pretrained-language-model-for-cont/) |
| Pretrained-language understanding | prompted sentence | PLM encoding | semantic representation | exploit PLM prior | [XJTU metadata](https://scholar.xjtu.edu.cn/zh/publications/fprompt-plm-flexible-prompt-on-pretrained-language-model-for-cont/) |
| Prompt pool | historical prompts | continuous update | prompt memory | preserve/adapt prompting across periods | [XJTU metadata](https://scholar.xjtu.edu.cn/zh/publications/fprompt-plm-flexible-prompt-on-pretrained-language-model-for-cont/) |
| Prototype pool | relation representations | update prototypes | relation anchors | classify seen relations by nearest prototype | [XJTU metadata](https://scholar.xjtu.edu.cn/zh/publications/fprompt-plm-flexible-prompt-on-pretrained-language-model-for-cont/) |
| Distillation losses | old/new model signals | preserve outputs/features/prompts | regularized model | reduce catastrophic forgetting | [XJTU metadata](https://scholar.xjtu.edu.cn/zh/publications/fprompt-plm-flexible-prompt-on-pretrained-language-model-for-cont/) |
| Prototype-diversity loss | prototypes | push/separate anchors | more diverse prototypes | reduce prototype collapse | [XJTU metadata](https://scholar.xjtu.edu.cn/zh/publications/fprompt-plm-flexible-prompt-on-pretrained-language-model-for-cont/) |

### Điều tôi vẫn chưa hiểu

- [ ] Flexible prompt được chọn theo task, input, hoặc time period?
- [ ] Prototype pool có lưu một prototype/relation hay nhiều prototype/relation?
- [ ] Distillation loss distill logits, features, prompts hay prototype relations?
- [ ] Có dùng exemplar replay không?

## Phase 5 - Section Recall

### Method - Flexible prompt + PLM

- **Input:** sentence/entity pair và prompt information.
- **Process:** PLM được điều kiện hóa bởi flexible prompt.
- **Output:** relation representation.
- **Purpose:** tận dụng pretrained knowledge trong few-shot continual setting.
- **Still unclear:** prompt parameterization chính xác.

### Method - Prompt pool + prototype pool

- **Input:** prompts/prototypes đã học qua các task/time periods.
- **Process:** cập nhật liên tục pool khi relation mới đến.
- **Output:** prompt memory và relation anchors cho seen relations.
- **Purpose:** giữ tri thức cũ mà vẫn thích nghi relation mới.
- **Still unclear:** pool growth, pruning và inference selection.

## Phase 6 - Equations

| Eq/block | Dùng để làm gì? | Biến chính | Behavior được khuyến khích | Evidence / ablation | Status |
|---|---|---|---|---|---|
| Flexible prompt | condition PLM | prompt embeddings | adapt to new relations | chưa có PDF | todo |
| Nearest prototype | classify relation | embedding, prototypes | choose closest relation anchor | chưa có PDF | todo |
| Distillation losses | retain old knowledge | old/new signals | reduce forgetting | chưa có PDF | todo |
| Prototype diversity | separate anchors | prototype vectors | reduce collapse/overlap | chưa có PDF | todo |
| Continual meta-finetuning | adapt across tasks | meta parameters/task data | fast few-shot adaptation | chưa có PDF | todo |

## Phase 7 - Loss Functions

```text
FPrompt-PLM training signal
├── relation classification / nearest prototype
├── prompt adaptation
├── continual meta-finetuning
├── multiple distillation losses
└── prototype-diversity regularization
```

| Loss/block | Inputs | Trains component | Behavior | Weight | Ablation |
|---|---|---|---|---|---|
| Nearest-prototype/classification | examples + prototypes | encoder/prototypes | classify seen relations | chưa có PDF | todo |
| Distillation losses | old and current model signals | encoder/prompt/prototype modules | preserve old knowledge | chưa có PDF | todo |
| Prototype-diversity loss | prototype pool | prototype space | separate relation anchors | chưa có PDF | todo |
| Meta-finetuning objective | support examples/tasks | prompt/encoder parameters | adapt quickly to few-shot relations | chưa có PDF | todo |

## Phase 8 - Experiments

| Experiment | Research question | Dataset | Baselines | Metric | Table/Figure | Main result | Caveat |
|---|---|---|---|---|---|---|---|
| Main CFS-RE results | FPrompt-PLM có cải thiện SOTA không? | FewRel/TACRED | cần đọc PDF | accuracy/F1 cần xác minh | cần đọc PDF | abstract báo cải thiện đáng kể | chưa có số |
| Ablation | prompt/prototype/distillation/diversity đóng góp gì? | FewRel/TACRED | variants | cần xác minh | cần đọc PDF | cần đọc PDF | chưa có PDF |
| Case study | prompt/prototype similarity cho thấy gì? | TACRED | qualitative | heatmap | README case study | 15 prototypes, 3 prompts, BERT Base | qualitative |
| Sensitivity | số prompts/prototypes/shots ảnh hưởng thế nào? | cần đọc PDF | variants | cần xác minh | cần đọc PDF | cần đọc PDF | chưa có PDF |

### Protocol fingerprint

- Dataset and split: README cho thấy FewRel và TACRED.
- Scenario / label space: continual few-shot relation extraction.
- Backbone: README case study nhắc BERT Base; cần kiểm main experiments.
- Seeds / number of runs: chưa có PDF.
- Metric and averaging: chưa có PDF.
- Memory/replay: prompt pool và prototype pool; chưa rõ có raw exemplar replay không.
- External data: chưa xác minh.
- Evaluation after each task: cần đọc PDF.

## Phase 9 - Claim to Evidence

| Claim | Where claim appears | Experiment | Evidence | My judgment | Caveat |
|---|---|---|---|---|---|
| FPrompt-PLM gồm flexible-prompt embedding, PLM understanding, nearest-prototype learning. | abstract/metadata | method claim | [XJTU metadata](https://scholar.xjtu.edu.cn/zh/publications/fprompt-plm-flexible-prompt-on-pretrained-language-model-for-cont/) | reported | cần PDF để lấy equations |
| Prompt pool và prototype pool được cập nhật liên tục. | abstract/metadata | method claim | [XJTU metadata](https://scholar.xjtu.edu.cn/zh/publications/fprompt-plm-flexible-prompt-on-pretrained-language-model-for-cont/) | reported | chưa biết growth/budget |
| Dùng multiple distillation losses và prototype-diversity loss. | abstract/metadata | method claim | [XJTU metadata](https://scholar.xjtu.edu.cn/zh/publications/fprompt-plm-flexible-prompt-on-pretrained-language-model-for-cont/) | reported | chưa rõ công thức |
| Code repo có FewRel/TACRED material và case study. | README | code/case study | [GitHub README](https://github.com/lyfxjtu/FPrompt-PLM) | reported | README không thay thế paper |
| Paper metadata TKDE 2024/DOI. | publisher/bibliography | metadata | [IEEE Xplore](https://ieeexplore.ieee.org/document/10584140/), [DBLP](https://dblp.org/rec/journals/tkde/ZhangLWWYWL24.html) | reliable metadata | PDF inaccessible locally |

## Phase 10 - Ablation Study

| Component | Intended purpose | With component | Without component | Difference | Conclusion justified | Not justified |
|---|---|---:|---:|---:|---|---|
| Flexible prompt | adapt PLM to few-shot relations | cần PDF | cần PDF | cần PDF | chưa kết luận | prompt là nguồn gain chính |
| Prompt pool | preserve prompt knowledge over time | cần PDF | cần PDF | cần PDF | chưa kết luận | pool scale tốt |
| Prototype pool | retain relation anchors | cần PDF | cần PDF | cần PDF | chưa kết luận | một prototype đủ cho mọi relation |
| Distillation losses | reduce forgetting | cần PDF | cần PDF | cần PDF | chưa kết luận | distillation luôn hơn replay |
| Prototype diversity | separate relation anchors | cần PDF | cần PDF | cần PDF | chưa kết luận | diversity không hại relation gần nghĩa |

## Phase 11 - Critical Reading

- Strongest expected contribution: kết hợp prompt memory và prototype memory trong CFS-RE.
- Weakest part hiện tại: chưa có PDF, nên chưa kiểm được protocol và quantitative evidence.
- Main assumption cần kiểm: pool selection/growth không làm inference quá tốn.
- Alternative explanation: gains có thể đến từ PLM/backbone hoặc task setup hơn là flexible prompt riêng.
- Missing experiment cần tìm: ablation từng loss, sensitivity số prompts/prototypes, comparison với CPL/ConPL cùng protocol.
- Generalization risk: relation labels/domain ngoài FewRel/TACRED có thể làm prototype/prompt quality giảm.
- Reproducibility risk: nếu code thiếu hyperparameters/checkpoints, khó reproduce.

## Phase 12 - Reproduction Check

| Item | Trạng thái | Cần làm |
|---|---|---|
| PDF local | blocked | IEEE download tự động bị chặn; cần tải thủ công hoặc dùng access khác |
| Metadata | done | IEEE/DBLP/XJTU đã có |
| Code | partial | repo GitHub đã xác định |
| Dataset split | todo | đọc PDF/code configs |
| Main table | todo | cần PDF |
| Ablation | todo | cần PDF |
| Equations | todo | cần PDF |
| Compute | todo | cần PDF/code |

## Phase 13 - Completeness / Oral Exam

### Mình tự trả lời sau khi đọc

1. FPrompt-PLM định nghĩa CFS-RE thế nào?
2. Flexible-prompt embedding khác prompt tuning/prefix tuning thông thường ở đâu?
3. Prompt pool và prototype pool được cập nhật khi task mới đến như thế nào?
4. Nearest-prototype learning dùng khoảng cách gì?
5. Distillation losses giữ knowledge cũ ở cấp nào?
6. Prototype-diversity loss có bằng chứng ablation mạnh không?
7. So sánh FPrompt với CPL/ConPL/WAVE++ cần giữ caveat protocol nào?

### Prompt oral exam

```text
Quiz me on FPrompt-PLM. Ask one question at a time. Focus on CFS-RE problem setup, flexible prompts, prompt pool, prototype pool, nearest-prototype learning, distillation, prototype diversity, and evidence gaps. Do not give the answer until I respond.
```

## Final Paper Note Handoff

### Ý cần chuyển sang paper note

- [ ] Bổ sung PDF local và page-level evidence.
- [ ] Điền công thức flexible prompt, nearest prototype, distillation, prototype diversity.
- [ ] Điền main results/ablation bằng số chính xác.
- [ ] Ghi rõ nếu paper dùng exemplar replay hay chỉ prompt/prototype memory.
- [ ] So sánh protocol với CPL, ConPL, WAVE-CRE và WAVE++.

## Liên kết

- [[FPrompt-PLM - Flexible-Prompt on Pretrained Language Model for Continual Few-Shot Relation Extraction]]
- [[Continual Few-Shot Relation Extraction]]
- [[Prompt Tuning]]
- [[Prompt Pool]]
- [[Prototype Learning]]
- [[Catastrophic Forgetting]]
