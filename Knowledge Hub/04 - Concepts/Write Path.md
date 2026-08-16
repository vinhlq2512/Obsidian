---
type: concept
status: developing
sources:
  - "[[2026-08-06_the-read-path-versus-the-write-path-strategies-and-technique]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - database
  - correctness
---

# Write Path

## Định nghĩa

Write path là đường xử lý ghi hoặc thay đổi fact trong hệ thống, như tạo order, đổi email, cập nhật balance hoặc xóa comment.

## Cách hiểu bằng lời của tôi

Write path muốn một nguồn sự thật rõ ràng, thứ tự update xác định, invariant được kiểm trước khi ack, và coordination khi nhiều node/copy cùng liên quan. Chính các yêu cầu này làm write path thường xung đột với read path tối ưu cho tốc độ.

## Chi phí thường bị đẩy vào write path

- Cập nhật nhiều [[Database Indexing|index]] gây [[Write Amplification]].
- Cập nhật denormalized fields để read nhanh hơn.
- Ghi event/outbox/CDC stream để nuôi read model.
- Fan-out dữ liệu tới timeline hoặc notification store.

## Liên kết

- [[Read Path]]
- [[Database Transaction]]
- [[ACID]]
- [[Write-Ahead Log]]
- [[Fan-Out on Write]]
