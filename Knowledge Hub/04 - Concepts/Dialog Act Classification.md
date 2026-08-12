---
type: concept
status: understood
sources:
  - "[[Practical NLP - Chapter 06 - Chatbots]]"
source_sections:
  - "[[Practical NLP - Chapter 06 - Chatbots]]"
first_seen: 2026-08-11
last_updated: 2026-08-11
tags:
  - concept
  - nlp
  - dialog-systems
---

# Dialog Act Classification

## Định nghĩa

Dialog act classification là bài toán phân loại vai trò của một câu nói trong ngữ cảnh hội thoại. Thay vì chỉ hỏi câu này "nói về cái gì", ta hỏi câu này đang làm hành động gì trong cuộc hội thoại.

Ví dụ nhãn có thể là:

- `inform`
- `request`
- `yes/no question`

## Trực giác

Một utterance trong dialog không chỉ mang nghĩa từ vựng, mà còn mang chức năng hội thoại. Cùng một ý tưởng bề mặt, nhưng trong ngữ cảnh khác nhau nó có thể là hỏi, xác nhận, cung cấp thông tin hoặc yêu cầu hành động.

## Cách hiểu bằng lời của tôi

Dialog act classification gần với [[Intent Detection]], nhưng nhấn mạnh vai trò của câu nói trong cuộc hội thoại hơn là chỉ nhãn ý định của người dùng. Nó là cách bot hiểu "người dùng đang làm gì ở lượt này" để quyết định bước tiếp theo.

## Khi nào dùng?

- Khi xây chatbot goal-oriented.
- Khi cần hiểu ý định theo từng turn của hội thoại.
- Khi muốn kết hợp với slot extraction để tạo dialog state.

## Liên hệ

- [[Dialog System]]
- [[Intent Detection]]

