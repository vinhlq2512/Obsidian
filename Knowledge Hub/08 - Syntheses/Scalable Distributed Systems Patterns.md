---
type: synthesis
status: developing
concepts:
  - "[[Load Balancer]]"
  - "[[API Gateway]]"
  - "[[Rate Limiting]]"
  - "[[Database Sharding]]"
  - "[[Data Replication]]"
  - "[[Message Broker]]"
  - "[[High Availability]]"
  - "[[Observability]]"
  - "[[Caching Strategy]]"
  - "[[Retry Pattern]]"
  - "[[CAP and PACELC]]"
sources:
  - "[[2024-08-29_a-crash-course-on-load-balancers-for-scaling]]"
  - "[[2024-10-03_api-gateway-newsletter]]"
  - "[[2025-09-04_a-guide-to-rate-limiting-strategies-bytebytego-newsletter]]"
  - "[[2025-07-17_a-guide-to-database-sharding-key-strategies-newsletter]]"
  - "[[2023-09-07_how-to-choose-a-replication-strategy]]"
  - "[[2026-01-08_must-know-message-broker-patterns]]"
created_at: 2026-08-16
updated_at: 2026-08-16
tags:
  - synthesis
  - system-design
---

# Scalable Distributed Systems Patterns

## Luồng mở rộng hệ thống

Một hệ thống thường không scale bằng một pattern duy nhất. Các pattern giải quyết các điểm nghẽn khác nhau:

```text
Traffic tăng
-> [[Load Balancer]] chia request qua nhiều app instance
-> [[API Gateway]] gom entrypoint và policy ở edge
-> [[Rate Limiting]] bảo vệ capacity tức thời
-> [[Caching Strategy]] giảm read load và latency
-> [[Database Sharding]] chia dữ liệu khi một database không đủ
-> [[Data Replication]] tăng availability, durability, read scale
-> [[Message Broker]] tách xử lý đồng bộ khỏi xử lý nền
-> [[Retry Pattern]] phục hồi lỗi transient nếu operation an toàn
-> [[Observability]] giúp thấy bottleneck, lỗi và trade-off trong runtime
```

## Mental model

Scale là bài toán di chuyển bottleneck. Khi app server nghẽn, thêm load balancer và instance. Khi database nghẽn, thêm read replica hoặc shard. Khi request đồng bộ làm user path chậm, đưa phần nền qua broker. Khi traffic burst làm downstream quá tải, thêm rate limiting hoặc backpressure. Mỗi bước làm một phần khỏe hơn nhưng cũng tạo complexity mới.

## Những cặp trade-off lặp lại

- Simplicity vs scalability: monolith và single database dễ vận hành hơn nhưng chạm trần sớm.
- Availability vs consistency: replication async và event-driven giúp hệ thống sống sót tốt hơn nhưng tạo stale state.
- Edge centralization vs blast radius: gateway/rate limit/caching ở edge quản trị dễ hơn nhưng lỗi config có thể ảnh hưởng rộng.
- Throughput vs debuggability: queue và async pipeline tăng throughput nhưng làm luồng nguyên nhân-kết quả khó nhìn hơn.
- Precision vs cost: sliding log rate limit chính xác hơn counter, tail sampling trace giàu tín hiệu hơn head sampling, nhưng đều tốn tài nguyên hơn.
- Latency vs consistency: [[CAP and PACELC]] nhắc rằng ngay cả khi không có partition, hệ phân tán vẫn thường đổi latency lấy consistency hoặc ngược lại.

## Checklist khi thiết kế

- Bottleneck hiện nằm ở CPU app, database read/write, network, third-party API hay coordination?
- Operation nào không được lặp lại khi retry?
- Dữ liệu nào cần strong consistency, dữ liệu nào chịu được eventual consistency?
- Key nào đại diện cho fairness: IP, user, tenant, API key, endpoint?
- Failure nào phải tự động failover, failure nào nên degrade có kiểm soát?
- Metric nào phản ánh trải nghiệm người dùng thật, không chỉ resource nội bộ?

## Liên kết

- [[System Design]]
- [[Distributed Systems]]
- [[Microservices Design Patterns]]
- [[Eventual Consistency]]
