---
type: concept
status: seed
sources:
  - "[[2024-12-12_database-performance-demystified-essential-tips-and-strategi]]"
  - "[[2026-04-02_database-performance-strategies-and-their-hidden-costs]]"
source_sections:
  - "[[2024-12-12_database-performance-demystified-essential-tips-and-strategi]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - database
  - performance
---

# Database Workload Isolation

## Định nghĩa

[[Database Workload Isolation]] là chiến lược tách hoặc giới hạn tài nguyên giữa các workload database khác nhau, ví dụ user-facing queries, batch jobs, ETL, analytics và maintenance.

## Cách hiểu bằng lời của tôi

Một database có thể nhanh khi chạy từng workload riêng, nhưng chậm khi batch job và request realtime tranh CPU/I/O/cache cùng lúc. Workload isolation đặt ranh giới để query user-facing không bị ETL hoặc import đêm kéo xuống.

## Cách làm

- Schedule batch job ngoài giờ cao điểm.
- Dùng resource groups/quotas cho CPU, memory, I/O.
- Tách read replica, warehouse hoặc specialized read store cho analytics.
- Chia batch lớn thành incremental chunks.
- Monitor latency của critical path, không chỉ tổng CPU.

## Liên kết

- [[Read Replica]]
- [[Materialized View]]
- [[Specialized Read Store]]
- [[Capacity Planning]]
- [[Load Testing]]
- [[Database Performance Tradeoffs]]
