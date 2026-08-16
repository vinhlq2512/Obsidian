---
type: concept
status: seed
sources:
  - "[[2026-06-04_the-path-of-a-request-a-tour-of-modern-web-architecture]]"
  - "[[2026-02-17_how-cloudflare-eliminates-cold-starts-for-serverless-workers]]"
source_sections:
  - "[[2026-06-04_the-path-of-a-request-a-tour-of-modern-web-architecture]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - edge
  - system-design
---

# Edge Function

## Định nghĩa

[[Edge Function]] là code chạy tại edge location/CDN point of presence để xử lý một phần logic gần user hơn origin.

## Cách hiểu bằng lời của tôi

CDN ban đầu chủ yếu serve file/cache response. Edge function làm ranh giới mờ hơn: validate request, rewrite route, personalize nhẹ, auth check đơn giản hoặc transform response ngay tại edge. Đổi lại, runtime bị giới hạn và state/consistency khó hơn app server trung tâm.

## Khi hữu ích

- Redirect/rewrite/routing gần user.
- Lightweight personalization hoặc A/B routing.
- Request filtering trước origin.
- Giảm latency cho logic đơn giản và cache-aware.

## Liên kết

- [[Content Delivery Network]]
- [[API Gateway]]
- [[Latency]]
- [[Caching Strategy]]
- [[Web Request Path]]
