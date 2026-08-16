---
type: concept
status: seed
sources:
  - "[[2026-04-09_must-know-cross-cutting-concerns-in-api-development]]"
  - "[[2025-10-11_ep184-api-vs-sdk]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - security
  - api
---

# SQL Injection

## Định nghĩa

SQL injection là vulnerability trong đó attacker đưa input độc hại vào query để làm database thực thi logic ngoài ý định.

## Cách hiểu bằng lời của tôi

Lỗi nằm ở việc để string input trở thành một phần của câu lệnh SQL. Khi input không còn là dữ liệu thuần mà biến thành code/query fragment, attacker có thể đọc, sửa hoặc suy luận dữ liệu.

## Cách phòng

- Dùng prepared statements hoặc parameterized queries.
- Không nối chuỗi SQL từ input thô.
- Validate input bằng schema/allowlist.
- Giới hạn quyền database account theo least privilege.
- Không trả lỗi database chi tiết ra client.

## Liên kết

- [[Input Validation]]
- [[API Security]]
- [[Database Schema Design]]
