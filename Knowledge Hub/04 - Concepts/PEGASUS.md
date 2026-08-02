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
  - transformer
---

# PEGASUS

## Định nghĩa

PEGASUS là một Transformer model family dùng cho abstractive summarization.

## Cách hiểu bằng lời của tôi

Trong Chapter 06, PEGASUS là model đại diện cho workflow fine-tune summarization: dùng pretrained seq2seq model, chuẩn bị input và target summaries, rồi fine-tune cho domain cụ thể.

## Cần biết

- PEGASUS thuộc nhóm model phù hợp với [[Abstractive Summarization]].
- [[Training a Summarization Model]] với PEGASUS cần tokenizer cho source text và target summary.
- [[Evaluating PEGASUS on the CNN-DailyMail Dataset]] là ví dụ cụ thể: dùng `article` làm input, `highlights` làm reference summary, sinh output rồi đánh giá bằng [[ROUGE]] và đọc mẫu.
- Domain cụ thể ảnh hưởng chất lượng summary, nên fine-tuning có thể giúp output sát ngữ cảnh hơn.

## Khi áp dụng

- Khi cần model summarization chuyên cho domain/task cụ thể.
- Khi có dataset gồm source document/dialogue và reference summary.

## Liên kết

- [[Summarization]]
- [[Abstractive Summarization]]
- [[Text Summarization Pipelines]]
- [[Training a Summarization Model]]
- [[Evaluating PEGASUS on the CNN-DailyMail Dataset]]
- [[ROUGE]]
- [[NLP Transformers - Chapter 06 - Summarization]]
