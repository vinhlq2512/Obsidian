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
  - evaluation
---

# Comparing Different Summaries

## Định nghĩa

Comparing different summaries là một trường hợp cụ thể của [[Measuring the Quality of Generated Text]]: đánh giá nhiều bản tóm tắt của cùng một input để chọn output tốt hơn, thường bằng cách kết hợp metric tự động như [[ROUGE]] với đọc thủ công.

## Cách hiểu bằng lời của tôi

So sánh summary không chỉ là hỏi "summary nào giống reference hơn?". Mình cần hỏi summary nào giữ đúng ý chính, ít bịa hơn, đọc mạch lạc hơn, và phù hợp mục tiêu người dùng hơn.

Metric cho mình tín hiệu nhanh, còn đọc thủ công cho mình biết summary có thật sự dùng được không.

## Quy trình so sánh

```text
source document
-> reference summary
-> summary A / summary B / baseline summary
-> compute ROUGE or another metric
-> inspect coverage, factuality, coherence
-> decide which summary is better for the actual task
```

## Các tiêu chí cần nhìn

- **Coverage**: summary có giữ các ý quan trọng của source không?
- **Factuality**: summary có thêm thông tin không có trong source không?
- **Coherence**: summary có đọc mạch lạc không?
- **Conciseness**: summary có ngắn gọn mà không mất ý chính không?
- **Metric overlap**: summary có overlap hợp lý với reference theo [[ROUGE]] không?
- **Baseline comparison**: summary có vượt [[Summarization Baseline|baseline]] rõ ràng không?
- **Task fit**: summary có phù hợp mục tiêu sử dụng thật không?

## Vì sao không chỉ dùng ROUGE?

[[ROUGE]] đo overlap với reference summary. Nó hữu ích khi cần so sánh nhiều model hoặc checkpoint nhanh, nhưng có thể bỏ lỡ các trường hợp:

- summary đúng ý nhưng dùng từ khác reference;
- summary overlap cao nhưng lặp, thiếu mạch hoặc sai facts;
- reference summary chỉ là một cách tóm tắt, không phải đáp án duy nhất;
- metric không phản ánh mục tiêu thật của người đọc.

## Khi áp dụng

- Khi so sánh output của nhiều [[Text Summarization Pipelines|summarization pipelines]].
- Khi chọn checkpoint tốt nhất sau fine-tuning.
- Khi quyết định model mới có đáng thay baseline không.
- Khi debug vì sao summary đọc ổn nhưng metric thấp, hoặc metric cao nhưng summary kém.

## Câu hỏi review

1. Vì sao so sánh summaries cần cả metric lẫn human review?
2. ROUGE giúp gì và thiếu gì khi so sánh summaries?
3. Nếu summary A ROUGE cao hơn nhưng bịa facts, còn summary B ROUGE thấp hơn nhưng đúng ý, nên phân tích thế nào?

## Gợi ý trả lời câu hỏi review

1. Metric giúp so sánh nhanh và nhất quán, human review kiểm tra chất lượng thật như đúng facts, đủ ý và mạch lạc.
2. ROUGE đo overlap với reference, nhưng không đảm bảo factuality, coherence hoặc đúng mục tiêu người đọc.
3. Không chọn chỉ theo điểm số; cần ghi rõ trade-off: A gần reference hơn về n-gram nhưng kém factuality, B có thể dùng được hơn nếu mục tiêu là summary đáng tin.

## Liên kết

- [[NLP Transformers - Chapter 06 - Summarization]]
- [[Measuring the Quality of Generated Text]]
- [[Summarization]]
- [[Text Summarization Pipelines]]
- [[Summarization Baseline]]
- [[ROUGE]]
- [[BLEU]]
- [[Abstractive Summarization]]
