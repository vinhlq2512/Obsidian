---
type: concept
status: seed
sources:
  - "[[2026-03-31_how-meta-turned-debugging-into-a-product]]"
  - "[[2026-01-06_how-ai-transformed-database-debugging-at-databricks]]"
source_sections:
  - "[[2026-03-31_how-meta-turned-debugging-into-a-product]]"
  - "[[2026-01-06_how-ai-transformed-database-debugging-at-databricks]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - system-design
---

# Dependency Graph

## Định nghĩa

[[Dependency Graph]] mô tả quan hệ phụ thuộc giữa service, database, queue, region, config và downstream system để hỗ trợ điều tra blast radius và root cause.

## Cách hiểu bằng lời của tôi

Khi incident xảy ra, câu hỏi không chỉ là "metric nào đỏ" mà là "metric đỏ này phụ thuộc vào thứ gì". Dependency graph giúp automation biết nên gọi analyzer nào tiếp theo và giúp engineer tránh nhìn sai service gây triệu chứng.

## Liên kết

- [[Analyzer Chaining]]
- [[Distributed Tracing]]
- [[Blast Radius]]
- [[Hidden Dependency]]
- [[Service Discovery]]
