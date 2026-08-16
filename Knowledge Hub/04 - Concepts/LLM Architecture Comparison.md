---
type: concept
status: seed
sources:
  - "[[2026-07-07_chatgpt-vs-gemini-vs-claude-how-they-differ]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - llm
  - architecture
---

# LLM Architecture Comparison

## Định nghĩa

LLM architecture comparison là cách so sánh các hệ model theo lựa chọn kiến trúc và vận hành, thay vì chỉ so sánh bằng benchmark hoặc cảm giác khi chat.

## Các trục so sánh

- Density: model dense, mixture-of-experts hoặc hệ routed nhiều model.
- Multimodality: pipeline tuần tự với encoder/projection riêng, hoặc native multimodal được huấn luyện từ đầu trên nhiều modality.
- Context: context window lớn chưa đủ; còn phải xử lý context rot, compaction và RAG.
- Alignment: RLHF, constitutional AI, model spec hoặc deliberative alignment đặt ưu tiên hành vi khác nhau.
- Reasoning: có thể dùng routed sub-model, adaptive thinking trong cùng model, hoặc chế độ reasoning chuyên biệt.

## Cách hiểu bằng lời của tôi

Không nên hỏi "model nào thông minh hơn" một cách chung chung. Câu hỏi đúng hơn là: model đó được tối ưu cho latency, multimodal, context dài, tool use, coding, safety hay reasoning? Cùng một benchmark có thể che mất trade-off vận hành phía sau.

## Liên kết

- [[Large Language Model]]
- [[Multimodal LLM]]
- [[LLM Inference Engineering]]
- [[LLM Evaluation]]
- [[AI Model Serving]]
- [[Context Engineering]]
