---
type: concept
status: seed
sources:
  - "[[2026-05-28_must-know-failure-modes-in-distributed-systems]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - distributed-systems
---

# Correlated Failure

## Định nghĩa

Correlated failure là failure mode trong đó nhiều component dự phòng cùng lỗi vì chúng chia sẻ cùng một nguyên nhân, dependency hoặc assumption.

## Cách hiểu bằng lời của tôi

Redundancy chỉ có giá trị khi các bản sao thật sự độc lập. Nếu nhiều node cùng chạy một bug, cùng phụ thuộc một config service, cùng đặt trong một failure domain, hoặc cùng bị ảnh hưởng bởi một deploy xấu, thì số lượng bản sao không còn bảo vệ hệ thống như tính toán trên giấy.

## Câu hỏi kiểm tra thiết kế

- Các replica có chung dependency ẩn nào không?
- Failover target có đủ capacity khi traffic dồn sang không?
- Multi-region có dùng chung control plane, config hoặc identity provider không?
- Test chaos có kiểm tra lỗi tương quan hay chỉ kiểm tra lỗi độc lập?

## Liên kết

- [[High Availability]]
- [[Data Replication]]
- [[Failover]]
- [[Chaos Engineering]]
- [[Distributed Systems]]
