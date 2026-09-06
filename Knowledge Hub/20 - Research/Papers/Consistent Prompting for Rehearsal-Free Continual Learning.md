---
type: paper
status: draft
title: "Consistent Prompting for Rehearsal-Free Continual Learning"
aliases:
  - CPrompt
authors:
  - Zhanxin Gao
  - Jun Cen
  - Xiaobin Chang
year: 2024
venue:
url: "https://arxiv.org/abs/2403.08568"
pdf:
doi: "10.48550/arXiv.2403.08568"
arxiv: "2403.08568"
code:
topic:
  - continual learning
  - prompt consistency
  - train-test mismatch
priority: high
reading_status: not-started
related_concepts:
  - "[[Continual Learning]]"
  - "[[Prompt Pool]]"
  - "[[Task Identity Inference]]"
created_at: 2026-09-05
updated_at: 2026-09-05
tags:
  - paper
  - continual-learning
  - prompting
---

# Consistent Prompting for Rehearsal-Free Continual Learning

## Tóm tắt một câu

CPrompt chỉ ra prompt-based continual learning có thể bị lệch giữa train và test do classifier inconsistency và prompt inconsistency, rồi thêm objective để căn chỉnh hai pha này.

## Vì sao cần cho đề tài

Đề tài có soft routing và prompt selection tại inference. CPrompt giúp đặt câu hỏi phản biện rất quan trọng: prompt được chọn khi test có khớp prompt được tối ưu khi train không?

## Nguồn đã kiểm

- arXiv: [2403.08568](https://arxiv.org/abs/2403.08568)

## Cần đọc tiếp

- Classifier consistency learning.
- Prompt consistency learning.
- Cách đo prompt selection accuracy.
