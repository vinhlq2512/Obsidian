---
type: concept
status: seed
sources:
  - "[[2026-05-19_how-snapchat-serves-a-billion-predictions-per-second]]"
  - "[[2025-08-19_how-reddit-delivers-notifications-to-tens-of-millions-of-use]]"
  - "[[2026-01-13_how-lyft-built-an-ml-platform-that-serves-millions-of-predic]]"
source_sections:
  - "[[2026-05-19_how-snapchat-serves-a-billion-predictions-per-second]]"
  - "[[2025-08-19_how-reddit-delivers-notifications-to-tens-of-millions-of-use]]"
  - "[[2026-01-13_how-lyft-built-an-ml-platform-that-serves-millions-of-predic]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - mlops
  - observability
---

# Prediction Logging

## Định nghĩa

[[Prediction Logging]] là việc ghi lại prediction, model version, input feature và outcome sau đó để phục vụ monitoring, debugging, training data generation và feedback loop.

## Cách hiểu bằng lời của tôi

Không log prediction thì ML platform bị mù sau response. Snap log feature/prediction và user action để tạo vòng training tiếp theo; Reddit dùng prediction logs để giảm train-serve skew vì training data phản ánh đúng feature production đã thấy.

## Liên kết

- [[Training-Serving Skew]]
- [[Model Feedback Loop]]
- [[AI Model Serving]]
- [[Observability]]
- [[Data Freshness]]
