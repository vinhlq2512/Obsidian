---
type: paper
status: draft
title: "Sentence Embedding Alignment for Lifelong Relation Extraction"
authors:
  - Hong Wang
  - Wenhan Xiong
  - Mo Yu
  - Xiaoxiao Guo
  - Shiyu Chang
  - William Yang Wang
year: 2019
venue: "NAACL 2019"
url: "https://aclanthology.org/N19-1086/"
pdf:
doi: "10.18653/v1/N19-1086"
arxiv: "1903.02588"
code:
topic:
  - lifelong relation extraction
  - sentence embedding alignment
  - catastrophic forgetting
priority: medium
reading_status: not-started
related_concepts:
  - "[[Continual Relation Extraction]]"
  - "[[Embedding Space Regularization]]"
  - "[[Catastrophic Forgetting]]"
created_at: 2026-09-05
updated_at: 2026-09-05
tags:
  - paper
  - continual-learning
  - relation-extraction
---

# Sentence Embedding Alignment for Lifelong Relation Extraction

## Tóm tắt một câu

Paper nền của lifelong/continual relation extraction, dùng alignment model để giảm distortion trong sentence embedding space khi học relation mới.

## Vì sao cần cho kế hoạch

Đọc để hiểu lịch sử trước prototype/prompt: forgetting trong CRE ban đầu được mô tả như embedding distortion và memory-efficient incremental learning.

## Nguồn đã kiểm

- ACL Anthology: [N19-1086](https://aclanthology.org/N19-1086/)
- arXiv: [1903.02588](https://arxiv.org/abs/1903.02588)

## Cần đọc tiếp

- Lifelong RE formulation.
- Alignment loss.
- Replay memory trong baseline.
