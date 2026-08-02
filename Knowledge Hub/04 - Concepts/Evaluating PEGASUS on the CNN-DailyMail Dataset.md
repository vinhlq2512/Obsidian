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

# Evaluating PEGASUS on the CNN-DailyMail Dataset

## Định nghĩa

Evaluating PEGASUS on the CNN/DailyMail Dataset là workflow dùng [[PEGASUS]] để sinh summary cho các bài báo trong CNN/DailyMail, rồi so sánh output với reference highlights bằng metric như [[ROUGE]] và đọc mẫu thủ công.

## Cách hiểu bằng lời của tôi

CNN/DailyMail cho mình một bài báo dài và bản tóm tắt tham chiếu. PEGASUS sinh summary từ `article`; evaluation so output đó với `highlights`.

Điểm quan trọng: đây không phải chỉ là chạy model rồi lấy một con số. Mình cần biết model có vượt [[Summarization Baseline|baseline]] không, và summary có thật sự giữ ý chính, đúng facts, mạch lạc không.

## Dữ liệu đầu vào

Trong note đọc ngày 30/07, dataset được ghi theo cấu trúc:

- `article`: văn bản nguồn cần tóm tắt.
- `highlights`: reference summary dùng để train/evaluate.
- `id`: định danh sample.

## Quy trình đánh giá

```text
CNN/DailyMail article
-> tokenizer
-> PEGASUS generate summary
-> compare with highlights
-> compute ROUGE
-> compare with baseline
-> inspect sample summaries manually
```

## Cần biết

- [[PEGASUS]] là model abstractive summarization, nên output có thể dùng câu mới chứ không chỉ copy câu từ bài báo.
- [[ROUGE]] đo overlap với `highlights`, hữu ích để so sánh nhanh nhiều model hoặc checkpoint.
- ROUGE cao không đảm bảo summary đúng facts; cần [[Measuring the Quality of Generated Text]].
- Nên dùng cùng tập validation/test, cùng generation settings và cùng metric để so sánh công bằng.
- Không nên ghi kết luận như "PEGASUS tốt hơn" nếu chưa có baseline hoặc sample review.

## Những điều cần soi khi đọc output

- Summary có giữ các ý chính trong `article` không?
- Summary có thêm facts không có trong bài báo không?
- Summary có quá dài, quá ngắn hoặc lặp không?
- Summary có giống `highlights` theo ROUGE nhưng đọc kém không?
- Summary có vượt baseline đơn giản hoặc pretrained pipeline baseline không?

## Khi áp dụng

- Khi muốn đánh giá model summarization pretrained hoặc fine-tuned.
- Khi chọn checkpoint PEGASUS tốt nhất sau training.
- Khi muốn hiểu ROUGE score có phản ánh chất lượng summary thật không.
- Khi xây workflow [[Text Summarization Pipelines|summarization pipeline]] có bước evaluation rõ ràng.

## Câu hỏi review

1. CNN/DailyMail cung cấp những field nào cho summarization?
2. Vì sao evaluation PEGASUS không nên chỉ nhìn ROUGE?
3. Cần giữ điều gì cố định để so sánh nhiều model/checkpoint công bằng?

## Gợi ý trả lời câu hỏi review

1. `article` là input source, `highlights` là reference summary, `id` là định danh sample.
2. Vì ROUGE chỉ đo overlap với reference, không đảm bảo factuality, coverage, coherence hoặc task fit.
3. Cùng dataset split, generation settings, metric implementation và baseline so sánh.

## Liên kết

- [[NLP Transformers - Chapter 06 - Summarization]]
- [[PEGASUS]]
- [[Text Summarization Pipelines]]
- [[Summarization Baseline]]
- [[Measuring the Quality of Generated Text]]
- [[Comparing Different Summaries]]
- [[ROUGE]]
- [[Abstractive Summarization]]
