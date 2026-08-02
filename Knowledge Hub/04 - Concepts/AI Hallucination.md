---
type: concept
status: developing
sources:
  - "[[CS224N 2026 - Lecture 16 - AIs Impact on Humanity]]"
source_sections:
  - "[[CS224N 2026 - Lecture 16 - AIs Impact on Humanity]]"
first_seen: 2026-08-02
last_updated: 2026-08-02
tags:
  - concept
  - llm
  - evaluation
  - cs224n
---

# AI Hallucination

## Định nghĩa

AI hallucination là hiện tượng model sinh thông tin nghe hợp lý nhưng sai, không được nguồn hỗ trợ, hoặc bịa metadata/citation/fact.

## Cách hiểu bằng lời của tôi

LLM tối ưu để sinh chuỗi có xác suất cao trong context, không tự động đảm bảo chuỗi đó có provenance thật. Vì vậy câu trả lời có thể rất tự tin, đúng format, nhưng vẫn không đúng sự thật.

## Dạng lỗi quan trọng

- Bịa citation hoặc paper không tồn tại.
- Sai tên tác giả, năm, venue, DOI hoặc arXiv ID.
- Trộn thông tin từ nhiều nguồn thành một claim sai.
- Trả lời vượt quá evidence trong context.
- Tạo reasoning trace nghe hợp lý nhưng không dẫn tới kết luận đúng.

## Cách giảm rủi ro

- Dùng [[Retrieval-Augmented Generation]] với evidence rõ ràng.
- Kiểm tra citation bằng nguồn độc lập.
- Tách bước generate và verify.
- Đánh giá bằng rubric có kiểm tra factuality, không chỉ fluency.

## Liên kết

- [[Large Language Model]]
- [[Retrieval-Augmented Generation]]
- [[Measuring the Quality of Generated Text]]
- [[LLM Agent]]
- [[CS224N]]
