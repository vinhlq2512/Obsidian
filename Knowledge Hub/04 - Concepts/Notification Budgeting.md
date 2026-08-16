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
  - product
---

# Notification Budgeting

## Định nghĩa

[[Notification Budgeting]] là việc quyết định số lượng push notification nên gửi cho từng user trong một khoảng thời gian để cân bằng engagement và notification fatigue.

## Cách hiểu bằng lời của tôi

Push notification là kênh có chi phí UX cao. Một notification thêm có thể kéo user quay lại, nhưng cũng có thể làm họ disable toàn bộ notification. Budgeter phải tối ưu giá trị biên của notification tiếp theo, không chỉ maximize click ngắn hạn.

## Tín hiệu cần cân bằng

- Positive: click, session, upvote, comment, return visit.
- Negative: disable notification, churn, long inactivity gap.
- Treatment effect: điều gì có thể xảy ra nếu user nhận ít/nhiều notification hơn.

## Liên kết

- [[Notification Recommender Pipeline]]
- [[Recommendation Funnel]]
- [[Causal Inference]]
- [[Reranking]]
- [[Product Recommendation System]]
