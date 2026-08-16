---
type: concept
status: seed
sources:
  - "[[2026-02-26_strong-consistency-in-databases-promises-and-costs]]"
  - "[[2025-06-19_a-guide-to-database-transactions-from-acid-to-concurrency-co]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - database
  - transaction
---

# Serializability

## Định nghĩa

Serializability là isolation guarantee trong đó kết quả của các transaction đồng thời tương đương với một thứ tự chạy tuần tự nào đó.

## Cách hiểu bằng lời của tôi

Serializability bảo vệ invariant khi nhiều transaction cùng chạm nhiều object. Nó không nhất thiết bảo đảm thứ tự tuần tự khớp với thời gian thực; đó là phần [[Linearizability]] bổ sung.

## Liên kết

- [[Transaction Isolation]]
- [[Database Transaction]]
- [[Strict Serializability]]
- [[Concurrency Control]]
