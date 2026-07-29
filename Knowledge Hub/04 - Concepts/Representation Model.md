---
type: concept
status: seed
source:
  - "[[Hands-On LLM - Chapter 01 - An Introduction to Large Language Models]]"
  - "[[Hands-On LLM - Chapter 04 - Text Classification]]"
tags:
  - concept
  - llm
  - embeddings
---

# Representation Model

## Định nghĩa

Representation model là language model tạo biểu diễn vector cho text thay vì chủ yếu sinh text mới.

## Cách hiểu bằng lời của tôi

Model này giống một bộ mã hóa ý nghĩa. Nó biến text thành vector để hệ thống phía sau dùng cho classification, clustering, reranking, retrieval hoặc similarity search.

## Cần biết

- Encoder-only models như BERT thường thuộc nhóm này.
- Thường nhanh và ổn định hơn generative models cho tác vụ phân loại/truy xuất.
- Chất lượng phụ thuộc vào embedding space và objective training.

## Liên kết

- [[Embedding]]
- [[Semantic Search]]
- [[Text Classification]]
- [[Generative Model]]

