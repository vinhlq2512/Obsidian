---
type: concept
status: understood
sources:
  - "[[2026-04-06_a-guide-to-context-engineering-for-llms]]"
  - "[[2026-08-04_why-an-llms-memory-gets-expensive-and-how-to-fix-it]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - llm
  - context-engineering
  - performance
---

# Context Compression

## Định nghĩa

Context Compression (Nén ngữ cảnh) là tập hợp các kỹ thuật nhằm rút gọn số lượng token đưa vào cửa sổ ngữ cảnh (Context Window) của LLM mà vẫn bảo toàn đầy đủ các thông tin ngữ nghĩa quan trọng phục vụ cho việc suy luận.

## Lý do cần Context Compression

1. **Chi phí Quadratic của Attention ($O(N^2)$)**: Chi phí tính toán và dung lượng bộ nhớ KV Cache tăng theo bình phương độ dài context.
2. **Hiện tượng Lost in the Middle**: LLM có xu hướng chú ý nhiều hơn vào đầu và cuối prompt, dễ bỏ qua thông tin nằm ở giữa context quá dài.
3. **Tiết kiệm Token Spend**: Giảm chi phí API trả theo token count.

## Phương pháp triển khai

```text
Raw Long Prompt / System History
-> Context Compression Engine:
   - Selective Token Pruning (Xóa stop-words, whitespace, redundant info)
   - Hierarchical Summarization (Tóm tắt hội thoại theo phân đoạn)
   - KV Cache Quantization (Nén KV cache từ FP16 xuống INT8/INT4)
-> Compressed Prompt -> Fast & Low-Cost LLM Inference
```

- **Prompt Trimming & Pruning**: Xóa bớt các đoạn code không liên quan hoặc thông tin trùng lặp.
- **Semantic Summarization**: Dùng một mô hình nhỏ (như SLM) để tóm tắt lịch sử hội thoại dài thành một đoạn tóm tắt súc tích trước khi append message mới.
- **Attention-based KV Cache Eviction**: Loại bỏ các token trong KV Cache có điểm Attention Weight thấp (ví dụ: StreamingLLM, H2O).

## Trade-off

- Nén quá mức có thể làm mất các thông tin chi tiết nhạy cảm (Edge cases/Nuances).
- Tốn thêm tài nguyên compute để chạy bước compression trước khi gọi LLM chính.

## Liên kết

- [[Context Engineering]]
- [[KV Cache]]
- [[LLM Cost Optimization]]
- [[LLM Memory]]
