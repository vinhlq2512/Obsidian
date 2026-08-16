---
type: concept
status: seed
sources:
  - "[[2026-06-04_the-path-of-a-request-a-tour-of-modern-web-architecture]]"
source_sections:
  - "[[2026-06-04_the-path-of-a-request-a-tour-of-modern-web-architecture]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - web-architecture
  - system-design
---

# Web Request Path

## Định nghĩa

[[Web Request Path]] là chuỗi các tầng mà một request đi qua từ browser/client tới backend/database và quay lại.

## Cách hiểu bằng lời của tôi

Một trang load nhanh không phải vì chỉ có một server giỏi, mà vì nhiều tầng cùng giảm tải: DNS tìm điểm đến, CDN hấp thụ cacheable traffic, load balancer chia tải, gateway áp policy, service mesh xử lý inter-service concerns, service chạy business logic, cache/database trả dữ liệu.

## Luồng rút gọn

```text
Browser
-> [[DNS]]
-> [[Content Delivery Network]]
-> [[Load Balancer]]
-> [[API Gateway]]
-> [[Authentication]]
-> [[Service Mesh]]
-> Service
-> [[Caching Strategy]]
-> Database
```

## Trade-off

- Mỗi hop thêm latency nhỏ.
- Reliability tổng hợp giảm nếu quá nhiều dependency nối tiếp.
- Edge/cache giảm tải origin nhưng tạo bài toán invalidation/staleness.
- Gateway/mesh gom cross-cutting concerns nhưng có thể tăng blast radius.

## Liên kết

- [[Modern Web Request Architecture]]
- [[API Gateway]]
- [[Reverse Proxy]]
- [[Cache Stampede]]
- [[Latency]]
