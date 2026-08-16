---
type: concept
status: understood
sources:
  - "[[2023-10-12_the-6-most-impactful-ways-redis-is-used-in-production-system]]"
source_sections:
  - "[[2023-10-12_the-6-most-impactful-ways-redis-is-used-in-production-system]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - distributed-systems
  - redis
---

# Distributed Lock

## Định nghĩa

Distributed Lock là cơ chế mutual exclusion giữa nhiều process hoặc service instance để chỉ một actor được thao tác lên tài nguyên chung tại một thời điểm.

## Cách hiểu bằng lời của tôi

Redis có thể làm lock service đơn giản vì command được xử lý tuần tự và thao tác như `SET key value NX PX timeout` có tính atomic. Nhưng distributed lock rất dễ sai nếu không có timeout, owner token và quy tắc release đúng.

## Cơ chế Redis cơ bản

- Client acquire lock bằng set-if-not-exists với TTL.
- Value nên là unique owner id.
- Chỉ owner hiện tại mới được release lock.
- TTL tránh lock sống mãi khi owner crash.

## Giới hạn

- Ở throughput cực cao, acquire/release lock có thể thành bottleneck.
- Không có fairness/order guarantee mạnh.
- Với tài nguyên cực quan trọng, cần đánh giá dedicated lock/coordination service.

## Liên kết

- [[Redis]]
- [[Leader Election]]
- [[Consensus]]
- [[Concurrency Control]]
