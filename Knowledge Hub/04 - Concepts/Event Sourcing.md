---
type: concept
status: understood
sources:
  - "[[2026-03-19_event-sourcing-explained-benefits-and-use-cases]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - system-design
  - event-driven
  - database
---

# Event Sourcing

## Định nghĩa

Event Sourcing là mẫu kiến trúc trong đó mọi thay đổi trạng thái của ứng dụng được ghi nhận dưới dạng một chuỗi các sự kiện không thể thay đổi (immutable events) lưu trong Event Store append-only. Trạng thái hiện tại của hệ thống được tính toán bằng cách replay lại các sự kiện này.

## Cách hiểu bằng lời của tôi

Thay vì chỉ lưu trạng thái kết quả (chẳng hạn `balance = 100` trong DB quan hệ), Event Sourcing lưu lại toàn bộ nhật ký giao dịch: `Deposited 50`, `Deposited 80`, `Withdrew 30`. Trạng thái hiện tại chỉ là hệ quả của lịch sử sự kiện. Điều này giúp có được Audit Log tự nhiên và khả năng khôi phục lại trạng thái ở bất kỳ thời điểm nào trong quá khứ (Time Travel).

## Cơ chế

```text
Command (User Intent)
-> Domain Validation
-> Generate Event (e.g., OrderPlaced)
-> Append to Event Store (Immutable Log)
-> Publish Event to Message Broker
-> Update Read Models (CQRS Projection)
```

- **Event Store**: Cơ sở dữ liệu append-only tối ưu hóa cho ghi chép nhanh và đọc theo sequence.
- **Snapshotting**: Để tránh phải replay hàng triệu sự kiện mỗi khi đọc trạng thái, hệ thống định kỳ lưu lại snapshot trạng thái tại mốc thời điểm $T$. Khi cần rebuild state, chỉ cần load snapshot tại $T$ và replay các event từ $T$ đến hiện tại.
- **CQRS Integration**: Event Sourcing thường đi kèm [[CQRS]] (Command Query Responsibility Segregation) để tách biệt luồng ghi sự kiện và luồng truy vấn read model.

## Trade-off

- **Auditability & Traceability**: Lịch sử tuyệt đối không thể sửa xóa, hỗ trợ tuân thủ pháp lý và forensic analysis.
- **Complexity**: Độ phức tạp cao trong việc xử lý schema evolution (khi cấu trúc event thay đổi theo thời gian).
- **Eventual Consistency**: Trạng thái ở read side có thể có độ trễ ngắn so với event log vừa ghi.
- **Storage Growth**: Dung lượng lưu trữ tăng liên tục theo thời gian vì không xóa dữ liệu cũ.

## Liên kết

- [[Transactional Outbox]]
- [[CQRS]]
- [[Change Data Capture]]
- [[Message Broker]]
- [[Distributed Data Consistency Patterns]]
