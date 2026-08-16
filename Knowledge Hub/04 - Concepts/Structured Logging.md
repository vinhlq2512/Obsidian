---
type: concept
status: developing
sources:
  - "[[2026-06-18_observability-for-beginners-logs-metrics-traces-and-everythi]]"
  - "[[2025-01-20_the-engineers-guide-to-observability-making-metrics-logs-and]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - observability
  - reliability
---

# Structured Logging

## Định nghĩa

Structured logging là cách ghi log dưới dạng record có field rõ ràng, ví dụ JSON với `request_id`, `user_id`, `latency_ms`, `service`, `error_code`, thay vì một dòng text tự do.

## Cách hiểu bằng lời của tôi

Free-text log dễ đọc lúc viết nhưng khó hỏi lại sau này. Structured log biến mỗi event thành dữ liệu có schema, nên có thể filter, aggregate và correlate qua nhiều service.

## Cần log gì

- Errors và exceptions kèm stack trace, timestamp, request/correlation ID.
- Key actions như login, cache miss, database query, feature flag change.
- State changes như deploy, restart, config update.
- Context đủ để tái dựng câu chuyện nhưng không đẩy bí mật hoặc dữ liệu nhạy cảm vào log.

## Trade-off

- Overlogging tạo noise và tốn storage.
- Underlogging khiến incident không truy ra root cause.
- Log level phải nhất quán; `ERROR`, `WARN`, `INFO`, `DEBUG` không nên dùng theo cảm tính.

## Liên kết

- [[Observability]]
- [[Distributed Tracing]]
- [[Metric Cardinality]]
- [[LLM Security]]
