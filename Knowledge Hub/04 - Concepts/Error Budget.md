---
type: concept
status: seed
sources:
  - "[[2023-11-07_shipping-to-production]]"
  - "[[2025-11-13_scalability-patterns-for-modern-distributed-systems]]"
source_sections:
  - "[[2023-11-07_shipping-to-production]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - sre
---

# Error Budget

## Định nghĩa

[[Error Budget]] là phần service degradation được chấp nhận trong một cửa sổ thời gian dựa trên [[Service Level Objective]], dùng để cân bằng tốc độ thay đổi và độ tin cậy.

## Cách hiểu bằng lời của tôi

Nếu SLO là 99.9% availability, team không cần giả vờ hệ thống phải hoàn hảo 100%. Error budget nói rõ ta được "tiêu" bao nhiêu lỗi trước khi user impact vượt ngưỡng. Khi budget còn nhiều, có thể chấp nhận rollout rủi ro hơn; khi budget cạn, nên dừng thay đổi nguy hiểm và tập trung vào reliability.

## Công thức trực giác

```text
error_budget = 1 - SLO_target
allowed_bad_time = time_window * error_budget
```

Ví dụ 99.9% uptime trong 30 ngày cho phép khoảng 0.1% thời gian degrade/down.

## Khi dùng

- Quyết định có cho phép risky deployment không.
- Điều chỉnh release process khi incident tăng.
- Ưu tiên reliability work khi user impact vượt mức chấp nhận.
- Nối business tolerance với engineering operations.

## Liên kết

- [[Service Level Objective]]
- [[Service Level Indicator]]
- [[Alerting]]
- [[Phased Rollout]]
- [[Incident Response]]
