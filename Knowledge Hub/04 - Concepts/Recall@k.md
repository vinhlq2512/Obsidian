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

# Recall@k

## Định nghĩa

Recall@k là metric đo tỷ lệ câu hỏi mà retriever đưa được document/passage liên quan vào top `k` kết quả.

## Cách hiểu bằng lời của tôi

Trong QA, recall@k trả lời câu hỏi: "Trong `k` đoạn mà retriever lấy ra, có đoạn chứa đáp án không?"

```text
question
-> retriever returns top-k passages
-> check whether answer appears in those passages
-> recall@k
```

## Công thức trực giác

```text
recall@k = số câu hỏi có relevant passage trong top-k / tổng số câu hỏi
```

Trong context QA của chương này, "relevant" thường nghĩa là passage có chứa answer.

## Khi áp dụng

- Dùng để đánh giá [[Retriever]] trước khi đánh giá [[Reader]].
- Dùng để chọn `top_k_retriever`: k lớn tăng cơ hội chứa đáp án, nhưng làm pipeline chậm hơn.
- Dùng để so sánh [[Sparse Retriever]] như [[BM25]] với [[Dense Passage Retrieval]].

## Điểm cần cẩn thận

- Recall@k cao không đảm bảo answer cuối cùng đúng; reader vẫn phải trích đúng span.
- k càng lớn thường recall càng cao, nhưng latency tăng vì reader phải xử lý nhiều passage hơn.
- Nếu label/relevance không đúng, recall@k cũng gây hiểu nhầm.

## Câu hỏi review

1. Recall@k đo gì trong QA retrieval?
2. Vì sao tăng k thường tăng recall nhưng làm pipeline chậm hơn?
3. Vì sao recall@k cao chưa đủ để nói QA pipeline tốt?

## Gợi ý trả lời câu hỏi review

1. Nó đo khả năng retriever đưa passage chứa đáp án vào top-k.
2. Vì lấy nhiều passage hơn thì dễ có passage đúng hơn, nhưng reader phải đọc nhiều input hơn.
3. Vì reader có thể trích sai answer hoặc ranking answer cuối cùng có thể sai.

## Liên kết

- [[NLP Transformers - Chapter 07 - Question Answering]]
- [[Evaluating the Retriever]]
- [[Retriever]]
- [[BM25]]
- [[Dense Passage Retrieval]]
- [[Mean Average Precision]]
