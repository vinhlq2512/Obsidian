---
type: concept
status: understood
sources:
  - "[[2025-06-29_when-kv-falls-cloudflares-two-hour-outage]]"
source_sections:
  - "[[2025-06-29_when-kv-falls-cloudflares-two-hour-outage]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - security
  - reliability
---

# Fail Closed

## Định nghĩa

Fail Closed là chế độ lỗi trong đó hệ thống từ chối hoặc chặn request khi không thể xác minh điều kiện an toàn.

## Cách hiểu bằng lời của tôi

Với auth/access/security, fail closed thường đúng hơn fail open vì cho nhầm người vào có thể tệ hơn lockout. Nhưng fail closed vẫn gây outage trải nghiệm, nên cần fallback flow, manual override hoặc degraded mode được thiết kế trước.

## Liên kết

- [[Authorization]]
- [[Authentication]]
- [[Least Privilege]]
- [[Graceful Degradation]]
- [[Kill Switch]]
