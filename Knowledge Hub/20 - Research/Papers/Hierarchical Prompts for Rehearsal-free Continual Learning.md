---
type: paper
status: draft
title: "Hierarchical Prompts for Rehearsal-free Continual Learning"
aliases:
  - H-Prompts
authors:
  - Yukun Zuo
  - Hantao Yao
  - Lu Yu
  - Liansheng Zhuang
  - Changsheng Xu
year: 2024
venue:
url: "https://arxiv.org/abs/2401.11544"
pdf:
doi: "10.48550/arXiv.2401.11544"
arxiv: "2401.11544"
code:
topic:
  - continual learning
  - hierarchical prompts
  - rehearsal-free learning
  - prompt distribution
priority: high
reading_status: not-started
related_concepts:
  - "[[Continual Learning]]"
  - "[[Prompt Pool]]"
  - "[[Prototype Learning]]"
created_at: 2026-09-05
updated_at: 2026-09-05
tags:
  - paper
  - continual-learning
  - prompting
---

# Hierarchical Prompts for Rehearsal-free Continual Learning

## Tóm tắt một câu

H-Prompts tổ chức prompt thành class prompt, task prompt và general prompt để giữ tri thức lớp cũ, tri thức task và tri thức tổng quát.

## Vì sao cần cho đề tài

Đề tài có Prompt Tree root-internal-leaf. H-Prompts là paper cần đọc để tránh claim rằng hierarchy prompt là hoàn toàn mới. Novelty nên được viết hẹp hơn:

- áp dụng hierarchy prompt vào Continual Relation Extraction;
- dùng prototype-guided soft routing theo relation/task tree;
- kết hợp với EMA Teacher/KD trong setting CRE.

## Nguồn đã kiểm

- arXiv: [2401.11544](https://arxiv.org/abs/2401.11544)

## Ghi chú evidence

Metadata và vai trò paper hiện ở mức `source-checked` từ arXiv abstract/html; chưa đọc PDF sâu.

## Cần đọc tiếp

- Class prompt có phải một dạng distribution/prototype memory không.
- Cross-task Knowledge Excavation liên quan thế nào tới KD/replay.
- Task identity có được cung cấp tại inference không.
