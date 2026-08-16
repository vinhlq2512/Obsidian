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

# Database Partitioning

## Định nghĩa

[[Database Partitioning]] là việc chia bảng/dataset thành các phần nhỏ hơn trong cùng một database hoặc engine để query và maintenance chỉ chạm vào phần dữ liệu liên quan.

## Cách hiểu bằng lời của tôi

Partitioning là "chia bảng lớn thành vùng dễ quản". Nếu query luôn lọc theo ngày, partition theo ngày/tháng giúp database bỏ qua partition không liên quan. Nó khác [[Database Sharding]]: partitioning thường vẫn trong một database/cluster logic, còn sharding phân phối dữ liệu qua nhiều server để scale ngang.

## Hai kiểu

- Horizontal partitioning: chia row theo key như date, region, tenant.
- Vertical partitioning: chia column, giữ field thường đọc ở bảng chính và đưa field nặng/ít dùng sang bảng khác.

## Trade-off

- Key partition phải match query pattern thật.
- Query xuyên nhiều partition có thể chậm.
- Maintenance, migration và constraint có thể phức tạp hơn.
- Không nên dùng partitioning để che schema/query design sai.

## Liên kết

- [[Database Sharding]]
- [[Query Planner]]
- [[Full Table Scan]]
- [[Database Schema Design]]
- [[Data Lifecycle Management]]
