---
type: concept
status: understood
sources:
  - "[[2025-05-15_engineering-trade-offs-eventual-consistency-in-practice-newsletter]]"
  - "[[2024-08-08_a-crash-course-on-microservices-design-patterns-newsletter]]"
  - "[[2023-09-07_how-to-choose-a-replication-strategy]]"
  - "[[2026-08-06_the-read-path-versus-the-write-path-strategies-and-technique]]"
  - "[[2025-02-27_mastering-data-consistency-across-microservices]]"
source_sections:
  - "[[2025-05-15_engineering-trade-offs-eventual-consistency-in-practice-newsletter]]"
  - "[[2023-09-07_how-to-choose-a-replication-strategy]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - distributed-systems
  - consistency
---

# Eventual Consistency

## Cách hiểu bằng lời của tôi

[[Eventual Consistency]] nghĩa là các bản sao hoặc service có thể tạm thời nhìn thấy state khác nhau, nhưng nếu không có update mới và quá trình đồng bộ hoàn tất, chúng sẽ hội tụ về cùng một kết quả. Đây là một trade-off để lấy availability, latency thấp hoặc khả năng scale trong hệ phân tán.

## Khi nào xuất hiện

- Async replication giữa primary và replica.
- Multi-leader hoặc leaderless replication có conflict/lag.
- Microservices mỗi service sở hữu database riêng.
- Workflow event-driven dùng message broker.
- Read model trong CQRS cập nhật chậm hơn write model.

## Điều cần thiết kế

- Người dùng có chịu được stale data không.
- Invariant nào bắt buộc strong consistency.
- Conflict được phát hiện và giải quyết ở đâu.
- UI/API truyền đạt trạng thái pending như thế nào.
- Retry/deduplication có làm side effect bị lặp không.

## Trade-off cần nhớ

Eventual consistency không phải "dữ liệu sai cũng được". Nó yêu cầu thiết kế rõ ràng về cửa sổ không nhất quán, compensation, conflict resolution và observability để biết khi hệ thống không hội tụ.

ByteByteGo nhấn mạnh eventual consistency là claim về điểm cuối của [[Staleness]]: các copy sẽ hội tụ nếu quá trình sync hoàn tất và không có update mới. Nếu không đo tail lag, retry backlog hoặc consumer lag, hệ thống có thể "eventual" trên lý thuyết nhưng không hội tụ trong thời gian user chịu được.

## Liên kết

- [[Data Replication]]
- [[Message Broker]]
- [[Idempotency Key]]
- [[Microservices Design Patterns]]
- [[Staleness]]
- [[Read Replica]]
- [[CQRS]]
- [[Saga Pattern]]
