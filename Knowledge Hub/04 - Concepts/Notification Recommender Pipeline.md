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
  - system-design
---

# Notification Recommender Pipeline

## Định nghĩa

[[Notification Recommender Pipeline]] là recommendation funnel chuyên cho push notification, gồm budgeting, retrieval, ranking và reranking để chọn nội dung vừa kịp thời vừa không gây mệt cho user.

## Cách hiểu bằng lời của tôi

Notification recommender khó hơn feed ở một điểm: hệ thống chủ động ngắt user. Vì vậy pipeline phải biết khi nào không gửi gì. Reddit dùng budgeter để giới hạn volume, retrieval để lấy candidate rẻ, ranking để dự đoán engagement và reranking để thêm diversity/product constraints.

## Luồng

```text
new content firehose
-> per-user notification budget
-> rule/model retrieval
-> DNN ranking đa mục tiêu
-> product reranking
-> push send hoặc stay silent
```

## Liên kết

- [[Notification Budgeting]]
- [[Two-Tower Retrieval]]
- [[Recommendation Funnel]]
- [[Reranking]]
- [[Data Freshness]]
- [[Precision-Recall Tradeoff]]
