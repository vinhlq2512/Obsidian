---
type: concept
status: developing
sources:
  - "[[2025-04-03_the-art-of-rest-api-design-idempotency-pagination-and-securi]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - api
  - database
  - system-design
---

# API Pagination

## Định nghĩa

API pagination là kỹ thuật chia kết quả danh sách thành nhiều page nhỏ để tránh payload lớn, full scan, query chậm và trải nghiệm không ổn định.

## Cách hiểu bằng lời của tôi

Endpoint list nguy hiểm hơn nhìn bề ngoài. Nếu trả mọi record, nó kéo database, network và client xuống cùng lúc. Pagination đặt giới hạn rõ cho mỗi request và cho client cách đi tiếp.

## Offset-based pagination

```text
GET /orders?limit=20&offset=40
```

- Dễ hiểu, dễ làm với SQL `LIMIT/OFFSET`.
- Phù hợp dashboard/admin page hoặc list tương đối ổn định.
- Kém với dataset lớn vì offset sâu phải skip nhiều row.
- Dễ duplicate/missing item nếu dữ liệu thay đổi giữa các page.

## Cursor-based pagination

```text
GET /orders?limit=20&after=cursor
```

- Dùng `created_at`, `id` hoặc cursor opaque để lấy page sau record cuối.
- Ổn định hơn khi có insert/delete.
- Phù hợp feed, event log, mobile infinite scroll, sync.
- Cần sort key ổn định và cách encode/decode cursor rõ.

## Liên kết

- [[REST API]]
- [[Database Indexing]]
- [[API Contract]]
- [[Idempotency Key]]
