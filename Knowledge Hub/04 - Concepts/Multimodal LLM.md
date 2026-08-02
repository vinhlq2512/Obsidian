---
type: concept
status: seed
sources:
  - "[[Hands-On LLM - Chapter 09 - Multimodal Large Language Models]]"
tags:
  - concept
  - multimodal
  - llm
---

# Multimodal LLM

## Định nghĩa

Multimodal LLM là model hoặc hệ thống language model có thể xử lý nhiều dạng dữ liệu như text, image, audio, video hoặc table.

## Cách hiểu bằng lời của tôi

Model cần biến các modality khác nhau thành representation mà language model có thể hiểu hoặc kết nối chúng trong cùng embedding space.

## Cần biết

- CLIP học shared space giữa text và image.
- Vision Transformer chia ảnh thành patches như token.
- Multimodal chat nối visual input với text generation.
- Cần cảnh giác hallucination khi model mô tả ảnh hoặc tài liệu.

## Liên kết

- [[Embedding]]
- [[Contrastive Learning]]
- [[Generative Model]]

