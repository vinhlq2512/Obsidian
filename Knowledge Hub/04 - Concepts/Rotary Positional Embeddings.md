---
type: concept
status: developing
sources:
  - "[[2021 - RoFormer - Enhanced Transformer with Rotary Position Embedding - arXiv 2104.09864v5]]"
source_sections:
  - "[[2021 - RoFormer - Enhanced Transformer with Rotary Position Embedding - arXiv 2104.09864v5]]"
first_seen: 2026-08-03
last_updated: 2026-08-03
tags:
  - concept
  - transformer
  - cs224n
---

# Rotary Positional Embeddings

## Định nghĩa

Rotary Positional Embeddings, hay RoPE, mã hoá vị trí bằng cách xoay query/key vectors trong không gian vector theo vị trí token.

## Cách hiểu bằng lời của tôi

RoPE không cộng thêm một vector vị trí vào embedding. Nó đưa vị trí vào hình học của attention: query và key bị xoay theo vị trí, nên dot product giữa chúng chứa thông tin khoảng cách tương đối.

## Cần biết

- RoPE thường áp dụng lên $Q$ và $K$, không phải trọng tâm ở $V$.
- Rất phổ biến trong nhiều decoder-only LLM hiện đại.
- Các kỹ thuật mở rộng context thường phải xử lý hoặc điều chỉnh RoPE.

## Liên kết

- [[Positional Embeddings]]
- [[Self-Attention]]
- [[Transformer]]
- [[CS224N]]
