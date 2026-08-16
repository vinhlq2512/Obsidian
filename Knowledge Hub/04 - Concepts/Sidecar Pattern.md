---
type: concept
status: understood
sources:
  - "[[2026-05-07_container-design-patterns-for-distributed-systems]]"
source_sections:
  - "[[2026-05-07_container-design-patterns-for-distributed-systems]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - containers
  - design-pattern
---

# Sidecar Pattern

## Định nghĩa

Sidecar Pattern là pattern đặt helper container cạnh main container để xử lý cross-cutting concern như log shipping, config sync hoặc proxy logic.

## Cách hiểu bằng lời của tôi

Sidecar giúp app chính đơn giản hơn bằng cách tách phần phụ trợ có thể tái sử dụng. Main app và sidecar thường share volume hoặc localhost trong cùng [[Kubernetes Pod]], nhưng vẫn có contract tích hợp về path, port, format và lifecycle.

## Khi dùng

- Cross-cutting concern giống nhau trên nhiều app.
- Helper có owner/release cadence riêng.
- Muốn reuse logic mà không nhúng library theo từng ngôn ngữ.

## Liên kết

- [[Service Mesh]]
- [[Observability]]
- [[Container Adapter Pattern]]
- [[Ambassador Pattern]]
