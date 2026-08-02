---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 06 - Summarization]]"
source_sections:
  - "[[NLP Transformers - Chapter 06 - Summarization]]"
first_seen: 2026-07-31
last_updated: 2026-08-02
created_at: 2026-08-02
updated_at: 2026-08-02
tags:
  - concept
  - nlp
  - summarization
  - training
---

# Training a Summarization Model

## Định nghĩa

Training a summarization model là workflow fine-tune một model sequence-to-sequence để biến văn bản nguồn thành summary mục tiêu, thường bằng cách dùng cặp `source text -> reference summary`.

## Cách hiểu bằng lời của tôi

Training summarization khác inference ở chỗ model không chỉ sinh summary từ input, mà còn học từ bản tóm tắt chuẩn. Trong lúc train, `article/dialogue` là input cho encoder, còn `summary/highlights` là target để decoder học sinh ra.

Mental model:

```text
source document
-> tokenize source
-> tokenize target summary
-> seq2seq data collator
-> encoder-decoder model
-> train with target labels
-> generate summaries
-> evaluate with ROUGE + human review
```

## Thành phần chính

- **Dataset**: gồm văn bản nguồn và reference summary, ví dụ CNN/DailyMail có `article`, `highlights`, `id`.
- **Tokenizer source**: tokenize văn bản đầu vào, có thể cần truncation nếu input quá dài.
- **Tokenizer target**: tokenize summary mục tiêu để làm labels cho decoder.
- **Data collator for seq2seq**: gom batch và padding phù hợp cho input/labels.
- **Model**: thường là [[Encoder-Decoder Architecture|encoder-decoder]] như [[PEGASUS]], BART hoặc T5.
- **Generation settings**: quyết định cách sinh summary khi evaluate.
- **Metric + review**: dùng [[ROUGE]] để so sánh nhanh, rồi đọc mẫu theo [[Measuring the Quality of Generated Text]].

## Vì sao cần tokenize target riêng?

Với summarization, output cũng là text. Model cần học sinh chuỗi target token theo từng bước, nên summary reference phải được tokenize thành labels.

Nếu chỉ tokenize input mà không chuẩn bị target labels, model không biết output đúng cần học là gì.

## Điểm dễ lỗi

- Input bị cắt mất thông tin quan trọng vì vượt max length.
- Target summary quá dài hoặc format không nhất quán.
- Padding của labels không được xử lý đúng, làm loss tính vào token padding.
- ROUGE tăng nhưng sample summary vẫn sai facts hoặc thiếu ý.
- Fine-tuned model không vượt [[Summarization Baseline|baseline]] rõ ràng.

## Khi áp dụng

- Khi pretrained summarization pipeline chưa đủ sát domain.
- Khi có dataset gồm source document/dialogue và reference summary.
- Khi cần summary theo format riêng, ví dụ dialogue summary, news summary hoặc report summary.
- Khi muốn chọn checkpoint tốt nhất bằng [[Evaluating PEGASUS on the CNN-DailyMail Dataset|evaluation workflow]].

## Câu hỏi review

1. Training summarization khác inference summarization ở điểm nào?
2. Vì sao target summary phải được tokenize thành labels?
3. Những lỗi nào có thể làm model fine-tuned có ROUGE ổn nhưng summary vẫn kém?

## Gợi ý trả lời câu hỏi review

1. Inference chỉ sinh summary từ input; training dùng cả input và reference summary để cập nhật model.
2. Vì decoder học sinh chuỗi output token, nên cần labels từ summary mục tiêu để tính loss.
3. Input bị truncation, target format lệch, metric không phản ánh factuality, hoặc model chỉ học overlap mà không giữ đúng ý.

## Liên kết

- [[NLP Transformers - Chapter 06 - Summarization]]
- [[Text Summarization Pipelines]]
- [[PEGASUS]]
- [[Evaluating PEGASUS on the CNN-DailyMail Dataset]]
- [[Summarization Baseline]]
- [[Measuring the Quality of Generated Text]]
- [[ROUGE]]
- [[Encoder-Decoder Architecture]]
