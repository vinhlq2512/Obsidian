---
type: concept
status: seed
sources:
  - "[[2023-10-26_a-crash-course-in-kubernetes]]"
  - "[[2025-01-02_kubernetes-made-easy-a-beginners-roadmap-to-container-orches]]"
  - "[[2026-04-30_a-beginners-guide-to-kubernetes]]"
  - "[[2025-11-05_how-databricks-implemented-intelligent-kubernetes-load-balan]]"
source_sections:
  - "[[2023-10-26_a-crash-course-in-kubernetes]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - kubernetes
  - networking
---

# Kubernetes Service

## Định nghĩa

[[Kubernetes Service]] là abstraction cung cấp endpoint ổn định và load balancing tới một nhóm pod được chọn bằng label.

## Cách hiểu bằng lời của tôi

Pod đến rồi đi, IP pod không ổn định. Service là tên/địa chỉ ổn định để client không cần biết pod nào đang sống. Kubernetes cập nhật backend endpoints khi pod được tạo, chết hoặc thay thế.

## Loại service phổ biến

- ClusterIP: chỉ truy cập nội bộ trong cluster.
- NodePort: mở port tĩnh trên node.
- LoadBalancer: nhờ cloud provider tạo load balancer bên ngoài.
- ExternalName: map service tới DNS name ngoài cluster.

## Giới hạn

Default Kubernetes service routing thường chọn backend ở cấp connection. Với HTTP/2/gRPC connection sống lâu, một connection có thể dồn nhiều request vào cùng pod, tạo traffic skew và tail latency. Khi đó cần [[Kubernetes Load Balancing]] ở tầng request hoặc client-side.

## Liên kết

- [[Kubernetes]]
- [[Kubernetes Pod]]
- [[Load Balancer]]
- [[Service Discovery]]
- [[Kubernetes Load Balancing]]
