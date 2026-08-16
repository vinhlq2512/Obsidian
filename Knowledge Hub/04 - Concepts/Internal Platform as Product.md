---
type: concept
status: seed
sources:
  - "[[2026-01-12_processing-trillions-how-lyft-s-feature-store-grew-by-12-33]]"
  - "[[2026-01-13_how-lyft-built-an-ml-platform-that-serves-millions-of-predic]]"
  - "[[2025-07-01_how-spotify-uses-genai-and-ml-to-annotate-a-hundred-million]]"
source_sections:
  - "[[2026-01-12_processing-trillions-how-lyft-s-feature-store-grew-by-12-33]]"
  - "[[2026-01-13_how-lyft-built-an-ml-platform-that-serves-millions-of-predic]]"
  - "[[2025-07-01_how-spotify-uses-genai-and-ml-to-annotate-a-hundred-million]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - platform
  - developer-productivity
---

# Internal Platform as Product

## Định nghĩa

[[Internal Platform as Product]] là cách vận hành platform nội bộ như sản phẩm có user, onboarding, documentation, roadmap, support, telemetry và lựa chọn scope rõ.

## Cách hiểu bằng lời của tôi

Platform adoption là vấn đề con người nhiều như vấn đề kỹ thuật. Lyft thành công vì làm feature creation đơn giản bằng SQL + JSON, generator tự tạo repo deploy được, local dev chạy được, discovery tìm được feature có sẵn, và team biết cắt use case ít giá trị.

## Nguyên tắc

- Làm 90% use case trở nên tầm thường.
- Có local dev, staging và docs tốt.
- Đo failed workflow, latency, adoption và support threads.
- Cắt scope để không biến platform thành DSL khổng lồ.

## Liên kết

- [[ML Platform]]
- [[Developer Velocity]]
- [[Feature Discovery]]
- [[Model Onboarding]]
- [[Data Platform as Code]]
