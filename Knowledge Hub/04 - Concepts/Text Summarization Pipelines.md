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
  - pipeline
---

# Text Summarization Pipelines

## Định nghĩa

Text summarization pipeline là workflow dùng model NLP để rút gọn văn bản dài thành bản tóm tắt ngắn hơn, thường bằng Hugging Face `pipeline("summarization")` hoặc một pipeline fine-tuning đầy đủ cho domain cụ thể.

## Cách hiểu bằng lời của tôi

Pipeline summarization không chỉ là "gọi model tóm tắt". Nó gồm nhiều quyết định nối nhau: chọn input, tokenizer, model encoder-decoder, decoding strategy, độ dài summary, rồi đánh giá summary bằng metric và đọc lại thủ công.

Mental model:

```text
article/document
-> tokenizer
-> summarization model
-> decoding/generation
-> summary text
-> [[Comparing Different Summaries|evaluate with ROUGE + human review]]
```

## Hai mức pipeline

### Pipeline inference nhanh

Dùng khi cần [[Summarization Baseline|baseline]] hoặc thử nhanh một pretrained model.

```python
from transformers import pipeline

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
summary = summarizer(article, max_length=45, min_length=15, do_sample=False)
```

Điểm cần nhớ:

- `article` là văn bản đầu vào.
- `max_length` và `min_length` giới hạn độ dài output.
- `do_sample=False` làm output ổn định hơn, thường phù hợp [[Summarization Baseline|baseline summarization]].
- Model summarization thường thuộc nhóm [[Encoder-Decoder Architecture|encoder-decoder]], vì cần đọc input rồi sinh output mới.

### Pipeline fine-tuning

Dùng khi cần summary sát domain hơn, ví dụ dialogue summarization hoặc tài liệu chuyên ngành. Phần này tương ứng với [[Training a Summarization Model]].

```text
dataset article/dialogue + reference summary
-> tokenize input
-> tokenize target summary
-> data collator for seq2seq
-> encoder-decoder model
-> train/fine-tune
-> generate summaries
-> evaluate with ROUGE
-> inspect errors manually
```

Một ví dụ cụ thể là [[Evaluating PEGASUS on the CNN-DailyMail Dataset]]: dùng `article` làm source, `highlights` làm reference summary, rồi đánh giá output của PEGASUS bằng ROUGE và human review.

## Thành phần quan trọng

- **Input document**: văn bản nguồn cần tóm tắt.
- **Reference summary**: bản tóm tắt chuẩn dùng để train/evaluate.
- **Tokenizer**: biến input và target summary thành token IDs.
- **Model**: thường là encoder-decoder như BART, T5 hoặc PEGASUS.
- **Decoding strategy**: quyết định cách sinh summary, liên quan tới [[Decoding Strategies for Text Generation]].
- **Metric**: [[ROUGE]] phổ biến trong summarization vì đo overlap với reference summary.
- **Comparison**: [[Comparing Different Summaries]] giúp so sánh summary theo metric, baseline và đọc thủ công.
- **Human review**: cần đọc lại vì metric tự động không đảm bảo summary đúng, đủ và không hallucinate.

## Vì sao summarization cần đánh giá cẩn thận?

- Summary có thể ngắn và trôi chảy nhưng bỏ sót ý quan trọng.
- Summary có thể giữ nhiều n-gram giống reference nhưng sai trọng tâm.
- Summary có thể thêm thông tin không có trong source.
- [[ROUGE]] hữu ích để so sánh nhanh, nhưng không thay thế kiểm tra factuality và coverage.

## Khi áp dụng

- Tóm tắt bài báo, hội thoại, báo cáo, transcript hoặc tài liệu dài.
- Tạo [[Summarization Baseline|baseline]] nhanh bằng pretrained summarization pipeline.
- Fine-tune khi domain hoặc format summary khác nhiều so với pretrained data.

## Khi không nên dùng máy móc

- Khi tài liệu quá dài vượt context/input length mà chưa có chunking strategy.
- Khi summary cần độ chính xác pháp lý/y tế/tài chính cao nhưng chưa có review.
- Khi reference summary hoặc metric không phản ánh mục tiêu thật của người dùng.

## Câu hỏi review

1. Summarization pipeline gồm những bước nào?
2. Vì sao summarization thường dùng encoder-decoder model?
3. `max_length`, `min_length` và decoding strategy ảnh hưởng summary thế nào?
4. Vì sao ROUGE không đủ để đánh giá summary?

## Gợi ý trả lời câu hỏi review

1. Input document -> tokenizer -> model -> decoding -> summary -> metric/human review.
2. Vì model cần đọc toàn bộ input bằng encoder rồi decoder sinh output tóm tắt mới.
3. Chúng kiểm soát độ dài và cách chọn token, nên ảnh hưởng mức cô đọng, ổn định và tự nhiên của summary.
4. Vì ROUGE chủ yếu đo overlap với reference, không đảm bảo factuality, coverage hoặc tính mạch lạc.

## Liên kết

- [[NLP Transformers - Chapter 06 - Summarization]]
- [[Text Generation]]
- [[Decoding Strategies for Text Generation]]
- [[Training a Summarization Model]]
- [[Summarization Baseline]]
- [[Comparing Different Summaries]]
- [[Evaluating PEGASUS on the CNN-DailyMail Dataset]]
- [[Encoder-Decoder Architecture]]
- [[Cross-Attention]]
- [[ROUGE]]
- [[PEGASUS]]
