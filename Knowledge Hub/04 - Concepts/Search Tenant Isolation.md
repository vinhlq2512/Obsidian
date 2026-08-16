---
type: concept
status: understood
sources:
  - "[[2024-11-30_when-elasticsearch-reached-its-limits-doordash-built-their-o]]"
  - "[[2025-12-04_how-discord-indexes-trillions-of-messages-without-falling-ap]]"
source_sections:
  - "[[2024-11-30_when-elasticsearch-reached-its-limits-doordash-built-their-o]]"
  - "[[2025-12-04_how-discord-indexes-trillions-of-messages-without-falling-ap]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - search
  - reliability
---

# Search Tenant Isolation

## Định nghĩa

Search Tenant Isolation là cách tách workload search theo tenant/use case/cell để spike, schema change hoặc lỗi của một workload không kéo sập workload khác.

## Cách hiểu bằng lời của tôi

Search cluster lớn dùng chung nhìn đơn giản lúc đầu, nhưng dễ gặp noisy neighbor và coordination tax. DoorDash dùng search stack riêng cho từng use case; Discord chia thành cell nhỏ hơn cho guild, DM và guild cực lớn.

## Liên kết

- [[Blast Radius]]
- [[Cell-Based Architecture]]
- [[Search Engine Architecture]]
- [[Kubernetes Autoscaling]]
- [[Cost Optimization]]
