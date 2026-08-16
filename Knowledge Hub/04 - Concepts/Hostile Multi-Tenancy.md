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
  - security
  - platform
---

# Hostile Multi-Tenancy

## Định nghĩa

[[Hostile Multi-Tenancy]] là bối cảnh nhiều tenant chạy trên cùng hạ tầng nhưng platform phải giả định code/input của từng tenant có thể độc hại.

## Cách hiểu bằng lời của tôi

Kubernetes/container phù hợp với tenant hợp tác trong cùng tổ chức. Nhưng build platform như Vercel chạy code của khách hàng lạ; một build script có thể cố đọc secret tenant khác hoặc escape sandbox. Threat model này đòi hỏi boundary mạnh hơn container thông thường.

## Liên kết

- [[Multi-Tenancy]]
- [[Sandboxed Build Execution]]
- [[Firecracker MicroVM]]
- [[Blast Radius]]
- [[Least Privilege]]
