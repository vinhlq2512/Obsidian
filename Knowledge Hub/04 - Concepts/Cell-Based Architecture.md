---
type: concept
status: understood
sources:
  - "[[2025-12-04_how-discord-indexes-trillions-of-messages-without-falling-ap]]"
source_sections:
  - "[[2025-12-04_how-discord-indexes-trillions-of-messages-without-falling-ap]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - system-design
---

# Cell-Based Architecture

## Định nghĩa

Cell-Based Architecture là kiến trúc chia hệ thống thành nhiều cell nhỏ, mỗi cell có tài nguyên và failure domain riêng.

## Cách hiểu bằng lời của tôi

Thay vì một cụm khổng lồ chịu mọi traffic, cell architecture chia hệ thống thành các cụm nhỏ hơn để giảm coordination overhead và blast radius. Với Discord search, nhiều Elasticsearch cell nhỏ thay cho vài cluster lớn giúp restart, upgrade và scale dễ hơn.

## Liên kết

- [[Search Tenant Isolation]]
- [[Blast Radius]]
- [[High Availability]]
- [[Partial Failure]]
