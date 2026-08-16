---
type: concept
status: developing
sources:
  - "[[2026-08-06_the-read-path-versus-the-write-path-strategies-and-technique]]"
  - "[[2025-02-27_mastering-data-consistency-across-microservices]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - consistency
  - database
---

# Staleness

## Định nghĩa

Staleness là khoảng thời gian một bản sao hoặc read model giữ giá trị khác với source of truth sau khi source đã được cập nhật.

## Cách hiểu bằng lời của tôi

Staleness không phải luôn là bug. Nó là một cửa sổ thiết kế. Follower count chậm vài phút có thể chấp nhận được; account balance hoặc seat inventory chậm vài giây có thể gây lỗi nghiệp vụ nghiêm trọng.

## Câu hỏi thiết kế

- Field này chịu stale bao lâu?
- User có cần [[Read-Your-Writes Consistency]] không?
- Mean lag có che tail lag nguy hiểm không?
- Khi copy không hội tụ, observability nào báo cho mình biết?

## Liên kết

- [[Eventual Consistency]]
- [[Data Replication]]
- [[Read Replica]]
- [[Materialized View]]
- [[Change Data Capture]]
