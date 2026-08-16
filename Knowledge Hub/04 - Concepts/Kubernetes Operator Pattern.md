---
type: concept
status: seed
sources:
  - "[[2023-11-02_kubernetes-when-and-how-to-apply-it]]"
  - "[[2025-10-01_how-airbnb-runs-distributed-databases-on-kubernetes-at-scale]]"
  - "[[2025-10-06_how-openai-uses-kubernetes-and-apache-kafka-for-genai]]"
  - "[[2026-03-17_how-reddit-migrated-petabyte-scale-kafka-from-ec2-to-kuberne]]"
source_sections:
  - "[[2023-11-02_kubernetes-when-and-how-to-apply-it]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - kubernetes
  - automation
---

# Kubernetes Operator Pattern

## Định nghĩa

[[Kubernetes Operator Pattern]] là cách đóng gói operational knowledge của một hệ thống vào Kubernetes custom resource và controller để tự động hóa lifecycle phức tạp.

## Cách hiểu bằng lời của tôi

Operator biến "runbook của con người" thành control loop. Thay vì engineer nhớ thứ tự upgrade, failover, backup, restore hay scale, họ khai báo resource, còn operator reconcile trạng thái an toàn.

## Cơ chế

```text
Custom Resource Definition
-> user khai báo desired state
-> operator controller watch resource
-> gọi Kubernetes API hoặc hệ thống ngoài
-> reconcile lifecycle
```

## Case study

- Airbnb dùng operator và admission hooks để serialize node/pod replacement cho distributed database, tránh mất quorum khi có planned và unplanned failure.
- OpenAI dùng Flink Kubernetes Operator để tự động hóa lifecycle của streaming jobs.
- Reddit fork Strimzi operator có kiểm soát để Kafka brokers trên Kubernetes gia nhập cụm EC2 cũ trong migration, rồi quay về operator chuẩn sau khi xong.

## Liên kết

- [[Kubernetes]]
- [[Declarative Reconciliation]]
- [[Stateful Workloads on Kubernetes]]
- [[Zero-Downtime Infrastructure Migration]]
- [[Workflow Orchestration]]
