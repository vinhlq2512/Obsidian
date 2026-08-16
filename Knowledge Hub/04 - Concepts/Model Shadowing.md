---
type: concept
status: seed
sources:
  - "[[2026-01-13_how-lyft-built-an-ml-platform-that-serves-millions-of-predic]]"
source_sections:
  - "[[2026-01-13_how-lyft-built-an-ml-platform-that-serves-millions-of-predic]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - mlops
  - deployment
---

# Model Shadowing

## Định nghĩa

[[Model Shadowing]] là kỹ thuật chạy model mới song song với model production trên cùng request để so output/metric mà chưa dùng kết quả mới cho quyết định thật.

## Cách hiểu bằng lời của tôi

Shadowing cho phép test model trên traffic thật mà không đặt user vào rủi ro. Platform có thể route request đến model production và model candidate, log prediction của cả hai, rồi phân tích divergence, latency và error trước rollout.

## Liên kết

- [[AI Model Serving]]
- [[Shadow Testing]]
- [[Prediction Logging]]
- [[Canary Deployment]]
- [[Model Self-Test]]
