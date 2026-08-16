---
type: concept
status: understood
sources:
  - "[[2025-06-17_how-the-google-cloud-outage-crashed-the-internet]]"
source_sections:
  - "[[2025-06-17_how-the-google-cloud-outage-crashed-the-internet]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - distributed-systems
---

# Global Metadata Replication

## Định nghĩa

Global Metadata Replication là cơ chế replicate policy, config hoặc metadata control-plane qua nhiều region để hệ thống có view nhất quán và cập nhật nhanh.

## Cách hiểu bằng lời của tôi

Replication nhanh là con dao hai lưỡi. Khi metadata đúng, hệ thống cập nhật toàn cầu rất nhanh. Khi metadata malformed hoặc chưa validate, cùng tốc độ đó có thể phát tán lỗi tới mọi region trước khi con người kịp phản ứng.

## Liên kết

- [[Data Replication]]
- [[Control Plane]]
- [[Feature Flag]]
- [[Phased Rollout]]
- [[Blast Radius]]
