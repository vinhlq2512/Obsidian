---
type: synthesis
status: seed
concepts:
  - "[[Capacity Planning]]"
  - "[[Peak QPS]]"
  - "[[Load Testing]]"
  - "[[Error Budget]]"
  - "[[Phased Rollout]]"
  - "[[Incident Response]]"
  - "[[Premortem]]"
  - "[[Postmortem]]"
  - "[[Root Cause Analysis]]"
  - "[[Risk Matrix]]"
  - "[[Rollback Strategy]]"
  - "[[Disaster Recovery]]"
  - "[[Backup and Restore]]"
sources:
  - "[[2023-06-29_capacity-planning]]"
  - "[[2025-02-06_the-tech-lead-s-guide-to-load-testing-like-a-pro-byte-sized-design]]"
  - "[[2024-12-04_writing-post-mortems-a-tech-lead-s-guide-to-learning-from-fa]]"
  - "[[2023-11-07_shipping-to-production]]"
  - "[[2024-12-23_the-chatgpt-outage-what-openais-post-mortem-revealed]]"
  - "[[2025-02-09_how-a-43-second-network-issue-led-to-a-24-hour-github-degrad]]"
questions: []
created_at: 2026-08-16
updated_at: 2026-08-16
tags:
  - synthesis
  - reliability
  - operations
  - bytebytego
---

# Reliability Operations Loop

## Ý chính

Reliability không chỉ là thêm retry, replica hay load balancer. Nó là một vòng lặp vận hành: ước lượng capacity, kiểm chứng bằng load test, triển khai theo pha, dùng error budget để quyết định risk, rồi học từ incident bằng postmortem.

## Vòng lặp

```text
[[Capacity Planning]]
-> [[Load Testing]]
-> [[Phased Rollout]]
-> [[Error Budget]] guardrail
-> [[Incident Response]]
-> [[Postmortem]]
-> action items + [[Disaster Recovery]] drills
-> cập nhật giả định capacity
```

## Câu hỏi vận hành

- Giả định capacity nào nếu sai sẽ tạo incident?
- Load test có mô phỏng đủ production scale và workflow nhiều bước không?
- Rollout có điểm dừng dựa trên SLI/SLO không?
- Error budget còn đủ để chấp nhận thay đổi rủi ro không?
- Backup/restore và failover đã được diễn tập dưới replication lag chưa?
- Postmortem có action item specific, owned, measurable không?

## Liên kết

- [[Resilience Failure Control Patterns]]
- [[Observability for Distributed Systems]]
- [[Service Level Objective]]
- [[Alerting]]
- [[Blast Radius]]
