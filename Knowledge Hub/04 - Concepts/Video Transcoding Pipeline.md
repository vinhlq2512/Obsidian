---
type: concept
status: seed
sources:
  - "[[2024-01-04_netflix-what-happens-when-you-press-play]]"
  - "[[2024-01-11_netflix-what-happens-when-you-press-play-part-2]]"
source_sections:
  - "[[2024-01-04_netflix-what-happens-when-you-press-play]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - system-design
  - media
---

# Video Transcoding Pipeline

## Định nghĩa

[[Video Transcoding Pipeline]] là pipeline chuyển media source thành nhiều định dạng/quality profile để nhiều thiết bị và điều kiện mạng khác nhau có thể phát video ổn định.

## Cách hiểu bằng lời của tôi

File video gốc quá lớn và không phù hợp trực tiếp với mọi device. Pipeline cần kiểm tra chất lượng, chia nhỏ để xử lý song song, encode thành nhiều profile, validate lại, rồi publish sang lớp phân phối.

## Luồng xử lý

```text
Source media
-> validate lỗi artifact, màu, frame
-> chia thành nhiều chunk nhỏ
-> encode/transcode song song
-> validate từng chunk
-> ghép hoặc package lại
-> tạo nhiều encoding profile
-> phân phối tới CDN/edge
```

## Vì sao cần chia chunk

Chia chunk giúp xử lý song song trên nhiều máy thay vì bắt một máy xử lý toàn bộ file lớn. Với workload media, parallelism là cách rút ngắn thời gian chuẩn bị nội dung trước khi publish.

## Liên kết

- [[Video Streaming Architecture]]
- [[Adaptive Bitrate Streaming]]
- [[Content Delivery Network]]
- [[Horizontal Scaling]]
