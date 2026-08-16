---
type: synthesis
status: seed
concepts:
  - "[[Client State Synchronization]]"
  - "[[Streaming Compression]]"
  - "[[Delta Update]]"
  - "[[Passive Session]]"
  - "[[Notification Recommender Pipeline]]"
  - "[[Mobile App Modularization]]"
  - "[[Sandboxed Build Execution]]"
  - "[[Design-to-Code Context]]"
sources:
  - "[[2025-01-08_how-discord-reduced-websocket-traffic-by-40percent]]"
  - "[[2025-08-19_how-reddit-delivers-notifications-to-tens-of-millions-of-use]]"
  - "[[2025-11-12_how-tinder-decomposed-its-ios-monolith-app-handling-70m-user]]"
  - "[[2026-05-26_how-vercel-cut-build-wait-times-from-90-seconds-to-5]]"
  - "[[2026-04-14_figma-design-to-code-code-to-design-clearly-explained]]"
questions: []
created_at: 2026-08-16
updated_at: 2026-08-16
tags:
  - synthesis
  - frontend
  - mobile
  - system-design
---

# Client Experience and Frontend Platform Patterns

## Luận điểm chính

Client-scale system design nằm ở giao điểm của UX, bandwidth, build platform và recommendation. Một app mượt không chỉ cần backend nhanh; nó cần đồng bộ state tiết kiệm, notification biết im lặng, build graph ngắn, và tooling nối design-code không tạo drift.

## Pattern chính

- [[Client State Synchronization]] dùng snapshot, [[Delta Update]], event stream hoặc passive mode tùy freshness và mức user đang tương tác.
- [[Streaming Compression]] giảm payload nhỏ/lặp trên connection dài như [[WebSocket]], nhưng chỉ tốt khi workload thật sự có pattern tái dùng.
- [[Notification Recommender Pipeline]] phải có [[Notification Budgeting]] trước ranking để tránh notification fatigue.
- [[Mobile App Modularization]] và [[Critical Path Build Graph]] cho thấy build time là vấn đề architecture, không chỉ vấn đề máy build.
- [[Sandboxed Build Execution]] và [[Build Provisioning Warm Pool]] biến build platform thành sản phẩm multi-tenant an toàn và nhanh.
- [[Design-to-Code Context]], [[Code Connect]] và [[Component Mapping]] giúp coding agent dùng design system thật thay vì đoán từ screenshot hoặc raw JSON nhiễu.

## Mental model

```text
user-facing client
-> realtime sync và notification budget
-> recommendation/reranking cho interruption
-> modular build graph cho developer loop
-> sandboxed build platform cho deploy
-> design-code context để giữ UI implementation sát design system
```

## Trade-off cần nhớ

- Gửi ít dữ liệu thường thắng nén mạnh hơn.
- Notification tốt là biết không gửi.
- Modularization cần policy giữ thành quả, nếu không code mới lại chảy về monolith.
- Design-code roundtrip luôn lossy; mapping và context shaping chỉ giảm drift, không xóa hoàn toàn.

## Liên kết

- [[WebSocket]]
- [[Recommendation Funnel]]
- [[Developer Velocity]]
- [[Model Context Protocol]]
- [[Legacy Modernization and Code Migration Patterns]]
