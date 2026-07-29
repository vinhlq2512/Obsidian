---
type: concept
status: seed
source:
  - "[[NLP Transformers - Chapter 01 - Hello Transformers]]"
tags:
  - concept
  - hugging-face
  - nlp
  - transformers
---

# Hugging Face

## Định nghĩa

Hugging Face là hệ sinh thái công cụ và cộng đồng để chia sẻ, tải, chạy, fine-tune và triển khai model machine learning, đặc biệt là Transformer cho NLP.

## Cách hiểu bằng lời của tôi

Hugging Face làm giảm ma sát khi thử nghiệm NLP: có thể tìm pretrained model trên Hub, chạy nhanh bằng `pipeline()`, xử lý tokenizer/model bằng Transformers, dùng Datasets để quản lý dữ liệu, và dùng Accelerate để chạy training trên phần cứng khác nhau.

## Cần biết

- Hub lưu model, dataset, demo và model cards.
- Transformers cung cấp API cho tokenizer, model, pipeline, inference và training.
- Datasets hỗ trợ tải, biến đổi và chia sẻ dataset.
- Tokenizers cung cấp tokenizer nhanh cho các mô hình NLP.
- Accelerate hỗ trợ training/inference trên CPU, GPU, multi-GPU hoặc distributed setup.

## Liên kết

- [[Transformer]]
- [[Tokenization]]
- [[Transfer Learning]]
- [[NLP Transformers - Chapter 01 - Hello Transformers]]
