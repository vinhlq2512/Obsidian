---
type: course-source
course: "[[CS224N]]"
status: developing
source_type: lecture
title: "CS224N 2026 - Lecture 11 - Evaluation"
year: 2026
venue: ""
arxiv: ""
source_file: "[[CS224N 2026 - Lecture 11 - Evaluation.pdf]]"
pages: 77
created_at: 2026-08-02
updated_at: 2026-08-02
related_concepts:
  - "[[Measuring the Quality of Generated Text]]"
tags:
  - cs224n
  - lecture
---

# CS224N 2026 - Lecture 11 - Evaluation

## Nguồn

- PDF gốc: [[CS224N 2026 - Lecture 11 - Evaluation.pdf]]
- Vai trò trong khoá: cách thiết kế benchmark/metric cho LLM và rủi ro khi leaderboard dẫn dắt nghiên cứu.
- Paper đọc kèm: [[2023 - Holistic Evaluation of Language Models - TMLR 2023]], [[2021 - Measuring Massive Multitask Language Understanding - arXiv 2009.03300v3]], [[2025 - Multimodal RewardBench - Holistic Evaluation of Reward Models for Vision Language Models - arXiv 2502.14191v1]].

## Mục tiêu cần hiểu

- Benchmark đo cái gì và không đo cái gì.
- Vì sao benchmark có shelf-life ngắn khi model frontier tiến nhanh.
- Khác biệt giữa reference-based/reference-free và model-free/model-based metrics.
- Vì sao human evaluation cũng có bias và giới hạn.

## Ý chính

- Benchmarks và leaderboards thúc đẩy tiến bộ nhưng cũng làm model tối ưu hoá theo bài test hơn là năng lực thật.
- Khi model vượt human ceiling trên benchmark cũ, benchmark mất khả năng phân biệt.
- Multi-task benchmarks như GLUE/SuperGLUE cố đo năng lực ngôn ngữ chung, nhưng vẫn phụ thuộc thiết kế task và phân phối dữ liệu.
- Dynamic/adversarial benchmarks tìm cách giảm overfitting và kiểm tra failure modes mới.
- Evaluation của LLM cần xem cả correctness, robustness, calibration, safety, bias, reasoning process và user preference.

## Trục thiết kế metric

| Câu hỏi | Lựa chọn |
| --- | --- |
| Có đáp án tham chiếu không? | reference-based vs reference-free |
| Ai chấm? | human, rule, model judge |
| Đo output hay quá trình? | final answer vs reasoning/tool trajectory |
| Đo task hẹp hay năng lực rộng? | single-task vs holistic benchmark |

## Failure modes của evaluation

- Data contamination: model đã thấy test set trong training.
- Benchmark saturation: mọi model mạnh đều đạt điểm cao, không phân biệt được nữa.
- Metric mismatch: điểm tự động cao nhưng trải nghiệm người dùng thấp.
- Model-as-judge bias: judge ưu ái style, độ dài, hoặc model cùng họ.
- Human eval noise: người chấm không nhất quán, rubric mơ hồ.

## Cách hiểu bằng lời của tôi

Evaluation không phải bước phụ sau khi train xong. Nó định nghĩa ta đang gọi “tiến bộ” là gì. Nếu metric lệch, cả hệ thống sẽ học cách thắng metric thay vì giải quyết vấn đề thật.

## Câu hỏi review

1. Vì sao benchmark có thể hết hữu dụng dù vẫn chạy được?
2. Reference-free metric cần trong trường hợp nào?
3. Model-as-judge có rủi ro gì?
4. Benchmark saturation khác data contamination thế nào?
5. Vì sao evaluation của agent/RAG cần đo nhiều hơn final answer?

## Liên kết

- [[Measuring the Quality of Generated Text]]
- [[Exact Match]]
- [[F1 Score]]
- [[ROUGE]]
- [[BLEU]]
- [[Evaluating the Retriever]]
- [[Evaluating the Reader]]
- [[CS224N]]
