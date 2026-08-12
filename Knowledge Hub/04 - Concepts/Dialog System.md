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

# Dialog System

## Định nghĩa

Dialog system là hệ thống xử lý hội thoại theo từng turn để hiểu người dùng, giữ ngữ cảnh, quyết định hành động tiếp theo và sinh phản hồi phù hợp.

## Cấu trúc cốt lõi

```text
User utterance
-> intent / dialog act
-> slot extraction
-> dialog state / context
-> policy / action
-> response generation
```

Với bot thoại, pipeline thường mở rộng thêm:

```text
Speech input
-> speech recognition
-> NLU
-> dialog manager
-> NLG
-> speech synthesis
```

## Thành phần cần nhớ

- `intent` hoặc `dialog act`: người dùng đang muốn làm gì.
- `slot` hoặc `entity`: thông tin cụ thể cần trích ra để phục vụ intent.
- `dialog state`: các giá trị đã biết của cuộc hội thoại ở thời điểm hiện tại.
- `context`: state cộng với lịch sử các turn trước.
- `dialog manager`: module quyết định nên hỏi thêm, xác nhận hay gọi action nào tiếp theo.
- `response generator`: sinh câu trả lời cuối cùng cho người dùng.

## Deep dive theo chapter

- `Dialog act classification` là bài toán phân loại vai trò của utterance trong hội thoại, và trong chapter nó được xem như phiên bản dialog-specific của [[Intent Detection]].
- `Slot identification` thường dùng sequence labeling để gắn entity/slot vào từng span trong câu, rồi chuyển giá trị đó vào state.
- `Joint understanding and tracking` là hướng gộp intent và slot vào một biểu diễn dialog state duy nhất, ví dụ `inform(price-cheap)`.
- `Response generation` có ba mức: fixed responses, template-based responses và automatic generation.
- Fixed responses phù hợp FAQ bot; template-based phù hợp clarifying question hoặc câu trả lời fact-driven; automatic generation phù hợp khi muốn tự nhiên hơn nhưng khó kiểm soát hơn.
- Các model cho dialog thường cần cân bằng giữa độ chính xác, chi phí nhãn và độ nặng khi triển khai.

## Cách hiểu bằng lời của tôi

Dialog system không chỉ là trả lời câu hỏi. Nó là một vòng lặp: hiểu câu hiện tại, ghép nó với những gì đã biết từ các turn trước, rồi quyết định bước tiếp theo để tiến gần tới mục tiêu của người dùng.

Phần khó nhất là không chỉ hiểu text, mà còn phải biến nó thành state có thể điều khiển được: intent nào, slot nào còn thiếu, nên hỏi tiếp hay đã đủ để trả lời.

## Khi áp dụng

- FAQ bot.
- Flow-based bot như đặt pizza, đặt vé, đặt lịch.
- Hệ thống cần thu thập slot theo nhiều lượt hội thoại.
- Bot có fallback hoặc handoff sang người thật.
- Hệ goal-oriented cần NLU rõ ràng và dialog manager có khả năng giữ state.

## Liên kết

- [[Practical NLP - Chapter 06 - Chatbots]]
- [[Intent Detection]]
- [[Dialog Act Classification]]
