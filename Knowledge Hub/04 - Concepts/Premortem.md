---
type: concept
status: seed
sources:
  - "[[2024-12-04_writing-post-mortems-a-tech-lead-s-guide-to-learning-from-fa]]"
source_sections:
  - "[[2024-12-04_writing-post-mortems-a-tech-lead-s-guide-to-learning-from-fa]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - planning
---

# Premortem

## Định nghĩa

[[Premortem]] là bài tập tưởng tượng một launch/project đã thất bại, rồi truy ngược để tìm rủi ro và mitigation trước khi sự cố thật xảy ra.

## Cách hiểu bằng lời của tôi

Premortem là postmortem chạy ngược thời gian. Thay vì đợi hệ thống sập mới học, team giả định "release này thành thảm họa" và hỏi: dependency nào nghẽn, config nào nguy hiểm, dữ liệu nào rollback khó, monitoring nào không thấy lỗi?

## Khi dùng

- Launch lớn hoặc thay đổi kiến trúc.
- Migration nhiều dependency.
- Dự án deadline gấp, margin lỗi thấp.
- Thay đổi có security, billing, auth hoặc data risk.

## Kết quả mong muốn

- Danh sách rủi ro theo probability/impact.
- Mitigation cụ thể cho rủi ro lớn.
- Rollback/recovery plan.
- Monitoring/alert cần thêm trước launch.
- Quyết định có giảm scope, staged rollout hoặc delay không.

## Liên kết

- [[Postmortem]]
- [[Phased Rollout]]
- [[Risk Matrix]]
- [[Blast Radius]]
- [[Chaos Engineering]]
