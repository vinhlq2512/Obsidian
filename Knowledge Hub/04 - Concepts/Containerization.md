---
type: concept
status: understood
sources:
  - "[[2024-02-15_virtualization-and-containerization-which-one-to-pick]]"
  - "[[2023-11-09_a-crash-course-in-docker]]"
source_sections:
  - "[[2024-02-15_virtualization-and-containerization-which-one-to-pick]]"
  - "[[2023-11-09_a-crash-course-in-docker]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - containers
  - system-design
---

# Containerization

## Định nghĩa

Containerization là cách chạy ứng dụng trong môi trường isolated ở mức hệ điều hành, chia sẻ kernel với host nhưng đóng gói app và dependency riêng.

## Cách hiểu bằng lời của tôi

Container không giả lập phần cứng như VM. Nó dùng OS-level isolation để tạo cảm giác app có filesystem, process tree và network riêng, trong khi vẫn dùng chung kernel. Đổi lại, container nhẹ và start nhanh hơn, nhưng isolation không cứng bằng VM.

## Khi chọn container

- Cần startup nhanh và scale động.
- Muốn environment dev/staging/prod nhất quán.
- Ứng dụng theo microservices hoặc cloud-native.
- CI/CD cần artifact portable và nhỏ.

## Liên kết

- [[Docker]]
- [[Virtualization]]
- [[Container Image]]
- [[Container Runtime]]
- [[Kubernetes]]
