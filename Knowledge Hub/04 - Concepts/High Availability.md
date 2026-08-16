---
type: concept
status: understood
sources:
  - "[[2024-02-08_what-is-high-availability-newsletter]]"
  - "[[2024-08-29_a-crash-course-on-load-balancers-for-scaling]]"
  - "[[2023-09-07_how-to-choose-a-replication-strategy]]"
  - "[[2025-08-07_top-strategies-to-improve-reliability-in-distributed-systems-part-1]]"
source_sections:
  - "[[2024-02-08_what-is-high-availability-newsletter]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - system-design
---

# High Availability

## Cách hiểu bằng lời của tôi

[[High Availability]] là thiết kế để hệ thống tiếp tục phục vụ khi một phần bị lỗi. Nó không chỉ là "uptime cao"; nó là tổ hợp của redundancy, failover, health checking, replication, change management và recovery automation.

## Công thức tinh thần

Availability phụ thuộc vào hai lực:

- MTBF: thời gian trung bình giữa các lần lỗi.
- MTTR: thời gian trung bình để phục hồi.

Muốn availability cao thì hoặc làm lỗi ít xảy ra hơn, hoặc phục hồi nhanh hơn. Trong hệ phân tán, cách thực tế thường là chấp nhận lỗi sẽ xảy ra và thiết kế để cô lập lỗi nhanh.

## Pattern thường dùng

- Redundant instances sau [[Load Balancer]].
- Health check và automatic failover.
- Database replication để có bản sao khi node chính gặp lỗi.
- Multi-zone hoặc multi-region deployment khi yêu cầu downtime thấp.
- Monitoring và alerting theo triệu chứng người dùng cảm nhận.

## Trade-off cần nhớ

- HA thường đổi lấy chi phí hạ tầng và vận hành cao hơn.
- Replication có thể tạo stale read hoặc conflict nếu dùng async/multi-leader.
- Failover tự động cần test kỹ, vì failover sai có thể gây outage lớn hơn lỗi ban đầu.
- Redundancy chỉ bảo vệ tốt khi failure không tương quan; nếu các replica chia sẻ cùng dependency hoặc cùng lỗi deploy, [[Correlated Failure]] có thể làm HA trên giấy mất tác dụng.

## Liên kết

- [[Data Replication]]
- [[Load Balancer]]
- [[Failover]]
- [[Correlated Failure]]
- [[Observability]]
- [[Eventual Consistency]]
