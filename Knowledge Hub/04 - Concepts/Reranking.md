---
type: concept
status: seed
sources:
  - "[[2025-08-19_how-reddit-delivers-notifications-to-tens-of-millions-of-use]]"
source_sections:
  - "[[2025-08-19_how-reddit-delivers-notifications-to-tens-of-millions-of-use]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - recommendation
  - ranking
---

# Reranking

## Định nghĩa

[[Reranking]] là bước điều chỉnh danh sách đã được ranking để áp dụng constraint hoặc mục tiêu cuối như diversity, freshness, business rule hoặc UX quality.

## Cách hiểu bằng lời của tôi

Model ranking dựa vào pattern lịch sử, nhưng product experience cần nhiều ràng buộc hơn: đừng gửi quá nhiều nội dung giống nhau, đừng spam một subreddit, đừng chỉ tối ưu click ngắn hạn. Reranking là lớp đưa judgement sản phẩm vào sau model score.

## Liên kết

- [[Ranking]]
- [[Recommendation Funnel]]
- [[Notification Recommender Pipeline]]
- [[Search Ranking]]
- [[Precision-Recall Tradeoff]]
