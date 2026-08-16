---
type: synthesis
status: seed
concepts:
  - "[[Distributed Counter]]"
  - "[[Rollup Pipeline]]"
  - "[[Event Log]]"
  - "[[Time-Series Data Storage]]"
  - "[[Data Lifecycle Management]]"
  - "[[Unified Domain Model]]"
  - "[[Real-Time Graph Architecture]]"
  - "[[Key-Value Graph Storage]]"
sources:
  - "[[2025-02-11_how-netflix-built-a-distributed-counter-for-billions-of-user]]"
  - "[[2025-03-18_how-netflix-stores-140-million-hours-of-viewing-data-per-day]]"
  - "[[2025-07-02_netflix-ended-data-chaos-with-unified-domain-models]]"
  - "[[2026-01-21_how-netflix-built-a-real-time-distributed-graph-for-internet]]"
questions: []
created_at: 2026-08-16
updated_at: 2026-08-16
tags:
  - synthesis
  - system-design
  - data-platform
  - bytebytego
---

# Netflix Data Platform Patterns

## Ý chính

Cụm source Netflix data platform cho thấy cùng một nguyên tắc lặp lại: dữ liệu ở scale lớn cần được tách theo access pattern, lifecycle, semantics và operational ownership. Một storage hoặc một schema chung không đủ khi workload gồm counter realtime, viewing history, domain model và graph quan hệ.

## Pattern chung

```text
high-volume events
-> durable/replayable log
-> stream processor hoặc rollup worker
-> read model/aggregate/graph storage
-> cache hoặc namespace riêng cho đường đọc nóng
-> lifecycle policy để kiểm soát storage growth
```

## Bài học theo cụm

- Counter: raw event giúp chính xác và idempotent, nhưng read cần rollup/cache để không scan event liên tục.
- Viewing history: dữ liệu gần đây và dữ liệu cũ nên nằm ở storage shape khác nhau, kèm rotation và compression.
- Unified domain model: scale tổ chức cũng là scale kỹ thuật; schema drift có thể phá hệ thống từ tầng semantics.
- Realtime graph: graph database chuyên dụng không luôn là lựa chọn đúng; nếu access pattern rõ, key-value storage có thể phục vụ graph traversal ở scale rất lớn.

## Trade-off lớn

- Tách theo namespace/cluster/type/age tăng operational complexity nhưng tạo isolation và khả năng tune riêng.
- Event log tăng audit/replay nhưng cần aggregate để đọc nhanh.
- Cache và read model làm latency thấp hơn nhưng phải ghi rõ freshness/consistency.
- Domain model trung tâm giảm integration debt nhưng cần governance và tooling để không trở thành bottleneck.

## Liên kết

- [[Distributed Counter]]
- [[Rollup Pipeline]]
- [[Event Log]]
- [[Time-Series Data Storage]]
- [[Data Lifecycle Management]]
- [[Unified Domain Model]]
- [[Real-Time Graph Architecture]]
- [[Property Graph]]
- [[Key-Value Graph Storage]]
