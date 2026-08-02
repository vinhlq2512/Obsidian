---
type: question
status: open
concepts:
  - "[[Layer Normalization]]"
  - "[[Transformer]]"
sources:
  - "[[27-07-2026]]"
  - "[[Layer Normalization]]"
created_at: 2026-08-02
updated_at: 2026-08-02
tags:
  - question
  - transformer
---

# When to Prefer Pre-LN Over Post-LN

## Tôi đang thắc mắc gì?

- Trong các kiến trúc LLM hiện đại, khi nào nên ưu tiên Pre-LN thay vì Post-LN?

## Vì sao câu hỏi này quan trọng?

- Vị trí LayerNorm ảnh hưởng độ ổn định khi train Transformer sâu.
- Khi đọc model config hoặc paper, cần hiểu chi tiết này thay đổi training dynamics như thế nào.

## Giải thích hiện tại

- [[Layer Normalization]] hiện ghi rằng Post-LN gần với Transformer gốc, còn Pre-LN thường ổn định hơn khi train model rất sâu.
- Ghi chú này chưa đủ để quyết định trong từng setup cụ thể.

## Cần kiểm tra thêm

- Pre-LN và Post-LN khác nhau thế nào về gradient flow?
- Có trade-off nào về chất lượng cuối cùng hoặc convergence không?
- RMSNorm nằm trong bức tranh này như thế nào?

## Source evidence

- [[27-07-2026]]
- [[Layer Normalization]]

## Related

- [[How Transformer Block Works]]
- [[Transformers]]

