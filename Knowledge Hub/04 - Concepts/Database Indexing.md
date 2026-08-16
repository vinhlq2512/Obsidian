---
type: concept
status: understood
sources:
  - "[[2025-06-26_database-indexing-demystified-index-types-and-use-cases-newsletter]]"
  - "[[2023-07-06_database-indexing-strategies-newsletter]]"
  - "[[2023-08-03_database-indexing-strategies-part-2-newsletter]]"
  - "[[2024-12-12_database-performance-demystified-essential-tips-and-strategi]]"
  - "[[2026-04-02_database-performance-strategies-and-their-hidden-costs]]"
source_sections:
  - "[[2025-06-26_database-indexing-demystified-index-types-and-use-cases-newsletter]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - database
  - system-design
---

# Database Indexing

## Cách hiểu bằng lời của tôi

[[Database Indexing]] là tạo cấu trúc dữ liệu phụ để database tìm record nhanh hơn mà không scan toàn bảng. Index là trade-off: tăng tốc read/query nhưng làm write chậm hơn, tốn storage hơn, và cần maintenance khi dữ liệu thay đổi.

## Điều cần quyết định

- Query pattern nào thật sự quan trọng.
- Column nào dùng để filter, sort, join hoặc range query.
- Cardinality/selectivity của column có đủ tốt không.
- Index có làm write path hoặc storage cost quá nặng không.

## Mental model

Index giống mục lục: đọc nhanh hơn vì biết đi đâu, nhưng mỗi lần sách thay đổi thì mục lục cũng phải cập nhật. Index sai có thể không được query planner dùng, hoặc dùng nhưng không đáng chi phí.

## Khi đọc execution plan

Index chỉ có giá trị khi [[Query Planner]] thật sự dùng nó cho query quan trọng. `EXPLAIN`/`EXPLAIN ANALYZE` giúp kiểm tra query đang index scan hay [[Full Table Scan]], join có dùng indexed columns không, và statistics có khiến planner chọn sai plan không.

## Liên kết

- [[B-Tree]]
- [[LSM Tree]]
- [[Query Execution Plan]]
- [[Query Planner]]
- [[Read Path]]
- [[Write Path]]
- [[Database Schema Design]]
- [[Database Sharding]]
- [[Scalable Distributed Systems Patterns]]
