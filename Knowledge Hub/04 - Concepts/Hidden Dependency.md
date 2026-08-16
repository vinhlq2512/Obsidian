---
type: concept
status: understood
sources:
  - "[[2025-06-17_how-the-google-cloud-outage-crashed-the-internet]]"
  - "[[2025-06-29_when-kv-falls-cloudflares-two-hour-outage]]"
  - "[[2025-07-18_cloudflares-july-2025-outage-the-global-outage-triggered-by]]"
source_sections:
  - "[[2025-06-17_how-the-google-cloud-outage-crashed-the-internet]]"
  - "[[2025-06-29_when-kv-falls-cloudflares-two-hour-outage]]"
  - "[[2025-07-18_cloudflares-july-2025-outage-the-global-outage-triggered-by]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - system-design
---

# Hidden Dependency

## Định nghĩa

Hidden Dependency là dependency không hiển thị rõ trong sơ đồ hoặc mental model vận hành, nhưng khi lỗi lại ảnh hưởng tới service tưởng như độc lập.

## Cách hiểu bằng lời của tôi

Outage lớn thường không bắt đầu từ dependency ai cũng biết. Nó bắt đầu từ thứ bị xem là phụ: status page chạy trên chính cloud đang outage, auth của edge provider phụ thuộc cloud khác, config test ảnh hưởng production route, hoặc cache được tưởng nhầm là fallback.

## Cách phát hiện

- Hỏi source of truth của mỗi critical path là gì.
- Theo dõi dependency của observability/status/incident tooling.
- Kiểm tra config path có chạm production dù tên là test/staging không.
- Chạy chaos drill cho cold read, provider outage và control plane unavailable.

## Liên kết

- [[Blast Radius]]
- [[Cold Read Path]]
- [[Control Plane]]
- [[Incident Response]]
- dependency mapping
