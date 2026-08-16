---
type: concept
status: seed
sources:
  - "[[Hands-On LLM - Chapter 09 - Multimodal Large Language Models]]"
  - "[[2025-12-22_multimodal-llms-basics-how-llms-process-text-images-audio-vi]]"
  - "[[2025-12-29_openai-clip-the-model-that-learnt-zero-shot-image-recognitio]]"
  - "[[2026-05-20_how-netflix-is-using-multimodal-ai-to-power-video-search]]"
  - "[[2026-07-07_chatgpt-vs-gemini-vs-claude-how-they-differ]]"
last_updated: 2026-08-16
tags:
  - concept
  - multimodal
  - llm
---

# Multimodal LLM

## Định nghĩa

Multimodal LLM là model hoặc hệ thống language model có thể xử lý nhiều dạng dữ liệu như text, image, audio, video hoặc table.

## Cách hiểu bằng lời của tôi

Model cần biến các modality khác nhau thành representation mà language model có thể hiểu hoặc kết nối chúng trong cùng embedding space.

## Cần biết

- CLIP học shared space giữa text và image.
- Vision Transformer chia ảnh thành patches như token.
- Multimodal chat nối visual input với text generation.
- Cần cảnh giác hallucination khi model mô tả ảnh hoặc tài liệu.
- Modality-specific encoders biến ảnh/audio/video thành representation ban đầu.
- Projection layer căn chỉnh representation của từng modality vào không gian mà language model dùng được.
- Audio thường được biến thành spectrogram rồi xử lý gần giống ảnh.
- Training thường có hai pha: feature alignment trước, visual instruction tuning sau.

## Từ ByteByteGo

ByteByteGo mô tả nguyên lý chung của multimodal LLM là đưa nhiều loại dữ liệu về một ngôn ngữ toán học chung: embedding vectors. Text token, image patch và audio segment đều trở thành chuỗi vector để backbone Transformer xử lý. Vì vậy điểm khó không chỉ là "đọc ảnh", mà là căn chỉnh modality-specific encoder với language model bằng projection layer và dữ liệu instruction phù hợp.

Trong so sánh ChatGPT, Gemini và Claude, ByteByteGo tách hai hướng multimodal: ghép encoder/projection vào text model theo pipeline tuần tự, hoặc huấn luyện model native multimodal ngay từ đầu trên nhiều modality. Case Netflix video search cũng nhắc một trade-off thực dụng: ensemble nhiều model chuyên biệt dễ kiểm soát hơn cho production search, nhưng một foundation model thống nhất có thể giảm fragmentation nếu giải được latency và quality.

## Liên kết

- [[Embedding]]
- [[Contrastive Learning]]
- [[Generative Model]]
- [[Transformer]]
- [[Self-Attention]]
- [[Instruction Fine-Tuning]]
- [[Multimodal Search]]
- [[LLM Architecture Comparison]]
