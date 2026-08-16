---
type: concept
status: seed
sources:
  - "[[2026-01-21_how-netflix-built-a-real-time-distributed-graph-for-internet]]"
  - "[[2025-07-02_netflix-ended-data-chaos-with-unified-domain-models]]"
source_sections:
  - "[[2026-01-21_how-netflix-built-a-real-time-distributed-graph-for-internet]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - system-design
  - graph
---

# Real-Time Graph Architecture

## Định nghĩa

[[Real-Time Graph Architecture]] là kiến trúc ingest event liên tục rồi cập nhật node/edge để các ứng dụng có thể query quan hệ gần realtime ở scale lớn.

## Cách hiểu bằng lời của tôi

Graph hữu ích khi câu hỏi là "A liên quan tới B qua những cạnh nào" thay vì chỉ lookup một row. Nhưng graph realtime ở scale lớn không nhất thiết phải dùng native graph database; có thể biểu diễn node/edge bằng key-value/document storage nếu access pattern chủ yếu là traversal theo adjacency list.

## Luồng xử lý

```text
Kafka topics
-> stream processor
-> filter/project/enrich events
-> transform thành node và edge
-> ghi vào graph storage theo namespace
-> query bằng lookup/traversal theo key
```

## Pattern từ nguồn Netflix RDG

- Kafka làm ingestion backbone durable và replayable.
- Flink xử lý event gần realtime, lọc noise và enrich bằng side input.
- Mỗi node type và edge type có topic/namespace riêng để scale và tune độc lập.
- Property graph model biểu diễn entity bằng node và interaction/relationship bằng edge.
- Key-value abstraction trên Cassandra được chọn vì phù hợp operational reality hơn native graph database.

## Trade-off

- Nhiều namespace/topic làm vận hành phức tạp hơn nhưng tạo isolation.
- Key-value graph storage nhanh cho adjacency lookup, nhưng không thay thế mọi kiểu graph query sâu/phức tạp.
- Cần lifecycle policy để edge cũ không làm graph tăng vô hạn.

## Liên kết

- [[Property Graph]]
- [[Key-Value Graph Storage]]
- [[Message Broker]]
- [[Event Log]]
- [[Data Lifecycle Management]]
- [[Unified Domain Model]]
