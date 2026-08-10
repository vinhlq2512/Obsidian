---
type: reading-section
book: "[[Practical Natural Language Processing]]"
status: summarized
chapter: 1
start_page: 44
end_page: 101
reading_date: 2026-08-04
planned_sessions:
  - "Tự note nền | 44-101 | Không nằm trong daily reading | 0 phút"
tags:
  - nlp
  - practical-nlp
---

# Practical NLP - Chapter 01 - NLP A Primer

## Mục tiêu cần hiểu

- NLP giải quyết những loại bài toán thực tế nào.
- Vì sao ngôn ngữ tự nhiên khó xử lý bằng máy.
- Khác biệt giữa heuristic-based NLP, machine learning cho NLP và deep learning cho NLP.
- Conversational agent cho thấy pipeline NLP thực tế như thế nào.

## Tóm tắt nền đã tự note

- NLP trong thực tế xuất hiện trong email, voice assistant, search, customer support, recommendation, translation và nhiều workflow sản phẩm khác. Vì vậy khi học NLP nên bắt đầu từ use case, không bắt đầu từ model.
- Một task NLP nên được nhìn bằng cặp input-output: input là text/speech/document/context; output có thể là label, entity, ranking, summary, translation, answer hoặc action.
- Ngôn ngữ khó vì có nhiều tầng: âm thanh/ký tự, từ, hình thái, cú pháp, ngữ nghĩa, diễn ngôn, ngữ cảnh và common sense. Cùng một câu có thể đổi nghĩa theo domain, người nói và tình huống.
- Ba hướng tiếp cận chính là heuristic, ML và DL. Heuristic dễ giải thích và có ích khi domain rõ; ML cần feature/label; DL học representation mạnh hơn nhưng cần dữ liệu, compute và kiểm soát lỗi tốt hơn.
- Conversational agent là ví dụ tốt vì nó buộc kết hợp nhiều phần: intent, entity/slot, dialog state, policy, response và fallback.

## Liên kết concept

- [[Language AI]]
- [[NLP Pipeline]]
- [[Text Classification]]
- [[Named Entity Recognition]]
- [[Intent Detection]]

## Mental model

```text
Use case thực tế
-> task NLP cụ thể
-> dữ liệu ngôn ngữ nhiều nhiễu
-> heuristic / ML / DL
-> evaluation theo sản phẩm
-> vòng lặp sửa lỗi
```

## Phần cần biết

- NLP không chỉ là model; nó là quá trình biến dữ liệu ngôn ngữ lộn xộn thành quyết định hoặc trải nghiệm sản phẩm.
- Chapter này là bản đồ khởi động để đọc Part II: classification, information extraction và chatbot.

## Câu hỏi review

1. Một bài toán NLP thực tế khác gì một benchmark NLP?
2. Vì sao language ambiguity làm NLP khó hơn dữ liệu có cấu trúc?
3. Khi nào heuristic vẫn đáng dùng thay vì model học máy?

## Gợi ý trả lời câu hỏi review

- **Một bài toán NLP thực tế khác benchmark NLP**: Bài toán thực tế phải cân nhắc giới hạn phần cứng, chi phí huấn luyện/vận hành, tính giải thích được và sự thiếu hụt dữ liệu. Benchmark thường có sẵn dữ liệu sạch, lớn và chỉ tập trung vào metric.
- **Language ambiguity làm NLP khó**: Máy tính khó phân biệt được ý nghĩa thực sự nếu chỉ dựa vào cú pháp vì giải quyết sự mơ hồ cần context và common knowledge. Dữ liệu có cấu trúc thường có định nghĩa cột/trường rõ ràng hơn.
- **Khi nào heuristic đáng dùng**: Khi không có đủ training data, domain quá đặc thù, cần độ tin cậy/tính giải thích cao, hoặc dùng làm baseline và guardrail cho model học máy.

## Liên kết

- [[Practical Natural Language Processing]]
- [[Practical NLP - Chapter 02 - NLP Pipeline]]
