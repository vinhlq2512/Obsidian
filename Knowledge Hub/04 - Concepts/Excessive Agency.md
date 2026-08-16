---
type: concept
status: developing
sources:
  - "[[2026-08-03_llm-security-basics-the-full-threat-model]]"
  - "[[2026-05-04_connecting-llms-to-the-real-world-tool-use-function-calling]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - llm
  - security
  - agent
---

# Excessive Agency

## Định nghĩa

Excessive agency là tình trạng LLM agent có quyền truy cập hoặc quyền hành động rộng hơn mức cần cho task, khiến lỗi prompt/context có thể biến thành thiệt hại thật.

## Cách hiểu bằng lời của tôi

LLM có thể sai mà chưa nguy hiểm nếu nó chỉ trả lời text. Nó trở nên nguy hiểm hơn khi vừa đọc dữ liệu riêng tư, vừa đọc nội dung không tin cậy, vừa có tool để gửi dữ liệu hoặc thực hiện hành động ra ngoài.

## Lethal trifecta

Ba yếu tố cùng xuất hiện làm rủi ro tăng mạnh:

- access to private data;
- exposure to untrusted content;
- outbound channel hoặc external action.

Loại bỏ một trong ba yếu tố thường giảm đáng kể blast radius.

Xem [[Lethal Trifecta]] và [[Agents Rule of Two]] để biến quan sát này thành rule thiết kế cụ thể.

## Giảm rủi ro

- Least privilege cho từng tool.
- Tách tool đọc dữ liệu khỏi tool ghi/gửi dữ liệu.
- Require approval cho action không thể rollback.
- Log tool trajectory để audit.
- Không expose toàn bộ MCP server nếu task chỉ cần một subset nhỏ.

## Liên kết

- [[LLM Security]]
- [[Prompt Injection]]
- [[Indirect Prompt Injection]]
- [[Lethal Trifecta]]
- [[Agents Rule of Two]]
- [[LLM Agent]]
- [[Tool Use]]
- [[Model Context Protocol]]
