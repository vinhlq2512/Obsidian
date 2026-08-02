---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 06 - Summarization]]"
source_sections:
  - "[[NLP Transformers - Chapter 06 - Summarization]]"
first_seen: 2026-07-30
last_updated: 2026-08-02
created_at: 2026-08-02
updated_at: 2026-08-02
tags:
  - concept
  - nlp
  - summarization
---

# Summarization

## Định nghĩa

Summarization là bài toán rút gọn văn bản dài thành bản tóm tắt ngắn hơn nhưng vẫn giữ các ý chính quan trọng.

## Cách hiểu bằng lời của tôi

Summary tốt không chỉ là văn bản ngắn. Nó phải chọn đúng thông tin đáng giữ, bỏ chi tiết phụ, giữ mạch ý và tránh thêm facts không có trong source.

## Cần biết

- Có hai hướng lớn: extractive và [[Abstractive Summarization]].
- Summarization thường dùng model [[Encoder-Decoder Architecture|encoder-decoder]] vì cần đọc input rồi sinh output mới.
- [[Text Summarization Pipelines]] gồm input, tokenizer, model, decoding strategy và evaluation.
- [[Summarization Baseline]] là điểm so sánh tối thiểu trước khi tin một model hoặc pipeline mới.
- [[ROUGE]] phổ biến hơn [[BLEU]] trong đánh giá summarization, nhưng vẫn cần human review.

## Khi áp dụng

- Tóm tắt bài báo, hội thoại, tài liệu dài, transcript hoặc report.
- Dùng pretrained pipeline để tạo [[Summarization Baseline|baseline]] nhanh.
- Fine-tune khi domain hoặc format summary khác nhiều so với dữ liệu pretraining/fine-tuning sẵn có.

## Liên kết

- [[Text Summarization Pipelines]]
- [[Summarization Baseline]]
- [[Abstractive Summarization]]
- [[ROUGE]]
- [[BLEU]]
- [[PEGASUS]]
- [[NLP Transformers - Chapter 06 - Summarization]]
