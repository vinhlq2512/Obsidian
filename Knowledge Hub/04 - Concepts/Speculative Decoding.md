---
type: concept
status: developing
sources:
  - "[[CS224N 2026 - Lecture 13 - Reasoning Part 2]]"
  - "[[2022 - Fast Inference from Transformers via Speculative Decoding - arXiv 2211.17192v2]]"
source_sections:
  - "[[CS224N 2026 - Lecture 13 - Reasoning Part 2]]"
first_seen: 2026-08-02
last_updated: 2026-08-02
tags:
  - concept
  - text-generation
  - cs224n
---

# Speculative Decoding

## Định nghĩa

Speculative decoding là kỹ thuật tăng tốc inference cho [[Autoregressive Language Model]] bằng cách dùng một draft model nhỏ đề xuất nhiều token, rồi dùng target model lớn kiểm tra và chấp nhận hoặc từ chối các token đó.

## Cách hiểu bằng lời của tôi

Không phải token nào cũng cần model lớn tự sinh từ đầu. Với token dễ đoán, model nhỏ có thể đoán trước; model lớn chỉ cần xác nhận. Nếu đoán đúng nhiều token liên tiếp, ta tiết kiệm được nhiều bước forward của model lớn.

## Cơ chế

```text
draft model sinh k token ứng viên
-> target model tính xác suất cho các token này
-> chấp nhận prefix token phù hợp
-> nếu gặp token bị reject, sample lại từ target model
-> tiếp tục vòng lặp
```

## Điều cần biết

- Mục tiêu là giảm latency mà vẫn giữ chất lượng gần target model.
- Draft model phải đủ nhanh và đủ gần target model để tỷ lệ accept cao.
- Đây là ví dụ cho việc cải thiện LLM bằng thuật toán inference, không chỉ bằng training.

## Liên kết

- [[Text Generation]]
- [[Beam Search Decoding]]
- [[Greedy Decoding]]
- [[Large Language Model]]
- [[CS224N]]
