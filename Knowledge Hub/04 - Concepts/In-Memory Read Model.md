---
type: concept
status: seed
sources:
  - "[[2025-09-09_how-netflix-tudum-supports-20-million-users-with-cqrs]]"
source_sections:
  - "[[2025-09-09_how-netflix-tudum-supports-20-million-users-with-cqrs]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - system-design
  - database
---

# In-Memory Read Model

## Định nghĩa

[[In-Memory Read Model]] là read model được load trực tiếp vào memory của service instance để phục vụ query local, thay vì mỗi request phải gọi network tới datastore hoặc cache ngoài.

## Cách hiểu bằng lời của tôi

Nếu read dataset đủ nhỏ và update không quá liên tục, ta có thể đổi bài toán từ "mỗi request đi hỏi store nào đó" thành "mỗi instance giữ bản sao đọc được". Lợi ích là giảm hop, giảm cache invalidation phức tạp, và preview/read path nhanh hơn.

## Điều kiện phù hợp

- Dataset nhỏ đến vừa, có thể nén và giữ trong RAM của mỗi instance.
- Read nhiều hơn write.
- Query cần latency rất thấp.
- Có cơ chế phân phối snapshot/delta để các instance bắt kịp phiên bản mới.
- Một số flow cần [[Read-Your-Writes Consistency]] có thể opt in theo request.

## Trade-off

- Tốn RAM trên mỗi instance.
- Cần cơ chế sync/version để tránh stale quá lâu.
- Không phù hợp với dataset quá lớn hoặc thay đổi liên tục từng request.
- Đổi complexity từ per-request I/O sang lifecycle của snapshot, propagation và consistency.

## Liên kết

- [[CQRS]]
- [[Read Path]]
- [[Materialized View]]
- [[Specialized Read Store]]
- [[Staleness]]
- [[Read-Your-Writes Consistency]]
