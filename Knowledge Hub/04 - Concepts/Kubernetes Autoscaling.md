---
type: concept
status: seed
sources:
  - "[[2023-11-02_kubernetes-when-and-how-to-apply-it]]"
  - "[[2025-01-02_kubernetes-made-easy-a-beginners-roadmap-to-container-orches]]"
source_sections:
  - "[[2025-01-02_kubernetes-made-easy-a-beginners-roadmap-to-container-orches]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - kubernetes
  - scaling
---

# Kubernetes Autoscaling

## Định nghĩa

[[Kubernetes Autoscaling]] là cơ chế tự động tăng/giảm pod hoặc node dựa trên nhu cầu workload và tài nguyên cluster.

## Cách hiểu bằng lời của tôi

Autoscaling trong Kubernetes có hai tầng hay bị nhầm: tăng số replica của workload và tăng số máy trong cluster. Pod scale mà không có node trống thì pod vẫn Pending; node scale mà metric workload sai thì vẫn có thể over/under-provision.

## Hai tầng chính

- Horizontal Pod Autoscaler: tăng/giảm số pod replica dựa trên metric như CPU, memory hoặc custom metric.
- Cluster Autoscaler: thêm node khi pod không schedule được vì thiếu tài nguyên, và xóa node khi underutilized.

## Trade-off

- Scale theo metric sai có thể tạo oscillation hoặc không phản ánh user load.
- Autoscaling không thay thế capacity planning cho peak lớn hoặc stateful workload.
- Scaling có độ trễ: image pull, pod startup, readiness và node provisioning đều mất thời gian.
- Cần request/limit hợp lý để scheduler và autoscaler có tín hiệu đúng.

## Liên kết

- [[Kubernetes]]
- [[Horizontal Scaling]]
- [[Backpressure]]
- [[Load Shedding]]
- [[Observability]]
