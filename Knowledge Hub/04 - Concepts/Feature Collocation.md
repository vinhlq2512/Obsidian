---
type: concept
status: seed
sources:
  - "[[2026-05-19_how-snapchat-serves-a-billion-predictions-per-second]]"
source_sections:
  - "[[2026-05-19_how-snapchat-serves-a-billion-predictions-per-second]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - mlops
  - performance
---

# Feature Collocation

## Định nghĩa

[[Feature Collocation]] là việc đặt một phần feature corpus ngay trên inference instance để tránh network lookup fanout trong ranking/inference hot path.

## Cách hiểu bằng lời của tôi

Ranking request cần score nhiều candidate. Nếu mỗi candidate phải gọi remote feature store, latency và network cost nổ. Snap colocate document features trong memory của inference instance cho một số workload, đổi memory cost lấy latency và data-plane cost thấp hơn.

## Trade-off

- Giảm network fanout và tail latency.
- Tăng memory footprint trên inference fleet.
- Chỉ đáng khi corpus, traffic và latency budget khiến remote lookup quá đắt.

## Liên kết

- [[Online Feature Store]]
- [[Feature Store Cache]]
- [[Prediction Serving Fanout]]
- [[Latency]]
- [[Cost Optimization]]
