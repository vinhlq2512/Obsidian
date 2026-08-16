---
type: concept
status: seed
sources:
  - "[[2023-09-14_why-is-kafka-so-fast-how-does-it-work]]"
  - "[[2025-05-08_messaging-patterns-explained-pub-sub-queues-and-event-stream]]"
  - "[[2023-08-17_how-to-choose-a-message-queue]]"
  - "[[2026-03-17_how-reddit-migrated-petabyte-scale-kafka-from-ec2-to-kuberne]]"
  - "[[2025-10-06_how-openai-uses-kubernetes-and-apache-kafka-for-genai]]"
source_sections:
  - "[[2023-09-14_why-is-kafka-so-fast-how-does-it-work]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - kafka
  - messaging
  - streaming
---

# Apache Kafka

## Định nghĩa

[[Apache Kafka]] là distributed event streaming platform xây quanh topic/partition append-only log, cho phép producer ghi event và nhiều consumer đọc/replay theo offset.

## Cách hiểu bằng lời của tôi

Kafka giống một log phân tán hơn là queue truyền thống. Message không biến mất khi một consumer đọc xong; broker giữ event theo retention, còn consumer tự quản lý vị trí đọc. Vì vậy Kafka hợp với analytics, telemetry, CDC, stream processing và nhiều read model cùng sinh từ một event history.

## Kiến trúc

- Producer: ghi event vào topic.
- Broker: lưu partition, nhận write/read, replicate dữ liệu.
- Topic: luồng logic của một loại event.
- [[Kafka Partition]]: log ordered, append-only, là đơn vị scale và ordering.
- Consumer: đọc event theo offset.
- [[Consumer Group]]: chia partition cho nhiều consumer để xử lý song song.
- Control plane: quản lý metadata cluster; hiện đại hơn có KRaft thay ZooKeeper.

## Vì sao Kafka nhanh

- Append-only log tạo sequential I/O.
- Batching giảm số network/disk operation nhỏ.
- Compression/SerDes giảm bytes truyền.
- Zero-copy giảm copy dữ liệu giữa kernel và application khi gửi tới consumer.
- Broker giữ logic tương đối đơn giản để scale bằng partition/broker.

## Trade-off

- Không phù hợp nếu chỉ cần delay queue đơn giản hoặc transactional task nhỏ.
- Ordering chỉ mạnh trong một partition.
- Consumer lag, partition skew và rebalance là các vấn đề vận hành chính.
- Exactly-once/transaction có overhead và cần chọn commit interval cẩn thận.

## Liên kết

- [[Event Stream]]
- [[Kafka Partition]]
- [[Consumer Group]]
- [[Delivery Semantics]]
- [[Message Broker]]
- [[Zero-Downtime Infrastructure Migration]]
