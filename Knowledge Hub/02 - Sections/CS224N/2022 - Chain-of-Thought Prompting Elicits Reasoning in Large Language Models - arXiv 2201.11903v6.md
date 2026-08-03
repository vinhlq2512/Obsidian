---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2022 - Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
year: 2022
venue: "arXiv"
arxiv: "2201.11903v6"
source_file: "[[2022 - Chain-of-Thought Prompting Elicits Reasoning in Large Language Models - arXiv 2201.11903v6.pdf]]"
pages: 43
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

# 2022 - Chain-of-Thought Prompting Elicits Reasoning in Large Language Models - arXiv 2201.11903v6

## Nguồn

- PDF gốc: [[2022 - Chain-of-Thought Prompting Elicits Reasoning in Large Language Models - arXiv 2201.11903v6.pdf]]
- Vai trò trong CS224N: paper nền cho chain-of-thought prompting và reasoning traces trong LLM.

## Câu hỏi trung tâm

Prompt yêu cầu model viết các bước trung gian có giúp LLM giải bài reasoning tốt hơn không?

## Kiến thức cốt lõi

- Chain-of-thought prompting thêm reasoning examples có lời giải từng bước vào prompt.
- Kỹ thuật này đặc biệt hiệu quả hơn khi model đủ lớn.
- CoT giúp model phân rã bài toán phức tạp thành các bước nhỏ.
- Nó không đảm bảo reasoning trace đúng, nhưng thường cải thiện final answer ở arithmetic/commonsense reasoning.
- Paper mở đường cho reasoning prompting và inference-time reasoning.

## Cơ chế / công thức / kiến trúc

```text
question + examples có reasoning steps
-> model bắt chước format suy luận từng bước
-> sinh intermediate reasoning
-> đưa ra final answer
```

## Khi áp dụng

- Dùng cho bài toán cần nhiều bước suy luận.
- Không dùng CoT như bằng chứng tuyệt đối rằng model “hiểu”.
- Nên kết hợp verification/self-consistency khi độ đúng quan trọng.

## Kết quả / bằng chứng đáng giữ

- Title nêu CoT prompting elicits reasoning in large language models.
- Lecture 12/13 đặt CoT trong cụm reasoning và decoding.
- Self-consistency paper sau đó mở rộng CoT bằng sampling nhiều reasoning paths.

## Cách hiểu bằng lời của tôi

CoT là cách dùng prompt để cho model thêm “không gian làm nháp”. Nhưng nháp nghe hợp lý vẫn có thể sai, nên cần kiểm tra kết quả.

## Câu hỏi review

1. CoT prompting thay đổi prompt như thế nào?
2. Vì sao CoT hiệu quả hơn ở model lớn?
3. CoT trace có phải bằng chứng reasoning đúng không?

## Liên kết

- [[Prompt Engineering]]
- [[Large Language Model]]
- [[Self-Consistency Decoding]]
- [[Test-Time Compute]]
- [[CS224N]]
