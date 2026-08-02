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
  - generation
---

# Abstractive Summarization

## Định nghĩa

Abstractive summarization là hướng tóm tắt trong đó model sinh câu mới để diễn đạt lại ý chính của văn bản nguồn, thay vì chỉ trích nguyên câu từ source.

## Cách hiểu bằng lời của tôi

Extractive summarization giống như chọn các câu quan trọng rồi ghép lại. Abstractive summarization giống như đọc hiểu rồi viết lại bằng câu mới. Vì có generation, nó tự nhiên hơn nhưng cũng có rủi ro thêm thông tin sai.

## Cần biết

- Thường dùng [[Encoder-Decoder Architecture|encoder-decoder models]] như BART, T5 hoặc [[PEGASUS]].
- Liên quan trực tiếp tới [[Text Generation]] và [[Decoding Strategies for Text Generation]].
- Cần đánh giá cả coverage, factuality, coherence và độ ngắn gọn.
- [[ROUGE]] đo overlap với reference summary nhưng không đảm bảo summary thật sự đúng.

## Khi áp dụng

- Khi cần summary tự nhiên, không chỉ copy câu nguồn.
- Khi source dài và cần nén ý theo cách dễ đọc.
- Khi có reference summaries để fine-tune/evaluate.

## Liên kết

- [[Summarization]]
- [[Text Summarization Pipelines]]
- [[Text Generation]]
- [[ROUGE]]
- [[PEGASUS]]

