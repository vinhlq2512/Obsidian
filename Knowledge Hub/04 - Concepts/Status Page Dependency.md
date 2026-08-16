---
type: concept
status: understood
sources:
  - "[[2025-06-17_how-the-google-cloud-outage-crashed-the-internet]]"
  - "[[2025-02-09_how-a-43-second-network-issue-led-to-a-24-hour-github-degrad]]"
source_sections:
  - "[[2025-06-17_how-the-google-cloud-outage-crashed-the-internet]]"
  - "[[2025-02-09_how-a-43-second-network-issue-led-to-a-24-hour-github-degrad]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - incident-response
---

# Status Page Dependency

## Định nghĩa

Status Page Dependency là rủi ro khi status page, monitoring hoặc customer communication phụ thuộc vào chính hạ tầng đang có thể outage.

## Cách hiểu bằng lời của tôi

Trong incident, communication cũng là production system. Nếu status page hoặc logging nằm cùng blast radius với service bị lỗi, khách hàng và on-call có thể bị mù đúng lúc cần thông tin nhất.

## Liên kết

- [[Incident Response]]
- [[Observability]]
- [[Hidden Dependency]]
- [[Postmortem]]
- [[Service Level Objective]]
