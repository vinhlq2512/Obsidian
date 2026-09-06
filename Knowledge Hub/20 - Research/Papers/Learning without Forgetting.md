---
type: paper
status: draft
title: "Learning without Forgetting"
aliases:
  - LwF
authors:
  - Zhizhong Li
  - Derek Hoiem
year: 2016
venue: "ECCV 2016"
url: "https://arxiv.org/abs/1606.09282"
pdf:
doi: "10.48550/arXiv.1606.09282"
arxiv: "1606.09282v3"
code:
topic:
  - continual learning
  - knowledge distillation
  - no old data
priority: medium
reading_status: not-started
related_concepts:
  - "[[Continual Learning]]"
  - "[[Knowledge Distillation]]"
  - "[[Catastrophic Forgetting]]"
created_at: 2026-09-05
updated_at: 2026-09-05
tags:
  - paper
  - continual-learning
  - distillation
---

# Learning without Forgetting

## Tóm tắt một câu

LwF dùng output của mô hình cũ trên dữ liệu task mới làm tín hiệu distillation để học khả năng mới mà không cần dữ liệu task cũ.

## Vì sao cần cho đề tài

Student-Teacher KD trong đề tài là hậu duệ trực tiếp của LwF. Paper này giúp viết phần nền cho:

- vì sao Teacher chỉ biết old labels vẫn có ích;
- vì sao KD trên dữ liệu task mới có thể giữ old behavior;
- giới hạn của KD khi dữ liệu task mới không kích hoạt old decision boundary.

## Nguồn đã kiểm

- arXiv: [1606.09282](https://arxiv.org/abs/1606.09282)

## Ghi chú evidence

Metadata và vai trò paper hiện ở mức `source-checked` từ arXiv abstract; chưa đọc PDF sâu.

## Cần đọc tiếp

- Công thức distillation loss.
- Temperature và old/new heads.
- Khi nào LwF thất bại vì dữ liệu mới không đại diện dữ liệu cũ.
