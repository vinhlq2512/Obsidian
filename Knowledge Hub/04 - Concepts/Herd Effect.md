---
type: concept
status: understood
sources:
  - "[[2025-06-17_how-the-google-cloud-outage-crashed-the-internet]]"
  - "[[2025-06-29_when-kv-falls-cloudflares-two-hour-outage]]"
source_sections:
  - "[[2025-06-17_how-the-google-cloud-outage-crashed-the-internet]]"
  - "[[2025-06-29_when-kv-falls-cloudflares-two-hour-outage]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - distributed-systems
---

# Herd Effect

## Định nghĩa

Herd Effect là hiện tượng nhiều client/task cùng retry, restart, refresh hoặc repopulate cache gần như đồng thời, làm backend đang hồi phục bị quá tải.

## Cách hiểu bằng lời của tôi

Sau khi incident được "fix", hệ thống vẫn có thể chết tiếp vì tất cả thành phần cùng lao vào dependency vừa sống lại. Google Cloud us-central1 phục hồi chậm vì task restart hàng loạt hit Spanner; Cloudflare cũng nhắc tới nguy cơ mass cache repopulation sau KV recovery.

## Cách giảm thiểu

- Randomized exponential backoff.
- Throttle restart hoặc namespace re-enable.
- Progressive recovery thay vì bật lại tất cả cùng lúc.
- Queue hoặc rate limiter cho cold read/cache refill.

## Liên kết

- [[Backpressure]]
- [[Rate Limiting]]
- [[Cache Stampede]]
- [[Retry Storm]]
- [[Phased Rollout]]
