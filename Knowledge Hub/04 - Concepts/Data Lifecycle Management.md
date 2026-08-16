---
type: concept
status: seed
sources:
  - "[[2025-03-18_how-netflix-stores-140-million-hours-of-viewing-data-per-day]]"
  - "[[2026-01-21_how-netflix-built-a-real-time-distributed-graph-for-internet]]"
  - "[[2025-02-11_how-netflix-built-a-distributed-counter-for-billions-of-user]]"
source_sections:
  - "[[2025-03-18_how-netflix-stores-140-million-hours-of-viewing-data-per-day]]"
  - "[[2026-01-21_how-netflix-built-a-real-time-distributed-graph-for-internet]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - data
  - system-design
---

# Data Lifecycle Management

## Định nghĩa

[[Data Lifecycle Management]] là tập chính sách quyết định dữ liệu được tạo, lưu, cache, nén, di chuyển, expire, archive hoặc xóa như thế nào trong suốt vòng đời của nó.

## Cách hiểu bằng lời của tôi

Dữ liệu không có cùng giá trị mãi mãi. Record vừa mới tạo có thể cần latency thấp và consistency tốt; vài tháng sau nó chỉ còn giá trị lịch sử; vài năm sau có thể chỉ cần summary. Lifecycle policy biến khác biệt đó thành kiến trúc storage cụ thể.

## Cơ chế thường gặp

- TTL để tự động expire dữ liệu không còn cần.
- Retention khác nhau cho raw event và aggregate.
- Data rotation từ cluster nhanh sang cluster rẻ hơn.
- Storage class tiering để chuyển object cũ/ít truy cập sang lớp lưu trữ rẻ hơn.
- Compression/downsampling cho dữ liệu cũ.
- Per-namespace/per-record/per-item expiration để kiểm soát graph hoặc event store phình ra.

## Câu hỏi thiết kế

- Dữ liệu mới/cũ được query khác nhau thế nào?
- Có cần audit/replay từ raw event không, hay aggregate là đủ?
- Dữ liệu nào được phép stale, dữ liệu nào phải read-your-writes?
- Expiration theo user, theo namespace hay theo item?

## Liên kết

- [[Time-Series Data Storage]]
- [[Event Log]]
- [[Caching Strategy]]
- [[Database Sharding]]
- [[Real-Time Graph Architecture]]
- [[Storage Class Tiering]]
- [[Cost Optimization]]
