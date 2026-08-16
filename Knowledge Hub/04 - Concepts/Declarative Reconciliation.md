---
type: concept
status: seed
sources:
  - "[[2023-11-02_kubernetes-when-and-how-to-apply-it]]"
  - "[[2026-04-30_a-beginners-guide-to-kubernetes]]"
source_sections:
  - "[[2023-11-02_kubernetes-when-and-how-to-apply-it]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - infrastructure
  - automation
---

# Declarative Reconciliation

## Định nghĩa

[[Declarative Reconciliation]] là pattern trong đó user khai báo desired state, còn controller liên tục quan sát actual state và thực hiện hành động để thu hẹp khoảng cách.

## Cách hiểu bằng lời của tôi

Imperative script nói từng bước phải làm. Declarative system nói trạng thái cuối muốn có. Vì vậy `apply` cùng một manifest nhiều lần vẫn nên đi tới cùng kết quả: ta không bắn thêm một command mới, mà nhắc lại lời hứa về trạng thái mong muốn.

## Cơ chế

```text
desired spec
-> store in API/state store
-> controller watch
-> compare actual vs desired
-> create/update/delete resources
-> repeat forever
```

## Vì sao quan trọng

- Tạo nền cho automation và self-healing.
- Cho phép mở rộng bằng resource mới như CRD.
- Giúp GitOps hoạt động: repo là desired state, controller reconcile cluster.
- Là lý do Kubernetes phù hợp với platform extensibility hơn các script thủ công.

## Liên kết

- [[Kubernetes]]
- [[Kubernetes Controller]]
- [[Kubernetes Operator Pattern]]
- [[Infrastructure as Code]]
