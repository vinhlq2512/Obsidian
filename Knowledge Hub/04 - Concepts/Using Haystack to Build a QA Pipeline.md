---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 07 - Question Answering]]"
source_sections:
  - "[[NLP Transformers - Chapter 07 - Question Answering]]"
first_seen: 2026-08-02
last_updated: 2026-08-02
created_at: 2026-08-02
updated_at: 2026-08-02
tags:
  - concept
  - nlp
  - question-answering
  - retrieval
---

# Using Haystack to Build a QA Pipeline

## Định nghĩa

Using Haystack to build a QA pipeline là cách dùng Haystack để ghép các thành phần của [[Question Answering]] thành một workflow chạy được: lưu tài liệu, truy xuất passage liên quan, đọc passage, rồi trả về answer.

## Cách hiểu bằng lời của tôi

Haystack không phải là model QA mới. Nó là framework giúp nối nhiều mảnh của hệ thống QA lại thành pipeline có thể thử nghiệm và thay thế từng phần.

```text
documents/reviews
-> DocumentStore
-> [[Retriever]]
-> [[Reader]]
-> answers + scores + supporting context
```

## Thành phần chính

- **DocumentStore**: nơi lưu corpus, metadata và index để retriever tìm kiếm.
- **Retriever**: lấy top-k document/passage có khả năng chứa câu trả lời; có thể bắt đầu bằng [[BM25]] trước khi thử dense retrieval.
- **Reader**: đọc các passage ứng viên và trích answer span.
- **Pipeline**: định nghĩa thứ tự các bước và cách output của bước trước đi vào bước sau.
- **Ranked answers**: nhiều passage có thể sinh nhiều answer candidate; hệ thống cần xếp hạng theo score.
- **Evaluation nodes**: tách đo retriever bằng [[Recall@k]]/[[Mean Average Precision]] và reader bằng [[Exact Match]]/[[F1 Score]].

## Mental model

```text
Tự viết QA từ đầu:
load data + index + retrieve + run reader + rank + debug

Dùng Haystack:
khai báo component
-> nối thành pipeline
-> thay retriever/reader dễ hơn
-> đánh giá từng bước rõ hơn
```

## Khi áp dụng

- Xây [[Building a Review-Based QA System]] trên nhiều review hoặc tài liệu ngắn.
- Muốn thử nhiều loại retriever mà không viết lại toàn bộ pipeline.
- Muốn so sánh baseline keyword retrieval như [[BM25]] với dense retriever.
- Cần tách lỗi rõ hơn: lỗi do dữ liệu/index, do [[Retriever]], hay do [[Reader]].
- Muốn trả lời kèm context hỗ trợ để biết answer đến từ đoạn nào.
- Muốn điều chỉnh `top_k_retriever` và `top_k_reader` để cân bằng recall, chất lượng answer và latency.

## Điểm cần cẩn thận

- Pipeline framework không tự làm dữ liệu tốt hơn; document cleaning và chunking vẫn quan trọng.
- Nếu retriever bỏ lỡ passage chứa đáp án, reader không có đủ bằng chứng để trích đúng.
- Nếu reader được huấn luyện trên domain khác, có thể cần [[Domain Adaptation]].
- Không nên chỉ ghi nhớ API cụ thể của Haystack; nên nhớ kiến trúc pipeline vì API có thể thay đổi theo version.

## Câu hỏi review

1. Haystack giúp gì khi xây QA pipeline?
2. DocumentStore khác retriever ở điểm nào?
3. Vì sao pipeline cần tách retriever và reader?
4. Khi QA pipeline trả lời sai, cần debug những tầng nào?
5. `top_k_retriever` ảnh hưởng gì đến recall và latency?

## Gợi ý trả lời câu hỏi review

1. Nó giúp nối document store, retriever, reader và bước xếp hạng answer thành một workflow chạy được.
2. DocumentStore lưu và index tài liệu; retriever truy vấn index để lấy passage liên quan.
3. Vì retriever quyết định context được đọc, còn reader quyết định span trả lời trong context đó.
4. Kiểm tra dữ liệu/chunking, index, retriever top-k, reader span, và cách rank answer cuối cùng.
5. Tăng `top_k_retriever` thường tăng cơ hội có passage đúng, nhưng reader phải xử lý nhiều passage hơn nên latency tăng.

## Liên kết

- [[NLP Transformers - Chapter 07 - Question Answering]]
- [[Question Answering]]
- [[Building a Review-Based QA System]]
- [[BM25]]
- [[Retriever]]
- [[Evaluating the Retriever]]
- [[Evaluating the Reader]]
- [[Reader]]
- [[Extractive QA]]
- [[Domain Adaptation]]
