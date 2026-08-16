---
type: concept
status: understood
sources:
  - "[[2024-04-04_a-crash-course-in-cicd]]"
source_sections:
  - "[[2024-04-04_a-crash-course-in-cicd]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - devops
  - system-design
---

# Continuous Delivery

## Định nghĩa

Continuous Delivery là practice giữ code luôn ở trạng thái có thể deploy được, với build, test, artifact và promotion qua môi trường được tự động hóa.

## Cách hiểu bằng lời của tôi

Delivery khác deployment ở chỗ production release vẫn có thể cần quyết định thủ công. Mục tiêu là mọi change đã qua pipeline đều đủ tin cậy để deploy khi team muốn.

## Cơ chế

- Build ra artifact có thể deploy.
- Chạy test qua QA/staging/performance environment.
- Dùng gate hoặc approval để promote artifact.
- Giữ rollback path rõ ràng nếu release có vấn đề.

## Liên kết

- [[Continuous Integration]]
- [[Continuous Deployment]]
- [[Deployment Pipeline]]
- [[Rollback Strategy]]
