---
type: concept
status: seed
sources:
  - "[[2025-10-07_how-pinterest-runs-spark-at-scale-with-moka]]"
source_sections:
  - "[[2025-10-07_how-pinterest-runs-spark-at-scale-with-moka]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - data-engineering
  - kubernetes
---

# Spark on Kubernetes Platform

## Định nghĩa

[[Spark on Kubernetes Platform]] là cách vận hành Spark jobs trên Kubernetes bằng container, operator, scheduler, autoscaling và observability thay cho Hadoop/YARN monolithic cluster.

## Cách hiểu bằng lời của tôi

Chạy Spark trên Kubernetes không chỉ là đổi nơi chạy executor. Ở scale lớn, platform phải có submission service, operator quản lý lifecycle, scheduler có queue/preemption, remote shuffle service, UI/logs/history và cơ chế migration validation.

## Pattern từ Moka

- Submission service nhận job từ workflow manager rồi tạo Kubernetes CRD.
- Spark Operator quản lý driver/executor lifecycle thay vì gọi trực tiếp `spark-submit`.
- Scheduler queue-based giúp job ưu tiên cao lấy lại tài nguyên.
- Remote shuffle tách shuffle storage khỏi compute để dynamic executor scaling tốt hơn.
- Dry-run validation so sánh output Hadoop/Moka trước khi chuyển production.

## Liên kết

- [[Kubernetes]]
- [[Kubernetes Operator Pattern]]
- [[Kubernetes Autoscaling]]
- [[Workflow Orchestration]]
- [[Remote Shuffle Service]]
- [[Data Pipeline Validation]]
- [[Cost Optimization]]
