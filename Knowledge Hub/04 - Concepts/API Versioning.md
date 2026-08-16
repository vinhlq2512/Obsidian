---
type: concept
status: developing
sources:
  - "[[2024-04-18_a-crash-course-in-api-versioning-strategies]]"
  - "[[2025-04-03_the-art-of-rest-api-design-idempotency-pagination-and-securi]]"
  - "[[2025-10-23_api-gateways-101-the-core-of-modern-api-management-security]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - api
  - system-design
---

# API Versioning

## Định nghĩa

API versioning là cách cho API thay đổi theo thời gian mà không phá client hiện tại, bằng cách cho client chọn version hoặc opt-in vào thay đổi.

## Cách hiểu bằng lời của tôi

API là contract dài hạn. Khi client đã tích hợp, ta không thể đổi shape payload, bỏ field hoặc siết validation một cách bất ngờ. Versioning là cơ chế quản lý thay đổi có lịch trình thay vì đẩy rủi ro sang client.

## Khi cần version mới

- Breaking change: bỏ field, đổi nghĩa field, thêm required parameter, đổi response shape.
- New feature không thể triển khai backward-compatible.
- Bug fix hoặc performance change làm client phải đổi cách dùng.
- Quy định/security yêu cầu thay đổi behavior.

## Chiến lược

- Additive change: chỉ thêm field/option backward-compatible, không phá client cũ.
- Explicit versioning: phát hành version mới khi cần thay đổi không tương thích.
- URI versioning dễ debug nhưng làm URL gắn với version.
- Header/media-type versioning giữ URI sạch nhưng khó inspect/cache hơn.
- Query parameter versioning dễ thử nhưng có thể đẩy logic version vào một endpoint phức tạp.

## Deprecation

- Duy trì càng ít version càng tốt.
- Thông báo sunset/deprecation rõ ràng, thường cần giai đoạn chuyển đổi.
- Version cũ vẫn cần security patch cho tới khi hết hỗ trợ.
- Gateway có thể route nhiều version song song và hỗ trợ lifecycle: deprecate, sunset, migration path.

## Liên kết

- [[REST API]]
- [[API Contract]]
- [[Backward Compatibility]]
- [[API Gateway]]
- [[API Lifecycle Management]]
