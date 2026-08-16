---
type: concept
status: seed
sources:
  - "[[2025-02-09_how-a-43-second-network-issue-led-to-a-24-hour-github-degrad]]"
  - "[[2024-12-04_writing-post-mortems-a-tech-lead-s-guide-to-learning-from-fa]]"
source_sections:
  - "[[2025-02-09_how-a-43-second-network-issue-led-to-a-24-hour-github-degrad]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - database
---

# Backup and Restore

## Định nghĩa

[[Backup and Restore]] là năng lực giữ bản sao độc lập của dữ liệu và khôi phục nó đủ nhanh, đủ đúng khi dữ liệu chính bị mất, hỏng hoặc conflict.

## Cách hiểu bằng lời của tôi

Backup chỉ có giá trị khi restore được trong thời gian chấp nhận. Một replica async không phải backup nếu nó có thể nhận dữ liệu thiếu hoặc conflict trong failover. Recovery plan phải đo restore speed, điểm khôi phục và quy trình kiểm chứng dữ liệu sau restore.

## Cần kiểm tra

- Backup có độc lập với replication path không?
- Restore mất bao lâu với dữ liệu thật?
- Có point-in-time recovery không?
- Có kiểm tra integrity sau restore không?
- Runbook có được diễn tập định kỳ không?

## Liên kết

- [[Disaster Recovery]]
- [[Data Replication]]
- [[Failover]]
- [[Database Transaction]]
- [[Postmortem]]
