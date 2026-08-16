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
  - machine-learning
  - product
---

# Causal Inference

## Định nghĩa

[[Causal Inference]] là cách ước lượng ảnh hưởng nhân quả của một can thiệp lên outcome, thay vì chỉ nhìn correlation trong dữ liệu quan sát.

## Cách hiểu bằng lời của tôi

Với notification, correlation dễ lừa: user nhận nhiều notification và vẫn active có thể vốn đã là user active. Causal modeling cố trả lời câu hỏi phản thực tế: nếu cùng user đó nhận ít hoặc nhiều notification hơn thì engagement/churn sẽ đổi thế nào.

## Liên kết

- [[Notification Budgeting]]
- [[Recommendation Funnel]]
- [[A-B Testing]]
- [[Data Pipeline Validation]]
