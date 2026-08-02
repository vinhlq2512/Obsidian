---
type: course-source
course: "[[CS224N]]"
status: developing
source_type: paper
title: "2022 - Fast Inference from Transformers via Speculative Decoding"
year: 2022
venue: "arXiv"
arxiv: "2211.17192v2"
source_file: "[[2022 - Fast Inference from Transformers via Speculative Decoding - arXiv 2211.17192v2.pdf]]"
pages: 13
created_at: 2026-08-02
updated_at: 2026-08-02
related_concepts:
  - "[[Transformer]]"
  - "[[Self-Attention]]"
  - "[[Multi-Head Attention]]"
  - "[[Beam Search Decoding]]"
  - "[[Text Generation]]"
tags:
  - cs224n
  - paper
---

# 2022 - Fast Inference from Transformers via Speculative Decoding - arXiv 2211.17192v2

## Nguồn

- PDF gốc: [[2022 - Fast Inference from Transformers via Speculative Decoding - arXiv 2211.17192v2.pdf]]
- Đọc cùng: [[CS224N 2026 - Lecture 13 - Reasoning Part 2]]
- Concept: [[Speculative Decoding]], [[Text Generation]]

## Vấn đề paper giải quyết

Autoregressive decoding chậm vì sinh $K$ token cần $K$ lần chạy tuần tự model lớn. Paper đề xuất tăng tốc bằng cách sinh nhiều token ứng viên song song bằng model nhỏ nhưng không đổi phân phối output của model lớn.

## Đóng góp chính

- Dùng approximation/draft model để đề xuất token.
- Dùng target model kiểm tra nhiều token cùng lúc.
- Có thể tăng tốc off-the-shelf models mà không cần retraining hoặc đổi architecture.

## Cơ chế

```text
draft model generate k tokens
-> target model evaluate batch token candidates
-> accept nhiều token nếu phù hợp
-> reject thì quay về target sampling
```

## Vì sao quan trọng với CS224N

Lecture 13 dùng paper này để minh hoạ rằng inference-time algorithm có thể cải thiện hệ thống LLM mà không cần train model mới.

## Hạn chế / câu hỏi

- Speedup phụ thuộc acceptance rate.
- Draft model quá yếu sẽ bị reject nhiều.
- Cần quản lý đúng sampling để không làm đổi distribution.

## Câu hỏi review

1. Tại sao decoding autoregressive vốn tuần tự?
2. Draft model đóng vai trò gì?
3. Điều kiện nào làm speculative decoding hiệu quả?
