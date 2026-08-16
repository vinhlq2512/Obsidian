---
type: concept
status: seed
sources:
  - "[[2026-06-04_the-path-of-a-request-a-tour-of-modern-web-architecture]]"
  - "[[2025-10-09_domain-name-system-the-internets-telephone-directory]]"
source_sections:
  - "[[2026-06-04_the-path-of-a-request-a-tour-of-modern-web-architecture]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - networking
  - system-design
---

# DNS

## Định nghĩa

[[DNS]] là hệ thống phân giải tên miền thành địa chỉ mạng để browser/client biết gửi request tới đâu.

## Cách hiểu bằng lời của tôi

DNS là bước đầu tiên trước khi request chạm vào CDN, load balancer hay app. Vì lookup được cache ở nhiều tầng, hệ thống thường rất nhanh; nhưng khi DNS sai, user thấy "app không vào được" dù server phía sau vẫn khỏe.

## Cơ chế

```text
browser
-> recursive resolver
-> root servers
-> TLD servers
-> authoritative name server
-> IP address
```

## Liên kết

- [[Web Request Path]]
- [[Content Delivery Network]]
- [[Load Balancer]]
- [[Latency]]
- [[Incident Response]]
