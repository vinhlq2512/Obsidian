---
type: reading-section
book: "[[Practical Natural Language Processing]]"
status: planned
chapter: 6
start_page: 356
end_page: 425
reading_date: 2026-08-10
planned_sessions:
  - "2026-08-10 | 356-375 | Chatbot taxonomy, FAQ, goal-oriented dialog | 55 phút"
  - "2026-08-11 | 376-400 | Dialog state, slots, response generation | 55 phút"
  - "2026-08-12 | 401-425 | End-to-end dialog, RL, human-in-the-loop, Rasa | 55 phút"
tags:
  - nlp
  - practical-nlp
  - chatbot
---

# Practical NLP - Chapter 06 - Chatbots

## Mục tiêu cần hiểu

- Phân loại chatbot theo FAQ, goal-oriented dialog và chitchat.
- Các thành phần của dialog system: intent, slot, state, policy, response.
- Vai trò của human-in-the-loop và framework như Rasa trong hệ thống thực tế.

## Định nghĩa quan trọng

- Chatbot
- Goal-oriented dialog
- Chitchat
- Dialog act classification
- Slot filling
- Response generation
- Human-in-the-loop
- Rasa NLU

## Mental model

```text
User utterance
-> intent / dialog act
-> slot extraction
-> dialog state
-> policy / action
-> response
```

## Phần cần biết

- Chatbot thực tế không chỉ là sinh câu trả lời; nó là quản lý trạng thái, ràng buộc task và fallback.
- Nên chú ý các failure modes: intent mơ hồ, slot thiếu, context drift, hallucinated response.

## Câu hỏi review

1. FAQ bot khác goal-oriented dialog ở đâu?
2. Slot filling ảnh hưởng thế nào tới hành động tiếp theo của bot?
3. Vì sao human-in-the-loop quan trọng trong chatbot production?

## Gợi ý trả lời câu hỏi review

- Trả lời bằng một flow đặt pizza hoặc recipe recommendation như chapter gợi ý.

## Liên kết

- [[Practical Natural Language Processing]]
- [[Intent Detection]]
