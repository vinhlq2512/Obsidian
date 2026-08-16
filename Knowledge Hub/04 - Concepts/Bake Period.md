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
  - reliability
  - deployment
---

# Bake Period

## Định nghĩa

Bake Period là khoảng thời gian chờ sau khi deploy một phần hoặc toàn bộ version mới để quan sát metric trước khi tiếp tục rollout.

## Cách hiểu bằng lời của tôi

Không phải bug nào cũng nổ ngay lúc process start. Bake period cho hệ thống thời gian gặp traffic thật, warm cache, chạy job nền và bộc lộ regression chậm trước khi tăng blast radius.

## Liên kết

- [[Canary Deployment]]
- [[Rollback Alarm]]
- [[Phased Rollout]]
- [[Observability]]
