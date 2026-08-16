---
type: concept
status: seed
sources:
  - "[[2025-03-18_how-netflix-stores-140-million-hours-of-viewing-data-per-day]]"
  - "[[2025-02-11_how-netflix-built-a-distributed-counter-for-billions-of-user]]"
source_sections:
  - "[[2025-03-18_how-netflix-stores-140-million-hours-of-viewing-data-per-day]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - database
  - system-design
---

# Time-Series Data Storage

## Định nghĩa

[[Time-Series Data Storage]] là cách lưu dữ liệu gắn với thời gian, thường tối ưu cho write liên tục, query theo time range, retention và downsampling/compression theo tuổi dữ liệu.

## Cách hiểu bằng lời của tôi

Dữ liệu thời gian không nên luôn được lưu cùng một kiểu từ lúc mới sinh đến lúc thành archive. Dữ liệu mới thường cần read/write nhanh; dữ liệu cũ thường cần rẻ, nén tốt và ít query hơn. Thiết kế tốt tách storage theo access pattern và tuổi dữ liệu.

## Pattern từ viewing history

- Recent/live data: giữ dạng dễ update, tối ưu latency vì user hay truy cập gần đây.
- Older/compressed data: nén để giảm storage, chấp nhận read chậm hơn.
- Historical summary: chỉ giữ thông tin tổng hợp đủ dùng cho use case dài hạn.
- Large value chunking: chia blob nén lớn thành chunk nhỏ để đọc/ghi song song.
- Data rotation: background job chuyển data từ recent sang past rồi sang historical.

## Pitfall

- Một row/user quá rộng làm read phải scan nhiều SSTable hoặc nhiều column.
- Pagination tránh timeout nhưng có thể làm tổng thời gian fetch toàn bộ history tăng.
- Nếu client fetch nhiều hơn cần thiết, storage tốt vẫn bị lãng phí network và latency.
- Compaction/read repair có thể trở thành chi phí nền lớn khi dữ liệu tăng.

## Liên kết

- [[LSM Tree]]
- [[Storage Engine]]
- [[Database Sharding]]
- [[Caching Strategy]]
- [[Data Lifecycle Management]]
