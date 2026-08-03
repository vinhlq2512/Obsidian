---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: lecture
title: "CS224N 2026 - Lecture 12 - Reasoning Part 1"
year: 2026
venue: ""
arxiv: ""
source_file: "[[CS224N 2026 - Lecture 12 - Reasoning Part 1.pdf]]"
pages: 68
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
# CS224N 2026 - Lecture 12 - Reasoning Part 1

## Nguồn

- PDF gốc: [[CS224N 2026 - Lecture 12 - Reasoning Part 1.pdf]]
- Vai trò trong khoá: decoding, neural text degeneration, DeepSeek-R1, PPO/GRPO/DAPO và bản chất reasoning.
- Paper đọc kèm: [[2025 - DeepSeek-R1 - Incentivizing Reasoning Capability in LLMs via Reinforcement Learning - arXiv 2501.12948v2]], [[2025 - DAPO - An Open-Source LLM Reinforcement Learning System at Scale - arXiv 2503.14476v2]], [[2024 - Scaling LLM Test-Time Compute Optimally Can Be More Effective Than Scaling Model Parameters - arXiv 2408.03314v1]].

## Mục tiêu cần hiểu

- Decoding algorithm biến phân phối token thành chuỗi output.
- Greedy, beam search và sampling tạo hành vi rất khác nhau.
- Reasoning model hiện đại dùng RL/test-time compute để cải thiện lời giải.
- RL cho reasoning có thể tạo năng lực nhưng cũng làm evaluation/phân tích phức tạp hơn.

## Ý chính

- Greedy decoding chọn token xác suất cao nhất ở từng bước, nhanh nhưng myopic.
- Beam search giữ top-k hypotheses, tốt cho một số mô hình cổ điển nhưng thường kém đa dạng và không còn mặc định cho LLM hiện đại.
- Sampling chấp nhận stochasticity để tạo output tự nhiên hơn và tránh degeneration trong generation mở.
- Reasoning không chỉ là decoding; nó liên quan tới training signal, process supervision, reward design và inference-time compute.
- DeepSeek-R1/R1-Zero cho thấy RL có thể khuyến khích reasoning traces, nhưng cần hiểu rõ reward và data pipeline.

## Decoding cơ bản

```text
logits
-> softmax distribution over vocabulary
-> decoding algorithm chọn token
-> append token vào context
-> lặp đến stop condition
```

So sánh:

| Thuật toán | Cách chọn | Điểm mạnh | Điểm yếu |
| --- | --- | --- | --- |
| Greedy | token xác suất cao nhất | nhanh, deterministic | dễ mắc local optimum |
| Beam search | giữ k chuỗi tốt nhất | tìm sequence có xác suất cao hơn | ít đa dạng, đắt hơn |
| Sampling | lấy mẫu từ phân phối | đa dạng, hợp open-ended generation | có variance, cần kiểm soát |

## Reasoning và RL

RL cho reasoning thường không chỉ thưởng đáp án cuối, mà có thể tác động tới cách model khám phá lời giải. Các biến thể như PPO, GRPO, DAPO tìm cách tối ưu policy dưới reward nhưng giảm chi phí/độ phức tạp khác nhau.

Điểm cần giữ: nếu reward chỉ đo output cuối, model có thể học shortcut; nếu reward/process signal tốt hơn, model có khả năng học chiến lược giải bài ổn định hơn.

## Cách hiểu bằng lời của tôi

Decoding là lúc “tính cách” của phân phối được bộc lộ. Cùng một model, greedy có thể khô và mắc kẹt; sampling có thể sáng tạo nhưng rủi ro. Với reasoning, vấn đề không chỉ là chọn token, mà là tạo điều kiện để model tiêu thêm compute đúng chỗ và được reward cho quá trình giải có ích.

## Câu hỏi review

1. Vì sao greedy decoding myopic?
2. Khi nào beam search giảm về greedy decoding?
3. Vì sao sampling từng được xem là bất ngờ với GPT-2?
4. Test-time compute giúp reasoning theo nghĩa nào?
5. Reward thiết kế sai có thể gây lỗi gì?

## Liên kết

- [[Greedy Decoding]]
- [[Beam Search Decoding]]
- [[Top-k Sampling]]
- [[Nucleus Sampling]]
- [[Text Generation]]
- [[Prompt Engineering]]
- [[CS224N]]
