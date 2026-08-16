---
type: concept
status: understood
sources:
  - "[[2024-06-06_a-crash-course-on-content-delivery-networks-cdn-newsletter]]"
  - "[[2025-08-28_a-detailed-guide-to-content-delivery-networks-newsletter]]"
  - "[[2024-01-11_netflix-what-happens-when-you-press-play-part-2]]"
  - "[[2026-03-24_how-netflix-live-streams-to-100-million-devices-in-60-second]]"
source_sections:
  - "[[2024-06-06_a-crash-course-on-content-delivery-networks-cdn-newsletter]]"
  - "[[2024-01-11_netflix-what-happens-when-you-press-play-part-2]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - system-design
  - networking
---

# Content Delivery Network

## Cách hiểu bằng lời của tôi

[[Content Delivery Network]] là mạng edge server phân tán theo địa lý để đưa content tới gần user hơn. Nó giảm latency, giảm tải origin, tăng availability, và thường thêm lớp bảo vệ như TLS, WAF hoặc DDoS mitigation.

## Luồng request

```text
User request
-> DNS/GSLB/Anycast chọn edge gần hoặc khỏe
-> edge cache lookup
-> cache hit: trả content
-> cache miss: fetch origin, lưu cache, trả content
```

## Thành phần

- Origin server: nguồn dữ liệu authoritative.
- Edge server/PoP: cache và phục vụ content gần user.
- DNS/GSLB/Anycast: route user tới edge phù hợp.
- Control plane: cấu hình cache, routing, purge, monitoring.

## Trade-off cần nhớ

CDN làm hệ thống nhanh và bền hơn, nhưng cache invalidation, TTL, purge propagation và debug edge behavior trở thành một phần của thiết kế.

## Ví dụ Netflix Open Connect

Netflix dùng CDN chuyên dụng cho video: backend ở AWS xử lý control plane, còn video stream từ Open Connect Appliance gần user. Với VOD, nội dung được preposition trước vào các OCA dựa trên dự đoán popularity theo location. Với live, edge/CDN phối hợp với [[Live Streaming Origin]] qua segment template, TTL cho 404 và cache metadata để tránh request storm kéo về origin.

## Liên kết

- [[Caching Strategy]]
- [[Load Balancer]]
- [[High Availability]]
- [[Proactive Caching]]
- [[Video Streaming Architecture]]
