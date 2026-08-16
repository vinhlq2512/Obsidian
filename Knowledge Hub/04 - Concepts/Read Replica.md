---
type: concept
status: developing
sources:
  - "[[2026-08-06_the-read-path-versus-the-write-path-strategies-and-technique]]"
  - "[[2025-07-03_a-guide-to-database-replication-key-concepts-and-strategies]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - database
  - replication
---

# Read Replica

## Định nghĩa

Read replica là bản sao database dùng để phục vụ read traffic, thường được cập nhật bất đồng bộ từ primary.

## Cách hiểu bằng lời của tôi

Read replica scale read throughput, không scale write throughput. Mỗi replica vẫn phải apply mọi write từ primary, nên khi write đã saturate primary thì thêm replica không giải quyết gốc rễ.

## Failure mode

User vừa write xong rồi reload nhưng request đọc bị route sang replica chưa bắt kịp, nên thấy giá trị cũ. Đây là vấn đề [[Staleness]]/replication lag.

## Cách giảm lỗi đọc stale

- Route read sau write về primary trong một khoảng ngắn.
- Route những query known-after-write về primary.
- Mang version token và chờ replica đã apply tới version đó.

## Liên kết

- [[Data Replication]]
- [[Read Path]]
- [[Read-Your-Writes Consistency]]
- [[Eventual Consistency]]
