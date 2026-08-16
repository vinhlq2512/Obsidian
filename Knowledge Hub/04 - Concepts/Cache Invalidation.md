---
type: concept
status: understood
sources:
  - "[[2024-11-21_distributed-caching-the-secret-to-high-performance-applicati]]"
  - "[[2023-10-12_the-6-most-impactful-ways-redis-is-used-in-production-system]]"
source_sections:
  - "[[2024-11-21_distributed-caching-the-secret-to-high-performance-applicati]]"
  - "[[2023-10-12_the-6-most-impactful-ways-redis-is-used-in-production-system]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - caching
  - system-design
---

# Cache Invalidation

## Định nghĩa

Cache Invalidation là cơ chế xóa hoặc cập nhật cached value khi dữ liệu gốc thay đổi hoặc khi cached value quá cũ.

## Cách hiểu bằng lời của tôi

Cache giúp nhanh hơn bằng cách chấp nhận nhiều bản copy của dữ liệu. Invalidation là phần trả nợ: hệ thống phải quyết định lúc nào bản copy không còn đáng tin và phải được xóa, refresh hoặc thay bằng bản mới.

## Cơ chế

- TTL: tự hết hạn sau một khoảng thời gian.
- Event-based invalidation: update database phát event để cache xóa/cập nhật key liên quan.
- Manual invalidation: ứng dụng chủ động xóa cache trong write path.
- Leasing: giới hạn một updater cho cache entry để tránh xung đột write.

## Trade-off

- TTL ngắn giảm stale data nhưng tăng cache miss.
- TTL dài tăng hit rate nhưng có thể phục vụ dữ liệu cũ.
- Event-based chính xác hơn nhưng làm architecture phức tạp hơn.

## Liên kết

- [[Caching Strategy]]
- [[Cache Stampede]]
- [[Data Freshness]]
- [[Eventual Consistency]]
