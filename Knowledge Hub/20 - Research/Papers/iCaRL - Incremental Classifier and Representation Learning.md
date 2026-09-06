---
type: paper
status: draft
title: "iCaRL: Incremental Classifier and Representation Learning"
aliases:
  - iCaRL
authors:
  - Sylvestre-Alvise Rebuffi
  - Alexander Kolesnikov
  - Georg Sperl
  - Christoph H. Lampert
year: 2017
venue: "CVPR 2017"
url: "https://arxiv.org/abs/1611.07725"
pdf:
doi: "10.48550/arXiv.1611.07725"
arxiv: "1611.07725v2"
code:
topic:
  - class-incremental learning
  - exemplar memory
  - nearest-mean classifier
  - knowledge distillation
priority: medium
reading_status: not-started
related_concepts:
  - "[[Continual Learning]]"
  - "[[Prototype Learning]]"
  - "[[Knowledge Distillation]]"
  - "[[Replay in Continual Learning]]"
created_at: 2026-09-05
updated_at: 2026-09-05
tags:
  - paper
  - continual-learning
  - prototype-learning
---

# iCaRL: Incremental Classifier and Representation Learning

## Tóm tắt một câu

iCaRL là class-incremental baseline kinh điển kết hợp exemplar memory, nearest-mean-of-exemplars classifier và representation learning.

## Vì sao cần cho đề tài

PrototypeMemory và NCM/prototype classifier trong đề tài cần nền từ iCaRL, dù domain của iCaRL là vision. Nó giúp bảo vệ các quyết định:

- dùng mean/prototype làm classifier;
- chọn exemplar/prototype có budget;
- báo old/new class accuracy và forgetting.

## Nguồn đã kiểm

- arXiv: [1611.07725](https://arxiv.org/abs/1611.07725)

## Ghi chú evidence

Metadata và vai trò paper hiện ở mức `source-checked` từ arXiv abstract; chưa đọc PDF sâu.

## Cần đọc tiếp

- Exemplar selection/herding.
- Nearest-mean-of-exemplars.
- Distillation khi thêm class mới.
