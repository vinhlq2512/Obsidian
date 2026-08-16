---
type: concept
status: understood
sources:
  - "[[2026-04-20_the-security-architecture-of-github-agentic-workflow]]"
source_sections:
  - "[[2026-04-20_the-security-architecture-of-github-agentic-workflow]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - ai-agent
  - security
---

# Safe Outputs Pipeline

## Định nghĩa

Safe Outputs Pipeline là pipeline deterministic kiểm tra, giới hạn và sanitize output agent trước khi output đó tác động tới hệ thống thật.

## Cách hiểu bằng lời của tôi

Ngay cả khi agent không có secret, nó vẫn có thể spam issue, tạo PR rác hoặc đưa nội dung độc hại ra ngoài. Safe outputs biến write operation thành staged intent: agent đề xuất, pipeline kiểm tra allowlist/quantity/content, rồi hệ thống mới thực thi.

## Các lớp kiểm soát

- Allowlist loại operation được phép.
- Quantity limit để tránh spam.
- Secret scanning và content sanitization.
- Moderation hoặc policy check trước khi publish.

## Liên kết

- [[Zero-Secret Agent Architecture]]
- [[Prompt Injection]]
- [[Kill Switch]]
- [[Least Privilege]]
- [[Agent Trust Boundary Logging]]
