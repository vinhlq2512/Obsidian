---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 07 - Question Answering]]"
source_sections:
  - "[[NLP Transformers - Chapter 07 - Question Answering]]"
first_seen: 2026-08-01
last_updated: 2026-08-02
created_at: 2026-08-02
updated_at: 2026-08-02
tags:
  - concept
  - nlp
  - question-answering
  - tokenization
---

# Tokenizing Text for QA

## Định nghĩa

Tokenizing text for QA là bước mã hóa cặp `(question, context)` thành input mà model extractive QA có thể xử lý.

## Cách hiểu bằng lời của tôi

Với QA, tokenizer không chỉ encode một câu đơn. Nó phải encode câu hỏi và context cùng lúc, giữ ranh giới giữa hai phần, và giữ metadata để sau này map answer span về text gốc.

```text
question + context
-> [CLS] question [SEP] context [SEP]
-> input_ids + token_type_ids + attention_mask + offsets
```

## Phần cần biết

- `input_ids` là token IDs đưa vào model.
- `token_type_ids` giúp phân biệt phần question và phần context khi model/tokenizer hỗ trợ.
- `attention_mask` cho biết token nào là thật và token nào là padding.
- Offset mapping giúp nối token prediction với vị trí ký tự trong text gốc.
- Với [[Extractive QA]], output start/end token chỉ hữu ích nếu ta biết token đó thuộc context nào.

## Khi áp dụng

- Dùng trước [[Span Classification]] và [[Extracting Answers from Text]].
- Cần đặc biệt cẩn thận khi context dài, vì truncation có thể làm mất answer.
- Khi debug QA, nên kiểm tra decoded tokens, ranh giới question/context và offset mapping.

## Câu hỏi review

1. Vì sao QA tokenizer cần nhận cả question và context?
2. `token_type_ids` giúp gì trong QA?
3. Vì sao offset mapping quan trọng khi extract answer?

## Gợi ý trả lời câu hỏi review

1. Vì model phải hiểu câu hỏi trong quan hệ với context để chọn answer span.
2. Nó giúp model biết token nào thuộc question và token nào thuộc context.
3. Vì model dự đoán vị trí token, còn output cuối cùng cần cắt đúng chuỗi answer từ text gốc.

## Liên kết

- [[NLP Transformers - Chapter 07 - Question Answering]]
- [[Question Answering]]
- [[Tokenizer Pipeline]]
- [[Extractive QA]]
- [[Span Classification]]
- [[Extracting Answers from Text]]
- [[Sliding Window for QA]]
