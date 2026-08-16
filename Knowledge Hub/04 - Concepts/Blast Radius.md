---
type: concept
status: seed
sources:
  - "[[2025-06-29_when-kv-falls-cloudflares-two-hour-outage-byte-sized-design]]"
  - "[[2025-03-11_on-september-24-2020-datadogs-us-region-suffered-a-multi-hour-outage-due-to-a-failure-in-its-service-discovery-byte-sized-design]]"
source_sections:
  - "[[2025-06-29_when-kv-falls-cloudflares-two-hour-outage-byte-sized-design]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - system-design
---

# Blast Radius

## Định nghĩa

[[Blast Radius]] là phạm vi ảnh hưởng khi một dependency, component, region, provider hoặc config lỗi.

## Cách hiểu bằng lời của tôi

Một hệ thống không chỉ cần biết "cái gì có thể hỏng", mà còn phải biết "nó kéo theo bao nhiêu thứ khác". Dependency dùng chung càng nằm trên critical path của nhiều sản phẩm thì blast radius càng lớn. Vấn đề thường không lộ ra khi cache hit; nó lộ ra lúc cold read, write, auth hoặc config refresh cần source-of-truth.

## Cách giảm blast radius

- Tách critical path giữa các sản phẩm/tenant/region.
- Có fallback hoặc degraded mode cho dependency dùng chung.
- Dùng kill switch có threat model rõ.
- Tránh để cache bị hiểu nhầm là fallback bền vững.
- Diễn tập incident để biết service nào fail open, fail closed hoặc shed load.

## Liên kết

- [[Partial Failure]]
- [[Cascading Failure]]
- [[Graceful Degradation]]
- [[Bulkhead Pattern]]
- [[Load Shedding]]
- [[High Availability]]
