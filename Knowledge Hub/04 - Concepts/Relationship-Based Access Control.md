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

# Relationship-Based Access Control

## Định nghĩa

[[Relationship-Based Access Control]] là authorization model quyết định quyền dựa trên quan hệ giữa subject và object, ví dụ owner, editor, viewer, member-of, parent-folder hoặc group membership.

## Cách hiểu bằng lời của tôi

ReBAC phù hợp với sản phẩm có object graph tự nhiên: document nằm trong folder, video nằm trong channel, user thuộc group, group nằm trong org. Thay vì copy quyền xuống mọi object con, ta định nghĩa quan hệ và rule kế thừa quyền.

## Cơ chế

- Lưu quyền dưới dạng [[Permission Tuple]].
- Namespace định nghĩa object type và relation hợp lệ.
- Rules/userset rewrite mô tả relation nào suy ra relation nào.
- Check quyền có thể traverse graph quan hệ hoặc dùng index denormalized cho group lớn.

## Trade-off

- Diễn đạt tốt permission inheritance và sharing.
- Check quyền có thể thành graph traversal sâu nếu group lồng nhau.
- Caching giúp rất nhiều nhưng phải gắn với consistency guarantee.
- Quyền bị revoke cần xử lý freshness để tránh "new enemy" problem.

## Liên kết

- [[Google Zanzibar]]
- [[Permission Tuple]]
- [[Authorization Consistency Token]]
- [[Fine-Grained Authorization]]
- [[Property Graph]]
