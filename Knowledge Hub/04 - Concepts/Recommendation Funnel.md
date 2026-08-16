---
type: concept
status: developing
sources:
  - "[[2026-08-10_how-to-fight-clickbait-meta-linkedin-youtube-case-studies]]"
  - "[[2024-02-29_how-video-recommendations-work-part-1]]"
  - "[[2025-08-19_how-reddit-delivers-notifications-to-tens-of-millions-of-use]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - recommendation
  - ranking
---

# Recommendation Funnel

## Định nghĩa

Recommendation funnel là kiến trúc nhiều tầng trong đó hệ thống dùng model rẻ để lọc candidate rộng, rồi dùng model đắt hơn trên tập nhỏ hơn để ranking cuối.

## Cách hiểu bằng lời của tôi

Funnel là cách mua compute đúng chỗ. Retrieval chạm corpus lớn nên phải rẻ. Early ranking thu hẹp candidate. Late ranking dùng model nặng hơn. Final pass có thể chỉnh diversity, integrity hoặc business constraints.

## Ví dụ từ ByteByteGo

Meta/Instagram giữ nhiều model chuyên biệt trong một staged funnel. Late-stage model dự đoán nhiều action khác nhau, rồi value model kết hợp positive signals như save với negative signals như "See Fewer Posts Like This".

Reddit áp dụng funnel cho push notification: budgeter quyết định có nên làm phiền user không, retrieval lấy vài trăm candidate rẻ, ranking dự đoán nhiều hành vi, rồi reranking áp UX/business constraints như diversity và content freshness.

## Trade-off

- Specialization cho phép kiểm soát từng objective.
- Nhiều model làm vận hành phức tạp hơn.
- Một funnel có nhiều điểm rollback hơn so với một model thống nhất.

## Liên kết

- [[Feed Retrieval]]
- [[Product Recommendation System]]
- [[Notification Budgeting]]
- [[Notification Recommender Pipeline]]
- [[Reranking]]
- [[Model Router]]
- [[LLM Evaluation]]
- [[Ranking]]
