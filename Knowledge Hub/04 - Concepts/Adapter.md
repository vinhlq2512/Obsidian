---
type: concept
status: developing
sources:
  - "[[CS224N 2026 - Lecture 09 - Efficient Adaptation]]"
  - "[[CS224N 2026 - Lecture 10 - RAG and Language Agents]]"
  - "[[2019 - Parameter-Efficient Transfer Learning for NLP - arXiv 1902.00751v2]]"
source_sections:
  - "[[CS224N 2026 - Lecture 09 - Efficient Adaptation]]"
first_seen: 2026-08-02
last_updated: 2026-08-02
tags:
  - concept
  - peft
  - cs224n
---

# Adapter

## Định nghĩa

Adapter là module nhỏ được chèn vào model pretrained để học task/domain mới mà không cần cập nhật toàn bộ tham số gốc.

## Cách hiểu bằng lời của tôi

Adapter giống một lớp biến đổi phụ đặt giữa các layer. Model gốc giữ nguyên, còn adapter học cách uốn representation cho task cụ thể.

## Công thức trực giác

Adapter bottleneck thường có dạng:

$$
f_\phi(x) = W_U\sigma(W_Dx)
$$

- $W_D$: down-projection từ chiều lớn $d$ xuống bottleneck nhỏ $k$.
- $W_U$: up-projection từ $k$ về lại $d$.
- $k \ll d$, nên số tham số train thêm nhỏ hơn full fine-tuning nhiều.

## Trade-off

- Tiết kiệm tham số và memory optimizer.
- Dễ lưu nhiều adapter cho nhiều task/language.
- Thêm latency/parameters khi inference nếu giữ module riêng.
- Capacity phụ thuộc kích thước bottleneck và vị trí chèn adapter.

## Liên kết

- [[Parameter-Efficient Fine-Tuning]]
- [[Fine-tuning]]
- [[Transformer]]
- [[CS224N]]
