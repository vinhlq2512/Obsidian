---
type: reading-section
book: "[[Practical Natural Language Processing]]"
status: in_progress
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

- Phân loại chatbot theo FAQ bot, flow-based bot và open-ended bot.
- Vì sao FAQ bot và flow-based bot đều thuộc goal-oriented dialog, còn open-ended bot thiên về chitchat.
- Các thành phần của dialog system: intent/dialog act, slot/entity, state/context, policy, response.
- Vai trò của dialog manager và vì sao hệ này thường cần state để đi từng turn.
- Cách Dialogflow minh hoạ việc tạo bot thực tế bằng intent và entity.

## Định nghĩa quan trọng

- Chatbot: hệ thống cho phép người dùng tương tác bằng ngôn ngữ tự nhiên, thường qua text hoặc speech.
- FAQ bot: bot truy xuất câu trả lời cố định từ một tập câu hỏi/đáp án đã biết.
- Flow-based bot: bot có luồng hội thoại được định sẵn để thu thập đủ thông tin cho một mục tiêu.
- Open-ended bot: bot trò chuyện mở, không bám một flow hay template cố định.
- Goal-oriented dialog: hội thoại phục vụ một mục tiêu cụ thể như đặt pizza hay đặt vé.
- Chitchat: hội thoại mở, thiên về tự nhiên và giải trí hơn là hoàn thành task.
- Dialog act / intent: ý định của câu người dùng.
- Slot / entity: mẩu thông tin cụ thể cần trích ra để phục vụ intent.
- Dialog state / context: trạng thái hội thoại, gồm intent, slot đã có và lịch sử turn.
- Dialog manager / task manager: module quyết định bot nên hỏi thêm, xác nhận hay trả lời gì tiếp theo.
- Response generation: bước sinh câu trả lời cuối cùng ở dạng tự nhiên.
- Dialogflow: nền tảng xây conversational agent, dùng trong ví dụ pizza shop của chương.

## Mental model

```text
User utterance
-> intent / dialog act
-> slot extraction
-> dialog state
-> policy / action
-> response
```

```text
Speech input
-> speech recognition
-> NLU
-> dialog/task manager
-> NLG
-> speech synthesis
```

## A Pipeline for Building Dialog Systems

- `Speech recognition`: đổi tiếng nói thành text, là cửa vào của bot thoại.
- `NLU`: phân tích text đầu vào để lấy các tín hiệu như sentiment, named entity, coreference và các thông tin ngầm/hiển ngôn khác.
- `Dialog/task manager`: gom thông tin qua nhiều turn, giữ state, rồi quyết định hành động kế tiếp theo rule hoặc RL.
- `NLG`: sinh câu trả lời dạng tự nhiên theo action đã chọn.
- `Speech synthesis`: đổi text trả lời thành tiếng nói ở đầu ra.
- Luồng ý nghĩa của pipeline là: input từ người dùng không được trả lời ngay lập tức mà phải đi qua nhận dạng, hiểu, lưu trạng thái, chọn hành động rồi mới sinh câu trả lời.
- Trong mô hình này, `dialog manager` là nơi tích lũy thông tin của cuộc hội thoại và quyết định bot nên hỏi tiếp, xác nhận, gọi API hay trả lời dứt điểm.
- Với domain hẹp như đặt pizza, pipeline này giúp bot giữ được mục tiêu hội thoại thay vì phản hồi rời rạc theo từng câu.
- Với chatbot chỉ chạy trên text, có thể bỏ phần speech recognition và speech synthesis, nhưng luồng NLU -> dialog manager -> NLG vẫn là lõi.
- Phần quan trọng nhất của pipeline là dialog manager vì đây là nơi state được cập nhật và strategy được chọn.

## Deep Dive into Components of a Dialog System

- `Dialog act classification` là bài toán xác định một utterance đang làm vai trò gì trong ngữ cảnh hội thoại. Trong chapter, đây chính là phiên bản NLU của `intent detection`.
- Ví dụ các nhãn như `inform`, `request`, `yes/no question` cho thấy mục tiêu là phân loại vai trò của câu nói, chứ không chỉ đọc nghĩa bề mặt.
- `Slot identification` là bước trích entity/slot từ utterance, thường dùng sequence labeling để gắn giá trị như `cheaper` vào slot `price`.
- Chọn ontology cho slot rất quan trọng: với travel bot, destination có thể cần `city` hoặc `airport`; với restaurant bot, `city` có thể là đủ.
- Làm riêng intent detection và slot extraction bằng hai model tách biệt cần nhiều nhãn và có thể chậm khi deploy.
- Một hướng tốt hơn là `joint understanding and tracking`, tức gộp intent và slot vào một `dialog state` như `inform(price-cheap)` để dự đoán đồng thời.
- `Response generation` có ba kiểu: `fixed responses` cho FAQ bot, `template-based` cho câu trả lời có cấu trúc, và `automatic generation` cho phản hồi tự nhiên hơn.
- Template-based responses đặc biệt hữu ích cho câu hỏi làm rõ hoặc câu trả lời fact-driven vì vừa kiểm soát được vừa ít lỗi ngữ pháp hơn.
- Các dataset goal-oriented thường dùng để benchmark gồm ATIS, SNIPS, DSTC và MultiWOZ; single-domain thường dễ hơn multidomain.
- Với ATIS intent prediction, CNN là baseline hợp lý vì bắt n-gram, RNN bắt được phụ thuộc ngữ cảnh tốt hơn, còn BERT cho kết quả mạnh nhất trong ví dụ của sách.

## Phần cần biết

- FAQ bot thường trả lời theo kiểu tra cứu: câu hỏi có thể được diễn đạt nhiều cách, nhưng bot vẫn ánh xạ về cùng một câu trả lời cố định.
- Flow-based bot khác ở chỗ bot chủ động dẫn dắt người dùng qua các câu hỏi để điền đủ slot, ví dụ size, topping, món phụ khi đặt pizza.
- Open-ended bot không cần flow cố định nên khó hơn: phản hồi phải hợp ngữ cảnh, tự nhiên và bám chủ đề.
- Trong dialog system, dialog manager giữ vai trò trung tâm vì nó gom thông tin qua nhiều turn rồi mới quyết định action tiếp theo.
- Goal-oriented systems thường domain-specific, nên khó mở rộng tổng quát nếu không có chiến lược học dữ liệu hoặc framework tốt.
- Dialogflow trong ví dụ chapter cho thấy cách tạo agent, dùng intent/entity và tận dụng default fallback/welcome intent để khởi động bot.
- Với bot text-only, có thể bỏ speech recognition và speech synthesis, nhưng NLU + dialog manager + NLG vẫn là lõi.
- Failure modes cần nhớ: intent mơ hồ, slot thiếu, context drift, response lệch mục tiêu.
- Trục khó nhất của chapter này là cân bằng giữa kiểm soát và linh hoạt: fixed/template dễ kiểm soát, automatic generation tự nhiên hơn nhưng khó khóa hành vi.

## Câu hỏi review

1. FAQ bot khác goal-oriented dialog ở đâu?
2. Slot filling ảnh hưởng thế nào tới hành động tiếp theo của bot?
3. Vì sao human-in-the-loop quan trọng trong chatbot production?

## Gợi ý trả lời câu hỏi review

- FAQ bot chủ yếu làm truy xuất câu trả lời cố định từ một tập Q/A đã biết; mỗi lượt người dùng thường độc lập. Goal-oriented dialog thì theo đuổi một mục tiêu cụ thể qua nhiều turn, cần lưu trạng thái và thu đủ thông tin trước khi hoàn thành task.
- Slot filling quyết định bot đã đủ dữ liệu để đi tiếp hay chưa. Nếu còn slot thiếu, bot phải hỏi thêm; nếu slot đã đủ, dialog manager mới chuyển sang action như xác nhận đơn, gọi API hay sinh response cuối.
- Human-in-the-loop quan trọng vì chatbot thực tế luôn có câu nhập mơ hồ, ngoại lệ và lỗi nhận dạng. Con người giúp gắn nhãn lại dữ liệu, sửa flow, kiểm tra fallback và cải thiện bot khi domain hoặc hành vi người dùng thay đổi.

## Liên kết

- [[Practical Natural Language Processing]]
- [[Intent Detection]]
- [[Dialog System]]
- [[Dialog Act Classification]]
