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

# Container Runtime

## Định nghĩa

Container Runtime là lớp phần mềm chịu trách nhiệm tạo, chạy và quản lý container process từ container image.

## Cách hiểu bằng lời của tôi

Image là công thức, runtime là thứ thật sự tạo process bị isolate trên host. Runtime dùng namespace, cgroups và filesystem layer để biến artifact tĩnh thành một container đang chạy.

## Ví dụ trong source

- Docker Engine từng là runtime phổ biến trong workflow Docker.
- containerd và CRI-O trở thành runtime thấp hơn được Kubernetes dùng rộng rãi.
- Orchestrator như Kubernetes không chỉ chạy container, mà còn điều phối nhiều container trên nhiều host.

## Liên kết

- [[Container Image]]
- [[Docker]]
- [[Kubernetes]]
- [[Control Groups]]
- [[Linux Namespace]]
