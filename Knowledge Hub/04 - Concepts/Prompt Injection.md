---
type: concept
status: developing
sources:
  - "[[2026-08-03_llm-security-basics-the-full-threat-model]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - llm
  - security
---

# Prompt Injection

## Định nghĩa

Prompt injection là tấn công đưa instruction-like text vào context để làm model ưu tiên lệnh của attacker thay vì ý định của hệ thống hoặc người vận hành.

## Cách hiểu bằng lời của tôi

Trong SQL, parameterization tách code khỏi data. Với LLM, cả rule, câu hỏi, email, web page, file và tool output đều trở thành token trong cùng context. Nếu data có dạng "hãy bỏ qua chỉ dẫn trước", model vẫn có thể bị nó tác động.

## Hai đường vào

- Direct injection: attacker gõ lệnh độc hại trực tiếp vào chat/input.
- [[Indirect Prompt Injection]]: attacker giấu instruction trong nội dung mà hệ thống retrieve hoặc đọc hộ user, ví dụ email, issue, website, document.

## Cách giảm rủi ro

- Coi nội dung bên ngoài là untrusted data.
- Không cho dữ liệu retrieve trực tiếp kích hoạt tool nhạy cảm.
- Tách bước plan/action khỏi raw external content khi có thể.
- Giới hạn quyền tool và thêm human approval cho action hậu quả cao.

## Liên kết

- [[LLM Security]]
- [[Indirect Prompt Injection]]
- [[Context Engineering]]
- [[Tool Use]]
- [[Retrieval-Augmented Generation]]
- [[Excessive Agency]]
