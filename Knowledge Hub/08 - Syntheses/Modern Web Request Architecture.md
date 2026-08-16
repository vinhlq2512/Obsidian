---
type: synthesis
status: seed
concepts:
  - "[[Web Request Path]]"
  - "[[DNS]]"
  - "[[Content Delivery Network]]"
  - "[[Load Balancer]]"
  - "[[Reverse Proxy]]"
  - "[[API Gateway]]"
  - "[[Authentication]]"
  - "[[Service Mesh]]"
  - "[[Caching Strategy]]"
  - "[[Cache Stampede]]"
  - "[[Health Check]]"
  - "[[TLS Termination]]"
  - "[[Edge Function]]"
sources:
  - "[[2026-06-04_the-path-of-a-request-a-tour-of-modern-web-architecture]]"
  - "[[2025-10-23_api-gateways-101-the-core-of-modern-api-management-security]]"
  - "[[2026-01-29_how-to-scale-an-api]]"
questions: []
created_at: 2026-08-16
updated_at: 2026-08-16
tags:
  - synthesis
  - web-architecture
  - system-design
  - bytebytego
---

# Modern Web Request Architecture

## Ý chính

Một request web hiện đại đi qua nhiều tầng, mỗi tầng đổi một chút latency lấy một khả năng: DNS định tuyến, CDN cache, load balancer chia tải, API gateway áp policy, service mesh chuẩn hóa inter-service traffic, cache giảm tải database, và database giữ source of truth.

## Request funnel

```text
[[DNS]]
-> [[Content Delivery Network]]
-> [[Load Balancer]] / [[Reverse Proxy]]
-> [[API Gateway]]
-> [[Authentication]] / [[API Security]]
-> [[Service Mesh]]
-> Service
-> [[Caching Strategy]]
-> Database
```

## Trade-off hệ thống

- Latency cộng dồn qua hop.
- Reliability nhân qua dependency, nên thêm layer phải có lý do.
- Edge/cache giảm load origin nhưng tạo [[Cache Stampede]] và stale data nếu quản lý kém.
- Gateway/mesh giảm duplication nhưng có thể thành blast radius nếu policy/config sai.

## Liên kết

- [[API Design Patterns]]
- [[Scalable Distributed Systems Patterns]]
- [[Observability for Distributed Systems]]
- [[Resilience Failure Control Patterns]]
