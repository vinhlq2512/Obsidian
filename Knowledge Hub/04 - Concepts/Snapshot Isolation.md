---
type: concept
status: seed
sources:
  - "[[2025-06-19_a-guide-to-database-transactions-from-acid-to-concurrency-co]]"
  - "[[2026-02-26_strong-consistency-in-databases-promises-and-costs]]"
source_sections:
  - "[[2025-06-19_a-guide-to-database-transactions-from-acid-to-concurrency-co]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - database
  - transaction
---

# Snapshot Isolation

## Định nghĩa

[[Snapshot Isolation]] là isolation model cho phép transaction đọc từ một snapshot nhất quán của database tại một thời điểm, thay vì thấy các thay đổi commit sau đó trong cùng transaction.

## Cách hiểu bằng lời của tôi

Snapshot isolation làm read ổn định hơn: transaction không bị "mặt đất đổi dưới chân" trong lúc đang chạy. Nó thường được triển khai bằng [[MVCC]]. Nhưng snapshot isolation không tự động bằng serializable trong mọi database; một số anomaly như write skew vẫn có thể xảy ra nếu invariant trải trên nhiều row.

## Cần nhớ

- Tốt cho long read/query cần view nhất quán.
- Giảm blocking giữa reader và writer.
- Vẫn cần hiểu conflict rule khi nhiều transaction cùng write.
- Không thay thế được [[Serializability]] khi invariant nghiệp vụ cần thứ tự tuần tự hoàn toàn.

## Liên kết

- [[MVCC]]
- [[Transaction Isolation]]
- [[Read-Your-Writes Consistency]]
- [[Serializability]]
- [[Strict Serializability]]
