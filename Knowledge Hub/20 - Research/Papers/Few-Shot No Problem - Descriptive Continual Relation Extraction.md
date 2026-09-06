---
type: paper
status: draft
title: "Few-Shot, No Problem: Descriptive Continual Relation Extraction"
aliases:
  - DCRE
authors:
  - Nguyen Xuan Thanh
  - Anh Duc Le
  - Quyen Tran
  - Thanh-Thien Le
  - Linh Ngo Van
  - Thien Huu Nguyen
year: 2025
venue: "AAAI 2025"
url: "https://ojs.aaai.org/index.php/AAAI/article/view/34715"
pdf:
doi: "10.1609/aaai.v39i24.34715"
arxiv: "2502.20596"
code:
topic:
  - few-shot continual relation extraction
  - relation descriptions
  - retrieval inference
  - large language model embeddings
priority: medium
reading_status: not-started
related_concepts:
  - "[[Continual Few-Shot Relation Extraction]]"
  - "[[Relation Extraction]]"
  - "[[Data Augmentation]]"
created_at: 2026-09-05
updated_at: 2026-09-05
tags:
  - paper
  - continual-learning
  - relation-extraction
---

# Few-Shot, No Problem: Descriptive Continual Relation Extraction

## Tóm tắt một câu

DCRE dùng LLM-generated relation descriptions, bi-encoder retrieval training và reciprocal-rank-fusion inference để tăng representation cho FCRE.

## Vì sao cần cho kế hoạch

Paper này liên quan trực tiếp tới phần relation descriptions và semantic routing. Nên đọc trước khi quyết định có dùng LLM-generated descriptions trong Prompt Tree hay để phần đó thành stretch.

## Nguồn đã kiểm

- AAAI: [Few-Shot, No Problem](https://ojs.aaai.org/index.php/AAAI/article/view/34715)
- arXiv: [2502.20596](https://arxiv.org/abs/2502.20596)

## Cần đọc tiếp

- Relation description generation.
- Bi-encoder retrieval training.
- Retrieval-based prediction vs NCM/prototype classifier.
