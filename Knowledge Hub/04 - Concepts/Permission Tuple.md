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
  - authorization
---

# Permission Tuple

## Định nghĩa

[[Permission Tuple]] là record biểu diễn một quan hệ authorization theo dạng `object, relation, user`, ví dụ `document:123, viewer, alice`.

## Cách hiểu bằng lời của tôi

Tuple là nguyên tử dữ liệu của ReBAC. Thay vì lưu một bảng quyền lớn theo role, hệ thống lưu các quan hệ nhỏ rồi dùng rule để suy ra quyền phức tạp: editor cũng là viewer, viewer của folder có thể xem document trong folder, group member kế thừa quyền của group.

## Vì sao hữu ích

- Dễ mô hình hóa sharing và inheritance.
- Một abstraction dùng được cho nhiều product/object type.
- Policy thay đổi qua namespace/rule mà không phải migrate toàn bộ dữ liệu.
- Có thể index/cache theo object, relation hoặc user tùy workload.

## Liên kết

- [[Relationship-Based Access Control]]
- [[Google Zanzibar]]
- [[Authorization]]
- [[Property Graph]]
