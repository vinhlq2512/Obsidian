---
type: synthesis
status: seed
concepts:
  - "[[Kubernetes]]"
  - "[[Declarative Reconciliation]]"
  - "[[Kubernetes Pod]]"
  - "[[Kubernetes Controller]]"
  - "[[Kubernetes Service]]"
  - "[[Kubernetes Operator Pattern]]"
  - "[[Kubernetes Autoscaling]]"
  - "[[Stateful Workloads on Kubernetes]]"
  - "[[Kubernetes Load Balancing]]"
  - "[[Zero-Downtime Infrastructure Migration]]"
sources:
  - "[[2023-10-26_a-crash-course-in-kubernetes]]"
  - "[[2023-11-02_kubernetes-when-and-how-to-apply-it]]"
  - "[[2025-01-02_kubernetes-made-easy-a-beginners-roadmap-to-container-orches]]"
  - "[[2026-04-30_a-beginners-guide-to-kubernetes]]"
  - "[[2025-10-01_how-airbnb-runs-distributed-databases-on-kubernetes-at-scale]]"
  - "[[2025-11-05_how-databricks-implemented-intelligent-kubernetes-load-balan]]"
  - "[[2026-03-17_how-reddit-migrated-petabyte-scale-kafka-from-ec2-to-kuberne]]"
  - "[[2025-10-06_how-openai-uses-kubernetes-and-apache-kafka-for-genai]]"
questions: []
created_at: 2026-08-16
updated_at: 2026-08-16
tags:
  - synthesis
  - kubernetes
  - system-design
  - bytebytego
---

# Kubernetes Platform Patterns

## Ý chính

Cụm Kubernetes của ByteByteGo cho thấy Kubernetes là một nền declarative automation hơn là "máy chạy container". Sức mạnh nằm ở reconciliation, extensibility và operator; rủi ro nằm ở complexity, health signal thiếu, networking mặc định và stateful workload.

## Bản đồ concept

```text
desired state
-> Kubernetes API/etcd
-> controllers/operators
-> pods on worker nodes
-> services expose stable endpoints
-> autoscaling adjusts pods/nodes
-> observability/probes tell platform what "healthy" means
```

## Case study map

- Airbnb: chạy distributed database trên Kubernetes bằng operator, multi-cluster/AZ isolation, EBS reattach, stale/replica reads và sequencing để giữ quorum.
- Databricks: vượt giới hạn Service/kube-proxy với client-side L7 load balancing và endpoint discovery realtime.
- Reddit: migrate Kafka petabyte-scale từ EC2 sang Kubernetes bằng DNS facade, broker co-existence, partition rebalance và control-plane migration sau cùng.
- OpenAI: chạy PyFlink trên Kubernetes với operator, per-namespace isolation, watchdogs cho Kafka topology và state checkpoint tách khỏi cluster.

## Trade-off cần nhớ

- Kubernetes tự động hóa tốt khi desired state và health signal được mô tả đúng.
- Nó không phát hiện lỗi nghiệp vụ nếu probe chỉ kiểm tra process còn sống.
- Stateful workload cần operator và fault-domain design; không thể đối xử như stateless deployment.
- Default networking đủ cho nhiều workload, nhưng connection dài/gRPC có thể cần routing thông minh hơn.

## Liên kết

- [[Kubernetes]]
- [[Declarative Reconciliation]]
- [[Kubernetes Operator Pattern]]
- [[Stateful Workloads on Kubernetes]]
- [[Kubernetes Load Balancing]]
- [[Zero-Downtime Infrastructure Migration]]
