---
type: paper
status: draft
title: "Serial Contrastive Knowledge Distillation for Continual Few-shot Relation Extraction"
aliases:
  - SCKD
authors:
  - Xinyi Wang
  - Zitao Wang
  - Wei Hu
year: 2023
venue: "Findings of ACL 2023"
url: "https://aclanthology.org/2023.findings-acl.804/"
pdf:
doi:
arxiv: "2305.06616"
code: "https://github.com/nju-websoft/SCKD"
topic:
  - continual few-shot relation extraction
  - knowledge distillation
  - contrastive learning
priority: high
reading_status: not-started
related_concepts:
  - "[[Continual Few-Shot Relation Extraction]]"
  - "[[Knowledge Distillation]]"
  - "[[Contrastive Learning]]"
created_at: 2026-09-05
updated_at: 2026-09-05
tags:
  - paper
  - continual-learning
  - relation-extraction
  - distillation
---

# Serial Contrastive Knowledge Distillation for Continual Few-shot Relation Extraction

## Tóm tắt một câu

SCKD dùng serial knowledge distillation để giữ knowledge từ các model trước và contrastive learning với pseudo samples để tách representation giữa các relation.

## Vì sao cần cho kế hoạch

Đây là baseline/đối chứng gần nhất cho phần KD trong đề tài. Nếu đề tài dùng Teacher-Student hoặc EMA Teacher, cần so với SCKD ở mức ý tưởng, và có thể reproduce nếu kịp.

## Nguồn đã kiểm

- ACL Anthology: [2023.findings-acl.804](https://aclanthology.org/2023.findings-acl.804/)
- arXiv: [2305.06616](https://arxiv.org/abs/2305.06616)
- Code: [nju-websoft/SCKD](https://github.com/nju-websoft/SCKD)

## Cần đọc tiếp

- Serial KD khác LwF ở đâu.
- Pseudo samples được tạo thế nào.
- Loss contrastive có thể reuse cho prototype router không.
