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

# Annotation Platform

## Định nghĩa

[[Annotation Platform]] là hạ tầng và workflow để tạo, phân phối, kiểm soát chất lượng, version và tích hợp label/annotation vào vòng đời ML.

## Cách hiểu bằng lời của tôi

Annotation không phải việc phụ trong spreadsheet. Với Spotify, annotation trở thành platform: có role rõ, routing task, escalation, dashboard, API/data model chung và integration với batch/orchestration. Nhờ vậy ML team không phải dựng pipeline label lại từ đầu.

## Thành phần

- Interface cho audio, video, text, metadata hoặc multi-label task.
- Workforce role: annotator, quality analyst, project manager.
- Task routing và escalation cho case mơ hồ.
- Metrics: agreement, throughput, completion, confidence, resolution time.
- API/data model chung để nối vào training/evaluation.

## Liên kết

- [[Human-in-the-Loop Labeling]]
- [[Annotation Debt]]
- [[Model Feedback Loop]]
- [[Data Pipeline Validation]]
- [[Internal Platform as Product]]
