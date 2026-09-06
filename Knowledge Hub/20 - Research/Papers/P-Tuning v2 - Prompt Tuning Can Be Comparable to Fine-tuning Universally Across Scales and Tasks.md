---
type: paper
status: draft
title: "P-Tuning v2: Prompt Tuning Can Be Comparable to Fine-tuning Universally Across Scales and Tasks"
aliases:
  - P-Tuning v2
authors:
  - Xiao Liu
  - Kaixuan Ji
  - Yicheng Fu
  - Weng Lam Tam
  - Zhengxiao Du
  - Zhilin Yang
  - Jie Tang
year: 2021
venue:
url: "https://arxiv.org/abs/2110.07602"
pdf:
doi: "10.48550/arXiv.2110.07602"
arxiv: "2110.07602"
code: "https://github.com/THUDM/P-tuning-v2"
topic:
  - prompt tuning
  - deep prompt tuning
  - natural language understanding
priority: medium
reading_status: not-started
related_concepts:
  - "[[Prompt Tuning]]"
  - "[[Prefix Tuning]]"
  - "[[Parameter-Efficient Fine-Tuning]]"
created_at: 2026-09-05
updated_at: 2026-09-05
tags:
  - paper
  - prompting
  - peft
---

# P-Tuning v2: Prompt Tuning Can Be Comparable to Fine-tuning Universally Across Scales and Tasks

## Tóm tắt một câu

P-Tuning v2 tối ưu deep prompt tuning cho NLU, cho thấy prompt tuning có thể cạnh tranh với fine-tuning trên nhiều model scale và task hơn các soft prompt đời đầu.

## Vì sao cần cho đề tài

Relation Extraction là NLU task, không phải generation task. Paper này giúp kiểm tra thiết kế prompt/prefix nào phù hợp hơn cho classification/sequence understanding.

## Nguồn đã kiểm

- arXiv: [2110.07602](https://arxiv.org/abs/2110.07602)
- Code: [THUDM/P-tuning-v2](https://github.com/THUDM/P-tuning-v2)

## Cần đọc tiếp

- Deep prompt tuning khác input soft prompt ở đâu.
- Thiết lập cho NLU/classification.
- Prompt tuning khi model cỡ BERT/RoBERTa có đủ mạnh không.
