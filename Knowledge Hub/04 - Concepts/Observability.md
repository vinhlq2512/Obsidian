---
type: concept
status: understood
sources:
  - "[[2026-06-18_observability-for-beginners-logs-metrics-traces-and-everythi]]"
  - "[[2025-01-20_the-engineers-guide-to-observability-making-metrics-logs-and]]"
source_sections:
  - "[[2026-06-18_observability-for-beginners-logs-metrics-traces-and-everythi]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - system-design
---

# Observability

## Cách hiểu bằng lời của tôi

[[Observability]] là khả năng đặt câu hỏi mới về trạng thái hệ thống dựa trên dữ liệu nó phát ra. Logs, metrics và traces là ba cách nhìn cùng một dòng event: logs giữ sự kiện cụ thể, metrics tổng hợp theo thời gian, traces nối các span qua nhiều service.

## Ba trụ cột

- Logs: tốt cho ngữ cảnh chi tiết của một event. Structured logging giúp query và filter tốt hơn free-text.
- Metrics: tốt cho câu hỏi tổng hợp như error rate, latency percentile, queue depth. Cần kiểm soát cardinality.
- Traces: tốt để theo request đi qua nhiều service, đặc biệt khi latency hoặc lỗi đến từ interaction giữa service.

## Cardinality

Cardinality là số lượng tổ hợp label/tag tạo ra time series. Label bounded như status code, region, environment thường ổn. Label không bounded như user ID, session ID, request ID có thể làm nổ số lượng series. Ngữ cảnh high-cardinality thường nên nằm trong logs hoặc traces, không nằm trong metrics.

## Monitoring vs observability

Monitoring kiểm tra điều kiện đã biết trước: database reachable, error rate dưới ngưỡng, queue depth bình thường. Observability giúp điều tra điều chưa đoán trước. Hệ trưởng thành cần cả hai.

## Alerting và dashboard

- Alert nên bắn theo symptom user cảm nhận: latency, error rate, request success rate của flow quan trọng.
- CPU/memory/disk là bằng chứng điều tra, không nên là pager chính nếu user chưa bị ảnh hưởng.
- Dashboard tốt là câu hỏi được đóng băng, không phải bộ sưu tập chart. Nếu không ai hỏi câu đó thường xuyên, panel nên bị xóa.
- Post-mortem tốt nên hỏi observability đã phát hiện lỗi đủ sớm chưa, dữ liệu nào thiếu, và action item nào đóng lỗ hổng đó.

## Liên kết

- [[High Availability]]
- [[Microservices Design Patterns]]
- [[Scalable Distributed Systems Patterns]]
- [[Structured Logging]]
- [[Metrics]]
- [[Metric Cardinality]]
- [[Distributed Tracing]]
- [[Service Level Objective]]
- [[Alerting]]
