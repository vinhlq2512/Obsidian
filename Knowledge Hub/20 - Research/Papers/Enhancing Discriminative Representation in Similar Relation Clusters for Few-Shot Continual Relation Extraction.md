---
type: paper
status: draft
title: "Enhancing Discriminative Representation in Similar Relation Clusters for Few-Shot Continual Relation Extraction"
aliases:
  - SIRUS
authors:
  - Anh Duc Le
  - Nam Le Hai
  - Thanh Xuan Nguyen
  - Linh Ngo Van
  - Nguyen Thi Ngoc Diep
  - Sang Dinh
  - Thien Huu Nguyen
year: 2025
venue: "NAACL 2025"
url: "https://aclanthology.org/2025.naacl-long.123/"
pdf:
doi: "10.18653/v1/2025.naacl-long.123"
arxiv:
code:
topic:
  - few-shot continual relation extraction
  - similar relation clusters
  - relation descriptions
priority: high
reading_status: not-started
related_concepts:
  - "[[Continual Few-Shot Relation Extraction]]"
  - "[[Relation Extraction]]"
  - "[[Contrastive Learning]]"
created_at: 2026-09-05
updated_at: 2026-09-05
tags:
  - paper
  - continual-learning
  - relation-extraction
---

# Enhancing Discriminative Representation in Similar Relation Clusters for Few-Shot Continual Relation Extraction

## Tóm tắt một câu

SIRUS dùng relation descriptions và dynamic clustering để nhận diện các relation tương tự nhau, rồi thiết kế loss giúp phân biệt tốt hơn các relation dễ nhầm.

## Vì sao cần cho kế hoạch

Đây là paper rất sát hypothesis `semantic/prototype hierarchy`. Nó giúp biến câu hỏi “hierarchy có ích không?” thành thí nghiệm trên similar-relation clusters, không chỉ đo average accuracy.

## Nguồn đã kiểm

- ACL Anthology: [2025.naacl-long.123](https://aclanthology.org/2025.naacl-long.123/)

## Cần đọc tiếp

- Cách tạo relation description clusters.
- Loss phân biệt similar relations.
- Cách đánh giá riêng trên analogous/similar relations.
