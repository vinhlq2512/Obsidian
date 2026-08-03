---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2023 - Scaling Autoregressive Multi-Modal Models - Pretraining and Instruction Tuning"
year: 2023
venue: "arXiv"
arxiv: "2309.02591v1"
source_file: "[[2023 - Scaling Autoregressive Multi-Modal Models - Pretraining and Instruction Tuning - arXiv 2309.02591v1.pdf]]"
pages: 19
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Transfer Learning]]"
  - "[[Large Language Model]]"
  - "[[Fine-tuning]]"
  - "[[RLHF]]"
tags:
  - cs224n
  - paper
---

# 2023 - Scaling Autoregressive Multi-Modal Models - Pretraining and Instruction Tuning - arXiv 2309.02591v1

## Nguồn

- PDF gốc: [[2023 - Scaling Autoregressive Multi-Modal Models - Pretraining and Instruction Tuning - arXiv 2309.02591v1.pdf]]
- Vai trò trong CS224N: paper về scaling autoregressive multimodal models qua pretraining và instruction tuning.

## Câu hỏi trung tâm

Autoregressive models có thể scale để vừa hiểu vừa sinh nội dung multimodal như thế nào?

## Kiến thức cốt lõi

- Paper trình bày hướng autoregressive mixed/multimodal model.
- Pretraining học phân phối dữ liệu đa phương thức ở scale lớn.
- Instruction tuning giúp model multimodal làm theo prompt tốt hơn.
- Multimodal generation đòi hỏi biểu diễn text-image nhất quán và data mixture cẩn thận.
- Nằm trong trục nối LLM với multimodal generation.

## Cơ chế / công thức / kiến trúc

```text
text/image multimodal data
-> tokenization/representation chung hoặc phối hợp
-> autoregressive pretraining
-> instruction tuning
-> zero-shot / prompted multimodal generation
```

## Khi áp dụng

- Dùng khi đọc Chameleon/Transfusion/Llama multimodal papers.
- Cần chú ý modality tokenization và objective.
- Instruction tuning multimodal phải xử lý cả intent ngôn ngữ lẫn output visual.

## Kết quả / bằng chứng đáng giữ

- First page nêu Scaling Autoregressive Multi-Modal Models: Pretraining and Instruction Tuning.
- Source showcase zero-shot generations và entities khó như text/hands.
- Paper thuộc cụm FAIR multimodal trong CS224N sources.

## Cách hiểu bằng lời của tôi

Multimodal autoregressive model cố dùng cùng trực giác “next token” cho nhiều loại tín hiệu hơn text, nhưng token và objective cho ảnh phức tạp hơn nhiều.

## Câu hỏi review

1. Autoregressive multimodal model sinh gì theo thứ tự?
2. Instruction tuning trong multimodal khác text-only ở đâu?
3. Vì sao data mixture quan trọng?

## Liên kết

- [[Multimodal LLM]]
- [[Autoregressive Language Model]]
- [[Instruction Fine-Tuning]]
- [[CS224N]]
