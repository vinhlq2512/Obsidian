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

# Continuous Integration

## Định nghĩa

Continuous Integration là practice tự động build, test và tích hợp code thường xuyên vào shared repository để giảm merge conflict và phát hiện lỗi sớm.

## Cách hiểu bằng lời của tôi

CI không chỉ là có tool chạy test. Ý chính là giảm thời gian code sống riêng trong silo. Mỗi thay đổi nhỏ được merge sớm, build/test tự động, và team nhận tín hiệu nhanh khi integration bị hỏng.

## Cơ chế

- Source control lưu code, test và build script.
- Pull request/review kiểm soát thay đổi trước khi merge.
- Pipeline tự động build artifact và chạy unit/integration tests.
- Failure phải alert đủ nhanh để team sửa khi context còn mới.

## Liên kết

- [[Deployment Pipeline]]
- [[Continuous Delivery]]
- testing
- code review
