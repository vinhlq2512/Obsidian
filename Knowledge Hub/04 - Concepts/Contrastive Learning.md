---
type: concept
status: seed
source:
  - "[[Hands-On LLM - Chapter 10 - Creating Text Embedding Models]]"
tags:
  - concept
  - machine-learning
  - embeddings
---

# Contrastive Learning

## Định nghĩa

Contrastive learning là phương pháp học biểu diễn bằng cách kéo các cặp liên quan lại gần nhau và đẩy các cặp không liên quan ra xa nhau trong embedding space.

## Cách hiểu bằng lời của tôi

Model học nghĩa của "giống nhau" từ các ví dụ so sánh. Nếu dữ liệu nói hai câu là paraphrase, vector của chúng nên gần nhau. Nếu chúng không liên quan, vector nên xa nhau.

## Cần biết

- Chất lượng positive/negative pairs cực kỳ quan trọng.
- Được dùng trong embedding models, CLIP, SBERT và retrieval training.
- Similarity học được phụ thuộc vào objective.

## Liên kết

- [[Embedding]]
- [[Semantic Search]]
- [[Multimodal LLM]]

