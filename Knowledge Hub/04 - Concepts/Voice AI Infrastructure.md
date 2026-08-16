---
type: concept
status: understood
sources:
  - "[[2026-07-01_how-openai-delivers-low-latency-voice-ai-for-900m-users]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - ai
  - voice-ai
  - streaming
  - real-time
---

# Voice AI Infrastructure

## Định nghĩa

Voice AI Infrastructure (Hạ tầng AI giọng nói thời gian thực) là hệ thống kiến trúc mạng, xử lý tín hiệu và mô hình AI được thiết kế để xử lý luồng âm thanh hai chiều (audio streaming) với độ trễ cực thấp (dưới 300ms) phục vụ tương tác giọng nói tự nhiên giữa người và máy.

## Luồng kiến trúc xử lý

```text
User Speech (Audio Chunk)
-> WebSockets / WebRTC Media Server (Edge POP)
-> Native End-to-End Multimodal Model (Speech-to-Speech)
   OR [ASR (STT) -> LLM -> TTS Pipeline with Speculative Decoding]
-> Audio Stream Chunk Response -> User Speaker
```

- **Native Speech-to-Speech**: Thay vì ghép 3 mô hình riêng biệt (Speech-to-Text $\rightarrow$ LLM $\rightarrow$ Text-to-Speech), các hệ thống voice AI thế hệ mới dùng mô hình đa thức thể nguyên bản (Native Multimodal Model) nhận audio token và sinh trực tiếp audio token. Kỹ thuật này loại bỏ độ trễ dịch giữa văn bản và âm thanh.
- **WebSockets / WebRTC**: Sử dụng giao thức truyền thông hai chiều thời gian thực để stream từng khung âm thanh (PCM/Opus chunks) ngay khi người dùng đang nói.
- **Interruption Handling**: Khả năng phát hiện giọng nói người dùng chen ngang (VAD - Voice Activity Detection) để dừng ngay lập tức luồng sinh audio của mô hình ở edge.

## Trade-off

- Đòi hỏi băng thông và máy chủ edge phủ rộng khắp thế giới để giảm RTT (Round-Trip Time).
- Xử lý audio token đòi hỏi memory footprint và GPU compute lớn hơn văn bản thuần túy.

## Liên kết

- [[WebSocket]]
- [[Multimodal LLM]]
- [[LLM Inference Engineering]]
- [[Real-Time Graph Architecture]]
