---
type: literature-note
status: active
project: "[[30 - Projects/Research Projects/Continual Relation Extraction with Task-Aware Prompt Adaptation/Continual Relation Extraction with Task-Aware Prompt Adaptation]]"
scope: "Research artifact W4-recovery: chuyển bốn paper đã đọc thành literature matrix v1, RQ A-D, metric list và protocol spec cho TAPTA"
papers:
  - "[[20 - Research/Papers/Consistent Prototype Learning for Few-Shot Continual Relation Extraction]]"
  - "[[20 - Research/Papers/Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors]]"
  - "[[20 - Research/Papers/Adaptive Prompting for Continual Relation Extraction]]"
  - "[[20 - Research/Papers/WAVE++ - Capturing Within-Task Variance for Continual Relation Extraction]]"
related_concepts:
  - "[[Continual Relation Extraction]]"
  - "[[Continual Few-Shot Relation Extraction]]"
  - "[[Prototype Learning]]"
  - "[[Prompt Pool]]"
  - "[[Task Identity Inference]]"
  - "[[Replay in Continual Learning]]"
  - "[[Knowledge Distillation]]"
created_at: 2026-09-05
updated_at: 2026-09-05
tags:
  - literature-note
  - research-artifact
  - continual-learning
  - relation-extraction
---

# Literature Matrix v1, RQ và Protocol Spec

## Mục tiêu artifact

Note này chuyển bốn paper đã đọc thành một nền triển khai cho đề tài [[30 - Projects/Research Projects/Continual Relation Extraction with Task-Aware Prompt Adaptation/Continual Relation Extraction with Task-Aware Prompt Adaptation]]. Trọng tâm không phải xếp hạng paper, mà là rút ra:

- literature matrix v1;
- RQ-A đến RQ-D;
- danh sách metric cần báo cáo;
- task split/protocol dự kiến cho experiment đầu tiên.

Các kết luận dưới đây dựa trên note hiện có trong vault. Chưa có kết quả local, vì vậy mọi số liệu paper được hiểu là `reported/observed`, không phải `reproduced`.

## Literature matrix v1

| Paper                                                                                                     | Setting                                                                | Knowledge cũ được giữ bằng gì?                                                        | Prompt/task-aware mechanism                                                                                       | Classifier/inference                                             | Điểm mạnh cần học                                                                                  | Hạn chế/gap cần tận dụng                                                                                                          |
| --------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| [[20 - Research/Papers/Consistent Prototype Learning for Few-Shot Continual Relation Extraction]]         | NK-CRE; mọi task đều N-way K-shot; FewRel 8 task, TACRED 8 task        | 1 raw exemplar + 1 prototype vector mỗi relation                                      | Discrete cloze prompt; task boundary dùng khi update memory, nhưng inference phân loại trên toàn relation đã thấy | Prototype similarity trên `[MASK]` representation                | Cho thấy prototype consistency và hard/confusing-class objective rất quan trọng trong few-shot CRE | Vẫn lưu raw sample; một prototype/relation có thể không phủ multimodality; chưa tách lỗi task routing và relation prediction      |
| [[20 - Research/Papers/Making Pre-trained Language Models Better Continual Few-Shot Relation Extractors]] | CFRE; task đầu data-rich, task sau 5/10-shot                           | Real exemplar memory + GPT-3.5 generated replay samples + current-task feature bucket | Hybrid prompt đưa RE về `[MASK]` representation; chưa có task router riêng                                        | Nearest-Class-Mean trên relation embedding                       | Prompt representation + MCL là baseline trực tiếp cho prompt-based FCRE                            | Task đầu không few-shot; replay phụ thuộc generated samples, cost/noise/provenance; task routing chưa phải vấn đề chính           |
| [[20 - Research/Papers/Adaptive Prompting for Continual Relation Extraction]]                             | CRE 10 task; FewRel/TACRED; raw-data-free theo nghĩa không lưu câu gốc | Task-specific prompt pools + Gaussian query/prompted-representation stats             | Prompt pool riêng theo task, top-K prefix experts; learned relation-level task predictor chọn pool lúc inference  | Shared MLP classifier; latent replay cho predictor và classifier | Closest competitor cho task-aware prompt adaptation; tách within-task variance và task predictor   | Predictor có thể drift/quên; vẫn cần task-defined pools; Gaussian đơn giản; raw-data-free không đồng nghĩa zero-memory            |
| [[20 - Research/Papers/WAVE++ - Capturing Within-Task Variance for Continual Relation Extraction]]        | CRE 10 task; FewRel/TACRED; mở rộng WAVE-CRE                           | Prompt pools + label descriptions + Gaussian latent stats                             | Cascade voting bằng Mahalanobis distance để suy ra task; label-description contrastive alignment                  | Shared classifier + latent replay                                | Tách rõ TII và WTP; cải thiện task prediction và accuracy so với WAVE-CRE                          | Inference chậm hơn do voting; phụ thuộc task boundaries/descriptions; Gaussian validation còn hẹp; memory/latency scaling chưa rõ |

## So sánh theo trục thiết kế

| Trục               | ConPL                                     | CPL                                   | WAVE-CRE                                           | WAVE++                                     | Hàm ý cho TAPTA                                                             |
| ------------------ | ----------------------------------------- | ------------------------------------- | -------------------------------------------------- | ------------------------------------------ | --------------------------------------------------------------------------- |
| Prompt             | Discrete prompt để lấy `[MASK]` embedding | Hybrid prompt + `[MASK]` embedding    | Prefix prompt pool theo task                       | Prefix prompt pool + descriptions          | Prompt không nên chỉ là template; nên là module có routing/composition      |
| Task identity      | Không có module task predictor riêng      | Không có module task predictor riêng  | Learned relation-level predictor rồi map sang task | Cascade voting không train predictor       | Đóng góp nên nằm ở suy luận task/prompt khi không có oracle task ID         |
| Prototype/memory   | Prototype + exemplar mỗi relation         | NCM prototype từ support/replay       | Gaussian latent stats theo relation                | Gaussian stats + descriptions              | Prototype hierarchy có thể dùng làm router, không chỉ classifier            |
| Replay             | Raw exemplar replay                       | Real + generated replay               | Latent replay                                      | Latent replay                              | Nếu claim rehearsal-free, phải nói rõ là no raw exemplar hoặc raw-data-free |
| Failure mode chính | Prototype distortion, confusing classes   | Overfitting, generated replay quality | Task predictor drift, wrong pool                   | Latency, description/statistics dependence | TAPTA cần đo riêng router error, relation error, memory và latency          |

## Research gap rút ra

### Gap 1: Task-aware prompt adaptation chưa đủ nếu chỉ dùng task-specific pool

`inferred`: WAVE-CRE/WAVE++ đã làm task-specific prompt pools và task inference. Vì vậy novelty của TAPTA không nên là “mỗi task có một prompt”, mà nên là **prototype-guided/hierarchical prompt routing khi inference không có task ID**.

### Gap 2: Prototype trong CRE chủ yếu làm classifier hoặc memory, chưa được khai thác đủ như routing structure

`inferred`: ConPL dùng prototype làm class anchor; CPL dùng NCM/prototype-like class means; WAVE dùng Gaussian stats cho task/pool selection. TAPTA có thể đặt prototype memory thành cấu trúc route prompt: relation prototype, internal/task prototype và soft routing path.

### Gap 3: Các paper chưa báo đủ router-error decomposition

`inferred`: WAVE++ tách TII và WTP rõ hơn, nhưng một thesis tốt vẫn cần báo `oracle vs predicted gap`, `router accuracy`, `similar-relation accuracy` để chứng minh phần task-aware routing thực sự là vấn đề trung tâm.

### Gap 4: Memory và latency chưa được chuẩn hóa công bằng

`inferred`: ConPL/CPL/WAVE/WAVE++ lưu các dạng memory khác nhau: raw samples, generated samples, prototypes, prompt parameters, Gaussian stats, descriptions. TAPTA nên báo memory footprint và inference latency thay vì chỉ accuracy.

## RQ-A đến RQ-D

### RQ-A — Task-aware prompt adaptation có giúp CRE/FCRE không?

**Câu hỏi:** So với shared prompt hoặc prototype classifier đơn giản, task-aware prompt có cải thiện final performance và giảm forgetting không?

**So sánh cần chạy:**

- P0 Shared Prompt.
- P1 Oracle-Task Prompt.
- P4 TAPTA minimal.

**Metric chính:** Final AA/Macro-F1, Average Forgetting, AIA.

### RQ-B — Không có task ID lúc inference thì mất bao nhiêu?

**Câu hỏi:** Khoảng cách giữa oracle task routing và predicted/prototype routing lớn đến đâu?

**So sánh cần chạy:**

- P1 Oracle-Task Prompt.
- P2 Learned Task Router.
- P3 Prototype Router.
- P4 TAPTA minimal.

**Metric chính:** Oracle vs Predicted gap, Router/Task-ID accuracy, Final AA/Macro-F1.

### RQ-C — Prototype/hierarchy có làm routing tốt hơn không?

**Câu hỏi:** Dùng relation/internal prototypes để route prompt có giảm nhầm lẫn giữa relation gần nghĩa và task gần nhau không?

**So sánh cần chạy:**

- P2 Learned Task Router.
- P3 Prototype Router.
- P4 TAPTA minimal.
- A1 P4 no hierarchy.
- A2 P4 hard routing.

**Metric chính:** Router accuracy, similar-relation accuracy, hard-vs-soft routing gap, confusion matrix theo relation pairs gần nghĩa.

### RQ-D — Memory/replay tương tác với prompt routing thế nào?

**Câu hỏi:** TAPTA còn cạnh tranh được trong setting `M=0` hoặc memory cực nhỏ không?

**So sánh cần chạy:**

- P4 `M=0` raw-data-free.
- P4 `M=1` exemplar/relation.
- A3 P4 no KD.

**Metric chính:** Final AA/Macro-F1, Forgetting, memory footprint, training/inference overhead.

## Protocol spec v1

### Formulation

Project nên dùng class-incremental CRE/FCRE:

```text
Task stream: T1, T2, ..., Tn
Relation set của task t: R_t
Relation sets giữa task: disjoint trong protocol chính
Sau task t, model dự đoán trên union R_1 ... R_t
Inference: không cấp oracle task ID trong protocol chính
```

Training có thể biết task boundary để tạo/update prompt/prototype, nhưng evaluation chính phải là cumulative label space không có task ID.

### Dataset ưu tiên

| Dataset | Protocol chính dự kiến | Lý do |
|---|---|---|
| FewRel | 80 public relations; ưu tiên 8 task × 10 relations theo ConPL/CPL để bắt đầu; sau đó cân nhắc 10 task theo WAVE/WAVE++ comparator | Dễ cân bằng, phổ biến trong FCRE/CRE, phù hợp debug prototype/routing |
| TACRED | Bỏ hoặc xử lý riêng `no_relation` theo baseline đang reproduce; bắt đầu 5-way 5-shot theo ConPL/CPL hoặc 10-task theo WAVE nếu chọn WAVE comparator | Khó hơn FewRel, có distribution gần thực tế hơn, nhưng preprocessing nhạy |

### Task split dự kiến

**Track A — strict few-shot thesis core:**

- FewRel: 8 task × 10 relation.
- Shot: 5-shot là primary; 10-shot là sensitivity; 2-shot chỉ stretch.
- Mục đích: so với ConPL/CPL rõ hơn, kiểm tra khi mọi task đều ít dữ liệu.

**Track B — WAVE-compatible comparator:**

- FewRel/TACRED: 10 task theo WAVE/WAVE++ nếu repo và split reproduce được.
- Mục đích: so với prompt/task-aware baselines gần nhất.

**Quyết định thực dụng:** bắt đầu code với Track A trên FewRel 5-shot, vì dễ tạo evaluator và baseline. Khi evaluator ổn mới thêm Track B để so prompt/task-aware comparator.

### Baseline tối thiểu

| ID | Model | Vai trò | Priority |
|---|---|---|---|
| B0 | Sequential FT | Lower bound catastrophic forgetting | Bắt buộc |
| B1 | Joint Training | Non-continual upper/reference | Bắt buộc |
| B2 | Frozen BERT + prototype/NCM sanity | Kiểm tra representation và evaluator | Bắt buộc |
| B3 | ConPL | Prototype/memory baseline | Bắt buộc |
| B4 | CPL | Prompt + contrastive + replay baseline | Bắt buộc |
| B5 | WAVE-CRE/WAVE++ hoặc EoE | Closest prompt/task-aware comparator | Bắt buộc nếu reproduce/smoke chạy được |

## Danh sách metric

### Metric chính

- Final Average Accuracy hoặc Final Macro-F1.
- Average Incremental Accuracy.
- Average Forgetting.
- Backward Transfer.
- Old/new relation split.

### Metric cho routing

- Router/Task-ID accuracy.
- Oracle vs predicted routing gap.
- Wrong-task but correct-relation cases nếu log được.
- Similar-relation subset accuracy.
- Confusion matrix theo relation pairs hoặc relation clusters.

### Metric chi phí

- Trainable parameters.
- Stored memory: raw examples, prototypes, prompt parameters, generated data count, latent stats.
- Inference latency hoặc số forward passes qua PLM.
- Training time theo task nếu có.

## Performance matrix evaluator

Evaluator phải lưu ma trận:

```text
          Test T1  Test T2  Test T3  ...  Test Tn
After T1    A11
After T2    A21      A22
After T3    A31      A32      A33
...
After Tn    An1      An2      An3         Ann
```

Từ cùng một matrix tính Final AA/Macro-F1, AIA, Forgetting và BWT để tránh mỗi baseline dùng công thức riêng.

## Decision cho tuần tiếp theo

- [ ] Khóa Track A FewRel 5-shot làm protocol debug đầu tiên.
- [ ] Tạo task-order file format gồm seed, task id, relation ids, train/dev/test ids.
- [ ] Viết evaluator nhận predictions theo từng checkpoint `after_task=t`.
- [ ] Chạy dummy prediction để kiểm tra ma trận `A_t,j`.
- [ ] Chưa implement TAPTA trước khi B0/B1/B2 chạy được.

## Liên kết

- [[30 - Projects/Research Projects/Continual Relation Extraction with Task-Aware Prompt Adaptation/Timeline cá nhân đến 2027-04-30]]
- [[30 - Projects/Research Projects/Continual Relation Extraction with Task-Aware Prompt Adaptation/Experiment Matrix và Metrics]]
- [[30 - Projects/Research Projects/Continual Relation Extraction with Task-Aware Prompt Adaptation/Weekly Tracker]]
- [[20 - Research/Literature Notes/Continual Relation Extraction - Prototype, Prompt và Replay]]

