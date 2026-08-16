---
type: concept
status: seed
sources:
  - "[[2026-03-31_how-meta-turned-debugging-into-a-product]]"
source_sections:
  - "[[2026-03-31_how-meta-turned-debugging-into-a-product]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - debugging
---

# Debugging as Code

## Định nghĩa

[[Debugging as Code]] là pattern biến workflow điều tra sự cố thành code có review, test, backtest, CI/CD và ownership rõ ràng.

## Cách hiểu bằng lời của tôi

Runbook dạng wiki dễ cũ, còn script cá nhân dễ thành tribal knowledge. Khi debugging được viết như software, tri thức điều tra trở thành artifact sống: chạy tự động khi alert bắn, được test trên incident cũ, và cập nhật cùng lifecycle với hệ thống.

## Cơ chế

```text
alert hoặc câu hỏi điều tra
-> analyzer kéo metrics/logs/config/deploy events
-> phát hiện pattern hoặc correlation
-> xuất structured finding
-> engineer review/approve mitigation
```

## Liên kết

- [[Root Cause Analysis]]
- [[Automated Root Cause Analysis]]
- [[Incident Response]]
- [[Observability]]
- [[Runbook Automation]]
- [[Shadow Testing]]
