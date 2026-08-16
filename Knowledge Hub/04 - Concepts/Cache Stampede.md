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
  - caching
  - reliability
---

# Cache Stampede

## Định nghĩa

[[Cache Stampede]] là tình huống nhiều request cùng thấy một cache entry hết hạn/miss và đồng thời đánh vào backend để tái tạo dữ liệu.

## Cách hiểu bằng lời của tôi

Cache bảo vệ database khỏi traffic hot, nhưng nếu key hot hết hạn cùng lúc, backend có thể nhận đúng spike mà cache vốn được thêm để tránh. Đây là failure mode của cache invalidation và TTL đồng bộ.

## Cách giảm

- Lock/singleflight để chỉ một request rebuild cache.
- TTL có jitter để tránh expire đồng loạt.
- Serve stale while revalidate cho dữ liệu chấp nhận stale.
- Prewarm cache cho hot keys.
- Rate limit hoặc backpressure khi cache miss surge.

## Liên kết

- [[Caching Strategy]]
- [[Content Delivery Network]]
- [[Backpressure]]
- [[Rate Limiting]]
- [[Database Workload Isolation]]
