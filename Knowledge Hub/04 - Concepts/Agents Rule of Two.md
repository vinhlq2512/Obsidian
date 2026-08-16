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

# Agents Rule of Two

## Định nghĩa

[[Agents Rule of Two]] là guideline thiết kế agent: không để một agent tự trị cùng lúc có cả ba đặc tính rủi ro gồm xử lý untrusted input, truy cập sensitive data, và hành động/gửi dữ liệu ra ngoài.

## Cách hiểu bằng lời của tôi

Rule này biến [[Lethal Trifecta]] thành nguyên tắc dễ kiểm tra. Agent có thể có tối đa hai trong ba năng lực nguy hiểm; nếu task đòi cả ba, cần tách component hoặc đưa human vào loop.

## Liên kết

- [[LLM Security]]
- [[Lethal Trifecta]]
- [[Excessive Agency]]
- [[Least Privilege]]
- [[Safe Outputs Pipeline]]
