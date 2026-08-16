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
  - model-quality
---

# Training-Serving Skew

## Định nghĩa

[[Training-Serving Skew]] là lỗi khi dữ liệu, feature, preprocessing hoặc phân phối mà model thấy lúc training khác với lúc serving production.

## Cách hiểu bằng lời của tôi

Model có thể score tốt offline nhưng tệ ngoài đời nếu feature online không giống feature offline. Đây là lỗi hệ thống, không chỉ lỗi model. Feature store, prediction logging và online/offline comparison tồn tại để phát hiện và giảm skew.

## Cách giảm

- Dùng cùng metadata và định nghĩa feature cho offline/online.
- Log feature thực tế tại thời điểm prediction.
- Recompute offline prediction để so với online output.
- Monitor feature/prediction distribution drift.

## Liên kết

- [[Feature Store]]
- [[Offline Feature Store]]
- [[Online Feature Store]]
- [[Prediction Logging]]
- [[Feature Drift]]
