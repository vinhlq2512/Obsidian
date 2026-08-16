---
type: concept
status: developing
sources:
  - "[[2026-05-21_a-guide-to-async-patterns-in-api-design]]"
  - "[[2025-03-13_api-protocols-101-a-guide-to-choose-the-right-one]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - api
  - integration
---

# Webhook

## Định nghĩa

Webhook là pattern event-driven trong đó provider gửi HTTP POST tới URL mà consumer đã đăng ký khi một event xảy ra.

## Cách hiểu bằng lời của tôi

Webhook đảo chiều polling: consumer không hỏi mãi "có gì mới chưa", provider chủ động gọi consumer. Nhưng receiver lúc này cũng là một server production, phải chịu trách nhiệm bảo mật, retry, idempotency và replay.

## Checklist production

- Verify signature để biết event đến từ provider thật.
- Dùng HTTPS.
- Xử lý duplicate delivery bằng [[Idempotency Key]] hoặc event id.
- Retry với backoff và có replay archive.
- Rate limit hoặc allowlist nếu endpoint public.

## Liên kết

- [[Async API Pattern]]
- [[API Security]]
- [[Retry Pattern]]
- [[Idempotency Key]]
- [[API Protocol]]
