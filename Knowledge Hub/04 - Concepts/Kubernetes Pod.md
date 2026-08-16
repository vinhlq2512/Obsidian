---
type: concept
status: seed
sources:
  - "[[2023-10-26_a-crash-course-in-kubernetes]]"
  - "[[2025-01-02_kubernetes-made-easy-a-beginners-roadmap-to-container-orches]]"
  - "[[2026-04-30_a-beginners-guide-to-kubernetes]]"
  - "[[2025-08-30_ep178-the-lifecycle-of-a-kubernetes-pod]]"
source_sections:
  - "[[2026-04-30_a-beginners-guide-to-kubernetes]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - kubernetes
  - infrastructure
---

# Kubernetes Pod

## Định nghĩa

[[Kubernetes Pod]] là đơn vị nhỏ nhất mà Kubernetes schedule lên node, bọc một hoặc nhiều container cùng sống, cùng chết và chia sẻ network/storage context.

## Cách hiểu bằng lời của tôi

Pod không phải container. Pod là "vỏ vận hành" mà Kubernetes đặt lên node. Container bên trong có thể là app chính và sidecar/helper, nhưng Kubernetes nhìn pod như đơn vị scheduling, networking và lifecycle.

## Pod chia sẻ gì

- Network namespace: container trong pod có thể nói chuyện qua `localhost`.
- IP address và port space của pod.
- Volume nếu được mount chung.
- Lifecycle/co-location: container trong pod được đặt cùng node và thường được quản lý cùng nhau.

## Pitfall

Pod disposable by design. Không nên coi IP pod hay filesystem local là định danh ổn định. Muốn ổn định traffic dùng [[Kubernetes Service]], muốn state lâu dài dùng volume/PVC hoặc storage ngoài.

## Liên kết

- [[Kubernetes]]
- [[Kubernetes Service]]
- [[Kubernetes Controller]]
- [[Service Mesh]]
- [[Stateful Workloads on Kubernetes]]
