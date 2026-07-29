---
type: concept
status: seed
source:
  - "[[Hands-On LLM - Chapter 01 - An Introduction to Large Language Models]]"
  - "[[Hands-On LLM - Chapter 03 - Looking Inside Large Language Models]]"
tags:
  - concept
  - llm
  - generation
---

# Generative Model

## Định nghĩa

Generative model là model có khả năng sinh dữ liệu mới, trong LLM thường là sinh token tiếp theo để tạo văn bản, code hoặc câu trả lời.

## Cách hiểu bằng lời của tôi

Model dạng này viết tiếp. Nó nhận context, dự đoán token kế tiếp, thêm token đó vào context, rồi lặp lại cho đến khi hoàn thành output.

## Cần biết

- Decoder-only models như GPT là ví dụ tiêu biểu.
- Output chịu ảnh hưởng mạnh bởi prompt và decoding strategy.
- Có thể dùng cho classification, nhưng thường tốn chi phí/latency hơn representation models.

## Liên kết

- [[Large Language Model]]
- [[Prompt Engineering]]
- [[Fine-tuning]]
- [[DPO]]

