---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: course-note
title: "CS224N 2019 - Notes 02 - Word Vectors II - GloVe Evaluation and Training"
year: 2019
venue: ""
arxiv: ""
source_file: "[[CS224N 2019 - Notes 02 - Word Vectors II - GloVe Evaluation and Training.pdf]]"
pages: 13
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Embedding]]"
  - "[[Tokenization]]"
  - "[[Measuring the Quality of Generated Text]]"
tags:
  - cs224n
  - course-note
---

# CS224N 2019 - Notes 02 - Word Vectors II - GloVe Evaluation and Training

## Nguồn

- PDF gốc: [[CS224N 2019 - Notes 02 - Word Vectors II - GloVe Evaluation and Training.pdf]]
- Vai trò trong CS224N: lecture note phụ trợ về GloVe, co-occurrence matrix và evaluation của word vectors.

## Câu hỏi trung tâm

GloVe học word vectors từ co-occurrence statistics như thế nào và đánh giá embedding ra sao?

## Kiến thức cốt lõi

- Co-occurrence matrix $X$ lưu số lần word $j$ xuất hiện trong context của word $i$.
- $P_{ij}=P(w_j|w_i)=X_{ij}/X_i$ là xác suất context word theo center word.
- GloVe khai thác global co-occurrence statistics thay vì chỉ local prediction windows.
- Intrinsic evaluation gồm analogy và similarity correlation.
- Extrinsic evaluation kiểm tra embedding trong task downstream như classification/window model.

## Cơ chế / công thức / kiến trúc

```text
corpus
-> word-word co-occurrence matrix X
-> xác suất context P_ij
-> GloVe objective học vectors phản ánh log co-occurrence
-> evaluate bằng intrinsic/extrinsic tasks
```

## Khi áp dụng

- Dùng để hiểu [[GloVe]] chi tiết hơn paper gốc.
- Khi đánh giá word vectors, phân biệt benchmark nhanh và task thật.
- Cẩn thận với ambiguity: một word vector tĩnh không giải quyết nhiều nghĩa theo context.

## Kết quả / bằng chứng đáng giữ

- Source first page liệt kê keyphrases: GloVe, intrinsic/extrinsic evaluations, analogies, ambiguity.
- Trang 2 định nghĩa co-occurrence matrix và $P_{ij}$.
- Note bàn cả evaluation và training, không chỉ công thức GloVe.

## Cách hiểu bằng lời của tôi

GloVe nhìn corpus như một bản đồ đồng xuất hiện toàn cục. Vector tốt là vector nén được bản đồ đó theo cách hữu ích cho nghĩa và downstream tasks.

## Câu hỏi review

1. $X_{ij}$ và $P_{ij}$ nghĩa là gì?
2. Intrinsic evaluation khác extrinsic evaluation ra sao?
3. GloVe khác skip-gram ở nguồn thống kê nào?

## Liên kết

- [[GloVe]]
- [[Embedding]]
- [[Word2Vec]]
- [[CS224N]]
