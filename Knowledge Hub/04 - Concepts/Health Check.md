---
type: concept
status: seed
sources:
  - "[[2026-01-29_how-to-scale-an-api]]"
  - "[[2026-06-04_the-path-of-a-request-a-tour-of-modern-web-architecture]]"
source_sections:
  - "[[2026-01-29_how-to-scale-an-api]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - system-design
---

# Health Check

## Định nghĩa

[[Health Check]] là kiểm tra định kỳ để xác định một instance/service có đủ khỏe để nhận traffic hoặc tiếp tục chạy workload không.

## Cách hiểu bằng lời của tôi

Health check là tín hiệu cho load balancer, orchestrator hoặc gateway. Nhưng health check quá nông chỉ nói process còn sống; nó có thể bỏ sót [[Gray Failure]]. Với critical path, cần phân biệt liveness, readiness và synthetic checks.

## Cần nhớ

- Liveness: process có nên bị restart không.
- Readiness: instance có nên nhận traffic không.
- Dependency check quá sâu có thể tạo cascading failure.
- Health check phải rẻ, ổn định và phản ánh khả năng phục vụ thật.

## Liên kết

- [[Load Balancer]]
- [[Kubernetes Pod]]
- [[Synthetic Monitoring]]
- [[Gray Failure]]
- [[Failover]]
