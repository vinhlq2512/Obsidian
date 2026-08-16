---
type: concept
status: understood
sources:
  - "[[2024-04-04_a-crash-course-in-cicd]]"
source_sections:
  - "[[2024-04-04_a-crash-course-in-cicd]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - devops
  - system-design
---

# Continuous Deployment

## Định nghĩa

Continuous Deployment là practice tự động deploy mọi thay đổi đã vượt qua automated tests tới production, không cần bước approval thủ công.

## Cách hiểu bằng lời của tôi

Continuous deployment chỉ an toàn khi pipeline, observability, rollback và deployment strategy đủ trưởng thành. Nếu không, tự động đưa code lên production chỉ làm lỗi tới người dùng nhanh hơn.

## Điều kiện cần

- Test tự động có độ tin cậy cao.
- [[Deployment Pipeline]] có gate rõ ràng.
- [[Rollback Alarm]] và metrics production phát hiện regression.
- Deployment strategy giảm blast radius như [[Canary Deployment]] hoặc [[Feature Flag]].

## Liên kết

- [[Continuous Delivery]]
- [[Deployment Pipeline]]
- [[Reliability Operations Loop]]
