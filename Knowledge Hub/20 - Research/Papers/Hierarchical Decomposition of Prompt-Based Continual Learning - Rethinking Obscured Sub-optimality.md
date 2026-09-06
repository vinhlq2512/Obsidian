---
type: paper
status: draft
title: "Hierarchical Decomposition of Prompt-Based Continual Learning: Rethinking Obscured Sub-optimality"
aliases:
  - HiDe-Prompt
authors:
  - Liyuan Wang
  - Jingyi Xie
  - Xingxing Zhang
  - Mingyi Huang
  - Hang Su
  - Jun Zhu
year: 2023
venue: "NeurIPS 2023 Spotlight"
url: "https://arxiv.org/abs/2310.07234"
pdf:
doi: "10.48550/arXiv.2310.07234"
arxiv: "2310.07234v1"
code: "https://github.com/thu-ml/HiDe-Prompt"
topic:
  - continual learning
  - prompt learning
  - task identity inference
  - hierarchical decomposition
priority: high
reading_status: not-started
related_concepts:
  - "[[Continual Learning]]"
  - "[[Prompt Pool]]"
  - "[[Task Identity Inference]]"
created_at: 2026-09-05
updated_at: 2026-09-05
tags:
  - paper
  - continual-learning
  - prompting
---

# Hierarchical Decomposition of Prompt-Based Continual Learning: Rethinking Obscured Sub-optimality

## Tóm tắt một câu

HiDe-Prompt phân rã prompt-based continual learning thành within-task prediction, task-identity inference và task-adaptive prediction, rồi tối ưu các thành phần này rõ ràng hơn.

## Vì sao cần cho đề tài

Đây là paper rất quan trọng để bảo vệ chữ **Task-Aware** trong tên đề tài. Nó cung cấp ngôn ngữ lý thuyết để tách:

- lỗi phân biệt relation trong cùng task;
- lỗi suy luận task;
- lỗi dự đoán sau khi đã chọn prompt/task.

Đề tài nên dùng decomposition này làm khung đánh giá thay vì chỉ báo final accuracy.

## Nguồn đã kiểm

- arXiv: [2310.07234](https://arxiv.org/abs/2310.07234)
- Code: [thu-ml/HiDe-Prompt](https://github.com/thu-ml/HiDe-Prompt)

## Ghi chú evidence

Metadata và vai trò paper hiện ở mức `source-checked` từ arXiv abstract; chưa đọc PDF sâu.

## Cần đọc tiếp

- Định nghĩa WTP, TII, TAP trong paper.
- Cách dùng statistics của uninstructed/instructed representations.
- Các metric tách riêng task routing và prediction.
