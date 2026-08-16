---
type: concept
status: developing
sources:
  - "[[2025-08-07_top-strategies-to-improve-reliability-in-distributed-systems-part-1]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - distributed-systems
---

# Failover

## Định nghĩa

Failover là cơ chế phát hiện một component không còn phục vụ được và chuyển traffic, quyền xử lý hoặc vai trò leader sang component khỏe hơn.

## Cách hiểu bằng lời của tôi

Failover là "đổi người gánh việc" khi một node/service/region bị lỗi. Với service stateless, việc này thường là load balancer bỏ instance lỗi khỏi rotation. Với hệ có state, failover khó hơn vì phải biết bản sao nào đủ mới, ai được quyền nhận write, và làm sao tránh hai node cùng nghĩ mình là leader.

## Cơ chế

```text
health signal xấu
-> phát hiện failure
-> loại node khỏi đường traffic hoặc promote backup
-> kiểm soát state/leader để tránh split-brain
-> tiếp tục phục vụ với capacity còn lại
```

## Trade-off

- Failover quá sớm có thể loại nhầm node chỉ đang chậm tạm thời.
- Failover quá muộn tạo downtime người dùng nhìn thấy.
- Active-active cho failover nhanh hơn, nhưng cần đồng bộ state và load-awareness tốt.
- Hệ cần một leader thường phải dùng leader election như Raft/Paxos, đổi lại thêm latency và complexity.

## Liên kết

- [[High Availability]]
- [[Load Balancer]]
- [[Data Replication]]
- [[Distributed Systems]]
- [[Correlated Failure]]
