---
type: concept
status: seed
sources:
  - "[[2023-10-26_a-crash-course-in-kubernetes]]"
  - "[[2023-11-02_kubernetes-when-and-how-to-apply-it]]"
  - "[[2026-04-30_a-beginners-guide-to-kubernetes]]"
source_sections:
  - "[[2023-10-26_a-crash-course-in-kubernetes]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - kubernetes
  - infrastructure
---

# Kubernetes Controller

## Định nghĩa

[[Kubernetes Controller]] là control loop quan sát resource trong Kubernetes API, so sánh actual state với desired state, rồi thay đổi cluster để hai trạng thái gần nhau hơn.

## Cách hiểu bằng lời của tôi

Controller là phần làm Kubernetes "sống". Deployment không tự rollout; Deployment controller đọc spec, tạo ReplicaSet mới, scale pod mới lên, scale pod cũ xuống, và rollback nếu cần.

## Ví dụ controller

- ReplicaSet controller: giữ số pod replica đúng mong muốn.
- Deployment controller: quản lý rollout/rollback giữa các ReplicaSet.
- StatefulSet controller: giữ identity/storage ổn định cho workload có state.
- Job controller: chạy pod tới khi task hoàn tất.
- DaemonSet controller: chạy một pod trên một tập node.

## Liên kết

- [[Kubernetes]]
- [[Declarative Reconciliation]]
- [[Kubernetes Pod]]
- [[Kubernetes Operator Pattern]]
- [[Kubernetes Autoscaling]]
