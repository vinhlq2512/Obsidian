---
type: concept
status: seed
sources:
  - "[[2025-02-09_how-a-43-second-network-issue-led-to-a-24-hour-github-degrad]]"
  - "[[2024-12-23_the-chatgpt-outage-what-openais-post-mortem-revealed]]"
  - "[[2025-06-29_when-kv-falls-cloudflares-two-hour-outage-byte-sized-design]]"
source_sections:
  - "[[2025-02-09_how-a-43-second-network-issue-led-to-a-24-hour-github-degrad]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - operations
---

# Disaster Recovery

## Định nghĩa

[[Disaster Recovery]] là tập thiết kế, dữ liệu, quy trình và diễn tập để khôi phục service sau sự cố lớn như region failure, data corruption, dependency outage hoặc rollout hỏng.

## Cách hiểu bằng lời của tôi

Backup tồn tại chưa đủ. Câu hỏi thực tế là khôi phục mất bao lâu, dữ liệu mất bao nhiêu, ai có quyền thao tác khi control plane đang hỏng, và failover có làm dữ liệu conflict không. Recovery plan chỉ đáng tin khi đã được diễn tập trong điều kiện giống sự cố thật.

## Cần kiểm chứng

- RTO: mất bao lâu để service phục hồi.
- RPO: chấp nhận mất bao nhiêu dữ liệu.
- Backup restore speed, không chỉ backup availability.
- Replication lag trước khi failover.
- Break-glass access khi control plane/identity path lỗi.
- Runbook và owner trong incident.

## Bài học từ GitHub

Replication không đồng nghĩa backup. Nếu failover sang region có dữ liệu chưa kịp replicate, hệ thống có thể tạo hai phía ghi conflict và cần reconciliation thủ công. Failover drill phải test cả network drop ngắn, replication lag và restore path.

## Liên kết

- [[Failover]]
- [[Data Replication]]
- [[Backup and Restore]]
- [[Postmortem]]
- [[Incident Response]]
- [[Blast Radius]]
