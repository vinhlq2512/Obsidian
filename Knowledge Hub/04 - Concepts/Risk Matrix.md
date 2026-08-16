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
  - planning
  - reliability
---

# Risk Matrix

## Định nghĩa

[[Risk Matrix]] là cách phân loại rủi ro theo xác suất xảy ra và mức độ ảnh hưởng để ưu tiên mitigation.

## Cách hiểu bằng lời của tôi

Trong premortem, team thường nghĩ ra rất nhiều cách hệ thống có thể fail. Risk matrix giúp tránh xử lý theo cảm giác: rủi ro impact cao và probability cao cần mitigation trước; rủi ro impact thấp có thể chỉ cần monitor hoặc chấp nhận.

## Khi dùng

- Premortem trước launch lớn.
- Đánh giá thay đổi kiến trúc hoặc dependency mới.
- Ưu tiên action item sau postmortem.
- Quyết định rollout theo pha hay rollback plan.

## Liên kết

- [[Premortem]]
- [[Postmortem]]
- [[Blast Radius]]
- [[Phased Rollout]]
