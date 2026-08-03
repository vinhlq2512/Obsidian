---
type: concept
status: developing
sources:
  - "[[2014 - GloVe - Global Vectors for Word Representation]]"
  - "[[CS224N 2019 - Notes 02 - Word Vectors II - GloVe Evaluation and Training]]"
source_sections:
  - "[[CS224N 2019 - Notes 02 - Word Vectors II - GloVe Evaluation and Training]]"
first_seen: 2026-08-03
last_updated: 2026-08-03
tags:
  - concept
  - nlp
  - cs224n
---

# GloVe

## Định nghĩa

GloVe, Global Vectors for Word Representation, là phương pháp học [[Embedding|word embeddings]] từ thống kê đồng xuất hiện toàn cục của từ trong corpus.

## Cách hiểu bằng lời của tôi

GloVe không chỉ học từ cửa sổ context cục bộ như [[Word2Vec]]. Nó nhìn toàn corpus như một ma trận đồng xuất hiện lớn rồi học vector sao cho quan hệ giữa vector phản ánh thống kê đó.

## Công thức trực giác

Nếu $X_{ij}$ là số lần từ $j$ xuất hiện trong context của từ $i$, GloVe khai thác thông tin từ co-occurrence ratios và log co-occurrence.

Mental model:

```text
corpus
-> word-word co-occurrence matrix
-> log co-occurrence statistics
-> học vector dense
```

## Cần biết

- GloVe nằm giữa count-based distributional semantics và neural embeddings.
- Vẫn là static embedding nên một word type thường chỉ có một vector.
- Đánh giá GloVe nên tách intrinsic evaluation và extrinsic evaluation.

## Liên kết

- [[Embedding]]
- [[Word2Vec]]
- [[Tokenization]]
- [[CS224N]]
