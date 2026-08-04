---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 10 - Training Transformers from Scratch]]"
source_sections:
  - "[[NLP Transformers - Chapter 10 - Training Transformers from Scratch]]"
first_seen: 2026-08-04
last_updated: 2026-08-04
tags:
  - concept
  - pretraining
  - nlp
  - transformers
---

# Language Modeling

## Định nghĩa

`Language Modeling` là bài toán học cấu trúc xác suất của text để model dự đoán token tiếp theo hoặc phục hồi token bị che, tùy objective.

## Vai trò

- Là nền tảng của nhiều quy trình [[Pretraining]].
- Giúp model học thống kê, ngữ cảnh và quy luật của corpus trước khi làm downstream task.
- Tùy objective mà hành vi học sẽ khác, ví dụ [[Causal Language Model|causal language modeling]] và [[Masked Language Modeling]].

## Cần biết

- Language modeling không trực tiếp học label của task downstream.
- Loss language modeling giảm không đồng nghĩa downstream task chắc chắn tốt hơn.
- Chất lượng corpus ảnh hưởng rất mạnh tới những gì model hấp thụ được.

## Cách hiểu bằng lời của tôi

Language modeling là cách cho model “đọc thật nhiều để học cách ngôn ngữ vận hành” trước khi giao cho nó một nhiệm vụ cụ thể như phân loại, QA hay sinh tóm tắt.

## Liên kết

- [[Pretraining]]
- [[Masked Language Modeling]]
- [[Causal Language Model]]
- [[NLP Transformers - Chapter 10 - Training Transformers from Scratch]]
