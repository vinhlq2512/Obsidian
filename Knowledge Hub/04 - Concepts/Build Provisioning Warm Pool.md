---
type: concept
status: seed
sources:
  - "[[2026-05-26_how-vercel-cut-build-wait-times-from-90-seconds-to-5]]"
source_sections:
  - "[[2026-05-26_how-vercel-cut-build-wait-times-from-90-seconds-to-5]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - build-system
  - performance
---

# Build Provisioning Warm Pool

## Định nghĩa

[[Build Provisioning Warm Pool]] là pool các build environment đã khởi động sẵn để request build có thể bắt đầu ngay thay vì đi qua cold provisioning path.

## Cách hiểu bằng lời của tôi

Warm pool đổi chi phí idle compute lấy tail latency tốt hơn cho developer. Vercel giữ cell đã boot sẵn, container image đã load, nên phần lớn build không phải chờ microVM/container khởi động từ đầu.

## Trade-off

- Giảm build wait time rõ rệt ở common path.
- Tốn chi phí vì warm cell có thể ngồi rảnh.
- Pool size phải theo traffic pattern, spike và workload đặc biệt.

## Liên kết

- [[Developer Velocity]]
- [[Sandboxed Build Execution]]
- [[Serverless Cold Start]]
- [[Provisioned Concurrency]]
- [[Cost Optimization]]
