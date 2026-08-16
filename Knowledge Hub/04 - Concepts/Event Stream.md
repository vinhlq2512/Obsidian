---
type: concept
status: seed
sources:
  - "[[2025-05-08_messaging-patterns-explained-pub-sub-queues-and-event-stream]]"
  - "[[2023-09-14_why-is-kafka-so-fast-how-does-it-work]]"
  - "[[2023-08-17_how-to-choose-a-message-queue]]"
source_sections:
  - "[[2025-05-08_messaging-patterns-explained-pub-sub-queues-and-event-stream]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - messaging
  - streaming
---

# Event Stream

## Định nghĩa

[[Event Stream]] là chuỗi event immutable, append-only, có thứ tự trong từng partition và được giữ lại theo retention để nhiều consumer có thể đọc/replay độc lập.

## Cách hiểu bằng lời của tôi

Event stream không chỉ vận chuyển message. Nó giữ lịch sử. Consumer đọc bằng offset của riêng mình, có thể chạy chậm, rewind, backfill hoặc dựng lại read model mà không ảnh hưởng consumer khác.

## Cơ chế

```text
producer
-> append event vào topic/partition
-> broker giữ event theo retention
-> consumer group đọc bằng offset
-> downstream aggregate, index, cache hoặc materialized view
```

## Khi hữu ích

- CDC từ database transaction log.
- Clickstream, telemetry, metrics/log ingestion.
- Rebuild state hoặc backfill khi logic thay đổi.
- Nhiều downstream system đọc cùng một lịch sử event.

## Liên kết

- [[Event Log]]
- [[Apache Kafka]]
- [[Kafka Partition]]
- [[Consumer Group]]
- [[Materialized View]]
- [[Change Data Capture]]
