---
type: concept
status: developing
sources:
  - "[[2026-01-12_a-guide-to-llm-evals]]"
  - "[[2025-09-16_how-anthropic-built-a-multi-agent-research-system]]"
  - "[[2026-01-20_this-isnt-an-ai-summarizer-and-that-matters-byte-sized-design]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - llm
  - evaluation
---

# LLM-as-Judge

## Định nghĩa

LLM-as-judge là cách dùng một model để chấm output của model/hệ thống khác theo rubric định nghĩa trước.

## Cách hiểu bằng lời của tôi

LLM-as-judge không biến đánh giá thành chân lý tuyệt đối. Nó là một công cụ scale review: chấm nhiều case nhanh hơn người, nhưng phải được calibrate bằng human labels và failure analysis.

## Khi hữu ích

- Output có nhiều cách đúng, khó exact match.
- Cần chấm factuality, completeness, citation hoặc tone.
- Cần regression check nhanh giữa prompt/model versions.

## Rủi ro

- Judge có bias riêng.
- Rubric mơ hồ làm score nhiễu.
- Có thể chấm hay về văn phong nhưng bỏ qua evidence thật.
- Không thay thế human review ở case high-stakes hoặc metric chưa ổn định.

## Liên kết

- [[LLM Evaluation]]
- [[Agent Evaluation]]
- [[Model Benchmarking]]
- [[AI Hallucination]]
