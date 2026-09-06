---
type: project-plan
status: active
project: "[[30 - Projects/Research Projects/Continual Relation Extraction with Task-Aware Prompt Adaptation/Continual Relation Extraction with Task-Aware Prompt Adaptation]]"
created_at: 2026-09-05
updated_at: 2026-09-05
tags:
  - experiment-plan
  - research-project
  - continual-learning
  - relation-extraction
---

# Experiment Matrix và Metrics

## Research questions

**RQ-A — Task-aware prompt có giúp continual relation extraction không?**

So sánh shared prompt, oracle-task prompt và learned/prototype router để đo giá trị thật của task awareness.

**RQ-B — Không có task ID lúc inference thì mất bao nhiêu performance?**

Đo gap giữa oracle routing và predicted routing.

**RQ-C — Prototype/hierarchy có làm routing tốt hơn không?**

Kiểm tra prototype-guided router, đặc biệt trên các relation gần nghĩa.

**RQ-D — Memory và prompt tương tác thế nào?**

So `M=0` rehearsal-free/raw-data-free với `M=1` exemplar/relation nếu đủ thời gian.

## Experiment matrix

| ID | Model | Shared Prompt | Task Prompt | Router | Prototype | Hierarchy | Replay | Mục đích |
|---|---|---|---|---|---|---|---|---|
| B0 | Sequential FT | - | - | - | - | - | 0 | Lower bound forgetting |
| B1 | Joint Training | - | - | - | - | - | full | Reference upper bound |
| B2 | Prototype sanity | - | - | - | relation | - | 0/1 | Kiểm tra representation/prototype |
| B3 | ConPL | - | - | - | relation | - | 1 | Prototype-based FCRE baseline |
| B4 | CPL | yes | - | - | model-specific | - | yes | Prompt + contrastive baseline |
| B5 | WAVE-CRE/WAVE++ hoặc EoE | yes | yes | learned/voting | model-specific | - | latent/0 | Closest task-aware prompt comparator |
| P0 | Shared Prompt | yes | - | - | - | - | 0/1 | Prompt baseline tối thiểu |
| P1 | Oracle-Task Prompt | yes | yes | oracle | - | - | 0/1 | Upper bound cho routing |
| P2 | Learned Task Router | yes | yes | learned | - | - | 0/1 | Test task prediction |
| P3 | Prototype Router | yes | yes | prototype | relation | - | 0/1 | Test semantic routing |
| P4 | TAPTA minimal | yes | yes | prototype-soft | relation/internal | yes | 0/1 | Proposed full model tối thiểu |
| A1 | P4 no hierarchy | yes | yes | prototype-soft | relation | - | 0/1 | Tree có cần không? |
| A2 | P4 hard routing | yes | yes | top-1 | relation/internal | yes | 0/1 | Soft routing có hơn hard routing không? |
| A3 | P4 no KD | yes | yes | prototype-soft | relation/internal | yes | 0/1 | KD có giúp chống quên không? |
| A4 | P4 EMA vs snapshot | yes | yes | prototype-soft | relation/internal | yes | 0/1 | EMA có hơn freeze checkpoint không? |

## Metrics bắt buộc

Evaluator phải lưu performance matrix:

```text
          Test T1  Test T2  Test T3  ...  Test Tn
After T1    A11
After T2    A21      A22
After T3    A31      A32      A33
...
After Tn    An1      An2      An3         Ann
```

Từ matrix này tính:

- Final Average Accuracy hoặc Final Macro-F1.
- Average Incremental Accuracy.
- Average Forgetting.
- Backward Transfer.
- Old/new split.
- Router/Task-ID accuracy.
- Oracle vs predicted routing gap.
- Similar-relation subset accuracy.
- Trainable parameters.
- Stored memory: raw examples, prototypes, prompt parameters, Gaussian/statistics nếu có.
- Inference latency hoặc số forward passes qua PLM.

## Protocol mặc định

| Thành phần | Setting khởi tạo |
|---|---|
| Backbone | `bert-base-uncased` hoặc backbone giống baseline cần reproduce |
| Input | sentence + marked head/tail entities |
| Max sequence length | 256 |
| Optimizer | AdamW |
| Encoder LR | `2e-5` nếu encoder trainable |
| Prompt/router LR | bắt đầu `5e-4` |
| Batch size | 16, dùng gradient accumulation nếu thiếu VRAM |
| Weight decay | 0.01 |
| Warm-up | 10% optimization steps |
| Epochs | tối đa 10/task cho vòng debug |
| Gradient clipping | 1.0 |
| Prompt length | 10 virtual tokens/component |
| Prompt top-k | 2 |
| Router temperature | 0.1 |
| Seeds | 2021, 2121, 2221, 2321, 2421 |
| Runs | 1 seed debug, 3 seeds pilot, 5 seeds finalists |

## Config cần có

```text
configs/
  conpl_original.yaml
  cpl_original.yaml
  wave_original.yaml
  common_fewrel_5shot.yaml
  common_tacred_5shot.yaml
  tapta_p0_shared_prompt.yaml
  tapta_p1_oracle_task_prompt.yaml
  tapta_p2_learned_router.yaml
  tapta_p3_prototype_router.yaml
  tapta_p4_full.yaml
```

Rule: với published baseline, chạy authors' config trước, common protocol sau. Không chỉnh baseline cho đến khi nó tốt rồi đem so với proposed method chạy config khác.

## Master experiment table

| ID | Date | Model | Dataset | Protocol | Memory | Seed | AA/F1 | Forget | Router Acc | Config | Result File | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E001 |  | Sequential FT | FewRel | 5-shot | 0 | 2021 |  |  | - |  |  | todo |
| E002 |  | Joint Training | FewRel | 5-shot | full | 2021 |  |  | - |  |  | todo |
| E003 |  | Prototype sanity | FewRel | 5-shot | 0/1 | 2021 |  |  | - |  |  | todo |
| E004 |  | ConPL | FewRel | 5-shot | 1 | 2021 |  |  | - |  |  | todo |
| E005 |  | P0 Shared Prompt | FewRel | 5-shot | 0/1 | 2021 |  |  | - |  |  | todo |

## Repository structure đề xuất

```text
thesis/
  data/
    raw/
    processed/
    task_orders/
  baselines/
    conpl/
    cpl/
    sckd/
    wave/
  src/
    models/
    prompts/
    router/
    prototypes/
    evaluation/
  configs/
  scripts/
  results/
    raw/
    aggregate/
    figures/
  paper_notes/
  weekly_reports/
  thesis/
```
