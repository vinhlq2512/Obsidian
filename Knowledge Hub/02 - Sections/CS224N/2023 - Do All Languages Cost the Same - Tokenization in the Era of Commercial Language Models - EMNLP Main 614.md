---
type: course-source
course: "[[CS224N]]"
status: completed
source_type: paper
title: "2023 - Do All Languages Cost the Same - Tokenization in the Era of Commercial Language Models"
year: 2023
venue: "EMNLP"
arxiv: ""
source_file: "[[2023 - Do All Languages Cost the Same - Tokenization in the Era of Commercial Language Models - EMNLP Main 614.pdf]]"
pages: 20
created_at: 2026-08-02
updated_at: 2026-08-03
completed_at: 2026-08-03
related_concepts:
  - "[[Tokenization]]"
  - "[[Large Language Model]]"
  - "[[Autoregressive Language Model]]"
tags:
  - cs224n
  - paper
---

# 2023 - Do All Languages Cost the Same - Tokenization in the Era of Commercial Language Models - EMNLP Main 614

## Nguồn

- PDF gốc: [[2023 - Do All Languages Cost the Same - Tokenization in the Era of Commercial Language Models - EMNLP Main 614.pdf]]
- Vai trò trong CS224N: paper về tokenization fairness và chi phí giữa các ngôn ngữ trong LLM thương mại.

## Câu hỏi trung tâm

Các ngôn ngữ khác nhau có bị tokenization làm tốn token/chi phí khác nhau không?

## Kiến thức cốt lõi

- Commercial LLMs tính chi phí và context theo token, không theo số từ hay số ký tự người dùng cảm nhận.
- Tokenizer thiên về ngôn ngữ high-resource có thể làm ngôn ngữ khác bị chia nhỏ hơn.
- Nếu cùng một nội dung cần nhiều token hơn, người dùng trả chi phí cao hơn và bị giới hạn context nặng hơn.
- Tokenization vì vậy là vấn đề fairness, access và multilingual quality.
- Paper nối trực tiếp với Lecture 14 về multilingual tokenization.

## Cơ chế / công thức / kiến trúc

```text
text ở nhiều ngôn ngữ
-> tokenizer của LLM
-> số token khác nhau cho cùng lượng thông tin
-> khác biệt chi phí, latency, context budget
```

## Khi áp dụng

- Khi xây app đa ngôn ngữ, đo token cost theo từng ngôn ngữ thật.
- Không giả định một tokenizer tối ưu cho tiếng Anh sẽ công bằng cho mọi ngôn ngữ.
- Cần đưa tokenization vào đánh giá product và model fairness.

## Kết quả / bằng chứng đáng giữ

- Title trực tiếp hỏi liệu mọi ngôn ngữ có cùng cost không.
- Lecture 14 nhấn mạnh multilingual tokenization và fairness.
- Vấn đề cost theo token là đặc thù thực tế của commercial LLMs.

## Cách hiểu bằng lời của tôi

Tokenizer có thể biến một ngôn ngữ thành “đắt hơn” dù người dùng viết cùng lượng ý nghĩa. Đây là bias hạ tầng, không chỉ bias output.

## Câu hỏi review

1. Vì sao token count ảnh hưởng tới fairness?
2. Ngôn ngữ low-resource có thể chịu bất lợi gì từ tokenizer?
3. Đo tokenization cost nên làm ở mức nào?

## Liên kết

- [[Tokenization]]
- [[BPE]]
- [[Multilingual Transformer]]
- [[Cross-Lingual Transfer]]
- [[CS224N]]
