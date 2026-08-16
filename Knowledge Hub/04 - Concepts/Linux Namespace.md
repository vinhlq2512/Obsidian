---
type: concept
status: understood
sources:
  - "[[2023-11-09_a-crash-course-in-docker]]"
source_sections:
  - "[[2023-11-09_a-crash-course-in-docker]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - linux
  - containers
---

# Linux Namespace

## Định nghĩa

Linux Namespace là primitive của Linux dùng để isolate view của process đối với tài nguyên như PID, mount, network và filesystem.

## Cách hiểu bằng lời của tôi

Container về bản chất vẫn là process trên host. Namespace làm cho process đó "nhìn thấy" một thế giới riêng: PID riêng, network riêng, mount riêng. Đây là lý do container có isolation nhẹ mà không cần guest OS riêng như VM.

## Liên kết

- [[Docker]]
- [[Containerization]]
- [[Control Groups]]
- [[Container Runtime]]
