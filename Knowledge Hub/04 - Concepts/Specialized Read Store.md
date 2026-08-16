---
type: concept
status: seed
sources:
  - "[[2026-08-06_the-read-path-versus-the-write-path-strategies-and-technique]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - database
  - architecture
---

# Specialized Read Store

## Định nghĩa

Specialized read store là hệ lưu trữ riêng được tối ưu cho một dạng query mà transactional database chính không phục vụ tốt.

## Cách hiểu bằng lời của tôi

Full-text search, graph traversal, vector search và analytics đều cần physical layout khác nhau. Khi database chính không thể tối ưu tất cả, ta tạo một read store riêng và đồng bộ dữ liệu sang đó.

## Sync mechanisms

- Dual-write: đơn giản nhưng dễ drift nếu write thứ hai fail.
- [[Change Data Capture]]: đọc log thay đổi từ storage engine.
- [[Transactional Outbox]]: ghi state change và event trong cùng transaction rồi publish sau.

## Failure mode

Silent drift: read store thiếu record hoặc tụt lại mà không báo lỗi rõ, khiến kết quả sai trông giống kết quả bình thường.

## Liên kết

- [[Read Path]]
- [[Vector Search Infrastructure]]
- [[Semantic Search]]
- [[Materialized View]]
- [[Staleness]]
