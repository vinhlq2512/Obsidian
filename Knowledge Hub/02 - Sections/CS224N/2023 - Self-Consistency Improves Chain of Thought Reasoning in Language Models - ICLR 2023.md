---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2023 - Self-Consistency Improves Chain of Thought Reasoning in Language Models"
year: 2023
venue: "ICLR 2023"
arxiv: ""
source_file: "[[2023 - Self-Consistency Improves Chain of Thought Reasoning in Language Models - ICLR 2023.pdf]]"
pages: 24
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Large Language Model]]"
  - "[[Autoregressive Language Model]]"
  - "[[Prompt Engineering]]"
tags:
  - cs224n
  - paper
---

# 2023 - Self-Consistency Improves Chain of Thought Reasoning in Language Models - ICLR 2023

## Nguồn

- PDF gốc: [[2023 - Self-Consistency Improves Chain of Thought Reasoning in Language Models - ICLR 2023.pdf]]
- Vai trò trong CS224N: paper về self-consistency như decoding strategy cho chain-of-thought reasoning.

## Câu hỏi trung tâm

Thay vì dùng một greedy reasoning path, lấy mẫu nhiều reasoning paths rồi chọn đáp án nhất quán có cải thiện reasoning không?

## Kiến thức cốt lõi

- Self-consistency thay greedy decoding trong CoT bằng sampling nhiều lời giải.
- Sau đó marginalize/chọn answer xuất hiện nhất quán nhất.
- Trực giác: bài toán phức tạp có nhiều đường suy luận khác nhau dẫn tới cùng đáp án đúng.
- Kỹ thuật cải thiện trên arithmetic và commonsense reasoning benchmarks.
- Đây là ví dụ rõ của test-time compute cho reasoning.

## Cơ chế / công thức / kiến trúc

```text
prompt CoT
-> sample nhiều reasoning paths
-> lấy final answer từ mỗi path
-> vote / marginalize answers
-> chọn answer consistent nhất
```

## Khi áp dụng

- Dùng khi model có khả năng sinh nhiều lời giải nhưng một lời giải đơn lẻ nhiễu.
- Tăng accuracy đổi lại tăng inference cost.
- Không đảm bảo đúng nếu nhiều path cùng sai do bias chung.

## Kết quả / bằng chứng đáng giữ

- Abstract nói thay greedy decoding bằng self-consistency.
- Source nêu gains trên GSM8K, SVAMP, AQuA, StrategyQA và ARC-challenge.
- Lecture reasoning đặt self-consistency trong nhóm decoding/test-time reasoning.

## Cách hiểu bằng lời của tôi

Self-consistency giống hỏi model nhiều lần rồi xem đáp án nào hội tụ. Nó tận dụng sự đa dạng của sampling để giảm rủi ro một trajectory sai.

## Câu hỏi review

1. Self-consistency thay đổi bước decoding nào của CoT?
2. Vì sao nhiều reasoning paths có thể tốt hơn một path?
3. Trade-off compute của self-consistency là gì?

## Liên kết

- [[Self-Consistency Decoding]]
- [[Prompt Engineering]]
- [[Test-Time Compute]]
- [[Top-k Sampling]]
- [[Nucleus Sampling]]
- [[CS224N]]
