---
type: reading-section
book: "[[Natural Language Processing with Transformers]]"
status: completed
chapter: 6
start_page: 164
end_page: 194
reading_date: 2026-07-30
planned_sessions:
  - "2026-07-30 | 164-179 | Abstractive summarization, baseline và metric | 50 phút"
  - "2026-07-31 | 180-194 | Fine-tuning summarization và viết lại quy trình | 50 phút"
estimated_minutes: 75
actual_minutes:
need_review: false
completed_at: 2026-07-31
tags:
  - nlp
  - summarization
  - evaluation
---

# NLP Transformers - Chapter 06 - Summarization

## Mục tiêu đọc

- Hiểu abstractive summarization và các baseline.
- Biết so sánh summary bằng BLEU và ROUGE.
- Nắm workflow fine-tune model summarization như PEGASUS.

## Ý chính

- Summary tốt không chỉ ngắn mà còn phải giữ thông tin cốt lõi.
- [[Text Summarization Pipelines]] nối input document, tokenizer, summarization model, decoding strategy và evaluation thành một workflow hoàn chỉnh.
- [[Training a Summarization Model]] khác inference ở chỗ cần tokenize cả source text và target summary để model học sinh output mong muốn.
- [[Summarization Baseline]] là vạch sàn để biết model/pipeline mới có thật sự tốt hơn cách đơn giản, rẻ và ổn định không.
- [[Measuring the Quality of Generated Text]] là lớp đánh giá rộng hơn: metric tự động chỉ là tín hiệu, còn chất lượng thật cần đúng ý, đúng facts, mạch lạc và hợp task.
- [[Comparing Different Summaries]] cần kết hợp metric tự động với đọc thủ công để kiểm tra coverage, factuality và coherence.
- [[Evaluating PEGASUS on the CNN-DailyMail Dataset]] nối phần dataset `article/highlights/id`, model PEGASUS, ROUGE và sample review thành một evaluation workflow cụ thể.
- BLEU thường dùng cho translation, ROUGE phổ biến hơn cho summarization.
- Fine-tuning trên domain cụ thể giúp summary sát ngữ cảnh hơn.

## Demo thực hành

Tóm tắt một đoạn dài và đánh giá nhanh bằng ROUGE.

```python
from transformers import pipeline

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

article = """
Transformers have become a standard architecture for natural language processing.
They are used for classification, question answering, summarization, translation,
and text generation. The Hugging Face ecosystem provides tools that make it easier
to load datasets, tokenize text, fine-tune models, and share trained models.
"""

summary = summarizer(article, max_length=45, min_length=15, do_sample=False)
print(summary[0]["summary_text"])
```

## Khái niệm quan trọng

- [[Text Summarization Pipelines]]
- [[Training a Summarization Model]]
- [[Summarization Baseline]]
- [[Measuring the Quality of Generated Text]]
- [[Comparing Different Summaries]]
- [[Evaluating PEGASUS on the CNN-DailyMail Dataset]]
- [[Summarization]]
- [[Abstractive Summarization]]
- [[BLEU]]
- [[ROUGE]]
- [[PEGASUS]]

## Active Recall

1. Extractive và abstractive summarization khác nhau thế nào?
2. ROUGE đo điều gì?
3. Vì sao metric tự động không đủ để đánh giá summary?
4. Khi fine-tune summarizer cần chú ý gì về input length?
5. Khi so sánh nhiều summary, vì sao không nên chọn chỉ theo ROUGE?
6. Generated text cần được đánh giá theo những chiều chất lượng nào ngoài overlap metric?
7. Khi đánh giá PEGASUS trên CNN/DailyMail, `article` và `highlights` đóng vai trò gì?
8. Vì sao training summarization cần tokenize target summary thành labels?

## Gợi ý trả lời câu hỏi review

1. Extractive summarization lấy câu/cụm có sẵn từ source; [[Abstractive Summarization]] sinh câu mới để diễn đạt lại ý chính. Abstractive thường tự nhiên hơn nhưng cần kiểm tra hallucination kỹ hơn.
2. [[ROUGE]] đo mức overlap giữa generated summary và reference summary, thường theo n-gram hoặc chuỗi con chung. Nó hữu ích để so sánh nhanh nhưng không đảm bảo summary đúng facts.
3. Metric tự động không đủ vì generated text có nhiều đáp án đúng. Một summary có thể ROUGE cao nhưng sai facts, hoặc ROUGE thấp vì paraphrase nhưng vẫn đúng ý và hữu ích.
4. Cần chú ý giới hạn input length của model. Nếu source bị truncate mất phần quan trọng, model có thể tạo summary thiếu ý dù training/evaluation nhìn vẫn chạy bình thường.
5. Vì [[Comparing Different Summaries]] cần nhìn thêm coverage, factuality, coherence, conciseness và task fit. Chọn chỉ theo ROUGE dễ bỏ qua summary đọc kém hoặc hallucinate.
6. Ngoài overlap metric, cần đánh giá correctness, coverage, factuality, fluency, coherence, conciseness và mức phù hợp với mục tiêu thật của người dùng.
7. Trong CNN/DailyMail, `article` là văn bản nguồn đưa vào model, còn `highlights` là reference summary dùng để train hoặc evaluate output của [[PEGASUS]].
8. Vì summarization là seq2seq: decoder cần học sinh chuỗi summary mục tiêu, nên target summary phải được tokenize thành labels để tính loss trong training.

## Tổng kết sau khi đọc

- Chapter 06 có ba lớp chính: tạo summary bằng pipeline, đánh giá generated text, và fine-tune summarization model cho domain cụ thể.
- [[Text Summarization Pipelines]] cho thấy model chỉ là một phần của workflow; tokenizer, decoding parameters, baseline và metric đều ảnh hưởng output.
- [[Training a Summarization Model]] cần source text cho encoder và target summary làm labels cho decoder.
- [[ROUGE]] hữu ích để so sánh nhanh nhưng phải đi cùng [[Comparing Different Summaries]] và human review.
- Khi dùng [[PEGASUS]], cần đánh giá trên dataset rõ ràng như CNN/DailyMail, so với [[Summarization Baseline|baseline]], rồi đọc sample để tìm lỗi factuality/coverage.

## Checklist

- [x] Đọc xong chapter
- [ ] Chạy demo summarization
- [ ] So sánh summary với bản tự viết
- [x] Tách concept cần dùng lại
- [x] Cập nhật tiến độ sách
