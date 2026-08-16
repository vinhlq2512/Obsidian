---
type: concept
status: developing
sources:
  - "[[2026-07-28_why-doordash-instacart-and-uber-eats-integrated-llms-into-se]]"
  - "[[2026-08-10_how-to-fight-clickbait-meta-linkedin-youtube-case-studies]]"
  - "[[2025-08-19_how-reddit-delivers-notifications-to-tens-of-millions-of-use]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - retrieval
  - search
  - embeddings
---

# Two-Tower Retrieval

## Định nghĩa

Two-tower retrieval là kiến trúc retrieval trong đó query encoder và document/item encoder tạo embeddings trong cùng không gian, rồi matching được tính bằng similarity giữa hai vector.

## Cách hiểu bằng lời của tôi

Một tower hiểu query, tower kia hiểu item. Document/item có thể được embed offline trước; query được embed online khi user tìm kiếm. Nhờ vậy hệ thống không phải chạy model nặng trên toàn bộ catalog mỗi request.

## Luồng cơ bản

```text
documents/items
-> document tower offline
-> vector index

user query
-> query tower online
-> ANN search
-> candidates
-> ranking
```

## Từ ByteByteGo

Uber Eats dùng fine-tuned Qwen làm backbone cho cả query tower và document tower để tạo shared embedding space đa vertical, đa thị trường và đa ngôn ngữ. Document tower chạy offline để precompute hàng tỷ vector; query tower chạy online cho request thật. Các optimization như Matryoshka Representation Learning, scalar quantization và pre-filter giúp kiến trúc này khả thi ở production scale.

LinkedIn dùng biến thể dual encoder cho feed retrieval: một encoder biểu diễn member/profile/activity, encoder còn lại biểu diễn post, cả hai nằm trong shared embedding space để nearest-neighbor search chạy dưới latency budget của feed.

Reddit dùng two-tower retrieval cho notification: post embedding được precompute và index trước, còn user embedding được tính online từ hành vi/metadata gần đây để lấy candidate nhanh trước khi ranking nặng hơn.

## Liên kết

- [[Semantic Search]]
- [[Embedding]]
- [[Vector Database]]
- [[AI Search]]
- [[Semantic Retrieval]]
- [[Feed Retrieval]]
- [[Notification Recommender Pipeline]]
- [[Fine-tuning]]
- [[Quantization]]
