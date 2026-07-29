---
type: concept
status: seed
source:
  - "[[Hands-On LLM - Chapter 08 - Semantic Search and Retrieval-Augmented Generation]]"
tags:
  - concept
  - retrieval
  - embeddings
---

# Semantic Search

## Định nghĩa

Semantic search là tìm kiếm theo ý nghĩa bằng cách so sánh embeddings của query và documents.

## Cách hiểu bằng lời của tôi

Thay vì chỉ khớp từ khóa, semantic search hỏi: query này gần đoạn nào về mặt nghĩa trong vector space?

## Cần biết

- Cần embedding model tốt, chunking hợp lý và vector database.
- Dense retrieval có thể tìm kết quả dùng từ khác nhưng cùng nghĩa.
- Có thể kết hợp keyword search và semantic search để tăng độ phủ.
- Reranking thường cải thiện kết quả top-k.

## Liên kết

- [[Embedding]]
- [[Vector Database]]
- [[Retrieval-Augmented Generation]]

