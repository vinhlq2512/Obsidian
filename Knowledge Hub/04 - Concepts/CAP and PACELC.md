---
type: concept
status: understood
sources:
  - "[[2024-10-10_cap-pacelc-acid-base-essential-concepts-for-an-architects-to-newsletter]]"
  - "[[2025-07-24_consistency-and-partition-tolerance-understanding-cap-vs-pac]]"
source_sections:
  - "[[2024-10-10_cap-pacelc-acid-base-essential-concepts-for-an-architects-to-newsletter]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - distributed-systems
  - consistency
---

# CAP and PACELC

## Cách hiểu bằng lời của tôi

[[CAP and PACELC]] là hai khung suy nghĩ về trade-off consistency trong hệ phân tán. CAP nói khi có network partition, hệ thống phải chọn giữa consistency và availability. PACELC bổ sung câu hỏi quan trọng hơn trong vận hành bình thường: nếu không có partition, ta vẫn thường phải chọn giữa latency và consistency.

## CAP

- Consistency: mọi node nhìn thấy dữ liệu như nhau theo định nghĩa mạnh.
- Availability: mỗi request tới node còn sống đều nhận response.
- Partition tolerance: hệ vẫn tồn tại khi network chia cắt.

Trong thực tế distributed system phải chịu partition, nên câu hỏi thường là CP hay AP trong lúc partition, không phải chọn CA một cách trừu tượng.

## PACELC

```text
If Partition:
  choose Availability or Consistency
Else:
  choose Latency or Consistency
```

PACELC hữu ích vì nhiều trade-off diễn ra cả khi hệ thống không hỏng: replication sync cho consistency tốt hơn nhưng làm latency cao hơn; async cho latency thấp hơn nhưng có stale read.

## Liên kết

- [[Data Replication]]
- [[Eventual Consistency]]
- [[High Availability]]
