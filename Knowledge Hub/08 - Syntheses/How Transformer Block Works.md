---
type: synthesis
status: evolving
concepts:
  - "[[Transformer]]"
  - "[[Self-Attention]]"
  - "[[Multi-Head Attention]]"
  - "[[Feed-Forward Layer]]"
  - "[[Layer Normalization]]"
  - "[[Positional Embeddings]]"
sources:
  - "[[NLP Transformers - Chapter 03 - Transformer Anatomy]]"
  - "[[Transformer]]"
questions:
  - "[[When to Prefer Pre-LN Over Post-LN]]"
created_at: 2026-08-02
updated_at: 2026-08-02
tags:
  - synthesis
  - transformer
---

# How Transformer Block Works

## Câu hỏi trung tâm

- Một Transformer block biến sequence embeddings thành contextualized embeddings như thế nào?

## Mental model

```text
token IDs
-> token embeddings + positional embeddings
-> multi-head self-attention: token trao đổi thông tin
-> residual + layer normalization: giữ tín hiệu ổn định
-> feed-forward layer: xử lý từng token sau khi đã có context
-> residual + layer normalization
-> contextualized embeddings
```

## Các concept cấu thành

- [[Self-Attention]]: mỗi token lấy thông tin từ các token liên quan trong sequence.
- [[Multi-Head Attention]]: chạy nhiều attention pattern song song để học nhiều kiểu quan hệ.
- [[Feed-Forward Layer]]: biến đổi từng token representation sau khi attention đã đưa context vào.
- [[Layer Normalization]]: giữ scale activation ổn định khi xếp nhiều layer.
- [[Positional Embeddings]]: thêm thông tin thứ tự vì attention tự thân không biết vị trí.

## Tại sao cần từng thành phần?

### Attention

- Attention là nơi token trao đổi thông tin với nhau.
- Nếu thiếu attention, representation của token khó dùng context xa.

### Feed-forward layer

- Attention chủ yếu trộn value vectors theo trọng số.
- Feed-forward layer thêm biến đổi phi tuyến trên từng token, giúp representation sâu hơn.

### Residual + LayerNorm

- Residual giữ đường truyền thông tin và gradient.
- LayerNorm cân lại scale activation để stack nhiều layer ổn định hơn.

## Tổng hợp của tôi

- Transformer block có thể nhớ như hai nhịp: `trao đổi thông tin giữa token` rồi `xử lý từng token`.
- Attention không thay thế MLP; attention quyết định lấy context từ đâu, còn feed-forward quyết định xử lý representation đã có context như thế nào.
- Normalization và residual không phải phần phụ trang trí; chúng là hạ tầng giúp nhiều block xếp chồng mà không làm training mất ổn định.

## Nguồn

- [[NLP Transformers - Chapter 03 - Transformer Anatomy]]
- [[Transformer]]
- [[Self-Attention]]
- [[Multi-Head Attention]]
- [[Feed-Forward Layer]]
- [[Layer Normalization]]

## Liên kết

- [[Transformers]]
- [[Encoder-only vs Decoder-only vs Encoder-Decoder]]

