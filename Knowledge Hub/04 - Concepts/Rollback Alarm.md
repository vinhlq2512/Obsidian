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

# Rollback Alarm

## Định nghĩa

Rollback Alarm là alert hoặc automated gate theo dõi metric rollout và kích hoạt rollback khi version mới vượt ngưỡng lỗi đã định nghĩa.

## Cách hiểu bằng lời của tôi

Rollback alarm biến "có vẻ ổn" thành tiêu chí vận hành cụ thể. Trước khi rollout, team phải biết metric nào xấu là dừng: error rate, latency, saturation, business KPI hoặc divergence so với version cũ.

## Khi dùng

- 1-box environment.
- [[Canary Deployment]].
- [[Phased Rollout]] hoặc progressive rollout.
- Full production deployment có yêu cầu rollback nhanh.

## Liên kết

- [[Rollback Strategy]]
- [[Observability]]
- [[Service Level Indicator]]
- [[Bake Period]]
