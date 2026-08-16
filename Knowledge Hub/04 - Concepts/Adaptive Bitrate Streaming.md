---
type: concept
status: seed
sources:
  - "[[2024-01-04_netflix-what-happens-when-you-press-play]]"
  - "[[2024-01-11_netflix-what-happens-when-you-press-play-part-2]]"
  - "[[2026-03-24_how-netflix-live-streams-to-100-million-devices-in-60-second]]"
source_sections:
  - "[[2024-01-11_netflix-what-happens-when-you-press-play-part-2]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - system-design
  - media
---

# Adaptive Bitrate Streaming

## Định nghĩa

[[Adaptive Bitrate Streaming]] là cách client chọn chất lượng video phù hợp với điều kiện mạng và thiết bị, rồi thay đổi chất lượng trong lúc xem nếu điều kiện thay đổi.

## Cách hiểu bằng lời của tôi

Thay vì cố stream một file chất lượng cao cố định, hệ thống chuẩn bị nhiều phiên bản của cùng nội dung. Client theo dõi mạng đang nhanh hay chậm, server đang khỏe hay quá tải, rồi chọn rendition vừa đủ tốt để tránh giật/dừng.

## Cơ chế

```text
Nhiều encoding profile
-> playback service trả endpoint/URL ứng viên
-> client probe chất lượng kết nối
-> client chọn OCA/rendition tốt nhất
-> trong lúc xem, client tiếp tục đo mạng
-> mạng xấu: hạ bitrate hoặc đổi OCA
-> mạng tốt: tăng bitrate
```

## Trade-off

- Tăng trải nghiệm người xem vì hệ thống ưu tiên phát liên tục hơn là giữ chất lượng tối đa bằng mọi giá.
- Cần pipeline encode ra nhiều profile, làm tăng storage và chi phí chuẩn bị nội dung.
- Client trở thành một thành phần điều phối quan trọng, nên SDK/app phải được kiểm soát tốt.

## Liên kết

- [[Video Streaming Architecture]]
- [[Video Transcoding Pipeline]]
- [[Content Delivery Network]]
- [[Latency]]
- [[Graceful Degradation]]
