---
type: concept
status: understood
sources:
  - "[[2025-08-14_a-guide-to-top-caching-strategies]]"
  - "[[2023-03-15_a-crash-course-in-caching-part-1-newsletter]]"
  - "[[2023-03-22_a-crash-course-in-caching-part-2-newsletter]]"
  - "[[2024-01-11_netflix-what-happens-when-you-press-play-part-2]]"
  - "[[2026-03-24_how-netflix-live-streams-to-100-million-devices-in-60-second]]"
source_sections:
  - "[[2025-08-14_a-guide-to-top-caching-strategies]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - system-design
---

# Caching Strategy

## Cách hiểu bằng lời của tôi

[[Caching Strategy]] là cách quyết định dữ liệu nào được giữ gần nơi đọc hơn, được cập nhật ra sao, và bị loại bỏ khi nào. Cache không chỉ để nhanh hơn; nó cũng là một điểm consistency/race-condition mới trong hệ thống.

## Write policy

- Write-through: write đi qua cache rồi xuống database; consistency tốt hơn nhưng write latency cao.
- Cache-aside: app đọc cache trước, miss thì đọc database rồi populate cache; write thường cập nhật database và invalidate cache.
- Write-back: write vào cache trước, flush xuống database sau; write nhanh nhưng mất dữ liệu nếu cache crash trước khi flush.

## Vấn đề phân tán

Distributed cache có thể stale vì invalidation thiếu, pub/sub update bị delay, concurrent update ghi đè nhau, hoặc node cache lệch trạng thái. Vì vậy cache cần TTL, versioned key, explicit invalidation, pub/sub sync hoặc chấp nhận [[Eventual Consistency]] rõ ràng.

## Pitfall

Thundering herd xảy ra khi một key nóng hết hạn và nhiều request cùng miss, đẩy tải về backend. Cách giảm: pre-warming, lock/token refresh, jitter TTL, stale-while-revalidate.

## Mở rộng từ video streaming

Với nội dung lớn và có thể dự đoán, cache có thể được fill chủ động trước khi user request. Netflix Open Connect là ví dụ: video được copy tới OCA theo dự đoán nhu cầu địa phương. Với live streaming, cache policy còn dùng để giảm storm: 404/503 có TTL ngắn giúp edge không lặp lại cùng request về origin trong vài giây.

## Liên kết

- [[Content Delivery Network]]
- [[Rate Limiting]]
- [[Eventual Consistency]]
- [[Scalable Distributed Systems Patterns]]
- [[Proactive Caching]]
- [[Live Streaming Origin]]
