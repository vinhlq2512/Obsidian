---
type: concept
status: developing
sources:
  - "[[2026-08-06_the-read-path-versus-the-write-path-strategies-and-technique]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - database
  - performance
---

# Read Path

## Định nghĩa

Read path là đường xử lý dùng để trả lời câu hỏi từ dữ liệu đã lưu, ví dụ lookup, query, render profile, search hoặc aggregate.

## Cách hiểu bằng lời của tôi

Read path muốn câu trả lời đã được chuẩn bị sẵn, nằm gần nơi cần đọc, ít coordination và đọc song song tốt. Vì vậy các tối ưu read thường tạo copy: index, cache, read replica, materialized view hoặc read store riêng.

## Pattern thường gặp

- [[Database Indexing]] để lookup/range query nhanh hơn.
- [[Caching Strategy]] để tránh tính lại hoặc gọi origin.
- [[Read Replica]] để tách read traffic khỏi primary.
- [[Materialized View]] để lưu kết quả query đã tính trước.
- [[Specialized Read Store]] cho search, analytics hoặc graph traversal.

## Trade-off

Mọi read optimization đều đẩy một phần chi phí sang [[Write Path]] hoặc background sync. Câu hỏi không phải "có copy không", mà là copy ở đâu, ai cập nhật, và được stale bao lâu.

## Liên kết

- [[Write Path]]
- [[Staleness]]
- [[CQRS]]
- [[Read-Your-Writes Consistency]]
