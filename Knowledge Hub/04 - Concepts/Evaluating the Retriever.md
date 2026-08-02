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
  - retrieval
  - evaluation
  - question-answering
---

# Evaluating the Retriever

## Định nghĩa

Evaluating the retriever là bước đo xem [[Retriever]] có lấy được passage/document chứa đáp án vào top kết quả hay không.

## Cách hiểu bằng lời của tôi

Trước khi trách reader, phải hỏi: "Reader đã được đưa đúng đoạn để đọc chưa?" Nếu retriever không tìm được passage chứa answer, reader gần như không thể cứu pipeline.

```text
question
-> retriever top-k passages
-> check answer appears in top-k
-> recall@k / mAP
```

## Metric chính

- [[Recall@k]]: passage đúng có xuất hiện trong top-k không.
- [[Mean Average Precision]]: passage đúng xuất hiện cao trong ranking đến mức nào.

## Khi áp dụng

- Dùng trước khi đánh giá end-to-end QA pipeline.
- Dùng để chọn `top_k_retriever`: k quá thấp có thể mất answer; k quá cao làm chậm reader.
- Dùng để so sánh [[BM25]] với [[Dense Passage Retrieval]].

## Điểm cần cẩn thận

- Retriever đặt upper bound cho QA pipeline: nếu passage đúng không vào top-k, reader không có bằng chứng.
- Recall cao ở k lớn không miễn phí; latency tăng theo số passage reader phải xử lý.
- Với dataset như [[SubjQA]], cần filter đúng theo product/item khi evaluate để không trộn tài liệu sai phạm vi.

## Câu hỏi review

1. Vì sao cần đánh giá retriever riêng?
2. Recall@k trả lời câu hỏi gì?
3. Vì sao k là trade-off giữa recall và latency?

## Gợi ý trả lời câu hỏi review

1. Vì reader chỉ đọc passage được retriever đưa vào; lỗi retrieval và lỗi extraction cần tách riêng.
2. Nó hỏi passage chứa đáp án có nằm trong top-k kết quả hay không.
3. k lớn tăng cơ hội có passage đúng nhưng reader phải xử lý nhiều passage hơn.

## Liên kết

- [[NLP Transformers - Chapter 07 - Question Answering]]
- [[Retriever]]
- [[Recall@k]]
- [[Mean Average Precision]]
- [[BM25]]
- [[Dense Passage Retrieval]]
- [[Evaluating the Reader]]
