---
type: concept
status: understood
sources:
  - "[[2023-11-09_a-crash-course-in-docker]]"
  - "[[2024-02-15_virtualization-and-containerization-which-one-to-pick]]"
source_sections:
  - "[[2023-11-09_a-crash-course-in-docker]]"
  - "[[2024-02-15_virtualization-and-containerization-which-one-to-pick]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - containers
---

# Container Image

## Định nghĩa

Container Image là artifact tĩnh chứa application code, dependency, config và root filesystem cần để khởi chạy container.

## Cách hiểu bằng lời của tôi

Image là "gói chạy được" chứ không phải process đang sống. Nó cho phép build một lần, chạy nhiều nơi, và dùng layer để tái sử dụng phần chung giữa nhiều image.

## Cơ chế

- Dockerfile mô tả các bước tạo image.
- Mỗi instruction có thể tạo layer mới.
- Base layer chứa OS/filesystem chung, layer trên thêm dependency và app.
- Khi chạy, runtime thêm writable layer để ghi state tạm thời.

## Liên kết

- [[Docker]]
- [[Container Runtime]]
- [[Deployment Pipeline]]
- immutable infrastructure
