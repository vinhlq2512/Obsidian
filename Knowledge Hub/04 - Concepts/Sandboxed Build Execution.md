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
  - security
---

# Sandboxed Build Execution

## Định nghĩa

[[Sandboxed Build Execution]] là cách chạy build script trong môi trường cô lập để code không tin cậy không thể ảnh hưởng tenant khác hoặc host platform.

## Cách hiểu bằng lời của tôi

Build script có quyền chạy code tùy ý. Nếu platform chạy build của nhiều khách hàng, build environment phải được xem như sandbox security boundary, không chỉ là chỗ cài dependency và chạy `npm build`.

## Pattern từ Vercel Hive

- Mỗi build chạy trong một cell microVM riêng.
- Container bên trong cell lo packaging/dependency.
- MicroVM lo kernel-level isolation.
- Cell bị destroy sau build để tránh leftover state leak.

## Liên kết

- [[Hostile Multi-Tenancy]]
- [[Firecracker MicroVM]]
- [[Build Provisioning Warm Pool]]
- [[Zero-Secret Agent Architecture]]
- [[Least Privilege]]
