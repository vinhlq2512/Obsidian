---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2021 - RoFormer - Enhanced Transformer with Rotary Position Embedding"
year: 2021
venue: "arXiv"
arxiv: "2104.09864v5"
source_file: "[[2021 - RoFormer - Enhanced Transformer with Rotary Position Embedding - arXiv 2104.09864v5.pdf]]"
pages: 14
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Embedding]]"
  - "[[Transformer]]"
  - "[[Self-Attention]]"
  - "[[Multi-Head Attention]]"
tags:
  - cs224n
  - paper
---

# 2021 - RoFormer - Enhanced Transformer with Rotary Position Embedding - arXiv 2104.09864v5

## Nguồn

- PDF gốc: [[2021 - RoFormer - Enhanced Transformer with Rotary Position Embedding - arXiv 2104.09864v5.pdf]]
- Vai trò trong CS224N: paper nền cho Rotary Positional Embedding (RoPE), kỹ thuật positional encoding phổ biến trong LLM.

## Câu hỏi trung tâm

Có thể mã hoá vị trí vào attention bằng phép xoay để biểu diễn quan hệ vị trí tương đối tốt hơn không?

## Kiến thức cốt lõi

- RoFormer giới thiệu rotary position embedding.
- RoPE mã hoá vị trí bằng cách xoay query/key trong không gian vector.
- Dot product giữa query/key sau xoay mang thông tin vị trí tương đối.
- RoPE trở nên phổ biến trong nhiều decoder-only LLM hiện đại.
- Paper nối trực tiếp với vấn đề positional information trong Transformer.

## Cơ chế / công thức / kiến trúc

```text
token embedding
-> tạo Q và K
-> áp phép xoay phụ thuộc vị trí lên Q/K
-> attention score chứa thông tin relative position
```

Trực giác: vị trí không được cộng như vector riêng, mà được nhúng vào hình học của attention.

## Khi áp dụng

- Dùng khi đọc kiến trúc LLM hiện đại.
- Chú ý các biến thể mở rộng context thường điều chỉnh RoPE.
- Liên hệ trực tiếp với [[Positional Embeddings]].

## Kết quả / bằng chứng đáng giữ

- Title nêu enhanced Transformer with Rotary Position Embedding.
- Lecture/notes CS224N xem positional encoding là phần bắt buộc vì attention không tự biết thứ tự.
- Vault đã có [[Positional Embeddings]] nhắc RoPE như biến thể phổ biến.

## Cách hiểu bằng lời của tôi

RoPE làm vị trí trở thành phép biến đổi trong attention, nhờ đó quan hệ tương đối giữa token đi vào score tự nhiên hơn.

## Câu hỏi review

1. Vì sao Transformer cần positional information?
2. RoPE áp vào Q/K hay V?
3. Vì sao RoPE hữu ích cho LLM hiện đại?

## Liên kết

- [[Positional Embeddings]]
- [[Self-Attention]]
- [[Transformer]]
- [[Rotary Positional Embeddings]]
- [[CS224N]]
