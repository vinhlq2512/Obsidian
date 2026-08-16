---
type: concept
status: seed
sources:
  - "[[2025-09-16_how-anthropic-built-a-multi-agent-research-system]]"
  - "[[2026-02-09_how-yelp-built-yelp-assistant]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - evaluation
  - grounding
  - llm
---

# Citation Quality

## Định nghĩa

Citation quality là mức độ citation trong câu trả lời thật sự hỗ trợ claim được đưa ra, đúng nguồn, đúng đoạn và không chỉ là trang trí.

## Cách hiểu bằng lời của tôi

Một câu trả lời có nhiều citation vẫn có thể không grounded nếu citation không chứng minh claim. Citation quality hỏi: claim này lấy từ đâu, nguồn đó có nói vậy không, và attribution có bị gắn nhầm không?

## Khi đánh giá

- Mỗi claim quan trọng có evidence tương ứng không?
- Citation có dẫn tới đúng source/snippet không?
- Có claim nào vượt quá bằng chứng không?
- Có dùng nguồn kém chất lượng khi nguồn tốt hơn tồn tại không?

## Liên kết

- [[Evidence-Grounded Generation]]
- [[LLM Evaluation]]
- [[Agent Evaluation]]
- [[AI Hallucination]]
