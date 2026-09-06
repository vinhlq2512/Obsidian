---
type: project-tracker
status: active
project: "[[30 - Projects/Research Projects/Continual Relation Extraction with Task-Aware Prompt Adaptation/Continual Relation Extraction with Task-Aware Prompt Adaptation]]"
created_at: 2026-09-05
updated_at: 2026-09-05
tags:
  - weekly-tracker
  - research-project
  - continual-learning
  - relation-extraction
---

# Weekly Tracker

## Gate hiện tại: W4

**Deadline:** 2026-09-05

**Mục tiêu:** biến bốn paper đã đọc thành foundation có thể triển khai: research matrix, RQ, protocol và danh sách artifact tuần sau.

### Checklist

- [x] Tóm tắt bốn paper đã đọc vào một bảng: problem, method, memory, task inference, limitation.
- [x] Chốt formulation: class-incremental CRE/FCRE, không có oracle task ID lúc inference.
- [x] Chốt RQ-A đến RQ-D trong [[30 - Projects/Research Projects/Continual Relation Extraction with Task-Aware Prompt Adaptation/Literature Matrix v1, RQ và Protocol Spec]].
- [x] Lập danh sách metric và task split dự kiến.
- [ ] Kiểm tra FewRel download/access và format.
- [ ] Kiểm tra TACRED access/preprocessing requirement.
- [ ] Tạo skeleton repo/code hoặc xác định repo đang dùng.
- [ ] Tạo task-order file format dự kiến.
- [ ] Viết weekly report 1 trang.

### Artifact đã tạo

- [[30 - Projects/Research Projects/Continual Relation Extraction with Task-Aware Prompt Adaptation/Literature Matrix v1, RQ và Protocol Spec]]

## Tuần W5-W6

**Thời gian:** 2026-09-06 đến 2026-09-20

**Mục tiêu:** dataset pipeline và evaluator.

### Checklist

- [ ] FewRel loader.
- [ ] TACRED loader hoặc access decision.
- [ ] Script tạo task order cố định theo seed.
- [ ] Performance matrix `A_t,j`.
- [ ] Hàm tính Final AA/Macro-F1, AIA, Forgetting, BWT.
- [ ] Dummy prediction test cho evaluator.
- [ ] Lưu output mẫu vào `results/`.

### Artifact cuối tuần

- `common_fewrel_5shot.yaml`.
- `common_tacred_5shot.yaml` hoặc TACRED access note.
- `evaluate.py` chạy được với dummy predictions.

## Tuần W7-W8

**Thời gian:** 2026-09-28 đến 2026-10-11

**Mục tiêu:** lower/upper baselines.

### Checklist

- [ ] Sequential FT 1 seed trên FewRel.
- [ ] Joint Training reference 1 seed trên FewRel.
- [ ] Frozen BERT + linear head.
- [ ] Nearest prototype sanity baseline.
- [ ] Plot accuracy over tasks.
- [ ] Plot forgetting over tasks.

### Artifact cuối tuần

- Baseline table v0.
- 2 plots đầu tiên.
- Ghi rõ known bugs/mismatch.

## Tuần W9-W11

**Thời gian:** 2026-10-12 đến 2026-11-01

**Mục tiêu:** ConPL/CPL reproduction tối thiểu.

### Checklist

- [ ] Clone/check ConPL environment.
- [ ] Chạy ConPL original config 1 seed.
- [ ] Ghi discrepancy với paper nếu có.
- [ ] Clone/check CPL environment.
- [ ] Chạy CPL original config 1 seed.
- [ ] Quyết định có chuyển sang common protocol được không.

### Artifact cuối tuần

- ConPL/CPL reproduction log.
- Baseline table v1.
- Decision: baseline nào đủ tin để so sánh.

## Tuần W12-W13

**Thời gian:** 2026-11-02 đến 2026-11-15

**Mục tiêu:** closest prompt/task-aware comparator.

### Checklist

- [ ] Check WAVE-CRE/WAVE++ repo.
- [ ] Nếu repo khó chạy, kiểm tra EoE làm comparator.
- [ ] Chạy smoke run 1 seed hoặc ghi reproduction blocker có evidence.
- [ ] Freeze baseline protocol v1.

### Artifact cuối tuần

- Closest comparator smoke result hoặc blocker report.
- Baseline protocol freeze v1.

## Tuần W14-W20

**Thời gian:** 2026-11-16 đến 2027-01-03

**Mục tiêu:** triển khai proposed method đến architecture freeze.

### Checklist

- [ ] P0 shared prompt.
- [ ] P1 oracle-task prompt.
- [ ] P2 learned router.
- [ ] P3 prototype router.
- [ ] P4 TAPTA minimal.
- [ ] Ablation tree vs flat.
- [ ] Ablation hard vs soft routing.
- [ ] Ablation no KD vs KD.
- [ ] Design decision memo.
- [ ] Architecture freeze vào 2027-01-03.

## Tuần W21-W30

**Thời gian:** 2027-01-04 đến 2027-03-07

**Mục tiêu:** full experiments, ablation và result freeze.

### Checklist

- [ ] FewRel finalists 3 seeds.
- [ ] TACRED finalists 3 seeds.
- [ ] 5 seeds cho model chính nếu compute đủ.
- [ ] Router accuracy analysis.
- [ ] Similar-relation error analysis.
- [ ] Memory/latency table.
- [ ] Final results table.
- [ ] Result freeze vào 2027-03-07.

## Tuần W31-W38

**Thời gian:** 2027-03-08 đến 2027-04-30

**Mục tiêu:** viết, sửa, đóng gói.

### Checklist

- [ ] Chương Introduction.
- [ ] Chương Related Work.
- [ ] Chương Method.
- [ ] Chương Experiments.
- [ ] Chương Results/Discussion.
- [ ] Appendix.
- [ ] Reproducibility package.
- [ ] Slide/demo nếu cần.

## Weekly report template

```markdown
# Week XX - YYYY-MM-DD

## Research Question

## Last Week Commitments
- [ ] ...

## Completed
Task:
Evidence:
Commit:
Config:
Result file:

## Experiments
| Exp ID | Hypothesis | Dataset | Seed | Config | Result | Status |
|---|---|---|---|---|---|---|

## Papers Read
| Paper | Core Idea | Relation to My Work | Decision |
|---|---|---|---|

## Key Finding

## Failed / Negative Results

## Blockers

## Next Week
Expected artifact:
Success/failure criterion:
```
