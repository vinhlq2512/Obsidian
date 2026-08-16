---
type: concept
status: seed
sources:
  - "[[2023-10-26_a-crash-course-in-kubernetes]]"
  - "[[2023-11-02_kubernetes-when-and-how-to-apply-it]]"
  - "[[2025-01-02_kubernetes-made-easy-a-beginners-roadmap-to-container-orches]]"
  - "[[2026-04-30_a-beginners-guide-to-kubernetes]]"
source_sections:
  - "[[2023-10-26_a-crash-course-in-kubernetes]]"
  - "[[2026-04-30_a-beginners-guide-to-kubernetes]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - infrastructure
  - system-design
---

# Kubernetes

## Định nghĩa

[[Kubernetes]] là platform orchestration cho containerized applications, dùng API khai báo desired state rồi liên tục reconcile actual state về desired state.

## Cách hiểu bằng lời của tôi

Kubernetes không phải chỉ là nơi chạy container. Ý tưởng lõi là: ta nói hệ thống "nên có gì", còn control plane, scheduler, kubelet và controllers liên tục làm việc để thực tế khớp với lời hứa đó.

## Kiến trúc cơ bản

- Control plane: API server, etcd, scheduler, controller manager.
- Worker node: kubelet, container runtime, kube-proxy/networking.
- Workload unit: [[Kubernetes Pod]].
- Stable access: [[Kubernetes Service]].
- Control logic: [[Kubernetes Controller]].

## Mental model

```text
desired state in API
-> persisted in etcd
-> controllers watch state
-> scheduler places pods
-> kubelet runs containers
-> controllers keep reconciling drift
```

## Giới hạn cần nhớ

Kubernetes chỉ giữ những lời hứa được khai báo. Nó có thể restart process đã exit, nhưng không tự biết application đang trả 500, dữ liệu sai, dependency logic hỏng hoặc architecture bottleneck nếu probe/observability không mô tả điều đó.

## Liên kết

- [[Kubernetes Pod]]
- [[Kubernetes Controller]]
- [[Kubernetes Service]]
- [[Kubernetes Operator Pattern]]
- [[Kubernetes Autoscaling]]
- [[Stateful Workloads on Kubernetes]]
- [[Observability]]
