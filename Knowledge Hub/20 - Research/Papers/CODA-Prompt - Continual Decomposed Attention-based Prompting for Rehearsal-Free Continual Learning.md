---
type: paper
status: draft
title: "CODA-Prompt: COntinual Decomposed Attention-based Prompting for Rehearsal-Free Continual Learning"
aliases:
  - CODA-Prompt
authors:
  - James Seale Smith
  - Leonid Karlinsky
  - Vyshnavi Gutta
  - Paola Cascante-Bonilla
  - Donghyun Kim
  - Assaf Arbelle
  - Rameswar Panda
  - Rogerio Feris
  - Zsolt Kira
year: 2023
venue: "CVPR 2023"
url: "https://arxiv.org/abs/2211.13218"
pdf:
doi: "10.48550/arXiv.2211.13218"
arxiv: "2211.13218v2"
code: "https://github.com/GT-RIPL/CODA-Prompt"
topic:
  - continual learning
  - prompt composition
  - attention-based prompting
  - rehearsal-free learning
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

# CODA-Prompt: COntinual Decomposed Attention-based Prompting for Rehearsal-Free Continual Learning

## Tóm tắt một câu

CODA-Prompt học các prompt components và lắp ghép chúng bằng trọng số phụ thuộc input, thay vì chỉ chọn prompt bằng key-query cố định.

## Vì sao cần cho đề tài

Đề tài đang có bước **Compositional Prompt Generation**:

$$
P_{final} = \sum_j w_j P_{path_j}
$$

CODA-Prompt là paper gần nhất để biện minh cho prompt composition theo input-conditioned weights. Điểm khác biệt tiềm năng của đề tài là chuyển composition này sang **cây relation/task** trong Continual Relation Extraction.

## Nguồn đã kiểm

- arXiv: [2211.13218](https://arxiv.org/abs/2211.13218)
- Code: [GT-RIPL/CODA-Prompt](https://github.com/GT-RIPL/CODA-Prompt)

## Ghi chú evidence

Metadata và vai trò paper hiện ở mức `source-checked` từ arXiv abstract; chưa đọc PDF sâu.

## Cần đọc tiếp

- Cách decomposed prompts được tham số hóa.
- Attention/query-key có được train end-to-end không.
- Metric về plasticity-stability.
