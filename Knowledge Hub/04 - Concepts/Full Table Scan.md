---
type: concept
status: seed
sources:
  - "[[2024-12-12_database-performance-demystified-essential-tips-and-strategi]]"
  - "[[2026-04-02_database-performance-strategies-and-their-hidden-costs]]"
source_sections:
  - "[[2026-04-02_database-performance-strategies-and-their-hidden-costs]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - database
  - performance
---

# Full Table Scan

## Định nghĩa

[[Full Table Scan]] là khi database đọc toàn bộ row trong bảng để tìm dữ liệu phù hợp, thay vì dùng index hoặc partition pruning để thu hẹp phạm vi đọc.

## Cách hiểu bằng lời của tôi

Full table scan không luôn xấu: bảng nhỏ scan toàn bộ có thể rẻ hơn dùng index. Nhưng khi bảng tăng từ vài chục nghìn lên vài triệu row, cùng một query có thể từ nhanh thành bottleneck lớn. Đây là dấu hiệu cần xem lại index, filter, partitioning hoặc data model.

## Khi thường xảy ra

- Column trong `WHERE` không có index phù hợp.
- Function/cast trên column làm index khó dùng.
- Statistics sai khiến planner đánh giá sai selectivity.
- Query cần quá nhiều row nên index không còn lợi.
- Filter không match partition key.

## Liên kết

- [[Query Execution Plan]]
- [[Database Indexing]]
- [[Query Planner]]
- [[Database Partitioning]]
