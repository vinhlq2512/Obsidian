---
type: concept
status: seed
sources:
  - "[[2026-02-26_strong-consistency-in-databases-promises-and-costs]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - consistency
  - database
---

# Strict Serializability

## Định nghĩa

Strict serializability là guarantee kết hợp serializable transactions với real-time ordering của linearizability.

## Cách hiểu bằng lời của tôi

Transaction vẫn có vẻ chạy tuần tự, và nếu T1 kết thúc trước khi T2 bắt đầu thì T2 phải thấy effect của T1. Đây là guarantee rất mạnh, nhưng thường cần coordination đắt.

## Ví dụ từ ByteByteGo

Google Spanner đạt external consistency bằng TrueTime và commit wait: khi commit, hệ thống chờ uncertainty window qua đi để timestamp của transaction sau chắc chắn lớn hơn.

## Liên kết

- [[Serializability]]
- [[Linearizability]]
- [[Strong Consistency]]
- [[Consensus]]
