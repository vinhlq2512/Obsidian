---
type: concept
status: developing
sources:
  - "[[2026-08-06_the-read-path-versus-the-write-path-strategies-and-technique]]"
  - "[[2025-02-27_mastering-data-consistency-across-microservices]]"
  - "[[2025-09-09_how-netflix-tudum-supports-20-million-users-with-cqrs]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - architecture
  - database
---

# CQRS

## Định nghĩa

CQRS (Command Query Responsibility Segregation) là pattern tách model xử lý write command khỏi model phục vụ read query.

## Cách hiểu bằng lời của tôi

Một model khó vừa tối ưu cho write đúng vừa tối ưu cho read nhanh. CQRS chấp nhận hai model: write model bảo vệ invariant, read model được precompute/denormalize để đọc nhanh. Giá phải trả là đồng bộ và staleness giữa hai model.

## Ghi nhớ

- CQRS không bắt buộc event sourcing.
- CQRS không bắt buộc hai database.
- User có thể thấy write vừa commit chưa xuất hiện ở read model nếu sync bất đồng bộ.

## Case Tudum

Nguồn Netflix Tudum cho thấy CQRS không tự động giải quyết latency. Thiết kế ban đầu tách write path của editor khỏi read path cho visitor, dùng Kafka và Cassandra-backed read store. Vấn đề nằm ở preview: chuỗi xử lý tuần tự cộng với near-cache refresh theo lịch làm editor thấy dữ liệu stale. Netflix giữ nguyên nguyên tắc CQRS nhưng đổi read path sang [[In-Memory Read Model]], loại bớt network I/O và cho preview opt in [[Read-Your-Writes Consistency]].

## Liên kết

- [[Read Path]]
- [[Write Path]]
- [[Materialized View]]
- [[Eventual Consistency]]
- [[Staleness]]
- [[In-Memory Read Model]]
- [[Read-Your-Writes Consistency]]
