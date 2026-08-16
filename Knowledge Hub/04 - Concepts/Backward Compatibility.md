---
type: concept
status: seed
sources:
  - "[[2024-04-18_a-crash-course-in-api-versioning-strategies]]"
  - "[[2025-04-03_the-art-of-rest-api-design-idempotency-pagination-and-securi]]"
first_seen: 2026-08-16
last_updated: 2026-08-16
tags:
  - concept
  - api
  - system-design
---

# Backward Compatibility

## Định nghĩa

Backward compatibility là khả năng thay đổi hệ thống mà client cũ vẫn tiếp tục hoạt động theo contract trước đó.

## Cách hiểu bằng lời của tôi

Nếu client đã tích hợp API hôm nay, thay đổi ngày mai không nên bắt họ sửa code ngay lập tức. Backward compatibility là kỷ luật giữ lời hứa cũ trong khi vẫn mở đường cho hành vi mới.

## Trong API

- Thêm optional field thường an toàn hơn đổi hoặc xóa field.
- Không thêm required parameter vào endpoint đang dùng.
- Không đổi nghĩa field hoặc response shape mà không version.
- Nếu cần breaking change, dùng [[API Versioning]] và deprecation rõ ràng.

## Liên kết

- [[API Versioning]]
- [[API Contract]]
- [[REST API]]
