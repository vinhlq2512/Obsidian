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
  - agent
---

# Lethal Trifecta

## Định nghĩa

[[Lethal Trifecta]] là cấu hình rủi ro cao khi cùng một agent có ba thứ: dữ liệu riêng tư, nội dung không tin cậy, và kênh gửi dữ liệu hoặc hành động ra ngoài.

## Cách hiểu bằng lời của tôi

Một agent chỉ đọc private data thì rủi ro khác với agent vừa đọc private data, vừa đọc email/web không tin cậy, vừa có thể gửi request/message ra ngoài. Khi đủ ba điều kiện, prompt injection có đường biến thành exfiltration hoặc action thật.

## Cách giảm blast radius

- Bỏ outbound channel nếu task chỉ cần đọc.
- Scope private data theo [[Least Privilege]].
- Tách agent đọc untrusted content khỏi agent có quyền ghi/gửi.
- Thêm human review cho action hậu quả cao.

## Liên kết

- [[Excessive Agency]]
- [[Indirect Prompt Injection]]
- [[Agents Rule of Two]]
- [[Tool Use]]
- [[Model Context Protocol]]
