---
type: reading-section
book: "[[Natural Language Processing with Transformers]]"
status: completed
chapter: 1
start_page: 21
end_page: 38
reading_date: 2026-07-23
planned_sessions:
  - "2026-07-23 | 21-38 | Tổng quan Transformer, Hugging Face và pipeline | 45 phút"
estimated_minutes: 45
actual_minutes: 45
need_review: false
tags:
  - nlp
  - transformers
  - hugging-face
---

# NLP Transformers - Chapter 01 - Hello Transformers

## Mục tiêu cần hiểu

- Hiểu Transformer giải quyết vấn đề gì trong NLP.
- Nắm khung encoder-decoder, attention, transfer learning.
- Biết hệ sinh thái Hugging Face gồm Hub, Transformers, Tokenizers, Datasets, Accelerate.

## Ý chính

- Transformer thay đổi NLP nhờ attention và khả năng transfer learning tốt.
- Hugging Face cung cấp công cụ cấp cao để dùng model có sẵn và fine-tune model.
- Một model có thể được áp dụng cho nhiều task như classification, NER, QA, summarization, translation, generation.
- Pipeline là cách chạy nhanh một tác vụ NLP bằng pretrained model mà chưa cần viết toàn bộ bước tiền xử lý, suy luận và hậu xử lý.
- Transfer learning giúp tận dụng model đã học từ corpus lớn, sau đó điều chỉnh cho downstream task cụ thể.

## Mental model

Thay vì huấn luyện một model NLP từ đầu cho từng bài toán, workflow hiện đại bắt đầu bằng pretrained Transformer. Mình dùng `pipeline()` để kiểm tra nhanh năng lực có sẵn, sau đó quyết định có cần fine-tune bằng dữ liệu riêng hay không.

Transformer có thể xem như một bộ máy tạo biểu diễn theo ngữ cảnh: mỗi token không được hiểu riêng lẻ, mà được cập nhật dựa trên các token liên quan trong cùng sequence thông qua attention. Vì vậy model xử lý tốt hơn các quan hệ xa trong câu so với cách đọc tuần tự kiểu RNN.

## Phần cần biết

- Encoder phù hợp với bài toán hiểu văn bản như classification hoặc NER.
- Decoder phù hợp với sinh văn bản từng token một.
- Encoder-decoder phù hợp với sequence-to-sequence như translation, summarization hoặc question answering dạng sinh.
- Pretraining tạo nền tảng tri thức ngôn ngữ chung; fine-tuning biến nền tảng đó thành năng lực cho task cụ thể.
- Hugging Face Hub lưu model, dataset và demo; thư viện Transformers cung cấp API để tải, chạy và fine-tune model.
- Các rủi ro khi dùng Transformer gồm chi phí tính toán, bias trong dữ liệu, giới hạn context, và khó diễn giải quyết định của model.

## Demo thực hành

Chạy thử nhiều pipeline để thấy cùng một API có thể xử lý nhiều task.

```python
from transformers import pipeline

sentiment = pipeline("sentiment-analysis")
ner = pipeline("ner", aggregation_strategy="simple")
summarizer = pipeline("summarization")

text = "Hugging Face is building useful tools for the NLP community in New York."

print(sentiment(text))
print(ner(text))
print(summarizer(
    "Transformers are neural network architectures based on attention. "
    "They power many modern NLP systems and can be fine-tuned for downstream tasks.",
    max_length=30,
    min_length=10,
))
```

## Khi áp dụng

- Dùng `pipeline()` khi cần thử nhanh một task phổ biến hoặc tạo baseline ban đầu.
- Dùng pretrained checkpoint khi bài toán có ít dữ liệu hoặc không đủ tài nguyên để train từ đầu.
- Fine-tune khi output của model có sẵn chưa bám sát domain, nhãn hoặc format cần dùng.
- Ưu tiên kiểm tra dataset, metric và lỗi mẫu trước khi tối ưu kiến trúc model.

## Định nghĩa quan trọng

- [[Transformer]]
- [[Self-Attention]]
- [[Transfer Learning]]
- [[Hugging Face]]

## Câu hỏi review

1. Encoder-decoder framework giải quyết bài toán gì?
2. Vì sao attention quan trọng hơn cách xử lý tuần tự truyền thống?
3. Hugging Face Hub khác gì thư viện Transformers?
4. Những thách thức chính khi dùng Transformer là gì?

## Gợi ý trả lời câu hỏi review

1. Encoder-decoder framework tách quá trình hiểu input và sinh output. Encoder biến input thành biểu diễn giàu ngữ cảnh, decoder dùng biểu diễn đó để tạo sequence đầu ra.
2. Attention cho phép model truy cập trực tiếp các token liên quan ở xa, thay vì ép mọi thông tin đi qua chuỗi hidden state tuần tự. Điều này giúp học quan hệ dài tốt hơn và huấn luyện song song hiệu quả hơn.
3. Hugging Face Hub là nơi chia sẻ model, dataset và artifacts; Transformers là thư viện Python để tải tokenizer/model, chạy inference, fine-tune và tích hợp vào workflow.
4. Các thách thức chính gồm chi phí compute, dữ liệu có bias, giới hạn độ dài context, model khó giải thích, và rủi ro dùng pretrained model không phù hợp domain.

## Liên kết

- Book: [[Natural Language Processing with Transformers]]
- Section tiếp theo: [[NLP Transformers - Chapter 02 - Text Classification]]
- Reading log: [[23-07-2026]]

## Checklist

- [x] Đọc xong chapter
- [x] Viết tóm tắt bằng lời của tôi
- [x] Chạy demo pipeline
- [x] Tách concept cần dùng lại
- [x] Chọn chapter tiếp theo
