---
type: synthesis
status: seed
concepts:
  - "[[GraphQL Federation]]"
  - "[[Java Virtual Threads]]"
  - "[[Generational Garbage Collection]]"
  - "[[Runtime Platform Migration]]"
  - "[[GraphQL]]"
  - "[[gRPC]]"
sources:
  - "[[2025-06-03_how-netflix-runs-on-java]]"
created_at: 2026-08-16
updated_at: 2026-08-16
tags:
  - synthesis
  - java
  - system-design
  - bytebytego
---

# Netflix Java Runtime Architecture

## Ý chính

Nguồn Netflix Java cho thấy platform backend không chỉ là chọn ngôn ngữ. Hiệu năng và reliability đến từ cách schema ownership, service fan-out, framework chuẩn, JVM runtime và migration tooling được thiết kế cùng nhau.

## Bản đồ luồng

```text
client
-> GraphQL gateway
-> federated Domain Graph Services
-> gRPC/service calls hoặc datastore
-> resolver response

platform migration
-> Spring Boot baseline
-> JDK mới
-> virtual threads cho blocking fan-out
-> generational GC để giảm latency spike
```

## Bài học

- Federated schema giúp nhiều team sở hữu domain độc lập, nhưng query fan-out cần timeout/fallback rất chặt.
- Virtual threads giảm complexity của reactive plumbing trong request/response backend, nhưng phải hiểu failure mode như thread pinning.
- GC pause là vấn đề reliability, không chỉ performance tuning.
- Runtime migration ở scale lớn cần automated tooling và compatibility layer; nếu không, framework cũ khóa cả tổ chức ở runtime cũ.

## Liên kết

- [[GraphQL Federation]]
- [[Java Virtual Threads]]
- [[Generational Garbage Collection]]
- [[Runtime Platform Migration]]
- [[Timeout]]
- [[Retry Storm]]
