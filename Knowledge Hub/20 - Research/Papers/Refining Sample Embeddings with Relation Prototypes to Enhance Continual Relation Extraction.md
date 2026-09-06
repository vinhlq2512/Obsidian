---
type: paper
status: draft
title: "Refining Sample Embeddings with Relation Prototypes to Enhance Continual Relation Extraction"
aliases:
  - RP-CRE
authors:
  - Li Cui
  - Deqing Yang
  - Jiaxin Yu
  - Chengwei Hu
  - Jiancheng Cheng
  - Jingjie Yi
  - Yanghua Xiao
year: 2021
venue: "ACL-IJCNLP 2021"
url: "https://aclanthology.org/2021.acl-long.20/"
pdf:
doi: "10.18653/v1/2021.acl-long.20"
arxiv:
code:
topic:
  - continual relation extraction
  - relation prototypes
  - memory network
priority: medium
reading_status: not-started
related_concepts:
  - "[[Continual Relation Extraction]]"
  - "[[Prototype Learning]]"
  - "[[Replay in Continual Learning]]"
created_at: 2026-09-05
updated_at: 2026-09-05
tags:
  - paper
  - continual-learning
  - relation-extraction
---

# Refining Sample Embeddings with Relation Prototypes to Enhance Continual Relation Extraction

## Tóm tắt một câu

RP-CRE dùng relation prototypes tính từ memorized samples để re-initialize memory network và refine sample embeddings qua các learning stage.

## Vì sao cần cho kế hoạch

Prototype không phải contribution mới trong CRE. Paper này giúp đề tài định vị novelty: không phải “dùng prototype”, mà là dùng prototype để tổ chức và route prompt theo task/relation hierarchy.

## Nguồn đã kiểm

- ACL Anthology: [2021.acl-long.20](https://aclanthology.org/2021.acl-long.20/)

## Cần đọc tiếp

- K-means memory sample selection.
- Prototype-based memory network.
- Relation embedding refinement.
