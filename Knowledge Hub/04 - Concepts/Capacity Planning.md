---
type: concept
status: seed
sources:
  - "[[2023-06-29_capacity-planning]]"
  - "[[2025-02-06_the-tech-lead-s-guide-to-load-testing-like-a-pro-byte-sized-design]]"
source_sections:
  - "[[2023-06-29_capacity-planning]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - system-design
---

# Capacity Planning

## Định nghĩa

[[Capacity Planning]] là quá trình ước lượng và vận hành tài nguyên cần thiết để hệ thống đáp ứng throughput, latency, storage, bandwidth và availability mục tiêu.

## Cách hiểu bằng lời của tôi

Capacity planning là biến yêu cầu mơ hồ thành con số đủ tốt để thiết kế: bao nhiêu QPS, request lớn cỡ nào, peak cao hơn average bao nhiêu, dữ liệu tăng ra sao, và cần bao nhiêu buffer. Con số ban đầu không cần đúng tuyệt đối, nhưng phải đủ rõ để kiểm chứng bằng monitoring và [[Load Testing]].

## Cơ chế

```text
requirements / DAU / event rate
-> average throughput
-> peak multiplier
-> request size + bandwidth
-> storage growth + retention
-> server/cache/database/queue capacity
-> alerts cho giả định quan trọng
```

## Điều cần đo

- Average QPS và [[Peak QPS]].
- Request/response size, ingress/egress bandwidth.
- Storage growth theo ngày/tháng/năm.
- Cache hit rate, queue depth, database latency.
- Headroom cho growth, traffic spike và rollout rủi ro.

## Pitfall

- Chỉ tính average QPS và quên peak.
- Quên egress bandwidth, đặc biệt với media/feed.
- Không biến giả định thành alert trong production.
- Overprovision quá nhiều gây tốn chi phí; underprovision tạo outage.

## Liên kết

- [[Peak QPS]]
- [[Load Testing]]
- [[Cost Optimization]]
- [[Observability]]
- [[Data Lifecycle Management]]
- [[Caching Strategy]]
