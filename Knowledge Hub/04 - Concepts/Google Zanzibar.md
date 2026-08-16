---
type: concept
status: seed
sources:
  - "[[2026-01-27_how-google-manages-trillions-of-authorizations-with-zanzibar]]"
source_sections:
  - "[[2026-01-27_how-google-manages-trillions-of-authorizations-with-zanzibar]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - security
  - distributed-systems
---

# Google Zanzibar

## Định nghĩa

[[Google Zanzibar]] là distributed authorization infrastructure của Google, dùng relation tuple, namespace policy và consistency token để trả lời permission checks ở quy mô rất lớn.

## Cách hiểu bằng lời của tôi

Zanzibar là ví dụ kinh điển cho bài toán: authorization vừa phải nhanh, vừa phải đúng, vừa phải global. Nó không nhúng logic quyền vào từng service; nó cho service mô hình hóa quan hệ, lưu tuple, rồi gọi một hệ authorization chung để check quyền với freshness phù hợp.

## Thành phần đáng nhớ

- [[Permission Tuple]]: dữ liệu quan hệ `object, relation, user`.
- Namespace/config: định nghĩa relation và rule kế thừa.
- Userset rewrite: union/intersection/exclusion để suy ra quyền.
- [[Authorization Consistency Token]]: token timestamp giúp check không dùng dữ liệu quá cũ.
- Cache + request dedup: giảm hotspot khi nhiều check giống nhau.
- Denormalized group index: tăng tốc membership cho group lồng sâu.

## Trade-off

- Stale reads nhanh cho common case; fresh reads đắt hơn vì cần coordination xa hơn.
- Write chậm hơn read vì phải giữ consistency.
- Shared auth service cần quota/isolation để client nóng không làm ảnh hưởng client khác.

## Liên kết

- [[Relationship-Based Access Control]]
- [[Fine-Grained Authorization]]
- [[Data Replication]]
- [[Strict Serializability]]
- [[Consistent Hashing]]
- [[Blast Radius]]
