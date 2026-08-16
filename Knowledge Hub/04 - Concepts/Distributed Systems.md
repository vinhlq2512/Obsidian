---
type: concept
status: seed
sources:
  - "[[2024-07-11_a-crash-course-on-distributed-systems-newsletter]]"
  - "[[2023-09-07_how-to-choose-a-replication-strategy]]"
  - "[[2024-08-08_a-crash-course-on-microservices-design-patterns-newsletter]]"
source_sections:
  - "[[2024-07-11_a-crash-course-on-distributed-systems-newsletter]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - distributed-systems
  - system-design
---

# Distributed Systems

## Cách hiểu bằng lời của tôi

[[Distributed Systems]] là hệ gồm nhiều node độc lập phối hợp qua network để cung cấp một chức năng chung. Lợi ích là scale, fault tolerance và locality; cái giá là latency, partial failure, consistency, coordination và observability đều khó hơn hệ đơn node.

## Câu hỏi cốt lõi

- Dữ liệu nằm ở đâu và được replicate thế nào?
- Node nào được quyền nhận write?
- Khi network chậm hoặc partition, hệ thống ưu tiên availability hay consistency?
- Request đi qua những service nào và được trace ra sao?
- Khi một phần lỗi, phần còn lại degrade hay sập dây chuyền?

## Liên kết

- [[Data Replication]]
- [[Eventual Consistency]]
- [[Message Broker]]
- [[Observability]]
