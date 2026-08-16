---
type: concept
status: developing
sources:
  - "[[2025-02-27_mastering-data-consistency-across-microservices]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - microservices
  - consistency
---

# Saga Pattern

## Định nghĩa

Saga pattern là cách duy trì consistency cho workflow nhiều service bằng chuỗi local transactions và compensating actions thay vì một distributed transaction khóa nhiều database.

## Cách hiểu bằng lời của tôi

Trong microservices, mỗi service sở hữu database riêng. Nếu order, payment và shipping cùng tham gia một nghiệp vụ, saga chia workflow thành từng bước local; nếu bước sau fail thì phát event hoặc gọi action bù để đưa hệ về trạng thái chấp nhận được.

## Hai kiểu điều phối

- Choreography: service phát/nghe event, không có controller trung tâm.
- Orchestration: một orchestrator quyết định bước tiếp theo và gọi service liên quan.

## Trade-off

- Giảm coupling và tránh distributed lock dài.
- Khó debug hơn transaction đơn vì state nằm rải qua event/service.
- Compensation không phải lúc nào cũng hoàn tác hoàn hảo, nhất là khi side effect đã ra ngoài.

## Liên kết

- [[Eventual Consistency]]
- [[Message Broker]]
- [[Transactional Outbox]]
- [[API Orchestration]]
- [[Database Transaction]]
