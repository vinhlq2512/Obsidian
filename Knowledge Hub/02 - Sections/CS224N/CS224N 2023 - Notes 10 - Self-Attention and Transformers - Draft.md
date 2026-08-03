---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: course-note
title: "CS224N 2023 - Notes 10 - Self-Attention and Transformers - Draft"
year: 2023
venue: ""
arxiv: ""
source_file: "[[CS224N 2023 - Notes 10 - Self-Attention and Transformers - Draft.pdf]]"
pages: 18
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Transformer]]"
  - "[[Self-Attention]]"
  - "[[Multi-Head Attention]]"
tags:
  - cs224n
  - course-note
---

# CS224N 2023 - Notes 10 - Self-Attention and Transformers - Draft

## Nguồn

- PDF gốc: [[CS224N 2023 - Notes 10 - Self-Attention and Transformers - Draft.pdf]]
- Vai trò trong CS224N: note chi tiết về self-attention và Transformer architecture.

## Câu hỏi trung tâm

Từ hạn chế của recurrent architectures, làm sao xây một kiến trúc sequence model dựa trên self-attention?

## Kiến thức cốt lõi

- Self-attention tạo contextual representation bằng cách mỗi token nhìn các token khác.
- Softmax thường chuẩn hoá trên dimension cuối để biến scores thành weights.
- Transformer encoder/decoder kết hợp embeddings, positional embeddings, multi-head attention, feed-forward, add & norm.
- Masked attention bảo vệ tính autoregressive trong decoder.
- Note giúp đi từ công thức attention đến kiến trúc đầy đủ.

## Cơ chế / công thức / kiến trúc

```text
embedding + position
-> Q/K/V projections
-> attention weights = softmax(QK^T / sqrt(d_k))
-> weighted sum of V
-> multi-head concat
-> feed-forward + residual/norm
```

## Khi áp dụng

- Dùng để bổ sung Lecture 05 khi cần công thức rõ hơn.
- Theo dõi tensor shape ở mỗi bước attention.
- Phân biệt encoder self-attention, decoder masked self-attention và cross-attention.

## Kết quả / bằng chứng đáng giữ

- Source summary nói note motivates moving away from recurrent architectures, introduces self-attention and Transformer.
- Trang đầu có sơ đồ encoder/decoder Transformer.
- Trang 2 giải thích softmax theo dimension cuối và embedding definition.

## Cách hiểu bằng lời của tôi

Self-attention là phép biến một sequence thành một sequence khác bằng cách học ma trận quan hệ giữa mọi token.

## Câu hỏi review

1. Self-attention tạo contextual representation thế nào?
2. Masked multi-head attention dùng ở đâu?
3. Vì sao cần positional embeddings?

## Liên kết

- [[Self-Attention]]
- [[Multi-Head Attention]]
- [[Transformer]]
- [[Positional Embeddings]]
- [[CS224N]]
