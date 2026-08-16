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
  - reliability
---

# Canary Deployment

## Định nghĩa

Canary Deployment là strategy gửi một phần nhỏ traffic hoặc user tới version mới, quan sát health metrics, rồi tăng dần tỷ lệ nếu version mới ổn.

## Cách hiểu bằng lời của tôi

Canary chỉ an toàn khi observability đủ chi tiết theo version. Nếu không đo được error rate, latency và behavior của version mới riêng biệt, team chỉ đang phát hành chậm hơn chứ không thật sự kiểm soát rủi ro.

## Cơ chế

- Bắt đầu với tỷ lệ nhỏ, ví dụ 1% traffic.
- So sánh metric version mới và version cũ trong [[Bake Period]].
- Tăng dần traffic nếu healthy; rollback nếu [[Rollback Alarm]] kích hoạt.

## Liên kết

- [[Phased Rollout]]
- [[Observability]]
- [[Rollback Alarm]]
- [[Feature Flag]]
