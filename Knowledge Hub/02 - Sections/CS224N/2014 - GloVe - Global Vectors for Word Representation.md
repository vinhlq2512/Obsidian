---
type: course-source
course: "[[CS224N]]"
status: developing
source_type: paper
title: "2014 - GloVe - Global Vectors for Word Representation"
year: 2014
venue: ""
arxiv: ""
source_file: "[[2014 - GloVe - Global Vectors for Word Representation.pdf]]"
pages: 12
created_at: 2026-08-02
updated_at: 2026-08-02
related_concepts:
  - "[[Embedding]]"
  - "[[Tokenization]]"
tags:
  - cs224n
  - paper
---

# 2014 - GloVe - Global Vectors for Word Representation

## Nguồn

- PDF gốc: [[2014 - GloVe - Global Vectors for Word Representation.pdf]]
- Đọc cùng: [[CS224N 2026 - Lecture 02 - Word Vectors]], [[CS224N 2019 - Notes 02 - Word Vectors II - GloVe Evaluation and Training]]
- Concept: [[Embedding]]

## Vấn đề paper giải quyết

Các phương pháp context-window như Word2Vec học từ local prediction, còn matrix factorization dùng global co-occurrence statistics. GloVe cố kết hợp hai phía: tận dụng thống kê co-occurrence toàn cục nhưng vẫn học vector dense hữu ích.

## Đóng góp chính

- Xây dựng mô hình log-bilinear regression trên ma trận word-word co-occurrence.
- Giải thích vì sao regularities tuyến tính có thể xuất hiện trong word vectors.
- Train trên các phần tử nonzero của co-occurrence matrix thay vì toàn bộ sparse matrix.

## Cơ chế trực giác

GloVe không chỉ hỏi “từ nào dự đoán context nào?” mà hỏi “tỷ lệ đồng xuất hiện giữa các từ nói gì về quan hệ nghĩa?”.

```text
corpus
-> word-word co-occurrence matrix
-> log co-occurrence ratios
-> học vector sao cho dot product phản ánh thống kê đồng xuất hiện
```

## Vì sao quan trọng với CS224N

GloVe là ví dụ đẹp cho việc học embedding từ global statistics. Nó giúp so sánh hai dòng ý tưởng trong embedding: local prediction và global count-based learning.

## Hạn chế / câu hỏi

- Vẫn là static word embedding nên một từ đa nghĩa có cùng vector trong mọi context.
- Phụ thuộc mạnh vào corpus và cách xây co-occurrence window.
- Cần so sánh với contextual representations như BERT để thấy bước tiến sau này.

## Câu hỏi review

1. GloVe khác Word2Vec ở nguồn tín hiệu training nào?
2. Vì sao co-occurrence ratio có thể mang thông tin nghĩa?
3. Static embedding thất bại ở polysemy như thế nào?
