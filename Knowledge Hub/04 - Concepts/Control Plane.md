---
type: concept
status: understood
sources:
  - "[[2025-06-17_how-the-google-cloud-outage-crashed-the-internet]]"
  - "[[2024-12-23_the-chatgpt-outage-what-openais-post-mortem-revealed]]"
  - "[[2025-07-18_cloudflares-july-2025-outage-the-global-outage-triggered-by]]"
source_sections:
  - "[[2025-06-17_how-the-google-cloud-outage-crashed-the-internet]]"
  - "[[2024-12-23_the-chatgpt-outage-what-openais-post-mortem-revealed]]"
  - "[[2025-07-18_cloudflares-july-2025-outage-the-global-outage-triggered-by]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - infrastructure
---

# Control Plane

## Định nghĩa

Control Plane là lớp điều khiển cấu hình, policy, routing, quota, scheduling hoặc topology của hệ thống, khác với lớp trực tiếp phục vụ traffic người dùng.

## Cách hiểu bằng lời của tôi

Control plane thường không nằm trên request business trực tiếp, nhưng nó quyết định data plane có biết chạy như thế nào không. Khi control plane lỗi, hệ thống có thể không mất compute, nhưng mất khả năng route, discover service, validate policy hoặc cập nhật cấu hình.

## Bài học từ source

- Google Cloud Service Control là gatekeeper cho API traffic; policy metadata lỗi làm nhiều API trả 503.
- OpenAI outage cho thấy Kubernetes control plane bị quá tải có thể kéo theo service discovery và DNS.
- Cloudflare 1.1.1.1 incident là lỗi control plane ở network route topology, không phải DNS resolver logic.

## Liên kết

- [[Data Plane]]
- [[Kubernetes]]
- [[Service Discovery]]
- [[Feature Flag]]
- [[Phased Rollout]]
