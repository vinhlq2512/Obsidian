---
type: concept
status: seed
sources:
  - "[[2025-10-23_api-gateways-101-the-core-of-modern-api-management-security]]"
  - "[[2026-01-29_how-to-scale-an-api]]"
  - "[[2026-06-04_the-path-of-a-request-a-tour-of-modern-web-architecture]]"
source_sections:
  - "[[2025-10-23_api-gateways-101-the-core-of-modern-api-management-security]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - networking
  - system-design
---

# Reverse Proxy

## Định nghĩa

[[Reverse Proxy]] là server đứng trước backend, nhận request từ client rồi chuyển tiếp tới service/server nội bộ phù hợp.

## Cách hiểu bằng lời của tôi

Forward proxy che client khỏi server; reverse proxy che backend khỏi client. Nó tạo một cửa vào ổn định, có thể làm load balancing, TLS termination, caching, compression, routing và security filtering trước khi request vào app.

## Khi xuất hiện

- [[Load Balancer]] ở edge.
- [[API Gateway]] trước microservices.
- CDN/origin shield trước origin.
- Ingress controller trong Kubernetes.

## Liên kết

- [[API Gateway]]
- [[Load Balancer]]
- [[TLS Termination]]
- [[Service Discovery]]
- [[Web Request Path]]
