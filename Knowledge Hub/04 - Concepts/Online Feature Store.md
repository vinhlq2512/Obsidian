---
type: concept
status: seed
sources:
  - "[[2026-01-12_processing-trillions-how-lyft-s-feature-store-grew-by-12-33]]"
  - "[[2026-05-19_how-snapchat-serves-a-billion-predictions-per-second]]"
source_sections:
  - "[[2026-01-12_processing-trillions-how-lyft-s-feature-store-grew-by-12-33]]"
  - "[[2026-05-19_how-snapchat-serves-a-billion-predictions-per-second]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - mlops
  - feature-store
---

# Online Feature Store

## Định nghĩa

[[Online Feature Store]] lưu và phục vụ feature latency thấp cho online prediction hoặc ranking request.

## Cách hiểu bằng lời của tôi

Online store nằm trên hot path nên yêu cầu khác offline store: lookup nhanh, payload nhỏ, retry/timeout rõ, cache hợp lý và monitoring tail latency. Lyft dùng DynamoDB làm source of truth, ValKey làm cache; Snap vận hành online feature store ở quy mô TB/s read.

## Liên kết

- [[Feature Store]]
- [[Offline Feature Store]]
- [[Feature Store Cache]]
- [[Feature Collocation]]
- [[AI Model Serving]]
- [[Latency]]
