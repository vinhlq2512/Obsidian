---
type: reading-section
book: "[[Hands-On Large Language Models]]"
status: not-started
chapter: 7
start_page: 280
end_page: 314
estimated_minutes: 85
need_review: true
tags:
  - llm
  - agents
  - langchain
---

# Hands-On LLM - Chapter 07 - Advanced Text Generation Techniques and Tools

## Mục tiêu cần hiểu

- Hiểu framework như LangChain giúp nối model, prompt, memory, tools và chains.
- Nắm chain là cách ghép nhiều bước xử lý LLM thành pipeline.
- Phân biệt conversation buffer, windowed buffer và conversation summary memory.
- Hiểu agent dùng reasoning từng bước để chọn hành động/tool.
- Biết ReAct kết hợp reasoning và acting trong một vòng lặp.

## Định nghĩa quan trọng

- **Chain**: chuỗi bước xử lý, thường gồm prompt template, model call và parser/tool.
- **Prompt template**: khuôn prompt có biến để tái sử dụng.
- **Memory**: cơ chế giữ context hội thoại hoặc tóm tắt lịch sử.
- **Agent**: hệ thống dùng LLM để quyết định bước tiếp theo và gọi tool.
- **ReAct**: pattern kết hợp reasoning và action để giải quyết task nhiều bước.

## Mental model

LLM đơn lẻ chỉ là một thành phần. Ứng dụng thật cần nối nhiều mảnh: input, prompt, model, output parser, memory, retrieval, tool và error handling. Chain làm pipeline ổn định hơn. Agent linh hoạt hơn nhưng khó kiểm soát hơn.

## Phần cần biết

- Memory giúp hội thoại có ngữ cảnh nhưng tăng token cost.
- Summary memory giảm token nhưng có thể làm mất chi tiết.
- Agent mạnh khi cần tool use, search, calculator, database hoặc nhiều bước động.
- Agent cần guardrails vì model có thể chọn tool sai hoặc tạo kế hoạch kém.

## Khi áp dụng

- Dùng chain khi workflow rõ và lặp lại.
- Dùng agent khi workflow không biết trước hoặc cần chọn tool linh hoạt.
- Với production, ưu tiên pipeline đơn giản trước khi dùng agent.

## Câu hỏi review

1. Chain khác agent ở điểm nào?
2. Memory kiểu summary có rủi ro gì?
3. ReAct giải quyết vấn đề gì?
4. Khi nào LangChain/DSPy/Haystack đáng dùng thay vì tự viết code?

## Gợi ý trả lời câu hỏi review

1. Chain là pipeline các bước đã định nghĩa trước, phù hợp workflow rõ ràng. Agent dùng LLM để quyết định hành động tiếp theo và có thể chọn tool động, linh hoạt hơn nhưng khó kiểm soát hơn.
2. Summary memory có thể làm mất chi tiết, tóm tắt sai, bỏ qua thông tin hiếm nhưng quan trọng, hoặc tích lũy lỗi qua nhiều vòng hội thoại.
3. ReAct giải quyết nhu cầu vừa suy luận vừa hành động: model nghĩ bước tiếp theo, gọi tool/search/calculator, quan sát kết quả rồi tiếp tục. Nó giúp LLM xử lý task nhiều bước cần thông tin ngoài model.
4. Các framework đáng dùng khi app cần nhiều component lặp lại như prompt templates, chains, retrieval, tool calling, memory, evaluation hoặc orchestration. Nếu workflow rất nhỏ và ổn định, tự viết code thường dễ kiểm soát hơn.

## Liên kết

- [[Prompt Engineering]]
- [[LLM Agent]]
- [[Generative Model]]
