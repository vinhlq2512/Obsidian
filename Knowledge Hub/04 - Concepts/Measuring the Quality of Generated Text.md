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
  - text-generation
  - evaluation
---

# Measuring the Quality of Generated Text

## Định nghĩa

Measuring the quality of generated text là quá trình đánh giá output do model sinh ra bằng metric tự động, so sánh với baseline/reference, và kiểm tra thủ công các yếu tố mà metric không thấy hết.

## Cách hiểu bằng lời của tôi

Generated text không có một đáp án duy nhất. Cùng một input có thể có nhiều output đúng, nên chất lượng không thể đo như bài toán classification đơn giản.

Mình cần nhìn theo hai lớp:

```text
automatic metrics -> so sánh nhanh, nhất quán, rẻ
human review -> kiểm tra đúng ý, đúng facts, mạch lạc, phù hợp mục tiêu
```

Metric giúp sàng lọc, nhưng quyết định cuối cùng vẫn phải quay lại câu hỏi: output này có dùng được cho task thật không?

## Những chiều chất lượng quan trọng

- **Correctness**: output có đúng với source hoặc yêu cầu không?
- **Coverage**: output có giữ đủ ý quan trọng không?
- **Factuality**: output có thêm thông tin sai hoặc không có trong source không?
- **Fluency**: câu chữ có tự nhiên, dễ đọc không?
- **Coherence**: các ý có nối với nhau mạch lạc không?
- **Conciseness**: output có gọn mà không mất nội dung chính không?
- **Task fit**: output có phù hợp mục tiêu thật của người dùng không?

## Metric trong summarization

- [[ROUGE]] thường dùng cho [[Summarization]] vì đo overlap giữa generated summary và reference summary.
- [[BLEU]] thiên về n-gram precision, phổ biến hơn trong translation và cần cẩn trọng khi dùng cho summarization.
- Metric overlap hữu ích để so sánh nhanh nhiều model/checkpoint, nhưng không đảm bảo factuality hoặc readability.
- Với summarization, nên kết hợp metric với [[Comparing Different Summaries]] và [[Summarization Baseline]].

## Quy trình đánh giá

```text
input
-> generated text
-> reference / expected behavior
-> metric score
-> compare with baseline
-> inspect samples manually
-> identify failure mode
```

## Failure mode cần soi

- Output giống reference về từ ngữ nhưng sai hoặc thiếu ý.
- Output đúng ý nhưng dùng cách diễn đạt khác nên metric thấp.
- Output trôi chảy nhưng hallucinate facts.
- Output quá dài, quá ngắn, hoặc lặp.
- Metric tổng tốt nhưng một nhóm sample cụ thể rất kém.

## Khi áp dụng

- Khi đánh giá summarization, translation, text generation hoặc QA dạng sinh text.
- Khi chọn model/checkpoint sau fine-tuning.
- Khi debug vì sao metric tăng nhưng người đọc thấy output tệ hơn.
- Khi cần quyết định model mới có vượt baseline đủ rõ để triển khai không.

## Câu hỏi review

1. Vì sao generated text khó đánh giá hơn classification?
2. Metric tự động giúp gì và thiếu gì?
3. Khi nào nên tin human review hơn metric?

## Gợi ý trả lời câu hỏi review

1. Vì một input có thể có nhiều output đúng, cách diễn đạt khác nhau và chất lượng phụ thuộc vào mục tiêu sử dụng.
2. Metric giúp so sánh nhanh, rẻ và nhất quán, nhưng thường không kiểm tra đủ factuality, coherence hoặc task fit.
3. Khi metric cao nhưng output sai facts/khó dùng, hoặc metric thấp do paraphrase nhưng summary vẫn đúng và phù hợp mục tiêu.

## Liên kết

- [[NLP Transformers - Chapter 06 - Summarization]]
- [[Summarization]]
- [[Text Generation]]
- [[Comparing Different Summaries]]
- [[Summarization Baseline]]
- [[ROUGE]]
- [[BLEU]]
