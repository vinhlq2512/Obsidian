---
type: concept
status: seed
sources:
  - "[[2025-11-05_how-databricks-implemented-intelligent-kubernetes-load-balan]]"
  - "[[2023-10-26_a-crash-course-in-kubernetes]]"
source_sections:
  - "[[2025-11-05_how-databricks-implemented-intelligent-kubernetes-load-balan]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - kubernetes
  - networking
---

# Kubernetes Load Balancing

## Định nghĩa

[[Kubernetes Load Balancing]] là cách phân phối traffic tới pod backend trong Kubernetes, từ Service/kube-proxy mặc định tới các chiến lược L7 hoặc client-side thông minh hơn.

## Cách hiểu bằng lời của tôi

Kubernetes Service giải quyết discovery endpoint ổn định, nhưng không phải lúc nào cũng phân phối request công bằng. Với connection dài như gRPC/HTTP2, load balancing ở cấp connection có thể làm một vài pod nóng còn pod khác rảnh.

## Pattern từ Databricks

- Control plane watch Kubernetes Services và EndpointSlices.
- Duy trì topology realtime: pod IP, readiness, zone, shard label.
- Stream endpoint update tới client/proxy qua xDS-like API.
- Client/RPC framework chọn backend theo tình trạng hiện tại thay vì chờ DNS TTL hoặc kube-proxy.

## Trade-off

- Client-side/L7 routing giảm tail latency và traffic skew.
- Đổi lại cần control plane riêng, integration vào RPC framework và observability tốt hơn.
- Với workload nhỏ hoặc short-lived HTTP request, Service mặc định có thể đủ.

## Liên kết

- [[Kubernetes Service]]
- [[Load Balancer]]
- [[Service Discovery]]
- [[Latency]]
- [[gRPC]]
