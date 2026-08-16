---
type: concept
status: understood
sources:
  - "[[2026-06-25_top-anti-patterns-to-avoid-in-service-architecture]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - system-design
  - microservices
  - anti-pattern
---

# Service Architecture Anti-Patterns

## Định nghĩa

Service Architecture Anti-Patterns (Các chống mẫu trong kiến trúc dịch vụ) là những quyết định thiết kế hệ thống có vẻ hợp lý ban đầu nhưng mang lại hậu quả xấu về độ phức tạp, khả năng bảo trì, hiệu năng và tính tin cậy khi hệ thống mở rộng.

## Các Anti-Pattern phổ biến

```text
Anti-Pattern: Distributed Monolith
Client -> Service A -> Sync HTTP -> Service B -> Sync HTTP -> Service C -> Shared DB
(Tách service nhưng dính chặt phụ thuộc và dùng chung DB -> Mất ưu điểm cả Monolith lẫn Microservices)
```

1. **Distributed Monolith (Khối đơn phân tán)**: Tách ứng dụng thành nhiều microservice nhưng các service vẫn liên kết chặt chẽ qua synchronous HTTP call và chung database. Hậu quả: latency tăng gấp bội, deploy 1 service phải deploy lại tất cả.
2. **Nano-Services (Dịch vụ siêu nhỏ)**: Tách service quá nhỏ (ví dụ 1 function = 1 service), gây overhead lớn về network, service discovery và monitoring.
3. **Shared Database (Dùng chung cơ sở dữ liệu)**: Nhiều microservice cùng đọc/ghi trực tiếp vào một database chung, làm mất tính đóng gói (encapsulation) và ranh giới domain.
4. **Chatty Services (Dịch vụ nói nhiều)**: Hai service liên tục gọi REST API qua lại hàng trăm lần để hoàn thành một tác vụ thay vì gom batch hoặc dùng asynchronous event.
5. **Hardcoded Secrets & Endpoint Coupling**: Cấu hình địa chỉ IP hoặc secret trực tiếp trong mã nguồn thay vì qua Service Discovery và Secret Manager.

## Cách khắc phục

- Áp dụng Domain-Driven Design (DDD) để định nghĩa đúng Bounded Context trước khi tách service.
- Chuyển từ giao tiếp đồng bộ sang asynchronous event-driven với Message Broker.
- Đảm bảo mỗi service làm chủ hoàn toàn database riêng (Database-per-service pattern).

## Liên kết

- [[Microservices Design Patterns]]
- [[Container and Service Architecture Tradeoffs]]
- [[Cascading Failure]]
- [[API Design Patterns]]
