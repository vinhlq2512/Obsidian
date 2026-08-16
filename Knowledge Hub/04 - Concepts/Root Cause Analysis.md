---
type: concept
status: seed
sources:
  - "[[2024-12-04_writing-post-mortems-a-tech-lead-s-guide-to-learning-from-fa]]"
  - "[[2024-12-23_the-chatgpt-outage-what-openais-post-mortem-revealed]]"
  - "[[2026-03-31_how-meta-turned-debugging-into-a-product]]"
source_sections:
  - "[[2024-12-04_writing-post-mortems-a-tech-lead-s-guide-to-learning-from-fa]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - incident
---

# Root Cause Analysis

## Định nghĩa

[[Root Cause Analysis]] là quá trình tìm trigger trực tiếp và các nguyên nhân hệ thống khiến incident xảy ra hoặc không bị chặn sớm.

## Cách hiểu bằng lời của tôi

Root cause không nên dừng ở "config sai" hay "deploy lỗi". Câu hỏi sâu hơn là vì sao config sai lọt qua review/test, vì sao monitor không phát hiện sớm, vì sao rollback khó, và vì sao blast radius lớn. RCA tốt tạo action item thay đổi hệ thống, không chỉ sửa triệu chứng.

Meta DrP thêm một góc nhìn quan trọng: nếu root-cause expertise cứ nằm trong đầu senior engineer, mỗi incident sẽ bị điều tra lại từ đầu. [[Debugging as Code]] biến logic điều tra thành analyzer có review, test, backtest và CI/CD.

## Cách hỏi

- Trigger đầu tiên là gì?
- Tại sao guardrail không chặn?
- Tại sao monitoring/alerting không phát hiện đủ sớm?
- Tại sao mitigation/recovery mất lâu?
- Điều gì là systemic gap chứ không phải lỗi cá nhân?

## Liên kết

- [[Postmortem]]
- [[Incident Response]]
- [[Observability]]
- [[Phased Rollout]]
- [[Blast Radius]]
- [[Debugging as Code]]
- [[Automated Root Cause Analysis]]
