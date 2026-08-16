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
  - devops
---

# Docker

## Định nghĩa

Docker là công nghệ phổ biến hóa container image và container runtime, giúp đóng gói app, dependency, config và filesystem thành artifact có thể chạy nhất quán qua nhiều môi trường.

## Cách hiểu bằng lời của tôi

Docker giải quyết một vấn đề rất thực dụng: app chạy ở máy dev nhưng lỗi ở production vì dependency và môi trường khác nhau. Docker biến môi trường chạy thành một phần của artifact, còn runtime tạo process được isolate bằng primitive của Linux.

## Cơ chế chính

- [[Container Image]] là artifact tĩnh mô tả app và filesystem.
- [[Container Runtime]] khởi chạy image thành process đang chạy.
- [[Linux Namespace]] tạo isolation cho process, mount, network.
- [[Control Groups]] giới hạn CPU, memory, I/O.
- Layered filesystem và writable layer giúp image bất biến, container runtime state tạm thời.

## Liên kết

- [[Containerization]]
- [[Virtualization]]
- [[Kubernetes]]
- [[Deployment Pipeline]]
