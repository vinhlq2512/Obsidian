---
type: concept
status: understood
sources:
  - "[[2025-06-17_how-the-google-cloud-outage-crashed-the-internet]]"
  - "[[2025-06-29_when-kv-falls-cloudflares-two-hour-outage]]"
  - "[[2026-06-11_must-know-deployment-strategies-from-big-bang-to-progressive]]"
source_sections:
  - "[[2025-06-17_how-the-google-cloud-outage-crashed-the-internet]]"
  - "[[2025-06-29_when-kv-falls-cloudflares-two-hour-outage]]"
  - "[[2026-06-11_must-know-deployment-strategies-from-big-bang-to-progressive]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - deployment
---

# Kill Switch

## Định nghĩa

Kill Switch là cơ chế tắt nhanh một feature, code path, validation, policy hoặc integration trong production để giảm impact khi incident xảy ra.

## Cách hiểu bằng lời của tôi

Kill switch là phanh khẩn cấp. Nó cần được thiết kế trước incident, có owner rõ, có observability, và phải được threat-model nếu tắt một check bảo mật.

## Bài học từ source

- Google có red-button để disable quota policy logic gây crash, nhưng feature không được bảo vệ bằng feature flag ngay từ rollout.
- Cloudflare Turnstile kill switch giảm lockout nhưng mở rủi ro token reuse, nên kill switch cũng cần security trade-off.

## Liên kết

- [[Feature Flag]]
- [[Rollback Strategy]]
- [[Fail Closed]]
- security trade-off
- [[Incident Response]]
