---
type: concept
status: understood
sources:
  - "[[2026-03-03_how-agoda-built-a-single-source-of-truth-for-financial-data]]"
source_sections:
  - "[[2026-03-03_how-agoda-built-a-single-source-of-truth-for-financial-data]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - data-engineering
  - system-design
---

# Data Contract

## Định nghĩa

Data Contract là thỏa thuận chính thức giữa producer và consumer về schema, rule, ý nghĩa field và điều kiện chất lượng của dữ liệu.

## Cách hiểu bằng lời của tôi

Data contract biến dữ liệu thành interface. Nếu API có contract để tránh phá client, data pipeline cũng cần contract để tránh producer đổi field hoặc logic làm downstream sai âm thầm.

## Hai kiểu trong source Agoda

- Detection contract: kiểm tra dữ liệu production và alert khi vi phạm.
- Preventative contract: chạy trong CI của upstream producer để chặn lỗi trước khi dữ liệu được publish.

## Liên kết

- [[Financial Source of Truth]]
- [[API Contract]]
- [[Backward Compatibility]]
- [[Data Freshness]]
- [[Observability]]
