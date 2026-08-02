---
type: course-source
course: "[[CS224N]]"
status: developing
source_type: paper
title: "2017 - Attention Is All You Need"
year: 2017
venue: "arXiv"
arxiv: "1706.03762v7"
source_file: "[[2017 - Attention Is All You Need - arXiv 1706.03762v7.pdf]]"
pages: 15
created_at: 2026-08-02
updated_at: 2026-08-02
related_concepts:
  - "[[Self-Attention]]"
  - "[[Multi-Head Attention]]"
tags:
  - cs224n
  - paper
---

# 2017 - Attention Is All You Need - arXiv 1706.03762v7

## Nguồn

- PDF gốc: [[2017 - Attention Is All You Need - arXiv 1706.03762v7.pdf]]
- Đọc cùng: [[CS224N 2026 - Lecture 05 - Attention and Transformers]]
- Concept: [[Transformer]], [[Self-Attention]], [[Multi-Head Attention]], [[Cross-Attention]]

## Vấn đề paper giải quyết

Sequence transduction trước đây dựa vào recurrent/convolutional networks và attention. Paper đặt câu hỏi: có thể bỏ recurrence và convolution hoàn toàn, chỉ dùng attention để xây encoder-decoder không?

## Đóng góp chính

- Đề xuất Transformer dựa hoàn toàn trên attention mechanisms.
- Dùng multi-head self-attention để trộn thông tin giữa token.
- Kết hợp positional encoding, feed-forward layers, residual connections và normalization.
- Cho thấy kiến trúc attention-only có thể đạt kết quả mạnh cho machine translation và train hiệu quả hơn nhờ parallelization.

## Cơ chế Transformer

```text
input embeddings + positional encoding
-> encoder stack: self-attention + feed-forward
-> decoder stack: masked self-attention + cross-attention + feed-forward
-> output distribution
```

Attention lõi:

$$
\text{Attention}(Q,K,V)=\text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$

## Vì sao quan trọng với CS224N

Đây là paper trung tâm của khoá. Từ Lecture 05 trở đi, hầu hết nội dung như BERT, GPT, pretraining, RAG, agents và multimodal models đều là biến thể hoặc hệ sinh thái xung quanh Transformer.

## Hạn chế / câu hỏi

- Self-attention có cost $O(n^2)$ theo sequence length.
- Cần positional signal vì attention không tự có thứ tự.
- Kiến trúc mở đường cho scaling nhưng cũng tạo bài toán memory/compute lớn.

## Câu hỏi review

1. Transformer bỏ recurrence bằng cách nào?
2. Vì sao cần scale $QK^T$ bằng $\sqrt{d_k}$?
3. Masked self-attention khác encoder self-attention ở đâu?
4. Multi-head attention đem lại lợi ích gì?
