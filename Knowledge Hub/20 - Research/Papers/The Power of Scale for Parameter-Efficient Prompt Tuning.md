---
type: paper
status: draft
title: "The Power of Scale for Parameter-Efficient Prompt Tuning"
aliases:
  - Prompt Tuning
authors:
  - Brian Lester
  - Rami Al-Rfou
  - Noah Constant
year: 2021
venue: "EMNLP 2021"
url: "https://arxiv.org/abs/2104.08691"
pdf:
doi: "10.48550/arXiv.2104.08691"
arxiv: "2104.08691"
code:
topic:
  - prompt tuning
  - parameter-efficient tuning
  - frozen language models
priority: high
reading_status: not-started
related_concepts:
  - "[[Prompt Tuning]]"
  - "[[Parameter-Efficient Fine-Tuning]]"
created_at: 2026-09-05
updated_at: 2026-09-05
tags:
  - paper
  - prompting
  - peft
---

# The Power of Scale for Parameter-Efficient Prompt Tuning

## Tóm tắt một câu

Paper khảo sát soft prompt tuning, trong đó chỉ các prompt embeddings được học bằng backpropagation còn language model giữ frozen.

## Vì sao cần cho đề tài

Đề tài dùng “tinh chỉnh prompt” nhưng người đọc có thể nhầm với prompt engineering thủ công. Paper này giúp tách:

- discrete prompt viết bằng chữ;
- soft prompt/prefix là tham số học được;
- frozen backbone và trainable prompt parameters.

## Nguồn đã kiểm

- arXiv: [2104.08691](https://arxiv.org/abs/2104.08691)

## Cần đọc tiếp

- Prompt length và initialization.
- Vì sao prompt tuning mạnh hơn khi model lớn.
- Robustness/domain transfer khi dùng frozen model.
