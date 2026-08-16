---
type: concept
status: understood
sources:
  - "[[2026-06-11_must-know-deployment-strategies-from-big-bang-to-progressive]]"
source_sections:
  - "[[2026-06-11_must-know-deployment-strategies-from-big-bang-to-progressive]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - database
  - deployment
  - system-design
---

# Expand-Contract Migration

## Định nghĩa

Expand-Contract Migration là pattern thay đổi schema theo nhiều deploy: thêm cấu trúc mới trước, chạy code tương thích hai bên, backfill, chuyển read/write, rồi mới xóa cấu trúc cũ.

## Cách hiểu bằng lời của tôi

Rollback code dễ hơn rollback schema. Expand-contract giữ mỗi bước deploy ở trạng thái rollback-safe, vì old code và new code có khoảng thời gian cùng hiểu được dữ liệu.

## Flow

```text
expand schema
-> dual write
-> backfill
-> read new schema
-> stop writing old schema
-> contract/remove old schema
```

## Trade-off

- An toàn hơn cho rolling/canary/blue-green.
- Chậm hơn vì một logical change thành nhiều deploy.
- Dễ để lại debt nếu team không hoàn tất phase contract.

## Liên kết

- [[Backward Compatibility]]
- [[Rolling Deployment]]
- [[Blue-Green Deployment]]
- [[Database Schema Design]]
- [[Rollback Strategy]]
