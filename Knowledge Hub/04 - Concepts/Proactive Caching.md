---
type: concept
status: seed
sources:
  - "[[2024-01-11_netflix-what-happens-when-you-press-play-part-2]]"
  - "[[2026-03-24_how-netflix-live-streams-to-100-million-devices-in-60-second]]"
source_sections:
  - "[[2024-01-11_netflix-what-happens-when-you-press-play-part-2]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - system-design
  - caching
---

# Proactive Caching

## Định nghĩa

[[Proactive Caching]] là chiến lược đưa dữ liệu vào cache trước khi user request, dựa trên dự đoán nhu cầu hoặc lịch publish.

## Cách hiểu bằng lời của tôi

Cache-aside chờ user hỏi rồi mới fill cache. Proactive caching làm ngược lại: hệ thống đoán trước nội dung nào sẽ nóng ở đâu, chuyển dữ liệu tới edge trong giờ thấp điểm, và giảm khả năng request đầu tiên phải đi xa về origin.

## Khi nào hữu ích

- Content lớn, đọc nhiều, thay đổi ít, ví dụ video VOD.
- Nhu cầu có thể dự đoán theo vị trí, lịch phát hành hoặc popularity.
- Miss về origin rất đắt, gây tải lớn hoặc làm tăng latency thấy rõ.

## Trade-off

- Tốn storage và bandwidth chuẩn bị trước.
- Dự đoán sai làm lãng phí cache capacity.
- Cần inventory/control plane biết dữ liệu nào đang nằm ở node nào.
- Không thay thế được logic invalidation khi nội dung bị đổi hoặc có lỗi.

## Liên kết

- [[Caching Strategy]]
- [[Content Delivery Network]]
- [[Video Streaming Architecture]]
- [[Recommendation Funnel]]
