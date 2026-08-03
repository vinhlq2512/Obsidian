---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2023 - Holistic Evaluation of Language Models"
year: 2023
venue: "TMLR 2023"
arxiv: ""
source_file: "[[2023 - Holistic Evaluation of Language Models - TMLR 2023.pdf]]"
pages: 162
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Large Language Model]]"
  - "[[Autoregressive Language Model]]"
  - "[[Measuring the Quality of Generated Text]]"
tags:
  - cs224n
  - paper
---

# 2023 - Holistic Evaluation of Language Models - TMLR 2023

## Nguồn

- PDF gốc: [[2023 - Holistic Evaluation of Language Models - TMLR 2023.pdf]]
- Vai trò trong CS224N: paper nền cho HELM và đánh giá LLM đa chiều.

## Câu hỏi trung tâm

Làm thế nào đánh giá language models một cách holistic thay vì chỉ bằng accuracy trên vài benchmark?

## Kiến thức cốt lõi

- HELM nhấn mạnh coverage rộng về scenarios, metrics và models.
- Evaluation cần đo accuracy, calibration, robustness, fairness, bias, toxicity, efficiency và nhiều khía cạnh khác.
- Một model có thể tốt ở metric này nhưng kém ở metric khác.
- Holistic evaluation giúp tránh leaderboard đơn chiều.
- Paper là nguồn chính cho Lecture 11 về benchmark pitfalls.

## Cơ chế / công thức / kiến trúc

```text
scenarios x models x metrics
-> chạy evaluation chuẩn hoá
-> phân tích trade-off đa chiều
-> không gom mọi thứ thành một điểm duy nhất nếu mất thông tin
```

## Khi áp dụng

- Dùng khi chọn model cho production hoặc research.
- Đừng chỉ nhìn accuracy; kiểm tra robustness/safety/cost.
- Cần rõ scenario nào quan trọng với use case.

## Kết quả / bằng chứng đáng giữ

- Title nêu holistic evaluation of language models.
- Lecture 11 đặt câu hỏi what/how to evaluate và pitfalls của benchmark.
- HELM trở thành ví dụ tiêu biểu cho evaluation đa chiều.

## Cách hiểu bằng lời của tôi

Đánh giá LLM giống kiểm tra một hệ thống phức tạp: điểm trung bình đẹp không nói hết model thất bại ở đâu.

## Câu hỏi review

1. Holistic evaluation khác leaderboard đơn metric ra sao?
2. Vì sao cần nhiều scenario?
3. Một model tốt accuracy nhưng kém calibration gây rủi ro gì?

## Liên kết

- [[Measuring the Quality of Generated Text]]
- [[Large Language Model]]
- [[AI Hallucination]]
- [[CS224N]]
