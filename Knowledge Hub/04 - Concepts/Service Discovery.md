---
type: concept
status: seed
sources:
  - "[[2025-10-02_service-discovery-101-the-phonebook-for-distributed-systems-newsletter]]"
  - "[[2024-10-03_api-gateway-newsletter]]"
source_sections:
  - "[[2025-10-02_service-discovery-101-the-phonebook-for-distributed-systems-newsletter]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - microservices
  - system-design
---

# Service Discovery

## Cách hiểu bằng lời của tôi

[[Service Discovery]] là cách service tìm network location hiện tại của service khác trong môi trường instance thay đổi liên tục. Thay vì hard-code host/port, hệ thống dùng registry, DNS hoặc control plane để biết instance nào đang khỏe.

## Cơ chế

```text
Service instance start
-> đăng ký endpoint và health vào registry
-> client/gateway/load balancer tra registry
-> route request tới instance khỏe
-> instance unhealthy bị rút khỏi pool
```

## Khi áp dụng

Nó đặc biệt quan trọng với microservices, autoscaling, container orchestration và multi-region deployment, nơi instance có thể xuất hiện/biến mất thường xuyên.

## Liên kết

- [[API Gateway]]
- [[Load Balancer]]
- [[Microservices Design Patterns]]
