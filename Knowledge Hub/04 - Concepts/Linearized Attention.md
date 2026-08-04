---
type: concept
status: seed
sources:
  - "[[NLP Transformers - Chapter 11 - Future Directions]]"
source_sections:
  - "[[NLP Transformers - Chapter 11 - Future Directions]]"
first_seen: 2026-08-04
last_updated: 2026-08-04
tags:
  - concept
  - transformer
  - attention
  - efficient-transformers
  - nlp
---

# Linearized Attention

## Định nghĩa

`Linearized Attention` là hướng giảm chi phí của attention bằng cách **đổi cách tính attention** để tránh phải tạo đầy đủ attention matrix `n x n` như trong [[Self-Attention]] chuẩn.

## Vấn đề giải quyết

Self-attention chuẩn có chi phí tăng rất nhanh theo độ dài sequence vì phải tính tương tác giữa gần như mọi cặp token.

Mental model:

```text
Full attention
-> tạo ma trận attention dày đặc
-> chi phí tăng mạnh theo sequence length

Linearized attention
-> viết lại phép tính attention theo dạng rẻ hơn
-> cố giảm quadratic bottleneck
```

## Cách hoạt động

Khác với [[Sparse Attention]] là bớt số cặp token được nhìn, linearized attention cố giữ ý tưởng attention nhưng **biến đổi phép tính** để phần compute có thể tách/gộp lại hiệu quả hơn.

Luồng trực giác:

```text
Q, K, V
-> biến đổi hoặc kernelize Q/K
-> sắp xếp lại phép nhân
-> tránh materialize toàn bộ attention matrix
-> giảm compute/memory khi sequence dài
```

Điểm cốt lõi cần nhớ: sparse attention giảm chi phí bằng **pattern thưa**, còn linearized attention giảm chi phí bằng **đổi dạng phép toán**.

## Vì sao hữu ích

- Nhắm tới bài toán context dài nơi full attention quá đắt.
- Là một hướng efficient attention khác với việc cắt bớt kết nối attention.
- Giúp mở rộng Transformer cho sequence dài hơn nếu approximation đủ tốt.

## Trade-off

- Có thể rẻ hơn full attention trên sequence dài.
- Nhưng thường phải đánh đổi bằng approximation hoặc thay đổi tính chất của attention chuẩn.
- Chất lượng phụ thuộc việc phép biến đổi mới có giữ được tín hiệu quan trọng hay không.
- Dễ hiểu nhầm là “attention y hệt nhưng miễn phí”, trong khi thực tế đây là một biến thể có giả định và đánh đổi riêng.

## So với sparse attention

| Hướng | Giảm chi phí bằng cách nào? | Ý tưởng chính | Rủi ro |
|---|---|---|---|
| [[Sparse Attention]] | Bỏ bớt các kết nối attention | Token chỉ nhìn một phần sequence | Có thể bỏ lỡ dependency xa |
| Linearized attention | Đổi cách tính attention | Tránh tạo attention matrix đầy đủ | Approximation có thể làm mất fidelity |

## Khi áp dụng

- Long-context modeling
- Efficient Transformer research
- Bài toán mà full attention chuẩn không còn phù hợp về compute hoặc memory

## Cách hiểu bằng lời của tôi

Nếu sparse attention là “nhìn ít chỗ hơn”, thì linearized attention là “tính thông minh hơn”. Nó cố giữ tinh thần của attention, nhưng viết lại phép tính để bớt cái giá phải trả khi sequence quá dài.

## Câu hỏi review

1. Linearized attention khác sparse attention ở ý tưởng cốt lõi nào?
2. Vì sao linearized attention không đơn giản chỉ là “attention chuẩn nhưng nhanh hơn”?
3. Khi nào linearized attention đáng cân nhắc hơn full attention?

## Liên kết

- [[Self-Attention]]
- [[Sparse Attention]]
- [[Multi-Head Attention]]
- [[NLP Transformers - Chapter 11 - Future Directions]]
