---
type: concept
status: seed
sources:
  - "[[2026-01-21_how-netflix-built-a-real-time-distributed-graph-for-internet]]"
source_sections:
  - "[[2026-01-21_how-netflix-built-a-real-time-distributed-graph-for-internet]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - graph
  - database
---

# Key-Value Graph Storage

## Định nghĩa

[[Key-Value Graph Storage]] là cách lưu graph trên key-value/document store, thường bằng cách gom adjacency list hoặc edge items theo key để traversal phổ biến thành point lookup nhanh.

## Cách hiểu bằng lời của tôi

Nếu query chính là "lấy các cạnh xuất phát từ node này", ta có thể lưu mỗi origin node như một record chứa nhiều edge item. Như vậy traversal một bước trở thành một lookup key-value, đổi lại các query graph tổng quát hoặc traversal sâu cần logic riêng.

## Pattern từ nguồn Netflix

- Mỗi node type/edge type nằm trong namespace riêng.
- Namespace có thể map tới cluster/storage backend riêng để scale độc lập.
- Khi edge mới có cùng origin, storage thêm item vào record hiện có.
- Khi ingest cùng node/edge, storage overwrite giá trị cũ để giữ property mới.
- TTL/expiration có thể đặt theo namespace, record hoặc item để kiểm soát growth.

## Trade-off

- Tối ưu rất tốt cho adjacency lookup và workload đã biết.
- Tránh phải vận hành native graph database nếu tổ chức đã mạnh về key-value/Cassandra.
- Không nên giả định nó hỗ trợ tự nhiên mọi query graph phức tạp như shortest path hoặc traversal sâu nhiều hop.

## Liên kết

- [[Real-Time Graph Architecture]]
- [[Property Graph]]
- [[Database Sharding]]
- [[Data Lifecycle Management]]
- [[Cassandra]]
