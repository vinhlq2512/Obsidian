---
type: concept
status: seed
sources:
  - "[[2026-08-03_llm-security-basics-the-full-threat-model]]"
source_sections:
  - "[[2026-08-03_llm-security-basics-the-full-threat-model]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - llm
  - security
---

# Untrusted Model Output

## Định nghĩa

[[Untrusted Model Output]] là nguyên tắc coi mọi response của model là dữ liệu chưa tin cậy trước khi đưa vào UI, database, command, API hoặc hệ downstream.

## Cách hiểu bằng lời của tôi

LLM output có thể bị prompt injection, hallucination hoặc poisoning tác động. Nếu output được render, execute hoặc gửi tiếp mà không sanitize/validate, lỗi text có thể trở thành lỗi bảo mật hoặc lỗi dữ liệu.

## Khi cần kiểm soát

- Render HTML/Markdown từ model.
- Dùng model output để gọi API hoặc shell command.
- Ghi dữ liệu model sinh ra vào database.
- Gửi email/message/action từ nội dung model.

## Liên kết

- [[LLM Security]]
- [[Safe Outputs Pipeline]]
- [[Input Validation]]
- [[Prompt Injection]]
- [[AI Hallucination]]
