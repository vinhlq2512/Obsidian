---
type: question
status: open
concepts:
  - "[[Positional Embeddings]]"
  - "[[Transformer]]"
sources:
  - "[[27-07-2026]]"
  - "[[Positional Embeddings]]"
created_at: 2026-08-02
updated_at: 2026-08-02
tags:
  - question
  - transformer
---

# How Do Positional Embeddings Scale Context Length

## Tôi đang thắc mắc gì?

- Absolute positional embeddings, relative positional embeddings và RoPE khác nhau thế nào khi mở rộng context length?

## Vì sao câu hỏi này quan trọng?

- Context length là giới hạn thực tế lớn của Transformer/LLM.
- Cách mã hóa vị trí ảnh hưởng khả năng model xử lý sequence dài hơn lúc train.

## Giải thích hiện tại

- [[Positional Embeddings]] giải thích vì sao Transformer cần thông tin thứ tự và có nhắc absolute/relative embeddings.
- Note hiện tại chưa tổng hợp rõ trade-off khi mở rộng context length.

## Cần kiểm tra thêm

- Absolute positional embeddings gặp hạn chế gì khi sequence dài hơn lúc train?
- Relative positional embeddings và RoPE giải quyết phần nào của vấn đề này?
- Khi fine-tune hoặc inference với context dài, cần chú ý gì?

## Source evidence

- [[27-07-2026]]
- [[Positional Embeddings]]

## Related

- [[Transformers]]

