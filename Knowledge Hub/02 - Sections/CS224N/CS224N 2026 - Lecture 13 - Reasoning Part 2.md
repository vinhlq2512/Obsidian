---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: lecture
title: "CS224N 2026 - Lecture 13 - Reasoning Part 2"
year: 2026
venue: ""
arxiv: ""
source_file: "[[CS224N 2026 - Lecture 13 - Reasoning Part 2.pdf]]"
pages: 59
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Prompt Engineering]]"
  - "[[Large Language Model]]"
tags:
  - cs224n
  - lecture
---
# CS224N 2026 - Lecture 13 - Reasoning Part 2

## Nguồn

- PDF gốc: [[CS224N 2026 - Lecture 13 - Reasoning Part 2.pdf]]
- Vai trò trong khoá: speculative decoding, on-policy/off-policy drift, long-context extension và inference-time scaling.
- Paper đọc kèm: [[2022 - Fast Inference from Transformers via Speculative Decoding - arXiv 2211.17192v2]], [[2023 - Lets Verify Step by Step - arXiv 2305.20050v1]].

## Mục tiêu cần hiểu

- [[Speculative Decoding|Speculative decoding]] tăng tốc inference bằng draft model và target model.
- Off-policy drift xuất hiện khi data/policy dùng để train không khớp policy đang triển khai.
- Long context extension không chỉ là tăng positional embeddings; còn là vấn đề attention, data và evaluation.
- Inference-time scaling dùng thêm compute lúc suy luận để cải thiện answer quality.

## Ý chính

- Large LM sinh token chậm vì mỗi token cần forward qua model lớn.
- [[Speculative Decoding|Speculative decoding]] dùng model nhỏ sinh nhiều token nháp, model lớn kiểm tra/chấp nhận để giữ phân phối đúng hơn nhưng giảm số lần gọi model lớn.
- Off-policy data có thể làm model học từ phân phối cũ, dẫn tới drift khi triển khai policy mới.
- On-policy distillation tìm cách thu data từ chính policy hiện tại để giảm mismatch.
- Long-context và test-time compute đều cho thấy inference không còn là bước cố định; ta có thể thiết kế thêm thuật toán quanh model.

## [[Speculative Decoding]] mental model

```text
draft model nhỏ sinh nhiều token ứng viên
-> target model lớn kiểm tra xác suất các token đó
-> chấp nhận prefix token phù hợp
-> nếu token bị reject, sample lại từ target
-> tăng tốc mà vẫn dựa vào target distribution
```

Trực giác: nhiều token dễ đoán không cần model lớn tự sinh từng token một. Model nhỏ “đề xuất”, model lớn “duyệt”.

## Off-policy vs on-policy

- **Off-policy**: data đến từ policy khác policy đang train/triển khai.
- **On-policy**: data đến từ chính policy hiện tại.
- Drift xảy ra khi model học tốt trên phân phối cũ nhưng hành vi rollout mới đi vào vùng khác.

## Cách hiểu bằng lời của tôi

Lecture này xem inference như một hệ thống chứ không chỉ là `model.generate()`. Ta có thể tăng tốc bằng model nhỏ, tăng chất lượng bằng compute lúc test, hoặc làm hỏng model nếu train/eval không khớp phân phối hành vi thật.

## Câu hỏi review

1. [[Speculative Decoding|Speculative decoding]] tăng tốc ở đâu?
2. Vì sao cần target model kiểm tra draft tokens?
3. Off-policy drift nguy hiểm trong RL/distillation như thế nào?
4. Long context extension có những rủi ro nào ngoài memory cost?
5. Inference-time scaling khác scaling model parameters ra sao?

## Liên kết

- [[Text Generation]]
- [[Autoregressive Language Model]]
- [[Beam Search Decoding]]
- [[Large Language Model]]
- [[CS224N]]
