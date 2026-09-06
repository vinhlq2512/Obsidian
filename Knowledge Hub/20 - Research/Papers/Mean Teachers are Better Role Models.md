---
type: paper
status: draft
title: "Mean teachers are better role models: Weight-averaged consistency targets improve semi-supervised deep learning results"
aliases:
  - Mean Teacher
authors:
  - Antti Tarvainen
  - Harri Valpola
year: 2017
venue: "NeurIPS 2017"
url: "https://arxiv.org/abs/1703.01780"
pdf:
doi: "10.48550/arXiv.1703.01780"
arxiv: "1703.01780v6"
code:
topic:
  - exponential moving average
  - teacher student learning
  - consistency regularization
priority: medium
reading_status: not-started
related_concepts:
  - "[[Knowledge Distillation]]"
  - "[[Model Distillation]]"
  - "[[Continual Learning]]"
created_at: 2026-09-05
updated_at: 2026-09-05
tags:
  - paper
  - distillation
  - semi-supervised-learning
---

# Mean teachers are better role models

## Tóm tắt một câu

Mean Teacher dùng exponential moving average của trọng số Student để tạo Teacher ổn định hơn cho consistency targets.

## Vì sao cần cho đề tài

Phần EMA trong đề tài cần paper này để tránh trình bày EMA như một mẹo tùy tiện. Tuy nhiên, cần viết rõ rằng Mean Teacher gốc thuộc semi-supervised learning, còn đề tài dùng ý tưởng weight averaging cho continual distillation.

## Nguồn đã kiểm

- arXiv: [1703.01780](https://arxiv.org/abs/1703.01780)

## Ghi chú evidence

Metadata và vai trò paper hiện ở mức `source-checked` từ arXiv abstract; chưa đọc PDF sâu.

## Cần đọc tiếp

- Công thức EMA.
- Consistency target.
- Khác biệt giữa semi-supervised consistency và continual KD.
