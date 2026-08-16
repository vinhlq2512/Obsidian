---
type: synthesis
status: seed
concepts:
  - "[[Docker]]"
  - "[[Containerization]]"
  - "[[Virtualization]]"
  - "[[Container Image]]"
  - "[[Container Runtime]]"
  - "[[Linux Namespace]]"
  - "[[Control Groups]]"
  - "[[Serverless Architecture]]"
  - "[[Monolithic Architecture]]"
  - "[[Modular Monolith]]"
  - "[[Microservices Architecture]]"
  - "[[Sidecar Pattern]]"
  - "[[Ambassador Pattern]]"
  - "[[Container Adapter Pattern]]"
  - "[[Work Queue Pattern]]"
  - "[[Scatter-Gather Pattern]]"
sources:
  - "[[2023-11-09_a-crash-course-in-docker]]"
  - "[[2024-02-15_virtualization-and-containerization-which-one-to-pick]]"
  - "[[2026-04-11_ep210-monolithic-vs-microservices-vs-serverless]]"
  - "[[2025-03-20_monolith-vs-microservices-vs-modular-monoliths-what-s-the-ri]]"
  - "[[2026-05-07_container-design-patterns-for-distributed-systems]]"
questions: []
created_at: 2026-08-16
updated_at: 2026-08-16
tags:
  - synthesis
  - containers
  - architecture
  - system-design
---

# Container and Service Architecture Tradeoffs

## Mental model

Kiến trúc runtime có hai lớp quyết định khác nhau: app được đóng gói/chạy bằng gì, và hệ thống được chia thành unit triển khai nào. [[Docker]] và [[Containerization]] giải quyết packaging/runtime consistency; [[Monolithic Architecture]], [[Modular Monolith]], [[Microservices Architecture]] và [[Serverless Architecture]] giải quyết boundary tổ chức, scaling và vận hành.

## Bảng so sánh nhanh

| Câu hỏi | Lựa chọn | Trade-off |
| --- | --- | --- |
| Cần isolation mạnh hay startup nhanh? | [[Virtualization]] vs [[Containerization]] | VM cô lập tốt hơn; container nhẹ, portable và hợp CI/CD hơn |
| Artifact chạy production là gì? | [[Container Image]], [[Container Runtime]] | Image bất biến, runtime tạo process isolated |
| Hệ thống mới nên bắt đầu thế nào? | [[Monolithic Architecture]] hoặc [[Modular Monolith]] | Đơn giản trước, tách boundary khi domain và scale đủ rõ |
| Khi nào microservices đáng tiền? | [[Microservices Architecture]] | Independent scaling/deploy đổi lấy tracing, consistency và orchestration |
| Khi nào serverless hợp? | [[Serverless Architecture]] | Event-driven/pay-per-use đổi lấy cold start, debugging và lock-in |
| Container phối hợp thế nào? | [[Sidecar Pattern]], [[Ambassador Pattern]], [[Container Adapter Pattern]] | Helper container tách cross-cutting concern nhưng tăng integration contract |
| Workload song song ra sao? | [[Work Queue Pattern]], [[Scatter-Gather Pattern]] | Queue hợp batch; scatter/gather hợp query nhiều shard |

## Bài học

- Container không phải VM nhẹ; nó là OS-level process isolation.
- Docker thắng lớn vì chuẩn hóa packaging, không chỉ vì runtime.
- Modular monolith thường là bước trung gian tốt trước microservices.
- Serverless hợp phần event-driven phụ trợ, không phải câu trả lời chung cho mọi workload.
- Container design patterns hữu ích khi boundary helper thật sự tái sử dụng được; nếu coupling quá chặt, tách container chỉ tạo thêm version skew.

## Liên kết

- [[Kubernetes Platform Patterns]]
- [[Deployment and CI-CD Release Strategies]]
- [[Microservices Design Patterns]]
- [[Reliability Operations Loop]]
