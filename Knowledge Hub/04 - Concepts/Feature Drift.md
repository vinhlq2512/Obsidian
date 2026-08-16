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
  - observability
---

# Feature Drift

## Định nghĩa

[[Feature Drift]] là thay đổi bất thường trong phân phối hoặc thống kê của feature theo thời gian, có thể làm model prediction lệch khỏi kỳ vọng.

## Cách hiểu bằng lời của tôi

Feature drift thường là dấu hiệu upstream pipeline, logging, user behavior hoặc product surface đã đổi. Snap monitor mean/distribution của feature và prediction để phát hiện khi một phần hệ thống ML không còn nhìn giống điều kiện training.

## Liên kết

- [[Training-Serving Skew]]
- [[Model Feedback Loop]]
- [[Observability]]
- [[Data Freshness]]
- [[Data Pipeline Validation]]
