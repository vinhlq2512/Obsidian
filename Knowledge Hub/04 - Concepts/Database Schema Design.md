---
type: concept
status: seed
sources:
  - "[[2025-06-12_database-schema-design-simplified-normalization-vs-denormali-newsletter]]"
  - "[[2025-07-02_netflix-ended-data-chaos-with-unified-domain-models]]"
  - "[[2026-04-16_a-guide-to-relational-database-design]]"
  - "[[2026-04-02_database-performance-strategies-and-their-hidden-costs]]"
  - "[[2025-09-17_the-pain-of-joins-in-mongodb-byte-sized-design]]"
source_sections:
  - "[[2025-06-12_database-schema-design-simplified-normalization-vs-denormali-newsletter]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - database
  - system-design
---

# Database Schema Design

## Cách hiểu bằng lời của tôi

[[Database Schema Design]] là cách mô hình hóa dữ liệu để cân bằng correctness, query performance, khả năng thay đổi và chi phí vận hành. Normalization giảm trùng lặp và giữ integrity tốt hơn; denormalization đổi thêm storage/duplication để đọc nhanh hoặc đơn giản hơn ở scale.

## Trade-off chính

- Normalization: dữ liệu sạch, ít duplication, dễ giữ invariant; query có thể cần nhiều join.
- Denormalization: read path nhanh hơn hoặc đơn giản hơn; write path phải cập nhật nhiều bản sao và dễ inconsistency.
- Document model: lưu chung dữ liệu thường đọc chung, nhưng phải tránh biến mỗi query thành nhiều join runtime.
- Schema không tĩnh: khi workload đổi, schema tối ưu hôm nay có thể thành bottleneck ngày mai.

## Khi áp dụng

Thiết kế schema nên bắt đầu từ access pattern quan trọng: hệ đọc-heavy, write-heavy, analytics, transactional hay event-driven sẽ cần shape khác nhau.

## Schema và semantics

Schema không chỉ là column/type. Ở hệ nhiều team, cùng một entity nghiệp vụ có thể bị định nghĩa khác nhau giữa API, database và pipeline. [[Unified Domain Model]] giải quyết tầng này bằng cách định nghĩa business entity một lần rồi generate/project ra schema cụ thể, giảm schema drift và integration debt.

## Liên kết

- [[Database Indexing]]
- [[Database Sharding]]
- [[Database Partitioning]]
- [[Join Operation]]
- [[Document Store]]
- [[Eventual Consistency]]
- [[Unified Domain Model]]
- [[API Contract]]
