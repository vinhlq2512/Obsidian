---
type: paper
status: draft
title: "Dark Experience for General Continual Learning: a Strong, Simple Baseline"
aliases:
  - DER
  - Dark Experience Replay
authors:
  - Pietro Buzzega
  - Matteo Boschini
  - Angelo Porrello
  - Davide Abati
  - Simone Calderara
year: 2020
venue: "NeurIPS 2020"
url: "https://arxiv.org/abs/2004.07211"
pdf:
doi: "10.48550/arXiv.2004.07211"
arxiv: "2004.07211"
code: "https://github.com/aimagelab/mammoth"
topic:
  - continual learning
  - dark experience replay
  - knowledge distillation
  - task-free continual learning
priority: medium
reading_status: not-started
related_concepts:
  - "[[Continual Learning]]"
  - "[[Knowledge Distillation]]"
  - "[[Replay in Continual Learning]]"
  - "[[Catastrophic Forgetting]]"
created_at: 2026-09-05
updated_at: 2026-09-05
tags:
  - paper
  - continual-learning
  - distillation
---

# Dark Experience for General Continual Learning

## Tóm tắt một câu

DER lưu lại logits trong quá trình học và dùng chúng như dark knowledge để regularize model khi học liên tục.

## Vì sao cần cho đề tài

Nếu muốn hiểu Teacher-Student/KD trong continual learning, DER là cầu nối tốt giữa distillation cổ điển và chống quên. Nó cũng giúp phân biệt:

- distill từ Teacher hiện tại;
- distill từ logits/history lưu trong memory;
- replay dữ liệu thô so với replay hành vi dự đoán.

## Nguồn đã kiểm

- arXiv: [2004.07211](https://arxiv.org/abs/2004.07211)
- Code framework thường dùng: [aimagelab/mammoth](https://github.com/aimagelab/mammoth)

## Cần đọc tiếp

- Dark Experience Replay và DER++ khác nhau ở đâu.
- Vì sao paper nhấn vào General Continual Learning.
- Cách logit matching liên quan tới Knowledge Distillation.
