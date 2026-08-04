---
type: concept
status: seed
sources:
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

## Embedding lookup khi thiếu nhãn

Trong bài toán ít hoặc chưa có nhãn, embedding có thể dùng để khám phá dữ liệu trước khi train classifier.

```text
Unlabeled texts
-> Encode thành text embeddings
-> Tính similarity / clustering
-> Tìm nhóm câu gần nhau
-> Chọn representative examples để gán nhãn
```

Khi đã có vài ví dụ gán nhãn, có thể dùng nearest-neighbor:

```text
New utterance
-> Embedding
-> Tìm labeled example gần nhất
-> Dự đoán label theo neighbor
```

Điểm cần nhớ: embedding lookup không học decision boundary rõ như classifier. Nó dựa vào giả định rằng các câu cùng nhãn nằm gần nhau trong embedding space. Nếu các intent gần nghĩa hoặc embedding model không hợp domain, kết quả dễ nhiễu.

## Liên kết

- [[Semantic Search]]
- [[Contrastive Learning]]
- [[Representation Model]]
- [[Retrieval-Augmented Generation]]
- [[Few-shot Learning]]
- [[Intent Detection]]
