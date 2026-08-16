---
type: concept
status: developing
sources:
  - "[[2026-06-15_a-guide-to-ai-inference-engineering]]"
  - "[[2025-10-20_what-actually-happens-when-you-press-send-to-chatgpt]]"
  - "[[2025-07-29_how-cursor-serves-billions-of-ai-code-completions-every-day]]"
  - "[[2026-07-01_how-openai-delivers-low-latency-voice-ai-for-900m-users]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - llm
  - inference
  - production
---

# LLM Inference Engineering

## Định nghĩa

LLM inference engineering là kỷ luật vận hành model đã train trong production sao cho đạt cân bằng latency, throughput, cost, reliability và quality.

## Cách hiểu bằng lời của tôi

Train model là tạo ra năng lực. Inference engineering là làm năng lực đó phục vụ user thật ở tốc độ, chi phí và độ ổn định chấp nhận được.

## Mental model

- Prefill: xử lý prompt và tạo token đầu tiên; thường compute-bound; đo bằng time to first token.
- Decode: sinh token tiếp theo tuần tự; thường memory-bandwidth-bound; đo bằng tokens per second.
- [[KV Cache]] nối hai pha này lại.

## Đòn bẩy chính

- Batching để tăng throughput.
- Prefix caching để tái dùng prompt chung.
- [[Quantization]] để giảm weight/memory bandwidth.
- Speculative decoding để tăng tốc decode.
- Tensor/expert parallelism để chạy model lớn qua nhiều GPU.
- Disaggregation để tách prefill và decode theo hạ tầng riêng.
- Streaming giúp user thấy token sớm thay vì chờ toàn bộ response.
- Với workload realtime như code completion hoặc voice AI, context selection, edge routing và protocol latency quan trọng ngang model speed.

## Case study từ ByteByteGo

- ChatGPT request path: HTTPS request -> context building -> tokenization -> model inference -> streaming -> optional tool/safety checks.
- Cursor autocomplete: client gửi context code nhỏ, backend dùng model latency thấp để trả inline suggestion, còn codebase indexing dùng embedding/vector search để lấy context khi chat.
- OpenAI voice AI: tách stateless relay và stateful transceiver để giữ WebRTC latency thấp ở quy mô lớn.

## Khi nên đầu tư

Tự tối ưu inference đáng cân nhắc khi API cost đã lớn, yêu cầu latency vượt khả năng provider chung, hoặc reliability/SLA cần kiểm soát sâu hơn. Ở giai đoạn sớm, dùng API có sẵn thường giúp học product nhanh hơn.

## Liên kết

- [[Transformer Inference Optimization]]
- [[KV Cache]]
- [[AI Model Serving]]
- [[AI Hardware Accelerator]]
- [[Model Benchmarking]]
- [[Quantization]]
