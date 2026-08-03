---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: lecture
title: "CS224N 2026 - Lecture 05 - Attention and Transformers"
year: 2026
venue: ""
arxiv: ""
source_file: "[[CS224N 2026 - Lecture 05 - Attention and Transformers.pdf]]"
pages: 70
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Transformer]]"
  - "[[Self-Attention]]"
  - "[[Multi-Head Attention]]"
tags:
  - cs224n
  - lecture
---
# CS224N 2026 - Lecture 05 - Attention and Transformers

## Nguồn

- PDF gốc: [[CS224N 2026 - Lecture 05 - Attention and Transformers.pdf]]
- Vai trò trong khoá: chuyển từ recurrence sang [[Self-Attention]] và [[Transformer]].
- Paper đọc kèm: [[2017 - Attention Is All You Need - arXiv 1706.03762v7]], [[2018 - Image Transformer - arXiv 1802.05751v3]], [[2018 - Music Transformer - Generating Music with Long-Term Structure - arXiv 1809.04281v3]].

## Mục tiêu cần hiểu

- Vì sao RNN gặp khó với vanishing gradients và parallelization.
- Attention giải quyết bài toán truy cập thông tin theo content như thế nào.
- Self-attention khác cross-attention ở nguồn của query/key/value.
- Transformer block kết hợp multi-head attention, feed-forward, residual connection và normalization ra sao.

## Ý chính

- RNN ép thông tin đi qua chuỗi hidden states; attention cho phép một vị trí chọn trực tiếp thông tin liên quan từ các vị trí khác.
- Trong seq2seq cổ điển, attention giúp decoder nhìn lại các encoder states thay vì phụ thuộc vào một vector context cố định.
- Self-attention đưa ý tưởng attention vào cùng một sequence: mỗi token tạo representation mới bằng cách lấy weighted sum từ các token khác.
- Transformer bỏ recurrence, dùng attention để trộn thông tin giữa token và feed-forward để xử lý từng vị trí.
- Lợi ích lớn: parallelization tốt hơn RNN và học dependency dài dễ hơn, nhưng cost attention theo sequence length thường là $O(n^2)$.

## Cơ chế self-attention

Mỗi token embedding được chiếu thành ba vector:

```text
x_i -> q_i, k_i, v_i
```

- Query $q_i$: token này đang tìm thông tin gì?
- Key $k_j$: token khác cung cấp loại thông tin gì?
- Value $v_j$: nội dung sẽ được trộn vào representation.

Score attention thường là dot product giữa query và key:

$$
score(i,j) = q_i^T k_j
$$

Sau softmax, ta có trọng số attention:

$$
\alpha_{ij} = \text{softmax}_j(score(i,j))
$$

Output cho token $i$:

$$
z_i = \sum_j \alpha_{ij} v_j
$$

## Multi-head attention

Một head chỉ tạo một phân phối attention. Multi-head attention chạy nhiều head song song để model có thể học nhiều loại quan hệ:

- quan hệ cú pháp;
- coreference;
- quan hệ local phrase;
- topic/global context;
- dấu hiệu task-specific.

Mental model:

```text
input tokens
-> nhiều attention heads nhìn nhiều kiểu quan hệ
-> concat heads
-> linear projection
-> representation giàu context hơn
```

## Transformer block

Một block thường gồm:

```text
input
-> multi-head self-attention
-> residual + layer norm
-> feed-forward layer
-> residual + layer norm
-> output
```

Self-attention trộn thông tin giữa token. Feed-forward layer biến đổi từng token độc lập. Residual và normalization giúp train sâu ổn định.

## Trade-off

- Tốt hơn RNN ở parallelization vì toàn bộ sequence có thể xử lý đồng thời.
- Tốt hơn RNN ở dependency dài vì token có đường truy cập trực tiếp.
- Đắt theo độ dài sequence vì attention matrix có kích thước $n \times n$.
- Cần positional information vì attention tự thân không biết thứ tự token.

## Cách hiểu bằng lời của tôi

Transformer thay câu hỏi “làm sao nén toàn bộ lịch sử vào hidden state?” bằng câu hỏi “mỗi token nên nhìn token nào, với trọng số bao nhiêu?”. Đây là bước nhảy quan trọng: context không còn là một đường dây tuần tự mà là một mạng quan hệ trực tiếp giữa mọi token.

## Câu hỏi review

1. Vì sao attention giúp học dependency dài tốt hơn RNN?
2. Query, key, value có vai trò gì?
3. Vì sao cần multi-head thay vì một attention head?
4. Feed-forward layer trong Transformer làm gì nếu self-attention đã trộn token?
5. Drawback chính của self-attention theo sequence length là gì?

## Gợi ý trả lời

1. Token có thể truy cập trực tiếp token xa thay vì truyền qua nhiều hidden states.
2. Query hỏi, key so khớp, value là nội dung được tổng hợp.
3. Nhiều head cho phép học nhiều loại quan hệ song song.
4. Nó biến đổi representation từng vị trí bằng phi tuyến tính sau khi đã nhận context.
5. Attention matrix tăng theo $O(n^2)$ với số token.

## Liên kết

- [[Self-Attention]]
- [[Multi-Head Attention]]
- [[Transformer]]
- [[Feed-Forward Layer]]
- [[Layer Normalization]]
- [[Positional Embeddings]]
- [[CS224N]]
