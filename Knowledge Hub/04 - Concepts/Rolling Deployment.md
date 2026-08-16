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

# Rolling Deployment

## Định nghĩa

Rolling Deployment là strategy cập nhật production từng nhóm instance, để version mới dần thay thế version cũ mà không dừng toàn hệ thống.

## Cách hiểu bằng lời của tôi

Rolling giảm downtime nhưng tạo mixed-version state. Trong lúc rollout, old và new cùng phục vụ traffic nên API, cache, database schema và message format phải backward-compatible.

## Rủi ro

- Bug chậm như memory leak có thể không lộ ngay trong rollout.
- Không target được nhóm user cụ thể.
- Rollback phức tạp nếu new version đã ghi dữ liệu old version không hiểu.

## Liên kết

- [[Phased Rollout]]
- [[Backward Compatibility]]
- [[Expand-Contract Migration]]
- [[Deployment Pipeline]]
