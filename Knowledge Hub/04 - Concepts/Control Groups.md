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
  - linux
  - containers
---

# Control Groups

## Định nghĩa

Control Groups, hay cgroups, là Linux primitive dùng để giới hạn và đo tài nguyên mà một process group được dùng, như CPU, memory, disk I/O và network.

## Cách hiểu bằng lời của tôi

Namespace tạo illusion về không gian riêng; cgroups tạo quota. Nếu không có cgroups, container vẫn share host resource nhưng không có cách rõ ràng để ngăn một container ăn hết CPU/memory của các container khác.

## Liên kết

- [[Docker]]
- [[Containerization]]
- [[Linux Namespace]]
- [[Kubernetes Pod]]
