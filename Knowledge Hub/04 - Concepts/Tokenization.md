---
type: concept
status: seed
source:
  - "[[Hands-On LLM - Chapter 02 - Tokens and Embeddings]]"
tags:
  - concept
  - llm
  - tokenization
---

# Tokenization

## Định nghĩa

Tokenization là quá trình chia text thành các token và ánh xạ chúng thành token IDs để language model xử lý.

## Cách hiểu bằng lời của tôi

Model không đọc chữ như con người. Tokenizer cắt text thành đơn vị nhỏ, biến chúng thành số, rồi embedding table biến số thành vector.

## Cần biết

- Token có thể là từ, mảnh từ, ký tự hoặc byte.
- Tokenizer khác nhau tạo số token khác nhau cho cùng một text.
- Token count ảnh hưởng chi phí, context window và latency.
- Special tokens có thể điều khiển sequence, padding, mask hoặc classification.

## Liên kết

- [[Embedding]]
- [[Large Language Model]]
- [[Transformer]]

