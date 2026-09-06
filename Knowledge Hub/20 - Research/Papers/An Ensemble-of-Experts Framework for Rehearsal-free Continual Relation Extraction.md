---
type: paper
status: draft
title: "An Ensemble-of-Experts Framework for Rehearsal-free Continual Relation Extraction"
aliases:
  - EoE
authors:
  - Shen Zhou
  - Yongqi Li
  - Xin Miao
  - Tieyun Qian
year: 2024
venue: "Findings of ACL 2024"
url: "https://aclanthology.org/2024.findings-acl.83/"
pdf:
doi: "10.18653/v1/2024.findings-acl.83"
arxiv:
code:
topic:
  - continual relation extraction
  - rehearsal-free learning
  - ensemble of experts
  - task identification
priority: high
reading_status: not-started
related_concepts:
  - "[[Continual Relation Extraction]]"
  - "[[Task Identity Inference]]"
  - "[[Replay in Continual Learning]]"
created_at: 2026-09-05
updated_at: 2026-09-05
tags:
  - paper
  - continual-learning
  - relation-extraction
---

# An Ensemble-of-Experts Framework for Rehearsal-free Continual Relation Extraction

## Tóm tắt một câu

EoE là paper CRE rehearsal-free chia bài toán thành task identification và within-task prediction, rồi dùng ensemble/cascade voting để gom năng lực nhiều experts.

## Vì sao cần cho đề tài

Đây là paper trực tiếp trong Continual Relation Extraction và nằm sát phần **task-aware / task-agnostic inference** của đề tài. Nếu đề tài muốn claim giảm lỗi routing hoặc giảm số forward pass so với cascade voting, EoE là baseline bắt buộc.

## Nguồn đã kiểm

- ACL Anthology: [2024.findings-acl.83](https://aclanthology.org/2024.findings-acl.83/)
- DOI: [10.18653/v1/2024.findings-acl.83](https://doi.org/10.18653/v1/2024.findings-acl.83)

## Ghi chú evidence

Metadata và mô tả hiện ở mức `source-checked` từ ACL Anthology; chưa đọc PDF sâu.

## Cần đọc tiếp

- Expert training và analogous-relation augmentation.
- Cascade voting.
- Cách paper đo task identification và within-task prediction.
