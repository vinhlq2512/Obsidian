---
type: concept
status: understood
sources:
  - "[[2024-12-23_the-chatgpt-outage-what-openais-post-mortem-revealed]]"
  - "[[2025-07-18_cloudflares-july-2025-outage-the-global-outage-triggered-by]]"
source_sections:
  - "[[2024-12-23_the-chatgpt-outage-what-openais-post-mortem-revealed]]"
  - "[[2025-07-18_cloudflares-july-2025-outage-the-global-outage-triggered-by]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - infrastructure
---

# Data Plane

## Định nghĩa

Data Plane là lớp trực tiếp xử lý traffic, request, packet hoặc workload thực tế của người dùng.

## Cách hiểu bằng lời của tôi

Data plane nên tiếp tục phục vụ được càng nhiều càng tốt khi [[Control Plane]] gặp vấn đề. Nếu data plane phụ thuộc quá chặt vào control plane cho mỗi request, một lỗi cấu hình hoặc API control plane có thể biến thành outage người dùng.

## Liên kết

- [[Control Plane]]
- [[Graceful Degradation]]
- [[Service Discovery]]
- [[Partial Failure]]
- [[Failover]]
