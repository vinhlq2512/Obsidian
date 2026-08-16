---
type: concept
status: seed
sources:
  - "[[2026-01-13_how-lyft-built-an-ml-platform-that-serves-millions-of-predic]]"
  - "[[2026-05-19_how-snapchat-serves-a-billion-predictions-per-second]]"
  - "[[2026-01-12_processing-trillions-how-lyft-s-feature-store-grew-by-12-33]]"
source_sections:
  - "[[2026-01-13_how-lyft-built-an-ml-platform-that-serves-millions-of-predic]]"
  - "[[2026-05-19_how-snapchat-serves-a-billion-predictions-per-second]]"
  - "[[2026-01-12_processing-trillions-how-lyft-s-feature-store-grew-by-12-33]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - mlops
  - platform
---

# ML Platform

## Định nghĩa

[[ML Platform]] là nền tảng nội bộ giúp team tạo feature, train, validate, deploy, serve, monitor và iterate model theo cách tự phục vụ nhưng vẫn có guardrail production.

## Cách hiểu bằng lời của tôi

ML platform tốt không chỉ là cụm GPU hoặc model registry. Nó là sản phẩm nội bộ làm cho đường đi từ dữ liệu đến prediction trở nên lặp lại được: feature có metadata, model có self-test, serving có observability, deployment có rollback, và user platform có workflow dễ dùng.

## Thành phần thường gặp

- [[Feature Store]] cho training và serving.
- Training workflow và model export.
- [[AI Model Serving]] hoặc prediction microservice.
- [[Model Shadowing]], [[Model Self-Test]] và validation.
- [[Prediction Logging]] và feedback loop.
- Documentation, generator, UI hoặc CLI để self-onboard.

## Liên kết

- [[AI Model Serving]]
- [[Feature Store]]
- [[Internal Platform as Product]]
- [[Developer Velocity]]
- [[Observability]]
