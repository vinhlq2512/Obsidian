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

# Big-Bang Deployment

## Định nghĩa

Big-Bang Deployment là strategy dừng version cũ, đưa version mới lên một lần và chấp nhận một khoảng downtime hoặc maintenance window.

## Cách hiểu bằng lời của tôi

Đây là strategy đơn giản nhất nhưng blast radius lớn nhất. Nếu version mới lỗi, tất cả user thấy lỗi cùng lúc; rollback cũng là một deploy lớn khác.

## Khi vẫn hợp lý

- Hệ thống nhỏ hoặc có maintenance window rõ.
- Thay đổi buộc phải đồng bộ, ví dụ migration phức tạp khó chạy song song.
- Team có rollback plan và thông báo downtime tốt.

## Liên kết

- [[Deployment Pipeline]]
- [[Rollback Strategy]]
- [[Blast Radius]]
