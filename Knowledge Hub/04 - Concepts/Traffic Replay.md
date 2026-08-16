---
type: concept
status: seed
sources:
  - "[[2025-01-05_modernizing-legacy-systems-without-breaking-production]]"
source_sections:
  - "[[2025-01-05_modernizing-legacy-systems-without-breaking-production]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - testing
  - migration
---

# Traffic Replay

## Định nghĩa

[[Traffic Replay]] là kỹ thuật capture traffic production, sanitize dữ liệu nhạy cảm, rồi chạy lại trên hệ mới hoặc môi trường test để so hành vi.

## Cách hiểu bằng lời của tôi

Test viết tay thường bỏ sót edge case thật. Traffic replay lấy chính lịch sử production làm test corpus, gồm mùa cao điểm, request hiếm, payload lạ và pattern user thật. Nó giúp migration thấy hệ mới khác hệ cũ ở đâu trước khi chuyển traffic thật.

## Cần có

- Capture không can thiệp vào production path.
- Sanitization để loại dữ liệu nhạy cảm.
- Storage nén và retention đủ dài.
- Replay acceleration để chạy nhanh hơn thời gian thật.
- Tool so diff behavior và performance.

## Liên kết

- [[Shadow Testing]]
- [[Behavioral Compatibility]]
- [[Load Testing]]
- [[Data Pipeline Validation]]
- [[Input Validation]]
