---
type: concept
status: seed
sources:
  - "[[2026-05-19_how-snapchat-serves-a-billion-predictions-per-second]]"
  - "[[2025-07-01_how-spotify-uses-genai-and-ml-to-annotate-a-hundred-million]]"
source_sections:
  - "[[2026-05-19_how-snapchat-serves-a-billion-predictions-per-second]]"
  - "[[2025-07-01_how-spotify-uses-genai-and-ml-to-annotate-a-hundred-million]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - mlops
  - feedback-loop
---

# Model Feedback Loop

## Định nghĩa

[[Model Feedback Loop]] là vòng đưa prediction, user outcome, annotation và monitoring signal quay lại training/evaluation để tạo model version tốt hơn.

## Cách hiểu bằng lời của tôi

ML platform không kết thúc ở response. Mỗi prediction tạo dữ liệu cho lần train sau; mỗi annotation sửa ground truth; mỗi drift signal cảnh báo pipeline. Platform trưởng thành là hệ thống liên tục tạo model version mới có kiểm soát.

## Liên kết

- [[Prediction Logging]]
- [[Incremental Model Training]]
- [[Annotation Platform]]
- [[Feature Drift]]
- [[Model Shadowing]]
