---
type: concept
status: seed
sources:
  - "[[2023-06-29_capacity-planning]]"
source_sections:
  - "[[2023-06-29_capacity-planning]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - performance
  - system-design
---

# Peak QPS

## Định nghĩa

[[Peak QPS]] là tốc độ request cao nhất hệ thống cần xử lý trong một khoảng thời gian quan trọng, thường cao hơn nhiều so với average QPS.

## Cách hiểu bằng lời của tôi

Average QPS giúp hiểu nền tải bình thường; peak QPS mới quyết định hệ thống có sống sót qua giờ cao điểm, launch, flash sale hoặc incident recovery không. Khi chưa có dữ liệu lịch sử, có thể dùng giả định phân bố như 80% traffic rơi vào 20% thời gian, rồi thêm buffer và kiểm chứng sau.

## Công thức trực giác

```text
average_qps = total_requests_per_day / 86400
peak_qps ~= requests_in_peak_window / seconds_in_peak_window
```

Ví dụ nguồn ByteByteGo dùng 5B pageviews/ngày và giả định 80% pageviews xảy ra trong 8 giờ:

```text
4B / 8h / 3600 ~= 138k QPS
```

## Cần nhớ

- Peak có thể do thời gian, event, marketing, retry storm hoặc failover.
- Autoscaling giúp nhưng không thay thế load test và capacity headroom.
- Peak QPS phải đi cùng request size, vì bandwidth và CPU phụ thuộc payload.

## Liên kết

- [[Capacity Planning]]
- [[Load Testing]]
- [[Rate Limiting]]
- [[Load Shedding]]
- [[Kubernetes Autoscaling|Autoscaling]]
