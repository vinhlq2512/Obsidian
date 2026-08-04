---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 11 - Future Directions]]"
source_sections:
  - "[[NLP Transformers - Chapter 11 - Future Directions]]"
first_seen: 2026-08-04
last_updated: 2026-08-04
tags:
  - concept
  - transformer
  - vision
  - multimodal
---

# Vision Transformer

## Định nghĩa

`Vision Transformer` là hướng áp dụng kiến trúc Transformer cho ảnh bằng cách biểu diễn ảnh thành một sequence các patch embeddings.

## Ý chính

- Ý tưởng cốt lõi là: nếu ảnh được chia thành các patch và mỗi patch được embed thành token, attention có thể xử lý chúng như sequence.
- Điều này cho thấy Transformer không chỉ dành cho text.
- Vision Transformer là một bước quan trọng mở đường cho các kiến trúc đa modality.

## Cách hiểu bằng lời của tôi

Vision Transformer biến ảnh thành “câu gồm các patch”. Khi đã đổi ảnh sang dạng sequence, attention có thể học quan hệ giữa các vùng ảnh giống như học quan hệ giữa các token trong câu.

## Liên kết

- [[Transformer]]
- [[Multimodal Transformer]]
- [[NLP Transformers - Chapter 11 - Future Directions]]
