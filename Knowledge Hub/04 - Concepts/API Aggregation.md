---
type: concept
status: seed
sources:
  - "[[2026-08-13_a-detailed-guide-to-api-composition-techniques]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - api
  - latency
---

# API Aggregation

## Định nghĩa

API aggregation là dạng composition trong đó nhiều upstream độc lập được gọi song song rồi merge kết quả.

## Cách hiểu bằng lời của tôi

Nếu bốn call độc lập cùng mất 40 ms, aggregation cố làm tổng latency gần 40 ms thay vì 160 ms. Nó phù hợp khi các branch không phụ thuộc kết quả của nhau.

## Điều cần kiểm

- Branch nào là required, branch nào optional?
- Nếu một branch lỗi, toàn response lỗi hay trả partial response?
- Có timeout riêng cho từng branch không?
- Có cache được branch nào trước khi compose không?

## Liên kết

- [[API Composition]]
- [[API Orchestration]]
- [[Latency]]
- [[Partial Failure]]
- [[Graceful Degradation]]
