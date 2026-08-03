---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2018 - On the Dimensionality of Word Embedding"
year: 2018
venue: "NeurIPS"
arxiv: ""
source_file: "[[2018 - On the Dimensionality of Word Embedding - NeurIPS.pdf]]"
pages: 12
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Embedding]]"
  - "[[Tokenization]]"
tags:
  - cs224n
  - paper
---

# 2018 - On the Dimensionality of Word Embedding - NeurIPS

## Nguồn

- PDF gốc: [[2018 - On the Dimensionality of Word Embedding - NeurIPS.pdf]]
- Vai trò trong CS224N: paper phân tích số chiều embedding và trade-off giữa capacity, data và noise.

## Câu hỏi trung tâm

Word embedding nên có bao nhiêu chiều, và vì sao tăng dimension không luôn tốt?

## Kiến thức cốt lõi

- Embedding dimension quyết định capacity của representation.
- Dimension quá thấp có thể underfit quan hệ nghĩa/cú pháp.
- Dimension quá cao có thể học noise, tốn compute và cần nhiều dữ liệu hơn.
- Số chiều tối ưu phụ thuộc corpus, objective và downstream task.
- Paper giúp tránh chọn 300/768/etc. như mặc định không suy nghĩ.

## Cơ chế / công thức / kiến trúc

```text
vocabulary + corpus statistics
-> chọn embedding dimension d
-> d thấp: nén mạnh, mất thông tin
-> d cao: nhiều capacity, nhiều tham số, rủi ro noise
```

Dimensionality là hyperparameter thống kê, không chỉ chi tiết engineering.

## Khi áp dụng

- Khi train embedding nhỏ, tune dimension cùng corpus size.
- Khi so sánh embedding, kiểm tra dimension có công bằng không.
- Liên hệ tới scaling model width trong LLM hiện đại.

## Kết quả / bằng chứng đáng giữ

- Tên paper và nguồn NeurIPS tập trung trực tiếp vào dimensionality của word embedding.
- Trong cụm CS224N, paper này bổ sung cho Word2Vec/GloVe bằng câu hỏi capacity.
- Nó giúp đặt embedding evaluation trong bối cảnh hyperparameter.

## Cách hiểu bằng lời của tôi

Embedding dimension giống kích thước chiếc hộp chứa thông tin. Hộp quá nhỏ làm mất chi tiết; hộp quá lớn có thể chứa cả nhiễu.

## Câu hỏi review

1. Dimension thấp và cao tạo trade-off gì?
2. Vì sao không có một số chiều tối ưu cho mọi task?
3. Dimension liên quan gì đến corpus size?

## Liên kết

- [[Embedding]]
- [[Word2Vec]]
- [[GloVe]]
- [[CS224N]]
