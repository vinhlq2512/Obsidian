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
  - distributed-systems
---

# Linearizability

## Định nghĩa

Linearizability là consistency guarantee cho operation đơn lẻ, nơi operation có vẻ xảy ra tức thời tại một điểm giữa lúc bắt đầu và kết thúc, và thứ tự quan sát tôn trọng thời gian thực.

## Cách hiểu bằng lời của tôi

Nếu write A hoàn tất trước khi read B bắt đầu, B phải thấy A hoặc trạng thái mới hơn. Đây là ngôn ngữ chính xác hơn cho nhiều điều ta gọi là strong consistency.

## Phân biệt

- Linearizability nói về ordering của operation theo real time.
- [[Serializability]] nói về transaction nhiều operation có kết quả như chạy tuần tự, nhưng thứ tự tuần tự không nhất thiết theo real time.
- Kết hợp cả hai thành [[Strict Serializability]].

## Liên kết

- [[Strong Consistency]]
- [[Consensus]]
- [[Database Transaction]]
- [[CAP and PACELC]]
