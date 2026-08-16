---
type: concept
status: seed
sources:
  - "[[2026-01-29_how-to-scale-an-api]]"
source_sections:
  - "[[2026-01-29_how-to-scale-an-api]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - api
  - developer-experience
---

# API Documentation

## Định nghĩa

[[API Documentation]] là tài liệu mô tả endpoint, authentication, request/response schema, error handling, limits và ví dụ tích hợp để developer dùng API đúng.

## Cách hiểu bằng lời của tôi

API tốt mà không có docs tốt vẫn khó dùng. Documentation giảm support cost, giảm integration bug và giúp client hiểu contract, version, auth, pagination, rate limit, retry/error semantics.

## Nên có

- Endpoint, method, path params, query params.
- Request/response examples.
- Auth/OAuth/JWT/API key instructions.
- Error codes và retry guidance.
- Rate limit headers.
- Version/deprecation notes.

## Liên kết

- [[API Contract]]
- [[API Lifecycle Management]]
- [[API Versioning]]
- [[API Security]]
- [[Rate Limiting]]
