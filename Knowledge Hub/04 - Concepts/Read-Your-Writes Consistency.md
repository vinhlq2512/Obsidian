---
type: concept
status: seed
sources:
  - "[[2025-02-27_mastering-data-consistency-across-microservices]]"
  - "[[2026-08-06_the-read-path-versus-the-write-path-strategies-and-technique]]"
  - "[[2025-09-09_how-netflix-tudum-supports-20-million-users-with-cqrs]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - consistency
  - distributed-systems
---

# Read-Your-Writes Consistency

## Định nghĩa

Read-your-writes consistency là guarantee rằng user/client vừa ghi dữ liệu sẽ thấy chính update của mình trong các read sau đó.

## Cách hiểu bằng lời của tôi

Không nhất thiết mọi người đều thấy update ngay. Nhưng người vừa sửa profile, thêm item vào cart hoặc đổi setting cần thấy kết quả của chính mình, nếu không họ sẽ nghĩ thao tác bị mất.

## Cách triển khai thường gặp

- Route read sau write về primary trong một khoảng ngắn.
- Gắn version token vào client và chỉ đọc từ replica đã catch up tới version đó.
- Hiển thị trạng thái pending nếu read model bất đồng bộ chưa bắt kịp.
- Cho phép một số request quan trọng opt in consistency mạnh hơn, ví dụ preview editor sau khi save.

## Liên kết

- [[Eventual Consistency]]
- [[Staleness]]
- [[Read Replica]]
- [[CQRS]]
- [[In-Memory Read Model]]
