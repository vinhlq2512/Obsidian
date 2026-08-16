---
type: concept
status: seed
sources:
  - "[[2024-12-04_writing-post-mortems-a-tech-lead-s-guide-to-learning-from-fa]]"
  - "[[2024-12-23_the-chatgpt-outage-what-openais-post-mortem-revealed]]"
  - "[[2025-02-09_how-a-43-second-network-issue-led-to-a-24-hour-github-degrad]]"
source_sections:
  - "[[2024-12-04_writing-post-mortems-a-tech-lead-s-guide-to-learning-from-fa]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - incident
---

# Postmortem

## Định nghĩa

[[Postmortem]] là tài liệu và quy trình học sau incident, tập trung vào timeline, impact, root cause, contributing factors và action items có owner.

## Cách hiểu bằng lời của tôi

Postmortem tốt không hỏi "ai làm hỏng", mà hỏi "hệ thống/quy trình nào cho phép lỗi này đi tới user". Nó biến một lần đau thành thay đổi cụ thể: alert mới, test mới, rollout guardrail mới, dependency tách ra, hoặc recovery path nhanh hơn.

## Cấu trúc nên có

- Summary: chuyện gì xảy ra, kéo dài bao lâu, ảnh hưởng ai.
- Impact: downtime, degraded path, user/revenue/internal cost.
- Timeline: phát hiện, mitigation, rollback, recovery.
- Root cause analysis: trigger và systemic gaps.
- Action items: specific, owned, measurable, có deadline.
- Follow-up: kiểm tra action có thật sự đóng rủi ro không.

## Anti-pattern

- Đổ lỗi cá nhân.
- Viết như PR/câu chuyện đẹp thay vì facts.
- Tạo danh sách action quá dài nhưng không ưu tiên.
- Không theo dõi action sau khi postmortem xong.

## Liên kết

- [[Incident Response]]
- [[Root Cause Analysis]]
- [[Premortem]]
- [[Alerting]]
- [[Blast Radius]]
- [[Disaster Recovery]]
