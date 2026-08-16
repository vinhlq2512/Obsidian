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
  - data-quality
---

# Annotation Debt

## Định nghĩa

[[Annotation Debt]] là nợ chất lượng tích lũy từ label không nhất quán, guideline cũ, provenance thiếu hoặc annotation không còn phù hợp với task/model hiện tại.

## Cách hiểu bằng lời của tôi

Annotation debt nguy hiểm vì nó không làm pipeline đỏ ngay. Nó làm search/ranking/moderation/recommendation kém dần mà khó truy nguyên. Cách xử lý giống code debt: version guideline, track provenance, audit label cũ và chuẩn hóa định nghĩa.

## Liên kết

- [[Annotation Platform]]
- [[Annotation Quality Metrics]]
- [[Data Contract]]
- [[Technical Debt]]
- [[Model Feedback Loop]]
