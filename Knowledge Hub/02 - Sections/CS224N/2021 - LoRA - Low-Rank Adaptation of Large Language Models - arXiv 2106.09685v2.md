---
type: course-source
course: "[[CS224N]]"
status: developing
source_type: paper
title: "2021 - LoRA - Low-Rank Adaptation of Large Language Models"
year: 2021
venue: "arXiv"
arxiv: "2106.09685v2"
source_file: "[[2021 - LoRA - Low-Rank Adaptation of Large Language Models - arXiv 2106.09685v2.pdf]]"
pages: 26
created_at: 2026-08-02
updated_at: 2026-08-02
related_concepts:
  - "[[Large Language Model]]"
  - "[[Autoregressive Language Model]]"
  - "[[Parameter-Efficient Fine-Tuning]]"
tags:
  - cs224n
  - paper
---

# 2021 - LoRA - Low-Rank Adaptation of Large Language Models - arXiv 2106.09685v2

## Nguồn

- PDF gốc: [[2021 - LoRA - Low-Rank Adaptation of Large Language Models - arXiv 2106.09685v2.pdf]]
- Đọc cùng: [[CS224N 2026 - Lecture 09 - Efficient Adaptation]]
- Concept: [[Parameter-Efficient Fine-Tuning]]

## Vấn đề paper giải quyết

Full fine-tuning LLM rất tốn kém, đặc biệt khi phải deploy nhiều model/task-specific copies. LoRA hỏi: có thể giữ nguyên weight pretrained và chỉ học một update nhỏ hạng thấp không?

## Đóng góp chính

- Freeze pretrained weights.
- Inject trainable low-rank decomposition matrices vào Transformer layers.
- Giảm mạnh số tham số trainable và memory optimizer.
- Hỗ trợ lưu nhiều task adapters nhẹ hơn so với nhiều bản full fine-tuned model.

## Cơ chế

$$
W' = W + \Delta W, \quad \Delta W = BA
$$

Trong đó $B$ và $A$ có rank nhỏ hơn nhiều so với ma trận gốc.

## Vì sao quan trọng với CS224N

Lecture 09 dùng LoRA như ví dụ PEFT cốt lõi: adapt model lớn bằng một phần nhỏ tham số.

## Hạn chế / câu hỏi

- Rank quá thấp có thể thiếu capacity.
- Chọn layer nào để áp dụng LoRA là quyết định quan trọng.
- Không thay thế hoàn toàn full fine-tuning trong mọi domain/task.

## Câu hỏi review

1. LoRA freeze cái gì và train cái gì?
2. Vì sao low-rank update tiết kiệm tham số?
3. LoRA khác adapter bottleneck như thế nào?
