---
type: concept
status: seed
sources:
  - "[[2026-03-24_how-netflix-live-streams-to-100-million-devices-in-60-second]]"
source_sections:
  - "[[2026-03-24_how-netflix-live-streams-to-100-million-devices-in-60-second]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - system-design
  - media
---

# Live Streaming Origin

## Định nghĩa

[[Live Streaming Origin]] là lớp origin chuyên cho livestream, nằm giữa pipeline encode/package realtime và CDN, chịu trách nhiệm publish segment, kiểm soát metadata, chống request storm và bảo vệ write path.

## Cách hiểu bằng lời của tôi

Với VOD, nội dung đã chuẩn bị xong trước. Với live, mỗi segment chỉ xuất hiện ngay trước lúc user cần xem. Origin vì vậy không chỉ là chỗ chứa file; nó là checkpoint quyết định segment nào hợp lệ, segment nào chưa tới lúc, segment nào lỗi cần che đi, và request nào nên được ưu tiên.

## Cơ chế nổi bật từ nguồn Netflix

- Segment template cho phép edge/CDN biết range segment hợp lệ tại từng thời điểm.
- Request tới segment hơi sớm có thể được origin giữ mở và trả ngay khi segment publish.
- 404 có TTL ngắn giúp CDN cache failure tạm thời, tránh request lặp liên tục về origin.
- Metadata event/rendition/segment được tách khỏi media data để xử lý request không tồn tại mà không đụng media store.
- Publishing path được cô lập khỏi CDN traffic để read surge không làm hỏng write deadline.

## Storage và cache

Live Origin cần write availability cao, replication nhanh và read latency thấp. Nguồn Netflix mô tả hướng dùng storage chunked trên Cassandra kết hợp write-through cache để gần như toàn bộ read load đi qua cache, còn write path vẫn được bảo vệ.

## Liên kết

- [[Video Streaming Architecture]]
- [[Content Delivery Network]]
- [[Caching Strategy]]
- [[Rate Limiting]]
- [[Load Shedding]]
- [[Read Path]]
- [[Write Path]]
- [[Strong Consistency]]
- [[Quorum]]
