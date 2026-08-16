---
type: concept
status: understood
sources:
  - "[[2026-03-03_how-agoda-built-a-single-source-of-truth-for-financial-data]]"
  - "[[2025-01-05_modernizing-legacy-systems-without-breaking-production]]"
  - "[[2025-05-04_pinterest-migrated-3-7m-lines-to-typescript-heres-how-they-p]]"
source_sections:
  - "[[2026-03-03_how-agoda-built-a-single-source-of-truth-for-financial-data]]"
  - "[[2025-01-05_modernizing-legacy-systems-without-breaking-production]]"
  - "[[2025-05-04_pinterest-migrated-3-7m-lines-to-typescript-heres-how-they-p]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - testing
  - data-engineering
  - system-design
---

# Shadow Testing

## Định nghĩa

Shadow Testing là kỹ thuật chạy phiên bản mới song song với phiên bản cũ trên cùng dữ liệu thật hoặc traffic thật, rồi so sánh output trước khi release.

## Cách hiểu bằng lời của tôi

Với pipeline tài chính, test unit không đủ. Shadow testing cho reviewer thấy thay đổi mới làm lệch số liệu ra sao trên dữ liệu production-like, giúp bắt side effect trước khi ảnh hưởng báo cáo thật.

## Cơ chế

- Chạy old pipeline và new pipeline trên cùng input.
- So sánh output theo bảng, partition, metric hoặc field quan trọng.
- Đưa diff summary vào code review để người review hiểu impact của thay đổi.
- Với code/service migration, mirror production traffic sang hệ mới và so response, latency, error rate hoặc output artifact trước cutover.

## Liên kết

- [[Financial Source of Truth]]
- [[Data Contract]]
- [[Phased Rollout]]
- [[Rollback Strategy]]
- [[Traffic Replay]]
- [[Behavioral Compatibility]]
