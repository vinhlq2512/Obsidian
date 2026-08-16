---
type: concept
status: seed
sources:
  - "[[2026-01-06_how-ai-transformed-database-debugging-at-databricks]]"
  - "[[2026-03-31_how-meta-turned-debugging-into-a-product]]"
source_sections:
  - "[[2026-01-06_how-ai-transformed-database-debugging-at-databricks]]"
  - "[[2026-03-31_how-meta-turned-debugging-into-a-product]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - debugging
  - reliability
---

# Context Gathering

## Định nghĩa

[[Context Gathering]] là bước gom baseline, metrics, logs, query traces, deploy/config changes và owner knowledge trước khi đưa ra giả thuyết nguyên nhân.

## Cách hiểu bằng lời của tôi

Trong incident, rất nhiều thời gian không nằm ở "sửa lỗi" mà ở tìm xem chuyện gì đang xảy ra. Tự động hóa context gathering là cách giảm MTTR mà chưa cần auto-remediation.

## Liên kết

- [[Observability]]
- [[Distributed Tracing]]
- [[Debugging as Code]]
- [[Diagnostic Agent]]
- [[Incident Response]]
