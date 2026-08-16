---
type: concept
status: understood
sources:
  - "[[2024-04-04_a-crash-course-in-cicd]]"
  - "[[2026-06-11_must-know-deployment-strategies-from-big-bang-to-progressive]]"
source_sections:
  - "[[2024-04-04_a-crash-course-in-cicd]]"
  - "[[2026-06-11_must-know-deployment-strategies-from-big-bang-to-progressive]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - deployment
  - system-design
---

# Blue-Green Deployment

## Định nghĩa

Blue-Green Deployment là strategy duy trì hai production environment tương đương; một environment nhận traffic thật, environment còn lại chạy version mới để test trước khi switch traffic.

## Cách hiểu bằng lời của tôi

Blue-green mua rollback nhanh bằng chi phí hạ tầng. Khi switch lỗi, chỉ cần chuyển traffic về environment cũ. Nhưng database/schema/session vẫn có thể là điểm khó nếu hai environment dùng chung state.

## Trade-off

- Ưu: rollback nhanh, test version mới trong environment gần production.
- Nhược: tốn gần gấp đôi hạ tầng và cần đồng bộ state cẩn thận.
- Schema change vẫn cần [[Expand-Contract Migration]] để rollback-safe.

## Liên kết

- [[Load Balancer]]
- [[Rollback Strategy]]
- [[Zero-Downtime Infrastructure Migration]]
- [[Deployment Pipeline]]
