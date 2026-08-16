---
type: concept
status: understood
sources:
  - "[[2025-03-20_monolith-vs-microservices-vs-modular-monoliths-what-s-the-ri]]"
  - "[[2026-04-11_ep210-monolithic-vs-microservices-vs-serverless]]"
source_sections:
  - "[[2025-03-20_monolith-vs-microservices-vs-modular-monoliths-what-s-the-ri]]"
  - "[[2026-04-11_ep210-monolithic-vs-microservices-vs-serverless]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - architecture
  - system-design
---

# Monolithic Architecture

## Định nghĩa

Monolithic Architecture là kiến trúc trong đó phần lớn logic ứng dụng nằm trong một codebase và được deploy như một đơn vị duy nhất.

## Cách hiểu bằng lời của tôi

Monolith không xấu mặc định. Nó đơn giản, dễ test, dễ deploy lúc đầu và giảm overhead phân tán. Vấn đề xuất hiện khi codebase, traffic hoặc team ownership lớn tới mức mọi thay đổi đều kéo cả hệ thống theo.

## Trade-off

- Ưu: development ban đầu nhanh, local testing đơn giản, ít network boundary.
- Nhược: khó scale từng phần, fault isolation yếu, deployment bị buộc chung.
- Phù hợp giai đoạn đầu hoặc domain chưa đủ rõ để tách service.

## Liên kết

- [[Modular Monolith]]
- [[Microservices Architecture]]
- [[Serverless Architecture]]
- [[Runtime Platform Migration]]
