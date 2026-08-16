---
type: concept
status: seed
sources:
  - "[[2025-04-15_inside-spotifys-ml-annotation-system-scaling-human-machine-l]]"
  - "[[2025-07-01_how-spotify-uses-genai-and-ml-to-annotate-a-hundred-million]]"
source_sections:
  - "[[2025-04-15_inside-spotifys-ml-annotation-system-scaling-human-machine-l]]"
  - "[[2025-07-01_how-spotify-uses-genai-and-ml-to-annotate-a-hundred-million]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - mlops
  - annotation
---

# Annotation Quality Metrics

## Định nghĩa

[[Annotation Quality Metrics]] là các chỉ số đo chất lượng và vận hành của annotation workflow, như reviewer agreement, escalation volume, time to resolution, confidence và downstream model impact.

## Cách hiểu bằng lời của tôi

Bad label không tạo outage rõ ràng, nó làm model quyết định sai âm thầm. Vì vậy annotation platform cần đo cả throughput lẫn chất lượng. Agreement thấp hoặc escalation tăng là tín hiệu guideline/task/model đang có vấn đề.

## Liên kết

- [[Annotation Platform]]
- [[Human-in-the-Loop Labeling]]
- [[Annotation Debt]]
- [[Data Pipeline Validation]]
- [[Model Feedback Loop]]
