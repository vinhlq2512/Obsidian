---
type: concept
status: seed
sources:
  - "[[2023-11-02_kubernetes-when-and-how-to-apply-it]]"
  - "[[2026-03-17_how-reddit-migrated-petabyte-scale-kafka-from-ec2-to-kuberne]]"
source_sections:
  - "[[2023-11-02_kubernetes-when-and-how-to-apply-it]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - infrastructure
  - automation
---

# Infrastructure as Code

## Định nghĩa

[[Infrastructure as Code]] là cách quản lý hạ tầng bằng file cấu hình/code có version, review và apply lặp lại được, thay vì thao tác thủ công trên server hoặc console.

## Cách hiểu bằng lời của tôi

IaC biến hạ tầng thành artifact có thể đọc, diff, review và rollback. Trong Kubernetes, manifest là desired state của resource; trong migration lớn, cấu hình như DNS facade hoặc Terraform giúp thay đổi hạ tầng có kiểm soát hơn lệnh thủ công.

## Liên kết

- [[Declarative Reconciliation]]
- [[Kubernetes]]
- [[Zero-Downtime Infrastructure Migration]]
- [[Technical Debt]]
