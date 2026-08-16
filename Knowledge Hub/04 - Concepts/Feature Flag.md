---
type: concept
status: understood
sources:
  - "[[2024-04-04_a-crash-course-in-cicd]]"
  - "[[2026-06-11_must-know-deployment-strategies-from-big-bang-to-progressive]]"
source_sections:
  - "[[2024-04-04_a-crash-course-in-cicd]]"
  - "[[2026-06-11_must-know-deployment-strategies-from-big-bang-to-progressive]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - deployment
  - system-design
---

# Feature Flag

## Định nghĩa

Feature Flag là runtime switch điều khiển code path hoặc feature mà không cần redeploy.

## Cách hiểu bằng lời của tôi

Feature flag tách "deploy code" khỏi "release feature". Code có thể nằm trong production nhưng feature chỉ bật cho một nhóm user, một market, một experiment hoặc được tắt ngay như kill switch khi có incident.

## Rủi ro

- Flag lâu ngày không dọn tạo flag debt.
- Nhiều flag tạo số tổ hợp code path khó test.
- Config change có thể gây incident nếu không có owner, audit và observability.

## Liên kết

- [[Canary Deployment]]
- A/B testing
- kill switch
- [[Technical Debt]]
