---
type: concept
status: seed
sources:
  - "[[2026-08-10_how-to-fight-clickbait-meta-linkedin-youtube-case-studies]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - ranking
  - recommendation
---

# Ranking

## Định nghĩa

Ranking là tầng sắp xếp candidate theo score hoặc objective sau khi retrieval đã thu hẹp không gian tìm kiếm.

## Cách hiểu bằng lời của tôi

Retrieval quyết định cái gì có cơ hội được thấy; ranking quyết định thứ tự cuối. Ranking có thể dùng model đắt hơn vì chỉ xử lý số candidate nhỏ hơn nhiều so với toàn bộ corpus.

## Cần biết

- Ranking objective không nên chỉ là engagement thô nếu proxy đó dễ bị thao túng.
- Multi-objective ranking có thể kết hợp positive signals, negative feedback, diversity và integrity.
- Ranking cần eval bằng outcome người dùng thật, không chỉ metric offline.

## Liên kết

- [[Feed Retrieval]]
- [[Recommendation Funnel]]
- [[Product Recommendation System]]
- [[LLM Evaluation]]
