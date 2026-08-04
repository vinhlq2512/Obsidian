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

# Sparse Attention

## Định nghĩa

`Sparse Attention` là cách giảm chi phí của self-attention bằng việc **không cho mỗi token chú ý tới toàn bộ sequence**. Thay vào đó, mỗi token chỉ nhìn một tập con token theo một attention pattern được thiết kế trước.

## Vấn đề giải quyết

Trong self-attention chuẩn, attention matrix có kích thước gần như `n x n`, nên compute và memory tăng rất nhanh khi sequence dài.

Mental model:

```text
Full attention
-> token nào cũng nhìn mọi token
-> mạnh nhưng đắt

Sparse attention
-> token chỉ nhìn một phần sequence
-> rẻ hơn nhưng có thể mất bớt global context
```

## Cách hoạt động

Ý tưởng cốt lõi là thay attention pattern dày đặc bằng pattern thưa hơn. Một vài kiểu thường gặp:

- local / sliding-window attention: token chủ yếu nhìn các token gần nó;
- global tokens: một số token đặc biệt vẫn nhìn rộng hoặc được mọi token nhìn tới;
- block hoặc strided pattern: sequence được chia thành các khối hoặc bước nhảy để mở rộng vùng nhìn mà không cần full attention.

Luồng trực giác:

```text
Sequence dài
-> chọn attention pattern thưa
-> chỉ tính score trên các cặp token được phép
-> giảm compute và memory
```

## Vì sao hữu ích

- Giúp Transformer xử lý sequence dài hơn.
- Giảm chi phí memory so với [[Self-Attention]] đầy đủ.
- Là một hướng quan trọng trong efficient Transformers bên cạnh [[Linearized Attention]].

## Trade-off

- Rẻ hơn full attention.
- Nhưng không phải token nào cũng tương tác trực tiếp với mọi token khác.
- Nếu attention pattern thiết kế kém, model có thể bỏ lỡ dependency xa quan trọng.
- Sparse attention thường là đánh đổi giữa coverage của context và chi phí tính toán.

## So với full self-attention

| Kiểu | Ai nhìn ai? | Chi phí | Rủi ro |
|---|---|---|---|
| [[Self-Attention]] chuẩn | Gần như mọi token nhìn mọi token | Cao | Tốn memory/compute khi sequence dài |
| Sparse attention | Chỉ nhìn theo pattern thưa | Thấp hơn | Có thể mất tương tác toàn cục trực tiếp |

## Khi áp dụng

- Long document modeling
- Long-context QA
- Các bài toán sequence dài nơi full attention quá đắt
- Kiến trúc efficient Transformer cần giảm quadratic cost

## Cách hiểu bằng lời của tôi

Sparse attention là cách nói với Transformer rằng: “không cần lúc nào cũng nhìn hết mọi thứ”. Model chỉ nhìn những phần được cho là đáng chú ý theo một pattern nhất định, để đổi lấy khả năng xử lý context dài hơn với chi phí thấp hơn.

## Câu hỏi review

1. Sparse attention giảm chi phí bằng cách nào?
2. Đánh đổi chính của sparse attention so với full attention là gì?
3. Vì sao local window thôi có thể chưa đủ?

## Liên kết

- [[Self-Attention]]
- [[Multi-Head Attention]]
- [[Linearized Attention]]
- [[NLP Transformers - Chapter 11 - Future Directions]]
