---
type: concept
status: seed
sources:
  - "[[2025-08-19_how-reddit-delivers-notifications-to-tens-of-millions-of-use]]"
  - "[[2025-01-05_modernizing-legacy-systems-without-breaking-production]]"
source_sections:
  - "[[2025-08-19_how-reddit-delivers-notifications-to-tens-of-millions-of-use]]"
  - "[[2025-01-05_modernizing-legacy-systems-without-breaking-production]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - experimentation
  - product
---

# A-B Testing

## Định nghĩa

[[A-B Testing]] là cách chia user hoặc traffic thành nhóm biến thể để đo tác động của thay đổi lên metric mục tiêu trong điều kiện có kiểm soát.

## Cách hiểu bằng lời của tôi

A/B test giúp phân biệt "người dùng kiểu này vốn đã khác" với "thay đổi này thật sự gây ra outcome khác". Trong hệ notification, intentionally varying notification volume tạo dữ liệu tốt hơn để ước lượng effect của budget.

## Liên kết

- [[Causal Inference]]
- [[Feature Flag]]
- [[Notification Budgeting]]
- [[Shadow Testing]]
- [[Data Pipeline Validation]]
