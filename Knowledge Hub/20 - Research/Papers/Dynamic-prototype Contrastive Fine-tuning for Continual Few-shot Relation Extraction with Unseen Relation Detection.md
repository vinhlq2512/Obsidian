---
type: paper
status: draft
title: "Dynamic-prototype Contrastive Fine-tuning for Continual Few-shot Relation Extraction with Unseen Relation Detection"
aliases:
  - DPC-FT
authors:
  - Si Miao Zhao
  - Zhen Tan
  - Ning Pang
  - Wei Dong Xiao
  - Xiang Zhao
year: 2025
venue: "COLING 2025"
url: "https://aclanthology.org/2025.coling-main.586/"
pdf:
doi:
arxiv:
code:
topic:
  - continual few-shot relation extraction
  - dynamic prototypes
  - unseen relation detection
priority: medium
reading_status: not-started
related_concepts:
  - "[[Continual Few-Shot Relation Extraction]]"
  - "[[Prototype Learning]]"
  - "[[Task Identity Inference]]"
created_at: 2026-09-05
updated_at: 2026-09-05
tags:
  - paper
  - continual-learning
  - relation-extraction
---

# Dynamic-prototype Contrastive Fine-tuning for Continual Few-shot Relation Extraction with Unseen Relation Detection

## Tóm tắt một câu

DPC-FT thêm lightweight relation encoder theo task và dynamic prototype module để phân bổ memory khác nhau cho relation dễ/khó, đồng thời xét unseen relation detection.

## Vì sao cần cho kế hoạch

Đây là stretch comparator quan trọng cho phần dynamic prototype và open-set/NOTA. Không nên reproduce sớm, nhưng cần đọc trước khi chốt novelty của PrototypeMemory.

## Nguồn đã kiểm

- ACL Anthology: [2025.coling-main.586](https://aclanthology.org/2025.coling-main.586/)

## Cần đọc tiếp

- Dynamic prototype allocation.
- Task-specific lightweight relation encoder.
- Unseen relation threshold.
