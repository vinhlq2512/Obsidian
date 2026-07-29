---
type: concept
status: seed
source:
  - "[[Hands-On LLM - Chapter 02 - Tokens and Embeddings]]"
  - "[[Hands-On LLM - Chapter 10 - Creating Text Embedding Models]]"
tags:
  - concept
  - embeddings
  - retrieval
---

# Embedding

## Định nghĩa

Embedding là vector số biểu diễn token, từ, câu, đoạn hoặc tài liệu trong không gian nhiều chiều.

## Cách hiểu bằng lời của tôi

Embedding là cách biến ý nghĩa thành tọa độ. Nếu hai text gần nhau trong embedding space, ta kỳ vọng chúng có liên quan theo tiêu chí mà model đã học.

## Cần biết

- Token embedding là input ban đầu của model.
- Contextualized embedding phụ thuộc vào câu xung quanh.
- Text embedding dùng cho semantic search, clustering, classification và recommendation.
- Similarity không cố định; nó phụ thuộc objective và dữ liệu training.

## Liên kết

- [[Semantic Search]]
- [[Contrastive Learning]]
- [[Representation Model]]
- [[Retrieval-Augmented Generation]]

