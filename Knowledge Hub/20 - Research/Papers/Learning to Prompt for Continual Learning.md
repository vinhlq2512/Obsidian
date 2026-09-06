---
type: paper
status: draft
title: "Learning to Prompt for Continual Learning"
aliases:
  - L2P
authors:
  - Zifeng Wang
  - Zizhao Zhang
  - Chen-Yu Lee
  - Han Zhang
  - Ruoxi Sun
  - Xiaoqi Ren
  - Guolong Su
  - Vincent Perot
  - Jennifer Dy
  - Tomas Pfister
year: 2022
venue: "CVPR 2022"
url: "https://arxiv.org/abs/2112.08654"
pdf:
doi: "10.48550/arXiv.2112.08654"
arxiv: "2112.08654v2"
code: "https://github.com/google-research/l2p"
topic:
  - continual learning
  - prompt learning
  - prompt pool
  - task-agnostic inference
priority: high
reading_status: not-started
related_concepts:
  - "[[Continual Learning]]"
  - "[[Prompt Pool]]"
  - "[[Task Identity Inference]]"
  - "[[Catastrophic Forgetting]]"
created_at: 2026-09-05
updated_at: 2026-09-05
tags:
  - paper
  - continual-learning
  - prompting
---

# Learning to Prompt for Continual Learning

## Tóm tắt một câu

L2P đề xuất học một prompt pool nhỏ cho continual learning, dùng key-query retrieval để chọn prompt theo input mà không cần task identity tại test time.

## Vì sao cần cho đề tài

Đây là paper nền trực tiếp cho ý tưởng **task-agnostic prompt selection**. Đề tài [[30 - Projects/Research Projects/Continual Relation Extraction with Task-Aware Prompt Adaptation/Continual Relation Extraction with Task-Aware Prompt Adaptation]] nên đọc L2P để xác định:

- prompt memory khác replay memory ở đâu;
- query-key prompt selection được train thế nào;
- claim không cần task identity tại inference được operationalize ra sao;
- hạn chế của flat prompt pool trước khi chuyển sang Prompt Tree.

## Nguồn đã kiểm

- arXiv: [2112.08654](https://arxiv.org/abs/2112.08654)
- Code: [google-research/l2p](https://github.com/google-research/l2p)

## Ghi chú evidence

Metadata và mô tả hiện ở mức `source-checked` từ arXiv abstract; chưa đọc PDF sâu.

## Cần đọc tiếp

- Cơ chế key-query selection.
- Loss cho prompt keys.
- Task-agnostic inference protocol.
- Cách tính memory/parameter budget.
