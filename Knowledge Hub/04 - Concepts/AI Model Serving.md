---
type: concept
status: developing
sources:
  - "[[2025-10-20_what-actually-happens-when-you-press-send-to-chatgpt]]"
  - "[[2025-07-29_how-cursor-serves-billions-of-ai-code-completions-every-day]]"
  - "[[2026-07-01_how-openai-delivers-low-latency-voice-ai-for-900m-users]]"
  - "[[2026-01-13_how-lyft-built-an-ml-platform-that-serves-millions-of-predic]]"
  - "[[2026-05-19_how-snapchat-serves-a-billion-predictions-per-second]]"
  - "[[2025-07-29_how-salesforce-cut-model-onboarding-time-by-75percent]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - llm
  - mlops
  - production
---

# AI Model Serving

## Định nghĩa

AI model serving là lớp production nhận request, chuẩn bị context/input, chạy model inference, trả output và vận hành các yêu cầu về latency, throughput, cost, reliability, security và observability.

## Cách hiểu bằng lời của tôi

Một model tốt chưa đủ để thành sản phẩm AI tốt. Serving là toàn bộ đường ống biến model thành trải nghiệm thật: request vào, context được lắp, token được sinh, output stream về user, tool/safety/memory chen vào đúng chỗ, và hệ thống vẫn chịu được tải lớn.

## Đường đi phổ biến của request LLM

```text
client request
-> auth / validation
-> context building
-> tokenization
-> inference
-> streaming response
-> optional tool calls / safety checks
-> logging and monitoring
```

## Case study từ ByteByteGo

- ChatGPT nhấn mạnh context building, tokenization, tool calling, safety guardrails, memory và streaming.
- Cursor code completion tối ưu cho nhiều request rất nhỏ, latency thấp, context code ngắn và codebase indexing bằng embeddings.
- OpenAI voice AI tối ưu continuous audio stream bằng WebRTC, edge relay và session routing để giữ round-trip thấp.
- LyftLearn Serving dùng repo/microservice riêng cho từng team, common serving library, model loading/predict hook, shadowing, metrics/logging và model self-tests.
- Snap Bento cho thấy ranking serving là workload bất đối xứng: một request nở thành hàng trăm/nghìn prediction, nên feature lookup, batching, serialization và hardware split quan trọng ngang model.
- Salesforce dùng managed serving platform như Bedrock CMI qua wrapper tương thích để giảm thời gian model onboarding mà không phá workflow prediction cũ.

## Cần biết

- Serving offline/batch ưu tiên throughput; serving interactive ưu tiên tail latency.
- Context selection và caching ảnh hưởng chi phí nhiều như model size.
- Privacy/security phải nằm trên đường request, không chỉ ở model.
- Observability cần đo cả system metric lẫn model quality/regression.
- Model production thường sống rất lâu, nên [[Backward Compatibility]], [[Model Self-Test]] và [[Model Shadowing]] quan trọng hơn novelty của framework.

## Liên kết

- [[LLM Inference Engineering]]
- [[ML Platform]]
- [[Prediction Serving Fanout]]
- [[Feature Store]]
- [[Model Self-Test]]
- [[Model Shadowing]]
- [[Prediction Logging]]
- [[Model Onboarding]]
- [[Context Engineering]]
- [[Tool Use]]
- [[LLM Memory]]
- [[LLM Security]]
- [[Observability]]
- [[Model Benchmarking]]
