---
type: concept
status: seed
sources:
  - "[[2026-03-31_how-meta-turned-debugging-into-a-product]]"
source_sections:
  - "[[2026-03-31_how-meta-turned-debugging-into-a-product]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - reliability
  - debugging
---

# Analyzer Chaining

## Định nghĩa

[[Analyzer Chaining]] là pattern cho phép một analyzer điều tra triệu chứng ở service này gọi analyzer của service/dependency khác và truyền context đã thu thập được.

## Cách hiểu bằng lời của tôi

Trong microservices, service báo lỗi thường không phải service gây lỗi. Analyzer chaining biến "ping team khác trong chat" thành call có cấu trúc giữa các domain analyzer, giúp root cause đi qua dependency graph nhanh hơn.

## Cơ chế

```text
API analyzer phát hiện lỗi theo region
-> correlate với latency/deploy/config
-> gọi storage analyzer kèm region + timestamp
-> storage analyzer xác nhận thay đổi gây timeout
-> trả finding về alert
```

## Liên kết

- [[Debugging as Code]]
- [[Automated Root Cause Analysis]]
- [[Microservices Architecture]]
- [[Distributed Tracing]]
- [[Dependency Graph]]
