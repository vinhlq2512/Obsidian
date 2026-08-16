---
type: concept
status: seed
sources:
  - "[[2024-01-04_netflix-what-happens-when-you-press-play]]"
  - "[[2024-01-11_netflix-what-happens-when-you-press-play-part-2]]"
  - "[[2026-03-24_how-netflix-live-streams-to-100-million-devices-in-60-second]]"
source_sections:
  - "[[2024-01-04_netflix-what-happens-when-you-press-play]]"
  - "[[2024-01-11_netflix-what-happens-when-you-press-play-part-2]]"
  - "[[2026-03-24_how-netflix-live-streams-to-100-million-devices-in-60-second]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - system-design
  - media
---

# Video Streaming Architecture

## Định nghĩa

[[Video Streaming Architecture]] là kiến trúc đưa video từ hệ thống chuẩn bị nội dung tới thiết bị người xem với latency thấp, chất lượng ổn định và khả năng chịu tải rất lớn.

## Cách hiểu bằng lời của tôi

Streaming video không chỉ là "đọc file từ server". Hệ thống phải chuẩn bị nhiều phiên bản video, đặt nội dung gần user, chọn route/CDN phù hợp, rồi để client thích nghi liên tục với mạng và thiết bị.

## Luồng tổng quát

```text
Media source
-> validate và chia chunk
-> encode/transcode thành nhiều profile
-> phân phối tới CDN/edge
-> client gửi play request tới backend/control plane
-> backend trả danh sách endpoint phù hợp
-> client chọn endpoint và tự điều chỉnh chất lượng khi mạng thay đổi
```

## Các mặt phẳng trong hệ thống

- Control plane: backend xử lý user, catalog, license, recommendation, playback decision và danh sách endpoint.
- Data plane: CDN/edge trực tiếp stream segment video tới client.
- Media pipeline: validate, chunk, transcode, package và publish nội dung.
- Client plane: app/SDK đo chất lượng kết nối, chọn server, đổi chất lượng hoặc đổi endpoint khi cần.

## Điểm thiết kế quan trọng

- Video nên được phục vụ gần user nhất có thể để giảm [[Latency]] và giảm tải đường backbone.
- Nhiều encoding profile giúp client chọn format phù hợp với device, network, plan và ngôn ngữ.
- Client thông minh là một phần của reliability: khi OCA/server/network xấu đi, client có thể chuyển endpoint hoặc hạ chất lượng.
- Live streaming khó hơn VOD vì segment được tạo theo thời gian thực và mỗi write/read đều bị ràng buộc bởi deadline ngắn.

## Liên kết

- [[Content Delivery Network]]
- [[Video Transcoding Pipeline]]
- [[Adaptive Bitrate Streaming]]
- [[Live Streaming Origin]]
- [[Caching Strategy]]
- [[Latency]]
