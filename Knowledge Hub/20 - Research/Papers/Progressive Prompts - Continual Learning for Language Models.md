---
type: paper
status: draft
title: "Progressive Prompts: Continual Learning for Language Models"
aliases:
  - Progressive Prompts
authors:
  - Anastasia Razdaibiedina
  - Yuning Mao
  - Rui Hou
  - Madian Khabsa
  - Mike Lewis
  - Amjad Almahairi
year: 2023
venue: "ICLR 2023"
url: "https://arxiv.org/abs/2301.12314"
pdf:
doi: "10.48550/arXiv.2301.12314"
arxiv: "2301.12314"
code:
topic:
  - continual learning
  - language models
  - prompt tuning
priority: medium
reading_status: not-started
related_concepts:
  - "[[Continual Learning]]"
  - "[[Prompt Tuning]]"
  - "[[Prompt Pool]]"
created_at: 2026-09-05
updated_at: 2026-09-05
tags:
  - paper
  - continual-learning
  - prompting
---

# Progressive Prompts: Continual Learning for Language Models

## Tóm tắt một câu

Progressive Prompts học prompt mới cho từng task và nối với prompt cũ để hỗ trợ forward transfer mà không replay dữ liệu cũ.

## Vì sao cần cho kế hoạch

Đây là paper nền cho câu hỏi: prompt cũ nên freeze, reuse, concatenate hay compose? Nó hỗ trợ thiết kế Prompt Tree nhưng không phải baseline CRE trực tiếp.

## Nguồn đã kiểm

- arXiv: [2301.12314](https://arxiv.org/abs/2301.12314)

## Cần đọc tiếp

- Prompt concatenation qua task.
- Forgetting khi prompt list dài dần.
- Khả năng forward transfer.
