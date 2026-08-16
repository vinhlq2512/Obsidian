---
type: concept
status: developing
sources:
  - "[[CS224N 2026 - Lecture 16 - AIs Impact on Humanity]]"
  - "[[2026-05-30_how-doordash-built-a-testing-system-to-evaluate-llms]]"
source_sections:
  - "[[CS224N 2026 - Lecture 16 - AIs Impact on Humanity]]"
first_seen: 2026-08-02
last_updated: 2026-08-16
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
- Thiết kế context có cấu trúc, ví dụ case state, để model không phải tự suy diễn trạng thái ẩn.
- Dùng simulation/eval để phát hiện failure mode trước khi gặp user thật, nhưng không nhầm eval với bằng chứng tuyệt đối.

## Từ ByteByteGo

Trong case DoorDash, hallucination được xử lý như lỗi hệ thống chứ không chỉ là lỗi prompt. Họ mô phỏng hội thoại, dùng backend giả lập, cho LLM-as-judge chấm theo rubric và cấu trúc lại context thành case state. Bài học chính: giảm hallucination cần cả [[LLM Evaluation]], context tốt và vòng lặp cải tiến, không chỉ "nhắc model đừng bịa".

## Liên kết

- [[Large Language Model]]
- [[Retrieval-Augmented Generation]]
- [[Context Engineering]]
- [[LLM Evaluation]]
- [[Measuring the Quality of Generated Text]]
- [[LLM Agent]]
- [[CS224N]]
