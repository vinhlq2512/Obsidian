---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: course-note
title: "CS224N 2019 - Notes 05 - Language Models RNN GRU and LSTM"
year: 2019
venue: ""
arxiv: ""
source_file: "[[CS224N 2019 - Notes 05 - Language Models RNN GRU and LSTM.pdf]]"
pages: 14
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Autoregressive Language Model]]"
  - "[[Large Language Model]]"
tags:
  - cs224n
  - course-note
---

# CS224N 2019 - Notes 05 - Language Models RNN GRU and LSTM

## Nguồn

- PDF gốc: [[CS224N 2019 - Notes 05 - Language Models RNN GRU and LSTM.pdf]]
- Vai trò trong CS224N: lecture note phụ trợ về language models, RNN, bidirectional/deep RNN, GRU và LSTM.

## Câu hỏi trung tâm

RNN-family models biểu diễn xác suất chuỗi và xử lý dependency dài như thế nào?

## Kiến thức cốt lõi

- Language model gán xác suất cho chuỗi bằng tích xác suất có điều kiện.
- N-gram LM dùng fixed context window nên không bắt được dependency xa.
- RNN dùng hidden state để nén lịch sử.
- GRU và LSTM thêm gates để kiểm soát ghi/quên memory, giảm vanishing gradient.
- Bidirectional RNN dùng context hai chiều cho understanding tasks nhưng không phù hợp generation left-to-right trực tiếp.

## Cơ chế / công thức / kiến trúc

LM chain rule:

$$
P(w_1, ..., w_m)=\prod_i P(w_i|w_1,...,w_{i-1})
$$

RNN update:

```text
x_t + h_{t-1}
-> recurrent cell
-> h_t
-> output distribution
```

GRU/LSTM thêm gates để quyết định thông tin nào giữ, xoá, hoặc ghi mới.

## Khi áp dụng

- Dùng để hiểu vì sao Transformer thay thế RNN trong nhiều task.
- GRU/LSTM vẫn quan trọng khi cần mô hình tuần tự nhẹ hoặc lịch sử deep learning.
- So sánh bidirectional context với causal generation.

## Kết quả / bằng chứng đáng giữ

- Source first page định nghĩa LM xác suất chuỗi và n-gram approximation.
- Note liệt kê keyphrases RNN, Bi-directional RNN, Deep RNN, GRU, LSTM.
- Trang cuối mô tả trực giác stages của LSTM.

## Cách hiểu bằng lời của tôi

RNN-family là nỗ lực làm memory tuần tự tốt hơn. Gates giúp memory bền hơn, nhưng vẫn không xoá giới hạn xử lý tuần tự như Transformer.

## Câu hỏi review

1. N-gram LM giới hạn ở đâu?
2. Hidden state trong RNN chứa gì?
3. GRU/LSTM dùng gates để giải quyết vấn đề nào?
4. Bidirectional RNN khác causal LM thế nào?

## Liên kết

- [[Autoregressive Language Model]]
- [[Causal Language Model]]
- [[GRU]]
- [[LSTM]]
- [[Transformer]]
- [[CS224N]]
