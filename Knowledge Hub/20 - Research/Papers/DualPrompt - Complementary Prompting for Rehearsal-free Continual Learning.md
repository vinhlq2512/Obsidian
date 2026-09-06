---
type: paper
status: draft
title: "DualPrompt: Complementary Prompting for Rehearsal-free Continual Learning"
aliases:
  - DualPrompt
authors:
  - Zifeng Wang
  - Zizhao Zhang
  - Sayna Ebrahimi
  - Ruoxi Sun
  - Han Zhang
  - Chen-Yu Lee
  - Xiaoqi Ren
  - Guolong Su
  - Vincent Perot
  - Jennifer Dy
  - Tomas Pfister
year: 2022
venue: "ECCV 2022"
url: "https://arxiv.org/abs/2204.04799"
pdf:
doi: "10.48550/arXiv.2204.04799"
arxiv: "2204.04799v2"
code: "https://github.com/google-research/l2p"
topic:
  - continual learning
  - rehearsal-free learning
  - prompt learning
  - task-invariant prompt
  - task-specific prompt
priority: high
reading_status: not-started
related_concepts:
  - "[[Continual Learning]]"
  - "[[Prompt Pool]]"
  - "[[Catastrophic Forgetting]]"
created_at: 2026-09-05
updated_at: 2026-09-05
tags:
  - paper
  - continual-learning
  - prompting
---

# DualPrompt: Complementary Prompting for Rehearsal-free Continual Learning

## Tóm tắt một câu

DualPrompt tách prompt thành phần bổ trợ cho tri thức task-invariant và task-specific, nhằm học class-incremental continual learning mà không lưu replay buffer.

## Vì sao cần cho đề tài

Thiết kế Prompt Tree của đề tài đang có root/internal/leaf prompts. DualPrompt là paper cần đọc để biện minh rằng prompt có thể được phân vai:

- prompt chung giữ tri thức ổn định;
- prompt task-specific giữ tri thức riêng;
- sự kết hợp hai loại prompt có thể tốt hơn một prompt pool phẳng.

## Nguồn đã kiểm

- arXiv: [2204.04799](https://arxiv.org/abs/2204.04799)
- Code được paper trỏ tới repo L2P: [google-research/l2p](https://github.com/google-research/l2p)

## Ghi chú evidence

Metadata và vai trò paper hiện ở mức `source-checked` từ arXiv abstract; chưa đọc PDF sâu.

## Cần đọc tiếp

- G-Prompt và E-Prompt được đặt ở layer nào.
- Khi inference chọn prompt thế nào.
- So sánh với L2P về forgetting và plasticity.
