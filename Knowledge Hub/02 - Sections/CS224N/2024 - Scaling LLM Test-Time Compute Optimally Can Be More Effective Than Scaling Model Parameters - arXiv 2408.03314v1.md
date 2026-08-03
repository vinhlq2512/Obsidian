---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2024 - Scaling LLM Test-Time Compute Optimally Can Be More Effective Than Scaling Model Parameters"
year: 2024
venue: "arXiv"
arxiv: "2408.03314v1"
source_file: "[[2024 - Scaling LLM Test-Time Compute Optimally Can Be More Effective Than Scaling Model Parameters - arXiv 2408.03314v1.pdf]]"
pages: 37
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[NLP]]"
tags:
  - cs224n
  - paper
---

# 2024 - Scaling LLM Test-Time Compute Optimally Can Be More Effective Than Scaling Model Parameters - arXiv 2408.03314v1

## Nguồn

- PDF gốc: [[2024 - Scaling LLM Test-Time Compute Optimally Can Be More Effective Than Scaling Model Parameters - arXiv 2408.03314v1.pdf]]
- Vai trò trong CS224N: paper về inference-time scaling/test-time compute cho reasoning.

## Câu hỏi trung tâm

Khi có thêm compute, nên tăng model size hay dùng thêm compute lúc inference để đạt kết quả tốt hơn?

## Kiến thức cốt lõi

- Test-time compute là compute dùng sau khi model đã train, ví dụ sampling nhiều lời giải, search, verification.
- Trong một số regime, scale compute lúc inference có thể hiệu quả hơn tăng parameter count.
- Cần tối ưu cách phân bổ compute theo độ khó bài toán.
- Paper liên hệ trực tiếp với self-consistency, verifier và reasoning models.
- Đây là nền cho lecture reasoning và small LM smart scaling.

## Cơ chế / công thức / kiến trúc

```text
model cố định
-> sinh nhiều candidates / reasoning traces
-> score bằng verifier/reward/model
-> chọn hoặc refine answer
-> tăng chất lượng bằng compute lúc test
```

## Khi áp dụng

- Dùng cho tasks mà answer quality quan trọng hơn latency.
- Cần chính sách adaptive: bài dễ dùng ít compute, bài khó dùng nhiều compute.
- Không miễn phí: tăng latency và cost inference.

## Kết quả / bằng chứng đáng giữ

- Title nói test-time compute có thể hiệu quả hơn scaling parameters.
- Lecture 12/13/19 đều nhấn mạnh inference-time scaling.
- Self-consistency và step-by-step verification là ví dụ cụ thể.

## Cách hiểu bằng lời của tôi

Thay vì làm model não to hơn, ta có thể cho nó nhiều thời gian suy nghĩ hơn. Nhưng thời gian đó phải được tổ chức bằng sampling/search/verification.

## Câu hỏi review

1. Test-time compute gồm những kỹ thuật nào?
2. Vì sao adaptive compute quan trọng?
3. Trade-off chính của inference-time scaling là gì?

## Liên kết

- [[Test-Time Compute]]
- [[Self-Consistency Decoding]]
- [[Speculative Decoding]]
- [[Prompt Engineering]]
- [[CS224N]]
