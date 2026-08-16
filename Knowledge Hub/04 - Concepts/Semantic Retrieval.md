---
type: concept
status: developing
sources:
  - "[[2026-08-10_how-to-fight-clickbait-meta-linkedin-youtube-case-studies]]"
  - "[[2026-07-28_why-doordash-instacart-and-uber-eats-integrated-llms-into-se]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - retrieval
  - embeddings
  - recommendation
---

# Semantic Retrieval

## Định nghĩa

Semantic retrieval là retrieval dựa trên meaning representation, thường dùng embeddings để match user/query với content/item theo ý nghĩa thay vì chỉ theo keyword hoặc behavior.

## Cách hiểu bằng lời của tôi

Semantic retrieval chuyển câu hỏi từ "user từng click gì giống cái này?" sang "nội dung này nói về điều gì và có liên quan tới intent/profile của user không?". Đây là cách giảm sức mạnh của engagement bait vì hệ thống không chỉ tối ưu proxy dễ bị thao túng.

## Cơ chế phổ biến

- Encode user/query thành vector.
- Encode item/content thành vector, thường offline.
- Lưu item vectors trong index.
- Online request chạy nearest-neighbor search để lấy candidate.

## Liên kết

- [[Semantic Search]]
- [[Two-Tower Retrieval]]
- [[Vector Search Infrastructure]]
- [[Feed Retrieval]]
- [[Cold Start Problem]]
