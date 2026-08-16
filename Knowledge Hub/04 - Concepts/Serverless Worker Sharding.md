---
type: concept
status: seed
sources:
  - "[[2026-02-17_how-cloudflare-eliminates-cold-starts-for-serverless-workers]]"
source_sections:
  - "[[2026-02-17_how-cloudflare-eliminates-cold-starts-for-serverless-workers]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - serverless
  - edge
---

# Serverless Worker Sharding

## Định nghĩa

[[Serverless Worker Sharding]] định tuyến request của một worker/app đến cùng một home server trong data center để giữ instance warm và giảm số lần cold start.

## Cách hiểu bằng lời của tôi

Cloudflare không cố làm mọi cold start nhanh hơn; họ làm cold start ít xảy ra hơn. Với low-traffic Worker, nếu request bị rải ra hàng trăm server thì server nào cũng thấy nó "lâu lâu mới đến" và liên tục eviction. Sharding gom request về một home server để memory reuse hiệu quả hơn.

## Cơ chế

```text
worker id + server list
-> consistent hash ring chọn home server
-> shard client forward request đến shard server nếu cần
-> nếu home server quá tải, request fallback về local lazy worker
```

## Trade-off

- Giảm eviction và tăng warm request rate.
- Thêm một lần nhảy nội bộ khi request không đến đúng home server.
- Cần load-shedding/fallback để một worker nóng không làm quá tải home server.

## Liên kết

- [[Serverless Cold Start]]
- [[Consistent Hashing]]
- [[Load Shedding]]
- [[Latency]]
- [[Edge Function]]
