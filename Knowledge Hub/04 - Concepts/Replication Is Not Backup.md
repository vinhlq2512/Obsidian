---
type: concept
status: understood
sources:
  - "[[2025-02-09_how-a-43-second-network-issue-led-to-a-24-hour-github-degrad]]"
source_sections:
  - "[[2025-02-09_how-a-43-second-network-issue-led-to-a-24-hour-github-degrad]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - database
---

# Replication Is Not Backup

## Định nghĩa

Replication Is Not Backup là nguyên tắc nhắc rằng replica có thể sao chép lỗi, thiếu dữ liệu hoặc trạng thái không nhất quán; nó không thay thế backup độc lập và restore plan.

## Cách hiểu bằng lời của tôi

Replica giúp availability và read scaling, nhưng nếu failover sang replica chưa nhận đủ writes, hệ thống có thể tạo split-brain hoặc mất dữ liệu. Backup phải trả lời câu hỏi khác: khôi phục về một điểm đúng trong quá khứ nhanh tới mức nào.

## Bài học từ GitHub incident

- Network drop ngắn kích hoạt cross-region failover.
- New primary thiếu một số transaction chưa replicate.
- Hai cụm nhận conflicting writes và cần reconcile thủ công.
- Backup có tồn tại nhưng restore chậm làm recovery kéo dài.

## Liên kết

- [[Data Replication]]
- [[Backup and Restore]]
- [[Failover]]
- [[Disaster Recovery]]
- recovery time objective
