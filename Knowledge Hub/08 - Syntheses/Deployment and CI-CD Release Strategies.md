---
type: synthesis
status: seed
concepts:
  - "[[Continuous Integration]]"
  - "[[Continuous Delivery]]"
  - "[[Continuous Deployment]]"
  - "[[Deployment Pipeline]]"
  - "[[Big-Bang Deployment]]"
  - "[[Rolling Deployment]]"
  - "[[Blue-Green Deployment]]"
  - "[[Canary Deployment]]"
  - "[[Feature Flag]]"
  - "[[Dark Launch]]"
  - "[[Shadow Traffic]]"
  - "[[Expand-Contract Migration]]"
  - "[[Rollback Alarm]]"
  - "[[Bake Period]]"
sources:
  - "[[2024-04-04_a-crash-course-in-cicd]]"
  - "[[2026-06-11_must-know-deployment-strategies-from-big-bang-to-progressive]]"
questions: []
created_at: 2026-08-16
updated_at: 2026-08-16
tags:
  - synthesis
  - devops
  - deployment
  - system-design
---

# Deployment and CI-CD Release Strategies

## Mental model

CI/CD không chỉ là automation. Nó là hệ thống giảm rủi ro khi code đi từ máy developer tới production. CI giảm rủi ro integration; delivery/deployment giảm rủi ro release; deployment strategies giảm blast radius; observability và rollback quyết định team có phát hiện lỗi đủ sớm không.

## Các lớp quyết định

| Câu hỏi | Concept | Ghi nhớ |
| --- | --- | --- |
| Code có tích hợp được không? | [[Continuous Integration]] | Merge nhỏ, build/test tự động, feedback nhanh |
| Artifact đã sẵn sàng release chưa? | [[Continuous Delivery]], [[Deployment Pipeline]] | Code luôn ở trạng thái deployable |
| Có tự động lên production không? | [[Continuous Deployment]] | Cần test, metric và rollback đủ trưởng thành |
| Rollout giảm blast radius thế nào? | [[Rolling Deployment]], [[Blue-Green Deployment]], [[Canary Deployment]] | Mỗi strategy đổi safety lấy cost/cognitive load |
| Deploy và release có tách được không? | [[Feature Flag]], [[Dark Launch]], [[Shadow Traffic]] | Chạy code không nhất thiết đồng nghĩa user thấy feature |
| Schema có rollback-safe không? | [[Expand-Contract Migration]] | Schema change cần nhiều bước tương thích ngược |
| Dừng rollout bằng gì? | [[Rollback Alarm]], [[Bake Period]] | Define health trước khi rollout, không thương lượng khi incident |

## Bài học

- Big-bang đơn giản nhưng blast radius lớn.
- Rolling không downtime nhưng tạo mixed-version state.
- Blue-green mua rollback nhanh bằng chi phí hạ tầng.
- Canary cần per-version observability; thiếu nó thì strategy yếu đi nhiều.
- Feature flag hữu ích nhưng phải có owner và cleanup để tránh flag debt.
- Expand-contract là nền tảng cho schema change an toàn trong rollout dần.

## Liên kết

- [[Reliability Operations Loop]]
- [[Observability for Distributed Systems]]
- [[Resilience Failure Control Patterns]]
- [[Zero-Downtime Infrastructure Migration]]
