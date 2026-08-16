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
  - infrastructure
  - system-design
---

# Virtualization

## Định nghĩa

Virtualization là kỹ thuật dùng hypervisor để chạy nhiều virtual machine trên cùng một host vật lý, mỗi VM có guest OS riêng và tài nguyên được ảo hóa.

## Cách hiểu bằng lời của tôi

Virtualization mua isolation mạnh hơn bằng chi phí resource lớn hơn. Mỗi VM giống một máy riêng với OS riêng, nên phù hợp legacy app, workload cần OS đa dạng hoặc yêu cầu isolation cao.

## Khi chọn VM

- Cần chạy nhiều hệ điều hành khác nhau.
- Legacy app khó containerize.
- Cần isolation mạnh giữa tenant/workload.
- Workload cần resource guarantee hoặc cấu hình OS riêng.

## Liên kết

- [[Containerization]]
- [[Docker]]
- [[Infrastructure as Code]]
- [[Runtime Platform Migration]]
