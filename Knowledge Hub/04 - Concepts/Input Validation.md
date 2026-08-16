---
type: concept
status: developing
sources:
  - "[[2026-03-26_how-to-implement-api-security]]"
  - "[[2025-04-03_the-art-of-rest-api-design-idempotency-pagination-and-securi]]"
  - "[[2026-04-09_must-know-cross-cutting-concerns-in-api-development]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - security
  - api
---

# Input Validation

## Định nghĩa

Input validation là kiểm tra dữ liệu API nhận vào theo type, length, format, range và schema trước khi hệ thống xử lý.

## Cách hiểu bằng lời của tôi

Không tin input chỉ vì caller đã đăng nhập. Client-side validation giúp UX, nhưng server-side validation mới là ranh giới bảo mật thật.

## Nguyên tắc

- Prefer allowlist: định nghĩa input hợp lệ và reject phần còn lại.
- Kiểm type, length, format, range, enum, unknown fields và payload size.
- Dùng schema để validation nhất quán giữa endpoint và test.
- Không để input thô đi thẳng vào query, command, URL fetch hoặc template.
- Validation là security boundary chống các lỗi như [[SQL Injection]] và [[Cross-Site Scripting]], không chỉ là kiểm tra form cho đẹp UX.

## Liên kết

- [[API Security]]
- [[API Contract]]
- [[REST API]]
- [[SQL Injection]]
- [[Cross-Site Scripting]]
- [[Cross-Site Request Forgery]]
- [[LLM Security]]
