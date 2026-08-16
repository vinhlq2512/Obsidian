---
type: synthesis
status: seed
concepts:
  - "[[ML Platform]]"
  - "[[Feature Store]]"
  - "[[Training-Serving Skew]]"
  - "[[AI Model Serving]]"
  - "[[Prediction Serving Fanout]]"
  - "[[Model Shadowing]]"
  - "[[Prediction Logging]]"
  - "[[Annotation Platform]]"
sources:
  - "[[2026-01-12_processing-trillions-how-lyft-s-feature-store-grew-by-12-33]]"
  - "[[2026-01-13_how-lyft-built-an-ml-platform-that-serves-millions-of-predic]]"
  - "[[2026-05-19_how-snapchat-serves-a-billion-predictions-per-second]]"
  - "[[2025-07-29_how-salesforce-cut-model-onboarding-time-by-75percent]]"
  - "[[2025-04-15_inside-spotifys-ml-annotation-system-scaling-human-machine-l]]"
  - "[[2025-07-01_how-spotify-uses-genai-and-ml-to-annotate-a-hundred-million]]"
questions: []
created_at: 2026-08-16
updated_at: 2026-08-16
tags:
  - synthesis
  - mlops
  - system-design
---

# ML Platform and Prediction Serving Patterns

## Luận điểm chính

Production ML platform là hệ thống vòng lặp, không phải pipeline một chiều. Feature được tạo và phục vụ ở hai thế giới offline/online, model được train/export/deploy liên tục, prediction được log để tạo training data mới, và annotation/quality feedback giữ ground truth không mục.

## Pattern chính

- [[Feature Store]] nối [[Offline Feature Store]] và [[Online Feature Store]] để giảm [[Training-Serving Skew]].
- [[AI Model Serving]] cần ownership, model loading/predict interface, observability, [[Model Self-Test]] và [[Model Shadowing]].
- [[Prediction Serving Fanout]] giải thích vì sao ranking platform phải tối ưu feature lookup, batching, serialization và compute placement.
- [[Feature Collocation]], [[Inference Compute Graph Split]] và [[Raw Feature Transport]] là các tối ưu data plane/inference khi scale rất lớn.
- [[Prediction Logging]], [[Model Feedback Loop]] và [[Incremental Model Training]] biến mỗi request thành dữ liệu cho model version tiếp theo.
- [[Annotation Platform]], [[Human-in-the-Loop Labeling]] và [[Annotation Quality Metrics]] giữ label quality trong các workflow nhiều con người và nhiều model.
- [[Internal Platform as Product]] và [[Model Onboarding]] quyết định adoption: platform phải làm đường đi phổ biến dễ hơn tự dựng.

## Mental model

```text
events + annotations
-> feature pipelines
-> offline store cho training
-> online store/cache cho serving
-> model training/export/deployment
-> prediction serving
-> prediction logs + outcomes
-> monitoring, drift, retraining, annotation feedback
```

## Trade-off cần nhớ

- Feature store càng dễ dùng thì càng phải có discovery và metadata để tránh duplication.
- Serving model lớn không chỉ tốn GPU; feature lookup và serialization có thể là chi phí chính.
- Managed serving giảm onboarding nhưng cần wrapper để giữ contract và standards nội bộ.
- Annotation nhanh nhưng thiếu quality metric sẽ tạo annotation debt.

## Liên kết

- [[Data Platform Processing Patterns]]
- [[AI Search and Recommendation Systems]]
- [[Production AI Evaluation and Observability]]
- [[Observability]]
- [[Cost Optimization]]
