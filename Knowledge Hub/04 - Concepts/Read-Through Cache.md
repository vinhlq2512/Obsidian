---
type: concept
status: understood
sources:
  - "[[2024-11-21_distributed-caching-the-secret-to-high-performance-applicati]]"
source_sections:
  - "[[2024-11-21_distributed-caching-the-secret-to-high-performance-applicati]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - caching
  - system-design
---

# Read-Through Cache

## Định nghĩa

Read-Through Cache là chiến lược trong đó mọi read đi qua cache; nếu miss, cache layer tự lấy dữ liệu từ database rồi lưu lại.

## Cách hiểu bằng lời của tôi

Khác với [[Cache-Aside]], read-through đẩy logic miss handling xuống cache layer. Application thấy một interface đọc thống nhất, còn cache chịu trách nhiệm fetch và populate.

## Trade-off

- Giảm code cache trong application.
- Phù hợp khi cache provider hoặc middleware hỗ trợ tích hợp với data source.
- Đổi lại, application có ít quyền kiểm soát hơn về dữ liệu nào được populate và khi nào.

## Liên kết

- [[Caching Strategy]]
- [[Cache-Aside]]
- [[Distributed Cache]]
- [[Cache Invalidation]]
