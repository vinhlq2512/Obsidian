---
type: reading-section
book: "[[Hands-On Large Language Models]]"
status: not-started
chapter: 9
start_page: 360
end_page: 395
estimated_minutes: 85
need_review: true
tags:
  - llm
  - multimodal
---

# Hands-On LLM - Chapter 09 - Multimodal Large Language Models

## Mục tiêu cần hiểu

- Hiểu [[Multimodal LLM]] xử lý nhiều modality như text và image.
- Nắm cách Transformer được áp dụng cho vision.
- Biết CLIP học shared embedding space giữa text và image.
- Hiểu BLIP-2 nối vision encoder với language model để làm image captioning và multimodal chat.
- Nắm preprocessing multimodal inputs trước khi đưa vào model.

## Định nghĩa quan trọng

- **Modality**: dạng dữ liệu như text, image, audio, video, table.
- **Multimodal embedding**: embedding cho nhiều modality trong cùng không gian so sánh.
- **CLIP**: model học liên kết text-image bằng contrastive learning.
- **Vision Transformer**: áp dụng Transformer cho image bằng cách chia ảnh thành patches.
- **BLIP-2**: kiến trúc nối image representation với LLM để sinh text dựa trên ảnh.

## Mental model

Multimodal model cần một cây cầu giữa các dạng dữ liệu. CLIP tạo cầu bằng shared embedding space. BLIP-2 tạo cầu bằng module chuyển representation hình ảnh sang dạng language model có thể dùng để sinh text.

## Phần cần biết

- Image có thể được biến thành sequence patch embeddings giống token sequence.
- CLIP mạnh cho retrieval, zero-shot image classification và image-text matching.
- Multimodal generation cần căn chỉnh vision features với text generation model.
- Multimodal chat cần xử lý cả prompt text lẫn image input.

## Khi áp dụng

- Dùng CLIP/OpenCLIP cho search ảnh bằng text hoặc tìm caption phù hợp.
- Dùng vision-language model cho captioning, VQA, phân tích ảnh, tài liệu và UI.
- Cẩn thận với hallucination: model có thể mô tả chi tiết không có trong ảnh.

## Câu hỏi review

1. Shared embedding space nghĩa là gì?
2. CLIP học liên kết text-image bằng cách nào?
3. Vision Transformer biến ảnh thành input sequence ra sao?
4. BLIP-2 giải quyết khoảng cách giữa vision và language model như thế nào?

## Gợi ý trả lời câu hỏi review

1. Shared embedding space là không gian vector chung nơi text và image có thể được so sánh trực tiếp. Caption và ảnh tương ứng nên nằm gần nhau, còn cặp không liên quan nên xa nhau.
2. CLIP học bằng contrastive learning trên cặp image-caption: kéo embedding của ảnh và caption đúng lại gần, đẩy các cặp sai ra xa trong batch.
3. Vision Transformer chia ảnh thành các patches, biến mỗi patch thành embedding giống token, thêm positional information rồi xử lý chuỗi patch embeddings bằng Transformer.
4. BLIP-2 dùng một thành phần trung gian để nối visual encoder với language model, chuyển thông tin hình ảnh thành representation mà LLM có thể dùng để sinh caption hoặc trả lời câu hỏi về ảnh.

## Liên kết

- [[Multimodal LLM]]
- [[Embedding]]
- [[Contrastive Learning]]
- [[Transformer]]
