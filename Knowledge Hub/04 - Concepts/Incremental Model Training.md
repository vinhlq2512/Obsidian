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
  - training
---

# Incremental Model Training

## Định nghĩa

[[Incremental Model Training]] là workflow liên tục thêm event mới vào training data, retrain hoặc update model, validate và deploy version mới.

## Cách hiểu bằng lời của tôi

Trong feed/ranking, model production không phải artifact đứng yên. Hành vi user đổi, corpus đổi, feature đổi. Incremental training giúp model theo kịp freshness, nhưng cần validation và deployment control plane để không tự động đưa model xấu vào production.

## Liên kết

- [[Model Feedback Loop]]
- [[Prediction Logging]]
- [[Feature Store]]
- [[Continuous Deployment]]
- [[Data Pipeline Validation]]
