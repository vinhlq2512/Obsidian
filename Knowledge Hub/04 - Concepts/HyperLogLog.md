---
type: concept
status: understood
sources:
  - "[[2023-10-12_the-6-most-impactful-ways-redis-is-used-in-production-system]]"
  - "[[2023-09-21_a-crash-course-in-redis]]"
source_sections:
  - "[[2023-10-12_the-6-most-impactful-ways-redis-is-used-in-production-system]]"
  - "[[2023-09-21_a-crash-course-in-redis]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - data-structures
  - analytics
  - redis
---

# HyperLogLog

## Định nghĩa

HyperLogLog là probabilistic data structure dùng để ước lượng số lượng phần tử duy nhất với memory gần như cố định.

## Cách hiểu bằng lời của tôi

Nếu chỉ cần biết có khoảng bao nhiêu unique visitor, không nhất thiết phải giữ toàn bộ user ID trong HashSet. [[HyperLogLog]] hy sinh một ít độ chính xác để tránh memory tăng tuyến tính theo số user.

## Khi dùng

- Đếm unique visitor, unique device, unique user trên web scale.
- Metric cần ước lượng đủ tốt hơn là exact count.
- Hệ thống muốn giữ memory footprint ổn định dù cardinality rất lớn.

## Trade-off

- Dùng ít memory và scale tốt.
- Không trả lời được "ai là các phần tử cụ thể".
- Có sai số, nên không phù hợp cho ledger, billing hoặc logic cần exactness.

## Liên kết

- [[Redis]]
- [[Metrics]]
- approximate counting
- [[Redis Data Structures]]
