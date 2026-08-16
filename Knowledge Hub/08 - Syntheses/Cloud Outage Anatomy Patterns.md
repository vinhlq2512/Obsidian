---
type: synthesis
status: seed
concepts:
  - "[[Control Plane]]"
  - "[[Data Plane]]"
  - "[[Hidden Dependency]]"
  - "[[Herd Effect]]"
  - "[[Kill Switch]]"
  - "[[Fail Closed]]"
  - "[[Cold Read Path]]"
  - "[[Replication Is Not Backup]]"
  - "[[Status Page Dependency]]"
  - "[[Global Metadata Replication]]"
sources:
  - "[[2025-06-17_how-the-google-cloud-outage-crashed-the-internet]]"
  - "[[2024-12-23_the-chatgpt-outage-what-openais-post-mortem-revealed]]"
  - "[[2025-07-18_cloudflares-july-2025-outage-the-global-outage-triggered-by]]"
  - "[[2025-06-29_when-kv-falls-cloudflares-two-hour-outage]]"
  - "[[2025-02-09_how-a-43-second-network-issue-led-to-a-24-hour-github-degrad]]"
questions: []
created_at: 2026-08-16
updated_at: 2026-08-16
tags:
  - synthesis
  - reliability
  - incident-response
  - system-design
---

# Cloud Outage Anatomy Patterns

## Mental model

Outage lớn thường là chuỗi coupling hơn là một lỗi đơn lẻ. Một config hoặc code path lỗi chạm [[Control Plane]], metadata replicate quá nhanh, recovery tạo [[Herd Effect]], cache che giấu [[Cold Read Path]], rồi observability/status cũng nằm trong cùng blast radius.

## Các pattern lặp lại

| Pattern | Concept | Câu hỏi cần hỏi trước incident |
| --- | --- | --- |
| Control/data coupling | [[Control Plane]], [[Data Plane]] | Data plane có tiếp tục chạy khi control plane mất không? |
| Dependency ẩn | [[Hidden Dependency]], [[Status Page Dependency]] | Công cụ incident/status có độc lập với hệ thống đang monitor không? |
| Recovery overload | [[Herd Effect]] | Restart/retry/cache refill có backoff và throttle không? |
| Emergency switch | [[Kill Switch]], [[Fail Closed]] | Tắt check này có mở rủi ro bảo mật hoặc data corruption không? |
| Cache illusion | [[Cold Read Path]] | Cache miss đi đâu nếu source of truth lỗi? |
| Data safety | [[Replication Is Not Backup]] | Failover có xét replication lag và restore speed không? |
| Global propagation | [[Global Metadata Replication]] | Metadata/config có validation, canary và blast-radius limit không? |

## Bài học

- Feature flag/kill switch phải có trước khi rollout, không chỉ sau khi incident bắt đầu.
- Metadata/config cần staging, dry-run, diff và progressive rollout như code.
- Cache nên được xem là performance optimization, không phải backup.
- Failover phải tối ưu consistency và recoverability, không chỉ availability.
- Status page và monitoring cần nằm ngoài failure domain của service chính.

## Liên kết

- [[Reliability Operations Loop]]
- [[Resilience Failure Control Patterns]]
- [[Observability for Distributed Systems]]
- [[Deployment and CI-CD Release Strategies]]
