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
  - reliability
  - observability
---

# Alerting

## Định nghĩa

Alerting là cơ chế đưa vấn đề cần hành động tới người hoặc hệ thống chịu trách nhiệm, dựa trên tín hiệu observability và mức độ nghiêm trọng.

## Cách hiểu bằng lời của tôi

Alert không phải để báo mọi điều bất thường. Alert tốt là lời gọi hành động: vấn đề đủ nghiêm trọng, đúng người nhận, có context để bắt đầu xử lý.

## 3 AM test

Nếu alert bắn lúc 3 giờ sáng, người trực có việc cụ thể cần làm không, và vấn đề có đủ nghiêm trọng để đánh thức họ không? Nếu câu trả lời là không, alert đó nên thành dashboard hoặc ticket, không phải pager.

## Nguyên tắc

- Alert theo symptom user-facing trước: latency, error rate, success rate.
- Dùng cause metric như CPU/memory/disk làm evidence điều tra.
- Có ownership, severity và escalation path rõ.
- Review alert định kỳ để giảm noise và missed incident.

## Liên kết

- [[Observability]]
- [[Metrics]]
- [[Service Level Objective]]
- [[High Availability]]
