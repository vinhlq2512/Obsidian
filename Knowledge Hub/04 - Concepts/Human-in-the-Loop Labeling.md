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

# Human-in-the-Loop Labeling

## Định nghĩa

[[Human-in-the-Loop Labeling]] kết hợp model/automation với reviewer người thật để tạo hoặc kiểm tra label, thường để model xử lý case dễ và con người xử lý case mơ hồ.

## Cách hiểu bằng lời của tôi

Không phải humans vs AI. Spotify dùng LLM để pre-label case rõ, còn domain expert và quality analyst tập trung vào judgement, ambiguity và policy nuance. Điểm quan trọng là có escalation path và metrics để biết khi nào automation đang lệch.

## Liên kết

- [[Annotation Platform]]
- [[Annotation Quality Metrics]]
- [[Annotation Debt]]
- [[LLM-as-Judge]]
- [[Model Feedback Loop]]
