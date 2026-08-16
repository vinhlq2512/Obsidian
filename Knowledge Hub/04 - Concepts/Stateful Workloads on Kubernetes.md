---
type: concept
status: seed
sources:
  - "[[2025-01-02_kubernetes-made-easy-a-beginners-roadmap-to-container-orches]]"
  - "[[2025-10-01_how-airbnb-runs-distributed-databases-on-kubernetes-at-scale]]"
  - "[[2026-03-17_how-reddit-migrated-petabyte-scale-kafka-from-ec2-to-kuberne]]"
source_sections:
  - "[[2025-10-01_how-airbnb-runs-distributed-databases-on-kubernetes-at-scale]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - kubernetes
  - database
---

# Stateful Workloads on Kubernetes

## Định nghĩa

[[Stateful Workloads on Kubernetes]] là cách chạy hệ thống cần identity, storage hoặc quorum ổn định trên nền pod/node vốn disposable.

## Cách hiểu bằng lời của tôi

Stateless app hợp với Kubernetes hơn vì pod chết có thể thay pod mới. Database, Kafka hoặc streaming state khó hơn: node replacement, storage attach, quorum, replica placement và latency spike đều ảnh hưởng correctness hoặc availability.

## Pattern từ source

- Dùng persistent volume/PVC hoặc storage ngoài để state sống lâu hơn pod.
- Dùng operator để encode thứ tự upgrade, replacement, failover và recovery.
- Tách cluster theo fault domain/AZ để giảm blast radius.
- Overprovision capacity để sống sót khi mất một zone/cluster.
- Với database, có thể dùng replica reads hoặc stale reads cho workload chấp nhận staleness để né leader/storage latency spike.

## Cần bảo vệ

- Quorum và replication factor.
- Metadata/logical state, không chỉ máy vật lý.
- Thứ tự planned maintenance khi đang có unplanned failure.
- Storage latency/tail latency.

## Liên kết

- [[Kubernetes]]
- [[Kubernetes Operator Pattern]]
- [[Quorum]]
- [[High Availability]]
- [[Zero-Downtime Infrastructure Migration]]
- [[Cassandra]]
