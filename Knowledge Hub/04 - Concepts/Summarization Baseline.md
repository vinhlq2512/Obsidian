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
  - evaluation
---

# Summarization Baseline

## Định nghĩa

Summarization baseline là điểm so sánh đơn giản, rẻ và ổn định để biết một hệ thống [[Summarization|summarization]] mạnh hơn có thật sự tạo ra cải thiện có ý nghĩa hay không.

## Cách hiểu bằng lời của tôi

Baseline là "vạch sàn" của bài toán. Trước khi tin một model lớn hoặc fine-tuning phức tạp, mình cần hỏi: nó có tốt hơn cách đơn giản nhất chưa, và tốt hơn ở điểm nào?

Trong summarization, baseline không nhất thiết phải hay. Nó cần đủ dễ hiểu để mình biết model đang thắng vì học được cách tóm tắt, hay chỉ đang tạo output nghe có vẻ trôi chảy.

## Các baseline thường gặp

- **Pretrained pipeline baseline**: dùng sẵn một [[Text Summarization Pipelines|summarization pipeline]] để tạo summary nhanh, chưa fine-tune cho domain riêng.
- **Deterministic decoding baseline**: đặt `do_sample=False` để output ổn định hơn khi so sánh nhiều lần.
- **Extractive baseline đơn giản**: lấy những câu đầu hoặc câu nổi bật trong document làm bản tóm tắt tham chiếu đơn giản.
- **Human/reference summary**: dùng reference summary để tính metric, nhưng vẫn cần đọc thủ công vì reference cũng chỉ là một cách tóm tắt.

## Vai trò trong workflow

```text
source document
-> baseline summary
-> model summary
-> metric comparison
-> human review
-> decide whether to fine-tune or adjust pipeline
```

## Cần biết

- Baseline giúp tránh nhầm "model lớn hơn" với "model tốt hơn cho task".
- [[ROUGE]] thường dùng để so sánh nhanh summary với reference summary.
- [[BLEU]] có thể dùng để hiểu overlap kiểu n-gram precision, nhưng không phải metric chính cho summarization.
- Metric tự động chỉ là tín hiệu ban đầu; vẫn phải kiểm tra factuality, coverage và readability.
- Nếu model fine-tuned không vượt baseline rõ ràng, cần kiểm tra dữ liệu, decoding parameters, input truncation hoặc metric.

## Khi áp dụng

- Khi thử nhanh một pretrained summarization model.
- Trước khi fine-tune [[PEGASUS]] hoặc model encoder-decoder khác cho domain cụ thể.
- Khi so sánh nhiều decoding strategy hoặc checkpoint.
- Khi muốn biết pipeline hiện tại có tạo summary tốt hơn cách đơn giản không.

## Câu hỏi review

1. Vì sao cần baseline trước khi fine-tune summarization model?
2. Baseline tốt cần mạnh nhất hay dễ hiểu nhất?
3. Vì sao ROUGE cao chưa chắc summary tốt?

## Gợi ý trả lời câu hỏi review

1. Vì baseline cho biết mức tối thiểu cần vượt qua; nếu model phức tạp không hơn baseline, workflow chưa đáng tin.
2. Baseline cần rẻ, ổn định và dễ diễn giải trước; không nhất thiết phải là model mạnh nhất.
3. Vì ROUGE đo overlap với reference, không đảm bảo summary đúng facts, đủ ý hoặc mạch lạc.

## Liên kết

- [[NLP Transformers - Chapter 06 - Summarization]]
- [[Summarization]]
- [[Text Summarization Pipelines]]
- [[Abstractive Summarization]]
- [[ROUGE]]
- [[BLEU]]
- [[PEGASUS]]
