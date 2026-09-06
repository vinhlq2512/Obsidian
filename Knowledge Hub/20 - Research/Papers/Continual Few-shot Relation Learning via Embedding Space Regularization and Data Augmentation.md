---
type: paper
status: draft
title: "Continual Few-shot Relation Learning via Embedding Space Regularization and Data Augmentation"
aliases:
  - ERDA
authors:
  - Chengwei Qin
  - Shafiq Joty
year: 2022
venue: "ACL 2022"
url: "https://aclanthology.org/2022.acl-long.198/"
pdf:
doi: "10.18653/v1/2022.acl-long.198"
arxiv: "2203.02135"
code: "https://github.com/qcwthu/Continual_Fewshot_Relation_Learning"
topic:
  - continual few-shot relation extraction
  - embedding space regularization
  - data augmentation
priority: high
reading_status: not-started
related_concepts:
  - "[[Continual Few-Shot Relation Extraction]]"
  - "[[Embedding Space Regularization]]"
  - "[[Data Augmentation]]"
created_at: 2026-09-05
updated_at: 2026-09-05
tags:
  - paper
  - continual-learning
  - relation-extraction
---

# Continual Few-shot Relation Learning via Embedding Space Regularization and Data Augmentation

## Tóm tắt một câu

ERDA formalize continual few-shot relation learning và dùng embedding-space regularization cùng data augmentation để giảm distribution incompatibility giữa task cũ và mới.

## Vì sao cần cho kế hoạch

Đây là mốc nền cho FCRE trước ConPL/CPL. Nếu muốn so protocol Legacy-FCRE và Strict all-few-shot, cần hiểu ERDA tạo task, dùng augmentation, và đánh giá như thế nào.

## Nguồn đã kiểm

- ACL Anthology: [2022.acl-long.198](https://aclanthology.org/2022.acl-long.198/)
- arXiv: [2203.02135](https://arxiv.org/abs/2203.02135)
- Code: [qcwthu/Continual_Fewshot_Relation_Learning](https://github.com/qcwthu/Continual_Fewshot_Relation_Learning)

## Cần đọc tiếp

- Protocol FCRE gốc.
- Embedding regularization loss.
- Augmentation pipeline và memory assumption.
