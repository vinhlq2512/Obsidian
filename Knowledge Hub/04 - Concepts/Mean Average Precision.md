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

# Mean Average Precision

## Định nghĩa

Mean average precision, viết tắt là mAP, là metric ranking thưởng cho retriever khi đặt các document liên quan ở vị trí cao trong danh sách kết quả.

## Cách hiểu bằng lời của tôi

Recall@k chỉ hỏi "có tìm thấy không?". mAP hỏi thêm "tìm thấy sớm đến mức nào?". Nếu passage đúng nằm ở rank 1 thì tốt hơn nằm ở rank 10.

```text
retrieved ranking
-> relevant passages càng lên cao càng tốt
-> average precision per query
-> mean over queries
```

## Khi áp dụng

- Dùng bổ sung cho [[Recall@k]] khi thứ tự ranking quan trọng.
- Hữu ích khi muốn reader đọc ít passage hơn mà vẫn thấy passage đúng sớm.
- Dùng để so sánh các retriever có recall gần nhau nhưng ranking khác nhau.

## Điểm cần cẩn thận

- mAP cần định nghĩa rõ document nào là relevant.
- Trong QA thực tế, passage đúng nằm cao giúp giảm latency vì có thể giảm `top_k_retriever`.
- mAP không thay thế evaluation của [[Reader]]; nó chỉ đánh giá ranking/retrieval.

## Câu hỏi review

1. mAP khác recall@k ở điểm nào?
2. Vì sao passage đúng ở rank cao quan trọng với QA pipeline?
3. mAP đánh giá retriever hay reader?

## Gợi ý trả lời câu hỏi review

1. Recall@k đo có tìm thấy trong top-k không; mAP thưởng việc đặt kết quả đúng ở rank cao.
2. Vì reader có thể đọc ít passage hơn, latency giảm và answer tốt dễ được chọn hơn.
3. mAP đánh giá retriever/ranking, không đánh giá reader trích answer.

## Liên kết

- [[NLP Transformers - Chapter 07 - Question Answering]]
- [[Evaluating the Retriever]]
- [[Recall@k]]
- [[Retriever]]
