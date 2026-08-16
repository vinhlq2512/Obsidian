---
type: concept
status: seed
sources:
  - "[[2026-05-19_how-snapchat-serves-a-billion-predictions-per-second]]"
source_sections:
  - "[[2026-05-19_how-snapchat-serves-a-billion-predictions-per-second]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - mlops
  - deployment
---

# Model Deployment Reconciliation

## Định nghĩa

[[Model Deployment Reconciliation]] là pattern lưu desired state của model deployment rồi liên tục so với actual state để tự động đưa serving fleet về cấu hình mong muốn.

## Cách hiểu bằng lời của tôi

Snap mượn mental model Kubernetes: không deploy model bằng thao tác thủ công từng fleet, mà khai báo model nào chạy ở đâu, version nào, config nào. Control plane reconcile khi actual state lệch desired state.

## Liên kết

- [[Declarative Reconciliation]]
- [[AI Model Serving]]
- [[Continuous Deployment]]
- [[Model Shadowing]]
- [[Rollback Strategy]]
