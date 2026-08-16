---
type: concept
status: understood
sources:
  - "[[2025-03-20_monolith-vs-microservices-vs-modular-monoliths-what-s-the-ri]]"
  - "[[2026-04-11_ep210-monolithic-vs-microservices-vs-serverless]]"
  - "[[2025-10-16_a-guide-to-microservices-architecture-for-building-scalable]]"
source_sections:
  - "[[2025-03-20_monolith-vs-microservices-vs-modular-monoliths-what-s-the-ri]]"
  - "[[2026-04-11_ep210-monolithic-vs-microservices-vs-serverless]]"
  - "[[2025-10-16_a-guide-to-microservices-architecture-for-building-scalable]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - architecture
  - system-design
---

# Microservices Architecture

## Định nghĩa

Microservices Architecture là kiến trúc chia hệ thống thành nhiều service độc lập, mỗi service có boundary, deployment, scaling và thường cả data ownership riêng.

## Cách hiểu bằng lời của tôi

Microservices mua independent scaling và team autonomy bằng distributed-systems complexity. Khi tách service, function call thành network call; transaction nội bộ thành consistency problem; log local thành tracing đa service.

## Khi đáng dùng

- Có domain boundary rõ.
- Một số phần cần scale/deploy độc lập.
- Nhiều team cần ownership riêng.
- Hệ thống đủ lớn để chi phí orchestration, observability và data consistency là hợp lý.

## Liên kết

- [[Microservices Design Patterns]]
- [[Service Discovery]]
- [[Distributed Tracing]]
- [[Eventual Consistency]]
- [[Modular Monolith]]
