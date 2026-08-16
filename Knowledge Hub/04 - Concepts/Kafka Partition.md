---
type: concept
status: seed
sources:
  - "[[2023-09-14_why-is-kafka-so-fast-how-does-it-work]]"
  - "[[2025-05-08_messaging-patterns-explained-pub-sub-queues-and-event-stream]]"
  - "[[2026-03-17_how-reddit-migrated-petabyte-scale-kafka-from-ec2-to-kuberne]]"
source_sections:
  - "[[2023-09-14_why-is-kafka-so-fast-how-does-it-work]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - kafka
  - streaming
---

# Kafka Partition

## Định nghĩa

[[Kafka Partition]] là một append-only ordered log bên trong topic Kafka, nơi event có offset tăng dần và được replicate giữa brokers.

## Cách hiểu bằng lời của tôi

Partition là đơn vị vừa giữ ordering vừa tạo scale. Muốn nhiều throughput hơn thì tăng partition/broker, nhưng ordering chỉ được đảm bảo trong từng partition. Vì vậy chọn partition key là quyết định kiến trúc, không phải chi tiết config.

## Cơ chế

- Producer ghi event vào partition, thường theo key/hash.
- Event trong partition có offset tăng dần.
- Một broker giữ leader replica; follower replica fetch để bắt kịp.
- Consumer trong cùng group được assign partition; một partition chỉ thuộc một consumer trong group tại một thời điểm.
- Rebalance xảy ra khi consumer join/leave hoặc partition assignment đổi.

## Trade-off

- Partition quá ít giới hạn parallelism.
- Partition quá nhiều tăng metadata, file handle, rebalance và operational overhead.
- Hot key tạo hot partition dù tổng cluster còn rảnh.
- Migration Kafka phải bảo vệ partition leadership, replica placement và metadata.

## Liên kết

- [[Apache Kafka]]
- [[Consumer Group]]
- [[Database Sharding]]
- [[Leader Election]]
- [[Data Replication]]
