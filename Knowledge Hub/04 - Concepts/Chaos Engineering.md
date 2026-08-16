---
type: concept
status: developing
sources:
  - "[[2024-04-11_embracing-chaos-to-improve-system-resilience-chaos-engineeri]]"
  - "[[2025-01-16_slack-breaks-stuff-on-purpose-with-chaos-testing]]"
  - "[[2025-01-20_the-engineers-guide-to-observability-making-metrics-logs-and]]"
  - "[[2023-03-15_netflix-is-chill-with-breaking-their-services]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - resilience
  - system-design
---

# Chaos Engineering

## Định nghĩa

Chaos engineering là kỷ luật thử nghiệm có kiểm soát trên hệ thống để tăng niềm tin rằng hệ thống chịu được điều kiện hỗn loạn trong production.

## Cách hiểu bằng lời của tôi

Không phải phá cho vui. Chaos engineering bắt đầu bằng giả thuyết, inject lỗi có giới hạn, quan sát bằng metrics/logs/traces, rồi dùng kết quả để sửa điểm yếu trước khi lỗi thật xảy ra.

## Luồng thực hành

```text
hypothesis
-> experiment design
-> chaos injection
-> observation
-> behavior analysis
-> learning and iteration
```

## Nguyên tắc

- Hypothesis-driven, không random phá hệ thống.
- Mô phỏng failure thực tế: instance chết, network chậm, dependency lỗi, AZ fail.
- Minimize blast radius và có rollback plan.
- Đo đủ lâu để tránh kết luận sớm.
- Gắn experiment với [[Observability]] và [[Service Level Objective]].

## Ví dụ Netflix MAP/FIT

Nguồn Netflix MAP nhấn mạnh failure testing ở middle layer: request được tag như failure request, đi qua service thật, rồi các dependency/downstream phải phản ứng đúng với trạng thái lỗi. Điểm học được là chaos test cần giữ failure trong blast radius của hệ đang test: không làm dependents thất vọng và không làm dependencies bị kéo vào lỗi dây chuyền.

## Liên kết

- [[High Availability]]
- [[Observability]]
- [[Alerting]]
- [[Retry Storm]]
- [[Circuit Breaker]]
- [[Backpressure]]
- [[Bulkhead Pattern]]
